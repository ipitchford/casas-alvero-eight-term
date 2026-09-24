"""Export the bounded Singular results and an exact univariate Bezout identity."""
from pathlib import Path
import hashlib
import json
import re

P = 13


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    out = [0]*max(len(a), len(b))
    for i, c in enumerate(a): out[i] = c
    for i, c in enumerate(b): out[i] = (out[i]+c) % P
    return trim(out)


def scale(a, k): return trim([k*c % P for c in a])


def mul(a, b):
    if not a or not b: return []
    out = [0]*(len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b): out[i+j] = (out[i+j]+c*d) % P
    return trim(out)


def divide(a, b):
    a = a[:]
    q = [0]*max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, P)
    while len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*inv % P
        q[k] = c
        for j, d in enumerate(b): a[k+j] = (a[k+j]-c*d) % P
        trim(a)
    return trim(q), a


def bezout(a, b):
    s, ss, t, tt = [1], [], [], [1]
    while b:
        q, r = divide(a, b)
        a, b = b, r
        s, ss = ss, add(s, scale(mul(q, ss), -1))
        t, tt = tt, add(t, scale(mul(q, tt), -1))
    inv = pow(a[-1], -1, P)
    return scale(a, inv), scale(s, inv), scale(t, inv)


def parse(s):
    out = {}
    for term in re.findall(r'[+-]?[^+-]+', s.strip()):
        match = re.fullmatch(r'([+-]?)(\d*)(?:u(\d*))?', term)
        if not match: raise ValueError(term)
        sign, c, e = match.groups()
        c = int(c or '1') * (-1 if sign == '-' else 1)
        e = int(e or '1') if 'u' in term else 0
        out[e] = (out.get(e, 0)+c) % P
    return trim([out.get(i, 0) for i in range(max(out, default=-1)+1)])


if __name__ == '__main__':
    base = Path(__file__).resolve().parent
    source = base/'resultants.sing.log'
    lines = source.read_text().splitlines()
    r3, r1 = [parse(lines[lines.index(tag)+1]) for tag in ['R3', 'R1']]
    b = [0]*17
    b[13], b[16] = 9, 4
    numerator = [0]*20
    numerator[0], numerator[13], numerator[16], numerator[19] = 8, 4, 9, 5
    k, remainder = divide(numerator, [12, 1])
    if remainder: raise ValueError('K not polynomial')
    c = scale(k, -1)
    d = add(mul([1, 1], add([8], scale(b, -1))), scale(c, -1))
    f, g = mul(c, r3), mul(d, r1)
    common, cu, cv = bezout(f, g)
    q17 = [1]
    for _ in range(17): q17 = mul(q17, [1, 1])
    if common != q17: raise ValueError('Wrong gcd')
    if add(mul(cu, f), mul(cv, g)) != q17: raise ValueError('Identity failed')
    sparse = [[], [], []]
    for line in (base/'b_zero.sing.log').read_text().splitlines():
        if line.startswith('C|'):
            _, i, coefficient, exponents = line.split('|')
            v, w = map(int, exponents.split(','))
            sparse[int(i)-1].append([int(coefficient) % P, v, w])
    data = {'prime': 13, 'coefficientOrder': 'ascending univariate powers',
            'R3': r3, 'R1': r1, 'bezoutC': cu, 'bezoutD': cv,
            'identity': 'bezoutC*c_num*R3+bezoutD*d_num*R1=(u+1)^17',
            'bZeroMultipliers': sparse,
            'sourceSha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in [source, base/'b_zero.sing.log']}}
    (base/'certificate.json').write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print(json.dumps({'resultantDegrees': [len(r3)-1, len(r1)-1],
                      'bezoutDegrees': [len(cu)-1, len(cv)-1],
                      'bZeroMultiplierTerms': [len(s) for s in sparse],
                      'result': 'exported; independent replay still required'}))
