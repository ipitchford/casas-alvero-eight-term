"""Independent small arithmetic audit; does not enumerate 4**13 assignments."""
import json
from itertools import product
from math import comb
from pathlib import Path
from random import Random

P = 17
ZERO, ONE, ZETA = (0, 0), (1, 0), (0, 1)


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def mul(x, y):
    # Polynomial multiplication followed by zeta**2 = -zeta-1.
    return ((x[0]*y[0] - x[1]*y[1]) % P,
            (x[0]*y[1] + x[1]*y[0] - x[1]*y[1]) % P)


def power(x, n):
    out = ONE
    for _ in range(n):
        out = mul(out, x)
    return out


def scale(c, x):
    return (c*x[0] % P, c*x[1] % P)


def encode(x):
    return x[0] + P*x[1]


roots = [ZERO, ONE, ZETA, power(ZETA, 2)]
require(all((x*x+x+1) % P for x in range(P)), "quadratic reducible")
require(power(ZETA, 3) == ONE, "zeta order")
for u, v in product(range(P), repeat=2):
    x = (u, v)
    require(encode(mul(x, ZETA)) == ((17-v) % 17)+17*((u-v+17) % 17),
            "C++ rotate1 disagrees")
    require(encode(mul(x, power(ZETA, 2))) == ((v-u+17) % 17)+17*((17-u) % 17),
            "C++ rotate2 disagrees")
require(1-1140 == -17*67 and 190-3*1140 == -17*190,
        "exact divided constants")
require(all(comb(20, j) % 17 == 0 for j in range(4, 17)),
        "middle divisibility")
require(all(comb(17, i) % 17 == 0 for i in range(1, 17)), "G17")
require(all(comb(18, i) % 17 == 0 for i in range(2, 17)), "G18")
require(all(comb(19, i) % 17 == 0 for i in range(3, 17)), "G19")


def coefficients(word):
    a = [ZERO] * 17
    a[0], a[3] = ONE, (16, 0)
    for j, choice in enumerate(word, 4):
        rho = roots[choice]
        direct = ZERO
        for i in range(j):
            direct = add(direct, scale(comb(j, i), mul(a[i], power(rho, j-i))))
        a[j] = scale(-1, direct)
        simplified = ZERO if choice == 0 else scale(comb(j, 3)-1, power(rho, j))
        if choice:
            for i in range(4, j):
                simplified = add(simplified, scale(-comb(j, i), mul(a[i], power(rho, j-i))))
        require(a[j] == simplified, "full G_j versus simplified recurrence")
    return a


single = []
for j, choice in product(range(4, 17), range(1, 4)):
    word = [0]*13
    word[j-4] = choice
    a = coefficients(word)
    value = ZERO
    for i in range(4, 17):
        value = add(value, scale(comb(20, i)//17, a[i]))
    if value == (16, 0):
        single.append([j, choice-1, encode(a[j])])
require(single == [[11, 0, 11]], "single-unit result")
rng = Random(20260923)
for _ in range(1024):
    coefficients([rng.randrange(4) for _ in range(13)])

here = Path(__file__).resolve().parent
producer = json.loads((here / "row8-residue-enumeration.json").read_text())
replay = json.loads((here / "audit-native-replay.json").read_text())
require(producer == replay, "native replay differs from producer receipt")
require(sum(replay["histogramByNumberOfUnitWitnesses"]) == 233310, "identity census")
require(sum(replay["filteredHistogram"]) == 180341, "filtered census")
print(json.dumps({"status": "PASS", "singleUnit": single,
                  "recurrenceSpotChecks": 1024, "nativeReceiptEqual": True,
                  "scope": "Small independent arithmetic checks and separately compiled native replay; no characteristic-zero lift claim."}, indent=2))
