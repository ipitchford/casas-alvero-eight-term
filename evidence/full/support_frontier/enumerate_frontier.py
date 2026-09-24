"""All centered degree-20 supports under the currently certified criteria.

No CAS, no publication, no inference that surviving supports are realizable.
Use --write to save the inventory. Default mode is read-only. --direct checks
every fast CLO determinant with an independent modular Gaussian elimination.
"""
from collections import Counter,defaultdict
from itertools import combinations
from math import comb,gcd
from pathlib import Path
import argparse
import hashlib
import json

N=20
PRIMES=(2,3,5,7,11,13,17,19)
INDICES=tuple(range(2,20))


def bit(j):return 1<<(j-2)


def mask(indices):return sum(bit(j) for j in indices)


def support(m):return [j for j in INDICES if m&bit(j)]


VISIBLE={p:mask(j for j in INDICES if comb(N,j)%p) for p in PRIMES}
UNIT={p:mask(j for j in INDICES if comb(N,j)%p==1) for p in PRIMES}
CLOSED_MASKS={
    'earlier13':mask([4,8,9,10,11,12,17,19]),
    'B13':mask([3,8,9,10,11,12,16,17,19]),
    'A_char0':mask([3,4,10,18,19]),
}
C_EXACT=mask([4,5,10,17,19])


