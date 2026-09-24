#!/usr/bin/env python3
"""Independent standard-library audit of the row-4 support {4,10,12}.

The producer modules are not imported.  The residue root set is reconstructed
by exhaustive evaluation in F_17^4, then its full factorization is checked.
Newton Jacobians and critical derivatives are computed rather than supplied.
"""
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

P = 17
ACTIVE = (4, 10, 12)
MODULUS = [2, 0, 4, 3, 1]
HERE = Path(__file__).resolve().parent
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def require(ok, why):
    if not ok:
        raise ArithmeticError(why)


def add(a, b):
    return tuple((a[i]+b[i]) % P for i in range(4))


def scale(a, c):
    return tuple(x*c % P for x in a)


def mul(a, b):
    c = [0]*7
    for i in range(4):
        for j in range(4):
            c[i+j] += a[i]*b[j]
    for k in range(6, 3, -1):
        v = c[k]
        c[k-4] -= 2*v
        c[k-2] -= 4*v
        c[k-1] -= 3*v
    return tuple(x % P for x in c[:4])


def fpow(a, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def ptr(a):
    a = [x % P for x in a]
    while len(a)>1 and a[-1] == 0:
        a.pop()
    return a


def prem(a, b):
    a, b = ptr(a), ptr(b)
    while a != [0] and len(a)>=len(b):
        c, s = a[-1]*pow(b[-1], -1, P) % P, len(a)-len(b)
        for i, x in enumerate(b):
            a[i+s] = (a[i+s]-c*x) % P
        a = ptr(a)
    return a


def pmul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return ptr(out)


def ppow(a, n, modulus):
    out = [1]
    while n:
        if n & 1:
            out = prem(pmul(out, a), modulus)
        a = prem(pmul(a, a), modulus)
        n //= 2
    return out


def pgcd(a, b):
    while ptr(b) != [0]:
        a, b = b, prem(a, b)
    return ptr([x*pow(a[-1], -1, P) for x in a])


def field_and_roots():
    x = [0, 1]
    p2 = ppow(x, P**2, MODULUS)
    p2 += [0]*max(0, 2-len(p2))
    p2[1] -= 1
    require(pgcd(MODULUS, p2) == [1], 'quartic has a factor of degree 1 or 2')
    require(ppow(x, P**4, MODULUS) == x, 'quartic Frobenius irreducibility condition')
    roots = []
    for r in product(range(P), repeat=4):
        r2 = mul(r, r)
        r4 = mul(r2, r2)
        r8 = mul(r4, r4)
        r16 = mul(r8, r8)
        r18 = mul(r16, r2)
        r20 = mul(r18, r2)
        if add(add(r20, scale(r18, -3)), add(scale(r2, 11), scale(r, 8))) == ZERO:
            roots.append(r)
    doubles = [r for r in roots if add(add(mul(r,r),scale(r,3)),scale(ONE,3)) == ZERO]
    require(len(roots) == 18 and len(doubles) == 2, 'complete residue root census')
    # A degree-20 product identity certifies completeness over the algebraic closure.
    factors = [ONE]
    for r in roots:
        for _ in range(2 if r in doubles else 1):
            out = [ZERO]*(len(factors)+1)
            for k, c in enumerate(factors):
                out[k] = add(out[k], mul(c, scale(r,-1)))
                out[k+1] = add(out[k+1], c)
            factors = out
    h = [ZERO]*21
    h[20], h[18], h[2], h[1] = ONE, scale(ONE,-3), scale(ONE,11), scale(ONE,8)
    require(factors == h, 'full residue factorization')
    require(ZERO in roots and ONE in roots and (6,0,0,0) in roots, 'fixed simple roots')
    return roots, doubles


def ordinary_family(u, s):
    a = [0]*21
    a[0], a[2] = 1, -1
    for j,v in u.items():
        a[j] = v
    a[18] = -sum(comb(18,i)*a[i]*s**(18-i) for i in range(18))
    f = [0]*21
    for i in range(19):
        f[20-i] = comb(20,i)*a[i]
    f[1] = -sum(f[2:])
    return f


def evaluate(f, x, modulus=None, order=0):
    out = 0
    for i in range(len(f)-1, order-1, -1):
        out = out*x + comb(i,order)*f[i]
        if modulus is not None:
            out %= modulus
    return out


def qadd(a,b,m=None):
    c=(a[0]+b[0],a[1]+b[1])
    return c if m is None else tuple(x % m for x in c)


def qmul(a,b,m=None):
    c=(a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0]-3*a[1]*b[1])
    return c if m is None else tuple(x % m for x in c)


