#!/usr/bin/env python3
"""Exact Q(sqrt(3)) check of the normal derivative flag."""
from fractions import Fraction as Q
from itertools import permutations
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


class E:
    def __init__(self, a=0, b=0):
        self.a, self.b = Q(a), Q(b)
    def __add__(self, other):
        other = other if isinstance(other,E) else E(other)
        return E(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self):
        return E(-self.a,-self.b)
    def __sub__(self, other):
        return self+-other if isinstance(other,E) else self+E(-other)
    def __mul__(self, other):
        other = other if isinstance(other,E) else E(other)
        return E(self.a*other.a+3*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __eq__(self, other):
        other = other if isinstance(other,E) else E(other)
        return self.a==other.a and self.b==other.b
    def __repr__(self):
        return f"({self.a})+({self.b})sqrt(3)"


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),E())
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def identity(n):
    return [[E(int(i==j)) for j in range(n)] for i in range(n)]


def poly_mul(a,b):
    out=[E()]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=out[i+j]+x*y
    return out


def charpoly(A):
    n=len(A)
    out=[E()]*(n+1)
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=[E(sign)]
        for i,j in enumerate(p):
            term=poly_mul(term,[-A[i][j],E(int(i==j))])
        for i,x in enumerate(term):
            out[i]=out[i]+x
    return out


def trim(a):
    a=list(map(Q,a))
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def remainder(a,b):
    a,b=trim(a),trim(b)
    while len(a)>=len(b) and a!=[0]:
        factor,shift=a[-1]/b[-1],len(a)-len(b)
        for i,c in enumerate(b):
            a[i+shift]-=factor*c
        a=trim(a)
    return a


def gcd(a,b):
    a,b=trim(a),trim(b)
    while b!=[0]:
        a,b=b,remainder(a,b)
    return [x/a[-1] for x in a]


def main():
    a,b=E(0,Q(1,2)),E(Q(1,2))
    A=[[E(),E(),b,a],[E(1),E(),E(),E()],
       [E(),b,E(),E()],[E(),a,E(),E()]]
    require(mm(A,transpose(A))==mm(transpose(A),A),"full normality")
    expected={1:[0,1],2:[0,0,1],3:[Q(-1,4),0,0,1],4:[0,-1,0,0,1]}
    polynomials={}
    for j in range(1,5):
        B=[row[:j] for row in A[:j]]
        cp=charpoly(B)
        require(cp==[E(x) for x in expected[j]],f"characteristic polynomial {j}")
        polynomials[j]=expected[j]
        if j in (2,3):
            require(mm(B,transpose(B))!=mm(transpose(B),B),"intermediate nonnormality")
        power=identity(j)
        for k in range(j):
            require(j*power[j-1][j-1]==sum((power[i][i] for i in range(j)),E()),
                    f"trace vector: dimension {j}, power {k}")
            power=mm(power,B)
    kernel=[[E()],[E()],[a],[-b]]
    require(mm(A,kernel)==[[E()]]*4,"original simple-eigenvalue kernel")
    require(kernel[0][0]==0 and kernel[1][0]==0,"kernel misses first two subspaces")
    require(gcd(expected[4],expected[1])==[0,1],"first shared spectrum")
    require(gcd(expected[4],expected[2])==[0,1],"second shared spectrum")
    require(gcd(expected[4],expected[3])==[1],"only missing spectral incidence")
    for n in range(5,51):
        t=Q(n-2,2*(n-1))
        require(0<t<1 and (1-t)**(n-1)*(1+(n-1)*t)>0,
                "positive definite hypothetical projector Gram matrix")
    print(json.dumps({"status":"PASS","full_matrix_normal":True,
                      "nonnormal_block_dimensions":[2,3],
                      "all_trace_vector_moments_checked":True,
                      "shared_original_eigenvalue":0,
                      "original_kernel_orthogonal_to_shared_blocks":True,
                      "only_missing_block_dimension":3,
                      "universal_plane_obstruction":"n independent projectors in real dimension 4"},indent=2))


if __name__=="__main__":
    main()
