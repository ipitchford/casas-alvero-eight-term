#!/usr/bin/env python3
"""Count marked residue assignments pruned by simple-mean cluster collapse.

This finite checker counts occupancy consequences of the separate proof.
It does not independently prove the valued-field cluster-collapse lemma.
"""
from collections import Counter
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def support(mask):
    return [j for j in range(1, 20) if (mask >> j) & 1]


masks = [sum(1 << i for i in range(j) if comb(j, i) % 2) for j in range(20)]
results = []
for typ, prescribed, cut, zero_cluster_size in [
        ('A', {4: 1, 16: 0}, [8, 12, 18], 16),
        ('B', {4: 0, 16: 1}, [2, 12, 18], 4)]:
    free = [j for j in range(2, 20) if j not in prescribed]
    before, after, removed = Counter(), Counter(), Counter()
    for word in range(1 << len(free)):
        w = dict(prescribed)
        w.update({j: (word >> i) & 1 for i, j in enumerate(free)})
        a = 1
        for j in range(2, 20):
            a |= w[j]*((a & masks[j]).bit_count() % 2) << j
        if sum((a >> j) & 1 for j in cut) % 2:
            continue
        before[a] += 1
        normalized_degrees = range(21-zero_cluster_size, 20)
        forbidden = all(w[j] == 0 for j in normalized_degrees)
        (removed if forbidden else after)[a] += 1
    lost_patterns = sorted(set(before)-set(after))
    results.append({'type': typ, 'meanResidueClusterSize': zero_cluster_size,
                    'forbiddenNormalizedWitnessLabels': list(range(21-zero_cluster_size, 20)),
                    'markedAssignmentsRemoved': sum(removed.values()),
                    'coefficientPatternsAffected': len(removed),
                    'coefficientPatternsRemovedEntirely': len(lost_patterns),
                    'fullyRemovedSupports': [support(a) for a in lost_patterns],
                    'markedAssignmentsRemaining': sum(after.values()),
                    'coefficientPatternsRemaining': len(after)})
require([r['markedAssignmentsRemoved'] for r in results] == [4, 4096], 'Wrong occupancy count')
require([r['coefficientPatternsAffected'] for r in results] == [3, 345], 'Wrong affected count')
require(all(r['coefficientPatternsRemovedEntirely'] == 0 for r in results), 'Unexpected coefficient-pattern loss')
print(json.dumps({'status': 'PASS', 'results': results,
                  'totalMarkedAssignmentsRemaining': sum(r['markedAssignmentsRemaining'] for r in results),
                  'totalCoefficientPatternsRemaining': sum(r['coefficientPatternsRemaining'] for r in results),
                  'scope': 'Occupancy pruning uses the proven cluster-collapse lemma plus the characteristic-zero simple-mean theorem. No coefficient residue pattern is entirely removed by this occupancy step.'}, indent=2))
