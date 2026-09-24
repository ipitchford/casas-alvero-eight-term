#!/usr/bin/env python3
"""Independently verify the F13 univariate-resultant seed classification.

Resultant identities are checked at more points than their affine-Sylvester
degree bound over F_(13^3)=F13[t]/(t^3-2), using direct determinants. Polynomial
gcds are then computed over F13. No CAS is used.
"""
from array import array
from hashlib import sha256
from pathlib import Path
import json
import re
import time


def require(ok, message):
    if not ok:
        raise ValueError(message)


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def parse(text):
    d = {}
    for term in re.findall(r'[+-]?[^+-]+', text):
        if 'u' in term:
            c, e = term.split('u')
            c = 1 if c in ['', '+'] else -1 if c == '-' else int(c)
            e = int(e) if e else 1
        else:
            c, e = int(term), 0
        require(e not in d, 'Duplicate coefficient')
        d[e] = c % 13
    return trim([d.get(e, 0) for e in range(max(d)+1)])


def gcd(a, b):
    while b:
        r = a[:]
        while r and len(r) >= len(b):
            k, c = len(r)-len(b), r[-1]*pow(b[-1], -1, 13) % 13
            for j, x in enumerate(b):
                r[k+j] = (r[k+j]-c*x) % 13
            trim(r)
        a, b = b, r
    return [(c*pow(a[-1], -1, 13)) % 13 for c in a]


started = time.monotonic()
source = Path(__file__).with_name('seed13-univariate.txt')
polys = {}
for line in source.read_text().splitlines():
    key, expression = line.split()
    require(key not in polys, 'Repeated source record')
    polys[key] = parse(expression)
require(set(polys) == {'B0_R2', 'B0_R1', 'U1_R2', 'U1_R1',
                       'GENERIC_C', 'GENERIC_R2', 'GENERIC_R1'}, 'Incomplete source')
require(all((x**3-2) % 13 for x in range(13)), 'The extension polynomial is reducible')

