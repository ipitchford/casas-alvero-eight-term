#!/usr/bin/env python3
"""Independent bounded arithmetic checks for the integrated written proof."""
from pathlib import Path
from math import comb,prod
from itertools import product
import hashlib,json
P=13

def add(a,b,sign=1):
    c=dict(a)
    for e,v in b.items():c[e]=(c.get(e,0)+sign*v)%P
    return {e:v for e,v in c.items() if v}
def mul(a,b,modM=False):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            e=i+j;v=x*y
            if modM:v*=pow(4,e//19,P);e%=19
            c[e]=(c.get(e,0)+v)%P
    return {e:v for e,v in c.items() if v}
def power(a,n,modM=False):
    z={0:1}
    for _ in range(n):z=mul(z,a,modM)
    return z

def residue(J):
    # Direct source matrix, modular Gaussian elimination, no campaign import.
    a=[[-1]+[j*comb(j-2,k-2) if k<=j else 0 for k in J] for j in J]+[[-1]+[(-1)**k for k in J]]
    answer=1;p=19;a=[[x%p for x in r] for r in a]
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];answer=-answer
        v=a[k][k];answer=answer*v%p
        for i in range(k+1,len(a)):
            ratio=a[i][k]*pow(v,-1,p)%p
            for j in range(k,len(a)):a[i][j]=(a[i][j]-ratio*a[k][j])%p
    return answer%p

def main():
    A={9:1,8:-1,0:-1};C={3:-1,2:3,1:-6,0:3}
    R=add(power(A,2),{i+13:v for i,v in power(C,2).items()},-1)
    D={2:4,0:-1};B={2:4,15:-4}
    H={}
    for i,c in R.items():H=add(H,{j:c*v for j,v in mul(power(B,i,True),power(D,19-i,True),True).items()})
    printed={18:5,17:-6,16:-3,15:3,14:-2,13:-6,11:1,10:3,8:-1,7:1,6:-1,5:3,4:6,3:5,2:-4,0:6}
    printed={e:v%P for e,v in printed.items()}
    if H!=printed:raise ValueError('Printed degree18 remainder mismatch')
    H4=sum(v*pow(4,e,P) for e,v in H.items())%P
    if H4!=8 or pow(13,6,19)!=11 or pow(13,9,19)!=18:raise ValueError('Irreducibility scalar check failed')
    if pow(6,19,P)!=7 or pow(7,19,P)!=6:raise ValueError('Deleted-denominator-root check failed')
    if 5*pow(4,2,P)%P!=2 or H[16]!=10:raise ValueError('Leading-polynomial mismatch check failed')
    table={(2,4,5):5,(2,5,16):13,(4,5,18):17,(5,16,18):12,(2,4,10):1,(2,10,16):18,(3,4,10):1,(3,10,16):14,(4,10,17):0,(10,16,17):11,(4,10,18):7,(10,16,18):2,(2,4,15):17,(2,15,16):9,(4,15,18):3,(15,16,18):2}
    expected={tuple(sorted((a,b,c))) for a,b,c in product((4,16),(5,10,15),(2,3,17,18)) if {a,b,c}&{2,9,10,11,18}}
    if expected!=set(table):raise ValueError('Sixteen-support table coverage mismatch')
    for support,want in table.items():
        got=residue([j for j in range(2,19) if j not in support])
        if got!=want:raise ValueError((support,got,want))
    J={1,2,3,5,6,7,13,14,15,16,18};K={2,4,5,6,7,13,14,15,17,18,19}
    if {20-j for j in J}!=K:raise ValueError('Theorem derivative coefficient indexing mismatch')
    visible={j for j in range(21) if comb(20,j)%13}
    if visible-J-{0,20}!={4,17,19}:raise ValueError('Lucas base-support mismatch')
    proof=Path('outputs/casas-alvero-extension/PROOF.md')
    print(json.dumps({'status':'PASS','proofSha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'remainderExactMatch':True,'H4':H4,'denominatorRootChecks':'PASS','irreducibilityScalarChecks':'PASS','sixteenSupportCoverage':'PASS','sixteenDeterminantResidues':'PASS','theoremIndexing':'PASS','base13VisibleSupport':'PASS'},indent=2))
if __name__=='__main__':main()
