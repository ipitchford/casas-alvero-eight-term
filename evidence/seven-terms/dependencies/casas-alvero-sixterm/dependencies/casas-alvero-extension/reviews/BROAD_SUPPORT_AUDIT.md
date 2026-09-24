# Audit of an infinite-family coefficient restriction

Date: 23 September 2026. Status: **PASS for the theorem and proof below**, conditional only on the independently replayed finite-field polynomial identity recorded here. The argument is independent of Ghosh's proposed proof and requires no finiteness or properness inference from an empty affine special fiber. Historical novelty and publication significance are separate questions.

## Exact theorem

Let e>=0, q=13^e, and N=20q. Let f in C[X] be a degree-N polynomial which is not a power of a linear polynomial up to a nonzero scalar, and suppose f shares a root with every derivative of orders 1,...,N-1. For **every root alpha of f**, at least one coefficient of

    f(alpha+X)

at exponent N-qj is nonzero, where

    J={1,2,3,5,6,7,13,14,15,16,18}.

Equivalently, for every root alpha, at least one Hasse derivative

    D^[q(20-j)]f(alpha), j in J,

is nonzero. Over characteristic zero this is equivalent to the corresponding ordinary derivative being nonzero.

The coefficient index qj is the **deficiency from degree N**, not the exponent of the monomial. This distinction matters in stating and implementing the result.

For e=0, if alpha is the center of mass, its deficiency-one coefficient is already zero. Hence the centered nonleading support must meet

    {2,3,5,6,7,13,14,15,16,18}.

In particular no nontrivial centered degree-20 CA polynomial has support contained in

    {0,4,8,9,10,11,12,17,19}

when index zero denotes the leading term. This excludes the entire nine-term ambient family

    X^20+a_4 X^16+a_8 X^12+a_9 X^11+a_10 X^10
        +a_11 X^9+a_12 X^8+a_17 X^3+a_19 X,

including every coefficient degeneration. It is a support restriction, not an assertion that all CA counterexamples require ten terms, and not a proof of the full conjecture in any unresolved degree.

## 1. The characteristic-13 base lemma, including all missing coefficients

Over an algebraically closed field k of characteristic 13, there is no polynomial

    h=X^20+A X^16+C X^3+D X

which has a nonzero root and shares a root with every nonconstant Hasse derivative. In fact only the Hasse derivatives of orders 16,3,1 need to be considered; all the other required conditions are automatically satisfied at zero.

### Case A is nonzero

A common root of h and D^[16]h is nonzero, because D^[16]h=9X^4+A. Scale it to 1 and keep h monic. Then A=4 and h(1)=0.

Choose a common root v for derivative order 3. If C is nonzero, v is necessarily nonzero. If C=0, h(1)=0 gives D=8, and

    D^[3]h(1)=binom(20,3)+4binom(16,3)=9+4=0;

therefore choose v=1. This last check is essential: taking v=0 would not generally justify the equation h(v)/v=0.

Choose a common root w for derivative order 1. If D is nonzero, w is necessarily nonzero. If D=0, take w=0; in this case the polynomial h(X)/X also vanishes at zero, so its evaluation at w is legitimately zero.

The derivative equations then give

    C=4v^17-4v^13,
    D=6w^19+w^15-3Cw^2.

The three remaining polynomial root conditions are E_1=E_v=E_w=0, where

    E_1=v^17w^2+4v^17-v^13w^2-4v^13+6w^19+w^15+5,
    E_v=5v^19+v^17w^2-v^13w^2+6w^19+w^15,
    E_w=5v^17w^2-5v^13w^2+7w^19+5w^15.

The exact certificate in `../root-mod13/certificate.txt` satisfies

    C_1 E_1+C_2 E_v+C_3 E_w=1 in F_13[v,w].

It was independently replayed by `replay_mod13.py`, which reconstructs the input equations from integer Hasse binomial coefficients and multiplies the exported polynomials using only the Python standard library. Normal and optimized runs both pass. Certificate SHA-256:

    23552e44cc926d21e48b0e57e2022d309b91c34df265292a8dc753f61cd000d9.

The multiplier term counts are 481,649,647. The identity excludes roots over every characteristic-13 extension, not only F_13 itself. This case therefore covers A nonzero with C or D equal to zero, as well as the exact three-coefficient support. Coincident witnesses are allowed.

The shorter alternative in `../explanation/MOD13_EXPLANATION.md` was also independently checked. Its deductions d=-5v^19, w^19=4v^19, and (4t^2-1)v^4=4(t^2-t^15), t=w/v, are correct. The denominator has only roots 6,7, neither solving t^19=4. Both squarings introducing the necessary polynomial R(T) use no further divisions. An independent SymPy expansion/remainder computation reproduces the full printed R and H, with H(4)=8, leading coefficient 5, coefficient of t^16 equal to 10, and gcd(H,t^19-4)=1. The cyclotomic proof of that gcd is valid: ord_19(13)=18 since 13^6=11 and 13^9=-1 modulo 19, so the non-linear factor of t^19-4 is irreducible of degree 18. The incompatible coefficients rule out a shared root. Thus the broad transfer can cite the shorter arithmetic proof instead of the large membership identity.

### Case A=0 and C is nonzero

Here D^[3]h=9X^17+C, so its common root with h is nonzero. Normalize it to 1. Then C=4 and h(1)=0 gives D=8.

A common root w of h and its first derivative is nonzero, because D=8. Dividing h(w)=0 by w gives

    w^19+4w^2+8=0,
    7w^19+12w^2+8=0.

