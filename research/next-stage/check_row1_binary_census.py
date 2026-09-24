#!/usr/bin/env python3
"""Complete 16-assignment residue check for each of two row-1 supports.

This checks the specified necessary first constraint only.  It does not claim
that surviving markings extend to characteristic-zero CA polynomials.
"""
from itertools import product
from math import comb
import json

PRIME = 17
ACTIVE_SETS = ((7, 8, 10, 16), (6, 10, 15, 16))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def coefficients(active, marking):
    marks = dict(zip(active, marking))
    a = [1] + [0] * 16
    # Inactive witnesses are chosen to be zero.  Then G_j(0)=a_j=0.
    for j in range(1, 17):
        witness = marks.get(j, 0)
        a[j] = -sum(comb(j, i) * a[i] * witness**(j-i)
                    for i in range(j)) % PRIME
        if j not in active:
            require(a[j] == 0, "An inactive coefficient did not vanish")
    require(a[0] == 1 and a[1:4] == [0, 0, 0], "Initial coefficient convention")

    # Re-evaluate each normalized Hasse derivative at its marked witness.
    for j in range(1, 17):
        w = marks.get(j, 0)
        require(sum(comb(j, i) * a[i] * w**(j-i)
                    for i in range(j+1)) % PRIME == 0,
                "A reconstructed G_j fails at its witness")
    return a


def weight(j):
    quotient, remainder = divmod(comb(20, j), PRIME)
    require(remainder == 0, "A middle binomial is not divisible by 17")
    return ((19-j) - 2*comb(20-j, 3))*quotient


def constraint(a):
    return (-133 + sum(weight(j)*a[j] for j in range(4, 17))) % PRIME


def one_census(active):
    records = []
    for marking in product((0, 1), repeat=len(active)):
        a = coefficients(active, marking)
        W = constraint(a)
        records.append({"witnesses": list(marking),
                        "activeCoefficients": [a[j] for j in active],
                        "W": W})
    require(len(records) == 16, "Incomplete binary marking count")
    require(len({tuple(r["witnesses"]) for r in records}) == 16,
            "Duplicate binary marking")
    surviving = [r for r in records if r["W"] == 0]
    expected = [{"witnesses": [0, 0, 0, 1],
                 "activeCoefficients": [0, 0, 0, 16], "W": 0}]
    require(surviving == expected, "Unexpected first-constraint survivors")
    require(constraint([1]+[0]*16) != 0, "The zero marking must be excluded")
    wrong_constant = [(r["W"]+1) % PRIME for r in records]
    require([i for i, r in enumerate(records) if r["W"] == 0] !=
            [i for i, value in enumerate(wrong_constant) if value == 0],
            "Constant-mutation control failed")
    return {"activeDeficiencies": list(active),
            "fullDeficiencySupport": sorted((*active, 17, 19)),
            "assignmentCount": len(records),
            "weightsModulo17": [weight(j) % PRIME for j in active],
            "survivors": surviving, "allAssignments": records}


def main():
    result = [one_census(active) for active in ACTIVE_SETS]
    print(json.dumps({
        "status": "PASS", "prime": PRIME, "censuses": result,
        "totalAssignments": sum(x["assignmentCount"] for x in result),
        "scope": "All binary residue markings of G_4,...,G_16 at the stated "
                 "supports, filtered by the specified divided first constraint. "
                 "No characteristic-zero lift or complete branch exclusion is claimed."
    }, indent=2))


if __name__ == "__main__":
    main()
