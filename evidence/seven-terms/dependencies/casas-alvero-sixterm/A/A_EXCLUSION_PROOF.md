# Excluding Family A by a forced collision of derivative witnesses

23 September 2026. Research candidate with exact internal certificates; external review and novelty assessment remain separate.

**Claim.** A monic characteristic-zero degree-20 Casas–Alvero polynomial with a root at zero and support contained in

    {20,17,16,10,2,1}

must be X^20. In particular, the six-term support with deficiencies {3,4,10,18,19} is excluded.

This conclusion does not follow from emptiness of a reduced coefficient mask: that mask has a nontrivial characteristic-13 point. The proof instead uses the simplicity of one of its roots to force exact equality of three characteristic-zero witnesses.

## 1. Complete classification of the reduced characteristic-13 seed

Let K be any algebraically closed field of characteristic13 and

    h=X^20+aX^17+bX^16+cX^2+dX.

The only potentially active Hasse orders at zero are 17,16,2,1. Their formulas are

    H17=9X^3+a,
    H16=9X^4+4aX+b,
    H2=8X^18+6aX^15+3bX^14+c,
    H1=7X^19+4aX^16+3bX^15+2cX+d.

### The a=0 cases

If b!=0, normalize a common root of h,H16 to 1. This gives b=4 and d=-5-c. For a common H2 root v, set

    c=-8v^18-12v^14,    d=-5-c.

In F13[w,v], form the ordinary ideal

    I0=(h(v),h(w),7w^19+12w^15+2cw+d).

The exact certificate `seed13-a-zero-certificate.txt` expresses 1 in I0. `check_seed_certificates.py zero` reconstructs these original equations and verifies the identity by sparse polynomial multiplication. No saturation or nonzero-coefficient assumption on c or d is used. Thus the b!=0 case is impossible.

If a=b=0,c!=0, normalize an H2 common root to 1, obtaining c=5,d=7. A common H1 root w is nonzero because d!=0. Put P=h/X=X^19+5X+7. Then H1-7P=X+10, so w=3, but P(3)=12, a contradiction. If a=b=c=0,d!=0, subtracting seven times h/X from H1 gives -6d!=0, again a contradiction. The remaining case is X^20.

### The a!=0 case

Normalize an H17 common root to 1. Then a=4 and d=-5-b-c. Put

    P=h/X=X^19+4X^16+bX^15+cX+d.

When c!=0, an H2 common root is nonzero, so Res_X(P,H2)=0. When c=0 its active condition is automatic at zero. Consequently the necessary condition valid in both cases is

    c*Res_X(P,H2)=0.

The analogous condition for H1 is d*Res_X(P,H1)=0. These multiplied resultants retain every coefficient degeneration.

The resultant computations split into three one-parameter cases:

1. If b=0, use c as parameter and d=-5-c. The gcd of the two multiplied resultants is 1 in F13[c], excluding this case.
2. If a marked H16 common root u equals 1, H16(1)=0 gives b=1. Using c as parameter and d=-6-c, the resultant gcd is c-4. Thus c=4,d=3.
3. If b!=0 and u!=1, then u!=0 and H16(u)=0 gives b=4u^4-3u. The equation P(u)=0 gives

       c=(5+b-5u^19-u^16)/(u-1),    d=-5-b-c.

   The numerator is divisible by u-1 as a polynomial, so c is a polynomial of degree18. The two multiplied resultant polynomials have degrees360 and378, and their gcd is1. This excludes every u!=0,1. The computation includes possible c=0 and d=0.

The exact resultant polynomials are saved in `seed13-univariate.txt`. The standard-library checker `check_seed_univariate.py` verifies their identities independently through Sylvester determinants over F13[t]/(t^3-2), at more distinct points than the degree bounds. The cubic is irreducible because2 is not a cube in F13. The respective parameter-degree bounds are 38,39 in the first two cases and684,702 in the third; these follow directly from the Sylvester matrix sizes37,38, the maximum entry degrees1 or18, and the extra coefficient factor. The checker then verifies all three polynomial gcds.

Therefore the only normalized nonmonomial seed is

    h0=X^20+4X^17+X^16+4X^2+3X.

