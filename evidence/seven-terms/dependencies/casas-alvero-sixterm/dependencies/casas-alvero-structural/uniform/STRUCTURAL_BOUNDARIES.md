# Structural boundary analysis for the p+7 seed family

Research note, 23 September 2026. No publication or priority claim.

Let p>7 be prime, let K be an algebraic closure of F_p, and set

\[
 h(X)=X^{p+7}+aX^{p+3}+cX^3+dX.
\]

The proposed uniform exclusion is false, even away from p=17 and even with a*c*d nonzero. A concrete example is

\[
 \boxed{p=19,\qquad h=X^{26}+3X^{22}+14X^3+X.}
\]

The root 1 supplies the Hasse derivative of order 22, root 2 supplies order 3, and root 13 supplies order 1. Every other derivative condition holds at zero. The accompanying standard-library checker verifies these statements directly from the Hasse formula.

This does not refute a characteristic-zero theorem. It limits which primes can support the intended specialization argument.

## 1. Common identities and active orders

The only derivative orders whose values at zero can be nonzero are p+3, 3, and 1. Lucas's theorem gives, modulo p,

\[
 H_{p+3}(h)=35X^4+a,
\]
\[
 H_3(h)=35X^{p+4}+aX^p+c,
\]
\[
 H_1(h)=7X^{p+6}+3aX^{p+2}+3cX^2+d.
\]

Thus checking these active orders is a complete check of the CA property for this family. If a coefficient is zero, its associated order also holds at the zero root.

Two useful identities are

\[
 h-X^3H_3(h)=-34X^{p+7}+dX,
\]
\[
 3(h/X)-H_1(h)=-4X^{p+6}+2d.
\]

They explain the constants 34 and 17 in the root-ratio reduction.

## 2. The exceptional characteristic 17 is completely classified

In characteristic 17, h is CA if and only if

\[
 d=0\quad\hbox{and}\quad ac=0.
\]

This includes the pure power, and the two nontrivial one-support families

\[
 X^{24}+aX^{20}\ (a\ne0),\qquad
 X^{24}+cX^3\ (c\ne0).
\]

To prove necessity, if c!=0 then a common root v with H3 is nonzero. The first identity forces d=0 because 34=0. If also a!=0, a common root r with H20 is nonzero and r^4=-a since 35=1. But then h(r)=c*r^3!=0, a contradiction. If c=0 and a!=0, the H20 common-root equation similarly forces d=0. If a=c=0 but d!=0, the equations at a common root with H1 would be w^23+d=0 and 7w^23+d=0, impossible. Sufficiency follows directly because the sole active derivative in each displayed family divides its nonzero-root factor.

## 3. Complete classification of the c=0 boundary for p!=17

Suppose a!=0 and c=0. Normalize a common root with H_(p+3) to 1. Then

\[
 a=-35,\qquad d=34.
\]

Since p!=17, d is nonzero, so a common root w with H1 is nonzero. Put

\[
 A=51/35,\qquad B=35/3.
\]

The two root/derivative equations are equivalent to

\[
 w^{p+6}=17,\qquad w^{p+2}=A,
\]

and consequently w^4=B. Since gcd(4,p+2)=1 and A,B belong to F_p^*, Bezout's identity for exponents implies w belongs to F_p^*. Therefore w^(p+2)=w^3, so

\[
 w=B/A=35^2/(9\cdot17).
\]

Existence is equivalent to B^3=A^4, namely

\[
 p\mid 3^7 17^4-35^7=-64\,156\,636\,448
   =-2^5\cdot23\cdot87\,169\,343.
\]

Both odd factors are prime. Hence, for p>7,p!=17, this boundary contains a nontrivial CA polynomial **exactly when**

\[
 p\in\{23,87\,169\,343\}.
\]

Conversely, for either listed prime the displayed w satisfies w^3=A and w^4=B, so w^(p+6)=w^7=AB=17. The two active conditions are then checked at 1 and w. Every original polynomial in this boundary is scaling-equivalent to the normalized one, since normalization used an existing common root and a is nonzero.

The small example is

\[
 \boxed{p=23,\qquad h=X^{30}+11X^{26}+11X,}
\]

with active witnesses 1 and 5.

## 4. Complete classification of the a=0 boundary for p!=17

Suppose a=0 and c!=0. Normalize a common root with H3 to 1. Then

\[
 c=-35,\qquad d=34.
\]

For a common root w with H1, the two equations reduce to

\[
 w^{p+6}=17,\qquad w^2=A=51/35.
\]

Since p+6 is odd, gcd(2,p+6)=1; hence w belongs to F_p^*. Thus w^7=17 and necessarily

\[
 w=17/A^3=17(35/51)^3.
\]

Existence is equivalent to A^7=17^2, or

