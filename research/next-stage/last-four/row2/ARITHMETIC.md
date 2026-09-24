# Independent exact arithmetic for the row-2 exclusion

24 September 2026. Result: **PASS for the finite identities and exhaustive residue arithmetic used in ROW2_PROOF.md.** No arithmetic correction to the proposed proof was needed. The adjacent checker is an independent reconstruction from binomial coefficients and elementary polynomial operations; it does not import a producer module or a computer-algebra library.

The mathematical proof of valuation bounds, separated-cluster coverage and arbitrary-ramification transfer remains a separate obligation. This arithmetic report does not substitute a finite unramified search for that argument.

## 1. Reconstruction of the normalized family

The checker constructs

f=X^20-190X^18+binom(20,4)aX^16+binom(20,10)bX^10+DX^3+FX^2+EX

by solving H3 f(1)=T for D and then f(1)=0 for E. It recovers exactly

D=153900-2713200a-22170720b+T,
E=189-4845a-184756b-D-F.

For f(1+Y)=sum c_kY^k, direct binomial expansion gives

c1=304589-5353725a-42678636b+2T+F,
c2=432820-7558200a-58198140b+3T+F,
c3=T,
c4=-576555+8817900a+38798760b,
c17=-2280, c18=0, c19=20, c20=1.

All coefficients of each c_k, for 4<=k<=16, are divisible by 17 as integer polynomials in a,b,T,F. Thus their membership in 17O is a coefficientwise statement, valid in ramified extensions. The coefficient at order nineteen in H2 is binom(19,2)=171, which is congruent to 1 modulo 17 and must not be omitted.

The exact cancellation identity is

c2-c1-T=17(7543-129675a-912912b).                         (A1)

At a=9,b=-47628, the bracket in (A1) is 43479013204 and has valuation one. The whole right side has valuation exactly two, with residue 8 after division by 17^2. This distinguishes the precision of the bracket from that of c2-c1-T. Combined with nu(a-9)>=2 and nu(b+47628)>=1 from the proof, (A1) indeed gives c2-c1-T in 17^2O.

## 2. Complete residue witness coverage

Let s^2=3 over F17. The element 3 is a nonsquare, so F17[s] is the quadratic field, with multiplication

(A+Bs)(C+Ds)=(AC+3BD)+(AD+BC)s.

The seed factors as

h=(X-1)^17 X(X^2-3).

Its four distinct root locations over the algebraic closure are therefore exactly 0,1,s,-s. The checker verifies the factorization and evaluates all three low Hasse derivatives at all four locations. The common locations are

| Derivative | Locations shared with h |
| --- | --- |
| H1 | 1 |
| H2 | 0,1 |
| H3 | 1 |
| G2=X^2-1 | 1 |

The roots 0,s,-s are simple. In the exact-support application, a4,a10 and F are nonzero. Consequently an active G4/G10 or H2 witness cannot be the unique actual root in residue class zero, which is the exact root zero. This is the explicit mathematical reason for restricting the two middle witnesses to 1,s,-s.

The checker enumerates all nine independent choices of these two locations. The resulting normalized coefficient pairs and divided residues are exactly

| a mod17 | b mod17 | 7543-129675a-912912b mod17 |
| ---: | ---: | ---: |
| 5 | 14 | 2 |
| 5 | 8 | 6 |
| 9 | 7 | 5 |
| 9 | 6 | 0 |

Thus the initial divided condition leaves four markings, corresponding to independent choices of sign for the G4 and G10 outside witnesses. No equality of the two signs is assumed.

At such an outside root r, G4 gives the exact identity

a=9-(r^2-3)^2.

At a=9 and r0^2=3, the nonconstant part of G10 is exactly 47628, explaining the reference value b=-47628. The shifted coefficient c4 has divided residue 8 at (a,b)=(9,6).

## 3. Leading-model ratio exclusion

For the leading model -2Y^17+kappa Y^4+lambda2Y^2+lambda1Y, the wild term contributes zero to its first three Hasse derivatives in characteristic seventeen. The surviving H2 and H3 terms are 6kappa Y^2+lambda2 and 4kappa Y.

The lambda2-nonzero case of the argument produces

rho^2=1/3=6, rho^13=5.

This has no solution over the algebraic closure. The checker performs exact polynomial division over F17:

(T^13-5) mod (T^2-6)=8T+12,
(T^2-6) mod (8T+12)=9.

The final remainder is a nonzero constant. Equivalently, rho^13=8rho forces rho=7, whose square is 15 rather than 6. These are geometric polynomial identities, not an enumeration confined to the prime field.

## 4. Quartic good-characteristic calculation

The relevant normalized quartic is q=X^4-6X^2+5X. The checker computes the determinant of its 7-by-7 Sylvester matrix with q' using fraction-free integer elimination. The resulting discriminant is exactly

4725 = 25*189, congruent to 16 modulo 17.

It is nonzero. The factor calculation q=X(X^3-6X+5), together with the cubic discriminant 189 and its constant coefficient 5, provides a second hand calculation of the same value. This verifies the numerical input to the proof's degree-four cluster-collapse lemma; the lemma itself is not certified merely by this determinant.

## 5. Final exact family and lift obstruction

After the proof establishes c1=c2=T=0, the checker substitutes

B=(7543-129675*9)/912912=-1387/1092,
F=5353725*9+42678636B-304589=-6329185.

The denominator is a 17-adic unit. It directly verifies that the reconstructed f has c1=c2=c3=0. Polynomial evaluation in Q[r0]/(r0^2-3), followed by reduction modulo 289, gives

f(r0)=170r0,
f'(r0)=130+283r0,
G10(r0)=204,
G10'(r0)=92r0.

The same quotient-algebra identities hold for both signs. Writing the actual outside root as r=r0+17h, the divided f equation therefore gives

0=10r0+11(r0+1)h.

Substitution into the divided G10 equation gives precisely

12+7r0h=(12r0-4)/(r0+1).

The denominator is nonzero because r0^2=3. Vanishing of the numerator would force r0=6, but 6^2=2 in F17, not 3. The checker also evaluates both signs in the quadratic field and records the nonzero values. Therefore the displayed finite residual obstruction covers all four combinations of G4/G10 signs, provided the proof's stated precision bounds hold.

## 6. Reproduction and limits

Run from this directory:

    python3 check_row2.py
    python3 -O check_row2.py

The saved verification.json and verification-optimized.json agree byte for byte. The checker uses explicit failure exceptions rather than assertions. It verifies coefficientwise divisibility, all visible-root incidences, the complete nine-marking sieve, the exact geometric Euclidean exclusion, the quartic discriminant, and the final quotient-ring identities. A deliberately altered final coefficient 170 to 171 is rejected as a negative control.

This is an independent finite-arithmetic certification. It does not by itself prove the preliminary divisibility T,F in 17O, the successive displacement bounds, the exact quartic-cluster collapse, or the characteristic-zero case cover. Those are assigned to the separate argument auditor. No arithmetic inconsistency with the proposed proof was found.
