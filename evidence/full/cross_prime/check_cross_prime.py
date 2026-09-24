#!/usr/bin/env python3
"""Exact algebra and finite residue checks for the p17/p2 comparison.

No CAS dependency and no assertion statements. This does not assert that a
surviving residue assignment lifts to characteristic zero.
"""
from collections import Counter
from fractions import Fraction
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


# Z[x,t,u,v0,v1,v2]
N = 6
ZERO = (0,)*N


def constant(c):
    return {ZERO: c} if c else {}


def variable(i):
    e = [0]*N
    e[i] = 1
    return {tuple(e): 1}


def add(*polys):
    out = Counter()
    for p in polys:
        for e, c in p.items():
            out[e] += c
    return {e: c for e, c in out.items() if c}


def scale(c, p):
    return {e: c*d for e, d in p.items() if c*d}


def mul(*polys):
    out = constant(1)
    for p in polys:
        new = Counter()
        for e, c in out.items():
            for f, d in p.items():
                new[tuple(a+b for a, b in zip(e, f))] += c*d
        out = {e: c for e, c in new.items() if c}
    return out


def power(p, k):
    return mul(*([p]*k))


def coefficient(p, degree):
    return {tuple([0]+list(e[1:])): c for e, c in p.items() if e[0] == degree}


x, t, u, v0, v1, v2 = [variable(i) for i in range(N)]
xt = add(x, scale(-1, t))
xu = add(x, scale(-1, u))
Vlow = add(v0, mul(v1, x), mul(v2, power(x, 2)))

G2 = add(power(x, 2), scale(-1, power(t, 2)))
require(G2 == mul(xt, add(x, t)), 'G2 factorization failed')
G3_67 = add(power(x, 3), scale(-3, mul(power(t, 2), x)), scale(2, power(t, 3)))
require(G3_67 == mul(power(xt, 2), add(x, scale(2, t))), 'G3 factorization failed')
G3_9 = add(power(x, 3), scale(-1, power(t, 3)))
require(G3_9 == mul(xt, add(power(x, 2), mul(t, x), power(t, 2))), 'Row9 G3 factorization failed')

U9 = mul(x, power(xt, 3))
expected9 = add(scale(-3, mul(t, v0)), scale(3, mul(power(t, 2), v1)), scale(-1, mul(power(t, 3), v2)))
require(coefficient(mul(U9, Vlow), 3) == expected9, 'Row9 coefficient obstruction failed')

U = mul(x, xt, power(xu, 2))
actual3 = coefficient(mul(U, Vlow), 3)
expected3 = add(scale(-1, mul(t, v0)), scale(-2, mul(u, v0)),
                mul(power(u, 2), v1), scale(2, mul(t, u, v1)),
                scale(-1, mul(t, power(u, 2), v2)))
require(actual3 == expected3, 'Double-root coefficient identity failed')
denominator = add(v0, scale(-2, mul(u, v1)), mul(power(u, 2), v2))
numerator = mul(u, add(scale(-2, v0), mul(u, v1)))
require(add(mul(t, denominator), scale(-1, numerator)) == scale(-1, actual3),
        'Rearranged scale identity failed')
expected2 = add(mul(power(u, 2), v0), scale(2, mul(t, u, v0)), scale(-1, mul(t, power(u, 2), v1)))
require(coefficient(mul(U, Vlow), 2) == expected2, 'X2 coefficient identity failed')
require(coefficient(mul(U, Vlow), 1) == scale(-1, mul(t, power(u, 2), v0)), 'X1 identity failed')

# After lambda=mu+1, nu(V1)>=1, mu>1/2, the u^2 V0 term is uniquely
# smallest in the X2 coefficient. Check the exact positive valuation gaps.
# An affine a*mu+b is positive for every mu>1/2 when a>=0 and
# a/2+b>=0, with either a>0 or b>0; these particular gaps are stronger.
gaps = {'X2_second_term_minus_first': (0, 2),
        'X2_third_term_minus_first': (1, 2),
        'G4_middle_term_minus_u4': (0, 3),
        'G4_row67_last_term_minus_u4': (0, 6)}
for name, (a, b) in gaps.items():
    require(a >= 0 and Fraction(a, 2)+b > 0, 'Valuation gap failed: '+name)
require(comb(20, 18) == 190 and comb(20, 19) == 20, 'Normalized coefficient conversion mismatch')
require((190 & -190) == 2 and (20 & -20) == 4, 'Coefficient valuations mismatch')

