# Family A: both proposed closed masks admit exact counterexamples

23 September 2026. Bounded research result; no publication or novelty claim.

This note records the initial failed mask-exclusion route. The subsequent forced-collision argument in `A_EXCLUSION_PROOF.md` excludes the characteristic-zero family despite these reduced examples.

The degree-20 characteristic-zero family under study has deficiencies

    {3,4,10,18,19},

so its nonleading monomials have degrees 17,16,10,2,1. At both 11 and 13, the coefficient with deficiency 10 disappears under the usual integral binomial-normalized valuation reduction. The proposed closed reduced mask is

    h=X^20+aX^17+bX^16+cX^2+dX.

**This mask cannot be excluded in either characteristic.** There are direct counterexamples over the prime fields. In characteristic 13 there is a counterexample with all four displayed coefficients nonzero, so requiring nonzero support does not rescue that mask either.

## Characteristic 13: an interior example

Take

    h=X^20+4X^17+X^16+4X^2+3X  over F_13.

Its only Hasse derivative orders with nonzero value at zero are 17,16,2,1. Direct binomial-coefficient calculation gives

    H17=9X^3+4,
    H16=9X^4+3X+1,
    H2 =8X^18+11X^15+3X^14+4,
    H1 =7X^19+3X^16+3X^15+8X+3.

The root 1 is common to h and each of H17,H16,H2:

    h(1)=13, H17(1)=13, H16(1)=13, H2(1)=26,

all zero modulo 13. The root 7 is common to h and H1. Modulo 13,

    7^2=10, 7^4=9, 7^5=11, 7^7=6, 7^8=3;

using exponent reduction modulo 12 for nonzero field elements gives

    h(7)=3+4*11+9+4*10+3*7=117=0,
    H1(7)=7*6+3*9+3*5+8*7+3=143=0.

Every other required derivative shares the root zero with h because its constant coefficient vanishes. This verifies the entire CA property, not merely a selected subset of derivative conditions. Since h(0)=0 and h!=X^20, it is not a monic pure 20th power.

## Characteristic 11: a boundary example

Take

    h=X^20+4X^17+5X^2+X  over F_11.

The active Hasse derivatives are

    H17=7X^3+4,
    H2 =3X^18+5X^15+5,
    H1 =9X^19+2X^16+10X+1.

The root 1 is common to h,H17,H1. The root 5 is common to h,H2: since 5 has multiplicative order 5 modulo 11,

    h(5)=1+4*3+5*3+5=33=0,
    H2(5)=3*4+5*1+5=22=0.

All remaining derivative orders use zero. Again this is a nontrivial CA polynomial. The coefficient b vanishes, which is allowed and must be covered by any closed-mask argument. Valuation reduction may erase an originally nonzero characteristic-zero coefficient, so this boundary cannot be dismissed merely because the original support has five nonzero coefficients.

## Exact search and checks

The quick search normalized a highest active Hasse common root to 1. In the a!=0 branch this fixes

    a=-binom(20,17)=4 modulo either prime,
    d=-1-a-b-c.

It then enumerated prime-field b,c. The lower-dimensional a=0 branches were normalized similarly. Each candidate was tested by exact univariate gcds between h and its active Hasse derivatives. This found the displayed examples immediately. The search also found three further characteristic-11 examples, retained in `quick-fp-search.json`.

An absence in that finite search would not prove absence with algebraic-closure coefficients. Here only its exact positive examples are used. `check_mask_counterexamples.py` is a separate direct checker: it evaluates all 19 Hasse conditions from the defining formula, checks nontriviality, and runs a coefficient-corruption control. Normal and optimized Python runs pass without CAS dependencies.

## Consequence for the campaign and reusable limitation

These examples obstruct the proposed characteristic-11 and characteristic-13 **closed-mask exclusion**. They say nothing against the Casas–Alvero conjecture in characteristic zero. A different prime, a condition retaining more information about the original coefficients, or a direct characteristic-zero argument would be needed for Family A.

The obstruction persists through Frobenius powers: if q=p^e and h is either example, then h(X^q) has the CA property in characteristic p. Derivatives of order not divisible by q vanish identically, and

    H_(qk)(h(X^q))=(H_k h)(X^q).

The exhibited common roots have qth roots in the algebraic closure, so all divisible-order conditions also hold. Consequently a support-mask strategy that only repeats either failed seed by Frobenius cannot remove the issue at higher degrees.

No Gröbner unit-ideal computation is appropriate for these closed masks: the explicit marked roots already exhibit points of their CA loci. No claimed all-coefficient degeneration exclusion was obtained, and no full degree-20 result follows.
