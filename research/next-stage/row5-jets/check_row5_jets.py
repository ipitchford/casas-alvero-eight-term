#!/usr/bin/env python3
"""Independent integer-polynomial verification of the row-5 implicit jets.

All divisions in the polynomial identities are checked coefficientwise.
Implicit derivatives are computed modulo 17^4 by inversion of a unit.
No floating point arithmetic, external CAS, or producer data is used.
"""
from math import comb
import json

P = 17


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(*polys):
    out = [0]*max((len(a) for a in polys), default=0)
    for a in polys:
        for i, c in enumerate(a):
            out[i] += c
    return trim(out)


def scale(a, n):
    return trim([n*c for c in a])


def shift(a, n):
    return [0]*n+a if a else []


def mono(n, c=1):
    return [0]*n+[c]


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1) if a and b else []
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def derivative(a):
    return trim([i*c for i, c in enumerate(a)][1:])


def at(a, x):
    out = 0
    for c in reversed(a):
        out = out*x+c
    return out


def translate(a, offset=-2, multiplier=17):
    """Exact polynomial a(offset+multiplier*t), ascending in t."""
    out = [0]*len(a)
    for n, c in enumerate(a):
        for k in range(n+1):
            out[k] += c*comb(n, k)*offset**(n-k)*multiplier**k
    return trim(out)


def family(g3):
    a3 = [2] if g3 == "one" else [0, 3, 0, -1]
    a4 = scale(add(mono(4), mono(2, -comb(4, 2)),
                   scale(shift(a3, 1), comb(4, 3))), -1)
    E0 = add([comb(20, 2)-1], scale(a3, -comb(20, 3)),
             scale(a4, -comb(20, 4)))
    F0 = add(mono(20), mono(18, -comb(20, 2)),
             scale(shift(a3, 17), comb(20, 3)),
             scale(shift(a4, 16), comb(20, 4)), shift(E0, 1))
    Fb = scale(add(mono(10), mono(1, -1)), comb(20, 10))
    Fc = scale(add(mono(8), mono(1, -1)), comb(20, 12))
    H0 = add([20-18*comb(20, 2)], scale(a3, 17*comb(20, 3)),
             scale(a4, 16*comb(20, 4)), E0)
    Eb, Ec = -comb(20, 10), -comb(20, 12)
    Hb, Hc = 9*comb(20, 10), 7*comb(20, 12)
    return {"a3": a3, "a4": a4, "E": (E0, [Eb], [Ec]),
            "F": (F0, Fb, Fc), "H": (H0, [Hb], [Hc])}


def sparse_add(*polys):
    out = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, 0)+coefficient
    return {e: c for e, c in out.items() if c}


def sparse_scale(poly, scalar):
    return {e: c*scalar for e, c in poly.items() if c*scalar}


def divided(poly, divisor):
    result = {}
    for exponent, coefficient in poly.items():
        quotient, remainder = divmod(coefficient, divisor)
        require(remainder == 0, "Polynomial division was not coefficientwise exact")
        if quotient:
            result[exponent] = quotient
    return result


def shifted_three(parts):
    """A(r)+B(r)*b+C(r)*c at r=-2+17*t."""
    out = {}
    for part, axis in zip(parts, ((0, 0), (1, 0), (0, 1))):
        for k, coefficient in enumerate(translate(part)):
            if coefficient:
                out[(k, *axis)] = coefficient
    return out


def residue(poly):
    return {e: c % P for e, c in poly.items() if c % P}


def sparse_at(poly, t, b, c):
    return sum(value*t**e[0]*b**e[1]*c**e[2] for e, value in poly.items())


def serial(poly):
    return [[list(e), c] for e, c in sorted(poly.items())]


def hensel_root(poly, precision=4):
    r, modulus = 15, 17
    require(at(poly, r) % modulus == 0, "Base residue is not a root")
    require(at(derivative(poly), r) % 17 != 0, "Nonunit root derivative")
    for _ in range(1, precision):
        value = at(poly, r)
        quotient, remainder = divmod(value, modulus)
        require(remainder == 0, "Lost Hensel precision")
        digit = -quotient*pow(at(derivative(poly), r), -1, 17) % 17
        r += modulus*digit
        modulus *= 17
        require(at(poly, r) % modulus == 0, "Incorrect Hensel digit")
    return r


