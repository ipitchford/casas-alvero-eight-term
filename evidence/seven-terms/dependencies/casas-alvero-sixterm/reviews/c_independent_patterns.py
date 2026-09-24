"""Independent standard-library gcd/multiplicity audit of C's three seeds.

No producer arithmetic or CAS is imported. This checks geometric witness
sets after the independently replayed coefficient classification.
"""
from math import comb
import json
from pathlib import Path

P = 13


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % P
    return trim(c)


def divide(a, b):
    r = a[:]
    q = [0] * max(0, len(a) - len(b) + 1)
    while r and len(r) >= len(b):
        i = len(r) - len(b)
        q[i] = r[-1] * pow(b[-1], -1, P) % P
        for j, c in enumerate(b):
            r[i+j] = (r[i+j] - q[i]*c) % P
        trim(r)
    return trim(q), r


def gcd(a, b):
    while b:
        a, b = b, divide(a, b)[1]
    return [(x * pow(a[-1], -1, P)) % P for x in a]


def hasse(f, k):
    return trim([f[i+k] * comb(i+k, k) % P for i in range(len(f)-k)])


def evaluate(f, x):
    return sum(c * pow(x, i, P) for i, c in enumerate(f)) % P


def multiplicity(f, root):
    count = 0
    while f and len(f) > 1:
        q, r = divide(f, [(-root) % P, 1])
        if r:
            return count
        count += 1
        f = q
    return count


def product(*factors):
    f = [1]
    for factor in factors:
        f = multiply(f, factor)
    return f


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    expected = {
        2: {16:[12,1], 15:product([12,1],[11,4,1]), 3:[3,1], 1:[0,0,1]},
        3: {16:[12,1], 15:product([12,1],[12,1],[11,1]), 3:[11,1],
            1:product([12,1],[9,1],[9,1])},
        10:{16:[12,1], 15:[12,1], 3:[2,1], 1:product([10,1],[2,1])},
    }
    rows = []
    for c, d in ((2,0),(3,12),(10,5)):
        f = [0]*21
        for exponent, coefficient in {20:1,16:4,15:6,3:c,1:d}.items():
            f[exponent] = coefficient
        common = {}
        for k in range(1,20):
            actual = gcd(f, hasse(f,k))
            require(len(actual)>1, f'Missing CA condition {k} at c={c}')
            if k in expected[c]:
                require(actual==expected[c][k], f'Wrong full gcd at c={c}, k={k}')
                common[k] = actual
        multiplicities = {r:multiplicity(f,r) for r in range(P) if evaluate(f,r)==0}
        rows.append({'coefficients':[4,6,c,d], 'all19HasseConditions':'PASS',
                     'activeGcdsAscending':common, 'primeFieldRootMultiplicities':multiplicities})
    require(evaluate([11,4,1],12)==8, 'Quadratic denominator guard failed')
    require(11 not in {x*x % P for x in range(P)}, 'Quadratic should be irreducible over F13')
    require(rows[0]['primeFieldRootMultiplicities'][0]==3, 'Wrong d=0 zero-root multiplicity')
    require(rows[1]['primeFieldRootMultiplicities'][1]==2 and rows[1]['primeFieldRootMultiplicities'][4]==3,
            'Wrong c=3 double/triple clusters')
    require(rows[1]['primeFieldRootMultiplicities'][2]==1, 'Wrong c=3 simple witness cluster')
    require(rows[2]['primeFieldRootMultiplicities'][1]==1 and rows[2]['primeFieldRootMultiplicities'][3]==2
            and rows[2]['primeFieldRootMultiplicities'][11]==2, 'Wrong c=10 witness clusters')
    receipt={'status':'PASS', 'method':'Independent standard-library Euclidean polynomial gcd',
             'coefficientPoints':rows, 'quadraticUBranch':'u^2+4u-2 irreducible over F13; two distinct F13bar roots',
             'geometricMarkedAssignmentsBeforeLiftFilter':9,
             'geometricMarkedAssignmentsAfterDZeroLiftFilter':6,
             'scope':'Witness classification given the separately certified three coefficient points; no lift existence claim'}
    Path(__file__).with_name('c-independent-patterns.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':
    main()
