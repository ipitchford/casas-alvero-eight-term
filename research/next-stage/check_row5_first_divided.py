#!/usr/bin/env python3
"""Independent exact constants and complete 27-assignment row-5 residue sieve."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json

P = 17
J = (4, 10, 12)
C = {j: comb(20, j) for j in J}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def evaluate(coefficients, x):
    value = 0
    for c in reversed(coefficients):
        value = value*x+c
    return value


def hasse(coefficients, k):
    return [comb(e, k)*coefficients[e] for e in range(k, len(coefficients))]


def family(a3, middle):
    f = [0]*21
    f[20], f[18], f[17] = 1, -190, 1140*a3
    for j in J:
        f[20-j] = C[j]*middle.get(j, 0)
    f[1] = -sum(f)
    return f


base = family(2, {})
directions = {}
for j in J:
    g = family(2, {j: 1})
    directions[j] = [x-y for x, y in zip(g, base)]
a3_direction = [x-y for x, y in zip(family(3, {}), base)]
need(evaluate(base, 1) == 0, "base root 1")
need(base[1] == -17*123, "base low coefficient")
need(evaluate(hasse(base, 1), 1) == 17*1957, "base first derivative")
need(evaluate(hasse(a3_direction, 1), 1) == 18240, "a3 derivative direction")
need(evaluate(hasse(base, 2), 1) % P == 3, "second Hasse coefficient")
need(evaluate(hasse(a3_direction, 2), 1) % P == 0, "second Hasse a3 direction")
for j in J:
    need(all(c % P == 0 for c in directions[j]), "nonintegral divided direction")
    need(evaluate(hasse(directions[j], 1), 1) == (19-j)*C[j],
         "first derivative weight")

fminus2 = [evaluate(base, -2)] + [evaluate(directions[j], -2) for j in J]
need(all(v % P == 0 for v in fminus2), "coefficientwise divisibility at -2")
divided = [v//P for v in fminus2]
need(divided == [-20446986, 18678330, 11150568, 1911780],
     "divided affine values at -2")
need([v % P for v in divided] == [2, 5, 13, 11], "divided affine residues")

# Total derivative after the exact substitution a3(y)=-y^3+3y.
total_jacobian = (evaluate(hasse(base, 1), -2)
                  -9*evaluate(a3_direction, -2))
need(total_jacobian % P == 16, "implicit total derivative")
need((-18240*9) % P == 9 and (1140*9) % P == 9,
     "t signs in the two divided constraints")
need(comb(19, 2) % P != 0, "G19 a2 coefficient must be a unit")
need(all(comb(19, j) % P == 0 for j in (3, 4, 10, 12)),
     "G19 middle coefficients must be 17-divisible")
delta = Fraction(1, 9)
need(17*delta == 1+8*delta < 18*delta, "zero-cluster radius boundary")
need(min(17*delta, 1+7*delta) == Fraction(16, 9), "linear coefficient bound")

# Root-domain completeness follows from h=X^17(X-1)^2(X+2).
h = [c % P for c in base]
need(h[20] == 1 and h[18] == 14 and h[17] == 2
     and all(h[e] == 0 for e in range(21) if e not in (17, 18, 20)),
     "seed differs")
need(evaluate(hasse(h, 1), -2) % P == 16, "simple residue -2")
need(evaluate(hasse(h, 1), 1) % P == 0
     and evaluate(hasse(h, 2), 1) % P == 3, "double residue 1")

records = []
survivors = {(y, w): [] for y in (1, -2) for w in (0, 1)}
for marks in product((0, 1, -2), repeat=3):
    chosen = dict(zip(J, marks))
    a = {0: 1, 1: 0, 2: -1, 3: 2}
    for j in range(4, 17):
        rho = chosen.get(j, 0)
        a[j] = -sum(comb(j, i)*a[i]*rho**(j-i) for i in range(j)) % P
        if j not in J:
            need(a[j] == 0, "inactive exact coefficient")
        need(sum(comb(j, i)*a[i]*rho**(j-i) for i in range(j+1)) % P == 0,
             "reconstructed normalized derivative")
    t = (-(divided[0]+sum(divided[k+1]*a[j] for k, j in enumerate(J)))
         * pow(16, -1, P)) % P
    branch_values = {}
    for y in (1, -2):
        tau = 0 if y == 1 else t
        val0 = (-123-sum((C[j]//17)*a[j] for j in J)+9*tau) % P
        val1 = (1957+sum((19-j)*(C[j]//17)*a[j] for j in J)+9*tau) % P
        for w, value in ((0, val0), (1, val1)):
            branch_values[f"y{y}_w{w}"] = value
            if value == 0:
                survivors[y, w].append({
                    "middleWitnessResidues": list(marks),
                    "middleCoefficientResidues": [a[j] for j in J],
                    "correctionT": tau,
                })
    records.append({"witnesses": list(marks), "coefficients": [a[j] for j in J],
                    "minus2CorrectionT": t, "dividedValues": branch_values})
need(len(records) == 27, "incomplete Cartesian product")
need([len(survivors[y, w]) for y in (1, -2) for w in (0, 1)] == [0, 2, 2, 6],
     "branch survivor counts differ")
need({tuple(r["middleWitnessResidues"]) for r in survivors[1, 1]}
     == {(-2, 0, -2), (-2, 1, -2)}, "near-one survivors differ")
need({tuple(r["middleWitnessResidues"]) for r in survivors[-2, 0]}
     == {(-2, 0, 0), (-2, 1, 0)}, "zero repeated-root survivors differ")
need({tuple(r["middleWitnessResidues"]) for r in survivors[-2, 1]}
     == {(-2, r10, r12) for r10 in (0, 1) for r12 in (0, 1, -2)},
     "near-one repeated-root survivors differ")

print(json.dumps({
    "status": "PASS",
    "support": [2, 3, 4, 10, 12, 19],
    "middleIndices": list(J),
    "assignments": 27,
    "branchTests": 108,
    "dividedBaseAtMinus2": divided,
    "dividedBaseAtMinus2Residues": [v % P for v in divided],
    "totalJacobianAtMinus2Mod17": 16,
    "zeroRepeatedRootRadiusBound": "1/9",
    "linearCoefficientValuationBound": "16/9",
    "branches": [
        {"G3WitnessResidue": y, "H1WitnessResidue": w,
         "survivorCount": len(survivors[y, w]), "survivors": survivors[y, w]}
        for y in (1, -2) for w in (0, 1)
    ],
    "allAssignments": records,
    "checkerSha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Complete first-divided necessary residue sieve; ten marked "
             "branch assignments survive; no row-5 or global support exclusion.",
}, indent=2))