def implicit_derivatives(F, T, r, precision=4):
    """First and degree-two Taylor coefficients of T(r(b,c),b,c)."""
    mod = 17**precision
    F0, Fb, Fc = F
    T0, Tb, Tc = T
    inv = pow(at(derivative(F0), r), -1, mod)
    rb = -at(Fb, r)*inv % mod
    rc = -at(Fc, r)*inv % mod
    frr = at(derivative(derivative(F0)), r)
    frb, frc = at(derivative(Fb), r), at(derivative(Fc), r)
    rbb = -(frr*rb*rb+2*frb*rb)*inv % mod
    rbc = -(frr*rb*rc+frb*rc+frc*rb)*inv % mod
    rcc = -(frr*rc*rc+2*frc*rc)*inv % mod
    tr = at(derivative(T0), r)
    trr = at(derivative(derivative(T0)), r)
    trb, trc = at(derivative(Tb), r), at(derivative(Tc), r)
    result = {
        "b": (at(Tb, r)+tr*rb) % mod,
        "c": (at(Tc, r)+tr*rc) % mod,
        "b2": (trr*rb*rb+2*trb*rb+tr*rbb)*pow(2, -1, mod) % mod,
        "bc": (trr*rb*rc+trb*rc+trc*rb+tr*rbc) % mod,
        "c2": (trr*rc*rc+2*trc*rc+tr*rcc)*pow(2, -1, mod) % mod
    }
    return {"modulus": mod, "coefficients": result}


def exact_quotient_residue(value, divisor):
    quotient, remainder = divmod(value, divisor)
    require(remainder == 0, "Scalar quotient was not exact")
    return quotient % 17


