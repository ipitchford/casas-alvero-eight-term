"""Read-only independent exact replay for the u=v collision exclusion.

Integer Sylvester determinants certify the supplied integer resultants at
more points than a proved coefficient-degree bound. Exact common factors
are divided in Z[u]; degree-preserving modular gcds certify coprimality of
the quotients over Q. This is not an affine modular-emptiness argument.
"""
from math import comb
from pathlib import Path
from time import perf_counter
import hashlib
import json


def require(ok,message):
    if not ok:raise ValueError(message)


def clean(a):
    while a and not a[-1]:a.pop()
    return a


def add(a,b):
    result=[0]*max(len(a),len(b))
    for i,c in enumerate(a):result[i]+=c
    for i,c in enumerate(b):result[i]+=c
    return clean(result)


def scale(a,n):return clean([n*c for c in a])


def mul(a,b):
    if not a or not b:return []
    result=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):result[i+j]+=c*d
    return clean(result)


def shift(a,k):return [0]*k+a if a else []


def power(a,n):
    result=[1]
    for _ in range(n):result=mul(result,a)
    return result


def exact_div(a,b):
    remainder=a[:]
    quotient=[0]*max(0,len(a)-len(b)+1)
    while len(remainder)>=len(b):
        k=len(remainder)-len(b)
        c,r=divmod(remainder[-1],b[-1])
        require(r==0,'Polynomial quotient is not integral')
        quotient[k]=c
        for j,d in enumerate(b):remainder[k+j]-=c*d
        clean(remainder)
    require(not remainder,'Polynomial division has a nonzero remainder')
    return clean(quotient)


def value(a,u):
    result=0
    for c in reversed(a):result=result*u+c
    return result


def gcd_mod(a,b,p):
    a,b=clean([c%p for c in a]),clean([c%p for c in b])
    while b:
        r=a[:]
        inv=pow(b[-1],-1,p)
        while len(r)>=len(b):
            k,c=len(r)-len(b),r[-1]*inv%p
            for j,d in enumerate(b):r[k+j]=(r[k+j]-c*d)%p
            clean(r)
        a,b=b,r
    inv=pow(a[-1],-1,p)
    return [c*inv%p for c in a]


def determinant(a):
    a=[row[:] for row in a]
    previous,sign,n=1,1,len(a)
    for k in range(n-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,r=divmod(a[i][j]*pivot-a[i][k]*a[k][j],previous)
                require(not r,'Integer Bareiss division not exact')
                a[i][j]=q
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]


def resultant(a,b):
    m,n=len(a)-1,len(b)-1
    ah,bh=list(reversed(a)),list(reversed(b))
    matrix=[[0]*(m+n) for _ in range(m+n)]
    for i in range(n):matrix[i][i:i+m+1]=ah
    for i in range(m):matrix[n+i][i:i+n+1]=bh
    return determinant(matrix)


