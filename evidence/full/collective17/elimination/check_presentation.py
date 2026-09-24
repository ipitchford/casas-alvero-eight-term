"""Independent standard-library replay of the compact integer presentation.

This checks exact coefficient identities, not the unevaluated final norm.
It imports no code from the producer or earlier mathematical checkers.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
P = 17


def require(ok, message):
    if not ok:
        raise ValueError(message)


def trim(a):
    a = [v % P for v in a]
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    c = [0]*max(len(a),len(b))
    for i,v in enumerate(a): c[i] += v
    for i,v in enumerate(b): c[i] += v
    return trim(c)


def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j] += v*w
    return trim(c)


def rem(a,b):
    a = trim(a)
    while len(a) >= len(b):
        d=len(a)-len(b)
        c=a[-1]*pow(b[-1],-1,P)%P
        for i,v in enumerate(b): a[d+i] -= c*v
        a=trim(a)
    return a


def gcd(a,b):
    while b: a,b=b,rem(a,b)
    return trim([v*pow(a[-1],-1,P) for v in a])


def power(a,n):
    out=[1]
    while n:
        if n & 1: out=mul(out,a)
        a=mul(a,a)
        n//=2
    return out


def main():
    raw=(HERE/'presentation.json').read_bytes()
    doc=json.loads(raw)
    f,g,q=doc['f'],doc['g_f_divided_by_X_minus_1_squared'],doc['g_divided_by_X']
    require([len(f),len(g),len(q)]==[21,19,18], 'polynomial dimensions')
    require(all(len(v)==14 for a in (f,g,q) for v in a), 'affine dimensions')
    require(q==g[1:] and g[0]==[0]*14, 'exact division by X')
    require(g[-1]==[1]+[0]*13 and q[-1]==[1]+[0]*13, 'monic norms')
    checks=0
    # Direct Hasse differentiation and an independent two-by-two solve,
    # performed in each affine basis direction.
    for column in range(14):
        a=[Fraction(0)]*21
        if column==0:
            a[0],a[3]=1,-1
        else:
            a[column+3]=1
        high=[comb(20,j)*a[j] for j in range(18)]
        v=sum(high)
        w=sum((20-j)*high[j] for j in range(18))
        # x=190*a18, y=20*a19 satisfy x+y=-v, 2x+y=-w.
        a[18],a[19]=Fraction(v-w,190),Fraction(w-2*v,20)
        expected=[comb(20,20-k)*a[20-k] for k in range(21)]
        require(expected==[v[column] for v in f], 'independent coefficient solve')
        require(sum(expected)==sum(k*v for k,v in enumerate(expected))==0, 'double root')
        reconstructed=[0]*21
        for k,v in enumerate(g):
            reconstructed[k] += v[column]
            reconstructed[k+1] -= 2*v[column]
            reconstructed[k+2] += v[column]
        require(reconstructed==expected, 'exact g identity')
        h2=sum(comb(k,2)*v for k,v in enumerate(expected) if k>=2)
        require(h2==17*doc['T'][column]==sum(v[column] for v in g), 'exact obstruction')
        for j in range(4,17):
            derivative=[comb(k+20-j,20-j)*expected[k+20-j] for k in range(j+1)]
            scaled=[comb(20,j)*v[column] for v in doc['G'][str(j)]]
            require(derivative==scaled, 'normalized Hasse identity')
            checks+=1
    require(all(v % P==0 for a in g for v in a[1:]), 'constant residue norm polynomial')
    d=trim([v[0] for v in g])
    h=mul(d,[1,-2,1])
    expected=[0]*21
    expected[20],expected[17],expected[2],expected[1]=1,16,14,3
    require(h==expected, 'fixed residue seed')
    require(gcd(d,trim([k*d[k] for k in range(1,len(d))]))==[1], 'squarefree degree-18 domain')
    q5=[14,12,15,0,14,1]
    q10=[9,7,4,11,1,0,6,0,16,4,1]
    require(mul(mul(mul([0,1],[2,1]),[-1,1]),mul(q5,q10))==d, 'root-domain factorization')
    # The Frobenius law is an exact identity modulo the squarefree root domain.
    k=[0]*20
    k[19],k[18],k[17],k[1]=1,1,1,-3
    require(trim(k)==mul([-1,1],d), 'r^17(r^2+r+1)=3r')
    require(gcd(d,[1,1,1])==[1], 'Frobenius denominator invertible')
    # Exclude r=1 by exact division of D by X-1 in F17[X].
    dd=d.copy(); quotient=[0]*18
    for i in range(18,0,-1):
        quotient[i-1]=dd[i]%P
        dd[i]-=quotient[i-1]; dd[i-1]+=quotient[i-1]
    require(not trim(dd),'divide out exceptional root')
    quotient=trim(quotient)
    numerator=add(add([7*v for v in power([1,1],17)],
                      [-49*v for v in mul(power([1,1],2),power([-1,1],15))]),
                  [5*v for v in power([-1,1],17)])
    require(not rem(numerator,quotient),'Frobenius conjugacy equation')
    require(gcd(quotient,[-1,1])==[1], 'conjugacy forward denominator')
    e=[5,0,-1]+[0]*14+[1]
    require(len(e)==18 and gcd(e,[0,-2])==[1], 'separable degree-17 conjugate')
    require(sum(v*pow(7,i,P) for i,v in enumerate(e))%P!=0, 'conjugacy inverse denominator')
    # Necessity masks are an already verified input, not re-proved here.
    dependency=HERE.parents[1]/doc['inventoryDependency']['relativePath']
    source=dependency.read_bytes()
    require(sha256(source).hexdigest()==doc['inventoryDependency']['sha256'],'inventory fingerprint')
    eligible=sorted(s for s in json.loads(source)['finalSurvivors']
                    if {3,18,19}<=set(s) and not {2,17}&set(s))
    require(eligible==doc['canonicalSupports'] and len(eligible)==240,'canonical coverage list')
    counts=Counter(len(s)-3 for s in eligible)
    require({str(k):v for k,v in sorted(counts.items())}==doc['canonicalSupportHistogram'],'support histogram')
    require(doc['completedAlgebra']['fullRank']==18**13,'full rank arithmetic')
    total=sum(v*17**k for k,v in counts.items())
    require(doc['completedAlgebra']['canonicalTotalRank']==total,'canonical rank arithmetic')
    require(all(doc['completedAlgebra']['canonicalRankByActiveSize'][str(k)]==17**k for k in counts),'individual ranks')
    print(json.dumps({'status':'PASS','presentationSHA256':sha256(raw).hexdigest(),
        'normalizedHasseCoefficientChecks':checks,'affineDirections':14,
        'exactDoubleRootDivision':True,'exactTIdentity':True,
        'squarefreeResidueDomainDegree':18,'frobeniusConjugacyChecked':True,
        'canonicalSupportCount':len(eligible),'canonicalHistogram':dict(sorted(counts.items())),
        'fullRank':18**13,'canonicalTotalRank':total,
        'scope':'Coefficient presentation and rank arithmetic replayed; finite-flat proof is prose, final norm unevaluated.'},indent=2))


if __name__=='__main__':
    main()
