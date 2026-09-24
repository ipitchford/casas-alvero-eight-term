"""Exact bounded F_p coefficient search for the closed seed family B.

A failed search only concerns coefficients in F_p. GCDs detect common roots
over the algebraic closure, so witnesses need not belong to F_p.
"""
from itertools import product
from math import comb
from time import perf_counter
import json


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def rem(a, b, p):
    a = a[:]
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        q = a[-1] * inv % p
        k = len(a) - len(b)
        for j, v in enumerate(b):
            a[j + k] = (a[j + k] - q * v) % p
        trim(a)
    return a


def gcd(a, b, p):
    a, b = trim(a[:]), trim(b[:])
    while b:
        a, b = b, rem(a, b, p)
    if a:
        inv = pow(a[-1], -1, p)
        a = [v * inv % p for v in a]
    return a


def derivative(f, k, p):
    return trim([comb(j, k) * f[j] % p for j in range(k, len(f))])


def run(p):
    start = perf_counter()
    survivors = []
    counts = [0] * 5
    for a, b, c, d in product(range(p), repeat=4):
        if not (a or b or c or d):
            continue
        f = [0] * 21
        f[20], f[17], f[4], f[3], f[1] = 1, a, b, c, d
        counts[0] += 1
        for i, k in enumerate([17, 4, 3, 1], 1):
            if len(gcd(f, derivative(f, k, p), p)) <= 1:
                break
            counts[i] += 1
        else:
            # Verify every derivative rather than relying on inactive-order logic.
            gs = [gcd(f, derivative(f, k, p), p) for k in range(1, 20)]
            if not all(len(g) > 1 for g in gs):
                raise RuntimeError("active derivative implication failed")
            survivors.append({"coefficients": [a, b, c, d], "gcds": gs})
    return {"prime": p, "coefficientTuples": p**4-1,
            "successiveSurvivors17_4_3_1": counts,
            "nontrivialExamples": survivors,
            "elapsedSeconds": perf_counter()-start,
            "scope": "All F_p coefficients; common roots over algebraic closure."}


if __name__ == "__main__":
    print(json.dumps([run(11), run(13)], indent=2))
