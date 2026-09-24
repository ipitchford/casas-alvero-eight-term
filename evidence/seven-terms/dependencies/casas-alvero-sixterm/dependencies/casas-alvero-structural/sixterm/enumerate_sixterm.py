#!/usr/bin/env python3
"""Exact centered degree20 support filter for SIX total terms.
Only stdlib; no import from earlier/frozen research packages. No CAS campaign.
"""
from itertools import combinations
from math import comb
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
N=20;PRIMES=(2,3,5,7,11,13,17,19)
T={4,8,9,10,11,12,17,19}
VISIBLE={p:{m for m in range(2,20) if comb(N,m)%p} for p in PRIMES}

def matrix(J):
    return [[-1]+[j*comb(j-2,k-2) if k<=j else 0 for k in J] for j in J]+[[-1]+[(-1)**j for j in J]]

def bareiss(a):
    a=[r[:] for r in a];sign=1;previous=1
    for k in range(len(a)-1):
        if not a[k][k]:
            pivot=next((i for i in range(k+1,len(a)) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                q,r=divmod(v*a[i][j]-a[i][k]*a[k][j],previous)
                if r:raise ArithmeticError('Bareiss division was not exact')
                a[i][j]=q
            a[i][k]=0
        previous=v
    return sign*a[-1][-1]

def gaussian(a,p):
    a=[[x%p for x in r] for r in a];det=1
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];det=-det
        v=a[k][k];det=det*v%p
        for i in range(k+1,len(a)):
            ratio=a[i][k]*pow(v,-1,p)%p
            for j in range(k,len(a)):a[i][j]=(a[i][j]-ratio*a[k][j])%p
    return det%p

def lucas_set(n,p):
    def digits(k):
        ds=[]
        while k:ds.append(k%p);k//=p
        return ds
    nd=digits(n)
    return {j for j in range(2,n) if all(jd<= (nd[i] if i<len(nd) else 0) for i,jd in enumerate(digits(j)))}

def permitted(S,p):
    visible=S&VISIBLE[p]
    if not visible:return False
    return len(visible)!=1 or comb(N,next(iter(visible)))%p==1

def main():
    for p in PRIMES:
        if VISIBLE[p]!=lucas_set(N,p):raise ValueError('Direct binomial and Lucas digit sets disagree')
    fixture=[list(J) for J in combinations(range(2,11),2) if bareiss(matrix(J))%11==0]
    if fixture!=[[3,8],[5,6],[6,8],[6,9],[7,9]]:raise ValueError('CLO degree12 fixture failed')
    stage={'all':0,'linearTerm':0,'allLucasSingleton':0,'massri':0,'cloDeterminant':0,'newForbiddenMask':0}
    single_prime_pass=Counter();records=[];survivors=[];excluded_by_new=[]
    for raw in combinations(range(2,20),5):
        S=set(raw);stage['all']+=1
        decisions={p:permitted(S,p) for p in PRIMES}
        for p,ok in decisions.items():single_prime_pass[p]+=int(ok)
        if 19 not in S:continue
        stage['linearTerm']+=1
        if not all(decisions.values()):continue
        stage['allLucasSingleton']+=1
        massri=bool(S&{5,10}) and bool(S&{10,15})
        if not massri:continue
        stage['massri']+=1
        J=[j for j in range(2,19) if j not in S];A=matrix(J)
        exact=bareiss(A);res=gaussian(A,19)
        if exact%19!=res:raise ValueError('Independent determinant checks disagree')
        record={'support':raw,'missingIndices':J,'determinant':str(exact),'residueMod19':res,'visibleSupports':{p:sorted(S&VISIBLE[p]) for p in PRIMES},'outsideForbiddenMask':sorted(S-T),'containedInForbiddenMask':S<=T}
        records.append(record)
        if res:continue
        stage['cloDeterminant']+=1
        if S<=T:excluded_by_new.append(raw);continue
        stage['newForbiddenMask']+=1;survivors.append(record)
    grouping={}
    for p in PRIMES:
        groups=defaultdict(list)
        for r in survivors:groups[tuple(r['visibleSupports'][p])].append(r['support'])
        grouping[p]=[{'visibleSupport':mask,'visibleCount':len(mask),'supportCount':len(supports),'supports':supports} for mask,supports in sorted(groups.items(),key=lambda kv:(len(kv[0]),-len(kv[1]),kv[0]))]
    result={'degree':20,'totalTerms':6,'supportSize':5,'primes':PRIMES,'visibleSets':{p:sorted(v) for p,v in VISIBLE.items()},'singlePrimePassCountsAmongAll8568':single_prime_pass,'stageCounts':stage,'massriAddsAfterAllPrimeSingletonFilters':stage['allLucasSingleton']-stage['massri'],'excludedByNewForbiddenMask':excluded_by_new,'survivors':[r['support'] for r in survivors],'survivorRecords':survivors,'visibleSupportGrouping':grouping,'allArithmeticEligibleRecords':records,'publishedDegree12Fixture':fixture,'assurance':'Exact necessary-condition enumeration; no claim that survivors are realizable; no Groebner computations.'}
    dest=Path(__file__).with_name('enumeration.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('survivorRecords','visibleSupportGrouping','allArithmeticEligibleRecords')},indent=2))
if __name__=='__main__':main()
