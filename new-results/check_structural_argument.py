#!/usr/bin/env python3
"""Small exact checks for STRUCTURAL_ARGUMENT.md; no producer imports."""
import json
from math import comb

P = 17
Q = (14, 12, 15, 0, 14, 1)


def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*x for x in a])


def rem(a, b):
    a, b = trim(a), trim(b)
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, P) % P
        a = add(a, [0]*k + scale(b, -c))
    return a


def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return rem(c, Q)


def power(a, n):
    b = [1]
    while n:
        if n & 1:
            b = mul(b, a)
        a = mul(a, a)
        n //= 2
    return b


def gcd(a, b):
    while trim(b) != [0]:
        a, b = b, rem(a, b)
    return scale(a, pow(trim(a)[-1], -1, P))


def eq(a, b, label):
    if trim(a) != trim(b):
        raise ValueError(label, a, b)


def valuation(n):
    if n == 0:
        raise ValueError("zero valuation")
    v = 0
    while n % P == 0:
        n //= P
        v += 1
    return v


x = [0, 1]
eq(power(x, P**5), x, "degree-five Frobenius")
eq(gcd(Q, add(power(x, P), scale(x, -1))), [1], "irreducibility")
u = {0: [1], 1: [0], 2: [0], 3: [-1]}
w = {j: [0] for j in range(4, 17)}
w.update({4: [-2], 9: x, 10: [1], 14: [-2]})
for j in range(4, 17):
    total = [0]
    for i in range(j):
        total = add(total, scale(mul(u[i], power(w[j], j-i)), comb(j, i)))
    u[j] = scale(total, -1)
expected = {
    4: [-7], 9: [-3, 7, 8, 5, -5],
    10: [4, -2, 5, 1, -1], 14: [-4, -8, 3, 4, -4]
}
for j in range(4, 17):
    eq(u[j], expected.get(j, [0]), f"coefficient {j}")
    r = w[j]
    h = add(add(power(r, 20), scale(power(r, 17), -1)),
            add(scale(power(r, 2), -3), scale(r, 3)))
    eq(h, [0], f"root incidence {j}")
t = [-8037]
for j in range(4, 17):
    weight = comb(19-j, 2) * (comb(20, j)//17)
    t = add(t, scale(u[j], weight))
    if weight % P != (3 * (-1)**j * pow(j*(j-3), -1, P)) % P:
        raise ValueError("closed weight formula", j)
eq(t, [0], "divided obstruction residue")
frob_delta = add(power(u[9], P), scale(u[9], -1))
eq(frob_delta, [7, -7, -8, 1, 7], "non-fixed coefficient")
if frob_delta == [0]:
    raise ValueError("coefficient must not be Frobenius fixed")
y = scale(mul(add(x, [1]), power(add(x, [-1]), P**5-2)), 7)
eq(power(y, P), add(power(y, 2), [-5]), "quadratic Frobenius law")

active = {4, 5, 8, 10, 11}
z = {0: 1, 1: 0, 2: 0, 3: -1}
for j in range(4, 17):
    z[j] = -sum(comb(j, i)*z[i] for i in range(j)) if j in active else 0
integer_t = -8037 + sum(comb(19-j, 2)*(comb(20, j)//17)*z[j]
                       for j in range(4, 17))
if integer_t != 11294240224 or valuation(integer_t) != 3:
    raise ValueError("third-order obstruction", integer_t)
print(json.dumps({
    "status": "PASS", "fieldPrime": P, "fieldDegree": 5,
    "residueActiveIndices": [4, 9, 10, 14],
    "residueDividedObstruction": 0,
    "frobeniusFixedCoefficientClaim": "FALSE",
    "integerActiveIndices": sorted(active),
    "integerCoefficients": {j: z[j] for j in sorted(active)},
    "integerDividedObstruction": integer_t,
    "integerObstructionValuation": 3,
    "scope": "two small exact examples; no census and no row-9 exclusion"
}, indent=2))
