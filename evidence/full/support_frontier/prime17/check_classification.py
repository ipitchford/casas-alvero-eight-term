"""Exact characteristic-17 chart/certificate replay; Python standard library only.

No producer imports, no CAS calls, no probabilistic tests, no output-file writes.
The F_17^2 grids are larger than rigorous coordinatewise resultant degree bounds.
"""
from pathlib import Path
from math import comb
from time import perf_counter
import hashlib
import json

BASE = Path(__file__).resolve().parent
P = 17


def require(ok, message):
    if not ok:
        raise ValueError(message)


def clean(f):
    return {m: c % P for m, c in f.items() if c % P}


def add(f, g):
    h = f.copy()
    for m, c in g.items():
        h[m] = (h.get(m, 0) + c) % P
        if not h[m]:
            del h[m]
    return h


def scale(f, c):
    return clean({m: c * v for m, v in f.items()})


def mul(f, g):
    h = {}
    for (a, b), c in f.items():
        for (d, e), v in g.items():
            m = (a+d, b+e)
            h[m] = (h.get(m, 0) + c*v) % P
    return clean(h)


def power(f, n):
    out = {(0, 0): 1}
    while n:
        if n & 1:
            out = mul(out, f)
        f = mul(f, f)
        n //= 2
    return out


ONE = {(0, 0): 1}
S = {(1, 0): 1}
T = {(0, 1): 1}


def parse_certificate(name):
    path = BASE / f"certificate_{name}.sing.log"
    lines = path.read_text().splitlines()
    require(lines[:2] == ['COUNTS', '3'], f'{name}: bad header')
    count = int(lines[2])
    out = {}
    cursor = 3
    while lines[cursor] != 'DONE':
        require(lines[cursor].startswith('POLY '), f'{name}: unexpected record')
        label = lines[cursor][5:]
        require(label not in out, f'{name}: duplicate {label}')
        cursor += 1
        f = {}
        while lines[cursor] != 'END':
            c, a, b = map(int, lines[cursor].split())
            require(a >= 0 and b >= 0 and c % P, 'bad term')
            require((a, b) not in f, 'duplicate monomial')
            f[(a, b)] = c % P
            cursor += 1
        out[label] = f
        cursor += 1
    require(cursor == len(lines)-1, f'{name}: trailing records')
    expected = {f'I{i}' for i in range(1, 4)}
    expected |= {f'T{j}' for j in range(1, count+1)}
    expected |= {f'M{i}_{j}' for i in range(1, 4) for j in range(1, count+1)}
    require(set(out) == expected, f'{name}: incomplete records')
    return out, count, hashlib.sha256(path.read_bytes()).hexdigest()


