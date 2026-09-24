# Independent audit of the nine characteristic-17 seeds

23 September 2026. Bounded audit of
`../support_frontier/prime17/CLASSIFICATION.md` and its exact certificates.
The characteristic-zero lifting problem is separate.

**Final status: PASS within the stated seed-classification scope.** The
algebraic chart cover, normalization, boundary proofs and deductions from
the certificate targets pass review. All nine seeds and their 19 Hasse
gcds pass independent exact arithmetic. The standalone certificate
checker passes ordinary and optimized Python replay, after independent
review of its field arithmetic, interpolation proof and ideal-membership
verification. No mathematical gap was identified in this classification.

## Full chart cover over an algebraically closed field

For a monic centered visible seed

\[
h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX
\]

the only potentially nonzero Hasse derivatives of orders 1 through 19
are 1,2,3,17,18,19. In particular every order 4 through 16 is identically
zero, which is stronger than merely having zero constant term. The six
formulas in the producer note agree with direct Lucas expansion.

If \(c\ne0\), the unique root of \(H_3h=X^{17}+c\) is nonzero.
Scaling it to one gives \(c=-1\), \(e=-a-b-d\), and the remainder
in the cubic/Frobenius decomposition is
\(Q=(X-1)(dX-b)\). A common \(H_{17}\) root is therefore either
one or a root of \(dX-b\). The separate \(b=0\) chart includes all
possible zero witnesses; when \(b\ne0\) and the chosen witness differs
from one, both it and \(d\) are nonzero and the parametrization
\(a=-s^2-t,b=st,d=t\) follows. No division by a quantity that might
vanish is used before its nonvanishing is established. Extending the
three charts to all parameter values does not invalidate necessity or
sufficiency: they still satisfy the two already-imposed derivative
conditions, and they overlap harmlessly.

If \(c=0,a\ne0\), an \(H_{18}\) witness is nonzero. Scaling it
to one gives \(a=-3,e=2-b-d\). The remaining resultants are exactly
those for orders 17,2,1. If \(c=a=0,b\ne0\), normalize an
\(H_{17}\) witness to one; this gives \(b=-1,e=-d\).

These are separate normalizations, each realized by one selected unit
witness in a characteristic-zero application. They never require two
different witnesses to equal one simultaneously. They preserve the
centered coefficient and root zero. A seed can have more than one
representative under the choices; pairwise inequivalence is unnecessary
and is explicitly not claimed.

## Why the targets imply geometric completeness

Every resultant involved has constant nonzero leading coefficients in
its two polynomials, independently of \(s,t\). Vanishing is therefore
equivalent to a common affine root over the algebraic closure; no
leading-degree degeneration or root-at-infinity case is being discarded.

The intended membership targets have the following consequences in an
arbitrary algebraically closed field of characteristic 17:

- In the \(c=-1,b=0\) chart, \(t^{20}=0\) forces \(t=0\).
  The second target becomes \(s^{20}+3s^3=s^3(s+3)^{17}\), giving
  \(s=0\) or \(-3\), rows 1 and 2.
- In the witness-one chart, the target 1 makes the chart empty.
- In the other-witness chart, \(t^{20}(t+5)=t^{20}(s+5)=0\)
  forces \(s=t=-5\) when \(t\ne0\), giving row 3. If \(t=0\),
  the final target becomes \(s^6(s^2-3)^{17}\), giving again rows
  1 and 2 because \(a=-s^2\). The parameter \(s\) can lie in a
  quadratic extension; the resulting coefficients still lie in
  \(\mathbb F_{17}\). Thus a prime-field parameter enumeration would
  have been insufficient even here.
- In the \(c=0,a=-3\) chart, the positive powers of
  \(s(s-2)\), \(st+6s-2t+5\), and \(t(t-11)(t-14)\)
  force those three polynomials to vanish. Their solutions are exactly
  \((s,t)=(0,11),(2,0),(2,11),(2,14)\), rows 4 through 7.

This direction requires only explicit ideal-membership identities,
not a trusted radical or Gröbner-basis assertion. Direct gcd checks
establish the converse for the retained rows. In particular the claim
that normalized coefficients lie in the prime field is a consequence
of these equations, not an initial restriction on the residue field.

## Boundary charts and monomial

For \(c=a=0,b=-1,e=-d\), \(d=0\) gives row 8. When \(d\ne0\),
an \(H_2\) witness \(r\) is nonzero. Substitution of
\(d=-3r^{18}\) into \(h(r)/r=0\) gives
\(-r^{16}(r-1)^2(2r+1)=0\). Hence \(r=1\) or 8 and
\(d=14\) or 12. The second value fails the \(H_1\) gcd test;
the first gives row 9.

