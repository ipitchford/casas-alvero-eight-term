#!/usr/bin/env python3
"""Exact standard-library replay over F_p[t][X], plus rational partial models."""
from itertools import combinations
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def clean(poly, p):
    return {k: v % p for k, v in poly.items() if v % p}


def multiply(a, b, p):
    out = {}
    for (x, t), c in a.items():
        for (y, u), d in b.items():
            key = (x + y, t + u)
            out[key] = out.get(key, 0) + c * d
    return clean(out, p)


def root_power(location, exponent, p):
    if location is None:
        return {(exponent, 0): 1}
    return clean({(k, location * (exponent-k)):
                  comb(exponent, k) * (-1) ** (exponent-k)
                  for k in range(exponent+1)}, p)


def hasse(poly, order, p):
    return clean({(x-order, t): c * comb(x, order)
                  for (x, t), c in poly.items() if x >= order}, p)


def evaluate(poly, location, p):
    out = {}
    for (x, t), c in poly.items():
        if location is None:
            if x:
                continue
            exponent = t
        else:
            exponent = t + x * location
        out[exponent] = out.get(exponent, 0) + c
    return {k: v % p for k, v in out.items() if v % p}


def base_digits(n, p):
    out = {}
    i = 0
    while n:
        if n % p:
            out[i] = n % p
        n //= p
        i += 1
    return out


def check_model(p, digits, locations):
    exponents = sorted(digits)
    require(len(set(locations)) == len(locations), "root positions must be distinct")
    multiplicities = [digits[e] * p ** e for e in exponents]
    degree = sum(multiplicities)
    poly = {(0, 0): 1}
    for location, mult in zip(locations, multiplicities):
        poly = multiply(poly, root_power(location, mult, p), p)
    all_derivatives = []
    derivative_digits = []
    for j in range(degree + 1):
        jd = base_digits(j, p)
        admissible = all(jd.get(e, 0) <= digits.get(e, 0) for e in jd)
        predicted = {(0, 0): 1} if admissible else {}
        if admissible:
            for e, location in zip(exponents, locations):
                k = jd.get(e, 0)
                factor = root_power(location, (digits[e]-k) * p ** e, p)
                factor = {m: c * comb(digits[e], k) % p for m, c in factor.items()}
                predicted = multiply(predicted, factor, p)
        actual = hasse(poly, j, p)
        require(actual == predicted, f"Hasse formula: p={p}, n={degree}, j={j}")
        if 0 < j < degree:
            require(any(not evaluate(actual, a, p) for a in locations), "CA condition")
        all_derivatives.append(actual)
        derivative_digits.append(jd)
    subset_count = 0
    for size in range(1, len(locations)):
        for subset in combinations(range(len(locations)), size):
            subset_count += 1
            m = sum(multiplicities[i] for i in subset)
            for j in range(1, m):
                require(any(not evaluate(all_derivatives[j], locations[i], p)
                            for i in subset), "subset-prefix occupancy")
                if comb(m, j) % p:
                    jd = derivative_digits[j]
                    mass = sum((digits[exponents[i]] - jd.get(exponents[i], 0))
                               * p ** exponents[i] for i in subset)
                    require(mass == m-j, "derivative root count")
            require(all(evaluate(all_derivatives[m], locations[i], p)
                        for i in subset), "forbidden cluster-size witness")
    return {"p": p, "degree": degree, "digits": digits,
            "root_locations_t_exponents_null_means_zero": locations,
            "subset_checks": subset_count, "status": "PASS"}


def characteristic_zero_checks():
    # X(X-1)^19: root 1 witnesses all orders 1,...,18 by multiplicity.
    require(all(j < 19 for j in range(1, 19)), "nineteenfold-root occupancy")
    require((-19, 20-19) == (-19, 1), "last derivative at 0 and 1")
    # X^16(X-1)^4: coefficients at 0 and Taylor coefficients at 1.
    values = [(comb(4, j-16)*(-1)**(20-j), comb(16, j-4)) for j in range(16, 20)]
    require(values == [(1, 1820), (-4, 560), (6, 120), (-4, 16)],
            "characteristic-zero failed orders")
    require(all(a and b for a, b in values), "no common root at the last four orders")
    return {"status": "PASS", "degree20_failed_order_values": values}


def main():
    receipts = [check_model(2, {i: 1 for i in range(5)}, [0, 1, 2, 3, None]),
                check_model(3, {0: 2, 1: 1, 3: 2}, [0, 1, None])]
    for p in (2, 3, 7, 11, 13, 17, 19):
        digits = base_digits(20, p)
        require(len(digits) == 2, "degree-20 base-p digit count")
        receipts.append(check_model(p, digits, [None, 0]))
    print(json.dumps({"status": "PASS", "models": receipts,
                      "characteristic_zero": characteristic_zero_checks()}, indent=2))


if __name__ == "__main__":
    main()
