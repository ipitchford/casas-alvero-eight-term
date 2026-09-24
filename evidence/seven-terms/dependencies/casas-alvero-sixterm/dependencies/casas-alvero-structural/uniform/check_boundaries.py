#!/usr/bin/env python3
"""Exact finite checks for STRUCTURAL_BOUNDARIES.md, standard library only."""
from math import comb, isqrt
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def value(f, root, p):
    return sum(c*pow(root, exponent, p) for exponent, c in f.items()) % p


def hasse_value(f, order, root, p):
    return sum(c*(comb(exponent, order) % p)*pow(root, exponent-order, p)
               for exponent, c in f.items() if exponent >= order) % p


def check(p, a, c, d, witnesses, label):
    require(prime(p) and p > 7, 'Invalid prime')
    n = p+7
    f = {e: coefficient % p for e, coefficient in
         [(n, 1), (p+3, a), (3, c), (1, d)] if coefficient % p}
    active = {e for e in f if 0 < e < n}
    require(active == set(witnesses), 'Active Hasse-order coverage incomplete')
    for order, root in witnesses.items():
        require(value(f, root, p) == 0, 'Witness is not a polynomial root')
        require(hasse_value(f, order, root, p) == 0, 'Witness is not a Hasse root')
    # All unlisted derivative orders have zero constant term, so share root 0.
    require(value(f, 0, p) == 0 and len(f) > 1, 'No nontrivial rooted polynomial')
    return {'label': label, 'prime': p, 'degree': n,
            'coefficients': {str(e): coefficient for e, coefficient in f.items()},
            'activeWitnesses': witnesses, 'offSupportWitness': 0, 'status': 'PASS'}


C = 3**7*17**4-35**7
A = 51**7-17**2*35**7
require(C == -(2**5)*23*87169343, 'c-zero integer factorization failed')
require(A == -(2**4)*(17**2)*1229*3114019, 'a-zero integer factorization failed')
for p in [23, 87169343, 1229, 3114019]:
    require(prime(p), 'A claimed prime factor is composite')

records = []
for p in [23, 87169343]:
    w = (35**2 * pow(9*17, -1, p)) % p
    records.append(check(p, -35, 0, 34, {p+3: 1, 1: w}, 'c=0 boundary'))
for p in [1229, 3114019]:
    w = (17*pow(35, 3, p)*pow(pow(51, 3, p), -1, p)) % p
    records.append(check(p, 0, -35, 34, {3: 1, 1: w}, 'a=0 boundary'))
records.append(check(19, 3, 14, 1, {22: 1, 3: 2, 1: 13}, 'all coefficients nonzero'))
records.append(check(17, -1, 0, 0, {20: 1}, 'p=17 a-only example'))
records.append(check(17, 0, -1, 0, {3: 1}, 'p=17 c-only example'))

# Targeted corruption control: changing the linear coefficient destroys root 1.
require(value({26: 1, 22: 3, 3: 14, 1: 2}, 1, 19) != 0,
        'Corruption control did not fail')
print(json.dumps({'status': 'PASS', 'cZeroObstructionInteger': C,
                  'aZeroObstructionInteger': A, 'examples': records,
                  'mutationControl': 'PASS',
                  'scope': 'Exact finite witnesses and integer factors; necessity is a written proof.'}, indent=2))
