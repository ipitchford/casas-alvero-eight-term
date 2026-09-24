#!/usr/bin/env python3
"""Exact first 2-saturation certificate for the full degree-20 incidence ideal.

Polynomials are expanded over Z, then checked coefficient by coefficient.
Only the final evaluation is modulo 2. No CAS or assertion statements are used.
The pre-existing residue enumeration is read solely to count the survivors.
"""
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


# Variables a1,...,a19,w. Keeping a1 free strengthens the identity check;
# the centered residue enumerator subsequently specializes a1=0.
N = 20
ONE = {(0,)*N: 1}


def const(c):
    return {next(iter(ONE)): c} if c else {}


def monomial(i, power=1):
    e = [0]*N
    e[i] = power
    return {tuple(e): 1}


def add(*polys):
    r = Counter()
    for p in polys:
        for e, c in p.items():
            r[e] += c
    return {e: c for e, c in r.items() if c}


def scale(c, p):
    return {e: c*d for e, d in p.items() if c*d}


def mul(p, q):
    r = Counter()
    for e, c in p.items():
        for f, d in q.items():
            r[tuple(a+b for a, b in zip(e, f))] += c*d
    return {e: c for e, c in r.items() if c}


def wpow(j):
    return monomial(19, j)


def at_bits(p, ones):
    # w is zero and a_i is one exactly at the listed indices.
    return sum(c for e, c in p.items()
               if not e[19] and all(not k or i+1 in ones for i, k in enumerate(e[:19]))) % 2


def v2(c):
    return (abs(c) & -abs(c)).bit_length()-1


F = add(ONE, *(scale(comb(20, j), monomial(j-1)) for j in range(1, 20)))
P = add(wpow(20), *(scale(comb(20, j), mul(monomial(j-1), wpow(20-j))) for j in range(1, 20)))
source = json.loads((Path(__file__).parent/'residue-patterns.json').read_text())
require(source['status'] == 'PASS', 'Residue enumeration did not pass')
results = []
for m, k, cut, label in [(4, 16, [8, 12, 18], 'A_16plus4'),
                         (16, 4, [2, 12, 18], 'B_4plus16')]:
    g = add(ONE, *(scale(comb(m, j), monomial(j-1)) for j in range(1, m+1)))
    q = add(wpow(k), *(scale(comb(k, j), mul(monomial(j-1), wpow(k-j))) for j in range(1, k+1)))
    # This is an exact Z-polynomial combination of incidence generators.
    S = add(P, mul(wpow(m), q), mul(add(g, ONE), add(F, g, q)))
    require(all(c % 2 == 0 for c in S.values()), 'The proposed numerator is not coefficientwise even')
    T = {e: c//2 for e, c in S.items()}
    branch = next(b for b in source['branches'] if b['type'] == label)
    survivors = []
    for p in branch['patterns']:
        ones = set(p['ones'])
        value = at_bits(T, ones)
        require(value == sum(i in ones for i in cut) % 2, 'Specialized quotient differs from claimed cut')
        if value == 0:
            survivors.append(p)
    # Binomial valuation root bounds: once the opposite visible coefficient
    # is in 2O, every degree e<k coefficient has this certified lower bound.
    lower = {e: max(v2(comb(20, e)), 1 if e == m else 0) for e in range(1, k)}
    ratios = {e: Fraction(v, k-e) for e, v in lower.items()}
    bound = min(ratios.values())
    expected_bound = Fraction(1, 14) if m == 4 else Fraction(1, 2)
    require(bound == expected_bound, 'Newton root bound mismatch')
    # G_k at a root in the zero cluster then bounds the opposite coefficient.
    derivative_bound = min([k*bound] + [v2(comb(k, i))+(k-i)*bound for i in range(1, k)])
    require(derivative_bound == (Fraction(8, 7) if m == 4 else Fraction(2)), 'G_k bound mismatch')
    projection = Counter(tuple(int(j in p['ones']) for j in [2, 8, 12, 18]) for p in survivors)
    results.append({'type': label, 'normalizingDegree': m, 'oppositeDegree': k,
                    'integralNumeratorTermCount': len(S),
                    'quotientPolynomialSHA256': __import__('hashlib').sha256(json.dumps(sorted(T.items())).encode()).hexdigest(),
                    'cutIndices': cut, 'survivingCoefficientPatterns': len(survivors),
                    'survivingMarkedAssignments': sum(p['markedAssignmentCount'] for p in survivors),
                    'rootValuationLowerBound': str(bound),
                    'oppositeNormalizedCoefficientValuationLowerBound': str(derivative_bound),
                    'projectedResidues_a2_a8_a12_a18': [{'bits': list(v), 'coefficientPatternCount': n} for v, n in sorted(projection.items())]})
require([r['survivingCoefficientPatterns'] for r in results] == [465, 603], 'Wrong survivor count')
require([r['survivingMarkedAssignments'] for r in results] == [40960, 40960], 'Wrong assignment count')
print(json.dumps({'status': 'PASS', 'certificate': 'S=P+w^m*q+(g+1)*(F+g+q), T=S/2 in Z[a1,...,a19,w]',
                  'results': results, 'remainingCoefficientPatterns': 1068,
                  'remainingMarkedResidueAssignments': 81920,
                  'scope': 'Exact necessary 2-saturation cuts and valuation bounds. Surviving patterns are not claimed to lift; neither residue type is excluded.'}, indent=2))
