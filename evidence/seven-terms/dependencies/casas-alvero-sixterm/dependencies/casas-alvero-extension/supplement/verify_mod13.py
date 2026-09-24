#!/usr/bin/env python3
"""Independent exact F13 identity and properness-hypothesis checker.

First derives all coefficients with FOUR symbolic witnesses from Hasse
monomials over Z; only then normalizes the first witness to 1. No CAS dependency.
A written finite-module argument, supplied separately, is needed to interpret
these exact checks as a characteristic-zero exclusion.
"""
from pathlib import Path
from math import comb
import hashlib,json
P=13
ONE={(0,0,0,0):1}
ROOTS=tuple({tuple(int(j==i) for j in range(4)):1} for i in range(4))

def add(*args):
    out={}
    for a in args:
        for e,c in a.items():out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}
def mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(x+y for x,y in zip(e,f));out[g]=out.get(g,0)+c*d
    return {e:c for e,c in out.items() if c}
def scale(a,c):return {e:c*d for e,d in a.items() if c*d}
def power(a,n):
    one={(0,)*len(next(iter(a))):1};out=one
    for _ in range(n):out=mul(out,a)
    return out

def mod(a):return {e:c%P for e,c in a.items() if c%P}
def normalize_first(a):
    out={}
    for e,c in a.items():out[e[1:]]=out.get(e[1:],0)+c
    return {e:c for e,c in out.items() if c}

def reconstruct():
    support=(4,10,17,19);f={20:ONE};A=[]
    for m,r in zip(support,ROOTS):
        k=20-m
        partial=add(*(scale(mul(c,power(r,d-k)),comb(d,k)) for d,c in f.items() if d>=k))
        a=scale(partial,-1);f[k]=a;A.append(a)
        # Check this Hasse condition immediately after solving its coefficient.
        full=add(*(scale(mul(c,power(r,d-k)),comb(d,k)) for d,c in f.items() if d>=k))
        if full:raise ValueError('Triangular Hasse derivative identity failed')
    # Divide f(r_i) by r_i, valid for the marked characteristic-zero witnesses.
    E=[add(*(mul(c,power(r,d-1)) for d,c in f.items())) for r in ROOTS]
    return [normalize_first(e) for e in E],[normalize_first(a) for a in A]

def parse(path):
    result={'I':[{}, {}, {}],'C':[{}, {}, {}]}
    for line in path.read_text().splitlines():
        kind,index,coefficient,exponents=line.split('|');i=int(index)-1;e=tuple(map(int,exponents.split(',')))
        if kind not in result or not 0<=i<3 or len(e)!=2 or min(e)<0:raise ValueError('Malformed certificate')
        if e in result[kind][i]:raise ValueError('Duplicate certificate term')
        result[kind][i][e]=int(coefficient)%P
    return result

def determinant_mod(matrix):
    a=[[x%P for x in r] for r in matrix];answer=1
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];answer=-answer
        pivot=a[k][k];answer=answer*pivot%P;inv=pow(pivot,-1,P)
        for i in range(k+1,len(a)):
            factor=a[i][k]*inv%P
            for j in range(k,len(a)):a[i][j]=(a[i][j]-factor*a[k][j])%P
    return answer%P

def main():
    root=Path(__file__).resolve().parent;path=root/'mod13-certificate.txt'
    E,A=reconstruct()
    if mod(A[1]):raise ValueError('Second coefficient does not vanish identically modulo13')
    chosen=[]
    for i in (0,2,3):
        reduced=mod(E[i])
        if any(e[0] for e in reduced):raise ValueError('Unexpected surviving u dependence')
        chosen.append({e[1:]:c for e,c in reduced.items()})
    cert=parse(path)
    if chosen!=cert['I']:raise ValueError('Certificate generators mismatch independently derived original equations')
    identity=mod(add(*(mul(c,e) for c,e in zip(cert['C'],chosen))))
    if identity!={(0,0):1}:raise ValueError('F13 identity failed')
    altered=[dict(c) for c in cert['C']];altered[0]=add(altered[0],{(0,0):1})
    if mod(add(*(mul(c,e) for c,e in zip(altered,chosen))))=={(0,0):1}:raise ValueError('Mutation control failed')

    F=add(E[1],scale(E[0],-1));G=add(E[2],scale(E[0],-1));W=add(E[3],scale(E[0],-1))
    if any(e[2] for q in (F,G) for e in q):raise ValueError('F or G still depends on w')
    if max(sum(e) for e in F)!=19 or max(sum(e) for e in G)!=19:raise ValueError('Unexpected degrees')
    topF={e[:2]:c for e,c in F.items() if sum(e)==19}
    topG={e[:2]:c for e,c in G.items() if sum(e)==19}
    if mod(topF)!={(19,0):1,(2,17):4} or mod(topG)!={(0,19):5}:raise ValueError('Leading binary forms differ')
    if max(e[2] for e in W)!=19 or {e:c for e,c in W.items() if e[2]==19}!={(0,0,19):1}:raise ValueError('w equation is not monicdegree19')
    # Degree37 Macaulay map (H18)^2 -> H37, using INTEGER leading forms.
    columns=[]
    for top in (topF,topG):
        for k in range(19):columns.append(mul(top,{(k,18-k):1}))
    matrix=[[column.get((i,37-i),0) for column in columns] for i in range(38)]
    det=determinant_mod(matrix)
    if det==0:raise ValueError('Macaulay matrix not invertible over Z_(13)')
    data={'status':'PASS','support':[4,10,17,19],'prime':13,'certificateSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'certificateTerms':[len(c) for c in cert['C']],'maximumCertificateTotalDegree':max(sum(e) for c in cert['C'] for e in c),'modularIdentity':'C1*E1+C2*Ev+C3*Ew=1','mutationControl':'PASS','coefficientBIdenticallyZeroMod13':True,'leadingFormsMod13':['u^19+4*u^2*v^17','5*v^19'],'macaulayDegree':37,'macaulayMatrixSize':38,'macaulayDeterminantMod13':det,'wRelation':'monicdegree19','finiteModuleGeneratorBound':comb(38,2)*19,'assurance':'Exact arithmetic and transfer hypotheses checked; normalization and finite-module implication are written proofs, not formally verified.'}
    (root/'mod13-verified-equations.json').write_text(json.dumps({'support':[4,10,17,19],'coefficientsAfterNormalization':[{','.join(map(str,e)):str(c) for e,c in q.items()} for q in A],'rootEquationsAfterNormalization':[{','.join(map(str,e)):str(c) for e,c in q.items()} for q in E]},indent=2)+'\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
