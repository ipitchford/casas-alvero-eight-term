"""Independent transcription of CLO Theorem 2, arXiv:1208.5404.

Standard-library exact Bareiss determinant plus a separate modular eliminator.
The J entries are coefficient indices at which a_j=0 (not derivative orders).
"""
from itertools import combinations
from math import comb
import json
from pathlib import Path


def delta(indices):
    js = tuple(indices)
    rows = []
    for row, j in enumerate(js):
        rows.append([-1] + [j * comb(j - 2, k - 2) if col <= row else 0
                            for col, k in enumerate(js)])
    rows.append([-1] + [(-1) ** j for j in js])
    return rows


def integer_det(matrix):
    a = [row[:] for row in matrix]
    size = len(a)
    divisor = 1
    sign = 1
    for k in range(size - 1):
        pivot_row = next((r for r in range(k, size) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                if numerator % divisor:
                    raise ArithmeticError("Bareiss division was not exact")
                a[i][j] = numerator // divisor
        for i in range(k + 1, size):
            a[i][k] = 0
        divisor = pivot
    return sign * a[-1][-1]


def modular_det(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    determinant = 1
    for k in range(len(a)):
        pivot_row = next((r for r in range(k, len(a)) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            determinant = -determinant
        pivot = a[k][k]
        determinant = determinant * pivot % p
        inverse = pow(pivot, -1, p)
        for i in range(k + 1, len(a)):
            factor = a[i][k] * inverse % p
            for j in range(k, len(a)):
                a[i][j] = (a[i][j] - factor * a[k][j]) % p
    return determinant % p


def check():
    published = [(3, 8), (5, 6), (6, 8), (6, 9), (7, 9)]
    degree12 = [pair for pair in combinations(range(2, 11), 2)
                if modular_det(delta(pair), 11) == 0]
    if degree12 != published:
        raise ValueError((degree12, published))
    rows = []
    for pair in combinations(range(2, 19), 2):
        js = [j for j in range(2, 19) if j not in pair]
        matrix = delta(js)
        exact = integer_det(matrix)
        residue = modular_det(matrix, 19)
        if exact % 19 != residue:
            raise ValueError((pair, exact, residue))
        rows.append({"support": [*pair, 19], "zero_indices": js,
                     "determinant": str(exact), "residue_mod_19": residue})
    survivors = [r["support"] for r in rows if r["residue_mod_19"] == 0]
    return {"source": "CLO Theorem 2; https://arxiv.org/html/1208.5404",
            "degree12_published_pairs_reproduced": [list(x) for x in degree12],
            "degree20_supports_checked": len(rows),
            "independent_determinants_agree": True,
            "degree20_surviving_supports": survivors,
            "records": rows}


if __name__ == "__main__":
    result = check()
    destination = Path(__file__).with_name("prior-art-determinant-results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "records"}, indent=2))
