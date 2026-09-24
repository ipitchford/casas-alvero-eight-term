"""Replay the saved rational families without importing the constructor."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def require(ok, why):
    if not ok:
        raise ValueError(why)


def unpack(values):
    return [Fraction(n, d) for n, d in values]


def eval_hasse(f, k, r):
    out = Fraction(0)
    for i in range(len(f)-1, k-1, -1):
        out = out*r+comb(i, k)*f[i]
    return out


def quad_square_remainder(f):
    q = [9, 18, 15, 6, 1]
    a = f.copy()
    while len(a) > 4:
        last = a.pop()
        offset = len(a)-4
        for j in range(4):
            a[offset+j] -= last*q[j]
    return a


def fp(q, p):
    return q.numerator*pow(q.denominator, -1, p) % p


def gcd_mod(a, b, p):
    def trimmed(v):
        while v and not v[-1]:
            v.pop()
        return v
    a, b = trimmed(a), trimmed(b)
    while b:
        r = a.copy()
        inverse = pow(b[-1], -1, p)
        while len(r) >= len(b):
            z = r[-1]*inverse % p
            offset = len(r)-len(b)
            for i, v in enumerate(b):
                r[offset+i] = (r[offset+i]-z*v) % p
            trimmed(r)
        a, b = b, r
    return [(v*pow(a[-1], -1, p)) % p for v in a]


def incidence(f, row, direction=False):
    require(len(f) == 21, 'polynomial length')
    require(f[20] == (0 if direction else 1), 'leading term')
    require(f[0] == f[19] == f[3] == 0, 'fixed zeros')
    high = {4: (-190, 0), 6: (-190, 2280), 7: (-190, 2280), 9: (0, -1140)}[row]
    require((f[18], f[17]) == ((0, 0) if direction else high), 'high coefficients')
    roots = {4: [(0,1),(0,6),(2,6)],
             6: [(0,1),(0,6),(2,6),(0,10),(1,10)],
             7: [(0,1),(2,1),(0,7),(1,7)],
             9: [(0,1),(1,1),(2,1)]}[row]
    for k, root in roots:
        require(eval_hasse(f, k, root) == 0, f'row {row}: H{k}({root})')
    if row == 4:
        require(all(v == 0 for v in quad_square_remainder(f)), 'quadratic square')
    if direction:
        require(all(q.denominator % 17 and fp(q,17) == 0 for q in f), 'direction reduction')
    require(all((f[20-j]/comb(20,j)).denominator % 17 for j in range(21)), 'normalized integrality')


def main():
    data = json.loads((BASE/'partial-families.json').read_text())
    inventory = json.loads((BASE.parent/'support_frontier/inventory.json').read_text())
    require(data['status'] == 'PARTIAL INCIDENCE FAMILIES, NOT CA POLYNOMIALS', 'scope label')
    result = []
    for record in data['rows']:
        row = record['row']
        selected = unpack(record['polynomialCoefficientsLowToHigh'])
        origin = unpack(record['familyOriginLowToHigh'])
        directions = [unpack(v) for v in record['familyDirectionsLowToHigh']]
        incidence(selected, row)
        incidence(origin, row)
        for direction in directions:
            incidence(direction, row, True)
        require(len(directions) == record['familyDimension'], 'dimension')
        parameters = unpack(record['selectedParameters'])
        rebuilt = [origin[i]+sum(z*d[i] for z,d in zip(parameters,directions)) for i in range(21)]
        require(rebuilt == selected, 'affine reconstruction')
        free_indices = [record['unknownIndices'][j] for j in record['freeColumns']]
        for i, direction in enumerate(directions):
            require([direction[20-j] for j in free_indices] ==
                    [Fraction(17 if i == k else 0) for k in range(len(free_indices))], 'linear independence')
        support = [j for j in range(2,20) if selected[20-j]]
        require(support == record['deficiencySupport'], 'exact support')
        require(support in inventory['finalSurvivors'], 'support criterion inventory')
        seed = [0]*21
        seed[20] = 1
        seed[18],seed[17],seed[3],seed[2],seed[1] = record['seed']
        require([fp(v,17) for v in selected] == seed, 'seed reduction')
        require([fp(v,17) for v in origin] == seed, 'origin seed')
        for k, root in record['visibleRationalWitnesses'].items():
            require(eval_hasse(selected,0,root) == eval_hasse(selected,int(k),root) == 0, 'visible incidence')
        for check in record['certifiedFailedDerivativeConditions']:
            k,p = check['hasseOrder'],check['prime']
            require(all(v.denominator % p for v in selected) and comb(20,k) % p, 'good reduction')
            a = [fp(v,p) for v in selected]
            b = [a[i]*comb(i,k) % p for i in range(k,21)]
            require(len(b) == 21-k and b[-1] != 0, 'degree preservation')
            require(gcd_mod(a,b,p) == [1], 'coprimality certificate')
        result.append({'row':row, 'dimension':len(directions), 'support':support,
                       'failedHasseOrders':[q['hasseOrder'] for q in record['certifiedFailedDerivativeConditions']]})
    require([r['row'] for r in result] == [4,6,7,9], 'complete assigned row list')
    print(json.dumps({'status':'PASS', 'scope':'Partial incidence only; every selected polynomial fails CA.', 'rows':result},indent=2))


if __name__ == '__main__':
    main()
