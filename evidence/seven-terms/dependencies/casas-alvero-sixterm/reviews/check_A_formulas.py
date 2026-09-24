"""Independent audit of the scalar identities used in A's lifting argument."""
from math import comb
from fractions import Fraction
import json


def trim(a):
    while a and not a[-1]: a.pop()
    return a


def gcd(a, b, p=13):
    while b:
        r = a[:]
        while len(r) >= len(b):
            k, c = len(r)-len(b), r[-1]*pow(b[-1], -1, p) % p
            for j, d in enumerate(b): r[k+j] = (r[k+j]-c*d) % p
            trim(r)
        a, b = b, r
    return [c*pow(a[-1], -1, p) % p for c in a]


def hasse(f, k, p=13):
    return trim([comb(i, k)*f[i] % p for i in range(k, len(f))])


def evaluate(f, x, p=13): return sum(c*pow(x, i, p) for i, c in enumerate(f)) % p


f = [0]*21
for k, c in [(20, 1), (17, 4), (16, 1), (2, 4), (1, 3)]: f[k] = c
gcds = {k: gcd(f, hasse(f, k)) for k in [17, 16, 2, 1]}
if any(gcds[k] != [12, 1] for k in [17, 16, 2]):
    raise ValueError('Residual witness rigidity gcd failed')
if evaluate(hasse(f, 1), 1) != 11:
    raise ValueError('Residual root 1 is not simple')
# Affine coefficient pairs [constant, coefficient of E], independently derived.
A = [-comb(20, 17), 0]
B = [-comb(20, 16)-comb(17, 16)*A[0], 0]
C = [-comb(20, 2)-comb(17, 2)*A[0]-comb(16, 2)*B[0], -comb(10, 2)]
D = [-1-A[0]-B[0]-C[0], -1-C[1]]
if [A, B, C, D] != [[-1140, 0], [14535, 0], [-1589350, -45], [1575954, 44]]:
    raise ValueError('Collision coefficient formulas differ')
if [comb(20, 10), comb(17, 10), comb(16, 10)] != [184756, 19448, 8008]:
    raise ValueError('H10 coefficient mismatch')
# Missing a=b=0 subchart, after H2 witness normalization: c=5,d=7.
h = [0]*21
h[20], h[2], h[1] = 1, 5, 7
if evaluate(h, 1) or evaluate(hasse(h, 2), 1):
    raise ValueError('Lower chart normalization mismatch')
P = h[1:]
H1 = hasse(h, 1)
difference = trim([(H1[i]-7*P[i]) % 13 for i in range(len(P))])
if difference != [10, 1] or evaluate(P, 3) != 12:
    raise ValueError('Lower chart contradiction failed')
print(json.dumps({'status': 'PASS', 'residualGcdsLowFirst': gcds,
                  'residualDerivativeAt1': 11,
                  'collisionCoefficientAffinePairs': {'A': A, 'B': B, 'C': C, 'D': D},
                  'H10BinomialCoefficients': [comb(20, 10), comb(17, 10), comb(16, 10)],
                  'a_b_zero_chart': {'H1_minus_7P': difference, 'P_at_3': evaluate(P, 3)}}, indent=2))
