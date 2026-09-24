#!/usr/bin/env python3
"""Portable exact audit of the last degree-20 four-term support certificate.

Only Python's standard library is used. This checks a Nullstellensatz identity
in F_31[u,v], not a black-box Groebner result. It independently reconstructs the
three defining equations from the Hasse derivative definition. The separate
finite-module lemma is required for the characteristic-zero conclusion.
"""
from pathlib import Path
from math import comb
import hashlib, json, sys

P=31
ONE={(0,0):1}
U={(1,0):1}
V={(0,1):1}

# Integer arithmetic first, so binomial constants and the monic leading
# coefficient needed by the lifting lemma are not inferred from F_31.
def add(*args):
    out={}
    for a in args:
        for k,v in a.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}

def scale(a,s): return {k:v*s for k,v in a.items() if v*s}

def mul(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            e=(i+k,j+l); out[e]=out.get(e,0)+x*y
    return {k:v for k,v in out.items() if v}

def power(a,n):
    out=ONE
    for _ in range(n): out=mul(out,a)
    return out

def mod(a): return {k:v%P for k,v in a.items() if v%P}

def equations():
    ms=(5,16,19); roots=(ONE,U,V)
    f={20:ONE}; coeffs=[]
    for m,r in zip(ms,roots):
        order=20-m
        evaluated={}
        for degree,coefficient in f.items():
            if degree>=order:
                evaluated=add(evaluated,scale(mul(coefficient,power(r,degree-order)),comb(degree,order)))
        a=scale(evaluated,-1); f[order]=a; coeffs.append(a)
    # f(X)=X*P(X), and the witnesses are nonzero over characteristic zero.
    E=[add(*(mul(c,power(r,k-1)) for k,c in f.items())) for r in roots]
    return E,coeffs

def parse(path):
    out={'I':[{}, {}, {}],'C':[{}, {}, {}]}
    for line in path.read_text().splitlines():
        kind,index,coefficient,exp=line.split('|')
        i=int(index)-1; e=tuple(map(int,exp.split(','))); c=int(coefficient)
        if kind not in out or not 0<=i<3 or len(e)!=2 or min(e)<0:
            raise ValueError('Malformed certificate term')
        if e in out[kind][i]: raise ValueError('Duplicate term')
        out[kind][i][e]=c%P
    return out

def verify(path):
    E,A=equations()
    cert=parse(path)
    if [mod(e) for e in E]!=cert['I']:
        raise ValueError('Exported generators do not match independently reconstructed Hasse equations')
    total=mod(add(*(mul(c,e) for c,e in zip(cert['C'],E))))
    if total!=ONE: raise ValueError('Exact F31 certificate identity failed')
    altered=[dict(c) for c in cert['C']]
    altered[0]=add(altered[0],ONE)
    if mod(add(*(mul(c,e) for c,e in zip(altered,E))))==ONE:
        raise ValueError('Certificate corruption control failed')
    # Exact hypotheses of finite generation, checked on the unreduced equations.
    Fu=add(E[1],scale(E[0],-1))
    Fv=add(E[2],scale(E[0],-1))
    leading=1-comb(20,16)
    if any(j for i,j in Fu) or max(i for i,j in Fu)!=19 or Fu.get((19,0))!=leading:
        raise ValueError('Univariate-u integrality relation failed')
    if leading%P==0: raise ValueError('Chosen prime is bad for the leading coefficient')
    if max(j for i,j in Fv)!=19 or Fv.get((0,19))!=1:
        raise ValueError('Monic-v integrality relation failed')
    if any(j==19 and i!=0 for i,j in Fv): raise ValueError('Nonconstant leading v coefficient')
    return {
      'status':'PASS','support':[5,16,19],'prime':P,
      'certificateSha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'identity':'C1*E1+C2*E2+C3*E3 = 1 in F31[u,v]',
      'generatorTermCounts':[len(mod(e)) for e in E],
      'certificateTermCounts':[len(c) for c in cert['C']],
      'maxCertificateTotalDegree':max(sum(k) for c in cert['C'] for k in c),
      'mutationControl':'PASS',
      'integrality':{'uDegree':19,'uLeadingInteger':leading,'uLeadingResidue':leading%P,'vDegree':19,'vLeadingCoefficient':1,'moduleGeneratorBound':361},
      'assurance':'Exact finite certificate and integrality hypotheses checked; normalization and Nakayama argument are written mathematical proofs, not formal verification.'
    }

if __name__=='__main__':
    if len(sys.argv)>2:
        raise SystemExit('Usage: verify_mod31.py [certificate.txt]')
    path=Path(sys.argv[1]) if len(sys.argv)==2 else Path(__file__).resolve().parent/'mod31-m-5-16-19.certificate.txt'
    print(json.dumps(verify(path),indent=2))
