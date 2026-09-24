#!/usr/bin/env python3
"""Check the compact characteristic-13 elimination using integer arithmetic.

No CAS required. The root-ratio derivation and finite-field irreducibility
argument are written in MOD13_EXPLANATION.md; this checks their finite inputs.
"""
import json

P = 13


def require(condition, message):
    if not condition:
        raise ValueError(message)


def clean(a):
    return {i: c % P for i, c in a.items() if c % P}


def add(*args):
    out = {}
    for a in args:
        for i, c in a.items():
            out[i] = out.get(i, 0) + c
    return clean(out)


def scale(a, c):
    return clean({i: c*x for i, x in a.items()})


def mul(a, b):
    out = {}
    for i, c in a.items():
        for j, d in b.items():
            out[i+j] = out.get(i+j, 0) + c*d
    return clean(out)


def power(a, n):
    result = {0: 1}
    for _ in range(n):
        result = mul(result, a)
    return result


def shift(a, n):
    return {i+n: c for i, c in a.items()}


def rem_m(a):
    # Reduction by t^19-4, monic.
    out = {}
    for i, c in a.items():
        q, r = divmod(i, 19)
        out[r] = out.get(r, 0) + c*pow(4, q, P)
    return clean(out)


def evaluate(a, x):
    return sum(c*pow(x, i, P) for i, c in a.items()) % P


D = clean({2: 4, 0: -1})
N = clean({2: 4, 15: -4})
R = add(power(clean({9: 1, 8: -1, 0: -1}), 2),
        scale(shift(power(clean({3: -1, 2: 3, 1: -6, 0: 3}), 2), 13), -1))
expected_R = clean({19: -1, 18: -6, 17: 3, 16: 4, 15: -2, 14: -3,
                    13: 4, 9: -2, 8: 2, 0: 1})
require(R == expected_R, 'Expanded quartic-elimination polynomial differs')
Np = [{0: 1}]
Dp = [{0: 1}]
for i in range(19):
    Np.append(rem_m(mul(Np[-1], N)))
    Dp.append(rem_m(mul(Dp[-1], D)))
H = {}
for k, coefficient in R.items():
    H = rem_m(add(H, scale(mul(Np[k], Dp[19-k]), coefficient)))
expected_H = clean({18: 5, 17: -6, 16: -3, 15: 3, 14: -2, 13: -6,
                    11: 1, 10: 3, 8: -1, 7: 1, 6: -1, 5: 3,
                    4: 6, 3: 5, 2: -4, 0: 6})
require(H == expected_H, 'Homogenized remainder differs')
require(evaluate(H, 4) == 8, 'Linear-factor exclusion failed')
Q = {18-k: pow(4, k, P) for k in range(19)}
require(mul(clean({1: 1, 0: -4}), Q) == clean({19: 1, 0: -4}), 'Factorization failed')
require(pow(13, 18, 19) == 1 and pow(13, 9, 19) == 18 and pow(13, 6, 19) == 11,
        'Frobenius-order inputs differ')
require(H[18] == 5 and H[16] != 5*Q[16] % P, 'Irreducible-factor exclusion failed')
require([t for t in range(P) if evaluate(D, t) == 0] == [6, 7], 'Denominator roots differ')
require(pow(6, 19, P) == 7 and pow(7, 19, P) == 6, 'Denominator nonvanishing failed')
require((9+4) % P == 0, 'c=0 branch does not retain the marked H3 root 1')
require(4*10 % P == 1, 'a=0 branch quadratic constant differs')
require(20 % P == 7 and 7 != 1, 'Binomial d-only branch differs')
altered = add(H, {0: 1})
require(altered != expected_H, 'Mutation control failed')
print(json.dumps({
    'status': 'PASS', 'prime': P, 'ratioEquation': 't^19=4',
    'quarticEliminationDegrees': [4, 3], 'Rdegree': max(R), 'Rterms': len(R),
    'Hdegree': max(H), 'Hterms': len(H), 'Hat4': evaluate(H, 4),
    'Hleading': H[18], 'Hcoefficient16': H[16], 'fiveQcoefficient16': 5*Q[16] % P,
    'frobeniusOrder': 18, 'denominatorRoots': [6, 7], 'degenerationArithmetic': 'PASS',
    'mutationControl': 'PASS',
    'scope': 'Finite arithmetic for characteristic-13 emptiness; lifting is a separate proof.'
}, indent=2))