\[
 p\mid51^7-17^2 35^7=-17\,696\,646\,119\,024
   =-2^4\cdot17^2\cdot1229\cdot3\,114\,019.
\]

Both remaining factors are prime. Therefore this boundary contains a nontrivial CA polynomial exactly at

\[
 p\in\{1229,3\,114\,019\}
\]

among primes p>7,p!=17. The normalized polynomials are X^(p+7)-35X^3+34X, with H3 witness 1 and H1 witness w. For p=1229 the latter witness is w=1137; for p=3114019 it is w=1799855.

## 5. Other zero-coefficient cases

For p>7,p!=17, any nontrivial CA polynomial in the family must have d!=0. If c!=0, the first common-root identity gives d=34v^(p+6)!=0. If c=0,a!=0, the H_(p+3) common-root equation likewise gives d=34r^(p+6)!=0. If a=c=0,d!=0, the binomial X^(p+7)+dX cannot be CA because its only active order H1 gives the incompatible multiplier 7!=1. Thus Sections 3 and 4 classify every nontrivial degeneration away from p=17.

## 6. The genuine three-coefficient case

When p!=17 and a,c,d are all nonzero, normalize a=-35 and let v,w be the H3 and H1 witnesses. Then

\[
 c=35v^p(1-v^4),\qquad d=34v^{p+6},\qquad
 t=w/v,\quad t^{p+6}=17.
\]

For p=19 the explicit choices

\[
 v=2,\quad w=13,\quad (a,c,d)=(3,14,1)
\]

give the counterexample recorded at the start. This is a case that a uniform classification must include, and it is not explained away by coefficient degeneration.

A bounded search of rational marked roots for primes 11<=p<300 found this as the only fully nonzero example in that search. A further check allowing algebraic H1 witnesses but rational H3 witnesses for primes below 100 also found only this example. Neither search is an exhaustive classification over algebraic closures, and neither supplies an exclusion for unlisted primes. The explicit witnesses, not search absence, are the theorem-level findings here.

## 7. The denominator D=51-35t^2 never vanishes on a genuine solution

In the normalized a!=0 case, the root-ratio derivation gives the **undivided** relation

\[
 (51-35t^2)v^4=35t^2(t^p-1).
\]

For p>7,p!=17, both v and t are nonzero. If D=51-35t^2 were zero, this equation would force t^p=1. In characteristic p, X^p-1=(X-1)^p, so t=1, giving D=51-35=16!=0. Contradiction. Thus dividing by D is legitimate without adding an exceptional prime.

Eliminating too early could produce the integer obstruction

    51^3-17*35^3=-596224=-2^8*17*137.

The apparent prime 137 is extraneous: the full Frobenius relation rules it out by the preceding argument. Equivalently, in z=t^2 coordinates D=0 would make z=51/35 an element of F_p. The numerator equation gives z^3=17, while z^p=289/z^6 gives z^7=289=z^6, hence z=1 and again D=16.

As controls for the root agent's subsequently derived fixed necessary polynomial H(z), I evaluated its saved integer coefficients at the explicit examples above. They vanish at (p,z)=(19,9), (23,2), and (87169343,65880709). These are positive-control checks of H, not an independent verification of its derivation.

Any uniform theorem extracting H via rational cancellation and primitive polynomial normalization must retain the primes dividing removed integer contents and denominator constants. Dividing by a polynomial content over Q is not automatically a valid implication modulo its prime factors. The denominator D itself, however, is resolved exactly above.

## 8. Relation to prior art and next use

The two boundary cases are two-element-support problems and belong to an established framework. Rosa Maria de Frutos Marin's 2013 doctoral thesis, *Perspectivas aritmeticas para la Conjetura de Casas-Alvero*, Universidad de Valladolid, gives the relevant one- and two-support modular criterion in Section 3.5, Theorem 3.5.1 (printed pp. 54–56), with related characteristic-zero calculations in Section 2.3 and lifting consequences in Propositions 3.5.3 and 3.5.5 (printed p. 57). [Primary thesis PDF](https://uvadoc.uva.es/bitstream/10324/3602/1/tesis367-130927.pdf), [university metadata](https://uvadoc.uva.es/handle/10324/3602?show=full).

The later two-support treatment in Marashdeh's [2026 primary manuscript, Theorem C](https://arxiv.org/html/2608.14726v1) therefore cannot be treated as the first general criterion. The boundary derivations here are self-contained explicit specializations used as exceptions and positive controls; no novelty is claimed for their underlying criterion.

The useful structural output is a complete degeneration classification plus explicit positive examples. It replaces an overly broad exclusion target with a sharper classification problem. The characteristic-13 seed remains valid and appears in none of the exceptional boundary lists; its genuinely three-coefficient case was handled separately by the compact ratio/cyclotomic proof.