# Weighted return to the original normalization: lambda=mu+1 and
# nu(a_j)=nu(b_j)-j*lambda. Pairs encode A*mu+B exactly.
def original_value(pair, j):
    return (pair[0]-j, pair[1]-j)


require(original_value((1, 0), 1) == (0, -1), 'Original repeated-root scale mismatch')
require(original_value((4, 4), 4) == (0, 0), 'Distinguished degree4 scale mismatch')
require(original_value((4, 0), 4) == (0, -4), 'Repeated-root degree4 scale mismatch')
orig18 = original_value((2, -1), 18)
orig19 = original_value((3, -1), 19)
require(orig18 == (-16, -19) and orig19 == (-16, -20), 'High coefficient scaling mismatch')
require((orig18[0], orig18[1]-orig18[0]) == (-16, -3), 'a18 formula in lambda differs')
require((orig19[0], orig19[1]-orig19[0]) == (-16, -4), 'a19 formula in lambda differs')
require((orig19[0]-orig18[0], orig19[1]-orig18[1]) == (0, -1), 'Coefficient ratio mismatch')

# Check simplicity of the distinguished root 1 in the actual p17 rows.
seed_simple = []
for row, b, d, e in [(4, 0, 11, 8), (6, 2, 11, 6), (7, 2, 14, 3)]:
    value = (20+18*14+17*b+2*d+e) % 17
    require(value != 0, 'Distinguished root is not simple at17')
    seed_simple.append({'row': row, 'hDerivativeAtOneMod17': value})

lower_masks = [sum(1 << i for i in range(j) if comb(j, i) % 2) for j in range(20)]
results = []
expected_counts = {
    ('4', 'A', 0): (50, 4095), ('4', 'A', 1): (58, 6143),
    ('4', 'B', 0): (145, 4608), ('4', 'B', 1): (97, 3584),
    ('6/7', 'A', 0): (50, 4095), ('6/7', 'A', 1): (58, 6143),
    ('6/7', 'B', 0): (145, 4608), ('6/7', 'B', 1): (97, 3584),
    ('9', 'A', 0): (22, 1535), ('9', 'A', 1): (24, 512),
    ('9', 'B', 0): (0, 0), ('9', 'B', 1): (161, 1536)}
for row in ['4', '6/7', '9']:
    for typ, base, cut, size in [('A', {4: 1, 16: 0}, [8, 12, 18], 16),
                                 ('B', {4: 0, 16: 1}, [2, 12, 18], 4)]:
        for eps in [0, 1]:
            given = dict(base)
            given[17] = 0
            if row == '4':
                given.update({2: eps, 3: 0})
            elif row == '6/7':
                given.update({2: eps, 3: eps})
            else:
                given.update({2: 0, 3: eps, 18: eps, 19: eps})
            free = [j for j in range(2, 20) if j not in given]
            counts = Counter()
            example = None
            h1_in_zero_count = 0
            for word in range(1 << len(free)):
                w = dict(given)
                w.update({j: (word >> i) & 1 for i, j in enumerate(free)})
                a = 1
                for j in range(2, 20):
                    a |= w[j]*((a & lower_masks[j]).bit_count() % 2) << j
                if sum((a >> j) & 1 for j in cut) % 2:
                    continue
                if all(w[j] == 0 for j in range(21-size, 20)):
                    continue
                counts[a] += 1
                if w[19] == 0:
                    h1_in_zero_count += 1
                if example is None:
                    example = {'normalizedCoefficientOnes': [j for j in range(1, 20) if (a >> j) & 1],
                               'unitWitnessNormalizedDegrees': [j for j in range(2, 20) if w[j]]}
            result = {'row': row, 'twoAdicType': typ, 'distinguishedRootResidue': eps,
                      'coefficientPatternCount': len(counts), 'markedAssignmentCount': sum(counts.values()),
                      'assignmentsWithH1WitnessInZeroCluster': h1_in_zero_count,
                      'sampleNecessaryResidueAssignment': example}
            require((len(counts), sum(counts.values())) == expected_counts[(row, typ, eps)], 'Cross-prime count mismatch')
            results.append(result)

print(json.dumps({'status': 'PASS', 'integerFactorAndCoefficientIdentities': 'PASS',
                  'originalNormalizationValuationTransport': 'PASS',
                  'valuationGapChecks': gaps, 'distinguishedRootSimplicityAt17': seed_simple,
                  'residueIntersectionResults': results,
                  'scope': 'One full scale/type subcase of row9 is excluded. Rows4/6/7 have additional conditional exact valuation restrictions. No complete p17 row is excluded, and surviving residue assignments are not claimed to lift.'}, indent=2))
