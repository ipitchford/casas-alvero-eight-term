#!/usr/bin/env python3
"""Exact finite arithmetic for the quadratic-coefficient support B.

This checks residue markings, binomial Taylor coefficients, second-jet
identities, and the final small-root residue. The ramification-safe proof
connecting them is in B_EXCLUSION.md. Standard library only.
"""
from itertools import product
from math import comb
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def model(a, b, u=0, quadratic=0):
    f = {20: 1, 16: C(20, 4)*a, 10: C(20, 10)*b,
         4: C(20, 16)*u}
    f[3] = -sum(C(j, 3)*v for j, v in f.items())
    f[2] = quadratic
    f[1] = -sum(f.values())
    require(sum(f.values()) == 0, 'f(1)')
    require(sum(C(j, 3)*v for j, v in f.items()) == 0, 'H3 f(1)')
    return f


def divided(integer, divisor):
    q, r = divmod(integer, divisor)
    require(r == 0, 'Nonexact integer division')
    return q


def main():
    records = []
    for marking in product((0, 1), repeat=3):
        a = [1]+[0]*16
        for j, w in zip((4, 10, 16), marking):
            a[j] = -sum(C(j, i)*a[i]*w**(j-i) for i in range(j)) % 17
        f = model(a[4], a[10], a[16])
        W1 = divided(sum(j*v for j, v in f.items()), 17) % 17
        W2 = divided(sum(C(j, 2)*v for j, v in f.items()), 17) % 17
        E0 = divided(f[1], 17) % 17
        cases = []
        if (W1-W2) % 17 == 0:
            cases.append(['unit', 'unit', -W1 % 17])
        if (W1+E0) % 17 == 0:
            cases.append(['unit', 'small', -W1 % 17])
        if (W2+E0) % 17 == 0:
            cases.append(['small', 'unit', -W2 % 17])
        records.append({'marking': list(marking),
                        'coefficients': [a[j] for j in (4, 10, 16)],
                        'W1_W2_E0': [W1, W2, E0], 'cases': cases})
    survivors = [r for r in records if r['cases']]
    require(survivors == [{'marking': [1, 1, 0], 'coefficients': [16, 5, 0],
                          'W1_W2_E0': [8, 9, 8],
                          'cases': [['small', 'unit', 8]]}], 'Residue sieve')

    # Taylor coefficients c_k/17 of f0 with linear coefficient zero,
    # eliminating D by H3 f0(1)=0 and F by f0(1)=0.
    A = []
    for k in range(1, 17):
        row = []
        for j in (0, 4, 10):
            cj = C(20, j)
            D = -cj*C(20-j, 3)
            F = -cj-D
            row.append(divided(cj*C(20-j, k)+D*C(3, k)+F*C(2, k), 17))
        A.append(row)
    require([c % 17 for c in A[0]] == [2, 8, 1], 'A1 coefficients')
    require([c % 17 for c in A[1]] == [13, 9, 6], 'A2 coefficients')
    require(all(c == 0 for c in A[2]), 'A3=0')
    require((A[3][0]-A[3][1]+209*A[3][2]) % 17 == 14, 'A4 baseline')
    require((A[0][0]-A[0][1]+209*A[0][2]) % 17 == 16, 'A1 baseline')
    require((A[1][0]-A[1][1]+209*A[1][2]) % 17 == 0, 'A2 baseline')

    require(C(17, 2) % 17 == C(18, 2) % 17 == 0,
            'High H2 terms at orders fifteen/sixteen')
    require(20*C(19, 2) % 17 == 3, 'Essential degree-nineteen H2 term')
    require(C(20, 2) % 17 == 3, 'Degree-twenty H2 term')
    second_jets = []
    jet_survivors = []
    for t, u in product(range(17), repeat=2):
        # Zero means the exact root one. Nonzero roots obey the unit equation.
        t1 = (-(12*t+9*u)*pow(16*pow(t, 15, 17), -1, 17) % 17) if t else 0
        u1 = (-(9*t+12*u)*pow(16*pow(u, 15, 17), -1, 17) % 17) if u else 0
        alpha1, beta1 = -4*t, 7*t+9*u
        alpha2 = -4*t1-6*t*t
        beta2 = 7*t1+9*u1+2*t*t+8*t*u+11*u*u
        require((9*alpha1+6*beta1) % 17 == (6*t+3*u) % 17, 'First A2 jet')
        second = (9*alpha2+6*beta2) % 17
        require(t1 == (12*t*t+9*t*u) % 17 and u1 == (9*t*u+12*u*u) % 17,
                'Root first corrections')
        require(second == (13*t*t+10*t*u) % 17, 'Second A2 jet')
        for v in range(17):
            first_h2 = (6*t+3*u+3*v) % 17
            second_h2 = (second+2*v*v) % 17
            if first_h2 == 0:
                require(second_h2 == (4*t*t+t*u+2*u*u) % 17,
                        'Discriminant-three quadratic form')
            if first_h2 == second_h2 == 0:
                jet_survivors.append([t, u, v])
        second_jets.append({'t0': t, 'u0': u, 't1': t1, 'u1': u1,
                            'A2_second': second})
    require(jet_survivors == [[0, 0, 0]], 'Unexpected second-jet marking')
    require(3 not in {x*x % 17 for x in range(17)}, 'Discriminant must be nonsquare')

    baseline = model(-1, 209)
    F = -sum(C(j, 2)*v for j, v in baseline.items())
    final = model(-1, 209, quadratic=F)
    D, E = final[3], final[1]
    require(D % 17 == 16 and divided(F, 17) % 17 == 8,
            'Final cubic/quadratic constants')
    require(divided(E, 17**2) % 17 == 9, 'Final linear constant')
    rho = -divided(F, 17)*pow(2*D, -1, 17) % 17
    obstruction = (divided(E, 17**2)+divided(F, 17)*rho+D*rho*rho) % 17
    require(rho == 4 and obstruction == 8, 'Final repeated-root contradiction')
    print(json.dumps({'status': 'PASS', 'binaryCensus': records,
                      'survivors': survivors, 'TaylorCoefficients': A,
                      'secondJets': second_jets, 'jetSurvivors': jet_survivors,
                      'secondJetAssignmentCount': 17**3, 'nonsquare': 3,
                      'finalConstants': {'D': D, 'F': F, 'E': E,
                                         'rDiv17': rho, 'obstruction': obstruction},
                      'scope': 'Finite arithmetic only. Cluster occupancy, valuation '
                               'bounds and the arbitrary-ramification jet bridge '
                               'are proved separately in B_EXCLUSION.md.'}, indent=2))


if __name__ == '__main__':
    main()
