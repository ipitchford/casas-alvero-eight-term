#!/usr/bin/env python3
"""Old-criteria-first baseline and reusable finite-field reduction groups."""
from itertools import combinations
from pathlib import Path
from math import comb
import json
from enumerate_sixterm import PRIMES,VISIBLE,T,permitted,matrix,bareiss,gaussian
from apply_two_visible import old_pair_test
ROOT=Path(__file__).resolve().parent

def all_old_tests(S):
    tests=[]
    for p in PRIMES:
        visible=sorted(S&VISIBLE[p])
        if len(visible)==2:tests.append(old_pair_test(20,*visible,p))
    return tests

def baseline(size):
    counts={'all':0,'allLucasSingleton':0,'oldTwoVisible':0,'massri':0,'cloDeterminant':0,'newCharacteristic13Mask':0};pre=[];post=[];records=[]
    for raw in combinations(range(2,20),size):
        S=set(raw);counts['all']+=1
        if not all(permitted(S,p) for p in PRIMES):continue
        counts['allLucasSingleton']+=1
        pair=all_old_tests(S)
        if any(t['excludes'] for t in pair):continue
        counts['oldTwoVisible']+=1
        if not(S&{5,10} and S&{10,15}):continue
        counts['massri']+=1
        J=[j for j in range(2,19) if j not in S];A=matrix(J);exact=bareiss(A);mod=gaussian(A,19)
        if exact%19!=mod:raise ValueError('Determinants disagree')
        if mod:continue
        counts['cloDeterminant']+=1;pre.append(raw)
        excluded=S<=T
        records.append({'support':raw,'oldPairTests':pair,'exactCloDeterminant':str(exact),'newMaskExcluded':excluded})
        if excluded:continue
        counts['newCharacteristic13Mask']+=1;post.append(raw)
    return {'lowerTermCount':size,'totalTermCount':size+1,'counts':counts,'oldOnlySurvivors':pre,'afterNewMask':post,'records':records}

def main():
    # Exhaustively validate the two formula indexings for every pair and prime.
    for r,s in combinations(range(2,20),2):
        for p in PRIMES:old_pair_test(20,r,s,p)
    bases=[baseline(4),baseline(5)]
    groups=[]
    for S in bases[1]['afterNewMask']:
        rec={'support':S,'polynomialExponents':[20]+[20-m for m in S],'primeModels':[]}
        for p in PRIMES:
            visible=sorted(set(S)&VISIBLE[p]);unit_indices=[m for m in visible if comb(20,m)%p==1]
            rec['primeModels'].append({'prime':p,'visibleDeficiencies':visible,'visibleExponents':[20-m for m in visible],'lowerCoefficientCount':len(visible),'binomialCaDegenerationIndex':unit_indices[0] if unit_indices else None,'closedMaskExclusionPossible':not unit_indices})
        groups.append(rec)
    result={'oldCriteria':'Lucas/singleton plus deFrutos2013 Prop3.5.5 (with both binomial residues !=1), Massri pair restrictions, CLO determinant','formulaCrossChecks':comb(18,2)*len(PRIMES),'baselines':bases,'survivorArithmeticModels':groups,'warning':'A finite-field binomial CA degeneration makes exclusion of the entire closed reduction mask impossible at that prime; it does not prove the characteristic-zero family exists.'}
    (ROOT/'old-baseline-and-groups.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'baselines':[{k:v for k,v in b.items() if k!='records'} for b in bases],'remainingSupportCount':len(groups),'formulaCrossChecks':result['formulaCrossChecks']},indent=2))
if __name__=='__main__':main()
