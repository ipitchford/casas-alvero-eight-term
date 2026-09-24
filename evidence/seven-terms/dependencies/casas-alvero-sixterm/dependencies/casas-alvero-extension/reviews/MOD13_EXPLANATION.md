# Compact elimination for the remaining five-term family at 13

23 September 2026. Internal derivation, not publication or external review. This note proves emptiness of the **reduced characteristic-13 system** and, after checking every coefficient degeneration, excludes the entire reduced sparse family except the pure power. A separate characteristic-zero specialization proof and any desired support enumeration are still necessary for a characteristic-zero conclusion.

## Reduced system and scope

The root agent's normalized support {4,10,17,19} corresponds to

    f=X^20+aX^16+bX^10+cX^3+dX.

At the prime 13, normalization of a common root with H16 to 1 gives a=4. The H10 equation gives b=0 independently of its marked root. The remaining coefficients are

    c=4v^17-4v^13,
    d=6w^19+w^15-3c*w^2.

The unsaturated root equations retained by the root computation are

    E1=5+c+d=0,
    Ev=v^19+4v^15+c*v^2+d=5v^19+d=0,
    Ew=w^19+4w^15+c*w^2+d=0.

Everything below takes place in an algebraic closure of F13. No rational-point enumeration is used, and no distinctness of the marked roots is imposed.

## 1. A nineteenth-power ratio

The first two equations give

    d=-5v^19,
    F(v):=5v^19-4v^17+4v^13-5=0.

In particular v != 0. Let

    P(X)=X^19+4X^15+cX^2+d,

so f=XP. The definition of d is exactly f'(w)=0. Since P(w)=0 as well,

    3P(w)-f'(w)=9w^19+2d=9w^19+3v^19=0.

Therefore w^19=4v^19. Set t=w/v. Then

    M(t):=t^19-4=0.

In particular w is also nonzero. Substitution in P(w)=0 and division by v^15 give

    (4t^2-1)v^4+4(t^15-t^2)=0.

Set

    D=4t^2-1,   N=4(t^2-t^15).

The polynomial D does not vanish at a root of M. Its two roots are 6 and 7 in F13, and 6^19=7, 7^19=6, neither of which is 4. Hence

    T:=v^4=N/D.

This denominator check handles all roots of M over the algebraic closure, because the quadratic already splits over F13.

## 2. A quartic eliminated by two squarings

Using v^4=T, the equation F(v)=0 reduces to

    A*v^3+B*v=5,
    A=5T^4,   B=4T^3(1-T).

Squaring once gives

    (A^2*T+B^2)v^2=25-2ABT.

In characteristic 13 this is

    T^6(-T^3+3T^2-6T+3)v^2=T^9-T^8-1.

Squaring again and using (v^2)^2=T yields the necessary equation

    R(T)=(T^9-T^8-1)^2-T^13(-T^3+3T^2-6T+3)^2=0.

No division by A, B, T, or the cubic expression has occurred, so the zero cases of those expressions are retained. Expanding gives only ten terms:

    R(T)=-T^19-6T^18+3T^17+4T^16-2T^15-3T^14
         +4T^13-2T^9+2T^8+1.

The squarings may introduce extraneous solutions; that is harmless for this necessary-condition exclusion.

## 3. The final small univariate obstruction

Let H(t) be the remainder of D^19 R(N/D) modulo M(t)=t^19-4. Exact polynomial arithmetic in F13[t] gives

    H(t)=5t^18-6t^17-3t^16+3t^15-2t^14-6t^13
         +t^11+3t^10-t^8+t^7-t^6+3t^5+6t^4
         +5t^3-4t^2+6.

The accompanying standard-library checker reconstructs this remainder directly from N,D,R; it does not trust a Gröbner-basis or resultant output. The hypothetical ratio must satisfy both M(t)=0 and H(t)=0.

We need only three simple facts about H: its leading coefficient is 5, its t^16 coefficient is -3=10 in F13, and H(4)=8.

First,

    M(t)=(t-4)Q(t),
    Q(t)=sum_{k=0}^{18}4^k*t^(18-k).

The polynomial Q is irreducible over F13. Indeed, write t=4*zeta. Its roots correspond to nontrivial nineteenth roots of unity. Since 19 is prime, these are primitive. Their Frobenius orbit has length ord_19(13)=18: Fermat gives order dividing 18, while 13^6=11 and 13^9=-1 modulo 19 rule out every proper divisor of 18. Thus each primitive root has degree 18 and Q is its minimal polynomial up to the indicated scalar change.

Now H(4)=8 rules out the linear factor t-4. If H and Q shared a root, irreducibility and their equal degree 18 would force H=5Q. But the t^16 coefficient of 5Q is 5*4^2=2 modulo 13, whereas that coefficient of H is 10. Contradiction.

Hence M and H have no common root, and the original reduced system has no solution over the algebraic closure of F13.

## 4. All coefficient degenerations: a characteristic-13 lemma

**Lemma.** Over an algebraically closed field of characteristic 13, if

    h(X)=X^20+aX^16+cX^3+dX

satisfies all Hasse-derivative Casas–Alvero common-root conditions, then h=X^20.

First suppose a != 0. The derivative H16(h)=9X^4+a has nonzero constant term. Choose a common root r != 0 and scale X by r to make it 1. Then a=4. If c != 0, every common root v with H3(h) is nonzero. If c=0, the root 1 is itself a common root with H3, since H3(h)(1)=9+4=0, so choose v=1. Therefore in both cases a nonzero marked root v exists. The preceding proof applies unchanged to every value of c and d, including zero. It excludes this entire case.

Now suppose a=0 and c != 0. Choose a common root with H3 and scale it to 1. Since H3(h)=9X^17+c, we have c=4, and h(1)=0 gives d=-5. Any common root w with H1 is nonzero because d != 0. The root equation divided by w and the derivative equation are

    w^19+4w^2-5=0,
    7w^19+12w^2-5=0.

Their linear combination gives w^19=4, and substitution gives w^2=10. But the roots of X^2-10 are 6 and 7 in F13, whose nineteenth powers are 7 and 6 respectively. Contradiction.

Finally suppose a=c=0 and d != 0. A common root w of h and H1(h) is nonzero. The equations w^19+d=0 and 7w^19+d=0 contradict one another because 6 != 0. The remaining case is a=c=d=0, namely h=X^20. QED.

This case analysis is essential for a valuation specialization: it is not legitimate to assume that a nonzero characteristic-zero coefficient stays nonzero in the residue field.

## 5. What this explains, and what it does not

The modular collapse is driven by three arithmetic features:

1. Both binomial contributions to the X^10 coefficient vanish modulo 13, leaving a four-term reduction.
2. The exponent differences 16-3 and the characteristic are both 13, which makes the linear combinations of the root and derivative equations cancel the middle terms.
3. The remaining exponent 19 is prime and 13 has order 18 modulo 19, so the final ratio equation has only a linear factor and one irreducible factor of degree 18. A very small remainder certificate excludes both.

These are reusable elimination tactics for sparse CA systems with an exponent gap equal to the characteristic. They do not yet constitute a classification of an infinite family: the last remainder and coprimality calculation are specific to the displayed constants and exponents.

The proof replaces a large ideal-membership certificate by a ten-term univariate polynomial and one explicit degree-18 remainder. It does **not** alone justify lifting from characteristic 13 to characteristic zero; that still requires a separate finite-module, valuation, or projective specialization argument. It does not assert that 13 is a good prime for all degree-20 CA polynomials. No historical priority claim is made.
