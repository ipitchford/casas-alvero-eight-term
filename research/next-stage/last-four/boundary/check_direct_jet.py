#!/usr/bin/env python3
"""Exact finite identities for the direct unit-16 obstruction; no proof claim by itself."""
from math import comb
from fractions import Fraction
import json


def require(ok, text):
    if not ok:
        raise ValueError(text)


def add(*terms):
    out = [0] * max(map(len, terms), default=0)
    for term in terms:
        for i, v in enumerate(term):
            out[i] += v
    while out and not out[-1]:
        out.pop()
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i+j] += v*w
    return add(out)


def mon(k, v=1):
    return [0]*k+[v]


def scale(a, v):
    return [c*v for c in a]


def val(n):
    if not n:
        return None
    v = 0
    while n % 17 == 0:
        n //= 17
        v += 1
    return v


def shift(a):
    return [sum(c*comb(k,j) for k,c in enumerate(a) if k>=j)
            for j in range(len(a))]


def reconstruct():
    # Q=f'-f/X, with u=-x^16-560*t*x^13 and D=-1140-775200*t-19380*u.
    q0 = add(mon(19,19), mul(mon(3,14535),mon(16,-1)),
             mul(mon(2,2),add([-1140],mon(16,19380))))
    q1 = add(mon(16,16*1140), mul(mon(3,14535),mon(13,-560)),
             mul(mon(2,2),add([-775200],mon(13,19380*560))))
    expected0=add(mon(19,-14516),mon(18,38760),mon(2,-2280))
    expected1=add(mon(16,-8121360),mon(15,21705600),mon(2,-1550400))
    require(q0==expected0 and q1==expected1,'Wrong Q identities')
    # f directions before elimination, including the normalization of D,E.
    directions = {
        'constant': add(mon(20),mon(3,-1140),mon(1,1139)),
        'u': add(mon(4,4845),mon(3,-19380),mon(1,14535)),
        't': add(mon(17,1140),mon(3,-775200),mon(1,774060)),
    }
    expected = {'constant':[-2261,-3230,0,4845],
                'u':[-24225,-29070,0,4845],
                't':[-1532160,-2170560,0,2713200]}
    for key, poly in directions.items():
        require(sum(poly)==0,'f(1) normalization')
        require(shift(poly)[1:5]==expected[key], 'Wrong cluster coefficients')
    require(all(val(comb(20,j))==1 for j in range(4,16)),
            'Middle ordinary coefficient factor must have value one')
    return q0,q1


def verify(q0):
    q=shift(q0)
    require(val(q[0])==val(q[1])==2,'Low jets')
    require(val(q[2])==1 and q[2]//17%17==1,'Second divided jet')
    require(all(v==0 or val(v)>=1 for v in q[3:17]),'Intermediate jets')
    require(q[17]%17==2,'Wild jet')
    values=[(i,Fraction(val(v))+Fraction(i,15)) for i,v in enumerate(q) if v]
    low=min(value for _,value in values)
    require(low==Fraction(17,15),'Lowest valuation')
    require([i for i,value in values if value==low]==[2,17],'Minimum terms')
    require((1+2*7)%17==15,'Initial coefficient does not vanish')
    require(Fraction(17,15)<Fraction(3,2)<3,'Strict perturbation separation')
    require(sum(q0)==21964 and val(sum(q0))==2,'Exact root-one case')
    return {'shiftedQ0':q,'termValuationsAtOneFifteenth':[[i,str(v)] for i,v in values],
            'minimalIndices':[2,17],'minimalValuation':'17/15','initialFactor':15}


def main():
    q0,q1=reconstruct()
    result=verify(q0)
    changed=q0.copy();changed[2]+=17
    try:
        verify(changed)
    except ValueError:
        rejected=True
    else:
        rejected=False
    require(rejected,'Mutation not rejected')
    print(json.dumps({'status':'PASS','Q0':q0,'Q1':q1,**result,
                      'negativeControlRejected':rejected,
                      'scope':'Exact polynomial identities and valuation comparisons only. '
                              'The collision and global normalization arguments are separate.'},indent=2))

if __name__=='__main__':
    main()
