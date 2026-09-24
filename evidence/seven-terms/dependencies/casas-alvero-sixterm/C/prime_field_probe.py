"""Bounded search for prime-field marked-root CA examples in family C.

This is a witness search only. Its absence results are not exclusions over
algebraic closures. Highest nonzero coefficient's Hasse witness is scaled to 1.
"""
from math import comb
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

def evaluate(terms, x, p, order=0):
    return sum(a*comb(n,order)*pow(x,n-order,p)
               for n,a in terms.items() if n>=order)%p

def witnesses(terms,p):
    roots=[x for x in range(p) if evaluate(terms,x,p)==0]
    answer={}
    for k in (16,15,3,1):
        ws=[x for x in roots if evaluate(terms,x,p,k)==0]
        if not ws:return None
        answer[str(k)]=ws
    return answer

results=[]
for p in (11,13):
    examples=[]; count=0
    for top in (16,15,3,1):
        coefficient=-comb(20,top)%p
        if not coefficient:continue
        if top==16:
            pairs=[(b,c) for b in range(p) for c in range(p)]
        elif top==15:
            pairs=[(coefficient,c) for c in range(p)]
        else:
            pairs=[(0,coefficient if top==3 else 0)]
        for b,c in pairs:
            a=coefficient if top==16 else 0
            d=(-1-a-b-c)%p
            if top==1 and d!=coefficient:continue
            terms={20:1,16:a,15:b,3:c,1:d}
            count+=1
            ws=witnesses(terms,p)
            if ws:examples.append({'coefficients':terms,'witnesses':ws})
    results.append({'p':p,'normalized_candidates':count,'examples':examples})
record={'scope':'Prime-field witnesses only; no extension-field exclusion',
        'family':'x20+a*x16+b*x15+c*x3+d*x','results':results}
(ROOT/'prime-field-probe.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
