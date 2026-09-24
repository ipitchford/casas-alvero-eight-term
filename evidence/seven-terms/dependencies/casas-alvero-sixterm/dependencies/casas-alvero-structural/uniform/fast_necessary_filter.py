#!/usr/bin/env python3
"""Bounded degree-72 necessary Frobenius test; pure integer arithmetic.

Passing does not establish a CA polynomial. A constant admissible gcd excludes
the normalized a!=0 case, conditional on the separately audited H derivation.
"""
from pathlib import Path
import hashlib
import json


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def clean(a, p):
    return trim([c % p for c in a])


def add(a, b, p):
    out = [0]*max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    return clean(out, p)


def scale(a, c, p):
    return clean([x*c for x in a], p)


def mul(a, b, p):
    if not a or not b:
        return []
    out = [0]*(len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] += c*d
    return clean(out, p)


def divide(a, b, p):
    a = clean(list(a), p)
    b = clean(list(b), p)
    if not b:
        raise ValueError('Division by zero polynomial')
    quotient = [0]*max(0, len(a)-len(b)+1)
    inverse = pow(b[-1], -1, p)
    while a and len(a) >= len(b):
        shift = len(a)-len(b)
        factor = a[-1]*inverse % p
        quotient[shift] = factor
        for j, c in enumerate(b):
            a[shift+j] = (a[shift+j]-factor*c) % p
        trim(a)
    return trim(quotient), a


def gcd(a, b, p):
    while b:
        a, b = b, divide(a, b, p)[1]
    return scale(a, pow(a[-1], -1, p), p) if a else []


def power_mod(a, n, modulus, p):
    result = [1]
    while n:
        if n & 1:
            result = divide(mul(result, a, p), modulus, p)[1]
        n //= 2
        if n:
            a = divide(mul(a, a, p), modulus, p)[1]
    return result


root = Path(__file__).resolve().parent.parent
source = root/'fixed-polynomial.json'
integer_H = list(reversed(json.loads(source.read_text())['H_coefficients_high_first']))
records = []
for p in [13, 19, 23, 79, 137, 257, 823, 1973, 87169343]:
    H = clean(list(integer_H), p)
    if not H:
        raise ValueError(f'H vanished identically modulo {p}')
    frobenius_remainder = add(power_mod([0, 1], p+6, H, p), [-289], p)
    G = gcd(H, frobenius_remainder, p)
    denominator = mul(mul([0, 1], [51, -35], p), [-595, 0, 0, 0, 0, 0, 3], p)
    forbidden = gcd(G, denominator, p)
    admissible, remainder = divide(G, forbidden, p)
    if remainder:
        raise ValueError('Denominator factor division was not exact')
    # z^(p+6)-289 is squarefree for these primes (derivative 6*z^(p+5)).
    # Therefore one division removes every inadmissible root, not only one layer.
    if gcd(admissible, denominator, p) != [1]:
        raise ValueError('Inadmissible denominator roots remain')
    if p in [19, 23, 87169343] and len(admissible) < 2:
        raise ValueError('The necessary test wrongly excludes a known example')
    records.append({'prime': p, 'Hdegree': len(H)-1, 'rawGcdDegree': len(G)-1,
                    'removedDenominatorDegree': len(forbidden)-1,
                    'admissibleDegree': len(admissible)-1,
                    'admissibleCoefficientsLowFirst': admissible,
                    'disposition': 'excluded a!=0 branch' if len(admissible) == 1
                                   else 'necessary test passes; existence not established'})
print(json.dumps({'status': 'PASS', 'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                  'test': 'gcd(H,z^(p+6)-289), deleting roots of z*(51-35z)*(3z^6-595)',
                  'records': records,
                  'scope': 'Necessary conditions only, using the separately derived fixed polynomial H.'}, indent=2))
