#!/usr/bin/env python3
"""Check both integral resultants by exact Sylvester determinants, then gcd mod p.

The degree bound is the Sylvester matrix size, since every matrix entry is
affine in e. Size+1 exact integer evaluations therefore prove each polynomial
identity, including its degree. No CAS is imported.
"""
from hashlib import sha256
from pathlib import Path
import json
import re
import time


def require(ok, message):
    if not ok:
        raise ValueError(message)


def parse_e(text):
    d = {}
    for term in re.findall(r'[+-]?[^+-]+', text):
        if 'e' in term:
            coefficient, exponent = term.split('e')
            coefficient = 1 if coefficient in ['', '+'] else -1 if coefficient == '-' else int(coefficient)
            exponent = int(exponent) if exponent else 1
        else:
            coefficient, exponent = int(term), 0
        require(exponent not in d, 'Duplicate coefficient in resultant')
        d[exponent] = coefficient
    return [d.get(e, 0) for e in range(max(d)+1)]


def determinant(a):
    a = [row[:] for row in a]
    previous, sign, n = 1, 1, len(a)
    for k in range(n-1):
        if not a[k][k]:
            pivot = next((j for j in range(k+1, n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                quotient, remainder = divmod(numerator, previous)
                require(remainder == 0, 'Bareiss division was not exact')
                a[i][j] = quotient
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def resultant(f, g):
    m, n = len(f)-1, len(g)-1
    fh, gh = list(reversed(f)), list(reversed(g))
    a = [[0]*(m+n) for _ in range(m+n)]
    for row in range(n):
        a[row][row:row+m+1] = fh
    for row in range(m):
        a[n+row][row:row+n+1] = gh
    return determinant(a)


def value(f, e):
    answer = 0
    for c in reversed(f):
        answer = answer*e+c
    return answer


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def gcd_mod(a, b, p):
    a, b = trim([c % p for c in a]), trim([c % p for c in b])
    while b:
        r = a[:]
        while r and len(r) >= len(b):
            k, c = len(r)-len(b), r[-1]*pow(b[-1], -1, p) % p
            for j, x in enumerate(b):
                r[k+j] = (r[k+j]-c*x) % p
            trim(r)
        a, b = b, r
    return [(c*pow(a[-1], -1, p)) % p for c in a]


def polynomials(e):
    A, B, C, D = -1140, 14535, -1589350-45*e, 1575954+44*e
    Q = [0]*20
    for k, c in [(19, 1), (16, A), (15, B), (9, e), (1, C), (0, D)]:
        Q[k] = c
    H10 = [0]*11
    for k, c in [(10, 184756), (7, 19448*A), (6, 8008*B), (0, e)]:
        H10[k] = c
    H1 = [0]*20
    for k, c in [(19, 20), (16, 17*A), (15, 16*B), (9, 10*e), (1, 2*C), (0, D)]:
        H1[k] = c
    return Q, H10, H1


started = time.monotonic()
source = Path(__file__).with_name('collision-resultants.log')
lines = source.read_text().splitlines()
R10 = parse_e(lines[lines.index('R10')+1])
R1 = parse_e(lines[lines.index('R1')+1])
require(len(R10)-1 == 19 and len(R1)-1 == 28, 'Unexpected resultant degrees')
require(R1[0] != 0, 'The e=0 degeneration is not excluded by the H1 resultant')
for index, bound, expected in [(1, 29, R10), (2, 38, R1)]:
    for e in range(bound+1):
        polys = polynomials(e)
        require(resultant(polys[0], polys[index]) == value(expected, e),
                f'Resultant interpolation identity failed at index={index}, e={e}')

p = 101
require(R10[-1] % p != 0 and R1[-1] % p != 0, 'Degree is not preserved modulo101')
G = gcd_mod(R10, R1, p)
require(G == [1], 'Resultants are not coprime modulo101')
print(json.dumps({'status': 'PASS', 'resultantDegrees': [19, 28],
                  'degreeBoundsFromAffineSylvesterMatrices': [29, 38],
                  'exactIntegerDeterminantEvaluations': [30, 39],
                  'modularGcdPrime': p, 'modularGcd': G, 'bothDegreesPreserved': True,
                  'H1ResultantAtZeroNonzero': True,
                  'sourceSha256': sha256(source.read_bytes()).hexdigest(),
                  'elapsedSeconds': round(time.monotonic()-started, 3),
                  'conclusion': 'The two characteristic-zero resultant polynomials are coprime; no collision-family parameter e satisfies both common-root conditions.'}, indent=2))