Subtract seven times the first equation from the second. In characteristic 13 this gives 10w^2+4=0, hence w^2=10. The first equation gives w^19=4. But

    w^19=w(w^2)^9=w*10^9=-w,

since 10^3=-1 in F_13. Thus w=9, whereas 9^2=3 is not 10. This contradiction holds over every extension field.

### Case A=C=0

If D=0, h=X^20 has no nonzero root, contrary to hypothesis. If D is nonzero, a common root with the first derivative would be nonzero and satisfy w^19=-D and 7w^19+D=0. This implies -6D=0, impossible in characteristic 13.

These cases exhaust all coefficients. Thus the base lemma is proved with no nonvanishing assumption left on A,C,D.

## 2. Valuation normalization at an arbitrary chosen root

Suppose the theorem is false for some f and chosen root alpha. Translate alpha to zero and make f monic. This preserves the CA property. Fix a valuation extending the 13-adic valuation to a field containing the coefficients and all roots. Such a valuation is the standard setup used in [CLO, Section 3](https://arxiv.org/html/1208.5404v1#S3); only valuation-ring integrality is used here, not discreteness or completeness.

Because f is nontrivial and zero is a root, another root is nonzero. Choose a nonzero root beta with minimal valuation among the finitely many nonzero roots and replace f(X) by beta^(-N)f(beta X). All roots now lie in the valuation ring O, and 1 remains a root. This scaling preserves the zero pattern of the coefficients in the theorem. The residue field has characteristic 13.

Write the normalized polynomial as

    f=X^N+sum_{i=1}^{N-1} binom(N,i)a_i X^(N-i),

with a_0=1 and constant coefficient zero. All a_i are integral. To see this, for each j=1,...,N-1, divide the Hasse derivative of order N-j by the nonzero characteristic-zero scalar binom(N,j). The resulting monic polynomial is

    X^j+sum_{i=1}^j binom(j,i)a_i X^(j-i).

At a common root with f, every previously known term is integral because the root is integral. Induction therefore expresses a_j as an integral sum. Divisibility of binom(N,j) by 13 causes no problem: the displayed polynomial identity is used over characteristic zero, and its normalized coefficients are proved integral by induction before any reduction.

This step is stronger than merely knowing that the ordinary coefficients of f are integral; it controls the otherwise dangerous denominators in the binomial normalization.

## 3. Lucas support calculation

Since q=13^e, the base-13 digits of N=20q are the digits (1,7) shifted e places. Lucas' binomial congruence gives

    binom(N,i) nonzero modulo 13

only if i=qj with

    j in {0,1,2,3,4,5,6,7,13,14,15,16,17,18,19,20}.

All other ordinary coefficients vanish upon reduction because their binomial factors are divisible by 13 and their normalized factors a_i are integral.

The contradiction hypothesis says that the coefficients at indices qj vanish identically for every j in J. Since binom(N,qj) is a nonzero integer, the corresponding a_(qj) are zero as well. The leading coefficient is one and the constant coefficient is zero. Thus the residue polynomial has exactly the form

    fbar(X)=X^(20q)+A X^(16q)+C X^(3q)+D X^q
           =h(X^q),

allowing any of A,C,D to vanish. Since f(1)=0 before reduction, h(1)=fbar(1)=0. In particular h has a nonzero root and cannot be X^20. This retained unit root is why the coefficient degeneration to a trivial pure power cannot invalidate the reduction.

## 4. Hasse derivatives pass through Frobenius

For every polynomial h over a characteristic-13 ring,

    h((X+T)^q)=h(X^q+T^q)
              =sum_k (D^[k]h)(X^q) T^(qk).

Comparing coefficients of T^(qk) gives

    D^[qk](h(X^q))=(D^[k]h)(X^q).

This holds for every e>=0, including e=0. No inverse Frobenius or separability assumption is needed.

For each k=1,...,19, the original characteristic-zero CA hypothesis supplies a shared root gamma_k of f and its Hasse derivative of order qk. These orders lie in 1,...,N-1. Each gamma_k is integral because it is a root of f. Hasse derivation commutes with coefficient reduction, so its residue gamma_bar_k satisfies

    h(gamma_bar_k^q)=0,
    (D^[k]h)(gamma_bar_k^q)=0.

Thus h is CA over the residue field, or its algebraic closure. Some witnesses may reduce to zero or collide; that is permitted by the CA condition and by the exhaustive base lemma. The base lemma contradicts h(1)=0. This proves the theorem.

## 5. Adversarial checks and boundaries

- The chosen root alpha is arbitrary; centering is needed only for the ten-index degree-20 corollary, not for the infinite-family theorem.
- The theorem asserts that at least one coefficient in a specified set is nonzero. It is not a uniform minimum-term theorem for degrees 20*13^e.
- Missing coefficients A,C,D were individually covered before applying valuation reduction. Exact-support certificates alone would have been insufficient.
- The certificate is a unit-ideal identity over F_13, so it excludes algebraic-closure solutions, not merely rational finite-field points.
- All shared-root witnesses are integral after a single global scaling, because they are roots of f. The proof does not normalize different derivative witnesses separately during the valuation step.
- Derivative orders in the Frobenius argument are qk, while the coefficient hypothesis uses deficiencies qj. Confusing these two index maps would state a different theorem.
- The proof does not require good reduction of every complex solution, finite generation over Z_(13), or a saturation argument. The retained unit root and binomial-integrality induction supply an independent reduction route.
- The standard Lucas/valuation/Frobenius mechanism is established mathematics. The possible contribution is this particular complete residue obstruction and its explicitly quantified support consequence; novelty remains for a separate audit.
- The full Casas–Alvero conjecture and unrestricted degree 20 remain open within this work.
