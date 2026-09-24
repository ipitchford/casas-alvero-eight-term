#!/usr/bin/env python3
"""Independent integral-polynomial reconstruction for the u=v audit.

No producer modules, jet tables, or certificates are imported. The divided
equations are formed as full integer polynomials before reduction modulo13.
"""
from math import comb
import json

P = 13
ZERO = (0, 0, 0)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def constant(c):
    return {ZERO: c} if c else {}


def add(*terms):
    out = {}
    for term in terms:
        for m, c in term.items():
            out[m] = out.get(m, 0)+c
    return {m: c for m, c in out.items() if c}


def scale(a, c):
    return {m: c*x for m, x in a.items() if c*x}


def mul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            k = tuple(i+j for i, j in zip(m, n))
            out[k] = out.get(k, 0)+x*y
    return {m: c for m, c in out.items() if c}


def power(a, n):
    answer = constant(1)
    for _ in range(n):
        answer = mul(answer, a)
    return answer


def divide13(a):
    require(all(c % P == 0 for c in a.values()), 'Divided equation is not an integer polynomial')
    return {m: c//P for m, c in a.items()}


def mod13(a):
    return {m: c % P for m, c in a.items() if c % P}


def evaluate(a, point):
    return sum(c*point[0]**m[0]*point[1]**m[1]*point[2]**m[2] for m, c in a.items())


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def gcd(a, b):
    while b:
        r = a[:]
        while r and len(r) >= len(b):
            k, c = len(r)-len(b), r[-1]*pow(b[-1], -1, P) % P
            for j, x in enumerate(b):
                r[k+j] = (r[k+j]-c*x) % P
            trim(r)
        a, b = b, r
    return [c*pow(a[-1], -1, P) % P for c in a]


def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % P


variables = [{(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}]
r, ell, k = variables
u = add(constant(2), scale(r, P))
D = add(constant(3), scale(ell, P))
C = scale(k, P)
A = -comb(20, 16)
B = add(scale(power(u, 5), -comb(20, 15)), scale(u, -16*A))
E = add(constant(-1-A), scale(B, -1), scale(C, -1), scale(D, -1))


def f(x):
    return add(power(x, 20), scale(power(x, 16), A), mul(B, power(x, 15)),
               mul(C, power(x, 10)), mul(D, power(x, 3)), mul(E, x))


H3 = add(scale(power(u, 17), comb(20, 3)), scale(power(u, 13), comb(16, 3)*A),
         scale(mul(B, power(u, 12)), comb(15, 3)), scale(mul(C, power(u, 7)), comb(10, 3)), D)
H1at1 = add(constant(20+16*A), scale(B, 15), scale(C, 10), scale(D, 3), E)
equations = [divide13(a) for a in [f(u), H3, H1at1, f(constant(4))]]
rows, constants = [], []
for a in equations:
    require(all(sum(m) <= 1 for m in mod13(a)), 'A nonlinear divided coefficient survives modulo13')
    rows.append([a.get((1, 0, 0), 0) % P, a.get((0, 1, 0), 0) % P, a.get((0, 0, 1), 0) % P])
    constants.append(a.get(ZERO, 0) % P)
require(rows == [[10, 6, 8], [4, 1, 7], [11, 2, 9], [10, 8, 5]], 'Wrong fully expanded jet matrix')
require(constants == [7, 6, 4, 3], 'Wrong fully expanded constants')
require((rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0]) % P == 12, 'Initial Jacobian failed')

point1, point4 = [12, 3, 3], [5, 7, 12]
for point, third, expected_det in [(point1, 2, 3), (point4, 3, 5)]:
    selected = [equations[0], equations[1], equations[third]]
    require(all(evaluate(a, point) % P == 0 for a in selected), 'Wrong affine solution')
    require(determinant3([rows[0], rows[1], rows[third]]) == expected_det, 'Nonunit Jacobian')

# A complete coefficient check of the second precision step: the three exact
# divided polynomials equal an affine map with a unit linear matrix plus13
# times integral polynomials. Their values at point1 also lie in13Z.
require(all(c % P == 0 for a in equations[:3] for m, c in a.items() if sum(m) >= 2),
        'Second-step nonlinear error is not in13Z[r,l,k]')
require(all(evaluate(a, point1) % P == 0 for a in equations[:3]), 'Second-step constants fail')
require(evaluate(equations[3], point1) % P == 6, 'Final f(4)/13 obstruction failed')

leading = comb(20, 10)//P
N4 = add(constant(leading*4**10+(comb(16, 10)*A//P)*4**6),
         scale(B, (comb(15, 10)//P)*4**5), k)
require(mod13(N4) == {ZERO: 10, (0, 0, 1): 1}, 'H10(4)/13 is not k-3 modulo13')
require(leading % P == 3, 'Normalized leading coefficient is not a unit')

h = [0]*21
for e, c in [(20, 1), (16, 4), (15, 6), (3, 3), (1, 12)]:
    h[e] = c
g1 = [1, 0, 0, 0, 0, 7, 11, 0, 0, 0, 1]
g4 = [4, 0, 0, 0, 0, 7, 11, 0, 0, 0, 1]
require(gcd(h, g1) == [9, 1] and gcd(h, g4) == [1], 'Final root gcds failed')
require(sum(i*c*pow(4, i-1, P) for i, c in enumerate(g1) if i) % P == 3,
        'G10 root4 is not simple')
hasse4 = [sum(comb(i, j)*c*pow(4, i-j, P) for i, c in enumerate(h) if i >= j) % P
          for j in range(4)]
require(hasse4 == [0, 0, 0, 5], 'The triple-root Taylor bound fails')

print(json.dumps({'status': 'PASS', 'method': 'Independent full integer-polynomial composition, then exact division by13',
                  'rows_r_ell_k': rows, 'constants': constants,
                  'initialUnitJacobianDeterminant': 12, 'secondUnitJacobianDeterminant': 3,
                  'allNonlinearDividedCoefficientsIn13Z': True,
                  'secondPrecisionPoint': point1, 'H10_at4_div13_reduction': 'k-3',
                  'G10DerivativeAt4': 3, 'fAt4Div13AtSecondPrecisionPoint': 6,
                  'finalGcds': {'wbar1': [9, 1], 'wbar4': [1]},
                  'scope': 'Exact arithmetic and coefficient identities supporting the written ramification-safe valuation audit.'}, indent=2))
