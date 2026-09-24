"""Independent coefficient-first audit of the two-adic residue enumeration.

The producer iterates marked witness words and groups their coefficients.
This audit iterates every possible coefficient vector, evaluates all
normalized derivatives at both possible residue roots, and counts their
marked witness choices. It does not infer a lift or rule one out.
"""
from itertools import product
from math import comb
from pathlib import Path
from collections import Counter
import json
import subprocess
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


ROOT = Path(__file__).resolve().parents[1]
producer_path = ROOT / "two_adic/enumerate_residue_patterns.py"
raw = subprocess.run([sys.executable, str(producer_path)], check=True,
                     capture_output=True, text=True)
producer = json.loads(raw.stdout)
recorded = json.loads((ROOT / "two_adic/residue-patterns.json").read_text())
optimized_recorded = json.loads((ROOT / "two_adic/residue-patterns-optimized.json").read_text())
require(producer == recorded == optimized_recorded,
        "Fresh producer output or optimized saved receipt changed")

indices = {j: [i for i in range(j + 1) if comb(j, i) % 2]
           for j in range(1, 20)}
summary = []
for prescribed, branch in zip(({4: 1, 16: 0}, {4: 0, 16: 1}),
                              producer["branches"]):
    free = [j for j in range(2, 20) if j not in prescribed]
    independent = Counter()
    for word in product((0, 1), repeat=len(free)):
        coeff = [0] * 20
        coeff[0] = 1
        for j, value in prescribed.items():
            coeff[j] = value
        for j, value in zip(free, word):
            coeff[j] = value
        choices = 1
        for j in range(1, 20):
            at_zero = coeff[j]
            at_one = sum(coeff[i] for i in indices[j]) % 2
            choices *= int(at_zero == 0) + int(at_one == 0)
            if not choices:
                break
        if choices:
            independent[tuple(j for j in range(1, 20) if coeff[j])] = choices
    reported = {tuple(r["ones"]): r["markedAssignmentCount"]
                for r in branch["patterns"]}
    require(dict(independent) == reported, "Independent coefficient census differs")
    summary.append({"branch": branch["type"],
                    "coefficientPatterns": len(independent),
                    "markedResidueAssignments": sum(independent.values())})

five = json.loads(subprocess.run(
    [sys.executable, str(ROOT / "five_adic/check_reduction.py")],
    check=True, capture_output=True, text=True).stdout)
require(five["status"] == "PASS", "Five-adic derivative arithmetic failed")
print(json.dumps({"status": "PASS", "method": "coefficient-first census",
                  "twoAdic": summary,
                  "fiveAdicArithmetic": "PASS",
                  "scope": "Residue identities and marked incidence counts only; no lift exclusion"},
                 indent=2))
