#!/usr/bin/env python3
"""Exact arithmetic checks for MIXED_STRATA.md; Python standard library only.

This checks the finite identities used by the proof.  Newton polygons,
cluster root counts and characteristic-zero transfer are argument obligations.
No assertion is used as an acceptance condition, so -O preserves all checks.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import sys

P = 17

def require(ok, message):
    if not ok:
        raise ValueError(message)

def val(n):
    if not n:
        return None
    e = 0
    while n % P == 0:
        n //= P
        e += 1
    return e

def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a

def add(a, b, scale=1, modulus=None):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += scale*x
    if modulus:
        c = [x % modulus for x in c]
    return trim(c)

def mul(a, b, modulus=None):
    c = [0] * (max(0, len(a)+len(b)-1))
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    if modulus:
        c = [x % modulus for x in c]
    return trim(c)

def power(a, e, modulus=None):
    c = [1]
    for _ in range(e):
        c = mul(c, a, modulus)
    return c

def compose(a, b, modulus=None):
    c = []
    for x in reversed(a):
        c = add(mul(c,b,modulus),[x],modulus=modulus)
    return c

def divide(a, b):
    a = trim([x%P for x in a])
    b = trim([x%P for x in b])
    require(bool(b), 'division by zero')
    q = [0] * max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        k = len(a)-len(b)
        t = a[-1]*pow(b[-1],-1,P)%P
        q[k] = t
        a = add(a,[0]*k+[(t*x)%P for x in b],-1,P)
    return trim(q),a

def shift(a):
    return [sum(comb(i,k)*x for i,x in enumerate(a) if i>=k)
            for k in range(len(a))]

def normalized_derivative(j, a):
    q = [0]*(j+1)
    for i,x in a.items():
        if i<=j:
            q[j-i] += comb(j,i)*x
    return trim(q)

def full_polynomial(J,a):
    f = [0]*21
    f[20] = 1
    d = -comb(20,3)
    for j in J:
        f[20-j] = comb(20,j)*a[j]
        d -= comb(20-j,3)*comb(20,j)*a[j]
    f[3] = d
    f[1] = -sum(f)
    require(sum(f)==0,'f(1) normalization')
    require(sum(comb(i,3)*x for i,x in enumerate(f) if i>=3)==0,
            'H3 normalization')
    return f

CASES = [
    dict(name='10-12-13-16',J=[10,12,13,16],residues=[16,14,1,0],
         baseline=[-1,65,-560,0],kappa=5,epsilon=6,
         derivatives=[10,16,0], variations=[[7,0,0],[14,1,0],[9,4,0]],
         lam=[14,2,0],phi=[12,10],quadratic=[13,2,5],
         remainder=[11,2],last=13,critical=13,quadjet=-780,
         H=1961247925,H2=10,forced=[242879,3],a16numerator=3,
         weights=[-42678636,-13226850,-4961280,-24225]),
    dict(name='9-10-15-16',J=[9,10,15,16],residues=[16,9,9,0],
         baseline=[-1,9,-22023,0],kappa=3,epsilon=7,
         derivatives=[9,0,9], variations=[[8,0,0],[5,0,0],[8,0,8]],
         lam=[12,0,3],phi=[15,13],quadratic=[6,16,3],
         remainder=[4,3],last=7,critical=10,quadjet=45,
         H=5132750687,H2=7,forced=[15890869,75],a16numerator=1,
         weights=[-53747200,-42678636,-248064,-24225]),
]

receipt = {'prime':P, 'checks':[], 'scope':'finite identities only; see MIXED_STRATA.md for valuation and coverage proofs'}
R = [0,-2,1]+[0]*14+[1]
for case in CASES:
    J=case['J']; a=dict(zip(J,case['baseline'])); av={0:1,**a}
    require([x%P for x in case['baseline']]==case['residues'],'baseline residues')
    f=full_polynomial(J,a); c=shift(f)
    zero={j:0 for j in J}
    base_poly=full_polynomial(J,zero)
    base_shift=shift(base_poly)
    require(all(base_shift[k]%P==0 for k in range(1,17)),
            'constant shifted coefficients lie in 17Z')
    for j in J:
        unit=zero.copy();unit[j]=1
        increment=add(shift(full_polynomial(J,unit)),base_shift,-1)
        require(all((increment[k] if k<len(increment) else 0)%P==0
                    for k in range(1,17)),
                'variable shifted coefficients lie in 17Z')
    weights=[((19-j)-2*comb(20-j,3))*comb(20,j) for j in J]
    require(weights==case['weights'],'H weights')
    require(c[1]==case['H'],'H baseline')
    require(val(c[1])==2 and c[1]//P**2%P==case['H2'],'H valuation')
    require(val(f[1])==1 and f[1]//P%P==case['epsilon'],'E valuation')
    require(f[3]%P==16,'D residue')
    require(val(c[2])==1 and c[2]//P%P==case['kappa'],'c2 residue')
    require(c[3]==0,'c3 exact zero')
    require(all(c[k]%P==0 for k in range(4,17)),'middle shifted coefficients')
    require(c[17]%P==1,'c17 residue')

    # Complete binary reconstruction and the divided-H condition.
    census=[]
    for bits in product((0,1),repeat=4):
        residues={0:1}
        for j,w in zip(J,bits):
            residues[j]=-sum(comb(j,i)*x*w**(j-i)
                             for i,x in residues.items())%P
        W=(-133+sum((h//P)*residues[j] for j,h in zip(J,weights)))%P
        census.append({'witnesses':list(bits),'coefficients':[residues[j] for j in J],'W':W})
    survivors=[x for x in census if x['W']==0]
    require(survivors==[
        {'witnesses':[0,0,0,1],'coefficients':[0,0,0,16],'W':0},
        {'witnesses':[1,1,1,0],'coefficients':case['residues'],'W':0}],
        'binary census survivor list')

    # First-order normalized-Gj recurrence at the all-unit baseline.
    derivatives=[]; variations={}
    for k,j in enumerate(J[:3]):
        g=normalized_derivative(j,av)
        require(sum(g)==0,'all-unit baseline Gj identity')
        derivative=sum(e*x for e,x in enumerate(g))%P
        derivatives.append(derivative)
        row=[0]*3;row[k]=-derivative
        for i,earlier in variations.items():
            for l in range(3):row[l]-=comb(j,i)*earlier[l]
        variations[j]=[x%P for x in row]
    require(derivatives==case['derivatives'],'derivative residues')
    require(list(variations.values())==case['variations'],'first variations')
    lam=[sum((h//P)*variations[j][k] for j,h in zip(J[:3],weights[:3]))%P
         for k in range(3)]
    require(lam==case['lam'],'lambda identity')

    # Exact finite-field elimination of a nonzero repeated leading point.
    phi=case['phi']; Q=add(compose(R,phi,P),R,-phi[1],P)
    require(Q==case['quadratic'],'R(phi)-beta*R identity')
    quotient,remainder=divide(R,Q)
    require(remainder==case['remainder'],'first Euclidean remainder')
    quotient2,last=divide(Q,remainder)
    require(last==[case['last']],'second Euclidean remainder')
    require(case['last']%P!=0,'Euclidean gcd unit')
    # In the zero-leading repeated branch, the paired roots have ratio beta.
    require(pow(phi[1],15,P)!=1,'zero-leading root ratio exclusion')

    g16=normalized_derivative(16,av)
    require(sum(g16)%P==(13 if J[0]==10 else 2),'G16 at unit residue')
    first_power=next(k for k,x in enumerate(g16) if k and x%P)
    require(first_power==case['a16numerator'],'small-root leading exponent')
    gcritical=normalized_derivative(case['critical'],av)
    jets=shift(gcritical)
    require(jets[0]==0 and jets[1]==0 and jets[2]==case['quadjet'],
            'critical derivative jets')
    require(jets[2]%P!=0,'critical quadratic jet unit')
    forced=Fraction(-c[1],weights[-1])
    require([forced.numerator,forced.denominator]==case['forced'],'forced a16')
    require(val(forced.numerator)-val(forced.denominator)==1,'forced a16 valuation')
    critical_weight=(weights[2] if J[0]==10 else weights[1]-comb(15,10)*weights[2])
    require(val(critical_weight)==1,'remaining coefficient solved by H with unit after division')
    if J[0]==9:
        require(comb(15,9)-1==5004 and comb(15,10)==3003,'G15 exact relation')
    receipt['checks'].append({
        'name':case['name'],'support':J+[17,19],
        'binary_census':census,'E_over_17_residue':case['epsilon'],
        'c2_over_17_residue':case['kappa'],'lambda':lam,
        'unit_derivative_residues':derivatives,
        'g16_unit_value':sum(g16)%P,'g16_small_exponent':first_power,
        'critical_Gj':case['critical'],'critical_quadratic_jet':jets[2],
        'quadratic':Q,'R_mod_quadratic':remainder,'last_remainder':last,
        'R_quotient':quotient,'quadratic_quotient':quotient2,
        'baseline_H':c[1],'baseline_H_valuation':val(c[1]),
        'critical_effective_H_weight':critical_weight,
        'forced_a16':[forced.numerator,forced.denominator],
        'forced_a16_valuation':1,
        'small_root_required_a16_valuation':[first_power,2],
    })

# A corrupted finite identity must fail; this protects against a dead checker path.
mutated=CASES[0]['quadratic'].copy();mutated[0]=(mutated[0]+1)%P
require(add(compose(R,CASES[0]['phi'],P),R,-CASES[0]['phi'][1],P)!=mutated,
        'negative control was not rejected')
receipt['negative_control']='changed quadratic constant rejected'
receipt['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
receipt['status']='PASS'
print(json.dumps(receipt,indent=2,sort_keys=True))
