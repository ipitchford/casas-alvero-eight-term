"""Read-only standard-library replay of family B's characteristic-13 certificate.

Resultants are verified independently at enough exact F_(13^3) points to
determine them under a proved Sylvester degree bound. No Singular is needed.
"""
from functools import lru_cache
from math import comb
from pathlib import Path
from time import perf_counter
import hashlib
import json

P = 13


def clean(a):
    while a and not a[-1]: a.pop()
    return a


def uadd(a, b):
    out = [0]*max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)) % P
    return clean(out)


def uscale(a, n): return clean([n*c % P for c in a])


def umul(a, b):
    if not a or not b: return []
    out = [0]*(len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b): out[i+j] = (out[i+j]+c*d) % P
    return clean(out)


def udivide(a, b):
    a = a[:]
    out = [0]*max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, P)
    while len(a) >= len(b):
        j, c = len(a)-len(b), a[-1]*inv % P
        out[j] = c
        for k, d in enumerate(b): a[j+k] = (a[j+k]-c*d) % P
        clean(a)
    return clean(out), a


# F_13[t]/(t^3-t-1); encoded by a0+13*a1+169*a2.
TRIPLES = [(i % P, i//P % P, i//(P*P)) for i in range(P**3)]


def fadd(a, b):
    a0, a1, a2 = TRIPLES[a]
    b0, b1, b2 = TRIPLES[b]
    return (a0+b0) % P + P*((a1+b1) % P) + P*P*((a2+b2) % P)


def fneg(a):
    a0, a1, a2 = TRIPLES[a]
    return (-a0) % P + P*((-a1) % P) + P*P*((-a2) % P)


def fmul(a, b):
    if not a or not b: return 0
    if a == 1: return b
    if b == 1: return a
    a0, a1, a2 = TRIPLES[a]
    b0, b1, b2 = TRIPLES[b]
    e3, e4 = a1*b2+a2*b1, a2*b2
    c0 = (a0*b0+e3) % P
    c1 = (a0*b1+a1*b0+e3+e4) % P
    c2 = (a0*b2+a1*b1+a2*b0+e4) % P
    return c0+P*c1+P*P*c2


def fpow(a, n):
    out = 1
    while n:
        if n & 1: out = fmul(out, a)
        a, n = fmul(a, a), n >> 1
    return out


@lru_cache(None)
def finv(a):
    if not a: raise ZeroDivisionError
    b = fpow(a, P**3-2)
    if fmul(a, b) != 1: raise ValueError('Field inverse failed')
    return b


def feval(a, x):
    value = 0
    for c in reversed(a): value = fadd(fmul(value, x), c)
    return value


def frem(a, b):
    a = a[:]
    inv = finv(b[-1])
    while len(a) >= len(b):
        shift = len(a)-len(b)
        factor = fmul(a[-1], inv)
        for j, c in enumerate(b):
            a[shift+j] = fadd(a[shift+j], fneg(fmul(factor, c)))
        clean(a)
    return a


def fresultant(a, b):
    a, b = clean(a[:]), clean(b[:])
    if not a or not b: return 0
    out = 1
    while len(b) > 1:
        m, n = len(a)-1, len(b)-1
        if m < n:
            if m*n % 2: out = fneg(out)
            a, b = b, a
            m, n = n, m
        r = frem(a, b)
        if not r: return 0
        if m*n % 2: out = fneg(out)
        out = fmul(out, fpow(b[-1], m-len(r)+1))
        a, b = b, r
    return fmul(out, fpow(b[0], len(a)-1))


def madd(a, b):
    out = dict(a)
    for exponents, c in b.items():
        out[exponents] = (out.get(exponents, 0)+c) % P
    return {e: c for e, c in out.items() if c}


def mscale(a, c): return {e: c*v % P for e, v in a.items() if c*v % P}


def mmul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            out[i+k, j+l] = (out.get((i+k, j+l), 0)+c*d) % P
    return {e: c for e, c in out.items() if c}


def eval_hasse(coefficients, order, variable):
    out = {}
    for exponent, coefficient in coefficients.items():
        if exponent < order: continue
        powers = [0, 0]
        powers[variable] = exponent-order
        out = madd(out, mscale(mmul(coefficient, {tuple(powers): 1}), comb(exponent, order)))
    return out


def main():
    start = perf_counter()
    path = Path(__file__).resolve().parent/'certificate.json'
    data = json.loads(path.read_text())
    if any((t**3-t-1) % P == 0 for t in range(P)):
        raise ValueError('Chosen cubic is not irreducible')
    # Degree three and no base-field root imply irreducibility.
    q = [1, 1]
    b = [0]*17
    b[13], b[16] = -4 % P, -comb(20, 4) % P
    numerator = [0]*20
    numerator[0], numerator[13], numerator[16], numerator[19] = 8, 4, 9, 5
    k, remainder = udivide(numerator, [12, 1])
    if remainder: raise ValueError('Nonexact removal of u-1')
    c = uscale(k, -1)
    d = uadd(umul(q, uadd([8], uscale(b, -1))), uscale(c, -1))
    # Verify the normalization identity before computing any resultant.
    original_c_numerator = uadd([5]+[0]*18+[8], b)
    if umul(c, [12, 1]) != original_c_numerator:
        raise ValueError('Incorrect rational coefficient parametrization')
    qb = umul(q, b)
    pc = [[] for _ in range(20)]
    dc3 = [[] for _ in range(18)]
    dc1 = [[] for _ in range(20)]
    pc[19], pc[16], pc[3], pc[2], pc[0] = q, uscale(q, 4), qb, c, d
    dc3[17], dc3[14], dc3[1], dc3[0] = uscale(q, comb(20, 3)), uscale(q, 4*comb(17, 3)), uscale(qb, 4), c
    dc1[19], dc1[16], dc1[3], dc1[2], dc1[0] = uscale(q, 20), uscale(q, 4*17), uscale(qb, 4), uscale(c, 3), d
    degrees = [max(len(a)-1 for a in collection) for collection in [pc, dc3, dc1]]
    bound3 = 17*degrees[0]+19*degrees[1]
    bound1 = 19*degrees[0]+19*degrees[2]
    bound = max(bound3, bound1)
    if degrees != [18, 18, 18] or [bound3, bound1] != [648, 684]:
        raise ValueError('Unexpected proved resultant degree bounds')
    r3, r1 = data['R3'], data['R1']
    if len(r3)-1 > bound3 or len(r1)-1 > bound1:
        raise ValueError('Supplied resultant exceeds degree bound')
    # q=0 drops both leading coefficients. Skip it and use 685 other points;
    # the degree argument then certifies the identity even at the skipped point.
    points = [t for t in range(P**3) if t != P-1][:bound+1]
    if len(points) != bound+1 or len(set(points)) != len(points):
        raise ValueError('Insufficient distinct evaluation points')
    for t in points:
        pv = [feval(coefficient, t) for coefficient in pc]
        d3v = [feval(coefficient, t) for coefficient in dc3]
        d1v = [feval(coefficient, t) for coefficient in dc1]
        if len(clean(pv[:])) != 20 or len(clean(d3v[:])) != 18 or len(clean(d1v[:])) != 20:
            raise ValueError('Specialized degree dropped')
        if fresultant(pv, d3v) != feval(r3, t):
            raise ValueError(f'R3 resultant mismatch at encoded field point {t}')
        if fresultant(pv, d1v) != feval(r1, t):
            raise ValueError(f'R1 resultant mismatch at encoded field point {t}')
    f, g = umul(c, r3), umul(d, r1)
    target = [comb(17, i) % P for i in range(18)]
    identity = uadd(umul(data['bezoutC'], f), umul(data['bezoutD'], g))
    if identity != target: raise ValueError('Bezout identity failed')
    if uadd(identity, f) == target: raise ValueError('Bezout mutation control failed')
    # Derive the b=0 equations from the original h and Hasse formula.
    one = {(0, 0): 1}
    cm = {(17, 0): -comb(20, 3) % P, (14, 0): -4*comb(17, 3) % P}
    dm = madd(mscale(one, -5), mscale(cm, -1))
    hcoeff = {20: one, 17: mscale(one, 4), 3: cm, 1: dm}
    generators = [eval_hasse(hcoeff, 0, 0), eval_hasse(hcoeff, 0, 1), eval_hasse(hcoeff, 1, 1)]
    total = {}
    for generator, saved in zip(generators, data['bZeroMultipliers'], strict=True):
        multiplier = {}
        for coefficient, i, j in saved:
            if (i, j) in multiplier: raise ValueError('Duplicate certificate monomial')
            multiplier[i, j] = coefficient % P
        total = madd(total, mmul(generator, multiplier))
    if total != one: raise ValueError('b=0 unit identity failed')
    if madd(total, generators[0]) == one: raise ValueError('b=0 mutation control failed')
    print(json.dumps({'status': 'PASS', 'certificateSha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'field': 'F13[t]/(t^3-t-1)', 'irreducibility': 'degree 3; no F13 roots',
                      'resultantCoefficientDegreeBounds': degrees,
                      'resultantDegreeBounds': [bound3, bound1], 'distinctFieldPoints': len(points),
                      'resultantDegrees': [len(r3)-1, len(r1)-1],
                      'univariateIdentity': 'C*c_num*R3+D*d_num*R1=(u+1)^17',
                      'bZeroUnitIdentity': 'PASS', 'bZeroMultiplierTerms': [len(s) for s in data['bZeroMultipliers']],
                      'mutationControls': 'PASS', 'elapsedSeconds': perf_counter()-start}, indent=2))


if __name__ == '__main__':
    main()
