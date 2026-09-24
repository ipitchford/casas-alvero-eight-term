"""One bounded exact residue-scenario lift in Z/17^N[eta]/Q5(eta)."""
from math import comb
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
P = 17
D = 5
RELATION = [3, 5, 2, 0, 3]  # eta^5 = 3+5eta+2eta^2+3eta^4.


def require(ok, why):
    if not ok:
        raise ValueError(why)


class Ring:
    def __init__(self, modulus):
        self.modulus = modulus
        self.zero = [0]*D
        self.one = [1]+[0]*(D-1)

    def scalar(self, c):
        return [c % self.modulus]+[0]*(D-1)

    def add(self, a, b):
        return [(x+y) % self.modulus for x,y in zip(a,b)]

    def neg(self, a):
        return [(-v) % self.modulus for v in a]

    def scale(self, a, c):
        return [(c*v) % self.modulus for v in a]

    def mul(self, a, b):
        c = [0]*(2*D-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                c[i+j] += x*y
        for k in range(len(c)-1,D-1,-1):
            for j,v in enumerate(RELATION):
                c[k-D+j] += c[k]*v
        return [v % self.modulus for v in c[:D]]

    def power(self, a, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out,a)
            a = self.mul(a,a)
            n //= 2
        return out

    def inverse_field(self, a):
        require(self.modulus == P and any(a), 'field inverse input')
        b = self.power(a,P**D-2)
        require(self.mul(a,b) == self.one, 'field inverse')
        return b


def parameters(r,s,t):
    a4 = r.add(r.neg(r.power(s,4)),r.scale(s,4))
    a9 = r.add(r.add(r.neg(r.power(t,9)),r.scale(r.power(t,6),84)),
               r.scale(r.mul(a4,r.power(t,5)),-126))
    a10 = r.add(r.add(r.scalar(119),r.scale(a4,-210)),r.scale(a9,-10))
    a14 = r.add(r.neg(r.power(s,14)),r.scale(r.power(s,11),364))
    for coefficient,a,power in [(1001,a4,10),(2002,a9,5),(1001,a10,4)]:
        a14 = r.add(a14,r.scale(r.mul(a,r.power(s,power)),-coefficient))
    return {4:a4,9:a9,10:a10,14:a14}


def polynomial(r,s,t):
    a = parameters(r,s,t)
    f = [r.zero.copy() for _ in range(21)]
    f[20],f[17] = r.one,r.scalar(-1140)
    f[2],f[1] = r.scalar(18221),r.scalar(-17082)
    for j,v in a.items():
        coefficient = r.scale(v,comb(20,j))
        f[20-j] = coefficient
        f[2] = r.add(f[2],r.scale(coefficient,-(19-j)))
        f[1] = r.add(f[1],r.scale(coefficient,18-j))
    return f


def evaluate(r,f,x,k=0):
    out = r.zero
    for i in range(len(f)-1,k-1,-1):
        out = r.add(r.mul(out,x),r.scale(f[i],comb(i,k)))
    return out


def obstruction(r,s,t):
    out = r.scalar(-8037)
    for j,v in parameters(r,s,t).items():
        out = r.add(out,r.scale(v,comb(19-j,2)*(comb(20,j)//17)))
    return out


def main():
    field = Ring(P)
    s,t = field.scalar(-2),[0,1,0,0,0]
    seed = polynomial(field,s,t)
    require(evaluate(field,seed,s) == evaluate(field,seed,t) == field.zero, 'initial roots')
    js,jt = evaluate(field,seed,s,1),evaluate(field,seed,t,1)
    invs,invt = field.inverse_field(js),field.inverse_field(jt)
    initial = parameters(field,s,t)
    z = initial[9]
    require(initial[4] == field.scalar(10), 'a4 residue')
    require(initial[10] == field.add(field.scalar(8),field.scale(z,7)), 'a10 residue')
    require(initial[14] == field.add(field.scalar(12),field.scale(z,11)), 'a14 residue')
    require(obstruction(field,s,t) == field.zero, 'first obstruction already nonzero')
    record = {'scope':'Single marked row9 residue scenario; not complete row9 exclusion.',
        'unramifiedPolynomialLowToHigh':[-3,-5,-2,0,-3,1],
        'deficiencySupport':[3,4,9,10,14,18,19],
        'residueWitnesses':{'s':s.copy(),'t':t.copy()},
        'residueParameters':initial,
        'jacobianDiagonalMod17':[js,jt], 'lifts':[]}
    for precision in range(2,9):
        modulus = P**precision
        lower = P**(precision-1)
        r = Ring(modulus)
        f = polynomial(r,s,t)
        fs,ft = evaluate(r,f,s),evaluate(r,f,t)
        require(all(v % lower == 0 for v in fs+ft), 'previous precision lost')
        ds = field.neg(field.mul([v//lower for v in fs],invs))
        dt = field.neg(field.mul([v//lower for v in ft],invt))
        s = [(v+lower*c) % modulus for v,c in zip(s,ds)]
        t = [(v+lower*c) % modulus for v,c in zip(t,dt)]
        f = polynomial(r,s,t)
        require(evaluate(r,f,s) == evaluate(r,f,t) == r.zero, 'Newton precision failure')
        require(evaluate(r,f,r.one) == evaluate(r,f,r.one,1) == r.zero, 'double root equations')
        obs = obstruction(r,s,t)
        require(evaluate(r,f,r.one,2) == r.scale(obs,17), 'exact obstruction formula')
        step = {'precision':precision,'modulus':modulus,'s':s.copy(),'t':t.copy(),
                'F_s':[0]*D,'F_t':[0]*D,'T':obs}
        record['lifts'].append(step)
        if any(obs):
            valuation = 0
            while all(v % P**(valuation+1) == 0 for v in obs):
                valuation += 1
            record.update({'status':'SCENARIO EXCLUDED','firstNonzeroPrecision':precision,
                'valuationOfT':valuation,
                'firstNonzeroTDigit':[(v//P**valuation) % P for v in obs],
                'frobeniusConjugateScenariosExcluded':5})
            print(json.dumps(record,indent=2))
            return
    record['status'] = 'NO OBSTRUCTION THROUGH PRECISION 8'
    print(json.dumps(record,indent=2))


if __name__ == '__main__':
    main()
