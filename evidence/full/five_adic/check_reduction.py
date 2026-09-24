"""Exact finite arithmetic for the full degree20 reduction at5, not a lift proof."""
from math import comb
import json

P=5

def require(ok,message):
    if not ok:raise ValueError(message)

def trim(a):
    while a and a[-1]%P==0:a.pop()
    return [c%P for c in a]

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):r[i+j]=(r[i+j]+c*d)%P
    return trim(r)

def power(a,n):
    result=[1]
    for _ in range(n):result=mul(result,a)
    return result

def value(a,x):return sum(c*pow(x,i,P) for i,c in enumerate(a))%P

def hasse(a,k):return trim([comb(i+k,k)*a[i+k]%P for i in range(max(0,len(a)-k))])

def multiplicity(a,r):
    return next(i for i in range(len(a)) if value(hasse(a,i),r))

require([j for j in range(21) if comb(20,j)%P]==[0,5,10,15,20], 'Wrong Lucas support')
cases=[([0,0,4,0,1],{0:10,1:5,4:5}),
       ([0,3,0,1,1],{0:5,1:10,2:5})]
records=[]
for q,expected in cases:
    f=power(q,5)
    require(f==[q[i//5] if i%5==0 else 0 for i in range(21)], 'Frobenius identity failed')
    roots=[x for x in range(P) if not value(f,x)]
    actual={r:multiplicity(f,r) for r in roots}
    require(actual==expected,'Root clusters differ')
    witnesses=[]
    for k in range(1,20):
        found=[r for r in roots if value(hasse(f,k),r)==0]
        require(found,f'No Hasse common root in order {k}')
        witnesses.append(found[0])
    records.append({'quarticAscending':q,'degree20Ascending':f,
                    'rootMultiplicities':actual,'all19HasseWitnesses':witnesses})
require(mul(mul([0,1],power([4,1],2)),[3,1])==cases[1][0], 'Second rooted quartic factorization failed')
require(hasse(cases[0][0],2)==[4,0,1] and hasse(cases[0][0],3)==[0,4], 'Quartic derivative formulas failed')
print(json.dumps({'status':'PASS','scope':'Two complete residue shapes; no characteristic-zero exclusion',
                  'records':records},indent=2))
