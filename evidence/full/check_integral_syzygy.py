#!/usr/bin/env python3
"""Independent symbolic replay of the first integral 2-saturation identity.

No root is assumed to have integral valuation.  This checks an integer
polynomial identity before reduction, not point lifting modulo four.
"""
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path

import sympy as sp


def require(condition, message):
    if not condition:
        raise ValueError(message)


def val2(n):
    require(n != 0, "The valuation of zero was requested")
    return (abs(n) & -abs(n)).bit_length() - 1


a = {j: sp.Symbol(f"a{j}") for j in range(2, 20)}
w = sp.Symbol("w")
variables = (w, *a.values())


def G(j, x):
    return x**j + sum(comb(j, i) * a[i] * x**(j-i)
                        for i in range(2, j+1))


def f(x):
    return x**20 + sum(comb(20, i) * a[i] * x**(20-i)
                         for i in range(2, 20))


records = []
base = Path(__file__).resolve().parent
residues = json.loads((base / "two_adic/residue-patterns.json").read_text())
for m, k, expected in [(4, 16, (8, 12, 18)),
                        (16, 4, (2, 12, 18))]:
    g, q, F, P = G(m, 1), G(k, w), f(1), f(w)
    S = sp.Poly(P + w**m * q + (g+1)*(F+g+q), *variables,
                domain=sp.ZZ)
    require(all(int(c) % 2 == 0 for c in S.coeffs()),
            "The integral syzygy is not coefficientwise divisible by two")
    require(any(int(c) % 2 for c in (S+1).coeffs()),
            "The parity negative control was not detected")
    Q = sp.Poly.from_dict({powers: int(c)//2 for powers, c in S.terms()},
                         variables, domain=sp.ZZ)
    local = Q.as_expr().subs({w: 0, a[m]: 1, a[k]: 0})
    remainder = sp.Poly(local - sum(a[i] for i in expected),
                        *a.values(), domain=sp.ZZ)
    require(all(int(c) % 2 == 0 for c in remainder.coeffs()),
            "The resulting residue cut differs from the stated one")
    branch = next(b for b in residues["branches"]
                  if b["type"].startswith("A" if m == 4 else "B"))
    survivors = [p for p in branch["patterns"]
                 if sum(i in p["ones"] for i in expected) % 2 == 0]
    # The selected power-of-two equation first gives a_m=-1 mod 2O;
    # f(1)=0 then gives a_k=0 mod 2O. Thus every coefficient below
    # the opposite cluster's unit coefficient has at least valuation one.
    require(all(comb(m, j) % 2 == 0 for j in range(1, m)),
            "The power-of-two integral sharpening hypothesis failed")
    require(comb(20, k) % 2 == 1,
            "The opposite visible coefficient does not have a unit pivot")
    require(all(comb(20, j) % 2 == 0
                for j in range(2, 20) if j not in (m, k)),
            "Unexpected visible normalized coefficient")
    radius = min(Fraction(max(1, val2(comb(20, e))), k-e)
                 for e in range(1, k))
    require(radius == (Fraction(1, 14) if k == 16 else Fraction(1, 2)),
            "Unexpected opposite-cluster root bound")
    records.append({
        "unitWitnessNormalizedDegree": m,
        "oppositeWitnessNormalizedDegree": k,
        "integerIdentityTerms": len(S.terms()),
        "quotientFingerprint": hashlib.sha256(str(Q.as_expr()).encode()).hexdigest(),
        "residueCutIndices": expected,
        "survivingCoefficientPatterns": len(survivors),
        "survivingMarkedAssignments": sum(p["markedAssignmentCount"] for p in survivors),
        "oppositeClusterRootValuationLowerBound": str(radius),
    })

require([r["survivingCoefficientPatterns"] for r in records] == [465, 603],
        "Unexpected number of surviving coefficient patterns")
require(all(r["survivingMarkedAssignments"] == 40960 for r in records),
        "Unexpected number of surviving marked assignments")
print(json.dumps({"status": "PASS", "records": records,
                  "scope": "Exact integral necessary identities; no exclusion of characteristic-zero lifts"},
                 indent=2))
