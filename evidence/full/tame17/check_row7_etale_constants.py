"""Exact arithmetic supporting the bounded row-7 etale audit."""
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


def hv(h, k, x):
    return sum(c * comb(e, k) * pow(x, e-k, 17)
               for e, c in h.items() if e >= k) % 17


a18, a19 = Fraction(-281200, 190), Fraction(279109, 20)
require(1-190+2280+190*a18+20*a19 == 0, "f(1) constant")
require(190-190*comb(18, 2)+2280*comb(17, 2)+190*a18 == 0,
        "H2f(1) constant")
rows = []
for j in range(4, 17):
    b, q = comb(20, j), comb(20-j, 2)
    d18, d19 = Fraction(-q*b, 190), Fraction((q-1)*b, 20)
    require(b % 17 == 0, "Visible binomial")
    require(b+190*d18+20*d19 == 0 and q*b+190*d18 == 0,
            "Elimination derivative identity")
    require(residue(d18) == residue(d19) == 0, "Nonzero reduced partial")
    rows.append({"j": j, "a18Partial": str(d18), "a19Partial": str(d19)})
h = {20: 1, 18: 14, 17: 2, 2: 14, 1: 3}
at_seven = [hv(h, k, 7) for k in range(3)]
require(at_seven == [0, 0, 8], "Cluster at7 is not exactlydouble")
critical_derivative = 2*at_seven[2]*pow(20, -1, 17) % 17
require(critical_derivative == 11, "Critical equation derivative not11")
require(hv(h, 1, 0) == 3 and hv(h, 1, 1) == 14, "Simple special roots")
require([residue(190*a18), residue(20*a19)] == [14, 3], "Wrong residue")
print(json.dumps({"status": "PASS", "row7HasseOrders0to2AtSeven": at_seven,
                  "criticalEquationDerivativeMod17": critical_derivative,
                  "constant_a18": str(a18), "constant_a19": str(a19),
                  "rows": rows,
                  "scope": "Exact arithmetic; Jacobian and uniqueness proved separately"}, indent=2))
