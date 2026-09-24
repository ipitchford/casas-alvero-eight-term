#!/usr/bin/env python3
"""Independent audit of the sparse degree-20 exclusion.

Uses SymPy rather than the producer's Singular, and reverses variable order.
The characteristic-zero implication additionally uses the proved finite-module
argument in sparse-theorem-addendum.md. This is not a full degree-20 proof.
"""
from itertools import product
from math import comb
import json
import sympy as sp


def det19_for_support(support):
    js = [j for j in range(2, 19) if j not in support]
    xs = {}
    for j in js:
        xs[j] = (pow(j, -1, 19) - sum(
            comb(j-2, k-2)*xs[k] for k in js if k < j)) % 19
    answer = (-1)**len(js) * (-1 + sum((-1)**j * xs[j] for j in js))
    for j in js:
        answer = answer*j % 19
    return answer % 19


def main():
    supports = [tuple(sorted((a, b, 19)))
                for a, b in product((4, 16), (5, 10, 15))]
    records = [{'support': s, 'determinant_mod19': det19_for_support(s)}
               for s in supports]
    if [r['support'] for r in records if r['determinant_mod19'] == 0] != [(5,16,19)]:
        raise ValueError('support-filter disagreement')
    u, v = sp.symbols('u v')
    a = -comb(20, 5)
    b = -comb(20, 16)*u**16-comb(15, 4)*a*u**11
    c = -20*v**19-15*a*v**14-4*b*v**3
    es = [1+a+b+c,
          u**19+a*u**14+b*u**3+c,
          v**19+a*v**14+b*v**3+c]
    p = sp.Poly(es[1]-es[0], u)
    q = sp.Poly(es[2]-es[0], v)
    if p.degree() != 19 or p.LC() != -4844 or p.LC() % 31 == 0:
        raise ValueError('u integrality relation invalid')
    if q.degree() != 19 or q.LC() != 1:
        raise ValueError('v integrality relation invalid')
    gs = sp.groebner(es, v, u, modulus=31, order='grevlex')
    if list(gs) != [sp.Integer(1)]:
        raise ValueError('modular ideal is not the unit ideal')
    print(json.dumps({
        'status': 'PASS', 'engine': 'SymPy', 'version': sp.__version__,
        'variable_order': ['v', 'u'], 'monomial_order': 'grevlex',
        'modulus': 31, 'basis': ['1'], 'saturation_used': False,
        'normalization_a': a, 'normalization_b': str(b),
        'normalization_c': str(c),
        'u_relation': str(p.as_expr()), 'u_leading_coefficient_mod31': 23,
        'v_relation': str(q.as_expr()), 'module_generator_bound': 361,
        'six_supports': records,
        'scope': 'No nontrivial centered characteristic-zero CA polynomial of degree 20 has at most four nonzero terms, conditional on cited CLO results and the written finite-module argument.'
    }, indent=2))


if __name__ == '__main__':
    main()
