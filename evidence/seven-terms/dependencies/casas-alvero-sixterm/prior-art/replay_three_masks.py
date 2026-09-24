"""Replay only the three authorized supports against Massri's binary-mask test.

Standard-library integer arithmetic, with explicit checks active under -O.
This is a source-implication check, not a CA nonexistence certificate.
"""
import json
from math import comb
from pathlib import Path


def goncharoff(nodes):
    n = len(nodes)
    a = [0] * n + [1]
    for i in range(n - 1, -1, -1):
        a[i] = -sum(comb(j, i) * a[j] * nodes[i] ** (j - i)
                    for j in range(i + 1, n + 1))
    for i, y in enumerate(nodes):
        if sum(comb(j, i) * a[j] * y ** (j - i)
               for j in range(i, n + 1)):
            raise RuntimeError(f'Goncharoff condition {i} failed')
    return a


def v19(value):
    if not value:
        return None
    power = 0
    while value % 19 == 0:
        value //= 19
        power += 1
    return power


def main():
    definitions = {'A': [3, 4, 10, 18, 19],
                   'B': [3, 10, 16, 17, 19],
                   'C': [4, 5, 10, 17, 19]}
    results = []
    for label, support in definitions.items():
        active = {20 - m for m in support}
        nodes = [0 if i == 0 or i in active else 1 for i in range(20)]
        coefficients = goncharoff(nodes)
        value = sum(coefficients)
        mapping, scenario = {}, []
        for i in range(1, 20):
            witness = i if i in active else 'mean'
            if witness not in mapping:
                mapping[witness] = len(mapping)
            scenario.append(mapping[witness])
        pair_failures = [list(pair) for pair in ((4, 16), (5, 10), (10, 15))
                         if all(nodes[i] == 1 for i in pair)]
        results.append(dict(label=label, deficiencies=support,
                            active_derivative_orders=sorted(active),
                            binary_nodes=nodes, integer_G_at_1=str(value),
                            v19=v19(value), excluded_by_corollary_7_3=v19(value) == 1,
                            forbidden_mean_pairs=pair_failures,
                            chosen_distinct_witness_scenario=scenario,
                            chosen_type=max(scenario),
                            warning='Matching witness pattern, not necessarily canonical minimal type.'))
    if any(r['excluded_by_corollary_7_3'] or r['forbidden_mean_pairs'] for r in results):
        raise RuntimeError('Potential prior-art collision: inspect results before relying on target frontier')
    destination = Path(__file__).with_name('three-mask-results.json')
    destination.write_text(json.dumps({'scope': 'Only supports A, B, C', 'results': results}, indent=2) + '\n')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
