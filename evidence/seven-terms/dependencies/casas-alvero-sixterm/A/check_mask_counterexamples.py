#!/usr/bin/env python3
"""Direct complete Hasse checks for two closed-mask counterexamples."""
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def hasse_value(f, k, x, p):
    return sum(c*comb(e, k)*pow(x, e-k, p)
               for e, c in f.items() if e >= k) % p


def check(p, coefficients, active_witnesses):
    f = {20: 1}
    f.update({e: c % p for e, c in coefficients.items() if c % p})
    require(set(active_witnesses) == set(f)-{20}, 'Active-order coverage failed')
    records = []
    for k in range(1, 20):
        x = active_witnesses.get(k, 0)
        require(hasse_value(f, 0, x, p) == 0, f'Polynomial witness failed: p={p}, k={k}')
        require(hasse_value(f, k, x, p) == 0, f'Hasse witness failed: p={p}, k={k}')
        records.append({'order': k, 'commonRoot': x})
    # h(0)=0, whereas a monic pure 20th power rooted at zero must equal X^20.
    require(hasse_value(f, 0, 0, p) == 0 and len(f) > 1, 'Example is trivial')
    corrupted = f.copy()
    corrupted[1] = (corrupted[1]+1) % p
    require(hasse_value(corrupted, 0, 1, p) != 0, 'Mutation control did not detect corruption')
    return {'prime': p, 'degree': 20, 'coefficients': f,
            'allNineteenHasseWitnesses': records, 'status': 'PASS'}


records = [check(11, {17: 4, 16: 0, 2: 5, 1: 1}, {17: 1, 2: 5, 1: 1}),
           check(13, {17: 4, 16: 1, 2: 4, 1: 3}, {17: 1, 16: 1, 2: 1, 1: 7})]
print(json.dumps({'status': 'PASS', 'records': records,
                  'scope': 'These prove that the closed characteristic-11 and characteristic-13 masks admit nontrivial CA polynomials. They do not give characteristic-zero counterexamples.'}, indent=2))
