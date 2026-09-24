"""Exact, fixed-degree necessary conditions for the p+7 sparse family."""
import json
from pathlib import Path
import sympy as s

z = s.symbols('z')
out = Path(__file__).resolve().parent

def numerator(expr):
    return s.Poly(s.cancel(expr).as_numer_denom()[0], z, domain=s.QQ).clear_denoms()[1].primitive()[1]

T = 35*(17-z**3)/(z**2*(51-35*z))
psi = 17**2/z**6
U = s.cancel(T.subs(z, psi))
A, B = 34*T, 35*(1-T)
E = A**4*T**2 + 6*A**2*B**2*T + B**4
O = 4*A*B*(A**2*T+B**2)
H = numerator((U*E-34**4)**2-T*(U*O)**2)
print('H degree', H.degree(), flush=True)
fac = s.factor_list(H)
print('H factors', [(f.degree(), e) for f,e in fac[1]], flush=True)
out.joinpath('fixed-polynomial.json').write_text(json.dumps({
    'variable': 'z=t^2', 'T': str(T), 'psi': str(psi),
    'H_coefficients_high_first': [int(x) for x in H.all_coeffs()],
    'factors': [{'degree': f.degree(), 'multiplicity': e,
                 'coefficients_high_first': [int(x) for x in f.all_coeffs()]}
                for f,e in fac[1]],
}, indent=2)+'\n')
G = H.sqf_part()
for step in range(1, 10):
    C = s.Poly(sum(c*17**(2*(G.degree()-i))*z**(6*i)
                  for i,c in enumerate(G.all_coeffs())), z)
    Gnew = s.gcd(G, C)
    print('dynamic gcd', step, G.degree(), C.degree(), Gnew.degree(), flush=True)
    out.joinpath(f'dynamic-gcd-{step}.json').write_text(json.dumps({
        'previous_degree': G.degree(), 'composition_degree': C.degree(),
        'gcd_degree': Gnew.degree(),
        'gcd_coefficients_high_first': [str(x) for x in Gnew.all_coeffs()],
    }, indent=2)+'\n')
    if Gnew.degree() == 0 or Gnew.degree() == G.degree():
        break
    G = Gnew
