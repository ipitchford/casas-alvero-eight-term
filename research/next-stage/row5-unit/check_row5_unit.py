#!/usr/bin/env python3
"""Reconstruct the four exact row-5 systems and check integer Bezout identities.

Uses only the Python standard library.  No polynomial gcd, rational division,
CAS, or certificate-producer code is used.  Conditions remain active under -O.
"""
from pathlib import Path
from math import comb
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def add(*polynomials):
    result = [0]*max((len(p) for p in polynomials), default=0)
    for poly in polynomials:
        for degree, value in enumerate(poly):
            result[degree] += value
    return canonical(result)


def scale(poly, integer):
    return canonical([integer*value for value in poly])


def multiply(left, right):
    if not left or not right:
        return []
    result = [0]*(len(left)+len(right)-1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            result[i+j] += value*other
    return canonical(result)


def power(poly, exponent):
    result = [1]
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def evaluate(polynomial_in_X, at):
    """The input is a dict from X degree to an integer polynomial in r."""
    answer = []
    for degree in range(max(polynomial_in_X), -1, -1):
        answer = add(multiply(answer, at), polynomial_in_X.get(degree, []))
    return answer


def normalized_G(a, order_degree, witness):
    return add(*(scale(multiply(a.get(i, []),
                               power(witness, order_degree-i)),
                       comb(order_degree, i))
                 for i in range(order_degree+1)))


def reconstruct(g3, g12):
    # Here "one" denotes the exact root 1, not merely residue 1.
    one, r = [1], [0, 1]
    require(g3 in ("one", "r") and g12 in ("one", "r"), "Unknown witness label")
    a = {0: [1], 1: [], 2: [-1]}
    witnesses = {3: one if g3 == "one" else r, 4: r, 10: one,
                 12: one if g12 == "one" else r}
    for j in (3, 4, 10, 12):
        a[j] = scale(normalized_G(a, j, witnesses[j]), -1)
        require(not normalized_G(a, j, witnesses[j]), "Incorrect G_j solution")

    f = {20-j: scale(value, comb(20, j)) for j, value in a.items()}
    # Set the ordinary coefficient E of X so that f(1)=0.
    E = scale(evaluate(f, one), -1)
    f[1] = E
    require(not evaluate(f, one), "The exact root 1 was not retained")
    require(not normalized_G(a, 2, one), "G_2(1) does not vanish")
    derivative = {degree-1: scale(value, degree)
                  for degree, value in f.items() if degree > 0}
    return a, E, evaluate(f, r), evaluate(derivative, one)


def verify_identity(A, P, B, Q, constant):
    require(constant != 0, "The Bezout constant must be nonzero")
    require(add(multiply(A, P), multiply(B, Q)) == [constant],
            "Integer Bezout identity failed")


def v17(integer):
    integer = abs(integer)
    require(integer != 0, "Infinite valuation is not expected")
    result = 0
    while integer % 17 == 0:
        integer //= 17
        result += 1
    return result


def main():
    path = ROOT/"row5-unit-certificates.json"
    raw = path.read_bytes()
    data = json.loads(raw)
    require(data["coefficientOrder"] == "ascending", "Wrong coefficient order")
    expected = {(g3, g12) for g3 in ("one", "r") for g12 in ("one", "r")}
    require(len(data["cases"]) == 4, "Expected four cases")
    found, reports = set(), []
    for case in data["cases"]:
        labels = case["G3Witness"], case["G12Witness"]
        require(labels in expected and labels not in found, "Case coverage error")
        found.add(labels)
        a, E, P, Q = reconstruct(*labels)
        for j in (3, 4, 10, 12):
            require(case["a"+str(j)] == a[j], "Wrong normalized coefficient")
        require(case["E"] == E, "Wrong ordinary linear coefficient")
        require(case["F_at_r"] == P, "Wrong f(r) polynomial")
        require(case["Fprime_at_one"] == Q, "Wrong f'(1) polynomial")
        require(case["gcdTarget"] == [1], "The certificate is not a unit identity")
        A = [int(x) for x in case["multiplierA"]]
        B = [int(x) for x in case["multiplierB"]]
        D = int(case["integerConstant"])
        verify_identity(A, P, B, Q, D)
        wrong = A[:]
        if not wrong:
            wrong = [1]
        else:
            wrong[0] += 1
        rejected = False
        try:
            verify_identity(wrong, P, B, Q, D)
        except ValueError:
            rejected = True
        require(rejected, "Multiplier mutation was accepted")
        reports.append({
            "G3Witness": labels[0], "G12Witness": labels[1],
            "degrees": {"f(r)": len(P)-1, "fprime(1)": len(Q)-1,
                        "A": len(A)-1, "B": len(B)-1},
            "integerConstant": str(D), "v17Constant": v17(D),
            "identity": "A*f(r)+B*fprime(1)=nonzero integer",
            "coefficientMutationRejected": rejected
        })
    require(found == expected, "Incomplete four-case cover")
    print(json.dumps({
        "status": "PASS",
        "certificateSHA256": hashlib.sha256(raw).hexdigest(),
        "cases": reports,
        "conclusion": "All four exact unit-witness systems are inconsistent "
                      "over every characteristic-zero field.",
        "scope": "Requires exact H1 witness 1, G4 witness r, G10 witness 1, "
                 "G3 witness 1 or r, and G12 witness 1 or r. "
                 "No zero-residue G10/G12 branch is addressed."
    }, indent=2))


if __name__ == "__main__":
    main()
