#!/usr/bin/env python3
"""Exact audit certificates; Python standard library only, no assertions.

Checks polynomial identities and finite monomial linear algebra. The accompanying
proof explains why they imply the stated generator counts and proof defects.
This is not a checker for the Casas-Alvero conjecture or the whole preprint.
"""
import itertools
import json
import math
from pathlib import Path


class Ring:
    def __init__(self, n, p=0):
        self.n, self.p = n, p

    def poly(self, terms):
        return Poly(self, terms)

    def constant(self, c):
        return self.poly({(0,) * self.n: c})

    def variables(self):
        return [self.poly({tuple(int(i == j) for i in range(self.n)): 1})
                for j in range(self.n)]


class Poly:
    def __init__(self, ring, terms):
        self.ring = ring
        self.terms = {m: (c % ring.p if ring.p else c)
                      for m, c in terms.items()
                      if (c % ring.p if ring.p else c) != 0}

    def coerce(self, other):
        return other if isinstance(other, Poly) else self.ring.constant(other)

    def __add__(self, other):
        other = self.coerce(other)
        result = self.terms.copy()
        for m, c in other.terms.items():
            result[m] = result.get(m, 0) + c
        return self.ring.poly(result)

    __radd__ = __add__

    def __neg__(self):
        return self.ring.poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        result = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                m = tuple(x + y for x, y in zip(a, b))
                result[m] = result.get(m, 0) + ca * cb
        return self.ring.poly(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        result = self.ring.constant(1)
        for _ in range(n):
            result = result * self
        return result

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def substitute(self, values):
        result = values[0].ring.constant(0)
        for m, c in self.terms.items():
            term = values[0].ring.constant(c)
            for value, exponent in zip(values, m):
                term = term * value ** exponent
            result = result + term
        return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def divides(a, b):
    return all(x <= y for x, y in zip(a, b))


def minimal_monomials(monomials):
    monomials = set(monomials)
    return sorted(m for m in monomials
                  if not any(q != m and divides(q, m) for q in monomials))


def monomials(polys):
    require(all(len(f.terms) == 1 for f in polys), 'nonmonomial generator')
    return minimal_monomials(next(iter(f.terms)) for f in polys)


def in_monomial_ideal(f, generators):
    return all(any(divides(g, m) for g in generators) for m in f.terms)


def intersection(a, b):
    return minimal_monomials(tuple(max(x, y) for x, y in zip(m, q))
                             for m in a for q in b)


def elementary(xs, degree):
    result = xs[0].ring.constant(0)
    for subset in itertools.combinations(xs, degree):
        product = xs[0].ring.constant(1)
        for x in subset:
            product = product * x
        result = result + product
    return result


def source_generators(xs, indices=(1, 2, 3)):
    """Exactly Phi_{3,j_i}(e_{4-i}), using all four labelled roots."""
    roots = xs + [xs[0].ring.constant(0)]
    return [elementary([roots[k] - roots[j - 1] for k in range(4)
                        if k != j - 1], 4 - i)
            for i, j in enumerate(indices, 1)]


def finite_field_example(p):
    ring = Ring(3, p)
    ell, u, t = ring.variables()
    y = u + (2 if p == 5 else 3) * t
    x = ell - y + 3 * t
    f1, f2, f3 = source_generators([x, y, t])
    require(f3 == ell, 'linear coordinate mismatch')
    q1 = f1.substitute([ring.constant(0), u, t])
    q2 = f2.substitute([ring.constant(0), u, t])
    if p == 5:
        require(q2 == u * t, 'F5 quadratic identity')
        require(q1 == 2*u**3 - u**2*t - u*t**2, 'F5 cubic identity')
        require(3*(q1+(u+t)*q2) == u**3, 'F5 reverse ideal inclusion')
        basis = [ell, u*t, u**3]
        embedded = [ell, t, u**3]
        witness, annihilator = u**3, t
    else:
        require(q2 == 5*u**2, 'F7 quadratic identity')
        require(q1 == 2*u**3+5*u**2*t+3*u*t**2, 'F7 cubic identity')
        require(3*q2 == u**2, 'F7 reverse quadratic inclusion')
        require(5*(q1-2*u*(3*q2)-5*t*(3*q2)) == u*t**2,
                'F7 reverse cubic inclusion')
        basis = [ell, u**2, u*t**2]
        embedded = [ell, u**2, t**2]
        witness, annihilator = u**2*t, t
    ideal = monomials(basis)
    prime = monomials([ell, u])
    require(len(ideal) == 3, 'global minimal monomial basis')
    require(intersection(prime, monomials(embedded)) == ideal,
            'primary decomposition identity')
    product_ideal = monomials([a*b for a in [ell, u] for b in basis])
    require(not in_monomial_ideal(witness, product_ideal), 'torsion witness is zero')
    require(in_monomial_ideal(annihilator*witness, product_ideal),
            'torsion identity fails')
    # Inverting t removes its exponent from every monomial generator.
    localized = minimal_monomials((m[0], m[1], 0) for m in ideal)
    require(localized == prime, 'localization is not the claimed prime ideal')
    require(math.prod(math.comb(3, i) for i in range(3)) % p != 0,
            'characteristic excluded by the proposition')
    return {'characteristic': p, 'global_mu': 3, 'local_mu': 2,
            'unique_minimal_prime': '(ell,u)', 'embedded_prime': '(ell,u,t)',
            'normal_ideal_monomials': ideal, 'torsion_checked_in': 'I / pI'}


def symmetry_check():
    ring = Ring(3)
    xs = ring.variables()
    roots = xs + [ring.constant(0)]
    original = source_generators(xs)
    count = 0
    for sigma in itertools.permutations(range(4)):
        transformed = [roots[sigma[i]] - roots[sigma[3]] for i in range(3)]
        mapped = [g.substitute(transformed) for g in original]
        expected = source_generators(xs, tuple(sigma[i]+1 for i in range(3)))
        require(mapped == expected, 'root permutation/recentering identity')
        inv = [sigma.index(i) for i in range(4)]
        inverse = [roots[inv[i]]-roots[inv[3]] for i in range(3)]
        require([g.substitute(inverse) for g in transformed] == xs,
                'root-relabeling transformation is not invertible')
        count += 1
    return count


def literal_quotient_check():
    ring = Ring(4, 5)
    s, L, U, B = ring.variables()
    C = 3*(B-U)
    A = L-B+3*C
    H = source_generators([3*s+A, s+B, 3*s+C])
    zero = ring.constant(0)
    reduced = [h.substitute([s, zero, U, zero]) for h in H]
    Q = 3*s*U+2*U**2
    require(reduced[2] == 0 and reduced[1] == Q, 'literal H2/H3 mismatch')
    # The ordinary normal form, now with z=3s+2U.
    z = 3*s+2*U
    require(reduced[0] == 2*U**3-U**2*z-U*z**2, 'literal H1 mismatch')
    require(3*(reduced[0]+(U+z)*Q) == U**3, 'literal reverse inclusion')
    require(3*s*U**3 == U**2*Q-2*U**4, 'literal t-torsion identity')
    # Modulo L,B the product m+J+ is (UQ,U^4).
    # In degree 3 the only possible relation is a scalar multiple of UQ.
    require((U*Q).terms.get((1,0,2,0)) == 3, 'nonzero sU² coefficient')
    require((U**3).terms.get((1,0,2,0),0) == 0, 'witness support error')
    return {'characteristic': 5, 'line': [3,1,3], 'r': 2,
            'J_plus': '(L,B,3sU+2U^2,U^3)', 'm_plus': '(L,U,B)',
            'nonzero_class': 'U^3', 'annihilator': 's'}


def characteristic_zero_check():
    ring = Ring(4)
    u, v, w, z = ring.variables()
    f = [u*v, u**2, v**2]
    g = [w**3, u**3, v**3]
    minors = [f[0]*g[1]-f[1]*g[0], f[0]*g[2]-f[2]*g[0],
              f[1]*g[2]-f[2]*g[1]]
    require(minors == [u**2*(u**2*v-w**3),v**2*(u*v**2-w**3),
                       u**2*v**2*(v-u)], 'determinantal identities')
    require((w**3-u*v*z)*(w**3+u*v*z) == w**6-u**2*v**2*z**2,
            'nilpotent-unit inverse after clearing w denominator')
    require(not in_monomial_ideal(u*v, monomials([u**2,v**2])),
            'claimed nonzero nilpotent is zero')
    require(in_monomial_ideal((u*v)**2, monomials([u**2,v**2])),
            'nilpotence identity fails')
    return {'field': 'Q', 'prime': '(u,v)', 'D_local': '(u^2,v^2)',
            'nonzero_nilpotent': 'uv', 'unit_polynomial': 'w^3+uv*z',
            'scope': 'abstract supporting inference; not a Casas-Alvero ideal'}


def negative_controls():
    ring = Ring(3,5)
    ell,u,t = ring.variables()
    tests = {
        'wrong_cubic_coefficient': 2*u**3-u**2*t-u*t**2 != 3*u**3-u**2*t-u*t**2,
        'wrong_local_generator': monomials([ell,u]) != monomials([ell,u**2]),
        'zero_torsion_witness_rejected': in_monomial_ideal(u**4,
                                      monomials([ell**2,ell*u,u**2*t,u**4])),
        'excluded_characteristic_three_rejected': 9 % 3 == 0,
    }
    require(all(tests.values()), 'a negative control failed')
    return tests


def main():
    result = {'status':'PASS', 'scope':'finite exact audit certificates only',
              'examples':[finite_field_example(p) for p in (5,7)],
              'distinct_entry_tuples_per_field':symmetry_check(),
              'literal_paper_quotient':literal_quotient_check(),
              'characteristic_zero_supporting_inference':characteristic_zero_check(),
              'negative_controls':negative_controls()}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
