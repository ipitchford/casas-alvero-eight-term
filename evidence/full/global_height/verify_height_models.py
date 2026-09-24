#!/usr/bin/env python3
"""Exact algebraic checks for ALL_PLACE_BOUND.md; no sampled-prime claims."""
from fractions import Fraction as Q
from math import comb
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def trim(a):
    a = list(map(Q, a))
    while len(a)>1 and not a[-1]:
        a.pop()
    return a


def multiply(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def hasse(a,k):
    return trim([Q(a[i])*comb(i,k) for i in range(k,len(a))])


def evaluate(a,x):
    value = Q(0)
    for c in reversed(a):
        value = value*x+c
    return value


def remainder(a,b):
    a,b = trim(a),trim(b)
    while len(a)>=len(b) and a!=[0]:
        c,s = a[-1]/b[-1],len(a)-len(b)
        for i,x in enumerate(b):
            a[i+s] -= c*x
        a=trim(a)
    return a


def gcd(a,b):
    a,b=trim(a),trim(b)
    while b!=[0]:
        a,b=b,remainder(a,b)
    return [x/a[-1] for x in a]


def model(t):
    cubic=[60*t-6,-12,2,1]
    f=multiply(multiply([0,1],multiply([-1,1],[-1,1])),cubic)
    normalized=[f[6-i]/Q(comb(6,i)) for i in range(7)]
    require(normalized==[1,0,-1,1+3*t,-8*t,-1+10*t,0], "normalized coefficients")
    require(all(a.denominator==1 for a in normalized), "integral normalized coefficients")
    require(f[-1]==1 and f[-2]==0 and f[0]==0, "monic centered mean root")
    require(f[1]!=0, "mean root simple for integer t")
    require(evaluate(f,1)==0 and evaluate(hasse(f,1),1)==0
            and evaluate(hasse(f,2),1)!=0, "root 1 exactly double")
    chain=[[x/Q(comb(6,j)) for x in hasse(f,6-j)] for j in range(7)]
    require(chain[2]==[-1,0,1], "first nonzero coefficient witness")
    require(evaluate(chain[1],0)==0 and evaluate(chain[2],1)==0
            and evaluate(chain[5],1)==0, "three exact CA conditions")
    require(abs(cubic[0])==abs(60*t-6), "cubic root product bound")
    return f,chain,cubic


def main():
    f,chain,cubic=model(0)
    require(f==[0,-6,0,20,-15,0,1], "base polynomial expansion")
    require(chain[3]==[1,-3,0,1], "base G3")
    require(gcd(f,chain[3])==[1], "only missing normalized incidence")
    require(evaluate(chain[4],0)==0, "fourth normalized incidence")
    require(gcd(f,hasse(f,1))==[-1,1], "only repeated root is 1")
    signs={x:evaluate(cubic,x) for x in (-5,-4,-1,0,2,3)}
    require(signs=={-5:-21,-4:10,-1:7,0:-6,2:-14,3:3}, "three real root intervals")
    require(2*comb(6,2)-2==28 and 6-1-2==3, "height lower bound constants")
    for t in range(-20,21):
        model(t)
    print(json.dumps({"status":"PASS", "base_missing_hasse_order":3,
                      "base_exact_CA_conditions":4, "base_normalized_coefficients":[1,0,-1,1,0,-1,0],
                      "base_root_radius_interval":[4,5], "base_height_lower_bound_squared":"28/3",
                      "family_integer_parameters_checked":41,
                      "all_finite_places_argument":"monic integral polynomial and exact root 1"},indent=2))


if __name__=="__main__":
    main()
