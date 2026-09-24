"""Replay literature-derived support filters and their Massri binary masks.

No old audit artifact is imported or modified. Arithmetic is standard-library.
This checks finite bookkeeping; the characteristic-zero inference is in REPORT.md.
"""
import json
from itertools import combinations
from math import comb
from pathlib import Path


def determinant_mod19(js):
    rows = [[-1] + [j * comb(j - 2, k - 2) if s <= r else 0
                       for s, k in enumerate(js)]
            for r, j in enumerate(js)]
    rows.append([-1] + [(-1) ** j for j in js])
    a = [[x % 19 for x in row] for row in rows]
    result = 1
    for k in range(len(a)):
        pivot_row = next((r for r in range(k, len(a)) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            result = -result
        pivot = a[k][k]
        result = result * pivot % 19
        inverse = pow(pivot, -1, 19)
        for r in range(k + 1, len(a)):
            factor = a[r][k] * inverse % 19
            for s in range(k, len(a)):
                a[r][s] = (a[r][s] - factor * a[k][s]) % 19
    return result


def goncharoff_value_at_one(nodes):
    n = len(nodes)
    coefficients = [0] * n + [1]
    for i in range(n - 1, -1, -1):
        coefficients[i] = -sum(comb(j, i) * coefficients[j]
                               * nodes[i] ** (j - i)
                               for j in range(i + 1, n + 1))
    for i, y in enumerate(nodes):
        if sum(comb(j, i) * coefficients[j] * y ** (j - i)
               for j in range(i, n + 1)) != 0:
            raise ArithmeticError("Goncharoff derivative condition failed")
    return sum(coefficients)


def valuation19(integer):
    if integer == 0:
        return None
    exponent = 0
    while integer % 19 == 0:
        integer //= 19
        exponent += 1
    return exponent


def support_record(support):
    support = set(support)
    active = {20 - m for m in support}
    nodes = [0 if i == 0 or i in active else 1 for i in range(20)]
    g1 = goncharoff_value_at_one(nodes)
    label_of = {1: 0}
    labels = []
    next_label = 1
    for derivative in range(1, 20):
        root_name = derivative if derivative in active else "mean"
        if root_name not in label_of:
            label_of[root_name] = next_label
            next_label += 1
        labels.append(label_of[root_name])
    return {
        "support": sorted(support),
        "active_derivative_orders": sorted(active),
        "clo_determinant_mod19": determinant_mod19(sorted(set(range(2, 19)) - support)),
        "passes_massri_pairs": bool(support & {10, 15}) and bool(support & {5, 10}),
        "massri_binary_nodes_y0_through_y19": nodes,
        "integer_G_at_1": str(g1),
        "v19_G_at_1": valuation19(g1),
        "chosen_distinct_witness_scenario": labels,
        "chosen_witness_type": max(labels),
    }


def run():
    output = []
    for size in (3, 4):
        basic = []
        for rest in combinations(range(2, 19), size - 1):
            support = set(rest) | {19}
            if support & {4, 16} and support & {5, 10, 15}:
                basic.append(support_record(support))
        clo = [r for r in basic if r["clo_determinant_mod19"] == 0]
        pairs = [r for r in basic if r["passes_massri_pairs"]]
        both = [r for r in clo if r["passes_massri_pairs"]]
        output.append({"support_size": size, "clo_prop15_count": len(basic),
                       "clo_and_massri_pairs_count": len(pairs),
                       "clo_determinant_survivors": clo,
                       "all_filters_survivors": both})
    expected = [[], [[4, 10, 17, 19], [5, 15, 16, 19]]]
    for item, targets in zip(output, expected):
        actual = [r["support"] for r in item["all_filters_survivors"]]
        if actual != targets:
            raise ArithmeticError((actual, targets))
    return output


if __name__ == "__main__":
    result = run()
    Path(__file__).with_name("support-overlap-results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    for item in result:
        print(json.dumps({k: v for k, v in item.items()
                          if k != "clo_determinant_survivors"}))
