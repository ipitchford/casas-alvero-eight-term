#!/usr/bin/env python3
"""Full normalized coefficient/witness residue enumeration for degree20 at2.

This classifies only the residue incidence equations. It neither constructs
characteristic-zero lifts nor assumes coefficient or witness differences lie
in2O. All coefficients of the original polynomial remain allowed.
"""
from collections import Counter
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def v2(n):
    require(n != 0, 'Infinite valuation requested')
    return (abs(n) & -abs(n)).bit_length()-1


def hasse(f, k, r, modulus):
    return sum(c*comb(e, k)*pow(r, e-k, modulus)
               for e, c in f.items() if e >= k) % modulus


visible = [j for j in range(21) if comb(20, j) % 2]
require(visible == [0, 4, 16, 20], 'Lucas visibility mismatch')
seeds = []
for active in [16, 4]:
    f = {20: 1, active: 1}
    witnesses = {j: (1 if j == active else 0) for j in range(1, 20)}
    for j, r in witnesses.items():
        require(hasse(f, 0, r, 2) == hasse(f, j, r, 2) == 0,
                'The binomial seed does not satisfy a Hasse condition')
    seeds.append({'nonleadingExponent': active, 'HasseWitnesses': witnesses})

# For a normalized derivative of degree j, G_j=X^j+sum binom(j,i)a_iX^(j-i).
# Its common witness reduces to0 or1. At0 it forces a_j=0; at1 it forces
# a_j to the Pascal sum of the preceding normalized coefficients.
lower_masks = [sum(1 << i for i in range(j) if comb(j, i) % 2) for j in range(20)]
branches = []
for label, prescribed in [('A_16plus4', {4: 1, 16: 0}),
                           ('B_4plus16', {4: 0, 16: 1})]:
    free = [j for j in range(2, 20) if j not in prescribed]
    require(len(free) == 16, 'Wrong number of free residue witness labels')
    counts = Counter()
    for word in range(1 << len(free)):
        witnesses = dict(prescribed)
        witnesses.update({j: (word >> k) & 1 for k, j in enumerate(free)})
        mask = 1  # a0=1 and a1=0; centered degree-one witness is exactly zero.
        for j in range(2, 20):
            preceding_sum = (mask & lower_masks[j]).bit_count() % 2
            aj = witnesses[j]*preceding_sum
            mask |= aj << j
            value = aj if witnesses[j] == 0 else preceding_sum ^ aj
            require(value == 0, 'A normalized derivative residue is nonzero')
        require(((mask >> 4) & 1) == prescribed[4]
                and ((mask >> 16) & 1) == prescribed[16], 'Visible coefficients mismatch')
        counts[mask] += 1
    expected = 873 if label.startswith('A') else 1128
    require(len(counts) == expected and sum(counts.values()) == 65536, 'Enumeration count differs')
    fixed = {str(j): (next(iter(counts)) >> j) & 1
             for j in range(1, 20) if len({(a >> j) & 1 for a in counts}) == 1}
    branches.append({'type': label, 'normalizedCoefficientPatternCount': len(counts),
                     'markedResidueAssignmentCount': sum(counts.values()),
                     'fixedNormalizedResidues': fixed,
                     'patterns': [{'ones': [j for j in range(1, 20) if (a >> j) & 1],
                                   'markedAssignmentCount': count}
                                  for a, count in sorted(counts.items())]})

# Exact approximate incidence points show that low integer precision by itself
# cannot remove these residue charts. They are NOT characteristic-zero points.
approximate = []
for label, a, modulus in [('A_mod16', {4: -1, 19: 3875}, 16),
                         ('B_mod4', {16: -1}, 4)]:
    ordinary = {20: 1}
    ordinary.update({20-j: comb(20, j)*c for j, c in a.items()})
    for j in range(1, 20):
        r = 1 if j in a else 0
        normalized_value = (pow(r, j, modulus)
                            +sum(comb(j, i)*c*pow(r, j-i, modulus) for i, c in a.items() if i <= j)) % modulus
        require(normalized_value == 0 and hasse(ordinary, 0, r, modulus) == 0,
                'Approximate normalized incidence point failed')
    exact_defect = sum(ordinary.values())
    approximate.append({'label': label, 'modulus': modulus,
                         'normalizedNonzeroCoefficients': a, 'fAtOne': exact_defect,
                         'fAtOneValuation2': v2(exact_defect)})

# The power-of-two normalized derivative equation at1 and f(1)=0 force actual
# divisibility by2 of the other visible normalized coefficient. Check all
# coefficients of the elimination identity, including the odd pivot.
elimination = []
for m, other in [(4, 16), (16, 4)]:
    pivot = comb(20, other)-(comb(20, m)*comb(m, other) if other <= m else 0)
    row = {j: comb(20, j)-(comb(20, m)*comb(m, j) if j <= m else 0)
           for j in range(2, 20) if j != m}
    require(pivot % 2 == 1 and all(c % 2 == 0 for j, c in row.items() if j != other),
            'Integral visible-coefficient sharpening failed')
    require((1-comb(20, m)) % 2 == 0, 'Elimination constant is odd')
    elimination.append({'normalizedDerivativeDegree': m, 'otherVisibleDeficiency': other,
                        'oddPivot': pivot, 'constant': 1-comb(20, m),
                        'allOtherLinearCoefficientsEven': True})

print(json.dumps({'status': 'PASS', 'LucasVisibleDeficiencies': visible,
                  'seeds': seeds, 'branches': branches,
                  'totalNormalizedCoefficientPatterns': sum(b['normalizedCoefficientPatternCount'] for b in branches),
                  'totalMarkedResidueAssignments': sum(b['markedResidueAssignmentCount'] for b in branches),
                  'integralSharpeningIdentities': elimination,
                  'approximateIncidencePoints': approximate,
                  'scope': 'Complete normalized residue incidence classification, with genuine integral-coefficient congruence consequences. No characteristic-zero lift or full exclusion is established.'}, indent=2))