# F_17[alpha]/(alpha^2-3). 3 is nonsquare, so this is a field of 289 elements.
require(3 not in {i*i % P for i in range(P)}, 'extension polynomial reducible')
SIZE = P*P
ADD = [[((x % P+y % P) % P) + P*((x//P+y//P) % P)
        for y in range(SIZE)] for x in range(SIZE)]
NEG = [((-x % P) % P) + P*((-(x//P)) % P) for x in range(SIZE)]
MUL = [[((x % P*(y % P)+3*(x//P)*(y//P)) % P)
        + P*((x % P*(y//P)+(x//P)*(y % P)) % P)
        for y in range(SIZE)] for x in range(SIZE)]


def fpow(a, n):
    out = 1
    while n:
        if n & 1:
            out = MUL[out][a]
        a = MUL[a][a]
        n //= 2
    return out


INV = [0]+[fpow(i, SIZE-2) for i in range(1, SIZE)]
require(all(MUL[i][INV[i]] == 1 for i in range(1, SIZE)), 'inverses')
require(all(ADD[i][NEG[i]] == 0 for i in range(SIZE)), 'negatives')


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def rem(a, b):
    a = a.copy()
    require(bool(b), 'division by zero')
    inv = INV[b[-1]]
    n = len(b)-1
    while len(a) >= len(b):
        k = len(a)-len(b)
        q = MUL[a[-1]][inv]
        if q:
            row = MUL[NEG[q]]
            for j in range(n):
                a[k+j] = ADD[a[k+j]][row[b[j]]]
        a.pop()
        trim(a)
    return a


def resultant(a, b):
    a, b = trim(a.copy()), trim(b.copy())
    require(bool(a) and bool(b), 'zero-polynomial resultant input')
    out = 1
    while len(b) > 1:
        m, n = len(a)-1, len(b)-1
        if m < n:
            if m*n % 2:
                out = NEG[out]
            a, b = b, a
            continue
        c = rem(a, b)
        if not c:
            return 0
        k = len(c)-1
        out = MUL[out][fpow(b[-1], m-k)]
        if m*n % 2:
            out = NEG[out]
        a, b = b, c
    return MUL[out][fpow(b[0], len(a)-1)]


def gcd(a, b):
    a, b = trim(a.copy()), trim(b.copy())
    while b:
        a, b = b, rem(a, b)
    return [MUL[c][INV[a[-1]]] for c in a] if a else []


def degree(f, i):
    return max((m[i] for m in f), default=0)


def evaluate(f, sp, tp):
    out = 0
    for (i, j), c in f.items():
        out = ADD[out][MUL[c][MUL[sp[i]][tp[j]]]]
    return out


def powers(value, n):
    out = [1]
    for _ in range(n):
        out.append(MUL[out[-1]][value])
    return out


def hasse_symbolic(h, k):
    return {i-k: scale(c, comb(i, k)) for i, c in h.items()
            if i >= k and comb(i, k) % P and c}


def chart(name):
    c = scale(ONE, -1)
    if name == 'c_nonzero':
        a, b, d = S, {}, T
    elif name == 'u_one':
        a, b, d = scale(add(ONE, S), -1), S, T
    elif name == 'u_other':
        a, b, d = scale(add(power(S, 2), T), -1), mul(S, T), T
    elif name == 'c_zero':
        a, b, c, d = scale(ONE, -3), S, {}, T
    else:
        raise ValueError(name)
    e = scale(add(add(a, b), d), -1)
    if name == 'c_zero':
        e = add(e, scale(ONE, -1))  # a=-3, so e=2-b-d.
    h = {20: ONE, 18: a, 17: b, 3: c, 2: d, 1: e}
    return {i: f for i, f in h.items() if f}


def verify_resultant(name, h, k, candidate):
    derivative = hasse_symbolic(h, k)
    m, n = max(h), max(derivative)
    bounds = [n*max(degree(f, j) for f in h.values())
              +m*max(degree(f, j) for f in derivative.values()) for j in (0, 1)]
    require(all(degree(candidate, j) <= bounds[j] for j in (0, 1)),
            f'{name} H{k}: candidate exceeds resultant degree bound')
    require(all(v < SIZE for v in bounds), 'field too small for exact grid')
    max_s = max(bounds[0], *(degree(f, 0) for f in h.values()))
    max_t = max(bounds[1], *(degree(f, 1) for f in h.values()))
    pp_s = [powers(v, max_s) for v in range(bounds[0]+1)]
    pp_t = [powers(v, max_t) for v in range(bounds[1]+1)]
    for si, sp in enumerate(pp_s):
        for ti, tp in enumerate(pp_t):
            a = [0]*(m+1)
            for i, f in h.items():
                a[i] = evaluate(f, sp, tp)
            b = [0]*(n+1)
            for i, f in derivative.items():
                b[i] = evaluate(f, sp, tp)
            value = resultant(a, b)
            require(value == evaluate(candidate, sp, tp),
                    f'{name} H{k}: resultant mismatch at ({si},{ti})')
    return {'hasseOrder': k, 'bidegreeBound': bounds,
            'exactEvaluations': (bounds[0]+1)*(bounds[1]+1)}


def target_checks(name, cert):
    if name == 'c_nonzero':
        expected = clean({(20, 0): 1, (11, 1): -3, (2, 2): -2,
                          (3, 0): 3, (2, 1): -8, (1, 2): -6})
        require(cert['T1'] == power(T, 20) and cert['T2'] == expected,
                'b=0 targets')
    elif name == 'u_one':
        require(cert['T1'] == ONE, 'u=1 target')
    elif name == 'u_other':
        require(cert['T1'] == mul(power(T, 20), add(T, scale(ONE, 5))), 'other T1')
        require(cert['T2'] == mul(power(T, 20), add(S, scale(ONE, 5))), 'other T2')
        special = {m: c for m, c in cert['T3'].items() if m[1] == 0}
        expected = mul(power(S, 6), power(add(power(S, 2), scale(ONE, -3)), 17))
        require(special == expected, 'other T3 specialization')
    elif name == 'c_zero':
        q1 = mul(S, add(S, scale(ONE, -2)))
        q2 = add(add(mul(S, T), scale(S, 6)), add(scale(T, -2), scale(ONE, 5)))
        q3 = mul(T, mul(add(T, scale(ONE, -11)), add(T, scale(ONE, -14))))
        for j, q, exponent in [(1, q1, 19), (2, q2, 19), (3, q3, 18)]:
            require(cert[f'T{j}'] == power(q, exponent), f'c=0 target {j}')


def seed_poly(row):
    a, b, c, d, e = row
    h = [0]*21
    h[20], h[18], h[17], h[3], h[2], h[1] = 1, a, b, c, d, e
    return h


def hasse(h, k):
    return trim([h[i]*comb(i, k) % P for i in range(k, len(h))])


def verify_seed_rows():
    rows = [(0, 0, 16, 0, 0), (14, 0, 16, 0, 3), (14, 8, 16, 12, 0),
            (14, 0, 0, 11, 8), (14, 2, 0, 0, 0), (14, 2, 0, 11, 6),
            (14, 2, 0, 14, 3), (0, 16, 0, 0, 0), (0, 16, 0, 14, 3)]
    out = []
    for row in rows:
        h = seed_poly(row)
        gd = {}
        for k in range(1, 20):
            g = gcd(h, hasse(h, k))
            require(len(g) > 1, f'row {row} fails derivative {k}')
            if k in [1, 2, 3, 17, 18, 19]:
                gd[str(k)] = g
        out.append({'coefficients': row, 'markedMonicGcdsLowToHigh': gd})
    for row in [(0, 16, 0, 12, 5), (0, 0, 0, 14, 2)]:
        h = seed_poly(row)
        require(gcd(h, hasse(h, 1)) == [1], 'boundary exclusion')
    require((pow(7, 19, 17)-3*7+2) % 17 == 1, 'last boundary value')
    return out


def main():
    started = perf_counter()
    # Euclidean-resultant orientation self-tests include nonmonic factors.
    require(resultant([16, 1], [15, 1]) == 16, 'linear resultant sign')
    require(resultant([15, 1], [16, 1]) == 1, 'swapped resultant sign')
    require(resultant([16, 0, 1], [15, 1]) == 3, 'quadratic resultant')
    report = {'field': 'F17[alpha]/(alpha^2-3)', 'charts': {}}
    for name in ['c_nonzero', 'u_one', 'u_other', 'c_zero']:
        cert, count, fingerprint = parse_certificate(name)
        target_checks(name, cert)
        for j in range(1, count+1):
            total = {}
            for i in range(1, 4):
                total = add(total, mul(cert[f'I{i}'], cert[f'M{i}_{j}']))
            require(total == cert[f'T{j}'], f'{name}: membership identity {j}')
        h = chart(name)
        orders = [17 if name == 'c_zero' else 18, 2, 1]
        checks = [verify_resultant(name, h, k, cert[f'I{i}'])
                  for i, k in enumerate(orders, 1)]
        report['charts'][name] = {'sha256': fingerprint,
            'membershipIdentities': count, 'resultants': checks,
            'certificateMonomials': sum(map(len, cert.values()))}
        print(json.dumps({'chart': name, 'status': 'PASS'}), flush=True)
    report['seeds'] = verify_seed_rows()
    report['status'] = 'PASS'
    report['elapsedSeconds'] = perf_counter()-started
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