For \(c=a=b=0,d\ne0\), normalize an \(H_2\) witness to one,
so \(d=-3,e=2\). Any common \(H_1\) root is nonzero, and
\(H_1h-3h/X=3X-4\) forces it to be 7. But \(h(7)/7=1\),
a contradiction. Finally \(c=a=b=d=0,e\ne0\) is impossible by
\(H_1h-3h/X=-2e\). The all-zero tuple is exactly \(X^{20}\),
retained separately by the classification. It is excluded in the
characteristic-zero reduction application by the retained unit root,
not by a blanket nonvanishing assumption on individual coefficients.

## Independent gcd pass and exact zeros in potential lifts

`check_prime17_seed_gcds.py` computes every monic
\(\gcd(h,H_kh)\), \(1\le k\le19\), for each of the nine rows
using the ordinary polynomial Euclidean algorithm over \(\mathbb F_{17}\).
All have positive degree. Its normal and optimized Python runs agree;
the full ascending coefficient arrays are in `prime17-seed-gcds.json`
and `prime17-seed-gcds-optimized.json`.

The mean residue root zero is simple exactly in rows 2,4,6,7,9, since
\(h'(0)=e\). Suppose a characteristic-zero normalized polynomial has
one of these residues. Factor \(f=Xq\); \(q(0)\) is a unit. For any
integral \(z\) of positive valuation, \(q(z)\) is also a unit.
Consequently an actual root of \(f\) reducing to zero equals zero
exactly. This argument permits arbitrary ramification.

If \(\gcd(h,H_kh)\) is a positive power of \(X\), every actual
\(H_kf\) common witness reduces to zero, hence equals zero. It follows
that \(H_kf(0)=0\), which is precisely the vanishing of the ordinary
coefficient of \(X^k\). In deficiency notation this is index \(20-k\).
Applying the complete gcd pass gives:

| Seed row | Coefficients \((a,b,c,d,e)\) | Forced ordinary exponents \(k\) | Forced deficiencies \(20-k\) |
|---|---|---|---|
| 2 | \((14,0,16,0,3)\) | 19 | 1 |
| 4 | \((14,0,0,11,8)\) | 3,17,19 | 17,3,1 |
| 6 | \((14,2,0,11,6)\) | 3,19 | 17,1 |
| 7 | \((14,2,0,14,3)\) | 3,19 | 17,1 |
| 9 | \((0,16,0,14,3)\) | 3,18,19 | 17,2,1 |

Exponent 19 was already zero by centering. All other entries are genuine
exact coefficient restrictions on unrestricted characteristic-zero
supports, conditional on the specified residue chart. There are no
additional pure-\(X\) gcd orders for these five rows. No exact zero is
inferred this way for the four rows whose mean residue root is multiple.
The normalization uses an actual unit common witness, so these statements
do not presume that two roots sharing a residue coincide.

These restrictions do not exclude a row or prove that any row lifts.

## Certificate replay audit

The producer's `check_classification.py` was independently inspected and
run under `python3` and `python3 -O`; both pass with identical mathematical
output. The receipts are `prime17-certificate-replay.log` and
`prime17-certificate-replay-optimized.log` in this audit directory.

The checker reconstructs each chart's polynomial directly, derives its
Hasse derivatives from integer binomial coefficients, and recomputes
the twelve exported resultants at **12,895 exact grid points** in
\(\mathbb F_{17}[\alpha]/(\alpha^2-3)\). The nonsquareness of 3
is checked; the two-coordinate arithmetic, additive inverses and all
288 multiplicative inverses are consistent with that field. The
Euclidean resultant recurrence has the correct leading-coefficient
factor and interchange sign, including nonmonic inputs.

For each coordinate, the degree bound is

\[
\deg_s\operatorname{Res}_X(h,g)
\le (\deg_Xg)\max_i\deg_s h_i
 +(\deg_Xh)\max_i\deg_s g_i,
\]

and similarly for \(t\). This follows from the two coefficient-group
homogeneities of the Sylvester determinant. The checker bounds the
exported polynomial by the same numbers and evaluates on a product of
more distinct field elements than each respective bound. The largest
bidegree bound is \((78,39)\), below the field cardinality 289.
Coordinatewise interpolation therefore proves polynomial identities,
not just agreement at selected rational points. The leading
\(X\)-coefficients stay constant and nonzero at every grid point.

Finally, sparse multiplication verifies **nine** complete membership
identities (2,1,3,3 in the four charts), along with the exact target
formulas or required specialization. The parser checks the complete
set of labeled polynomial records and rejects duplicate monomials,
missing records and trailing content. No Gröbner basis, radical output,
CAS call or producer-library import is trusted by this replay. The
certificate logs are fixed evidence inputs; their hashes appear in the
receipts.

This validates the complete geometric **point classification** up to
the stated scaling. It does not assert that the incidence schemes are
reduced, that these points lift, or that their ramified neighborhoods
have been excluded. Priority was not assessed in this bounded audit.
