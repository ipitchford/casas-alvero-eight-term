#!/usr/bin/env python3
"""Replay exact F13 ideal-membership certificates using sparse integer lists."""
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

P = 13


def require(ok, message):
    if not ok:
        raise ValueError(message)


def add(a, b):
    c = a.copy()
    for m, v in b.items():
        c[m] = (c.get(m, 0)+v) % P
        if not c[m]:
            del c[m]
    return c


def scale(a, c):
    return {m: c*v % P for m, v in a.items() if c*v % P}


def mul(a, b):
    c = {}
    for m, x in a.items():
        for n, y in b.items():
            k = tuple(i+j for i, j in zip(m, n))
            c[k] = (c.get(k, 0)+x*y) % P
    return {m: v for m, v in c.items() if v}


def power(a, n, unit):
    c = unit
    for _ in range(n):
        c = mul(c, a)
    return c


def parse(text, names):
    result = {}
    for raw in text.replace('-', '+-').split('+'):
        if not raw:
            continue
        sign = -1 if raw.startswith('-') else 1
        term = raw[1:] if sign < 0 else raw
        match = re.match(r'\d*', term)
        prefix = match.group()
        coefficient = sign*(int(prefix) if prefix else 1) % P
        monomial_text = term[len(prefix):]
        factors = re.findall(r'([wvu])(\d*)', monomial_text)
        require(''.join(v+e for v, e in factors) == monomial_text, 'Unparsed monomial')
        powers = [0]*len(names)
        for v, e in factors:
            require(v in names, 'Unexpected variable')
            powers[names.index(v)] += int(e) if e else 1
        m = tuple(powers)
        result[m] = (result.get(m, 0)+coefficient) % P
    return {m: v for m, v in result.items() if v}


def replay(branch):
    source = Path(__file__).with_name(f'seed13-a-{branch}-certificate.txt')
    lines = source.read_text().splitlines()
    names = lines[0].split()[1:]
    require(names == (['w', 'v', 'u'] if branch == 'nonzero' else ['w', 'v']), 'Wrong ring')
    I, J, L = {}, {}, {}
    for line in lines[1:]:
        fields = line.split()
        tag, i = fields[0], int(fields[1])
        if tag == 'L':
            j, expression = int(fields[2]), fields[3]
            require((i, j) not in L, 'Duplicate matrix entry')
            L[i, j] = parse(expression, names)
        else:
            table = I if tag == 'I' else J if tag == 'J' else None
            require(table is not None and i not in table, 'Unexpected or duplicate polynomial')
            table[i] = parse(fields[2], names)
    unit = parse('1', names)
    w, v = parse('w', names), parse('v', names)
    pw = lambda a, n: power(a, n, unit)
    if branch == 'nonzero':
        u, a = parse('u', names), scale(unit, 4)
        b = add(scale(pw(u, 4), -9), scale(u, -3))
        c = add(add(scale(pw(v, 18), -8), scale(pw(v, 15), -11)), scale(mul(b, pw(v, 14)), -3))
        targets = [add(u, scale(unit, -1)), add(v, scale(unit, -1)), add(w, scale(unit, 6))]
    else:
        a, b = {}, scale(unit, 4)
        c = add(scale(pw(v, 18), -8), scale(mul(b, pw(v, 14)), -3))
        targets = [unit]
    d = scale(add(add(add(unit, a), b), c), -1)
    def f(x):
        return add(add(add(add(pw(x, 20), mul(a, pw(x, 17))), mul(b, pw(x, 16))),
                       mul(c, pw(x, 2))), mul(d, x))
    h1 = add(add(add(add(scale(pw(w, 19), 7), scale(mul(a, pw(w, 16)), 4)),
                        scale(mul(b, pw(w, 15)), 3)), scale(mul(c, w), 2)), d)
    generators = [f(u), f(v), f(w), h1] if branch == 'nonzero' else [f(v), f(w), h1]
    require(I == {i+1: f for i, f in enumerate(generators)}, 'Original ideal differs from derived equations')
    require(J == {i+1: f for i, f in enumerate(targets)}, 'Target equations differ')
    for j, target in J.items():
        total = {}
        for i, generator in I.items():
            require((i, j) in L, 'Missing matrix entry')
            total = add(total, mul(generator, L[i, j]))
        require(total == target, f'Ideal-membership replay failed for target{j}')
    if branch == 'nonzero':
        point = [7, 1, 1]
        for generator in I.values():
            value = sum(c*pow(point[0], m[0], P)*pow(point[1], m[1], P)*pow(point[2], m[2], P)
                        for m, c in generator.items()) % P
            require(value == 0, 'Reverse inclusion at the point failed')
    return {'branch': branch, 'status': 'PASS', 'generatorCount': len(I),
            'targetCount': len(J), 'matrixTermCount': sum(map(len, L.values())),
            'sourceSha256': sha256(source.read_bytes()).hexdigest()}


argument = sys.argv[1] if len(sys.argv) > 1 else 'zero'
require(argument in ['zero', 'nonzero', 'all'], 'Unknown branch argument')
records = [replay(b) for b in (['zero', 'nonzero'] if argument == 'all' else [argument])]
print(json.dumps({'status': 'PASS', 'records': records,
                  'scope': 'Exact sparse-polynomial identity replay of the stated ordinary ideals, including reconstruction of original generators.'}, indent=2))
