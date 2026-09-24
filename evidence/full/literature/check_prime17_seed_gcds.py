"""Exact Hasse gcds for the nine reported characteristic-17 seed rows.

This verifies those rows and extracts simple-mean rigidity consequences.
It does not, by itself, prove the nine-row classification complete.
"""
from math import comb
import json

P = 17
ROWS = [(0, 0, 16, 0, 0), (14, 0, 16, 0, 3), (14, 8, 16, 12, 0),
        (14, 0, 0, 11, 8), (14, 2, 0, 0, 0), (14, 2, 0, 11, 6),
        (14, 2, 0, 14, 3), (0, 16, 0, 0, 0), (0, 16, 0, 14, 3)]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(a):
    a = [v % P for v in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def rem(a, b):
    a, b = trim(a), trim(b)
    require(bool(b), "Division by zero")
    while len(a) >= len(b):
        shift = len(a) - len(b)
        q = a[-1] * pow(b[-1], -1, P) % P
        for i, c in enumerate(b):
            a[i + shift] = (a[i + shift] - q*c) % P
        a = trim(a)
    return a


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, rem(a, b)
    require(bool(a), "Indeterminate gcd")
    return [(x * pow(a[-1], -1, P)) % P for x in a]


def hasse(a, k):
    return trim([comb(i+k, k) * a[i+k] for i in range(max(0, len(a)-k))])


records = []
for index, row in enumerate(ROWS, 1):
    h = [0] * 21
    h[20] = 1
    for exponent, coeff in zip((18, 17, 3, 2, 1), row):
        h[exponent] = coeff
    divisors = {str(k): gcd(h, hasse(h, k)) for k in range(1, 20)}
    require(all(len(g) > 1 for g in divisors.values()), "Seed fails a Hasse condition")
    pure_orders = [int(k) for k, g in divisors.items()
                   if all(c == 0 for c in g[:-1])]
    simple = row[-1] != 0
    forced = pure_orders if simple else []
    records.append({"row": index, "coefficients_a18_b17_c3_d2_e1": row,
                    "meanRootSimple": simple, "monicGcdsAscending": divisors,
                    "purePowerXGcdOrders": pure_orders,
                    "forcedExactZeroOrdinaryExponents": forced,
                    "forcedExactZeroDeficiencies": [20-k for k in forced]})
expected = {2: [19], 4: [3, 17, 19], 6: [3, 19], 7: [3, 19], 9: [3, 18, 19]}
require({r["row"]: r["forcedExactZeroOrdinaryExponents"]
         for r in records if r["meanRootSimple"]} == expected,
        "Unexpected exact coefficient-zero consequences")
print(json.dumps({"status": "PASS", "records": records,
                  "scope": "Seed gcds and simple-mean consequences; completeness requires separate chart certificates"},
                 indent=2))
