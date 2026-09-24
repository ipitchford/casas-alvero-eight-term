"""Construct explicit partial-incidence families, never CA counterexamples.

All arithmetic is exact, using only the Python standard library. The chosen
supports already occur in the complete earlier necessary-criterion inventory.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def require(ok, why):
    if not ok:
        raise ValueError(why)


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def multiply(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def remainder(a, b):
    a = [F(v) for v in a]
    while len(a) >= len(b):
        z, k = a[-1]/b[-1], len(a)-len(b)
        for j, v in enumerate(b):
            a[k+j] -= z*v
        trim(a)
    return a


def hasse_at(a, k, root):
    return sum(c*comb(i, k)*root**(i-k) for i, c in enumerate(a) if i >= k)


def monomial(degree):
    return [0]*degree+[1]


QUAD = [3, 3, 1]
QUAD2 = multiply(QUAD, QUAD)


def constraints(row, a):
    if row == 4:
        rem = remainder(a, QUAD2)
        return [hasse_at(a, 0, 1), hasse_at(a, 0, 6), hasse_at(a, 2, 6)] + rem + [0]*(4-len(rem))
    if row == 6:
        return [hasse_at(a, 0, 1), hasse_at(a, 0, 6), hasse_at(a, 2, 6),
                hasse_at(a, 0, 10), hasse_at(a, 1, 10)]
    if row == 7:
        return [hasse_at(a, 0, 1), hasse_at(a, 2, 1),
                hasse_at(a, 0, 7), hasse_at(a, 1, 7)]
    if row == 9:
        return [hasse_at(a, k, 1) for k in range(3)]
    raise ValueError(row)


def modular_pivots(matrix, p=17):
    m = [[int(v) % p for v in row] for row in matrix]
    out, row = [], 0
    for col in range(len(m[0])):
        pivot = next((r for r in range(row, len(m)) if m[r][col]), None)
        if pivot is None:
            continue
        m[row], m[pivot] = m[pivot], m[row]
        inv = pow(m[row][col], -1, p)
        m[row] = [v*inv % p for v in m[row]]
        for r in range(len(m)):
            if r != row:
                c = m[r][col]
                m[r] = [(a-c*b) % p for a, b in zip(m[r], m[row])]
        out.append(col)
        row += 1
        if row == len(m):
            break
    return out


def solve(square, rhs):
    n = len(square)
    a = [[F(v) for v in row]+[F(b)] for row, b in zip(square, rhs)]
    for j in range(n):
        r = next(r for r in range(j, n) if a[r][j])
        a[j], a[r] = a[r], a[j]
        v = a[j][j]
        a[j] = [x/v for x in a[j]]
        for r in range(n):
            if r != j:
                v = a[r][j]
                a[r] = [x-v*y for x, y in zip(a[r], a[j])]
    return [row[-1] for row in a]


def mod_fraction(q, p):
    q = F(q)
    return q.numerator*pow(q.denominator, -1, p) % p


def gcd_mod(a, b, p):
    a = trim([int(v) % p for v in a])
    b = trim([int(v) % p for v in b])
    while b:
        r = a.copy()
        while len(r) >= len(b):
            z, k = r[-1]*pow(b[-1], -1, p) % p, len(r)-len(b)
            for j, v in enumerate(b):
                r[k+j] = (r[k+j]-z*v) % p
            trim(r)
        a, b = b, r
    return [(v*pow(a[-1], -1, p)) % p for v in a]


def pair(q):
    q = F(q)
    return [q.numerator, q.denominator]


def construct(row, support, seed):
    fixed = {2: -190, 3: 0} if row == 4 else {2: -190, 3: 2280}
    if row == 9:
        fixed = {2: 0, 3: -1140}
    a = [F(0)]*21
    a[20] = F(1)
    for j, value in fixed.items():
        a[20-j] = F(value)
    a[2], a[1] = F(seed[3]), F(seed[4])
    unknown = sorted(set(support)-set(fixed))
    matrix = list(map(list, zip(*(constraints(row, monomial(20-j)) for j in unknown))))
    c0 = constraints(row, a)
    require(all(v.denominator == 1 and v.numerator % 17 == 0 for v in c0), 'bad seed residue')
    rhs = [-v/17 for v in c0]
    pivots = modular_pivots(matrix)
    require(len(pivots) == len(matrix), f'row {row}: rank loss')
    free = [j for j in range(len(unknown)) if j not in pivots]
    square = [[line[j] for j in pivots] for line in matrix]

    def point(parameters):
        z = [F(0)]*len(unknown)
        for i, j in enumerate(free):
            z[j] = F(parameters[i])
        rr = [rhs[i]-sum(matrix[i][j]*z[j] for j in free) for i in range(len(matrix))]
        zz = solve(square, rr)
        for j, value in zip(pivots, zz):
            z[j] = value
        out = a.copy()
        for j, value in zip(unknown, z):
            out[20-j] += 17*value
        return out

    selected = None
    for shift in range(1, 30):
        parameters = [F(shift+i) for i in range(len(free))]
        f = point(parameters)
        actual = [j for j in range(2, 20) if f[20-j]]
        if actual == support:
            selected = parameters
            break
    require(selected is not None, f'row {row}: could not realize full support')
    require(all(v == 0 for v in constraints(row, f)), f'row {row}: incidence failure')
    require(f[19] == f[0] == f[3] == 0, 'center/constant/H3')
    for j, value in fixed.items():
        require(f[20-j] == value, 'fixed coefficient')
    reduction = [mod_fraction(v, 17) for v in f]
    expected = [0]*21
    expected[20] = 1
    expected[18], expected[17], expected[3], expected[2], expected[1] = seed
    require(reduction == expected, 'full seed mismatch')
    require(all((f[20-j]/comb(20, j)).denominator % 17 for j in range(21)), 'normalized integrality')
    # Explicitly validate each visible Hasse incidence, not just matrix rank.
    witnesses = {19: 0, 3: 0}
    if row == 4:
        witnesses.update({18: 1, 17: 0, 2: 6})
        require(not remainder(f, QUAD2), 'row4 double factors')
    elif row == 6:
        witnesses.update({18: 1, 17: 1, 2: 6, 1: 10})
    elif row == 7:
        witnesses.update({18: 1, 17: 1, 2: 1, 1: 7})
    else:
        witnesses.update({18: 0, 17: 1, 2: 1, 1: 1})
    for k, r in witnesses.items():
        require(hasse_at(f, 0, r) == hasse_at(f, k, r) == 0, f'visible H{k}')
    # Record deterministic exact coprimality obstructions for unresolved orders.
    failures = []
    for k in range(4, 17):
        if f[k] == 0:
            continue
        for p in [101, 103, 107, 109, 113, 127]:
            if any(v.denominator % p == 0 for v in f) or comb(20, k) % p == 0:
                continue
            ff = [mod_fraction(v, p) for v in f]
            dd = [ff[i]*comb(i, k) % p for i in range(k, 21)]
            if gcd_mod(ff, dd, p) == [1]:
                failures.append({'hasseOrder': k, 'prime': p, 'monicModularGcd': [1]})
                break
    require(bool(failures), 'no certified failure of CA found')
    # An affine basis verifies the whole partial-incidence family, not one point.
    origin = point([0]*len(free))
    directions = []
    for i in range(len(free)):
        unit = [0]*len(free)
        unit[i] = 1
        direction = [v-w for v, w in zip(point(unit), origin)]
        require(all(v == 0 for v in constraints(row, direction)), 'kernel incidence')
        require(direction[20] == direction[19] == direction[0] == direction[3] == 0, 'kernel fixed')
        directions.append(direction)
    return {'row': row, 'deficiencySupport': support, 'seed': seed,
            'unknownIndices': unknown, 'pivotColumns': pivots,
            'freeColumns': free, 'linearRankModulo17': len(pivots),
            'familyDimension': len(free), 'selectedParameters': list(map(pair, selected)),
            'polynomialCoefficientsLowToHigh': list(map(pair, f)),
            'familyOriginLowToHigh': list(map(pair, origin)),
            'familyDirectionsLowToHigh': [list(map(pair, v)) for v in directions],
            'visibleRationalWitnesses': witnesses,
            'additionalDoubleFactor': QUAD if row == 4 else None,
            'certifiedFailedDerivativeConditions': failures}


def main():
    inventory = json.loads((BASE.parent/'support_frontier/inventory.json').read_text())
    surviving = inventory['finalSurvivors']
    choices = {
        4: ([2,4,5,6,7,8,9,10,11,12,14,15,18,19], [14,0,0,11,8]),
        6: ([2,3,4,6,7,8,9,10,11,12,13,14,15,18,19], [14,2,0,11,6]),
        7: ([2,3,4,6,7,8,9,10,11,12,13,14,15,18,19], [14,2,0,14,3]),
        9: ([3,4,5,6,7,8,9,10,11,12,14,15,16,18,19], [0,16,0,14,3])}
    conditions = {4: ({2,18,19},{3,17}), 6: ({2,3,18,19},{17}),
                  7: ({2,3,18,19},{17}), 9: ({3,18,19},{2,17})}
    counts = {}
    for row, (required, forbidden) in conditions.items():
        allowed = [s for s in surviving if required <= set(s) and not forbidden & set(s)]
        counts[str(row)] = {'required': sorted(required), 'forbidden': sorted(forbidden),
            'supportCount': len(allowed), 'maxNonleadingTerms': max(map(len, allowed))}
    result = {'status': 'PARTIAL INCIDENCE FAMILIES, NOT CA POLYNOMIALS',
              'branchSupportCounts': counts, 'rows': []}
    for row, (support, seed) in choices.items():
        require(support in surviving, 'support not in necessary-criterion inventory')
        result['rows'].append(construct(row, support, seed))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
