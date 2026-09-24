#!/usr/bin/env python3
"""Replay the finite arithmetic example in P19_CLUSTER_FIRST_JET.md."""
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    p = 19
    support = (12, 13, 15, 16, 17, 19)
    c = [0, 0] + [comb(19, i - 1) // 19 for i in range(2, 20)]
    for i in range(2, 20):
        require(19 * c[i] == comb(19, i - 1), "nonintegral divided coefficient")
        require(c[i] % p == (-1) ** i * pow(i - 1, -1, p) % p,
                "divided coefficient residue")
    alpha = [1, 0]
    matrix = [[0] * 20 for _ in range(20)]
    for i in range(2, 20):
        if i not in support:
            alpha.append(0)
            continue
        alpha.append(-sum(comb(i, j) * alpha[j] for j in range(i)))
        for m in support:
            matrix[i][m] = -sum(comb(i, j) * matrix[j][m] for j in range(i))
            if i == m:
                matrix[i][m] -= i * sum(comb(i - 1, j) * alpha[j] for j in range(i))
    b = [sum(comb(i, j) * alpha[j] for j in range(i + 1)) for i in range(20)]
    f0 = sum(c[i] * alpha[i] for i in range(2, 20))
    weights = {m: sum(c[i] * matrix[i][m] for i in range(2, 20)) % p
               for m in support}
    require([alpha[j] for j in support] == [-1, 12, -806, 7995, -48672, 3424616],
            "constant coefficients")
    require(all(alpha[i] == 0 or b[i] == 0 for i in range(2, 20)),
            "constant scenario derivative equations")
    require(f0 == 2107898 and f0 % p == 0, "constant divided identity")
    require(alpha[19] % p == 18 and b[18] % p == 5, "residue endpoints")
    require(weights == {12: 9, 13: 0, 15: 15, 16: 0, 17: 0, 19: 0},
            "first-jet weights")
    require(sum(weights.values()) % p == b[18] % p, "weight-sum identity")
    ratio = -weights[12] * pow(weights[15], -1, p) % p
    require(ratio == 7 and pow(ratio, 17, p) != 1, "two-phase obstruction")
    phases = {j: int(j == 13) for j in support}
    require(sum(weights[j] * phases[j] for j in support) % p == 0,
            "surviving first-jet assignment")
    print(json.dumps({"status": "PASS", "scope": "finite first-jet example only",
                      "support": support, "constant_F": f0, "b18_mod19": b[18] % p,
                      "weights_mod19": weights, "forced_zero_displacements": [12, 15],
                      "surviving_phase_assignment": phases}, indent=2))


if __name__ == "__main__":
    main()
