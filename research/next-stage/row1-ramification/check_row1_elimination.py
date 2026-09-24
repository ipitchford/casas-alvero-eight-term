#!/usr/bin/env python3
"""Independent reconstruction of the row-1 elimination and error polynomials.

The producer used direct coefficient formulas and binomial translation.
This checker forms f as an X-polynomial, differentiates it, and translates
with Horner composition. It uses only exact standard-library arithmetic.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(*polynomials):
    out = [0]*max((len(a) for a in polynomials), default=0)
    for a in polynomials:
        for i, c in enumerate(a):
            out[i] += c
    return trim(out)


def scale(a, scalar):
    return trim([scalar*c for c in a])


def product(a, b):
    if not a or not b:
        return []
    out = [0]*(len(a)+len(b)-1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i+j] += left*right
    return trim(out)


def monomial(degree, coefficient=1):
    return [0]*degree+[coefficient]


def compose(a, at):
    out = []
    for coefficient in reversed(a):
        out = add(product(out, at), [coefficient])
    return out


def evaluate_X(poly, at):
    out = []
    for degree in range(max(poly), -1, -1):
        out = add(product(out, at), poly.get(degree, []))
    return out


def derivative(a):
    return [degree*coefficient for degree, coefficient in enumerate(a)][1:]


def v17(integer):
    if not integer:
        return None
    integer = abs(integer)
    count = 0
    while integer % 17 == 0:
        integer //= 17
        count += 1
    return count


def reconstruct_direction(index):
    # Coefficients in this X-polynomial are themselves integer polynomials in x.
    # index=None is the constant direction; 3,6,10 are normalized parameters.
    x = [0, 1]
    u = (monomial(16, -1) if index is None
         else monomial(16-index, -comb(16, index)))
    f = {4: scale(u, comb(20,16))}
    if index is None:
        f[20] = [1]
    else:
        f[20-index] = [comb(20,index)]
    D = scale(add(*(scale(coefficient, comb(degree,3))
                    for degree, coefficient in f.items())), -1)
    f[3] = D
    E = scale(add(*f.values()), -1)
    f[1] = E
    require(not add(*f.values()), "f(1) normalization failed")
    require(not add(*(scale(coefficient,comb(degree,3))
                      for degree,coefficient in f.items())),
            "H_3 f(1) normalization failed")
    quotient = {degree-1:coefficient for degree,coefficient in f.items()}
    differentiated = {degree-1:scale(coefficient,degree)
                      for degree,coefficient in f.items()}
    P = evaluate_X(quotient,x)
    Q = add(evaluate_X(differentiated,x),scale(P,-1))
    return {"u":u,"D":D,"E":E,"P":P,"Q":Q}


def expected_valuation(degree):
    if degree in (0,1):
        return None
    if degree in (3,21):
        return 2
    if 17 <= degree <= 19 or 34 <= degree <= 35:
        return 0
    return 1


def eight_marking_census():
    active = (6,10,16)
    records = []
    for code in range(8):
        marks = [(code >> (2-k)) & 1 for k in range(3)]
        witness = dict(zip(active,marks))
        a = [1]+[0]*16
        for j in range(1,17):
            w = witness.get(j,0)
            a[j] = -sum(comb(j,i)*a[i]*w**(j-i) for i in range(j)) % 17
            if j not in active:
                require(a[j]==0,"Inactive normalized coefficient is nonzero")
        # Reconstruct f'(1) from H_3f(1)=f(1)=0 instead of importing
        # the simplified first-divided weight formula.
        ordinary = {20:1}
        ordinary.update({20-j:comb(20,j)*a[j] for j in active})
        D = -sum(comb(degree,3)*coefficient
                 for degree,coefficient in ordinary.items())
        ordinary[3]=D
        E=-sum(ordinary.values())
        ordinary[1]=E
        H=sum(degree*coefficient for degree,coefficient in ordinary.items())
        require(H%17==0,"First derivative is not divisible by 17")
        W=H//17%17
        simplified=(-133+sum(((19-j)-2*comb(20-j,3))*
                             (comb(20,j)//17)*a[j] for j in active))%17
        require(W==simplified,"The first-divided formula disagrees with f'(1)")
        for j in range(1,17):
            w=witness.get(j,0)
            require(sum(comb(j,i)*a[i]*w**(j-i)
                        for i in range(j+1))%17==0,
                    "A normalized derivative fails at its marked root")
        records.append({"witnesses":marks,"activeCoefficients":[a[j] for j in active],
                        "firstDividedResidue":W})
    expected=[
        ([0,0,0],[0,0,0],3),([0,0,1],[0,0,16],0),
        ([0,1,0],[0,16,0],2),([0,1,1],[0,16,0],2),
        ([1,0,0],[16,0,0],5),([1,0,1],[16,0,0],5),
        ([1,1,0],[16,5,0],10),([1,1,1],[16,5,12],12)]
    require([(r["witnesses"],r["activeCoefficients"],r["firstDividedResidue"])
             for r in records]==expected,"Eight-marking table differs")
    survivors=[r for r in records if r["firstDividedResidue"]==0]
    require(len(survivors)==1 and survivors[0]["activeCoefficients"]==[0,0,16],
            "Unexpected survivor of eight-marking check")
    return {"activeDeficiencies":list(active),"assignmentCount":8,
            "allAssignments":records,"survivors":survivors,
            "scope":"Assumes a3 has residue zero and its contribution to f'(1)/17 "
                    "vanishes; the latter uses the separate valuation bound v17(a3)>=3/2."}


def verify(data):
    require(data["coefficientOrder"]=="ascending","Unexpected coefficient order")
    directions = {name:reconstruct_direction(index) for name,index in
                  (("constant",None),("t",3),("a6",6),("a10",10))}
    require(data["sourceParts"]==directions,"Source polynomial arrays disagree")
    P0,Q0,P1,Q1=(directions[name][key] for name,key in
                 (("constant","P"),("constant","Q"),("t","P"),("t","Q")))
    R = add(product(P0,Q1),scale(product(Q0,P1),-1))
    translated = compose(R,[1,1])
    require(data["R"]==R,"Wrong R polynomial")
    require(data["R_at_one_plus_z"]==translated,"Wrong translated R polynomial")
    require(len(translated)==36 and translated[:2]==[0,0] and translated[2]!=0,
            "The exact z-order must be two and total degree 35")
    require(data["R_dividedBy_z2"]==translated[2:],"Wrong divided R polynomial")
    values=[[degree,v17(value)] for degree,value in enumerate(translated)]
    require(values==data["valuationTable"],"Incorrect saved valuation table")
    require(all(value==expected_valuation(degree) for degree,value in values),
            "The proposed coefficient valuation pattern fails")
    require(translated[2]%17==0 and translated[2]//17%17==7,
            "Wrong z^2 initial coefficient")
    require(translated[17]%17==16,"Wrong z^17 initial coefficient")
    require(sum(Q1)==12033840 and sum(Q1)%17==16,
            "Q1(1) is not the stated unit")
    require(data["Q1_at_one"]==sum(Q1),"Wrong saved Q1(1)")

    error_reports={}
    for name in ("a6","a10"):
        Pk,Qk=directions[name]["P"],directions[name]["Q"]
        require(all(c%17==0 for c in Pk+Qk),
                "An input error multiplier is not divisible by 17")
        L=add(product(Q1,Pk),scale(product(P1,Qk),-1))
        Lz=compose(L,[1,1])
        require(Lz[:2]==[0,0] and all(c%17==0 for c in Lz),
                "Error eliminant does not have the factor 17z^2")
        A=[c//17 for c in Lz[2:]]
        expected={"L":L,"translatedL":Lz,"dividedBy17z2":A}
        require(data["errors"][name]==expected,"Wrong error coefficient arrays")
        require(sum(Pk)==0 and sum(derivative(Pk))==sum(Qk),
                "Normalization explanation of the double factor fails")
        error_reports[name]={"degreeAfter17z2Division":len(A)-1,
                             "minimumInputMultiplierValuation":
                             min(v17(c) for c in Pk+Qk if c)}
    require(sum(P0)==sum(P1)==0,"P directions must vanish at x=1")
    require(sum(derivative(P0))==sum(Q0) and
            sum(derivative(P1))==sum(Q1),"P'(1)=Q(1) identities fail")

    # pi^15=17; the coefficient of Z^k in S(pi Z)/17 has this value.
    scaled=[]
    for k,coefficient in enumerate(translated[2:]):
        weight=Fraction(v17(coefficient))+Fraction(k,15)-1
        require(weight>=0,"A negative scaled coefficient valuation appears")
        scaled.append([k,str(weight)])
    zero_indices=[k for k,weight in scaled if weight=="0"]
    require(zero_indices==[0,15],"Unexpected terms in the initial polynomial")
    require(v17(sum(Q0))==2,"Q0(1) must have valuation two")
    require(v17(sum(directions["constant"]["E"]))==1,
            "The x=1 baseline E must have valuation one")
    return {"valuationTable":values,"errorDivisibility":error_reports,
            "scaledCoefficientValuations":scaled,
            "initialPolynomialAscending":[7]+[0]*14+[16],
            "Q1_at_one":sum(Q1),"Q1_at_one_mod17":sum(Q1)%17,
            "xEqualsOne":{"Q0":sum(Q0),"v17Q0":2,
                          "E0":sum(directions["constant"]["E"]),"v17E0":1}}


def main():
    path=ROOT/"row1-elimination-certificate.json"
    raw=path.read_bytes()
    data=json.loads(raw)
    report=verify(data)
    census=eight_marking_census()
    require(pow(5,15,17)==7,"5 is not the stated base-field root")
    require((17**4-1)%15==0,"The unramified degree-four residue field is insufficient")
    require(all((17**d-1)%15!=0 for d in (1,2)),
            "Unexpected order of 17 modulo 15")
    mutation=json.loads(raw)
    mutation["R"][0]+=1
    rejected=False
    try:
        verify(mutation)
    except ValueError:
        rejected=True
    require(rejected,"Changed eliminant coefficient was accepted")
    print(json.dumps({"status":"PASS",
                      "certificateSHA256":hashlib.sha256(raw).hexdigest(),
                      **report,"binaryCensus":census,
                      "residueFieldChecks":{"fiveTo15Modulo17":7,
                                            "orderOf17Modulo15":4,
                                            "rootDerivative":"-15*Z^14, nonzero at every root"},
                      "negativeControlRejected":rejected,
                      "scope":"Exact elimination, all coefficient valuations, "
                              "17z^2 factors in both error directions, and the "
                              "initial polynomial. No full CA exclusion follows "
                              "without the common-root and coefficient-valuation "
                              "hypotheses in the accompanying note."},indent=2))


if __name__=="__main__":
    main()
