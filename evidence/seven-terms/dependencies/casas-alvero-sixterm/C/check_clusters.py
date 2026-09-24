"""Replay finite-field cluster gcds, independently of the seed Groebner basis."""
import json
from pathlib import Path
import sympy as s

x=s.symbols('x')
def poly(a):return s.Poly(a,x,modulus=13)
def require(test,message):
    if not test:raise RuntimeError(message)

expected={
  2:{16:x-1,15:(x-1)*(x*x+4*x-2),3:x+3,1:x*x},
  3:{16:x-1,15:(x-1)**2*(x-2),3:x-2,1:(x-1)*(x-4)**2},
  10:{16:x-1,15:x-1,3:x+2,1:(x-3)*(x+2)},
}
records=[]
for c,d in ((2,0),(3,12),(10,5)):
    h=poly(x**20+4*x**16+6*x**15+c*x**3+d*x)
    row={'coefficients':[4,6,c,d],'gcds':{}}
    for order in (16,15,3,1):
        derivative=poly(sum(coefficient*s.binomial(exponent[0],order)*x**(exponent[0]-order)
                            for exponent,coefficient in h.terms() if exponent[0]>=order))
        result=s.gcd(h,derivative).monic()
        require(result==poly(expected[c][order]).monic(),f'Cluster mismatch c={c},order={order}')
        row['gcds'][str(order)]=str(result.as_expr())
    records.append(row)

receipt={'status':'PASS','scope':'Gcds at the three stated coefficient points; not completeness of classification',
         'coefficient_order':['a','b','c','d'],'points':records}
Path(__file__).with_name('cluster-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
