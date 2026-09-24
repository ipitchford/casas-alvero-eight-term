#!/usr/bin/env python3
"""Exact small-prime coefficient search; absence is not closure exclusion."""
import json
from math import comb


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def rem(a, b, p):
    a = a[:]
    while a and len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, p) % p
        for j, x in enumerate(b):
            a[k+j] = (a[k+j]-c*x) % p
        trim(a)
    return a


def gcd(a, b, p):
    while b:
        a, b = b, rem(a, b, p)
    return [(x*pow(a[-1], -1, p)) % p for x in a] if a else []


def value(a, x, p):
    return sum(c*pow(x, j, p) for j, c in enumerate(a)) % p


def check(p, a, b, c, d):
    f = [0]*21
    for e, coefficient in [(20, 1), (17, a), (16, b), (2, c), (1, d)]:
        f[e] = coefficient % p
    factors, rational = {}, {}
    for k in [17, 16, 2, 1]:
        if not f[k]:
            continue
        hk = trim([comb(e, k)*f[e] % p for e in range(k, 21)])
        g = gcd(f, hk, p)
        if len(g) < 2:
            return None
        factors[k] = g
        rational[k] = [x for x in range(p) if value(g, x, p) == 0]
    return {'p': p, 'a': a % p, 'b': b % p, 'c': c % p, 'd': d % p,
            'commonFactorsLowFirst': factors, 'rationalCommonRoots': rational}


records = []
for p in [11, 13]:
    candidates = []
    a = -comb(20, 17) % p
    for b in range(p):
        for c in range(p):
            candidates.append((a, b, c, -1-a-b-c))
    b = -comb(20, 16) % p
    for c in range(p):
        candidates.append((0, b, c, -1-b-c))
    c = -comb(20, 2) % p
    candidates.append((0, 0, c, -1-c))
    # If only d survives, normalization at an H1 common root gives d=-20,
    # and h(1)=0 would additionally require d=-1, impossible at 11 or 13.
    examples = [r for coefficients in candidates
                if (r := check(p, *coefficients)) is not None]
    records.append({'prime': p, 'normalizedCoefficientChoicesTested': len(candidates),
                    'examples': examples})
print(json.dumps({'status': 'completed', 'records': records,
                  'scope': 'Exhausts prime-field coefficients after normalizing a highest active derivative common root to 1. No absence claim over algebraic-closure coefficients.'}, indent=2))
