#!/usr/bin/env python3
"""Independent integer-list reconstruction of PROOF.md equations (2),(14)."""
from functools import reduce
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def scale(a, c):
    return trim([c*x for x in a])


def add(a, b):
    c = [0]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def mul(a, b):
    if not a or not b:
        return []
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def power(a, n):
    answer = [1]
    for _ in range(n):
        answer = mul(answer, a)
    return answer


def require(ok, message):
    if not ok:
        raise ValueError(message)


P = [35*17, 0, 0, -35]
Q = [0, 0, 51, -35]
R = [-35*17**5]+[0]*17+[35]
S = [-35*17**5]+[0]*5+[51*17**3]
A = scale(P, 34)
B = scale(add(Q, scale(P, -1)), 35)
E = add(add(mul(power(A, 4), power(P, 2)),
            scale(mul(mul(power(A, 2), power(B, 2)), mul(P, Q)), 6)),
        mul(power(B, 4), power(Q, 2)))
O = scale(mul(mul(A, B), add(mul(power(A, 2), P), mul(power(B, 2), Q))), 4)
raw = add(power(add(mul(R, E), scale(mul(S, power(Q, 6)), -34**4)), 2),
          scale(mul(mul(P, Q), mul(power(R, 2), power(O, 2))), -1))
content = reduce(gcd, raw)
require(content == 17**8, 'Unexpected numerical content')
H = [x//(17**8) for x in raw]
require(len(H)-1 == 72 and reduce(gcd, H) == 1, 'Degree or primitivity failed')
source = Path(__file__).resolve().parent.parent/'fixed-polynomial.json'
saved = list(reversed(json.loads(source.read_text())['H_coefficients_high_first']))
require(H == saved, 'The displayed formula differs from the saved H')

# The denominator before content cancellation is S^2 Q^12. The denominator
# in equation (14) is z^24 (35z-51)^12 (3z^6-595)^2.
denominator14 = mul([0]*24+[1], mul(power([-51, 35], 12),
                                   power([-595]+[0]*5+[3], 2)))
require(mul(power(S, 2), power(Q, 12)) == scale(denominator14, 17**8),
        'Equation (14) denominator identity failed')

print(json.dumps({'status': 'PASS', 'Hdegree': len(H)-1, 'rawContent': content,
                  'Hprimitive': True, 'savedHMatches': True,
                  'equation14DenominatorIdentity': True,
                  'sourceSha256': sha256(source.read_bytes()).hexdigest(),
                  'scope': 'Independent standard-library integer reconstruction of equations (2) and (14); normalization and necessity are hand-audited separately.'}, indent=2))