def qeval(f,x,m=None,order=0):
    out=(0,0)
    for i in range(len(f)-1,order-1,-1):
        out=qadd(qmul(out,x,m),(comb(i,order)*f[i],0),m)
    return out


def ell_coefficients():
    base = ordinary_family({},6)
    directions = [base]
    for j in range(4,17):
        unit = ordinary_family({j:1},6)
        directions.append([a-b for a,b in zip(unit,base)])
    coefficients = []
    for f in directions:
        phi, value = evaluate(f,6), qeval(f,(0,1))
        require(phi % P == 0 and all(x % P == 0 for x in value),
                'coefficientwise divisibility before evaluation of u')
        require(all(x % P == 0 for x in qeval(f,(0,1),order=1)),
                'critical displacement has coefficientwise order at least 17')
        sigma = -(phi//P)*pow(9,-1,P) % P
        coefficients.append(((value[0]//P+3*sigma)%P,(value[1]//P+4*sigma)%P))
    # Compute the two implicit derivatives from the residue polynomial itself.
    h=[0]*21
    h[20],h[18],h[2],h[1]=1,-3,11,8
    require(evaluate(h,6,P,order=1)==5, 'argument derivative at s')
    partial_s_at_6=(6-6**2)%P
    require((evaluate(h,6,P,order=1)+partial_s_at_6)%P==9,'total s derivative')
    require(qeval(h,(0,1),P,order=2)==(3,0),'critical ordinary second derivative is 6')
    return coefficients


def census(roots,doubles,ell):
    domain=[r for r in roots if r!=ZERO]
    require(len(domain)==17,'active nonzero witness domain')
    powers={r:[fpow(r,k) for k in range(13)] for r in domain}
    weights={alpha:[add(scale(ONE,a),scale(alpha,b)) for a,b in ell] for alpha in doubles}
    survivors=[]
    tested=0
    for witnesses in product(domain,repeat=3):
        u={}
        for j,r in zip(ACTIVE,witnesses):
            rp=powers[r]
            value=add(scale(rp[j],-1),scale(rp[j-2],comb(j,2)))
            for i in ACTIVE:
                if i<j:
                    value=add(value,scale(mul(u[i],rp[j-i]),-comb(j,i)))
            u[j]=value
        for alpha in doubles:
            tested+=1
            value=weights[alpha][0]
            for j in ACTIVE:
                value=add(value,mul(weights[alpha][j-3],u[j]))
            if value==ZERO:
                survivors.append({'alpha':list(alpha),'witnesses':[list(r) for r in witnesses],
                                  'u':{str(j):list(u[j]) for j in ACTIVE}})
    require(tested==2*17**3,'orientation census size')
    require(len(survivors)==2,'exactly two oriented survivors')
    for s in survivors:
        require(s['witnesses']==[[10,0,0,0],[1,0,0,0],[6,0,0,0]],'surviving simple witness classes')
        require(s['u']=={'4':[1,0,0,0],'10':[4,0,0,0],'12':[9,0,0,0]},'surviving coefficient residues')
    return domain,survivors,tested


def lift_data(t,s,m):
    a=[0]*21
    a[0],a[2]=1,-1
    for j,w in ((4,t),(10,1),(12,s),(18,s)):
        a[j]=-sum(comb(j,i)*a[i]*pow(w,j-i,m) for i in range(j))%m
    f=[0]*21
    for i in range(19):
        f[20-i]=comb(20,i)*a[i]%m
    f[1]=-sum(f[2:])%m
    return f,a


def equations(t,s,m):
    f,_=lift_data(t,s,m)
    return [evaluate(f,t,m),evaluate(f,s,m)]


def jacobian(t,s):
    # Exact polynomial congruence, not a floating finite difference:
    # (E(x+17e_j)-E(x))/17 = partial_j E(x) mod 17.
    m=P**2
    e=equations(t,s,m)
    columns=[]
    for dt,ds in ((P,0),(0,P)):
        shifted=equations(t+dt,s+ds,m)
        differences=[(a-b)%m for a,b in zip(shifted,e)]
        require(all(x%P==0 for x in differences),'Jacobian difference division')
        columns.append([x//P%P for x in differences])
    return [[columns[j][i] for j in range(2)] for i in range(2)]


def solve2(J,rhs):
    a,b=J[0]
    c,d=J[1]
    inv=pow((a*d-b*c)%P,-1,P)
    return [(d*rhs[0]-b*rhs[1])*inv%P,(-c*rhs[0]+a*rhs[1])*inv%P]


def qinverse(a):
    norm=(a[0]**2-3*a[0]*a[1]+3*a[1]**2)%P
    inv=pow(norm,-1,P)
    return ((a[0]-3*a[1])*inv%P,-a[1]*inv%P)


def lift():
    t,s=10,6
    J=jacobian(t,s)
    require(J==[[2,12],[0,9]],'independently reconstructed square Jacobian')
    stages=[]
    for k in (1,2):
        pk,m=P**k,P**(k+1)
        e=equations(t,s,m)
        require(all(x%pk==0 for x in e),'square system preceding precision')
        dt,ds=solve2(jacobian(t,s),[-x//pk%P for x in e])
        t,s=t+pk*dt,s+pk*ds
        f,a=lift_data(t,s,m)
        require(equations(t,s,m)==[0,0],'square-system Newton replay')
        require(evaluate(f,1,m)==evaluate(f,s,m,order=2)==0,'fixed visible equations')
        stages.append({'precision':k+1,'t':t,'s':s,'u':{str(j):a[j] for j in ACTIVE}})
    m=P**3
    f,a=lift_data(t,s,m)
    criticals=[]
    for initial in ((0,1),(-3,-1)):
        r=tuple(x%m for x in initial)
        for k in (1,2):
            pk,sub=P**k,P**(k+1)
            residual=qeval(f,r,sub,order=1)
            require(all(c%pk==0 for c in residual),'critical preceding precision')
            second=tuple(2*c%P for c in qeval(f,r,P,order=2))
            require(second==(6,0),'computed ordinary second derivative')
            correction=qmul(tuple(-c//pk%P for c in residual),qinverse(second),P)
            r=qadd(r,tuple(pk*c for c in correction),sub)
            require(qeval(f,r,sub,order=1)==(0,0),'critical Newton replay')
        value=qeval(f,r,m)
        require(all(c%(P**2)==0 for c in value),'first critical obstruction vanishes')
        divided=tuple(c//(P**2) for c in value)
        norm=(divided[0]**2-3*divided[0]*divided[1]+3*divided[1]**2)%P
        require(norm!=0,'second critical obstruction is a unit in both orientations')
        criticals.append({'root':list(r),'value':list(value),'divided':list(divided),'norm_mod17':norm})
    require(criticals[0]['divided']==[9,4] and criticals[1]['divided']==[14,13],
            'conjugate second obstructions')
    return J,stages,f,criticals


def main():
    roots,doubles=field_and_roots()
    ell=ell_coefficients()
    domain,survivors,tested=census(roots,doubles,ell)
    J,stages,f,criticals=lift()
    # Frozen receipts are read only after all computations have completed.
    producer=json.loads((HERE/'row4-first-obstruction.json').read_text())
    require(producer['nonzero_root_domain']==[list(r) for r in domain],'producer root-domain comparison')
    require(producer['ell_affine_pair_coefficients']==[list(c) for c in ell],'producer ell comparison')
    expected=[{k:s[k] for k in ('alpha','witnesses','u')} for s in producer['first_division_survivors']]
    require(sorted(survivors,key=lambda s:s['alpha'])==sorted(expected,key=lambda s:s['alpha']),
            'producer survivor comparison')
    receipt=json.loads((HERE/'row4-smallest-support-lift.json').read_text())
    require(stages==receipt['lift_stages'] and f==receipt['ordinary_coefficients'],'producer lift comparison')
    require(criticals[0]['root']==receipt['critical_root'] and criticals[0]['value']==receipt['critical_value'],
            'producer critical-value comparison')
    files=['row4_first_obstruction.py','row4-first-obstruction.json','lift_row4_smallest_support.py',
           'row4-smallest-support-lift.json','ROW4_SMALLEST_SUPPORT_EXCLUSION.md']
    hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files}
    print(json.dumps({'status':'PASS','scope':'Row4 exact deficiency support {2,4,10,12,18,19} only',
                      'implementation':'standard library; no producer imports or FLINT',
                      'field_elements_tested':17**4,'distinct_roots':len(roots),'oriented_markings':tested,
                      'survivors':survivors,'ell_active':[list(ell[0])]+[list(ell[j-3]) for j in ACTIVE],
                      'square_jacobian_mod17':J,'lift_stages':stages,'critical_orientations':criticals,
                      'unused_filter':'quadratic first-jet feature was not invoked',
                      'producer_fingerprints':hashes},indent=2))


if __name__=='__main__':
    main()
