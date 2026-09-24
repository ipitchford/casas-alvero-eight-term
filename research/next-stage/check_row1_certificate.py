#!/usr/bin/env python3
"""Read-only independent integer-convolution check of the row-1 certificate.

The certificate producer used rational polynomial Euclidean division.  This
checker does no polynomial division and uses no producer code or external CAS.
Every condition uses explicit exceptions and remains active under python -O.
"""
from pathlib import Path
from math import gcd
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(poly):
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return result


def convolution(left, right):
    if not left or not right:
        return []
    result = [0] * (len(left) + len(right) - 1)
    for i in range(len(left)):
        for j in range(len(right)):
            result[i + j] += left[i] * right[j]
    return trim(result)


def add(left, right):
    result = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        result[i] += value
    for i, value in enumerate(right):
        result[i] += value
    return trim(result)


def valuation17(value):
    require(value != 0, "Valuation of zero is not finite")
    value = abs(value)
    exponent = 0
    while value % 17 == 0:
        value //= 17
        exponent += 1
    return exponent


def source_polynomials():
    # Construct from the mathematical statement, not certificate coefficient data.
    P = [0] * 20
    for degree, coefficient in ((19, -4844), (18, 19380), (16, -14535),
                                (2, -1140), (0, 1139)):
        P[degree] = coefficient
    Q = [0] * 20
    for degree, coefficient in ((19, -14516), (18, 38760), (2, -2280)):
        Q[degree] = coefficient
    return P, Q


def check_identity(A, B, D, P, Q):
    require(D > 0, "D must be a positive nonzero integer")
    total = add(convolution(A, P), convolution(B, Q))
    require(total == [D], "The integer polynomial AP+BQ is not D")
    require(valuation17(D) == 3, "D does not have 17-adic valuation three")
    require(gcd(D, *A, *B) == 1, "Certificate was not made primitive")


def main():
    path = ROOT / "row1-certificate.json"
    raw = path.read_bytes()
    certificate = json.loads(raw)
    require(certificate["coefficientOrder"] == "ascending", "Wrong coefficient order")
    require(certificate["format"] == "integer-polynomial-bezout-v1", "Wrong format")
    P, Q = source_polynomials()
    require(certificate["P"] == P and certificate["Q"] == Q,
            "Certificate names a different pair of source polynomials")
    A = [int(x) for x in certificate["A"]]
    B = [int(x) for x in certificate["B"]]
    D = int(certificate["D"])
    require(len(A) == len(B) == 19 and A[-1] and B[-1],
            "Unexpected multiplier degrees")
    check_identity(A, B, D, P, Q)

    mutated = A[:]
    mutated[0] += 1
    rejected = False
    try:
        check_identity(mutated, B, D, P, Q)
    except ValueError:
        rejected = True
    require(rejected, "A one-coefficient mutation was accepted")
    rejected_constant = False
    try:
        check_identity(A, B, D + 1, P, Q)
    except ValueError:
        rejected_constant = True
    require(rejected_constant, "A false Bezout constant was accepted")

    print(json.dumps({
        "status": "PASS",
        "certificateSHA256": hashlib.sha256(raw).hexdigest(),
        "degrees": {"P": 19, "Q": 19, "A": 18, "B": 18},
        "D": str(D),
        "Ddiv17cubedModulo17": (D // 17**3) % 17,
        "v17D": valuation17(D),
        "identity": "A*P+B*Q=D in Z[X]",
        "negativeControls": {
            "changedAConstantRejected": rejected,
            "changedDRejected": rejected_constant
        },
        "scope": "At an integral input, min(v17(P),v17(Q))<=3. "
                 "The local characteristic-zero application requires its own hypotheses."
    }, indent=2))


if __name__ == "__main__":
    main()
