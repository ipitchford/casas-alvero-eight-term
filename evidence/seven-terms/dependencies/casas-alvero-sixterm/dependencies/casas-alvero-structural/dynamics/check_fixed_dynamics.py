"""Independent, standard-library reconstruction and mod-11 Bezout certificate.

No SymPy/Singular is used. Assertions are deliberately avoided, so python -O
performs exactly the same checks. Coefficient arrays are in ascending order.
"""
from functools import reduce
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def scale(a, k):
    return trim([k * v for v in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] += v * w
    return trim(c)


def power(a, n):
    c = [1]
    for _ in range(n):
        c = mul(c, a)
    return c


def monomial(k, n):
    return [0] * n + [k]


def mod(a, p):
    return trim([v % p for v in a])


def divmod_poly(a, b, p):
    a, b = mod(a, p), mod(b, p)
    require(bool(b), 'Polynomial division by zero')
    q = [0] * max(0, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, p)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] * inverse % p
        q[shift] = coefficient
        for i, v in enumerate(b):
            a[i + shift] = (a[i + shift] - coefficient * v) % p
        a = trim(a)
    return trim(q), a


def xgcd(a, b, p):
    old_r, r = mod(a, p), mod(b, p)
    old_s, s = [1], []
    old_t, t = [], [1]
    steps = []
    while r:
        q, new_r = divmod_poly(old_r, r, p)
        steps.append([len(old_r) - 1, len(r) - 1, len(new_r) - 1])
        old_r, r = r, new_r
        old_s, s = s, mod(sub(old_s, mul(q, s)), p)
        old_t, t = t, mod(sub(old_t, mul(q, t)), p)
    inverse = pow(old_r[-1], -1, p)
    return (mod(scale(old_r, inverse), p),
            mod(scale(old_s, inverse), p),
            mod(scale(old_t, inverse), p), steps)


P = [595, 0, 0, -35]
Q = [0, 0, 51, -35]
R = add([-35 * 17**5], monomial(35, 18))
S = add([-35 * 17**5], monomial(51 * 17**3, 6))
A = scale(P, 34)
B = scale(sub(Q, P), 35)
En = add(add(mul(power(A, 4), power(P, 2)),
             scale(mul(mul(mul(power(A, 2), power(B, 2)), P), Q), 6)),
         mul(power(B, 4), power(Q, 2)))
On = scale(mul(mul(A, B), add(mul(power(A, 2), P),
                              mul(power(B, 2), Q))), 4)
N = sub(power(sub(mul(R, En), scale(mul(S, power(Q, 6)), 34**4)), 2),
        mul(mul(mul(P, Q), power(R, 2)), power(On, 2)))
content = reduce(gcd, (abs(v) for v in N))
require(content == 17**8, 'Unexpected primitive content')
H = [v // content for v in N]
frozen = json.loads((ROOT / 'fixed-polynomial.json').read_text())
require(H[::-1] == frozen['H_coefficients_high_first'],
        'Reconstructed H disagrees with parent polynomial')
require(len(H) - 1 == 72, 'Unexpected H degree')

# C(z) = z^(6 deg H) H(17^2/z^6).
C = [0] * 433
for i, coefficient in enumerate(H):
    C[432 - 6*i] = coefficient * 17**(2*i)
C = trim(C)
require(len(C) - 1 == 432, 'Unexpected composition degree')

p = 11
require(len(mod(H, p)) == len(H), 'H degree drops modulo 11')
require(len(mod(C, p)) == len(C), 'C degree drops modulo 11')
g, U, V, steps = xgcd(H, C, p)
require(g == [1], 'Mod-11 gcd is not one')
require(mod(add(mul(U, H), mul(V, C)), p) == [1],
        'Independent Bezout identity verification failed')
certificate = {
    'modulus': p, 'coefficient_order': 'ascending',
    'identity': 'U(z)*H(z) + V(z)*C(z) = 1 in F_11[z]',
    'U': U, 'V': V, 'euclidean_degree_steps': steps,
}
(HERE / 'bezout-mod11.json').write_text(json.dumps(certificate, indent=2) + '\n')

checks = {}
for p in (11, 13, 19, 23, 29, 31):
    gp, _, _, _ = xgcd(H, C, p)
    checks[str(p)] = {
        'H_degree': len(mod(H, p)) - 1,
        'C_degree': len(mod(C, p)) - 1,
        'gcd_degree': len(gp) - 1,
    }
K = 51**7 - 17**2 * 35**7
receipt = {
    'status': 'PASS', 'arithmetic': 'Python standard library integers',
    'raw_norm_content': content, 'H_degree': len(H) - 1,
    'C_degree': len(C) - 1,
    'H_coefficients_sha256': sha256(json.dumps(H).encode()).hexdigest(),
    'mod11_Bezout_verified': True,
    'mod11_U_degree': len(U) - 1, 'mod11_V_degree': len(V) - 1,
    'modular_checks': checks,
    'degenerate_a_zero_obstruction_K': K,
}
(HERE / 'independent-dynamics-check.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
