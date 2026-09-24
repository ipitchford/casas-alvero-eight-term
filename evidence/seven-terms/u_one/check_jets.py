#!/usr/bin/env python3
"""Exact arithmetic for the u=1 branch; no CAS and no unramified assumption.

The written valuation arguments justify using these jets over all ramified
extensions. This checker verifies their coefficients, ranks, multiplicities,
and final polynomial identities.
"""
from math import comb
import json

P = 13


def require(ok, message):
    if not ok:
        raise ValueError(message)


def base(d0):
    return {20: 1, 16: -4845, 15: 62016, 3: d0, 1: -57172-d0}


def H(f, k, x, modulus):
    return sum(c*comb(e, k)*pow(x, e-k, modulus)
               for e, c in f.items() if e >= k) % modulus


def derivative_H(f, k, x):
    return (k+1)*H(f, k+1, x, P) % P


def parameter_H(power, k, x):
    return ((comb(power, k)*pow(x, power-k, P) if power >= k else 0)
            -(pow(x, 1-k, P) if k <= 1 else 0)) % P


def jet(d0, k, r, moving):
    residue = H(base(d0), k, r, P*P)
    require(residue % P == 0, 'Jet base is not a root modulo13')
    return [residue//P, derivative_H(base(d0), k, r) if moving else 0,
            parameter_H(10, k, r), parameter_H(3, k, r)]


def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % P


def solve(rows):
    matrix = [[row[1], row[2], row[3], -row[0] % P] for row in rows]
    det = determinant3([row[:3] for row in matrix])
    require(det != 0, 'Jet system is not uniquely solvable over every residue field')
    for k in range(3):
        pivot = next((i for i in range(k, 3) if matrix[i][k] % P), None)
        require(pivot is not None, 'Missing pivot')
        matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
        inverse = pow(matrix[k][k] % P, -1, P)
        matrix[k] = [v*inverse % P for v in matrix[k]]
        for i in range(3):
            if i != k:
                coefficient = matrix[i][k]
                matrix[i] = [(x-coefficient*y) % P for x, y in zip(matrix[i], matrix[k])]
    return [row[3] for row in matrix], det


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    c = [0]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim([x % P for x in c])


def scale(a, c):
    return trim([c*x % P for x in a])


def mul(a, b):
    if not a or not b:
        return []
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim([x % P for x in c])


def divide(a, b):
    a = a[:]
    quotient = [0]*max(0, len(a)-len(b)+1)
    inverse = pow(b[-1], -1, P)
    while a and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]*inverse % P
        quotient[k] = c
        for j, x in enumerate(b):
            a[k+j] = (a[k+j]-c*x) % P
        trim(a)
    return trim(quotient), a


def xgcd(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, [1], [], [], [1]
    while r1:
        q, r = divide(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, scale(mul(q, s1), -1))
        t0, t1 = t1, add(t0, scale(mul(q, t1), -1))
    inverse = pow(r0[-1], -1, P)
    return scale(r0, inverse), scale(s0, inverse), scale(t0, inverse)


def multiplicity(d0, r, derivative_order=0):
    f = base(d0)
    for j in range(21-derivative_order):
        coefficient = comb(j+derivative_order, derivative_order)*H(f, j+derivative_order, r, P) % P
        if coefficient:
            return j, coefficient
    raise ValueError('Unexpected zero polynomial')


require(comb(20, 10) == 184756 and 184756 % 169 == 39, 'Middle coefficient factor failed')
require((-4845*comb(16, 10))//184756 == -210
        and -4845*comb(16, 10) == -210*184756, 'Normalized A term failed')
require(62016*comb(15, 10) == 1008*184756, 'Normalized B term failed')
require(pow(14212 % P, -1, P) == 9, 'Normalization inverse failed')

jacobians = []
for r, d0 in [(2, 3), (11, 10)]:
    f = base(d0)
    J = [[derivative_H(f, 0, r), parameter_H(3, 0, r)],
         [derivative_H(f, 3, r), parameter_H(3, 3, r)]]
    det = (J[0][0]*J[1][1]-J[0][1]*J[1][0]) % P
    require(det == 11, 'The valuation Jacobian is not a unit')
    require(H(f, 0, r, P) == H(f, 3, r, P) == 0, 'Wrong marked base point')
    jacobians.append({'vResidue': r, 'DResidue': d0, 'matrix': J, 'determinant': det})

require(multiplicity(10, 3) == (2, 3) and multiplicity(10, 3, 1) == (1, 6),
        'The w=3 cluster calculation failed')
require(multiplicity(10, 11) == (2, 7), 'The v=w=11 cluster calculation failed')
require(multiplicity(3, 4) == (3, 5) and multiplicity(3, 4, 1) == (2, 2),
        'The half-valuation w=4 cluster calculation failed')
require(multiplicity(3, 1) == (2, 9), 'The w=1 cluster calculation failed')
require(multiplicity(3, 0) == (1, 12), 'The final zero root is not simple')
require(sum(c*e for e, c in base(3).items()) == 13*61198,
        'The exact derivative-at-one constant failed')

branches = [
    ('v11_w3', 10, 11, jet(10, 0, 3, False), [8, 1, 11], [1]),
    ('v11_w11', 10, 11, jet(10, 1, 11, True), [0, 5, 6], [1]),
    ('v2_w4', 3, 2, jet(3, 0, 4, False), [5, 12, 7], [1]),
    ('v2_w1', 3, 2, jet(3, 1, 1, False), [1, 0, 3], [0, 1]),
]
records = []
for name, d0, r, last_row, expected_solution, expected_gcd in branches:
    rows = [jet(d0, 0, r, True), jet(d0, 3, r, True), last_row]
    solution, det = solve(rows)
    require(solution == expected_solution, 'Unexpected first-jet solution')
    normalized_constant = 9*solution[1] % P
    h = [base(d0).get(j, 0) % P for j in range(21)]
    G10 = [normalized_constant, 0, 0, 0, 0, 7, 11, 0, 0, 0, 1]
    g, U, V = xgcd(h, G10)
    require(g == expected_gcd, 'Unexpected middle-derivative gcd')
    require(add(mul(U, h), mul(V, G10)) == g, 'Bezout identity replay failed')
    records.append({'branch': name, 'jetRowsConstant_R_S_T': rows,
                    'linearSystemDeterminant': det, 'solution_R_S_T': solution,
                    'normalizedMiddleCoefficient': normalized_constant,
                    'gcdLowFirst': g, 'bezoutU_LowFirst': U, 'bezoutV_LowFirst': V})

print(json.dumps({'status': 'PASS', 'unitJacobians': jacobians, 'records': records,
                  'scope': 'Exact finite arithmetic for the four u=1 branches. The written valuation arguments prove integrality and applicability over arbitrary ramified extensions; C!=0 is used in the final branch.'}, indent=2))
