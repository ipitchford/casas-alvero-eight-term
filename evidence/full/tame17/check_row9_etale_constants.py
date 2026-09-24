"""Exact arithmetic supporting the structural row-9 etale audit.

The Hensel/uniqueness argument is proved in ROW9_ETALE_AUDIT.md; it is not
replaced by finite sampling here.
"""
from fractions import Fraction
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def residue(q):
    q = Fraction(q)
    require(q.denominator % 17 != 0, "Nonintegral rational coefficient")
    return q.numerator * pow(q.denominator, -1, 17) % 17


c18, c19 = Fraction(18221, 190), Fraction(-17082, 20)
require(1 - 1140 + 190*c18 + 20*c19 == 0, "f(1) constant term")
require(20 - 17*1140 + 380*c18 + 20*c19 == 0, "f'(1) constant term")
require([residue(190*c18), residue(20*c19)] == [14, 3], "Wrong seed")
rows = []
for j in range(4, 17):
    b = comb(20, j)
    a18_derivative = Fraction(-(19-j)*b, 190)
    a19_derivative = Fraction((18-j)*b, 20)
    require(b % 17 == 0, "Binomial coefficient visible")
    require(b + 190*a18_derivative + 20*a19_derivative == 0, "f(1) coefficient")
    require((20-j)*b + 380*a18_derivative + 20*a19_derivative == 0,
            "f'(1) coefficient")
    require(residue(a18_derivative) == residue(a19_derivative) == 0,
            "Eliminated coefficient derivative is not divisible by17")
    # Each G_j uses only a_i for i<=j; the coefficient of a_j is1.
    require(comb(j, j) == 1, "Normalized-derivative diagonal")
    rows.append({"j": j, "binomial": b,
                 "a18Partial": str(a18_derivative), "a19Partial": str(a19_derivative)})
require((190*20 - 380*20) % 17 == 8, "Elimination determinant")
print(json.dumps({"status": "PASS", "eliminationDeterminantMod17": 8,
                  "constant_a18": str(c18), "constant_a19": str(c19),
                  "normalizedCoefficientResidues_a18_a19": [residue(c18), residue(c19)],
                  "rows": rows,
                  "scope": "Exact coefficient arithmetic; structural Jacobian and Hensel proof in accompanying audit"},
                 indent=2))