`check_boundaries.py` verifies integer factorizations, primality of the finite listed factors by deterministic trial division, and every displayed finite-field witness directly from the Hasse formula. It does not prove necessity; the written exponent argument does that. No numerical root approximation is used.

## 9. A practical fixed-degree necessary test

Conditional on the root agent's separately audited fixed polynomial H(z), a genuine normalized a!=0 solution at p>7,p!=17 must satisfy

    H(z)=0,    z^(p+6)=289.

It must avoid the zeros of z*(51-35z)*(3z^6-595), the denominators of T(z) and T(289/z^6). Therefore compute the gcd of H and z^(p+6)-289 modulo p and remove its factors shared with this denominator polynomial. The power can be computed modulo H by repeated squaring, so the polynomial degree remains at most 72 and the number of polynomial multiplications grows logarithmically with p.

The polynomial z^(p+6)-289 is squarefree: its derivative is 6z^(p+5), with p>7 and p!=17. Consequently its roots are all simple and one gcd-and-division removes every forbidden root.

`fast_necessary_filter.py` implements this directly using integer lists, modular polynomial multiplication, Euclidean division, and gcd. It uses no CAS. The bounded test results are:

| p | Admissible gcd | Conclusion from this test |
|---:|---|---|
| 13 | 1 | a!=0 branch excluded |
| 19 | z-9 | candidate; explicit CA example verified separately |
| 23 | z-2 | candidate; explicit CA example verified separately |
| 79 | z-18 | candidate only |
| 137 | 1 | a!=0 branch excluded |
| 257 | z-8 | candidate only |
| 823 | 1 | a!=0 branch excluded |
| 1973 | 1 | a!=0 branch excluded |
| 87169343 | z-65880709 | candidate; explicit CA example verified separately |

No denominator factor removal was needed in these nine cases. Normal and optimized Python runs produced PASS receipts. In particular the resultant's factors 137, 823, and 1973 are false positives for the a!=0 branch, while 79 and 257 remain unresolved by this necessary test. A nonconstant gcd does not prove the existence of v, w, or a CA polynomial.

The separate `check_fixed_controls.py` directly evaluates H and its homogenized Frobenius transform C on the known examples at 19, 23, and 87169343, and verifies that the stored resultant integer is divisible by each of those primes. This is a positive-control check rather than an independent reconstruction of the large resultant.

## 10. Exact completion of the small-prime candidates

The necessary test in Section 9 leaves 79 and 257 unresolved. An additional exact compatibility condition excludes both; this is an algebraic-closure exclusion, not absence in a rational-root search.

When the surviving factor of the z-condition is linear, z belongs to F_p. The equations t^2=z and t^p=17/t^6 then imply

    t=17/z^3 in F_p,    T=35(17-z^3)/(z^2(51-35z)) in F_p.

The marked root v must simultaneously satisfy

    q(v)=v^4-T=0,
    v^p(34v^6-35v^4+35)-34=0.

Reduce the second polynomial modulo q and call the remainder r. The four small surviving cases give:

| p | z | t | T | r(v) | gcd(q,r) |
|---:|---:|---:|---:|---|---|
| 19 | 9 | 16 | 16 | 16v^3+10v+4 | v-2 |
| 23 | 2 | 5 | 1 | 11v+12 | v-1 |
| 79 | 18 | 27 | 2 | 40v^3+59v+45 | 1 |
| 257 | 8 | 120 | 162 | 111v^3+19v+223 | 1 |

The last two coprimality assertions have the short identities

    (53v^2+59v+22)(v^4-2)
      +(52v^3+40v^2+61v+1)(40v^3+59v+45)=1  mod 79,

    (79v^2+254v+77)(v^4-162)
      +(122v^3+132v^2+247v+200)(111v^3+19v+223)=1  mod 257.

At 19 and 23, reconstruction gives exactly the explicit polynomials from Section 1 and Section 3, respectively. `finish_linear_candidates.py` verifies the reduction, both Bezout identities by multiplication, and every defining Hasse condition on the positive controls. Normal and optimized runs pass.

Finally, `check_primes_below_10000.py` performs the degree-72 necessary test directly for **every prime 7<p<10000**. It does not read or use the giant integer resultant. There are 1,225 primes in this interval. The separately classified characteristic 17 is skipped; of the remaining 1,224, exactly 1,220 have constant admissible gcd. The only surviving factors are those at 19, 23, 79, and 257 just completed above. The normal run took 5.511 seconds.

Combining this finite check with the written a=0 classification and the characteristic-17 classification proves the bounded conclusion:

> For a prime 7<p<10000, a nontrivial characteristic-p CA polynomial of the form X^(p+7)+aX^(p+3)+cX^3+dX exists if and only if p belongs to {17,19,23,1229}.

This classifies existence in the stated finite range only. It does not classify all large exceptional primes. The exclusions rely on the separately audited derivation of H; the direct Hasse witnesses establish existence independently of H.
