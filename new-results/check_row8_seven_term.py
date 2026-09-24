#!/usr/bin/env python3
"""Independent small row-8 support census in F17[s]/(s^2-14).

No imports from an earlier checker or producer. This exhausts only 1,216
assignments across seven specified supports, not the full 4^13 census.
"""
from hashlib import sha256
from argparse import ArgumentParser
from itertools import product
from math import comb
from pathlib import Path
import json

P = 17
ZERO, ONE = (0, 0), (1, 0)
DOMAIN = (ZERO, ONE, (8, 9), (8, 8))
SUPPORTS = (
    (2, 3, 4, 10, 12, 19),
    (3, 4, 9, 10, 12, 19),
    (3, 4, 5, 10, 13, 19),
    (3, 4, 10, 12, 15, 19),
    (3, 7, 9, 10, 16, 19),
    (3, 6, 10, 16, 17, 19),
    (3, 4, 10, 13, 18, 19),
)
SEEDS = (
    (0, 0, 16, 0, 0), (14, 0, 16, 0, 3), (14, 8, 16, 12, 0),
    (14, 0, 0, 11, 8), (14, 2, 0, 0, 0), (14, 2, 0, 11, 6),
    (14, 2, 0, 14, 3), (0, 16, 0, 0, 0), (0, 16, 0, 14, 3),
)
VISIBLE_INDICES = (2, 3, 17, 18, 19)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def add(x, y):
    return ((x[0]+y[0]) % P, (x[1]+y[1]) % P)


def neg(x):
    return ((-x[0]) % P, (-x[1]) % P)


def mul(x, y):
    return ((x[0]*y[0]+14*x[1]*y[1]) % P,
            (x[0]*y[1]+x[1]*y[0]) % P)


def power(x, n):
    y = ONE
    while n:
        if n & 1:
            y = mul(y, x)
        x = mul(x, x)
        n //= 2
    return y


need(all((t*t-14) % P for t in range(P)), "field polynomial reducible")
need(len(set(DOMAIN)) == 4, "duplicate root-domain entries")
need(all(power(r, 3) == ONE for r in DOMAIN[1:]), "cube root error")
for r in DOMAIN:
    need(mul(power(r, 17), add(power(r, 3), neg(ONE))) == ZERO,
         "root not on row-8 seed")
need([j for j in range(21) if comb(20, j) % P]
     == [0, 1, 2, 3, 17, 18, 19, 20], "visibility differs")
need(1-comb(20, 3) == -17*67, "divided constant differs")
need(comb(20, 2)-3*comb(20, 3) == -17*190,
     "divided a2 coefficient differs")

parser = ArgumentParser(description=__doc__)
parser.add_argument('--inventory', type=Path,
                    help='Explicit predecessor inventory; otherwise resolve work/package layout.')
args = parser.parse_args()
here = Path(__file__).resolve()
if args.inventory is not None:
    inventory_path = args.inventory
else:
    candidates = (
        here.parent.parent/'evidence/full/support_frontier/inventory.json',
        here.parents[2]/'casas-alvero-full/support_frontier/inventory.json',
    )
    inventory_path = next((p for p in candidates if p.is_file()), None)
    need(inventory_path is not None, 'inventory unavailable; pass --inventory')
inventory = json.loads(inventory_path.read_text())
seven = [tuple(s) for s in inventory['finalSurvivors'] if len(s) == 6]
need(len(seven) == 14 and len(set(seven)) == 14, "seven-term inventory differs")
need(set(SUPPORTS) == {s for s in seven if 3 in s},
     "specified supports do not match all seven containing 3")

records = []
for support in SUPPORTS:
    active = tuple(j for j in range(4, 17) if j in support)
    visited = survivors = 0
    totals = {}
    for choices in product(range(4), repeat=len(active)):
        labels = dict(zip(active, choices))
        a = [ZERO for _ in range(20)]
        a[0], a[3] = ONE, (16, 0)
        for j in range(4, 17):
            rho = DOMAIN[labels[j]] if j in labels else ZERO
            value = ZERO
            for i in range(j):
                value = add(value, mul((comb(j, i) % P, 0),
                            mul(a[i], power(rho, j-i))))
            a[j] = neg(value)
            if j not in active:
                need(a[j] == ZERO, "inactive zero witness did not give zero")
        total = ZERO
        for j in range(4, 17):
            c = comb(20, j)
            need(c % 17 == 0, "invalid divided coefficient")
            total = add(total, mul((c//17 % P, 0), a[j]))
        visited += 1
        totals[str(total)] = totals.get(str(total), 0)+1
        survivors += total == (16, 0)
    need(visited == 4**len(active), "incomplete Cartesian product")
    need(sum(totals.values()) == visited, "histogram misses records")
    need(survivors == 0, "support has a necessary-condition survivor")
    rows = [i for i, seed in enumerate(SEEDS, 1)
            if all(not c or j in support for j, c in zip(VISIBLE_INDICES, seed))]
    records.append({
        'deficiencySupport': list(support), 'activeMiddle': list(active),
        'assignments': visited, 'afterDividedIdentity': survivors,
        'seedRowsAllowedByExactZeroCoefficients': rows,
        'attainedSumCount': len(totals),
        'sumHistogramSha256': sha256(
            json.dumps(totals, sort_keys=True).encode()).hexdigest(),
    })
need(sum(r['assignments'] for r in records) == 1216, "assignment total differs")
expected_rows = [[5, 8], [8], [8], [8], [8], [1, 8], [8, 9]]
need([r['seedRowsAllowedByExactZeroCoefficients'] for r in records] == expected_rows,
     "global row routing differs")
row4_excluded = (2, 4, 10, 12, 18, 19)
row9_combined = (3, 4, 10, 13, 18, 19)
globally_excluded = {tuple(r['deficiencySupport']) for r in records
                     if r['seedRowsAllowedByExactZeroCoefficients'] == [8]}
need(len(globally_excluded) == 4, 'pure row-8 global count differs')
need(next(r for r in records if tuple(r['deficiencySupport']) == row9_combined)
     ['activeMiddle'] == [4, 10, 13], 'existing row-9 case does not match')
globally_excluded.update((row4_excluded, row9_combined))
need(len(globally_excluded) == 6 and globally_excluded <= set(seven),
     'global exclusions do not remove six predecessor entries')
remaining = [list(s) for s in seven if s not in globally_excluded]
need(len(remaining) == 8, 'remaining frontier size differs')
print(json.dumps({
    'status': 'PASS',
    'field': 'F17[s]/(s^2-14)',
    'totalAssignments': 1216,
    'totalDividedIdentitySurvivors': 0,
    'collisionFiltersUsed': False,
    'inputInventorySha256': sha256(inventory_path.read_bytes()).hexdigest(),
    'checkerSha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'supports': records,
    'globallyExcludedWithPriorLocalTheorems': [list(s) for s in sorted(globally_excluded)],
    'remainingSevenTermSupports': remaining,
    'scope': 'Complete row-8 necessary census for seven exact supports; five '
             'global exclusions after stated seed routing and prior row-9 theorem. '
             'Adding the separately proved row-4 global corollary changes 14 to 8.',
}, indent=2))
