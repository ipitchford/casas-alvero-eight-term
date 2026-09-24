"""Independent replay: general binomial equations, no producer imports.

The divided obstruction is recovered from H_2 f(1) modulo 17^3, not from
the producer's hard-coded linear functional or parameter recurrences.
"""
from pathlib import Path
from math import comb
import json

BASE = Path(__file__).resolve().parent
P = 17
Q = [-3,-5,-2,0,-3,1]


def require(ok, why):
    if not ok:
        raise ValueError(why)


class Algebra:
    def __init__(self, modulus):
        self.m = modulus

    def const(self, n):
        return (n % self.m,0,0,0,0)

    def add(self, x, y):
        return tuple((a+b) % self.m for a,b in zip(x,y))

    def times_integer(self, x, n):
        return tuple(a*n % self.m for a in x)

    def multiply(self, x, y):
        v = [0]*9
        for i in range(5):
            for j in range(5):
                v[i+j] = (v[i+j]+x[i]*y[j]) % self.m
        for degree in range(8,4,-1):
            c = v[degree]
            for j in range(5):
                v[degree-5+j] = (v[degree-5+j]-c*Q[j]) % self.m
        return tuple(v[:5])

    def pow(self, x, n):
        y = self.const(1)
        while n:
            if n & 1:
                y = self.multiply(y,x)
            x = self.multiply(x,x)
            n >>= 1
        return y


def derivative_value(A, f, k, r):
    value = A.const(0)
    for i,c in enumerate(f):
        if i >= k:
            term = A.times_integer(A.multiply(c,A.pow(r,i-k)),comb(i,k))
            value = A.add(value,term)
    return value


def normalized_parameters(A,s,t):
    a = [A.const(0) for _ in range(21)]
    a[0],a[3] = A.const(1),A.const(-1)
    witnesses = {j:A.const(0) for j in range(4,17)}
    witnesses.update({4:s,9:t,10:A.const(1),14:s})
    for j in range(4,17):
        total = A.const(0)
        for i in range(j):
            term = A.multiply(a[i],A.pow(witnesses[j],j-i))
            total = A.add(total,A.times_integer(term,comb(j,i)))
        a[j] = A.times_integer(total,-1)
    prefix = [A.const(0) for _ in range(21)]
    for j in range(18):
        prefix[20-j] = A.times_integer(a[j],comb(20,j))
    s0 = derivative_value(A,prefix,0,A.const(1))
    s1 = derivative_value(A,prefix,1,A.const(1))
    a[18] = A.times_integer(A.add(s0,A.times_integer(s1,-1)),pow(190,-1,A.m))
    a[19] = A.times_integer(A.add(s1,A.times_integer(s0,-2)),pow(20,-1,A.m))
    f = [A.times_integer(a[20-i],comb(20,i)) for i in range(21)]
    return a,f


def polynomial_gcd(a,b,p):
    def trim(v):
        while v and v[-1] % p == 0:
            v.pop()
        return [c % p for c in v]
    a,b = trim(a),trim(b)
    while b:
        rem = a.copy()
        while len(rem) >= len(b):
            z = rem[-1]*pow(b[-1],-1,p) % p
            offset = len(rem)-len(b)
            for i,v in enumerate(b):
                rem[offset+i] = (rem[offset+i]-z*v) % p
            rem = trim(rem)
        a,b = b,rem
    return [v*pow(a[-1],-1,p) % p for v in a]


def main():
    cert = json.loads((BASE/'row9-one-scenario.json').read_text())
    require(cert['unramifiedPolynomialLowToHigh'] == Q, 'defining polynomial')
    require(cert['firstNonzeroPrecision'] == 2 and len(cert['lifts']) == 1, 'bounded certificate form')
    require(cert['deficiencySupport'] == [3,4,9,10,14,18,19], 'scenario support')
    field = Algebra(17)
    eta = (0,1,0,0,0)
    eta17 = field.pow(eta,17)
    require(polynomial_gcd(Q,list(field.add(eta17,field.times_integer(eta,-1))),17) == [1], 'irreducibility proper Frobenius test')
    require(field.pow(eta,17**5) == eta, 'irreducibility full Frobenius test')
    # Since degree five is prime, the preceding two conditions prove irreducibility.
    residue_s,residue_t = field.const(-2),eta
    ar,hr = normalized_parameters(field,residue_s,residue_t)
    expected = [field.const(0) for _ in range(21)]
    for degree,value in {20:1,17:-1,2:-3,1:3}.items():
        expected[degree] = field.const(value)
    require(hr == expected, 'seed identity')
    require(all(comb(20,j) % 17 == 0 for j in range(4,17)), 'parameter-independence coefficients')
    jacobian = [derivative_value(field,hr,1,x) for x in (residue_s,residue_t)]
    for entry in jacobian:
        inv = field.pow(entry,17**5-2)
        require(field.multiply(entry,inv) == field.const(1), 'Jacobian unit')
    require([list(v) for v in jacobian] == cert['jacobianDiagonalMod17'], 'Jacobian certificate')
    step = cert['lifts'][0]
    require(step['modulus'] == 289 and step['precision'] == 2, 'precision')
    s,t = tuple(step['s']),tuple(step['t'])
    require(tuple(v % 17 for v in s) == residue_s and tuple(v % 17 for v in t) == residue_t, 'residues')
    small = Algebra(289)
    a,f = normalized_parameters(small,s,t)
    require(derivative_value(small,f,0,s) == small.const(0), 'F(s)')
    require(derivative_value(small,f,0,t) == small.const(0), 'F(t)')
    require(derivative_value(small,f,0,small.const(1)) == small.const(0), 'f(1)')
    require(derivative_value(small,f,1,small.const(1)) == small.const(0), 'H1 f(1)')
    high = Algebra(4913)
    _,fh = normalized_parameters(high,s,t)
    second = derivative_value(high,fh,2,high.const(1))
    require(all(v % 17 == 0 for v in second), 'divisible H2')
    divided = tuple(v//17 for v in second)
    require(list(divided) == step['T'], 'independently recovered T')
    require(all(v % 17 == 0 for v in divided), 'first congruence')
    digit = tuple((v//17) % 17 for v in divided)
    require(list(digit) == cert['firstNonzeroTDigit'], 'obstruction digit')
    require(any(digit), 'nonzero obstruction')
    inverse = field.pow(digit,17**5-2)
    require(field.multiply(digit,inverse) == field.const(1), 'obstruction is nonzero in field')
    orbit = []
    value = digit
    for _ in range(5):
        require(any(value), 'conjugate obstruction')
        orbit.append(list(value))
        value = field.pow(value,17)
    require(value == digit, 'Frobenius orbit closure')
    print(json.dumps({'status':'PASS','precision':2,
        'scope':'Five marked row9 scenarios in one Frobenius orbit only.',
        'FEquationsCheckedModulo':289,'H2EvaluatedModulo':4913,
        'TValuation':1,'H2Valuation':2,
        'obstructionDigitLowToHigh':list(digit),
        'nonzeroFrobeniusConjugateDigits':orbit},indent=2))


if __name__ == '__main__':
    main()
