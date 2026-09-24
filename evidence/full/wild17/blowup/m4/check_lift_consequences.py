#!/usr/bin/env python3
"""Exact auxiliary arithmetic for LIFT_CONSEQUENCES.md; no lift search."""
from fractions import Fraction
from math import comb
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def trim(a):
    a = [v % 17 for v in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*v for v in a])


def mul(a, b):
    out = [0]*(max(0, len(a)+len(b)-1))
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divmodp(a, b):
    a, b = trim(a), trim(b)
    require(bool(b), 'division by zero')
    q = [0]*max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        d = len(a)-len(b)
        c = a[-1]*pow(b[-1], -1, 17) % 17
        q[d] = c
        for j, x in enumerate(b):
            a[j+d] -= c*x
        a = trim(a)
    return trim(q), a


def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s, old_t, t = [1], [], [], [1]
    while r:
        q, new_r = divmodp(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, add(old_s, scale(mul(q, s), -1))
        old_t, t = t, add(old_t, scale(mul(q, t), -1))
    inverse = pow(old_r[-1], -1, 17)
    return scale(old_r, inverse), scale(old_s, inverse), scale(old_t, inverse)


# This identity certifies CA4 in characteristic17 after the stated normalization.
quartic = [0, 5, -6, 0, 1]
derivative = [5, -12, 0, 4]
gcd, bezout_f, bezout_df = extended_gcd(quartic, derivative)
require(gcd == [1], 'the normalized quartic retains a common first root')
require(add(mul(bezout_f, quartic), mul(bezout_df, derivative)) == [1],
        'quartic Bezout identity failed')

# Integer coefficient identities in f-X^17 Q_T and in f(1)/17.
require(comb(20, 2)-3 == 17*11, 'Q_T linear coefficient differs')
require(comb(20, 3)-1 == 17*67, 'Q_T constant coefficient differs')
require(3*comb(20, 3)-3 == 17*201, 'Q_T T coefficient differs')
require(1-comb(20, 3) == -17*67, 'divided constant differs')
require(comb(20, 2)-3*comb(20, 3) == -17*190, 'divided T coefficient differs')
require(all(comb(20, j) % 17 == 0 for j in range(4, 17)),
        'an ordinary middle coefficient is not divisible by17')
require(comb(17, 16)//17 == 1 and comb(20, 17) % 17 == 1,
        'first-correction H3 coefficient differs')
require(all((z*z+z+1) % 17 for z in range(17)), 'cube roots are not in the quadratic extension')

delta = Fraction(1, 13)
require(16*delta-1 == 3*delta, 'a19 divided valuation differs')
require(2*delta < 3*delta < 4*delta < 1, 'power-series separation fails')
# Valuations of unramified coefficients are nonnegative integers. The constant
# has valuation>=1. No term except the linear one can be as small as 2delta.
require(min(Fraction(1), 4*delta) == 4*delta, 'nonunit-linear bound differs')
require(min(Fraction(1), 1+2*delta, 4*delta) > 3*delta,
        'next-lift nonunit case lacks a strict contradiction')

# The first correction by itself has a survivor for every residue-linked
# linear functional: gamma=0 and all z_j=0 annihilate it identically.
u, v = 0, 12
b, c = 6*u*u % 17, (4*v**3-12*u*u*v) % 17
g = [0]*18
g[1], g[2], g[4], g[17] = c, b, 16, 1
evaluate = lambda f, x: sum(a*pow(x, i, 17) for i, a in enumerate(f)) % 17
require(pow(v, 13, 17) == 14 and b == 0 and c == 10, 'control model differs')
require(evaluate(g, 0) == evaluate(g, v) == 0 and c != 0,
        'control mean is not simple')
for k, witness in [(1, v), (2, 0), (3, 0)]:
    H = [comb(i, k)*g[i] % 17 for i in range(k, len(g))]
    require(evaluate(H, witness) == 0, 'control Hasse witness fails')

print(json.dumps({'status': 'PASS',
                  'quarticBezout': {'coefficientOnFAscending': bezout_f,
                                     'coefficientOnH1Ascending': bezout_df},
                  'allNonzeroZeroClusterRootValuations': '1/13',
                  'normalizedCoefficientValuations': {
                      'a2': 'zero exactly, or2/13', 'a17': 'zero exactly, or14/13',
                      'a18': 'zero exactly, or15/13', 'a19': '16/13'},
                  'powerSeriesValuationConflict': {'required': '3/13',
                      'linearUnit': '2/13', 'linearNonunitLowerBound': '4/13'},
                  'firstCorrectionUniversalSurvivor': {'u': u, 'v': v, 'gamma': 0,
                                                      'allZeroMiddleLabels': 0},
                  'scope': 'Auxiliary exact arithmetic for the proved cluster and next-lift arguments; no whole-stratum exclusion.'}, indent=2))