Exact univariate gcds give

    gcd(h0,H17)=gcd(h0,H16)=gcd(h0,H2)=X-1,
    gcd(h0,H1)=X-7.

Moreover h0'(1)=11!=0 in F13. The direct witnesses establishing that h0 is CA are retained in `check_mask_counterexamples.py`; the nontrivial seed really exists.

## 2. Valuation reduction and exact witness collision

Suppose f is a nonmonomial characteristic-zero CA polynomial with the specified support. Extend a 13-adic valuation to a field containing its coefficients and roots. Scale a nonzero root of minimum valuation to 1. All roots are integral, and a unit root remains.

Write f=sum_j binom(20,j)*a_j*X^(20-j), with a0=1 and a20=0. Each a_j is integral by induction: at an integral common root beta of f and its derivative of order20-j, the monic normalized derivative equation is

    sum_(i=0)^j binom(j,i)*a_i*beta^(j-i)=0.

This expresses a_j using earlier integral coefficients. Since13 divides binom(20,10), the X10 coefficient disappears under reduction. Thus the reduction is a seed from Section1; it is nonmonomial because the unit root remains a root.

Section1 excludes all reduced a=0 cases. Hence the ordinary X17 coefficient is a unit. The H17 equation is1140*X^3+A17; since1140 is also a13-adic unit, any H17 common root is a unit. Scale one such root to1. This second scaling preserves integrality and the unit-root condition. The normalized reduction is exactly h0.

Let r16,r2 be characteristic-zero common roots with H16,H2. They are integral, and their reductions are1 by the gcd statements in Section1. Both f(r16) and f(1) vanish. The divided difference

    (f(r16)-f(1))/(r16-1)

is interpreted as the polynomial divided difference, whose reduction at r16=1 is h0'(1)=11, a unit. Since the product of this unit with r16-1 is zero in a field, r16=1. The same argument gives r2=1.

This argument needs no unramified assumption, discrete valuation, completeness, or lifting theorem. It is a direct divided-difference identity in the valuation ring.

## 3. The resulting characteristic-zero one-parameter family

Write the ordinary X10 coefficient as e. The exact equations H17(1)=H16(1)=H2(1)=f(1)=0 give

    A17=-1140,
    B16=14535,
    C2=-1589350-45e,
    D1=1575954+44e.

Put

    Q=f/X=X^19-1140X^16+14535X^15+eX^9+C2*X+D1,
    H10=184756X^10-22170720X^7+116396280X^6+e,
    H1=20X^19-19380X^16+232560X^15+10eX^9+2C2*X+D1.

Define R10(e)=Res_X(Q,H10) and R1(e)=Res_X(Q,H1). They have degrees19 and28. Their reductions modulo101 retain those degrees and are coprime. Therefore they are coprime over Q as well.

If e!=0, every common H10 root is nonzero and supplies R10(e)=0. The H1 condition always supplies R1(e)=0: a nonzero common root is a root of Q, while a zero common root forces D1=0, which makes Q(0)=H1(0)=0. This contradicts coprimality.

If e=0, the H10 condition can be automatic at zero, but R1(0)!=0, again impossible. Thus this proof also covers the X10-coefficient degeneration and establishes the claim for the whole closed support, not only six nonzero terms.

The exact integer resultant polynomials are retained in `collision-resultants.log`. `check_collision_resultants.py` independently verifies each resultant identity using30 and39 exact integer Sylvester determinants: the parameter-degree bounds29 and38 follow because each matrix entry is affine in e. It then checks the degrees, leading coefficients modulo101, modular gcd1, and R1(0)!=0. This check uses only integer arithmetic and proves the asserted rational coprimality without trusting a CAS gcd output.

## Scope and proof status

This excludes one specified support family. It does not alone establish a seven-term lower bound in degree20, and it does not solve the unrestricted conjecture. The reusable step is that a nonempty reduced CA locus can still be useful when it forces derivative witnesses to reduce to the same simple root; the divided-difference identity then forces their exact characteristic-zero collision.

The earlier failed closed-mask exclusion remains documented in `A_RESEARCH_NOTE.md`. Multivariate Gröbner computations suggested the seed classification, but their transformation-matrix extraction exceeded the bounded runtime. The proof above uses independently checked univariate resultants instead; it does not depend on those incomplete transformation attempts.