def pair_excludes(r,s,p):
    B,D,C=comb(20,r)%p,comb(20,s)%p,comb(20-r,s-r)%p
    if B in (0,1) or D in (0,1):return False
    g=gcd(r,s)
    residual=(pow(B,s//g,p)*pow(C-1,(s-r)//g,p)*pow(D-C,r//g,p)
              -pow(B-1,r//g,p)*pow(D-1,s//g,p))%p
    source=(pow(D,r//g,p)*pow(B-comb(s,r),(r//g),p)*pow(B-D*comb(s,r),(s-r)//g,p)
            -(-1)**((s-r)//g)*pow(D-1,s//g,p)*pow(B-1,r//g,p))%p
    if source!=(-1)**((s-r)//g)*residual%p:raise ValueError('Old pair source formula mismatch')
    return residual!=0


PAIR_BAD={p:{mask(pair) for pair in combinations(support(VISIBLE[p]),2) if pair_excludes(*pair,p)} for p in PRIMES}
BINOM={(j,k):comb(j-2,k-2)%19 for j in range(2,19) for k in range(2,j+1)}
INVERSE={j:pow(j,-1,19) for j in range(2,19)}


def clo_fast(J):
    # Schur complement of the invertible lower triangular block.
    z=[]
    determinant=1
    for i,j in enumerate(J):
        z.append((INVERSE[j]-sum(BINOM[j,k]*z[t] for t,k in enumerate(J[:i])))%19)
        determinant=determinant*j%19
    return ((-1)**len(J)*determinant*(sum((-1)**j*x for j,x in zip(J,z,strict=True))-1))%19


def clo_direct(J,p=19):
    a=[[-1]+[j*comb(j-2,k-2) if k<=j else 0 for k in J] for j in J]
    a.append([-1]+[(-1)**j for j in J])
    a=[[x%p for x in row] for row in a]
    det=1
    for k in range(len(a)):
        r=next((r for r in range(k,len(a)) if a[r][k]),None)
        if r is None:return 0
        if r!=k:a[k],a[r]=a[r],a[k];det=-det
        pivot=a[k][k];det=det*pivot%p
        inv=pow(pivot,-1,p)
        for r in range(k+1,len(a)):
            c=a[r][k]*inv%p
            for j in range(k,len(a)):a[r][j]=(a[r][j]-c*a[k][j])%p
    return det%p


def lucas(n,m,p):
    while n or m:
        if m%p>n%p:return False
        n//=p;m//=p
    return True


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--direct',action='store_true')
    args=parser.parse_args()
    for p in PRIMES:
        if support(VISIBLE[p])!=[j for j in INDICES if lucas(N,j,p)]:
            raise ValueError('Lucas and integer-binomial visibility disagree')
    fixture=[list(J) for J in combinations(range(2,11),2) if clo_direct(J,11)==0]
    if fixture!=[[3,8],[5,6],[6,8],[6,9],[7,9]]:raise ValueError('CLO published fixture failed')
    stages=['all','linearTerm','lucasSingleton','oldTwoVisible','massri','twoMissingMeanDerivatives','cloDeterminant','earlier13','B13','A_char0','C_exact']
    counts={stage:[0]*19 for stage in stages}
    for k in range(1,19):counts['all'][k]=comb(18,k)
    rejected_masks={name:[] for name in CLOSED_MASKS}
    rejected_masks['C_exact']=[]
    survivors=[]
    direct_checks=0
    old_survivors=[]
    for lower in range(1<<17):
        S=lower|bit(19)
        k=S.bit_count()
        counts['linearTerm'][k]+=1
        vsets=[S&VISIBLE[p] for p in PRIMES]
        if any(v==0 or (v.bit_count()==1 and not v&UNIT[p]) for p,v in zip(PRIMES,vsets,strict=True)):continue
        counts['lucasSingleton'][k]+=1
        if any(v in PAIR_BAD[p] for p,v in zip(PRIMES,vsets,strict=True)):continue
        counts['oldTwoVisible'][k]+=1
        if not (S&mask([5,10]) and S&mask([10,15])):continue
        counts['massri'][k]+=1
        J=[j for j in range(2,19) if not S&bit(j)]
        if len(J)<2:continue
        counts['twoMissingMeanDerivatives'][k]+=1
        residue=clo_fast(J)
        if args.direct or residue==0 or S%101==0:
            if clo_direct(J)!=residue:raise ValueError(f'CLO determinant mismatch {S}')
            direct_checks+=1
        if residue:continue
        counts['cloDeterminant'][k]+=1
        old_survivors.append(S)
        stop=False
        for name,T in CLOSED_MASKS.items():
            if S&~T==0:
                rejected_masks[name].append(S);stop=True;break
            counts[name][k]+=1
        if stop:continue
        if S==C_EXACT:
            rejected_masks['C_exact'].append(S);continue
        counts['C_exact'][k]+=1
        survivors.append(S)
    grouping={}
    for p in PRIMES:
        groups=defaultdict(list)
        for S in survivors:groups[S&VISIBLE[p]].append(S)
        maximal=[]
        for M in sorted(groups,key=lambda m:(-m.bit_count(),m)):
            if not any(M&~T==0 for T in maximal):maximal.append(M)
        grouping[str(p)]={
            'visibleDeficiencies':support(VISIBLE[p]),'invisibleDeficiencies':support(mask(INDICES)^VISIBLE[p]),
            'visibleMaskCount':len(groups),'maximalModelCount':len(maximal),
            'maximalModels':[{'visibleDeficiencies':support(M),'polynomialExponents':[20]+[20-j for j in support(M)],
                              'coveredSurvivorCount':sum(len(v) for K,v in groups.items() if K&~M==0),
                              'binomialCADegenerations':support(M&UNIT[p])} for M in maximal],
            'visibleSizeHistogram':dict(sorted(Counter((S&VISIBLE[p]).bit_count() for S in survivors).items())),
            'groups':[{'visibleDeficiencies':support(M),'supportCount':len(v),
                       'termCountHistogram':dict(sorted(Counter(S.bit_count()+1 for S in v).items())),
                       'binomialCADegenerations':support(M&UNIT[p])} for M,v in sorted(groups.items())],
        }
    table=[{'nonleadingTerms':k,'totalTerms':k+1,**{stage:counts[stage][k] for stage in stages}} for k in range(1,19)]
    inventory={'degree':20,'convention':'S subset{2,...,19}; coefficient at m multiplies X^(20-m); leading term counted separately',
               'criterionOrder':stages,'countsByTermCount':table,'oldSurvivorCount':len(old_survivors),
               'finalSurvivorCount':len(survivors),'finalSurvivors':[support(S) for S in survivors],
               'newCriterionExclusions':{name:[support(S) for S in sets] for name,sets in rejected_masks.items()},
               'closedMasks':{name:support(T) for name,T in CLOSED_MASKS.items()},'CExactSupport':support(C_EXACT),
               'primeGroups':grouping,'publishedDegree12Fixture':fixture,
               'scope':'Necessary-condition coverage only; no surviving support is asserted realizable; not a full CA solution.'}
    canonical=json.dumps(inventory,sort_keys=True,separators=(',',':')).encode()
    summary={k:inventory[k] for k in ['degree','criterionOrder','countsByTermCount','oldSurvivorCount','finalSurvivorCount','newCriterionExclusions']}
    summary['primeModelSummary']={p:{k:v[k] for k in ['visibleMaskCount','maximalModelCount','visibleSizeHistogram','maximalModels']} for p,v in grouping.items()}
    summary['inventorySha256']=hashlib.sha256(canonical).hexdigest()
    if args.write:
        base=Path(__file__).resolve().parent
        (base/'inventory.json').write_bytes(canonical+b'\n')
        (base/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({'summary':summary,'directDeterminantChecks':direct_checks,'allEligibleDirectlyChecked':args.direct},indent=2))


if __name__=='__main__':main()
