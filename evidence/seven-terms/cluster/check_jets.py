"""Exact arithmetic replay for C's residue row (v,u,w)=(2,1,4).

The arbitrary-ramification argument is in PROOF.md. This checker derives
the displayed integer jets and verifies the final Bezout identity. No CAS.
"""
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
P=13
A=-comb(20,16)
B0=-comb(20,15)-16*A
D0=3
E0=-1-A-B0-D0
coefficients={20:1,16:A,15:B0,3:D0,1:E0}

def require(condition,message):
    if not condition:raise RuntimeError(message)

def hasse(x,k):
    return sum(c*comb(n,k)*x**(n-k) for n,c in coefficients.items() if n>=k)

def clean(a):
    a=[x%P for x in a]
    while a and not a[-1]:a.pop()
    return a

def add(a,b):
    return clean([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                  for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return clean(c)

require((A,B0,E0)==(-4845,62016,-57175),'Normalization constants fail')
expansion=[-comb(20,15)*comb(5,i)-(16*A if i<=1 else 0) for i in range(6)]
require(expansion==[62016,0,-155040,-155040,-77520,-15504],
        'Exact expansion of B(1+s) fails')
require((-155040)%13!=0,'Quadratic coefficient must be a unit')
J=[[hasse(2,1)%13,(2**3-2)%13],[(4*hasse(2,4))%13,1]]
require(J==[[9,6],[4,1]],'Wrong local Jacobian')
require((J[0][0]*J[1][1]-J[0][1]*J[1][0])%13==11,'Jacobian is not a unit')
require(hasse(1,1)==13*61198,'Constant f prime(1) is incorrect')
require(hasse(1,2)%13==9,'Linear s coefficient is not 9')
require(hasse(4,1)%13==0 and hasse(4,2)%13==0,'Triple-cluster low jets are nonzero')
require((3*hasse(4,3))%13==2,'Quadratic Taylor coefficient of f prime is not 2')

base_values=[hasse(2,0),hasse(2,3),hasse(4,0)]
require(all(a%13==0 for a in base_values),'Constant defects not divisible by 13')
constants=[a//13%13 for a in base_values]
require(constants==[12,6,1],'Wrong first-order constants')
M=[
    [hasse(2,1)%13,(2**3-2)%13,(2**10-2)%13],
    [(4*hasse(2,4))%13,1,(comb(10,3)*2**7)%13],
    [0,(4**3-4)%13,(4**10-4)%13],
]
require(M==[[9,6,8],[4,1,7],[0,8,5]],'Wrong first-order matrix')
det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
     -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
     +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))%13
require(det==2,'Jet system is not invertible')
solution=[5,7,12] # (t,l,k)
require(all((sum(a*b for a,b in zip(row,solution))+constant)%13==0
            for row,constant in zip(M,constants)),'Jet solution fails')

middle=comb(20,10)
require(middle%13==0 and (middle//13)%13==3,'Middle binomial valuation mismatch')
require(comb(16,10)%13==0 and comb(15,10)%13==0,'Middle derivative coefficients not divisible')
inv=pow(middle//13,-1,13)
g=[0]*11
g[10]=1
g[6]=(comb(16,10)//13*A*inv)%13
g[5]=(comb(15,10)//13*B0*inv)%13
g[0]=(solution[2]*inv)%13
require((g[6],g[5],g[0])==(11,7,4),'Divided H10 reduction fails')
h=[0]*21
for n,c in coefficients.items():h[n]=c%13
require([(n,c) for n,c in enumerate(h) if c]==[(1,12),(3,3),(15,6),(16,4),(20,1)],
        'Seed reduction mismatch')
U=[2,-3,5,-1,5,3,0,6,-2,1]
V=[-3,-6,-4,3,2,6,4,-3,5,4,0,-1,1,2,-5,4,0,-6,2,-1]
identity=add(mul(U,h),mul(V,g))
require(identity==[1],'Final Bezout identity fails')
require(add(identity,h)!=[1],'Mutation control fails')
receipt={
    'status':'PASS','arithmetic':'Python standard-library integers',
    'baseCoefficients':{str(k):v for k,v in coefficients.items()},
    'BExpansionAtOne':expansion,'localJacobian':J,'localJacobianDeterminant':11,
    'firstOrderMatrix':M,'constantVector':constants,'matrixDeterminant':det,
    'uniqueResidueSolution_t_l_k':solution,
    'middleDerivativeReductionAscending':g,
    'Bezout_U_ascending':clean(U),'Bezout_V_ascending':clean(V),
    'BezoutIdentity':'U*h+V*g=1 in F13[X]',
    'scope':'Arithmetic replay; arbitrary-ramification inequalities are proved in PROOF.md',
}
print(json.dumps(receipt,indent=2))

