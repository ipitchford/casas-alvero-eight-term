"""Exact F17 polynomial/extension-field replay for the m4 reduced model.

No producer code or computer-algebra package is imported.
"""
from math import comb
import json

P = 17


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*x for x in a])


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divmodp(a, b):
    a, b = trim(a), trim(b)
    require(b != [0], "division by zero")
    q = [0]*max(1, len(a)-len(b)+1)
    inv = pow(b[-1], -1, P)
    while a != [0] and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]*inv % P
        q[k] = c
        for i, x in enumerate(b):
            a[i+k] = (a[i+k]-c*x) % P
        a = trim(a)
    return trim(q), a


def rem(a, b):
    return divmodp(a, b)[1]


def gcd(a, b):
    while b != [0]:
        a, b = b, rem(a, b)
    return scale(a, pow(a[-1], -1, P))


def power(a, n, modulus=None):
    out = [1]
    while n:
        if n & 1:
            out = mul(out, a)
            if modulus:
                out = rem(out, modulus)
        a = mul(a, a)
        if modulus:
            a = rem(a, modulus)
        n //= 2
    return out


def hasse(a, k):
    return trim([comb(j, k)*a[j] for j in range(k, len(a))])


def irreducible(f):
    d = len(f)-1
    x = [0, 1]
    for k in range(1, d//2+1):
        require(gcd(f, add(power(x, P**k, f), scale(x, -1))) == [1],
                "factor has proper irreducible divisor")
    require(rem(add(power(x, P**d, f), scale(x, -1)), f) == [0],
            "factor Frobenius identity failed")


def field_gcds(phi, triple=False):
    """Compute in F17[t]/phi, then Euclid in the independent variable Y."""
    def emul(a, b):
        return rem(mul(a, b), phi)

    def einv(a):
        require(a != [0], "zero extension inverse")
        return power(a, P**(len(phi)-1)-2, phi)

    def ytrim(a):
        while len(a) > 1 and a[-1] == [0]:
            a.pop()
        return a

    def yrem(a, b):
        a = [x[:] for x in a]
        inverse = einv(b[-1])
        while a != [[0]] and len(a) >= len(b):
            k, c = len(a)-len(b), emul(a[-1], inverse)
            for i, x in enumerate(b):
                a[i+k] = add(a[i+k], scale(emul(c, x), -1))
            a = ytrim(a)
        return a

    def ygcd(a, b):
        while b != [[0]]:
            a, b = b, yrem(a, b)
        inverse = einv(a[-1])
        return [emul(x, inverse) for x in a]

    def yh(a, k):
        return ytrim([scale(a[j], comb(j, k)) for j in range(k, len(a))])

    t = rem([0, 1], phi)
    d = add(power(t, 3, phi), scale(t, -3))
    q = add([12], scale(d, -4))
    require(q != [0] and d != [0] and t != [0], "excluded degeneration")
    H = [[0] for _ in range(18)]
    H[1], H[2], H[4], H[17] = scale(d, 4), [6], [16], q
    expected1 = [scale(t, -1), [1]]
    if triple:
        expected1 = [emul(t, t), scale(t, -2), [1]]
    got1 = ygcd(H, yh(H, 1))
    got2 = ygcd(H, yh(H, 2))
    got3 = ygcd(H, yh(H, 3))
    require(got1 == expected1, "unexpected first-derivative gcd")
    require(got2 == [[16], [1]], "unexpected second-derivative gcd")
    require(got3 == [[0], [1]], "unexpected third-derivative gcd")
    return {"parameterFactor": phi, "H1GcdAscendingOverExtension": got1,
            "H2GcdAscendingOverExtension": got2,
            "H3GcdAscendingOverExtension": got3}


def main():
    q = [12, 12, 0, 13]
    R = add(mul([0]*15+[1], q), [11, 0, 3])
    factors = [([8, 1], 2), ([10, 1], 2), ([16, 1], 3),
               ([6, 6, 0, 9, 1, 1], 1),
               ([9, 8, 7, 13, 1, 0, 1], 1)]
    product = [13]
    for phi, exponent in factors:
        irreducible(phi)
        product = mul(product, power(phi, exponent))
    require(product == R, "R factorization mismatch")
    expected_derivative_gcd = mul(mul([8, 1], [10, 1]), power([16, 1], 2))
    require(gcd(R, hasse(R, 1)) == expected_derivative_gcd, "squarefree degree")
    for name, polynomial in [('q', q), ('t', [0, 1]),
                             ('d', [0, 14, 0, 1]), ('t+1', [1, 1])]:
        require(gcd(R, polynomial) == [1], "degeneration: "+name)
    require(gcd(R, [1, 0, 16]) == [16, 1], "H2 at v degeneration")
    require(gcd(R, [2, 14, 0, 1]) == power([16, 1], 2), "H1 at u degeneration")
    extension_records = [field_gcds(phi, phi == [16, 1]) for phi, _ in factors]
    boundary_records = []
    for name, data, expected in [
        ('u=v=0', {17: 1, 4: -1}, [[0,0,0,1], [0,0,1], [0,1]]),
        ('u=0,v!=0', {17: -3, 4: -1, 1: 4}, [[16,1], [0,1], [0,1]]),
        ('v=0,u!=0', {17: -5, 4: -1, 2: 6}, [[0,1], [16,1], [0,1]])]:
        H = [0]*18
        for exponent, coefficient in data.items():
            H[exponent] = coefficient % P
        got = [gcd(H, hasse(H, k)) for k in (1, 2, 3)]
        require(got == expected, "boundary gcd: "+name)
        boundary_records.append({"chart": name, "HasseGcdsAscending": got})
    distinct_t = sum(len(phi)-1 for phi, _ in factors)
    count = 1+13+13+13*distinct_t
    require(distinct_t == 14 and count == 209, "reduced marked point count")
    quartic = trim([0, 5, -6, 0, 1])
    require(gcd(quartic, hasse(quartic, 1)) == [1], "CA quartic at prime17")
    require(gcd([5, -12, 0, 4], [0, 0, -6, 0, 3]) == [1],
            "origin initial forms share a finite projective root")
    print(json.dumps({"status": "PASS", "prime": 17,
                      "RAscending": R, "factorization": factors,
                      "distinctNonzeroTValues": distinct_t,
                      "reducedMarkedPoints": count,
                      "extensionGcds": extension_records,
                      "boundaryGcds": boundary_records,
                      "scope": "Reduced characteristic-17 model and marked root multiplicities only; no original characteristic-zero lift exclusion."}, indent=2))


if __name__ == '__main__':
    main()
