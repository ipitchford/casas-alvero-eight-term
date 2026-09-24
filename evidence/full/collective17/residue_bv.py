"""Complete-domain bounded row9 search using bit-vectors, without LP/division.

Each F17 linear congruence is encoded by the alternating hexadecimal digit
sum, because 16=-1 mod17. No integer variables or remainder operator enter
the solver. Finite-field models are independently replayed with FLINT.
"""
import argparse
import json
from math import comb
import subprocess
import sys
import time
from pathlib import Path


def require(ok, why):
    if not ok:
        raise ValueError(why)


def options():
    p = argparse.ArgumentParser()
    p.add_argument('--wall-seconds',type=float,default=55)
    p.add_argument('--timeout-ms',type=int,default=30000)
    p.add_argument('--models',type=int,default=1)
    p.add_argument('--nonprime',action='store_true')
    p.add_argument('--degree10',action='store_true')
    p.add_argument('--subfield5',action='store_true')
    p.add_argument('--old-support-filter',action='store_true')
    p.add_argument('--fixture',action='store_true')
    p.add_argument('--initial-fixture',action='store_true')
    p.add_argument('--worker',action='store_true',help=argparse.SUPPRESS)
    return p.parse_args()


def worker(args):
    import flint
    import z3
    start = time.monotonic()
    require(not (args.subfield5 and args.degree10),'incompatible field domains')
    dim = 5 if args.subfield5 else 10
    q = [-3,-5,-2,0,-3,1] if args.subfield5 else [-8,7,4,-6,1,0,6,0,-1,4,1]
    K = flint.fq_default_ctx(modulus=flint.fmpz_mod_poly_ctx(17)(q),var='z')
    polyctx = flint.fq_default_poly_ctx(K)
    X = polyctx.gen()
    h = X**20-X**17+14*X**2+3*X
    _,factors = h.factor()

    def vector(x):
        a = [int(v) for v in x.to_list()]
        return tuple(a+[0]*(dim-len(a)))

    if not args.subfield5:
        require(all(f.degree()==1 for f,_ in factors),'seed did not split')
    roots = sorted([-f[0]/f[1] for f,_ in factors if f.degree()==1],key=vector)
    count = 8 if args.subfield5 else 18
    require(len(roots)==count and len(set(map(vector,roots)))==count,'root inventory')
    require(all(h(r).is_zero() for r in roots),'seed root replay')
    basis = [K([0]*j+[1]) for j in range(dim)]
    powers = [[r**j for j in range(17)] for r in roots]
    matrix = [[[vector(v*b) for b in basis] for v in row] for row in powers]
    prime = [i for i,r in enumerate(roots) if not any(vector(r)[1:])]
    degree10 = [i for i,r in enumerate(roots) if r**(17**5) != r]
    degree5 = [i for i,r in enumerate(roots) if i not in prime and i not in degree10]
    require((len(prime),len(degree5),len(degree10))==(3,5,0 if args.subfield5 else 10),'Frobenius strata')
    idx = {vector(v):i for i,v in enumerate(roots)}
    zero,one,minus2 = (idx[vector(K(c))] for c in (0,1,-2))
    fixture = {j:zero for j in range(4,17)}
    fixture.update({4:minus2,9:degree5[0],10:one,14:minus2})
    solver = z3.SolverFor('QF_BV')
    solver.set(timeout=args.timeout_ms)
    a = {j:[z3.BitVec(f'a_{j}_{d}',5) for d in range(dim)] for j in range(4,17)}
    choices = {j:z3.BitVec(f'r_{j}',5) for j in range(4,17)}
    for row in a.values():
        solver.add(*[z3.ULE(v,16) for v in row])
    for choice in choices.values():
        solver.add(z3.ULE(choice,count-1))
    cache = {}
    equation_count = 0
    max_width = 0

    def congruence(terms,constant):
        nonlocal equation_count,max_width
        constant %= 17
        maximum = constant+16*sum(c for c,_ in terms)
        width = max(5,maximum.bit_length())
        require(width <= 24,'unexpected sum bound')
        max_width = max(max_width,width)
        summands = []
        if constant:
            summands.append(z3.BitVecVal(constant,width))
        for c,v in terms:
            key=(width,c,v.get_id())
            if key not in cache:
                ext=z3.ZeroExt(width-5,v)
                cache[key]=ext if c==1 else z3.BitVecVal(c,width)*ext
            summands.append(cache[key])
        # Balanced addition reduces expression depth; bounds preclude overflow.
        if not summands:
            return z3.BoolVal(True)
        while len(summands)>1:
            summands=[summands[i]+summands[i+1] if i+1<len(summands) else summands[i]
                      for i in range(0,len(summands),2)]
        value=summands[0]
        chunks=(width+3)//4
        fold=z3.BitVecVal(0,8)
        for k in range(chunks):
            high=min(width-1,4*k+3)
            digit=z3.Extract(high,4*k,value)
            digit=z3.ZeroExt(8-(high-4*k+1),digit)
            fold=fold+digit if k%2==0 else fold-digit
        lo=-15*(chunks//2)
        hi=15*((chunks+1)//2)
        require(-128<lo and hi<128,'signed folded range')
        multiples=[z3.BitVecVal(v % 256,8) for v in range(lo,hi+1) if v%17==0]
        equation_count += 1
        return z3.Or(*[fold==v for v in multiples])

    for j in range(4,17):
        for ri in range(count):
            equations=[]
            for d in range(dim):
                constant=(vector(powers[ri][j])[d]
                    -comb(j,3)*vector(powers[ri][j-3])[d]) % 17
                terms=[(1,a[j][d])]
                for i in range(4,j):
                    for c in range(dim):
                        scalar=comb(j,i)*matrix[ri][j-i][c][d] % 17
                        if scalar:
                            terms.append((scalar,a[i][c]))
                equations.append(congruence(terms,constant))
            solver.add(z3.Implies(choices[j]==ri,z3.And(*equations)))
    weights={j:comb(19-j,2)*(comb(20,j)//17) % 17 for j in range(4,17)}
    for d in range(dim):
        solver.add(congruence([(weights[j],a[j][d]) for j in range(4,17)],-8037 if d==0 else 0))
    if args.nonprime:
        solver.add(z3.Or(*[choices[j]==i for j in choices for i in degree5+degree10]))
    if args.degree10:
        solver.add(z3.Or(*[choices[j]==i for j in choices for i in degree10]))
    support_count=None
    if args.old_support_filter:
        inventory=json.loads((Path(__file__).resolve().parent.parent/'support_frontier/inventory.json').read_text())
        supports=[set(s) for s in inventory['finalSurvivors']
                  if {3,18,19}<=set(s) and not {2,17}&set(s)]
        require(len(supports)==240,'eligible support inventory changed')
        solver.add(z3.Or(*[z3.And(*[(choices[j]!=zero if j in support else choices[j]==zero)
                                    for j in range(4,17)]) for support in supports]))
        support_count=len(supports)
    if args.fixture:
        solver.add(*[choices[j]==fixture[j] for j in choices])
    if args.initial_fixture:
        aa=[K(1),K(0),K(0),K(-1)]
        for j in range(4,17):
            r=roots[fixture[j]]
            aa.append(-sum((K(comb(j,i))*aa[i]*r**(j-i) for i in range(j)),K(0)))
            solver.set_initial_value(choices[j],z3.BitVecVal(fixture[j],5))
            for d,c in enumerate(vector(aa[j])):
                solver.set_initial_value(a[j][d],z3.BitVecVal(c,5))
    built=time.monotonic()-start
    print(json.dumps({'phase':'built','seconds':built,'conditionalCongruences':equation_count,
                      'maxPositiveSumWidth':max_width,'cachedScalarTerms':len(cache)}),file=sys.stderr,flush=True)
    results=[]
    status='model_limit'
    reason=None
    for _ in range(args.models):
        before=time.monotonic()
        answer=solver.check()
        print(json.dumps({'phase':'check','result':str(answer),'seconds':time.monotonic()-before}),file=sys.stderr,flush=True)
        if answer!=z3.sat:
            status=str(answer)
            reason=solver.reason_unknown() if answer==z3.unknown else 'No independent UNSAT certificate exported'
            break
        model=solver.model()
        selected={j:model.eval(choices[j]).as_long() for j in choices}
        aa=[K(1),K(0),K(0),K(-1)]
        for j in range(4,17):
            r=roots[selected[j]]
            v=-sum((K(comb(j,i))*aa[i]*r**(j-i) for i in range(j)),K(0))
            require(vector(v)==tuple(model.eval(c).as_long() for c in a[j]),'model recurrence replay')
            aa.append(v)
        T=K(-8037)+sum((K(weights[j])*aa[j] for j in weights),K(0))
        require(T.is_zero(),'residue obstruction replay')
        point={'choiceIndices':selected,'witnesses':{j:vector(roots[i]) for j,i in selected.items()},
               'coefficients':{j:vector(aa[j]) for j in range(4,17)},
               'usesDegree10Root':any(i in degree10 for i in selected.values()),
               'usesDegree5Root':any(i in degree5 for i in selected.values()),'replay':'PASS'}
        results.append(point)
        solver.add(z3.Or(*[choices[j]!=selected[j] for j in choices]))
    print(json.dumps({'status':status,'reason':reason,'buildSeconds':built,
        'elapsedSeconds':time.monotonic()-start,'solver':'QF_BV; no Int/Mod/URem',
        'scope':'Residue assignments only; incomplete enumeration and no characteristic-zero conclusion.',
        'completeRootDomain':[vector(r) for r in roots],
        'fieldDegree':dim,
        'canonicalOldSupportCount':support_count,
        'domainScope':'All eight F17^5-valued roots only; degree10-root component separate.' if args.subfield5 else 'All eighteen roots in F17^10.',
        'fieldModulusAscending':[v%17 for v in q],
        'assignmentUpperBound':count**13,'models':results},indent=2))


def main():
    args=options()
    if args.worker:
        worker(args)
        return
    command=[sys.executable,__file__,*sys.argv[1:],'--worker']
    start=time.monotonic()
    try:
        r=subprocess.run(command,text=True,capture_output=True,timeout=args.wall_seconds)
    except subprocess.TimeoutExpired as error:
        stderr=error.stderr or ''
        if isinstance(stderr,bytes):
            stderr=stderr.decode(errors='replace')
        print(json.dumps({'status':'external_wall_timeout','elapsedSeconds':time.monotonic()-start,
            'wallSeconds':args.wall_seconds,'progress':stderr[-4000:],
            'scope':'No solver result and no mathematical conclusion.'},indent=2))
        return
    if r.stderr:
        print(r.stderr,file=sys.stderr,end='')
    print(r.stdout,end='')
    raise SystemExit(r.returncode)


if __name__=='__main__':
    main()
