#!/usr/bin/env python3
"""Independent, standard-library arithmetic audit of the C first-jet arguments.

No producer arithmetic or saved certificate is imported.  The valuation proof
is in AUDIT.md; this reconstructs its finite constants from the integer f.
"""
from fractions import Fraction
from math import comb
import json
from pathlib import Path

P = 13
A, B = -4845, 62016


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def hasse(f, k):
    return {n-k: a*comb(n, k) for n, a in f.items() if n >= k}


def evaluate(f, x):
    return sum(a*x**n for n, a in f.items())


def base(d):
    return {20: 1, 16: A, 15: B, 3: d, 1: -1-A-B-d}


def jet(d, r, order):
    """Constant and (R,S,T) coefficients, v=r+13R,C=13S,D=d+13T."""
    f = base(d)
    k = hasse(f, order)
    c = evaluate(k, r)
    require(c % P == 0, "base equation is not divisible by 13")
    return [c//P % P,
            evaluate(hasse(k, 1), r) % P,
            evaluate(hasse({10: 1, 1: -1}, order), r) % P,
            evaluate(hasse({3: 1, 1: -1}, order), r) % P]


def solve(rows):
    mat = [[a % P for a in row[1:]] + [-row[0] % P] for row in rows]
    n = 3
    for j in range(n):
        pivot = next((i for i in range(j, n) if mat[i][j]), None)
        require(pivot is not None, "linear system is not full rank")
        mat[j], mat[pivot] = mat[pivot], mat[j]
        inv = pow(mat[j][j], -1, P)
        mat[j] = [a*inv % P for a in mat[j]]
        for i in range(n):
            if i != j:
                a = mat[i][j]
                mat[i] = [(x-a*y) % P for x, y in zip(mat[i], mat[j])]
    return [mat[i][-1] for i in range(n)]


def trim(a):
    a = [x % P for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    out = [0]*max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)


def scale(a, c):
    return trim([c*x for x in a])


def mul(a, b):
    if not a or not b:
        return []
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)


def divrem(a, b):
    a, b = trim(a), trim(b)
    require(bool(b), "zero polynomial divisor")
    q = [0]*max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        d = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, P) % P
        q[d] = c
        for j, x in enumerate(b): a[d+j] = (a[d+j]-c*x) % P
        a = trim(a)
    return trim(q), a


def egcd(a, b):
    oldr, r = trim(a), trim(b)
    olds, s, oldt, t = [1], [], [], [1]
    while r:
        q, newr = divrem(oldr, r)
        oldr, r = r, newr
        olds, s = s, add(olds, scale(mul(q, s), -1))
        oldt, t = t, add(oldt, scale(mul(q, t), -1))
    inv = pow(oldr[-1], -1, P)
    out = tuple(scale(v, inv) for v in (oldr, olds, oldt))
    require(add(mul(a, out[1]), mul(b, out[2])) == out[0], "Bezout replay failed")
    return out


def dense(f):
    a = [0]*(max(f)+1)
    for n, c in f.items(): a[n] = c % P
    return trim(a)


require(A == -comb(20, 16), "H16 normalization")
require(B == -comb(20, 15)-16*A, "H15 normalization")
require(Fraction(comb(16, 10)*A, comb(20, 10)) == -210, "G10 X6")
require(Fraction(comb(15, 10)*B, comb(20, 10)) == 1008, "G10 X5")
require(comb(20, 10) % 169 == 39, "G10 leading valuation")

# B(1+s)-B(1) = -15504s^2(10+10s+5s^2+s^3).
beta = [comb(20, 15)*(5*(1 if k == 1 else 0)-comb(5, k))
        for k in range(1, 6)]
require(beta == [0, -155040, -155040, -77520, -15504], "B expansion")
require(beta[1] % P != 0, "quadratic beta coefficient must be a unit")

rows3 = [jet(3, 2, 0), jet(3, 2, 3)]
rows10 = [jet(10, 11, 0), jet(10, 11, 3)]
require(rows3 == [[12, 9, 8, 6], [6, 4, 7, 1]], "c3 first jets")
require(rows10 == [[2, 0, 12, 7], [3, 4, 6, 1]], "c10 first jets")
for rows in [rows3, rows10]:
    require((rows[0][1]*rows[1][3]-rows[0][3]*rows[1][1]) % P == 11,
            "nonunit two-variable Jacobian")

extra = {
    "v2_w1": jet(3, 1, 1),
    "v2_w4": jet(3, 4, 0),
    "v11_w3": jet(10, 3, 0),
    "v11_w11": jet(10, 11, 1),
}
# Here R is the motion of v, not a motion of the fixed evaluation point.
for key in ["v2_w1", "v2_w4", "v11_w3"]:
    extra[key][1] = 0
require(extra == {"v2_w1": [7, 0, 9, 2], "v2_w4": [1, 0, 5, 8],
                  "v11_w3": [9, 0, 0, 11], "v11_w11": [7, 1, 1, 11]},
        "additional jet equations")

f3 = base(3)
require(evaluate(hasse(f3, 1), 1) == 13*61198, "f'(1) constant")
require(evaluate(hasse(f3, 2), 1) % P == 9, "quotient linear coefficient")
require(evaluate(hasse(f3, 1), 4) % P == 0, "f'(4) integral-order defect")
require(evaluate(hasse(f3, 2), 4) % P == 0, "f''(4) integral-order defect")
require(3*evaluate(hasse(f3, 3), 4) % P == 2, "quadratic term of f' at 4")
require(2*evaluate(hasse(base(10), 2), 3) % P == 6, "simple f' root at 3")

expected = {"v2_w1": [1, 0, 3], "v2_w4": [5, 12, 7],
            "v11_w3": [8, 1, 11], "v11_w11": [0, 5, 6]}
out = {"status": "PASS", "beta_coefficients": beta, "first_jets_c3": rows3,
       "first_jets_c10": rows10, "branches": {}}
for key, ext in extra.items():
    d = 3 if key.startswith("v2_") else 10
    values = solve((rows3 if d == 3 else rows10)+[ext])
    require(values == expected[key], "unexpected jet solution: "+key)
    const = 9*values[1] % P
    h = dense(base(d))
    g = dense({10: 1, 6: 11, 5: 7, 0: const})
    gcd, bez_h, bez_g = egcd(h, g)
    require(gcd == ([0, 1] if key == "v2_w1" else [1]), "final gcd: "+key)
    out["branches"][key] = {"extra_jet": ext, "R_S_T": values,
                              "G10_constant": const, "gcd": gcd,
                              "bezout_h": bez_h, "bezout_G10": bez_g}

target = Path(__file__).with_name("independent-jets.json")
target.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"status": "PASS", "branches": list(out["branches"]),
                  "output": str(target)}))
