"""Independent standard-library checks of saved domains, SAT models, and folds.

This performs no search, calls no SMT solver, and imports no encoder code.
Timeout files are checked as domain records, never as unsatisfiability proofs.
"""
from pathlib import Path
from math import comb
import json

BASE=Path(__file__).resolve().parent


def require(ok,why):
    if not ok:
        raise ValueError(why)


def pgcd(a,b):
    def trim(x):
        while x and x[-1]%17==0:
            x.pop()
        return [v%17 for v in x]
    a,b=trim(a),trim(b)
    while b:
        r=a.copy()
        while len(r)>=len(b):
            v=r[-1]*pow(b[-1],-1,17)%17
            start=len(r)-len(b)
            for i,c in enumerate(b):
                r[start+i]=(r[start+i]-v*c)%17
            r=trim(r)
        a,b=b,r
    return [(c*pow(a[-1],-1,17))%17 for c in a]


class Field:
    def __init__(self,q):
        self.q=q
        self.d=len(q)-1

    def scalar(self,n):
        return (n%17,)+(0,)*(self.d-1)

    def add(self,x,y):
        return tuple((a+b)%17 for a,b in zip(x,y))

    def scale(self,x,c):
        return tuple(a*c%17 for a in x)

    def mul(self,x,y):
        c=[0]*(2*self.d-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y):
                c[i+j]+=a*b
        for k in range(len(c)-1,self.d-1,-1):
            for j in range(self.d):
                c[k-self.d+j]-=c[k]*self.q[j]
        return tuple(v%17 for v in c[:self.d])

    def power(self,x,n):
        out=self.scalar(1)
        while n:
            if n&1:
                out=self.mul(out,x)
            x=self.mul(x,x)
            n//=2
        return out

    def peval(self,coefficients,x):
        out=self.scalar(0)
        for c in reversed(coefficients):
            out=self.add(self.mul(out,x),self.scalar(c))
        return out

    def irreducible(self):
        x=(0,1)+(0,)*(self.d-2)
        proper={5:[1],10:[2,5]}[self.d]
        require(self.power(x,17**self.d)==x,'full Frobenius check')
        for n in proper:
            v=self.add(self.power(x,17**n),self.scale(x,-1))
            require(pgcd(self.q.copy(),list(v))==[1],'proper Frobenius gcd')


def main():
    fold_checks=0
    for width in range(5,16):
        chunks=(width+3)//4
        lo,hi=-15*(chunks//2),15*((chunks+1)//2)
        allowed={m%256 for m in range(lo,hi+1) if m%17==0}
        for n in range(1<<width):
            folded=sum((1 if k%2==0 else -1)*((n>>(4*k))&15) for k in range(chunks))%256
            require((folded in allowed)==(n%17==0),'fold arithmetic mismatch')
            fold_checks+=1
    names=['bv-fixture','bv-nonprime','bv-initial-fixture','bv-subfield5','bv-subfield5-supports']
    fields={}
    records=[]
    for name in names:
        data=json.loads((BASE/f'{name}.json').read_text())
        require(data['status'] in ['model_limit','unknown'],'unexpected search result')
        if data['status']=='unknown':
            require(data['reason']=='timeout' and not data['models'],'timeout scope')
        q=tuple(data['fieldModulusAscending'])
        if q not in fields:
            fields[q]=Field(list(q))
            fields[q].irreducible()
        F=fields[q]
        roots=list(map(tuple,data['completeRootDomain']))
        expected=8 if F.d==5 else 18
        require(len(roots)==len(set(roots))==expected,'root count')
        require(all(len(r)==F.d and all(0<=c<17 for c in r) for r in roots),'root encoding')
        h=[0]*21
        h[20],h[17],h[2],h[1]=1,-1,-3,3
        require(all(F.peval(h,r)==F.scalar(0) for r in roots),'root evaluation')
        require(F.scalar(0) in roots and F.scalar(1) in roots and F.scalar(-2) in roots,'prime roots')
        hp=[i*h[i] for i in range(1,21)]
        require(all(F.peval(hp,r)!=F.scalar(0) for r in roots if r!=F.scalar(1)),'simple roots')
        require(F.peval([comb(i,2)*h[i] for i in range(2,21)],F.scalar(1))==F.scalar(0),'H2 at1')
        require(F.peval([comb(i,3)*h[i] for i in range(3,21)],F.scalar(1))!=F.scalar(0),'multiplicity3')
        prime=[r for r in roots if not any(r[1:])]
        require(len(prime)==3,'prime-field root count')
        degree5=[r for r in roots if r not in prime and F.power(r,17**5)==r]
        require(len(degree5)==5,'degree-five roots')
        # In dimension5, completeness also uses the independently verified
        # irreducibility of the degree10 seed factor (checked below).
        for model in data['models']:
            a=[F.scalar(1),F.scalar(0),F.scalar(0),F.scalar(-1)]
            for j in range(4,17):
                ri=model['choiceIndices'][str(j)]
                require(0<=ri<len(roots),'choice index')
                r=roots[ri]
                require(r==tuple(model['witnesses'][str(j)]),'selected vector')
                value=F.scalar(0)
                for i in range(j):
                    value=F.add(value,F.scale(F.mul(a[i],F.power(r,j-i)),comb(j,i)))
                value=F.scale(value,-1)
                require(value==tuple(model['coefficients'][str(j)]),'triangular recurrence')
                a.append(value)
            T=F.scalar(-8037)
            for j in range(4,17):
                T=F.add(T,F.scale(a[j],comb(19-j,2)*(comb(20,j)//17)))
            require(T==F.scalar(0),'extra residue equation')
            require(any(tuple(v) in degree5 for v in model['witnesses'].values()),'extension-field fixture')
        records.append({'file':name+'.json','status':data['status'],'fieldDegree':F.d,
            'completeDomainSize':expected,'verifiedModels':len(data['models'])})
    require(any(f.d==10 for f in fields.values()),'degree-ten irreducibility missing')
    print(json.dumps({'status':'PASS','exhaustiveFoldChecks':fold_checks,'savedSearchRecords':records,
        'scope':'One known SAT fixture verified. Four timeout records give no mathematical result.'},indent=2))


if __name__=='__main__':
    main()
