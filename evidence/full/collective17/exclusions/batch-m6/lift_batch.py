"""Lift every residual Frobenius orbit through at most six 17-adic digits."""
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import time
import argparse

HERE=Path(__file__).resolve().parent
D=10
P=17
REL=[8,-7,-4,6,-1,0,-6,0,1,-4]


def need(ok,why):
    if not ok: raise ValueError(why)


class Ring:
    def __init__(self,modulus):
        self.modulus=modulus
        self.zero=[0]*D
        self.one=[1]+[0]*(D-1)

    def scalar(self,c): return [c%self.modulus]+[0]*(D-1)
    def add(self,a,b): return [(x+y)%self.modulus for x,y in zip(a,b)]
    def scale(self,a,c): return [(x*c)%self.modulus for x in a]

    def mul(self,a,b):
        c=[0]*(2*D-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        for k in range(2*D-2,D-1,-1):
            v=c[k]%self.modulus
            for j,w in enumerate(REL): c[k-D+j]+=v*w
        return [x%self.modulus for x in c[:D]]

    def power(self,a,n):
        out=self.one
        while n:
            if n&1: out=self.mul(out,a)
            a=self.mul(a,a); n//=2
        return out

    def evaluate(self,f,x,derivative=0):
        out=self.zero
        for i in range(len(f)-1,derivative-1,-1):
            out=self.add(self.mul(out,x),self.scale(f[i],comb(i,derivative)))
        return out


def parameters(r,active,mark,roots):
    a={}
    for j,ri in zip(active,mark):
        x=roots[ri]
        v=r.add(r.scale(r.power(x,j),-1),r.scale(r.power(x,j-3),comb(j,3)))
        for i,ai in a.items():
            v=r.add(v,r.scale(r.mul(ai,r.power(x,j-i)),-comb(j,i)))
        a[j]=v
    return a


def affine(r,v,a):
    out=r.scalar(v[0])
    for j,aj in a.items(): out=r.add(out,r.scale(aj,v[j-3]))
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--directory',type=Path,default=HERE)
    args=parser.parse_args();destination=args.directory.resolve()
    start=time.monotonic()
    residue_raw=(destination/'residue-batch.json').read_bytes()
    residue=json.loads(residue_raw)
    presentation=json.loads((HERE.parents[1]/'elimination/presentation.json').read_text())
    field=Ring(P)
    q_template=presentation['g_divided_by_X']
    cases=[]
    for case in residue['cases']:
        active=case['active']; records=[]
        for orbit in case['frobeniusOrbits']:
            mark=orbit['representative']
            selected=sorted(set(mark))
            roots={i:residue['nonzeroRoots'][i].copy() for i in selected}
            a=parameters(field,active,mark,roots)
            q=[affine(field,v,a) for v in q_template]
            need(affine(field,presentation['T'],a)==field.zero,'nonzero first obstruction')
            diagonal={i:field.evaluate(q,roots[i],1) for i in selected}
            inverse={i:field.power(v,17**10-2) for i,v in diagonal.items()}
            for i in selected:
                need(field.mul(diagonal[i],inverse[i])==field.one,'singular square system')
                need(field.evaluate(q,roots[i])==field.zero,'initial root invalid')
            rec={'representative':mark,'orbitSize':orbit['size'],'distinctRootIndices':selected,
                 'jacobianDiagonalMod17':diagonal,'residueParameters':a,'steps':[]}
            for precision in range(2,7):
                mod=P**precision; lower=P**(precision-1); ring=Ring(mod)
                a=parameters(ring,active,mark,roots)
                q=[affine(ring,v,a) for v in q_template]
                updates={}
                for i in selected:
                    error=ring.evaluate(q,roots[i])
                    need(all(v%lower==0 for v in error),'previous precision lost')
                    delta=field.scale(field.mul([v//lower for v in error],inverse[i]),-1)
                    updates[i]=[(x+lower*d)%mod for x,d in zip(roots[i],delta)]
                roots=updates
                a=parameters(ring,active,mark,roots)
                q=[affine(ring,v,a) for v in q_template]
                need(all(ring.evaluate(q,roots[i])==ring.zero for i in selected),'new precision failure')
                t=affine(ring,presentation['T'],a)
                rec['steps'].append({'precision':precision,'rootCoordinates':roots,
                                     'parameters':a,'T':t})
                if any(t):
                    valuation=0
                    while all(v%P**(valuation+1)==0 for v in t): valuation+=1
                    rec['status']='EXCLUDED'
                    rec['valuationOfT']=valuation
                    rec['firstNonzeroTDigit']=[v//P**valuation%P for v in t]
                    break
            else:
                rec['status']='UNRESOLVED_THROUGH_PRECISION_6'
            records.append(rec)
            print(json.dumps({'active':active,'representative':mark,'orbit':orbit['size'],
                              'status':rec['status'],'T':rec['steps'][-1]['T']}),flush=True)
        cases.append({'active':active,'support':case['support'],'orbits':records,
                      'status':'EXCLUDED' if all(r['status']=='EXCLUDED' for r in records)
                                           else 'RESIDUAL_ORBITS'})
    doc={'scope':'All first-residue survivors of the specified complete canonical batch.',
         'residueCertificateSHA256':sha256(residue_raw).hexdigest(),
         'unramifiedPolynomialAscending':[-8,7,4,-6,1,0,6,0,-1,4,1],
         'squareSystem':'q_u(r)=0 for distinct marked roots, q=f/[X*(X-1)^2]; normalized derivatives determine active u recursively.',
         'cases':cases,'elapsedSeconds':time.monotonic()-start}
    (destination/'lift-batch.json').write_text(json.dumps(doc,indent=2)+'\n')
    print(json.dumps({'seconds':doc['elapsedSeconds'],'caseStatuses':[c['status'] for c in cases]}),flush=True)


if __name__=='__main__': main()
