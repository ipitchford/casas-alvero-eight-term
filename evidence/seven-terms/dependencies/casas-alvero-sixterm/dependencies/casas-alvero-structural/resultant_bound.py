"""Retain integral contents before deriving a finite exceptional-prime bound."""
import json
import sys
from pathlib import Path
import sympy as s

sys.set_int_max_str_digits(200000)
out = Path(__file__).resolve().parent
z = s.symbols('z')
P = 35*(17-z**3)
Q = z**2*(51-35*z)
R = 35*(z**18-17**5)
S = 17**3*(51*z**6-35*17**2)
A, B = 34*P, 35*(Q-P)
En = s.Poly(A**4*P**2 + 6*A**2*B**2*P*Q + B**4*Q**2, z)
On = s.Poly(4*A*B*(A**2*P+B**2*Q), z)
N = s.Poly(R, z)*En - s.Poly(34**4*S*Q**6, z)
N = N**2-s.Poly(P*Q*R**2,z)*On**2
content, H = N.primitive()
frozen = json.loads(out.joinpath('fixed-polynomial.json').read_text())
if [int(c) for c in H.all_coeffs()] != frozen['H_coefficients_high_first']:
    raise RuntimeError('The reconstructed primitive polynomial does not match H')
print('integral content', content, s.factorint(content), flush=True)
C = s.Poly(sum(c*17**(2*(H.degree()-i))*z**(6*i)
              for i,c in enumerate(H.all_coeffs())), z)
print('resultant start', H.degree(), C.degree(), flush=True)
res = int(s.resultant(H,C))
print('resultant digits', len(str(abs(res))), flush=True)
out.joinpath('resultant-integer.txt').write_text(str(res)+'\n')
record = {'H_degree': H.degree(), 'C_degree': C.degree(),
          'raw_numerator_content': str(content),
          'content_factorization': {str(p):int(e) for p,e in s.factorint(content).items()},
          'resultant_nonzero': res != 0, 'resultant_digits': len(str(abs(res)))}
small = {}
residual = abs(res)
for p in s.primerange(2,10000):
    while residual % p == 0:
        small[str(p)] = small.get(str(p),0)+1
        residual //=p
record['trial_factors_below_10000'] = small
record['unfactored_cofactor'] = str(residual)
record['unfactored_cofactor_digits'] = len(str(residual))
out.joinpath('resultant-bound.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='unfactored_cofactor'},indent=2),flush=True)
