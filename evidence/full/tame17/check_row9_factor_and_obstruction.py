"""Exact standalone factorization, irreducibility, and linear-jet checks."""
from math import comb
from fractions import Fraction
import json

P = 17


def require(ok, message):
    if not ok:
        raise ValueError(message)


def trim(a):
    while a and a[-1] % P == 0:
        a.pop()
    return [v % P for v in a]


def add(a, b):
    c = [0]*max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] = (c[i+j]+u*v) % P
    return trim(c)


def rem(a, b):
    a = trim(a.copy())
    while len(a) >= len(b):
        c = a[-1]*pow(b[-1], -1, P) % P
        offset = len(a)-len(b)
        for i, v in enumerate(b):
            a[offset+i] = (a[offset+i]-c*v) % P
        a = trim(a)
    return a


def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    return trim([v*pow(a[-1], -1, P) for v in a])


def power_mod(a, n, modulus):
    out = [1]
    while n:
        if n & 1:
            out = rem(mul(out, a), modulus)
        a = rem(mul(a, a), modulus)
        n //= 2
    return out


def irreducibility_check(f, proper_powers):
    degree = len(f)-1
    x = [0, 1]
    q = x
    records = {}
    for i in range(1, degree+1):
        q = power_mod(q, P, f)
        if i in proper_powers:
            test = gcd(f, add(q, [0, -1]))
            require(test == [1], 'proper subfield gcd')
            records[str(i)] = {'remainder': q, 'gcdWithXPowerMinusX': test}
    require(q == x, 'full Frobenius remainder')
    return {'degree': degree, 'properPowerChecks': records,
            'fullFrobeniusRemainder': q, 'irreducible': True}


def double_root_coefficients(u):
    a18 = Fraction(18221-sum((19-j)*comb(20, j)*u[j] for j in range(4, 17)), 190)
    a19 = Fraction(-17082+sum((18-j)*comb(20, j)*u[j] for j in range(4, 17)), 20)
    f = [Fraction(0)]*21
    f[20], f[17], f[2], f[1] = 1, -1140, 190*a18, 20*a19
    for j in range(4, 17):
        f[20-j] = comb(20, j)*u[j]
    require(sum(f) == 0, 'f(1)')
    require(sum(i*v for i, v in enumerate(f)) == 0, 'f prime(1)')
    h2 = sum(comb(i, 2)*v for i, v in enumerate(f) if i >= 2)
    rhs = -136629+sum(comb(19-j, 2)*comb(20, j)*u[j] for j in range(4, 17))
    require(h2 == rhs, 'exact H2 obstruction')
    return h2


def main():
    q5 = [14, 12, 15, 0, 14, 1]
    q10 = [9, 7, 4, 11, 1, 0, 6, 0, 16, 4, 1]
    f = mul(mul(mul([0, 1], [2, 1]), mul(mul([-1, 1], [-1, 1]), [-1, 1])), mul(q5, q10))
    h = [0]*21
    h[20], h[17], h[2], h[1] = 1, 16, 14, 3
    require(f == h, 'seed factorization')
    checks = [irreducibility_check(q5, {1}), irreducibility_check(q10, {2, 5})]
    zero = {j: 0 for j in range(4, 17)}
    constant = double_root_coefficients(zero)
    coefficients = []
    for j in range(4, 17):
        u = zero.copy()
        u[j] = 1
        value = double_root_coefficients(u)-constant
        require(value.denominator == 1 and value.numerator % 17 == 0, 'integral jet coefficient')
        coefficients.append(int(value/17) % 17)
    require(constant == -136629 and constant/17 == -8037, 'jet constant')
    require(coefficients == [5,15,3,9,9,16,10,16,9,9,3,15,5], 'mod17 jet coefficients')
    print(json.dumps({'status': 'PASS', 'factorizationChecked': True,
        'irreducibilityChecks': checks, 'splittingFieldDegree': 10,
        'distinctSeedRootCount': 18, 'H2DividedBy17Constant': -8037,
        'H2DividedBy17ConstantMod17': 4,
        'H2DividedBy17CoefficientsMod17ForJ4Through16': coefficients}, indent=2))


if __name__ == '__main__':
    main()