q = 13**3
digits = [(i % 13, (i//13) % 13, i//169) for i in range(q)]
neg = [(-a % 13)+13*(-b % 13)+169*(-c % 13) for a, b, c in digits]
M = array('H', [0])*(q*q)
S = array('H', [0])*(q*q)
for i, (a0, a1, a2) in enumerate(digits):
    offset = i*q
    for j, (b0, b1, b2) in enumerate(digits):
        M[offset+j] = ((a0*b0+2*(a1*b2+a2*b1)) % 13
                       +13*((a0*b1+a1*b0+2*a2*b2) % 13)
                       +169*((a0*b2+a1*b1+a2*b0) % 13))
        S[offset+j] = ((a0-b0) % 13)+13*((a1-b1) % 13)+169*((a2-b2) % 13)


def mul(a, b):
    return M[a*q+b]


def add(a, b):
    return S[a*q+neg[b]]


def power(a, n):
    answer = 1
    while n:
        if n & 1:
            answer = mul(answer, a)
        a, n = mul(a, a), n//2
    return answer


inverse = [0]+[power(x, q-2) for x in range(1, q)]
require(all(mul(x, inverse[x]) == 1 for x in range(1, q)), 'Extension inversion failed')


def value(f, x):
    answer = 0
    for c in reversed(f):
        answer = add(mul(answer, x), c)
    return answer


def determinant(a):
    n, answer = len(a), 1
    for k in range(n):
        if not a[k][k]:
            pivot_row = next((i for i in range(k+1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            answer = neg[answer]
        pivot = a[k][k]
        answer = mul(answer, pivot)
        pivot_inverse, row_k = inverse[pivot], a[k]
        for i in range(k+1, n):
            row_i = a[i]
            if not row_i[k]:
                continue
            offset = mul(row_i[k], pivot_inverse)*q
            for j in range(k+1, n):
                row_i[j] = S[row_i[j]*q+M[offset+row_k[j]]]
            row_i[k] = 0
    return answer


def resultant(f, g):
    m, n = len(f)-1, len(g)-1
    fh, gh = list(reversed(f)), list(reversed(g))
    matrix = [[0]*(m+n) for _ in range(m+n)]
    for row in range(n):
        matrix[row][row:row+m+1] = fh
    for row in range(m):
        matrix[n+row][row:row+n+1] = gh
    return determinant(matrix)


def relations(branch, u):
    if branch == 'B0':
        b, c, d = 0, u, add(8, neg[u])
    elif branch == 'U1':
        b, c, d = 1, u, add(7, neg[u])
    else:
        b = add(mul(4, power(u, 4)), mul(10, u))
        c = value(polys['GENERIC_C'], u)
        numerator = add(add(add(5, b), mul(8, power(u, 19))), neg[power(u, 16)])
        require(mul(add(u, 12), c) == numerator, 'Exact c division failed')
        d = add(add(8, neg[b]), neg[c])
    f, h2, h1 = [0]*20, [0]*19, [0]*20
    for k, v in [(19, 1), (16, 4), (15, b), (1, c), (0, d)]:
        f[k] = v
    for k, v in [(18, 8), (15, 11), (14, mul(3, b)), (0, c)]:
        h2[k] = v
    for k, v in [(19, 7), (16, 3), (15, mul(3, b)), (1, mul(2, c)), (0, d)]:
        h1[k] = v
    return f, h2, h1, c, d


records = []
for branch, bound2, bound1 in [('B0', 38, 39), ('U1', 38, 39), ('GENERIC', 684, 702)]:
    for suffix, bound, index, factor_index in [('R2', bound2, 1, 3), ('R1', bound1, 2, 4)]:
        expected = polys[branch+'_'+suffix]
        require(len(expected)-1 <= bound < q, 'Invalid interpolation bound')
        for u in range(bound+1):
            r = relations(branch, u)
            actual = mul(r[factor_index], resultant(r[0], r[index]))
            require(actual == value(expected, u), f'Resultant identity failed: {branch} {suffix}, point={u}')
    G = gcd(polys[branch+'_R2'], polys[branch+'_R1'])
    expected_gcd = [9, 1] if branch == 'U1' else [1]
    require(G == expected_gcd, 'Unexpected resultant gcd')
    records.append({'branch': branch, 'resultantDegrees': [len(polys[branch+'_R2'])-1, len(polys[branch+'_R1'])-1],
                    'degreeBounds': [bound2, bound1], 'exactExtensionFieldDeterminants': [bound2+1, bound1+1],
                    'gcdLowFirst': G})

P19 = [0]*20
for k, c in [(19, 1), (16, 4), (15, 1), (1, 4), (0, 3)]:
    P19[k] = c
hasse_specs = [(17, {3: 9, 0: 4}, [12, 1]),
               (16, {4: 9, 1: 3, 0: 1}, [12, 1]),
               (2, {18: 8, 15: 11, 14: 3, 0: 4}, [12, 1]),
               (1, {19: 7, 16: 3, 15: 3, 1: 8, 0: 3}, [6, 1])]
for order, coefficients, expected_gcd in hasse_specs:
    Hk = [coefficients.get(k, 0) for k in range(max(coefficients)+1)]
    require(gcd(P19, Hk) == expected_gcd, f'Final marked-root gcd failed for H{order}')
require(sum([7, 3, 3, 8, 3]) % 13 == 11, 'The root at1 is not simple')

print(json.dumps({'status': 'PASS', 'records': records,
                  'extensionField': 'F13[t]/(t^3-2)', 'sourceSha256': sha256(source.read_bytes()).hexdigest(),
                  'finalMarkedRootGcds': {'H17': 'X-1', 'H16': 'X-1', 'H2': 'X-1', 'H1': 'X-7'},
                  'derivativeAtOne': 11,
                  'elapsedSeconds': round(time.monotonic()-started, 3),
                  'conclusion': 'For the normalized a!=0 seed, b=0 and a marked H16 root u!=0,1 are impossible; u=1 forces b=1,c=4,d=3.'}, indent=2))
