"""Exact finite arithmetic for the row-4 quadratic lifting proof.

This does not certify the implicit-function or Weierstrass arguments.
All polynomials are ascending coefficient arrays over F_17.
"""
from math import comb, lcm
import json

P = 17


def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a or [0]


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*x for x in a])


def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def rem(a, b):
    a, b = trim(a), trim(b)
    inv = pow(b[-1], -1, P)
    while a != [0] and len(a) >= len(b):
        t, k = a[-1]*inv % P, len(a)-len(b)
        for j, v in enumerate(b):
            a[j+k] = (a[j+k]-t*v) % P
        a = trim(a)
    return a


def gcd(a, b):
    while b != [0]:
        a, b = b, rem(a, b)
    return scale(a, pow(a[-1], -1, P))


def power_mod(a, n, f):
    r = [1]
    while n:
        if n & 1:
            r = rem(mul(r, a), f)
        a = rem(mul(a, a), f)
        n //= 2
    return r


def hasse(a, k):
    return trim([comb(j, k)*a[j] for j in range(k, len(a))])


def value(a, x):
    out = 0
    for c in reversed(a):
        out = (out*x+c) % P
    return out


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def irreducible(f):
    d = len(f)-1
    # For the degrees 1, 2 and 4 here, checking all k<=d/2 is sufficient.
    x = [0, 1]
    for k in range(1, d//2+1):
        require(gcd(f, add(power_mod(x, P**k, f), scale(x, -1))) == [1],
                'proper-degree factor detected')
    require(rem(add(power_mod(x, P**d, f), scale(x, -1)), f) == [0],
            'Frobenius irreducibility identity failed')


def main():
    h = [0]*21
    h[1], h[2], h[18], h[20] = 8, 11, 14, 1
    q = [3, 3, 1]
    factors = [([0, 1], 1), ([7, 1], 1), ([11, 1], 1),
               ([16, 1], 1), (q, 2), ([2, 0, 4, 3, 1], 1),
               ([14, 5, 14, 12, 1], 1), ([11, 4, 16, 13, 1], 1)]
    product = [1]
    for f, exponent in factors:
        irreducible(f)
        for _ in range(exponent):
            product = mul(product, f)
    require(product == h, 'factorization mismatch')
    require(gcd(h, hasse(h, 1)) == q, 'multiple-cluster gcd mismatch')
    require(gcd(h, hasse(h, 2)) == [11, 1], 'H2 witness must reduce to 6')
    require(gcd(h, hasse(h, 17)) == [0, 1], 'H17 witness must reduce to 0')
    require(gcd(h, hasse(h, 18)) == [16, 1], 'H18 witness must reduce to 1')
    require(rem(hasse(h, 2), q) == [3], 'H2 at double clusters')
    require(rem(scale(hasse(h, 2), 2*pow(20, -1, P)), q) == [2],
            'critical-root derivative must be 2')
    require(all(comb(18, j) % P == 0 and comb(20, j) % P == 0
                for j in range(4, 17)), 'parameter derivatives not divisible')
    require(comb(18, 2) == 153, 'a18 elimination constant')
    require(190-1 == 189 and 20 % P != 0, 'a19 elimination constants')
    # Reduction of f_{u,s} is X20-3X18-3s18 X2+(2+3s18)X.
    s = 6
    specialized = [0]*21
    specialized[20], specialized[18] = 1, -3
    specialized[2] = -3*pow(s, 18, P)
    specialized[1] = 2+3*pow(s, 18, P)
    require(trim(specialized) == h, 'specialized family does not give seed')
    partial_s = [0, 3*18*pow(s, 17, P), -3*18*pow(s, 17, P)]
    fixed_derivative = value(hasse(h, 1), s)
    parameter_derivative = value(partial_s, s)
    require((fixed_derivative, parameter_derivative) == (5, 4),
            'simple H2 witness derivative decomposition')
    require((fixed_derivative+parameter_derivative) % P == 9,
            'total simple-witness derivative must be 9')
    splitting_degree = lcm(*(len(f)-1 for f, _ in factors))
    require(splitting_degree == 4, 'unexpected splitting degree')
    print(json.dumps({
        'status': 'PASS',
        'prime': P,
        'distinct_residue_roots': sum(len(f)-1 for f, _ in factors),
        'splitting_field_degree': splitting_degree,
        'simple_witness_total_derivative': 9,
        'critical_root_derivative': 2,
        'factorization': factors,
        'scope': 'Finite constants only; formal lifting coverage is proved in ROW4_QUADRATIC_LIFTING.md.'
    }, indent=2))


if __name__ == '__main__':
    main()
