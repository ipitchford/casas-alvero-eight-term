#!/usr/bin/env python3
"""Exact arithmetic replay; it does not certify analytic/valuation arguments."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def vp(n, p):
    require(n != 0, 'zero has no finite valuation')
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


# A pair (constant, slope) denotes constant+slope*delta.
def shifted(bounds, constant, slope):
    return {(c+constant, s+slope) for c, s in bounds}


def dominates(lhs, rhs):
    """Prove min(lhs)>=min(rhs) for all delta>=0 by all affine breakpoints."""
    lines = lhs | rhs
    points = {Fraction(0)}
    for c, s in lines:
        for d, t in lines:
            if s != t:
                x = Fraction(d-c, s-t)
                if x >= 0:
                    points.add(x)
    # Between breakpoints both lower envelopes are affine. Endpoints and
    # the asymptotic slopes certify the entire positive ray.
    for x in points:
        require(min(c+s*x for c, s in lhs) >= min(c+s*x for c, s in rhs),
                'tropical bound fails at an exact breakpoint')
    require(min(s for c, s in lhs) >= min(s for c, s in rhs),
            'tropical bound fails at infinity')


tropical = []
for J in range(4, 17):
    bounds = {0: {(0, 0)}, 2: {(0, 2)}, 3: {(0, 0)}}
    for j in range(4, J+1):
        bounds[j] = {(0, 0)}
    for j in range(J+1, 20):
        generated = set()
        for i in range(j):
            if i == 1:
                continue
            generated |= shifted(bounds[i], vp(comb(j, i), 17), j-i)
        target = {(0, j-J)} if j <= 16 else {(0, j), (1, j-J)}
        dominates(generated, target)
        bounds[j] = target
    other_terms = set()
    for j in range(20):
        if j in (1, 3):
            continue
        other_terms |= shifted(bounds[j], vp(comb(20, j), 17), 20-j)
    dominates(other_terms, {(0, 20), (1, 20-J)})
    delta = Fraction(1, J-3)
    require(17*delta == 1+(20-J)*delta < 20*delta,
            'minimal-root cancellation threshold differs')
    for L in range(4, J+1):
        # The product U*V coefficient uses U-index r=(20-L)-s, 0<=s<=3.
        require(min(17-((20-L)-s) for s in range(4)) == L-3,
                'cluster-factor coefficient lower bound differs')
    for j in range(20):
        if j == 1:
            continue
        valuation = min(c+s*delta for c, s in bounds[j])
        scaled = vp(comb(20, j), 17)+valuation+(20-j-17)*delta
        require(scaled >= 0, 'rescaling is not coefficientwise integral')
        if j < J and j != 3:
            require(scaled > 0, 'a forbidden high-degree term survives')
    tropical.append({'J': J, 'nondegenerateScale': str(delta), 'm': 20-J})


def add(P, Q, scalar=1):
    result = dict(P)
    for monomial, coefficient in Q.items():
        c = (result.get(monomial, 0)+scalar*coefficient) % 17
        if c:
            result[monomial] = c
        else:
            result.pop(monomial, None)
    return result


def monomial(n, index, degree, coefficient=1):
    exponents = [0]*n
    exponents[index] = degree
    return {tuple(exponents): coefficient % 17} if coefficient % 17 else {}


def times_variable(P, index, power):
    result = {}
    for key, value in P.items():
        new = list(key)
        new[index] += power
        result[tuple(new)] = value
    return result


def validate_equation(E, n, index, m):
    lead = next(iter(monomial(n, index, 17)))
    require(E.get(lead) == 1, 'leading coefficient is not one')
    require(all(key == lead or sum(key) == m for key in E),
            'the lower tail is not homogeneous of degree m')
    require(m < 17, 'the purported leading term need not lead')


models = []
for m in range(4, 14):
    n = m-2
    coefficients = {m: {tuple([0]*n): 16}, m-1: {}}
    equations = []
    for k in range(m-2, 0, -1):
        c = monomial(n, k-1, m-k, comb(m, k))
        for i in range(k+1, m-1):
            c = add(c, times_variable(coefficients[i], k-1, i-k), -comb(i, k))
        require(all(sum(key) == m-k for key in c), 'coefficient degree differs')
        coefficients[k] = c
        derivative = {}
        for i in range(k, m+1):
            derivative = add(derivative, times_variable(coefficients[i], k-1, i-k), comb(i, k))
        require(not derivative, 'Hasse common-root identity failed')
    for k in range(1, m-1):
        E = monomial(n, k-1, 17)
        for i, coefficient in coefficients.items():
            E = add(E, times_variable(coefficient, k-1, i))
        validate_equation(E, n, k-1, m)
        equations.append(E)
    # Exact criterion used by the hand proof; no enormous basis expansion.
    leads = [next(iter(monomial(n, k, 17))) for k in range(n)]
    require(all(all(min(a, b) == 0 for a, b in zip(leads[i], leads[j]))
                for i in range(n) for j in range(i)), 'leading monomials are not coprime')
    broken = add(equations[0], monomial(n, 1, 18))
    try:
        validate_equation(broken, n, 0, m)
    except ValueError:
        pass
    else:
        raise ValueError('bad leading-degree negative control accepted')
    models.append({'m': m, 'variables': n, 'standardMonomialDimension': 17**n,
                   'equationTermCounts': [len(E) for E in equations]})


base = Path(__file__).resolve().parent
strata = json.loads((base/'residue-strata.json').read_text())
nondegenerate = degenerate = 0
by_J = {}
for record in strata['strata']:
    J, L, count = (record[name] for name in
                   ('lastUnitDegree', 'lastUnitCoefficientDegree', 'count'))
    require(4 <= L <= J <= 16 and count > 0, 'invalid J/L stratum')
    by_J.setdefault(J, [0, 0])[int(J != L)] += count
    if J == L:
        nondegenerate += count
    else:
        degenerate += count
require((nondegenerate, degenerate) == (179765, 576), 'stratum counts differ')
require(nondegenerate+degenerate == strata['totalFilteredAssignments'] == 180341,
        'strata are not a complete partition')
require(strata['nondegenerateAssignments'] == nondegenerate and
        strata['degenerateAssignments'] == degenerate, 'reported stratum totals differ')
require(nondegenerate+degenerate != nondegenerate, 'degenerate-case failure control')
prior = json.loads((base.parent/'row8-residue-enumeration.json').read_text())
require(prior['afterUnitRootCollisionObstructions'] == nondegenerate+degenerate,
        'new strata do not cover the prior census')

# Complete prime-19 special fibre. The DFS stores no exponentially large output.
# Since each w is literally a chosen bit, the derivative recurrence below has
# leading term 0 or 1; every f(w) is then checked from the ordinary coefficients.
require([j for j in range(21) if comb(20, j) % 19] == [0, 1, 19, 20],
        'degree20 Lucas visibility at19 differs')
require(all(comb(19, j) % 19 == 0 for j in range(1, 19)), 'G19 does not collapse')
binomials = [[comb(j, i) % 19 for i in range(j+1)] for j in range(20)]
a = [0]*21
a[0], a[19] = 1, 18
point_count = 0
checksum = 0


def traverse(j):
    global point_count, checksum
    if j == 19:
        require(sum(binomials[19][i]*a[i] for i in range(20)) % 19 == 0,
                'G19(1) fails at a marked point')
        require(sum(comb(20, i)*a[i] for i in range(21)) % 19 == 0,
                'f(1) fails at a marked point')
        point_count += 1
        checksum = (checksum+sum((i+1)*a[i] for i in range(21))) % 1000000007
        return
    a[j] = 0  # w_j=0; constant coefficient of G_j is a_j.
    traverse(j+1)
    a[j] = -sum(binomials[j][i]*a[i] for i in range(j)) % 19  # w_j=1
    require(sum(binomials[j][i]*a[i] for i in range(j+1)) % 19 == 0,
            'triangular derivative equation fails')
    traverse(j+1)


traverse(2)
require(point_count == 2**17, 'prime19 marked fibre is incomplete')

print(json.dumps({'status': 'PASS', 'tropicalBounds': tropical,
                  'finiteLeadingModels': models, 'strataByJ': by_J,
                  'nondegenerateAssignments': nondegenerate,
                  'degenerateAssignmentsRetained': degenerate,
                  'prime19MarkedSpecialFibrePoints': point_count,
                  'prime19CoefficientChecksum': checksum,
                  'negativeControls': ['degree18 lower-tail mutation rejected',
                                       'discarding576degeneratecases rejected'],
                  'scope': 'Exact arithmetic and polynomial identities only; no lift enumeration or branch exclusion.'}, indent=2))