def main():
    started=perf_counter()
    path=Path(__file__).resolve().parent/'certificate.json'
    data=json.loads(path.read_text())
    A=-comb(20,16)
    B=[0,-16*A,0,0,0,-comb(20,15)]
    # f(u)/u=0 and H3(u)=0 express D and E affinely in the X10 coefficient.
    D0=add(add(scale([0]*17+[1],-comb(20,3)),scale([0]*13+[1],-comb(16,3)*A)),scale(shift(B,12),-comb(15,3)))
    Dcoef=[0]*7+[-comb(10,3)]
    E0=scale(add(add(add([0]*19+[1],scale([0]*15+[1],A)),shift(B,14)),shift(D0,2)),-1)
    Ecoef=scale(add([0]*9+[1],shift(Dcoef,2)),-1)
    L0=add(add([1],Dcoef),Ecoef)
    N0=scale(add(add(add([1+A],B),D0),E0),-1)
    L,N=exact_div(L0,[-1,1]),exact_div(N0,[-1,1])
    D=add(mul(D0,L),mul(Dcoef,N))
    E=add(mul(E0,L),mul(Ecoef,N))
    require([len(L)-1,len(N)-1,len(D)-1,len(E)-1]==[8,18,25,25],'Unexpected parameter degrees')
    # Verify f(1)=0 directly as a polynomial identity after clearing L.
    require(not add(add(add(add(scale(L,1+A),mul(L,B)),N),D),E),'f(1) identity failed')
    coefficients={20:L,16:scale(L,A),15:mul(L,B),10:N,3:D,1:E}
    def evaluate_hasse_at_u(order):
        out=[]
        for exponent,c in coefficients.items():
            if exponent>=order:out=add(out,shift(scale(c,comb(exponent,order)),exponent-order))
        return out
    require(not evaluate_hasse_at_u(0),'f(u) identity failed')
    require(not evaluate_hasse_at_u(15),'H15(u) identity failed')
    require(not evaluate_hasse_at_u(3),'H3(u) identity failed')
    Q=[[] for _ in range(20)]
    for exponent,c in coefficients.items():Q[exponent-1]=c
    def hasse(order):
        out=[[] for _ in range(21-order)]
        for exponent,c in coefficients.items():
            if exponent>=order:out[exponent-order]=scale(c,comb(exponent,order))
        return out
    H10,H1=hasse(10),hasse(1)
    maxima=[max(map(len,p))-1 for p in [Q,H10,H1]]
    bounds=[10*maxima[0]+19*maxima[1],19*maxima[0]+19*maxima[2]]
    require(maxima==[25,18,25] and bounds==[592,950],'Wrong proved Sylvester degree bounds')
    R10,R1=data['R10'],data['R1']
    require([len(R10)-1,len(R1)-1]==[422,661],'Wrong supplied resultant degrees')
    evaluations=[]
    for expected,other,bound in zip([R10,R1],[H10,H1],bounds,strict=True):
        require(len(expected)-1<=bound,'Supplied resultant exceeds degree bound')
        for u in range(bound+1):
            fv=[value(c,u) for c in Q]
            hv=[value(c,u) for c in other]
            require(resultant(fv,hv)==value(expected,u),f'Integer resultant mismatch at parameter{u}')
        evaluations.append(bound+1)
    L10=power(L,10)
    S10,S1=exact_div(mul(N,R10),L10),exact_div(R1,L10)
    require([len(S10)-1,len(S1)-1]==[360,581],'Wrong quotient degrees')
    prime=None
    for p in [101,103,107,109,127,131,137,139]:
        if any(f[-1]%p==0 for f in [S10,S1,L,N]):continue
        if gcd_mod(S10,S1,p)==[1] and gcd_mod(L,N,p)==[1]:prime=p;break
    require(prime is not None,'No degree-preserving coprimality prime found')
    # The only excluded exact-division parameter u=1 is absent in our residue class.
    require(value(L,2)%13==4,'Denominator not a unit at the target residue')
    # A coefficient perturbation is detected even at a single integer evaluation.
    changed=R10[:];changed[0]+=1
    require(value(changed,0)!=resultant([value(c,0) for c in Q],[value(c,0) for c in H10]),'Mutation control failed')
    print(json.dumps({'status':'PASS','certificateSha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                      'parameterDegreesL_N_D_E':[len(L)-1,len(N)-1,len(D)-1,len(E)-1],
                      'coefficientDegreeBoundsQ_H10_H1':maxima,'resultantDegreeBounds':bounds,
                      'integerDeterminantEvaluations':evaluations,'resultantDegrees':[len(R10)-1,len(R1)-1],
                      'exactCommonFactor':'L^10','quotientDegrees':[len(S10)-1,len(S1)-1],
                      'degreePreservingPrime':prime,'quotientModularGcd':[1],'L_N_ModularGcd':[1],
                      'parameterizationIdentities':'f(1)=f(u)=H15(u)=H3(u)=0',
                      'L_at_2_mod13':4,'mutationControl':'PASS','elapsedSeconds':perf_counter()-started},indent=2))


if __name__=='__main__':main()
