#!/usr/bin/env python3
"""ONE exact bounded last-mask probe in F13. Standard library, no CAS.
Family h=x20+a*x4+c*x3+d*x. Normalize a=4, exclude c=0,d=0
by separate hand arguments. Then T=v16!=0, A=5T+1!=0,
Q(v)=A*v3+(3-4T)*v-5=0, and v16=T.
"""
from pathlib import Path
from itertools import permutations
import json,time
P=13;ZERO=();ONE=(1,)

def norm(a):
    a=[x%P for x in a]
    while a and not a[-1]:a.pop()
    return tuple(a)
def add(a,b):return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a):return norm([-x for x in a])
def sub(a,b):return add(a,neg(b))
def scale(a,c):return norm([c*x for x in a])
def mul(a,b):
    if not a or not b:return ZERO
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
    return norm(c)
def power(a,k):
    z=ONE
    for _ in range(k):z=mul(z,a)
    return z
def divmod_poly(a,b):
    if not b:raise ZeroDivisionError
    r=list(a);q=[0]*max(0,len(a)-len(b)+1);inv=pow(b[-1],-1,P)
    while len(r)>=len(b):
        i=len(r)-len(b);c=r[-1]*inv%P;q[i]=c
        for j,y in enumerate(b):r[i+j]=(r[i+j]-c*y)%P
        while r and not r[-1]:r.pop()
    return norm(q),norm(r)
def mod(a,b):return divmod_poly(a,b)[1]
def gcdex(a,b):
    r0,r1=a,b;s0,s1=ONE,ZERO;t0,t1=ZERO,ONE
    while r1:
        q,r=divmod_poly(r0,r1);r0,r1=r1,r;s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
    c=pow(r0[-1],-1,P)
    return scale(r0,c),scale(s0,c),scale(t0,c)
def determinant(m):
    out=ZERO
    for perm in permutations(range(len(m))):
        inv=sum(perm[i]>perm[j] for i in range(len(m)) for j in range(i+1,len(m)))
        term=ONE
        for i,j in enumerate(perm):term=mul(term,m[i][j])
        out=add(out,scale(term,(-1)**inv))
    return out

def main():
    start=time.monotonic();X=(0,1)
    A=(1,5);B=(3,-4)
    # q0+q1*v+q2*v2 represents A^k*v^k modulo Q, checked by construction.
    vector=(ONE,ZERO,ZERO)
    for _ in range(16):
        q0,q1,q2=vector
        vector=(scale(q2,5),sub(mul(A,q0),mul(B,q2)),mul(A,q1))
    r0=sub(vector[0],mul(X,power(A,16)));r1=vector[1];r2=vector[2]
    Q=[A,ZERO,B,(-5,)]
    matrix=[Q+[ZERO],[ZERO]+Q,[r2,r1,r0,ZERO,ZERO],[ZERO,r2,r1,r0,ZERO],[ZERO,ZERO,r2,r1,r0]]
    R=determinant(matrix)
    if not R:raise ValueError('Identically zero elimination polynomial')
    raw=R;removed={}
    for name,factor in [('T',X),('5T+1',A)]:
        count=0
        while True:
            q,r=divmod_poly(R,factor)
            if r:break
            R=q;count+=1
        removed[name]=count
    # t=w/v; Wronskian and root equation, with D nonzero.
    D=(4,0,10);E=(-6,0,1,-1) # -t3+t2-6
    U=add(mul(E,add(sub(power(X,19),(5,)),scale(power(X,2),4))),mul(D,add(sub(scale(power(X,3),4),scale(power(X,2),3)),(-1,))))
    H=ZERO;deg=len(R)-1
    for i,c in enumerate(R):H=mod(add(H,scale(mul(mod(power(E,i),U),mod(power(D,deg-i),U)),c)),U)
    g,s,t=gcdex(U,H)
    if add(mul(s,U),mul(t,H))!=g:raise ValueError('Bezout replay failed')
    result={'status':'UNIT' if g==ONE else 'NONUNIT','field':13,'elapsedSeconds':time.monotonic()-start,'rawResultantDegree':len(raw)-1,'removedKnownNonzeroFactors':removed,'R':R,'Rdegree':deg,'ratioPolynomialU':U,'Udegree':len(U)-1,'substitutedRemainderH':H,'Hdegree':len(H)-1,'gcd':g,'bezoutU':s,'bezoutH':t,'coefficientOrder':'ascending powers','scope':'Necessary equations for a!=0,c!=0,d!=0 chart; zero charts require the accompanying handwritten proofs.'}
    Path(__file__).with_name('last-mask-probe.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
