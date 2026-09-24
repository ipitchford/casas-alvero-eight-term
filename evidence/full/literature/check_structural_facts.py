#!/usr/bin/env python3
"""Small independent exact checks supporting REPORT.md; not a CA proof."""
from math import comb
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def evaluate_hasse(f, k, x, p):
    return sum(c*comb(e, k)*x**(e-k)
               for e, c in f.items() if e >= k) % p


records = []
for f in ({5: 1, 4: 1}, {20: 1, 16: 1}, {20: 1, 4: 1}):
    n = max(f)
    witnesses = {}
    for k in range(1, n):
        roots = [r for r in (0, 1) if evaluate_hasse(f, 0, r, 2) == 0
                 and evaluate_hasse(f, k, r, 2) == 0]
        require(bool(roots), f"missing Hasse witness at degree {n}, order {k}")
        witnesses[k] = roots
    require(evaluate_hasse(f, 0, 0, 2) == evaluate_hasse(f, 0, 1, 2) == 0,
            "seed does not have two distinct roots")
    records.append({"coefficients": f, "hasse_witnesses": witnesses})

visible = [m for m in range(1, 20) if comb(20, m) % 2]
require(visible == [4, 16], "incorrect 2-adic visible indices")
require([(a, b) for a in range(2) for b in range(2)
         if (1+a+b) % 2 == 0 and (a*b) % 2 == 0] == [(0, 1), (1, 0)],
        "incorrect two-chart equations")

# Translation X -> X+1 exchanges the two degree-20 seeds.
translated = [sum(c*comb(e, k) for e, c in {20: 1, 16: 1}.items() if e >= k) % 2
              for k in range(21)]
require({k: c for k, c in enumerate(translated) if c} == {20: 1, 4: 1},
        "seed translation fails")

n = 20
D = (n*n-3*n+4)//2
columns = comb(n*(n-1)//2, n-2)
require(D == 172 and columns == 7083408064081415263479975,
        "Macaulay dimensions fail")
print(json.dumps({"status": "PASS", "visible_deficiencies": visible,
                  "characteristic_two_seeds": records,
                  "macaulay_degree": D, "macaulay_columns": columns,
                  "raw_root_assignments": n**(n-1),
                  "scope": "seed identities and matrix-size arithmetic only"}, indent=2))