def main():
    model = family("r")
    F, H, E = (shifted_three(model[label]) for label in ("F", "H", "E"))
    first = {label: residue(divided(poly, 17))
             for label, poly in (("F", F), ("H", H), ("E", E))}
    expected = {
        "F": {(0,0,0):3, (1,0,0):16, (0,1,0):13, (0,0,1):11},
        "H": {(0,0,0):7, (1,0,0):9, (0,1,0):11, (0,0,1):3},
        "E": {(0,0,0):7, (1,0,0):9, (0,1,0):12, (0,0,1):2}
    }
    require(first == expected, "General first jets disagree")
    # All-orders, finite polynomial identities; not just truncated series tests.
    KH = divided(sparse_add(H, sparse_scale(F, 9),
                            {(0,1,0):-17*9}), 17**2)
    KE = divided(sparse_add(E, sparse_scale(F, 9),
                            {(0,1,0):-17*10, (0,0,1):-17*16}), 17**2)
    require(sparse_at(KH,3,0,0)%17 == 5, "General second H constant")
    require(sparse_at(KE,3,0,0)%17 == 14, "General second E constant")
    r0 = hensel_root(model["F"][0])
    require(r0 % 17**3 == 4095, "Wrong general baseline root")
    require(exact_quotient_residue(at(model["H"][0],r0),17**2)==5,
            "Baseline H/17^2")
    require(exact_quotient_residue(at(model["E"][0],r0),17**2)==14,
            "Baseline E/17^2")
    general_derivatives = {
        label: implicit_derivatives(model["F"],model[label],r0)
        for label in ("H","E")}
    for label, expected_pair in (("H",(9,0)),("E",(10,16))):
        actual = general_derivatives[label]["coefficients"]
        require((actual["b"]//17%17,actual["c"]//17%17)==expected_pair,
                "Wrong first implicit derivative")
        require(all(actual[k]%17**2==0 for k in ("b2","bc","c2")),
                "Wrong quadratic implicit coefficient divisibility")
    require((-5*pow(9,-1,17))%17==7, "b/17 value")
    require((14+10*7)%17==16, "E/17^2 constant after H=0")

    # Exact G10(1): b is an integer polynomial in r.
    bp = add([comb(10,2)-1],scale(model["a3"],-comb(10,3)),
             scale(model["a4"],-comb(10,4)))
    star = {}
    for label in ("F","H","E"):
        T0,Tb,Tc = model[label]
        star[label]=(add(T0,multiply(Tb,bp)),[],Tc)
    FS,HS,ES=(shifted_three(star[label]) for label in ("F","H","E"))
    KHS = divided(sparse_add(HS,sparse_scale(FS,9)),17**2)
    KES = divided(sparse_add(ES,sparse_scale(FS,9),
                             {(0,0,1):-17*16}),17**2)
    require(sparse_at(KHS,3,0,0)%17==11, "Exact-G10 H constant")
    require(sparse_at(KES,3,0,0)%17==15, "Exact-G10 E constant")
    rs=hensel_root(star["F"][0])
    require(rs%17**3==49, "Wrong exact-G10 baseline root")
    require(exact_quotient_residue(at(star["H"][0],rs),17**2)==11,
            "Exact-G10 baseline H")
    require(exact_quotient_residue(at(star["E"][0],rs),17**2)==15,
            "Exact-G10 baseline E")
    require(exact_quotient_residue(at(bp,rs),17)==12,
            "Exact-G10 baseline b")
    star_derivatives=implicit_derivatives(star["F"],star["H"],rs)
    require(star_derivatives["coefficients"]["c"]%17**2==0,
            "Exact-G10 c derivative does not cancel to order two")
    h2_at_one = (comb(20,2)-comb(18,2)*comb(20,2)
                 +comb(17,2)*comb(20,3)*2
                 +comb(16,2)*comb(20,4)*7) % 17
    g10_derivative_at_one = (10-8*comb(10,2)
                            +7*comb(10,3)*2+6*comb(10,4)*7) % 17
    require(h2_at_one == 3 and g10_derivative_at_one == 1,
            "Near-unit root derivative constants")

    # Unit G12, with b free.  G3 witness is 1 or r.
    unit_expectations=[
        ("one","r",[[16,16],[0,1]],(0,0),8),
        ("r","r",[[16,16],[9,1]],(0,0),8),
        ("r","one",[[16,1],[9,0]],(8,0),15)]
    unit_reports=[]
    for g3,g12,jacobian,solution,e_residue in unit_expectations:
        source=family(g3)
        if g12=="r":
            c0=add(mono(12,-1),mono(10,comb(12,2)),
                   scale(shift(source["a3"],9),-comb(12,3)),
                   scale(shift(source["a4"],8),-comb(12,4)))
            cb=mono(2,-comb(12,10))
        else:
            c0=add([comb(12,2)-1],
                   scale(source["a3"],-comb(12,3)),
                   scale(source["a4"],-comb(12,4)))
            cb=[-comb(12,10)]
        shifts={}
        for label in ("F","H","E"):
            T0,Tb,Tc=source[label]
            parts=(add(T0,multiply(Tc,c0)),
                   add(Tb,multiply(Tc,cb)),[])
            shifts[label]=divided(shifted_three(parts),17)
        rf,rh=(residue(shifts[label]) for label in ("F","H"))
        allowed={(0,0,0),(1,0,0),(0,1,0)}
        require(set(rf)<=allowed and set(rh)<=allowed,"Unit jets not affine")
        matrix=[[poly.get((1,0,0),0),poly.get((0,1,0),0)] for poly in (rf,rh)]
        require(matrix==jacobian,"Wrong unit-G12 Jacobian")
        constant=[poly.get((0,0,0),0) for poly in (rf,rh)]
        determinant=(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])%17
        require(determinant!=0,"Singular unit-G12 Jacobian")
        require(all((constant[i]+matrix[i][0]*solution[0]
                     +matrix[i][1]*solution[1])%17==0 for i in range(2)),
                "Wrong unit-G12 residue solution")
        require(sparse_at(shifts["E"],*solution,0)%17==e_residue,
                "Wrong unit-G12 E/17 residue")
        unit_reports.append({"G3Witness":g3,"G12Witness":g12,
                             "jacobian":matrix,"constant":constant,
                             "uniqueSolution_t_b":list(solution),
                             "determinant":determinant,"Ediv17":e_residue})

    # A mutation in the exact all-orders polynomial relation must fail.
    bad=sparse_add(H,sparse_scale(F,9),{(0,1,0):-17*9,(0,0,0):1})
    rejected=False
    try:
        divided(bad,17**2)
    except ValueError:
        rejected=True
    require(rejected,"Polynomial-identity mutation was accepted")
    print(json.dumps({
        "status":"PASS",
        "firstDividedJets":{label:serial(poly) for label,poly in first.items()},
        "generalBaseline":{"rModulo17cubed":r0%17**3,
                           "Hdiv17squared":5,"Ediv17squared":14},
        "generalImplicitDerivatives":general_derivatives,
        "allOrdersIdentities":{
            "H":"H+9F-153b=17^2*KH(t,b,c)",
            "E":"E+9F-17(10b+16c)=17^2*KE(t,b,c)",
            "KH":serial(KH),"KE":serial(KE),
            "KH_at_3_0_0_mod17":5,"KE_at_3_0_0_mod17":14},
        "exactG10Baseline":{"rModulo17cubed":rs%17**3,
                            "Hdiv17squared":11,"Ediv17squared":15,"bdiv17":12},
        "exactG10ImplicitDerivatives":star_derivatives,
        "nearUnitRootDerivativeConstants":{
            "Hasse2_f_at_1_mod17":h2_at_one,
            "G10prime_at_1_mod17":g10_derivative_at_one},
        "exactG10AllOrdersIdentities":{
            "H":"Hstar+9Fstar=17^2*KHS(t,c)",
            "E":"Estar+9Fstar-272c=17^2*KES(t,c)",
            "KHS":serial(KHS),"KES":serial(KES),
            "KHS_at_3_0_mod17":11,"KES_at_3_0_mod17":15},
        "unitG12":unit_reports,
        "negativeControlRejected":rejected,
        "scope":"Exact constants, unit derivative calculations, and integral "
                "polynomial identities. Root valuation consequences require "
                "the hypotheses stated in the accompanying note."
    },indent=2))


if __name__=="__main__":
    main()
