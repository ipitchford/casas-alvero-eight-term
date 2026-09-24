#!/usr/bin/env python3
"""Independent coefficient reconstruction of the direct unit-16 Q jet."""
from fractions import Fraction
from math import comb
import json

def require(condition, label):
    if not condition:
        raise ValueError(label)

def v17(n):
    if n==0:
        return None
    k=0
    while n%17==0:
        n//=17;k+=1
    return k

# Q=f'-f/X.  A term A*X^e contributes (e-1)A*X^(e-1).
# Solve H3f(1)=0 for D.  Then substitute u=-x^16-560*t*x^13.
# Keep separate arrays for coefficients of 1 and t.
Q=[[0]*20 for _ in range(2)]
Q[0][19]+=19
Q[1][16]+=16*1140
Q[0][2]-=2*1140
Q[1][2]-=2*comb(17,3)*1140
for degree,coefficient in ((3,3*4845),(2,-2*comb(4,3)*4845)):
    Q[0][degree+16]-=coefficient
    Q[1][degree+13]-=560*coefficient
expected0={19:-14516,18:38760,2:-2280}
expected1={16:-8121360,15:21705600,2:-1550400}
require(Q[0]==[expected0.get(i,0) for i in range(20)],'Q0 reconstruction')
require(Q[1]==[expected1.get(i,0) for i in range(20)],'Q1 reconstruction')
jets=[sum(comb(k,i)*Q[0][k] for k in range(i,20)) for i in range(20)]
require([v17(jets[i]) for i in range(3)]==[2,2,1],'three low valuations')
require(jets[2]//17%17==1 and jets[17]%17==2,'initial residues')
require(all(jets[i]%17==0 for i in range(3,17)),'intermediate divisibility')
values=[(i,Fraction(v17(x))+Fraction(i,15)) for i,x in enumerate(jets) if x]
minimum=min(v for i,v in values)
require(minimum==Fraction(17,15),'minimum valuation')
require([i for i,v in values if v==minimum]==[2,17],'minimum indices')
require((1+2*7)%17==15,'nonzero leading residue')
require(v17(sum(Q[0]))==2,'root exactly one')
require(sum(Q[1])%17==16,'Q1 at one is unit')
print(json.dumps({'status':'PASS','Q0':Q[0],'Q1':Q[1],'Q0_shifted':jets,
    'lowest_terms':[2,17],'lowest_value':'17/15','leading_factor':15,
    'root_one_value':sum(Q[0]),'scope':'finite integer identities only'},indent=2))
