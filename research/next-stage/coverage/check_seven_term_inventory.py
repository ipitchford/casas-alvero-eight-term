#!/usr/bin/env python3
"""Independent seven-total-term support enumeration; direct CLO determinants only."""
from itertools import combinations
from math import comb,gcd
import json

P=(2,3,5,7,11,13,17,19)
EXPECTED=sorted([
[2,3,4,10,12,19],[3,4,9,10,12,19],[3,4,5,10,13,19],
[3,4,10,12,15,19],[3,7,9,10,16,19],[3,6,10,16,17,19],
[7,8,10,16,17,19],[10,12,13,16,17,19],[6,10,15,16,17,19],
[9,10,15,16,17,19],[2,4,10,12,18,19],[3,4,10,13,18,19],
[2,4,10,17,18,19],[4,10,16,17,18,19]])

def need(ok,why):
 if not ok:raise ValueError(why)

def determinant(a,p):
 a=[[v%p for v in row] for row in a];out=1
 for k in range(len(a)):
  r=next((r for r in range(k,len(a)) if a[r][k]),None)
  if r is None:return 0
  if r!=k:a[r],a[k]=a[k],a[r];out=-out
  v=a[k][k];out=out*v%p
  for i in range(k+1,len(a)):
   factor=a[i][k]*pow(v,-1,p)%p
   a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[k])]
 return out%p

def clo(S):
 J=[j for j in range(2,19) if j not in S]
 A=[[-1]+[j*comb(j-2,k-2) if k<=j else 0 for k in J] for j in J]
 A.append([-1]+[(-1)**j for j in J])
 return determinant(A,19)

def pair_bad(r,s,p):
 B,D,C=comb(20,r)%p,comb(20,s)%p,comb(20-r,s-r)%p
 if B in (0,1) or D in (0,1):return False
 g=gcd(r,s)
 return (pow(B,s//g,p)*pow(C-1,(s-r)//g,p)*pow(D-C,r//g,p)
         -pow(B-1,r//g,p)*pow(D-1,s//g,p))%p!=0

counts={'linearTermSupports':0,'afterSingleton':0,'afterTwoVisible':0,'afterCLO':0}
survivors=[];massri_redundant=True
for tail in combinations(range(2,19),5):
 S=set((*tail,19));counts['linearTermSupports']+=1
 V=[[j for j in sorted(S) if comb(20,j)%p] for p in P]
 if any(not v or (len(v)==1 and comb(20,v[0])%p!=1) for p,v in zip(P,V)):continue
 counts['afterSingleton']+=1
 if any(len(v)==2 and pair_bad(*v,p) for p,v in zip(P,V)):continue
 counts['afterTwoVisible']+=1
 massri_redundant &= bool(S & {5,10}) and bool(S & {10,15})
 if clo(S):continue
 counts['afterCLO']+=1;survivors.append(sorted(S))
need(counts=={'linearTermSupports':6188,'afterSingleton':586,'afterTwoVisible':348,'afterCLO':14},'Unexpected census counts')
need(sorted(survivors)==EXPECTED,'Incomplete or changed support list')
need(massri_redundant,'Additional filter is not redundant')
need(determinant([[1,2],[3,4]],19)==17,'Determinant sign control')
need(determinant([[1,2],[2,4]],19)==0,'Singular determinant control')
print(json.dumps({'status':'PASS','counts':counts,'survivors':sorted(survivors),
                  'massriFilterApplied':False,'massriConditionsRedundant':True,
                  'scope':'Necessary support restrictions only; no listed support is asserted realizable. '
                          'Uses the published two-visible and CLO determinant criteria; it does not prove them.'},indent=2))
