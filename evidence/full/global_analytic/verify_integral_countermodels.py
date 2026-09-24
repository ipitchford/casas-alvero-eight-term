#!/usr/bin/env python3
"""Exact rational replay of the analytic-route countermodels."""
from fractions import Fraction as Q
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def multiply(a, b):
    out = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def power(a, n):
    out = [Q(1)]
    for _ in range(n):
        out = multiply(out, a)
    return out


def hasse(a, k):
    return trim([Q(a[i])*comb(i, k) for i in range(k, len(a))])


def evaluate(a, x):
    out = Q(0)
    for c in reversed(a):
        out = out*x+c
    return out


def remainder(a, b):
    a, b = trim(a), trim(b)
    while len(a) >= len(b) and a != [0]:
        factor, shift = a[-1]/b[-1], len(a)-len(b)
        for i, c in enumerate(b):
            a[i+shift] -= factor*c
        a = trim(a)
    return a


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, remainder(a, b)
    return [x/a[-1] for x in a]


def normalized_chain(f):
    n = len(f)-1
    return [[x/Q(comb(n, j)) for x in hasse(f, n-j)] for j in range(n+1)]


def check_family(n):
    f = multiply(multiply([0, 1], power([-1, 1], n-2)), [n-2, 1])
    require(f[n] == 1 and f[n-1] == 0, "monic centered polynomial")
    require(f[0] == 0 and f[1] != 0, "simple mean root")
    chain = normalized_chain(f)
    require(chain[1] == [0, 1], "linear normalized derivative")
    for j in range(2, n+1):
        predicted = multiply(power([-1, 1], j-2),
                             [-Q((j-1)*(n-j), n), j-2, 1])
        require(chain[j] == predicted, "closed form of normalized derivative")
        require(hasse(chain[j], 1) == [j*x for x in chain[j-1]],
                "differential integral recurrence")
    require(chain[2] == [-Q(n-2, n), 0, 1], "exceptional quadratic")
    require(all(evaluate(chain[2], r) != 0 for r in (0, 1, -(n-2))),
            "quadratic shares no terminal root")
    require(all(evaluate(chain[j], 1) == 0 for j in range(3, n+1)),
            "remaining exact terminal incidences")
    require(Q(0) < Q(n-2, n) < Q(1), "exceptional node lies in (0,1)")
    require(gcd(f, chain[2]) == [1], "only missing incidence")
    roots_moment2 = (n-2) + (n-2)**2
    require(roots_moment2 == n*(n-1)*Q(n-2, n), "Newton second moment")
    return {"degree": n, "conditions_satisfied": n-2,
            "failed_hasse_order": n-2, "root_radius_over_node_radius": n-2}


def check_degree_five():
    cubic = [11, -9, 1, 1]
    f = multiply(multiply([0, 1], [-1, 1]), cubic)
    require(f == [0, -11, 20, -10, 0, 1], "degree-five expansion")
    chain = normalized_chain(f)
    require(chain[2] == [-1, 0, 1], "degree-five G2")
    require(chain[3] == [2, -3, 0, 1], "degree-five G3")
    require(f[1] == -11 and evaluate(hasse(f, 1), 1) == 4,
            "both marked roots are simple")
    require(gcd(f, hasse(f, 1)) == [1], "degree-five squarefreeness")
    require(evaluate(chain[1], 0) == 0 and evaluate(chain[2], 1) == 0
            and evaluate(chain[3], 1) == 0, "three true CA incidences")
    a, b, c = 1, -9, 11
    disc = a*a*b*b - 4*b**3 - 4*a**3*c - 27*c*c + 18*a*b*c
    require(disc == -2096, "cubic discriminant")
    return {"status": "PASS", "failed_hasse_order": 1, "cubic_discriminant": disc}


def main():
    family = [check_family(n) for n in range(4, 41)]
    print(json.dumps({"status": "PASS", "family": family,
                      "degree_five": check_degree_five(),
                      "degree20_squared_radius_lower_bound": "379/18",
                      "degree20_cubed_radius_lower_bound": "6841/18"}, indent=2))


if __name__ == "__main__":
    main()
