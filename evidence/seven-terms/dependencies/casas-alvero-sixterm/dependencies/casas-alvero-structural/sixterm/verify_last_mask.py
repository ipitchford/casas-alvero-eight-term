#!/usr/bin/env python3
"""Independent exact replay for ONE last-mask probe.
Uses a 19x19 Sylvester determinant with polynomial Bareiss elimination,
independent of the producer's 5x5 determinant and scaled-power recurrence.
All arithmetic is Python standard library over F13.
"""
from pathlib import Path
import hashlib,json
p=13
Z={};ONE={0:1};X={1:1}
def add(a,b):
    c=dict(a)
    for i,x in b.items():c[i]=(c.get(i,0)+x)%p
    return {i:x for i,x in c.items() if x}
def scale(a,c):return {i:x*c%p for i,x in a.items() if x*c%p}
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=(c.get(i+j,0)+x*y)%p
    return {i:x for i,x in c.items() if x}
def divmod_poly(a,b):
    if not b:raise ZeroDivisionError
    r=dict(a);q={};db=max(b);ib=pow(b[db],-1,p)
    while r and max(r)>=db:
        k=max(r)-db;c=r[max(r)]*ib%p;q[k]=c
        r=sub(r,{i+k:c*x%p for i,x in b.items()})
    return q,r
def mod(a,b):return divmod_poly(a,b)[1]
def power(a,k,m=None):
    z=ONE
    for _ in range(k):
        z=mul(z,a)
        if m is not None:z=mod(z,m)
    return z
def exactdiv(a,b):
    q,r=divmod_poly(a,b)
    if r:raise ValueError('Polynomial Bareiss division was not exact')
    return q
def det(a):
    a=[[dict(x) for x in row] for row in a];prev=ONE;sgn=1;n=len(a)
    for k in range(n-1):
        if not a[k][k]:
            index=next((i for i in range(k+1,n) if a[i][k]),None)
            if index is None:return Z
            a[k],a[index]=a[index],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):a[i][j]=exactdiv(sub(mul(pivot,a[i][j]),mul(a[i][k],a[k][j])),prev)
            a[i][k]=Z
        prev=pivot
    return scale(a[-1][-1],sgn)
def fromlist(a):return {i:x%p for i,x in enumerate(a) if x%p}
def evaluate(a,t):return sum(c*pow(t,i,p) for i,c in a.items())%p

def main():
    root=Path(__file__).resolve().parent;path=root/'last-mask-probe.json';data=json.loads(path.read_text())
    A={0:1,1:5};B={0:3,1:-4};Q=[A,Z,B,{0:-5}]
    F=[ONE]+[Z]*15+[scale(X,-1)]
    matrix=[[Z]*i+F+[Z]*(2-i) for i in range(3)]+[[Z]*i+Q+[Z]*(15-i) for i in range(16)]
    R=det(matrix)
    if R!=fromlist(data['R']):raise ValueError('Independent19x19 resultant does not match supplied R')
    D={0:4,2:10};E={0:-6,2:1,3:-1}
    U=add(mul(E,{19:1,2:4,0:-5}),mul(D,{3:4,2:-3,0:-1}))
    if U!=fromlist(data['ratioPolynomialU']):raise ValueError('Ratio-polynomial identity failed')
    H={}
    for i,c in R.items():H=mod(add(H,scale(mul(power(E,i,U),power(D,19-i,U)),c)),U)
    if H!=fromlist(data['substitutedRemainderH']):raise ValueError('Independent substituted remainder differs')
    cu=fromlist(data['bezoutU']);ch=fromlist(data['bezoutH'])
    if add(mul(cu,U),mul(ch,H))!=ONE:raise ValueError('Bezout identity failed')
    if add(mul(add(cu,ONE),U),mul(ch,H))==ONE:raise ValueError('Mutation control failed')
    # Exact scalar checks used by the zero-coefficient and denominator charts.
    if pow(9,6,p)!=1 or pow(8,3,p)!=5 or pow(2,16,p)!=3:raise ValueError('Zero-chart scalar identities failed')
    roots=[t for t in range(p) if evaluate(D,t)==0]
    if roots!=[6,7] or [evaluate(E,t) for t in roots]!=[9,12]:raise ValueError('Denominator chart check failed')
    result={'status':'PASS','producerRecordSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'independentResultantMethod':'19x19 Sylvester matrix, polynomial Bareiss; producer used5x5 scaled remainder','Rdegree':max(R),'Udegree':max(U),'Hdegree':max(H),'bezoutCoefficientSlots':len(data['bezoutU'])+len(data['bezoutH']),'bezoutNonzeroTerms':len(cu)+len(ch),'exactBezoutIdentity':'CU*U+CH*H=1','mutationControl':'PASS','zeroChartScalarChecks':'PASS','denominatorChart':'D roots6,7 have B values9,12','assurance':'Arithmetic identities verified; the accompanying normalization and necessary-equation implications remain written mathematics.'}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
