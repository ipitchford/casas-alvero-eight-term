"""Complete bounded first-residue batch, using FLINT extension arithmetic."""
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import time
import flint
import argparse

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--middle-size',type=int,choices=[5])
    parser.add_argument('--directory',type=Path,default=HERE)
    args=parser.parse_args()
    destination=args.directory.resolve();destination.mkdir(parents=True,exist_ok=True)
    active_sizes=[args.middle_size] if args.middle_size else [3,4]
    started=time.monotonic()
    source=(HERE.parent/'elimination/presentation.json').read_bytes()
    presentation=json.loads(source)
    supports=sorted((s for s in presentation['canonicalSupports'] if len(s)-3 in active_sizes),
                    key=lambda s:(len(s),s))
    if len(supports)!=(21 if args.middle_size else 7):
        raise ValueError('wrong batch')
    modulus=[-8,7,4,-6,1,0,6,0,-1,4,1]
    K=flint.fq_default_ctx(modulus=flint.fmpz_mod_poly_ctx(17)(modulus),var='z')
    R=flint.fq_default_poly_ctx(K)
    X=R.gen()
    h=X**20-X**17-3*X**2+3*X
    _, factors=h.factor()
    if any(f.degree()!=1 for f,m in factors):
        raise ValueError('incomplete splitting field')

    def vector(x):
        v=[int(c) for c in x.to_list()]
        return tuple(v+[0]*(10-len(v)))

    roots=sorted((-f[0]/f[1] for f,m in factors if not f[0].is_zero()),key=vector)
    if len(roots)!=17 or len(set(map(vector,roots)))!=17:
        raise ValueError('incorrect nonzero domain')
    vectors=list(map(vector,roots))
    frobenius=[vectors.index(vector(r**17)) for r in roots]
    powers=[[r**i for i in range(17)] for r in roots]
    cases=[]
    for support in supports:
        beginning=time.monotonic()
        active=[j for j in support if 4<=j<=16]
        weights=[comb(19-j,2)*(comb(20,j)//17) % 17 for j in active]
        constants=[[ -powers[r][j]+comb(j,3)*powers[r][j-3]
                     for r in range(17)] for j in active]
        transitions=[[[comb(j,i)*powers[r][j-i] for r in range(17)]
                       for i in active[:k]] for k,j in enumerate(active)]
        survivors=[]
        seen=0
        digest=sha256()

        def visit(k,choices,parameters,total):
            nonlocal seen
            for ri in range(17):
                a=constants[k][ri]
                for i in range(k):
                    a-=transitions[k][i][ri]*parameters[i]
                t=total+weights[k]*a
                mark=choices+[ri]
                if k+1<len(active):
                    visit(k+1,mark,parameters+[a],t)
                else:
                    seen+=1
                    if not args.middle_size:
                        digest.update(bytes(vector(t)))
                    if t.is_zero():
                        survivors.append(mark)

        visit(0,[],[],K(-8037))
        if seen!=17**len(active):
            raise ValueError('incomplete tree')
        survivor_set={tuple(v) for v in survivors}
        orbits=[]
        while survivor_set:
            first=min(survivor_set)
            orbit=[]; v=first
            while v not in orbit:
                if v not in survivor_set:
                    raise ValueError('Frobenius closure failure')
                orbit.append(v)
                v=tuple(frobenius[i] for i in v)
            if v!=first:
                raise ValueError('Frobenius orbit failure')
            survivor_set.difference_update(orbit)
            orbits.append({'representative':list(first),'size':len(orbit)})
        case={'support':support,'active':active,'markingsChecked':seen,
              'residueTStreamSHA256':digest.hexdigest() if not args.middle_size else None,'survivors':survivors,
              'frobeniusOrbits':orbits,'elapsedSeconds':time.monotonic()-beginning}
        cases.append(case)
        print(json.dumps({'active':active,'markings':seen,'survivors':len(survivors),
                          'orbits':len(orbits),'seconds':case['elapsedSeconds']}),flush=True)
    doc={'scope':'Complete residue enumeration for the specified canonical systems; higher-precision lifting separate.',
         'activeSizes':active_sizes,
         'presentationSHA256':sha256(source).hexdigest(),
         'fieldPolynomialAscending':modulus,'nonzeroRoots':vectors,
         'frobeniusPermutation':frobenius,'cases':cases,
         'totalMarkingsChecked':sum(c['markingsChecked'] for c in cases),
         'elapsedSeconds':time.monotonic()-started}
    (destination/'residue-batch.json').write_text(json.dumps(doc,indent=2)+'\n')
    # Plain integer input lets a native replay avoid any JSON dependency.
    items=[10,17,len(cases)]+modulus
    items += [c for r in vectors for c in r]
    for case in cases:
        items += [len(case['active'])]+case['active']
    (destination/'native-input.txt').write_text(' '.join(map(str,items))+'\n')
    print(json.dumps({'complete':True,'totalMarkings':doc['totalMarkingsChecked'],
                      'seconds':doc['elapsedSeconds']}),flush=True)


if __name__=='__main__':
    main()
