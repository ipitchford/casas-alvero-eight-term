#!/usr/bin/env python3
"""Exact necessary root-ratio exclusions for every prime 7<p<10000.

This directly uses H modulo p; it neither reads nor relies on the large integer
resultant. The v-lift and coefficient boundaries are checked separately.
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
from time import monotonic

with contextlib.redirect_stdout(io.StringIO()):
    import fast_necessary_filter as poly


def primes_below(n):
    sieve = bytearray(b'\x01')*n
    sieve[0:2] = b'\x00\x00'
    for p in range(2, n):
        if sieve[p]:
            yield p
            for j in range(p*p, n, p):
                sieve[j] = 0


started = monotonic()
source = Path(__file__).resolve().parent.parent/'fixed-polynomial.json'
integer_H = list(reversed(json.loads(source.read_text())['H_coefficients_high_first']))
excluded, survivors, all_primes = [], [], []
for p in primes_below(10000):
    if p <= 7:
        continue
    all_primes.append(p)
    if p == 17:
        continue
    H = poly.clean(list(integer_H), p)
    if not H or len(H) == 1:
        raise ValueError(f'Unexpected degeneration of H at {p}')
    power_relation = poly.add(poly.power_mod([0, 1], p+6, H, p), [-289], p)
    G = poly.gcd(H, power_relation, p)
    denominator = poly.mul(poly.mul([0, 1], [51, -35], p),
                           [-595, 0, 0, 0, 0, 0, 3], p)
    forbidden = poly.gcd(G, denominator, p)
    admissible, remainder = poly.divide(G, forbidden, p)
    if remainder or poly.gcd(admissible, denominator, p) != [1]:
        raise ValueError(f'Denominator deletion failed at {p}')
    if len(admissible) == 1:
        excluded.append(p)
    else:
        survivors.append({'prime': p, 'gcdLowFirst': admissible})

expected = [{'prime': 19, 'gcdLowFirst': [10, 1]},
            {'prime': 23, 'gcdLowFirst': [21, 1]},
            {'prime': 79, 'gcdLowFirst': [61, 1]},
            {'prime': 257, 'gcdLowFirst': [249, 1]}]
if len(all_primes) != 1225 or survivors != expected:
    raise ValueError(f'Unexpected range result: count={len(all_primes)}, survivors={survivors}')

print(json.dumps({'status': 'PASS', 'range': '7<p<10000',
                  'primeCount': len(all_primes), 'testedNormalizedBranchCount': len(all_primes)-1,
                  'separateCharacteristic17Case': True, 'excludedNormalizedBranchCount': len(excluded),
                  'excludedNormalizedBranchPrimes': excluded, 'survivingNormalizedBranchFactors': survivors,
                  'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                  'elapsedSeconds': round(monotonic()-started, 3),
                  'scope': 'Exact bounded necessary-gcd test. Combining the separate v-lift and boundary proofs gives nontrivial members exactly at p=17,19,23,1229 in this range.',
                  'usesIntegerResultant': False}, indent=2))
