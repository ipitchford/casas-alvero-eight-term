#!/usr/bin/env python3
"""Complete the exact v-lift for four linear root-ratio candidates.

No CAS is used. The two exclusions have explicit Bezout identities; the two
positive controls are checked directly against the defining Hasse formula.
"""
import contextlib
import io
import json
from math import comb

with contextlib.redirect_stdout(io.StringIO()):
    import fast_necessary_filter as poly


def require(ok, message):
    if not ok:
        raise ValueError(message)


def subtract(a, b, p):
    return poly.add(a, poly.scale(b, -1, p), p)


def xgcd(a, b, p):
    old_r, r = a, b
    old_s, s = [1], []
    old_t, t = [], [1]
    while r:
        quotient, remainder = poly.divide(old_r, r, p)
        old_r, r = r, remainder
        old_s, s = s, subtract(old_s, poly.mul(quotient, s, p), p)
        old_t, t = t, subtract(old_t, poly.mul(quotient, t, p), p)
    inverse = pow(old_r[-1], -1, p)
    return [poly.scale(a, inverse, p) for a in [old_r, old_s, old_t]]


def hasse(f, order, x, p):
    return sum(c*comb(e, order)*pow(x, e-order, p)
               for e, c in f.items() if e >= order) % p


records = []
for p, z in [(19, 9), (23, 2), (79, 18), (257, 8)]:
    require(pow(z, p+6, p) == 289 % p, 'Invalid candidate z')
    t = 17*pow(z, -3, p) % p
    require(t*t % p == z and pow(t, p+6, p) == 17 % p,
            'The reconstruction of t failed')
    denominator = z*z*(51-35*z) % p
    require(denominator != 0, 'Forbidden denominator')
    T = 35*(17-z**3)*pow(denominator, -1, p) % p
    require(T != 0, 'The root v would vanish')
    quartic = [-T % p, 0, 0, 0, 1]
    vp = poly.power_mod([0, 1], p, quartic, p)
    relation = poly.add(poly.mul(vp, [35, 0, 0, 0, -35, 0, 34], p), [-34], p)
    remainder = poly.divide(relation, quartic, p)[1]
    G, A, B = xgcd(quartic, remainder, p)
    # Replay the certificate by multiplication, independently of the Euclidean
    # recurrence. This exact identity is the exclusion certificate when G=1.
    require(poly.add(poly.mul(A, quartic, p), poly.mul(B, remainder, p), p) == G,
            'Bezout identity replay failed')
    record = {'prime': p, 'z': z, 't': t, 'T': T,
              'quarticLowFirst': quartic, 'remainderLowFirst': remainder,
              'gcdLowFirst': G, 'bezoutALowFirst': A, 'bezoutBLowFirst': B}
    if len(G) == 1:
        require(p in [79, 257], 'A known example was excluded')
        record['conclusion'] = 'excluded: no marked root v over the algebraic closure'
    else:
        require(len(G) == 2 and p in [19, 23], 'Unexpected residual factor')
        v = -G[0]*pow(G[1], -1, p) % p
        w = t*v % p
        a = -35 % p
        c = 35*pow(v, p, p)*(1-pow(v, 4, p)) % p
        d = 34*pow(v, p+6, p) % p
        f = {p+7: 1, p+3: a, 3: c, 1: d}
        witnesses = {p+3: 1, 3: v, 1: w}
        for order, x in witnesses.items():
            require(hasse(f, 0, x, p) == 0 and hasse(f, order, x, p) == 0,
                    'Direct Hasse witness failed')
        require(hasse(f, 0, 0, p) == 0, 'Root zero is missing')
        # For every other Hasse order the constant coefficient is zero,
        # so zero is a simultaneous root. This covers every required order.
        for order in range(1, p+7):
            if order not in witnesses:
                require(hasse(f, order, 0, p) == 0, 'Off-support order failed')
        record.update({'conclusion': 'explicit nontrivial CA polynomial verified',
                       'v': v, 'w': w, 'a': a, 'c': c, 'd': d,
                       'activeWitnesses': witnesses})
    records.append(record)

print(json.dumps({'status': 'PASS', 'records': records,
                  'scope': 'Completes these linear candidates, conditional on the prior necessary z reduction.'},
                 indent=2))
