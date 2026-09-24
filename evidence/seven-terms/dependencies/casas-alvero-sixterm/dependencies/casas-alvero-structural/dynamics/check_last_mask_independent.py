"""Independent direct-resultant audit of the final characteristic-13 mask.

Unlike the producer, this uses the full cubic/degree-16 resultant, not its
pseudo-remainder and 5x5 determinant. Explicit exceptions survive python -O.
"""
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / 'sixterm' / 'last-mask-probe.json'
data = json.loads(INPUT.read_text())
v, T, t = s.symbols('v T t')


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def polynomial(coefficients, variable):
    return s.Poly(sum(c * variable**i for i, c in enumerate(coefficients)),
                  variable, modulus=13)


Q = (5*T+1)*v**3 + (3-4*T)*v - 5
R = s.Poly(s.resultant(Q, v**16-T, v), T, modulus=13)
require(R == polynomial(data['R'], T), 'Direct resultant mismatch')
require(R.degree() == 19, 'Unexpected resultant degree')

D, E = 10*t**2+4, -t**3+t**2-6
direct_U = s.Poly(E*(t**19+4*t**2-5) + D*(4*t**3-3*t**2-1),
                  t, modulus=13)
U = polynomial(data['ratioPolynomialU'], t)
require(direct_U == U, 'Ratio polynomial mismatch')
composition = s.Poly(sum(c*E**i*D**(19-i)
                        for i, c in enumerate(data['R'])), t, modulus=13)
H = polynomial(data['substitutedRemainderH'], t)
require(composition.rem(U) == H, 'Substitution remainder mismatch')

BU = polynomial(data['bezoutU'], t)
BH = polynomial(data['bezoutH'], t)
require(BU*U + BH*H == s.Poly(1, t, modulus=13),
        'Bezout identity fails')

# Every zero of the quadratic denominator is among these two field elements.
require(s.Poly(D, t, modulus=13) == s.Poly(10*(t-6)*(t-7), t, modulus=13),
        'Denominator factorization fails')
require([int(E.subs(t, w)) % 13 for w in (6, 7)] == [9, 12],
        'Denominator branch is not excluded')

# Constants in each coefficient degeneration; proofs are in the audit note.
require(pow(9, 6, 13) == 1 and pow(8, 3, 13) == 5,
        'c=0 chart constants fail')
require(pow(2, 16, 13) == 3, 'd=0 chart constant fails')
require(pow(10, 9, 13) == 12 and pow(9, 2, 13) == 3,
        'a=0 chart constants fail')

receipt = {
    'status': 'PASS',
    'method': 'SymPy direct resultant of cubic and degree-16 equation',
    'direct_resultant_matches_all_coefficients': True,
    'R_degree': R.degree(), 'U_degree': U.degree(), 'H_degree': H.degree(),
    'homogenized_substitution_remainder_matches': True,
    'Bezout_identity_verified_by_multiplication': True,
    'Bezout_degrees': [BU.degree(), BH.degree()],
    'saved_Bezout_array_lengths': [len(data['bezoutU']), len(data['bezoutH'])],
    'denominator_and_zero_chart_constants_checked': True,
}
(HERE / 'last-mask-independent-check.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
