#!/usr/bin/env python3
"""Exact finite arithmetic behind the full-support row8 bound and residue cut.

This verifies binomial valuations, the integer divided equation, all seed
Hasse gcds, the single-unit classification, and every displayed census sample.
The complete census itself has two separate C++ implementations.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def vp(n, p):
    require(n != 0, 'valuation of zero')
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def trim(a):
    a = [x % 17 for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def remainder(a, b):
    a, b = trim(a), trim(b)
    while len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, 17) % 17
        for i, x in enumerate(b):
            a[i+k] = (a[i+k]-c*x) % 17
        a = trim(a)
    return a


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, remainder(a, b)
    return [(x*pow(a[-1], -1, 17)) % 17 for x in a]


h = [0]*21
h[20], h[17] = 1, -1
gcd_degrees = {}
for k in range(1, 20):
    derivative = [comb(e+k, k)*h[e+k] for e in range(21-k)]
    g = gcd(h, derivative)
    gcd_degrees[k] = len(g)-1
    if k in [1, 2, 3]:
        require(g == [0]*17+[1], 'Low derivative common-root cluster differs')
    elif k == 17:
        require(g == [16, 0, 0, 1], 'H17 common roots differ')
    elif k in [18, 19]:
        require(g == [0]*(20-k)+[1], 'High derivative common roots differ')
    else:
        require(trim(derivative) == [] and len(g) == 21, 'Middle ordinary Hasse derivative should vanish')

require([j for j in range(21) if comb(20, j) % 17] == [0, 1, 2, 3, 17, 18, 19, 20], 'Lucas support at17 differs')
require(all(vp(comb(17, j), 17) == 1 for j in range(1, 17)), 'G17 valuations differ')
require(all(vp(comb(18, j), 17) == 1 for j in range(2, 17)), 'G18 valuations differ')
require(all(vp(comb(19, j), 17) == 1 for j in range(3, 17)), 'G19 valuations differ')
require(all(comb(19, j) % 17 for j in [0, 2, 17, 18, 19]), 'G19 visible terms differ')

# Pairs (constant,slope) represent lower-bound terms constant+slope*delta.
a17 = {(0, 17), (1, 1)}
a18 = {(0, 18), (1, 2)} | {(c, s+1) for c, s in a17}
a19 = {(0, 19), (1, 3)} | {(c, s+2) for c, s in a17} | {(c, s+1) for c, s in a18}
require(a18 == {(0, 18), (1, 2)} and a19 == {(0, 19), (1, 3)}, 'Coupled tropical bound differs')
low_terms = ({(c, s+3) for c, s in a17} | {(c, s+2) for c, s in a18}
             | {(c, s+1) for c, s in a19})
require(low_terms == {(0, 20), (1, 4)}, 'Bounds at the minimum root differ')
delta = Fraction(1, 13)
require(17*delta == 1+4*delta and 20*delta > 17*delta, 'Newton radius intersection differs')
require(16*delta > 1, 'Simplified coefficient bounds are not valid')
require([1+i*delta for i in [1, 2, 3]] == [Fraction(14, 13), Fraction(15, 13), Fraction(16, 13)], 'Final coefficient bounds differ')

C = {j: comb(20, j) for j in range(1, 20)}
require(1-C[3] == -17*67 and C[2]-3*C[3] == -17*190, 'Divided identity constants differ')
require([C[j] for j in [17, 18, 19]] == [1140, 190, 20], 'Low coefficient identity differs')
require(all(C[j] % 17 == 0 for j in range(4, 17)), 'Middle coefficients are not divisible by17')
require([j for j in range(21) if comb(20, j) % 2] == [0, 4, 16, 20], 'Pair obstruction support differs')
require([j for j in range(21) if comb(20, j) % 5] == [0, 5, 10, 15, 20], 'Triple obstruction support differs')


def add(a, b):
    return ((a[0]+b[0]) % 17, (a[1]+b[1]) % 17)


def mul(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % 17,
            (a[0]*b[1]+a[1]*b[0]-a[1]*b[1]) % 17)


def power(a, n):
    v = (1, 0)
    for _ in range(n):
        v = mul(v, a)
    return v


require(all((x*x+x+1) % 17 for x in range(17)), 'Cube-root extension reducible')
roots = [(1, 0), (0, 1), (16, 16)]
require(all(power(r, 3) == (1, 0) for r in roots), 'Cube-root arithmetic failed')


def reconstruct(labels):
    a = [(0, 0)]*20
    a[0], a[3] = (1, 0), (16, 0)
    for j, e in enumerate(labels, 4):
        if e == -1:
            continue
        rho = roots[e]
        s = (0, 0)
        for i in range(j):
            s = add(s, mul((comb(j, i) % 17, 0), mul(a[i], power(rho, j-i))))
        a[j] = ((-s[0]) % 17, (-s[1]) % 17)
    total = (0, 0)
    for j in range(4, 17):
        total = add(total, mul((C[j]//17 % 17, 0), a[j]))
    return a, total


single = []
for j in range(4, 17):
    for e in range(3):
        labels = [-1]*13
        labels[j-4] = e
        a, total = reconstruct(labels)
        if total == (16, 0):
            single.append({'degree': j, 'unitExponent': e, 'coefficient': a[j]})
require(single == [{'degree': 11, 'unitExponent': 0, 'coefficient': (11, 0)}], 'Single-unit classification differs')

base = Path(__file__).parent
census = json.loads((base/'row8-residue-enumeration.json').read_text())
independent = json.loads((base/'row8-independent-census.json').read_text())
require(census['status'] == independent['status'] == 'PASS', 'Census did not pass')
require(census['afterDividedIdentity'] == independent['afterDividedIdentity'] == 233310, 'Census totals differ')
require(census['afterUnitRootCollisionObstructions'] == independent['afterCommonRootObstructions'] == 180341, 'Filtered totals differ')
require(sum(census['histogramByNumberOfUnitWitnesses']) == 233310 and sum(census['filteredHistogram']) == 180341, 'Histograms do not sum')
for number, labels in census['sampleUnitRootExponentsByWitnessCount'].items():
    require(sum(e >= 0 for e in labels) == int(number), 'Sample unit count differs')
    _, total = reconstruct(labels)
    require(total == (16, 0), 'Sample fails the divided identity')
    require(not (labels[0] >= 0 and labels[0] == labels[12]), 'Sample violates pair obstruction')
    require(not (labels[1] >= 0 and labels[1] == labels[6] == labels[11]), 'Sample violates triple obstruction')

print(json.dumps({'status': 'PASS', 'allNineteenSeedHasseGcdDegrees': gcd_degrees,
                  'zeroClusterMinimumNonzeroRootValuation': '1/13',
                  'coefficientValuationBounds_a17_a18_a19': ['14/13', '15/13', '16/13'],
                  'dividedIdentityRightHandSideMod17': 16,
                  'singleUnitWitnessCases': single,
                  'twoIndependentCensusTotals': [233310, 180341],
                  'scope': 'Exact support for proved necessary conditions and a complete finite residue census; no characteristic-zero lift or row exclusion.'}, indent=2))
