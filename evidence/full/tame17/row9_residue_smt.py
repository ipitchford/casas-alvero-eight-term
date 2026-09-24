#!/usr/bin/env python3
"""Bounded complete-domain residue search for the row-9 extra equation.

This is a search prototype, not a proof-producing unsatisfiability checker.
All returned points are independently replayed in the finite field. The
model covers all marked residue assignments, not characteristic-zero lifts.
"""
import argparse
import json
from math import comb
import subprocess
import sys
import time

import flint
import z3


def require(condition, message):
    if not condition:
        raise ValueError(message)


parser = argparse.ArgumentParser()
parser.add_argument("--timeout-ms", type=int, default=30000)
parser.add_argument("--wall-seconds", type=float, default=60)
parser.add_argument("--nonprime", action="store_true")
parser.add_argument("--_worker", action="store_true", help=argparse.SUPPRESS)
args = parser.parse_args()
if not args._worker:
    require(args.wall_seconds > 0, "The wall-clock limit must be positive")
    # The solver's internal timeout is advisory during some native kernels.
    # Run it in a separately killable process, including model construction.
    try:
        child = subprocess.run([sys.executable, __file__, *sys.argv[1:], "--_worker"],
                               text=True, capture_output=True,
                               timeout=args.wall_seconds)
    except subprocess.TimeoutExpired:
        print(json.dumps({"status": "external_wall_timeout",
                          "wallSeconds": args.wall_seconds,
                          "scope": "No solver result or mathematical conclusion"}, indent=2))
        raise SystemExit(0)
    if child.stderr:
        print(child.stderr, file=sys.stderr, end="")
    print(child.stdout, end="")
    raise SystemExit(child.returncode)
started = time.monotonic()

q = [-8, 7, 4, -6, 1, 0, 6, 0, -1, 4, 1]
K = flint.fq_default_ctx(modulus=flint.fmpz_mod_poly_ctx(17)(q), var="z")
P = flint.fq_default_poly_ctx(K)
X = P.gen()
h = X**20-X**17+14*X**2+3*X
_, factors = h.factor()
require(all(g.degree() == 1 for g, _ in factors), "The seed did not split")


def vector(a):
    values = [int(c) for c in a.to_list()]
    return tuple(values + [0]*(10-len(values)))


roots = sorted([-g[0]/g[1] for g, _ in factors], key=vector)
require(len(roots) == 18 and len(set(map(vector, roots))) == 18,
        "Wrong number of distinct residue roots")
require(all(h(r).is_zero() for r in roots), "Root replay failed")
basis = [K([0]*j+[1]) for j in range(10)]
powers = [[r**j for j in range(17)] for r in roots]
# Multiplication by a fixed residue root power is a linear map over F17.
matrices = [[[vector(power*b) for b in basis] for power in row] for row in powers]
solver = z3.Solver()
solver.set(timeout=args.timeout_ms)
coefficients = [[z3.IntVal(int(j == 0))]+[z3.IntVal(0)]*9 for j in range(17)]
coefficients[3][0] = z3.IntVal(16)
choice = {}
for j in range(4, 17):
    coefficients[j] = [z3.Int(f"a{j}_{d}") for d in range(10)]
    solver.add(*[z3.And(v >= 0, v < 17) for v in coefficients[j]])
    choice[j] = z3.Int(f"root{j}")
    solver.add(choice[j] >= 0, choice[j] < 18)
    for ri in range(18):
        equations = []
        for d in range(10):
            terms = [coefficients[j][d]]
            for i in range(j):
                multiplier = comb(j, i) % 17
                if not multiplier:
                    continue
                matrix = matrices[ri][j-i]
                for c in range(10):
                    scalar = multiplier*matrix[c][d] % 17
                    if scalar:
                        terms.append(scalar*coefficients[i][c])
            equations.append(z3.Sum(terms) % 17 == 0)
        solver.add(z3.Implies(choice[j] == ri, z3.And(equations)))

weights = {j: comb(19-j, 2)*(comb(20, j)//17) % 17 for j in range(4, 17)}
for d in range(10):
    solver.add((z3.Sum([weights[j]*coefficients[j][d] for j in range(4, 17)])
                + (-8037 if d == 0 else 0)) % 17 == 0)
if args.nonprime:
    nonprime_indices = [i for i, r in enumerate(roots) if any(vector(r)[1:])]
    solver.add(z3.Or([choice[j] == i for j in choice for i in nonprime_indices]))

build_seconds = time.monotonic()-started
result = solver.check()
output = {"status": str(result), "buildSeconds": build_seconds,
          "elapsedSeconds": time.monotonic()-started,
          "scope": "Residue assignments only; no characteristic-zero conclusion",
          "fieldModulusAscending": [c % 17 for c in q],
          "distinctRootCount": 18,
          "markedAssignmentUpperBound": 18**13}
if result == z3.sat:
    model = solver.model()
    selected = {j: model.eval(choice[j]).as_long() for j in choice}
    a = [K(1), K(0), K(0), K(-1)]
    for j in range(4, 17):
        r = roots[selected[j]]
        aj = -sum((K(comb(j,i))*a[i]*r**(j-i) for i in range(j)), K(0))
        require(vector(aj) == tuple(model.eval(v).as_long() for v in coefficients[j]),
                "Model and independent triangular recurrence differ")
        a.append(aj)
    T = K(-8037)+sum((K(weights[j])*a[j] for j in weights), K(0))
    require(T.is_zero(), "The extra residue equation failed replay")
    output["witnesses"] = {j: vector(roots[ri]) for j, ri in selected.items()}
    output["coefficients"] = {j: vector(a[j]) for j in range(4,17)}
    output["independentFiniteFieldReplay"] = "PASS"
elif result == z3.unknown:
    output["reason"] = solver.reason_unknown()
else:
    output["warning"] = "No independent unsatisfiability certificate was exported"
print(json.dumps(output, indent=2))
