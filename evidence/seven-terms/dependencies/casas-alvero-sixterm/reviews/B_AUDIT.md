# Independent audit of Family B

23 September 2026. Internal mathematical and arithmetic audit; no publication or historical-priority certification. Producer files were not edited.

**Verdict: the certificate and the reconstructed argument prove the closed characteristic-13 seed exclusion, including all coefficient-zero cases. The characteristic-zero transfer is valid with the valuation normalization described below.** This eliminates support B; it does not eliminate A or C and does not by itself prove a seven-term lower bound.

The audited seed is

\[
h(X)=X^{20}+aX^{17}+bX^4+cX^3+dX.
\]

Only the monomial can satisfy the Hasse CA conditions, over any algebraically closed field of characteristic 13. The certificate identities actually apply over every field extension of \(\mathbf F_{13}\).

The proof reconstruction below was checked against `B/DERIVATION.md`, `B/certificate.json`, and `B/verify_certificate.py`, then aligned with the completed `B/PROOF.md`. The final proof's slightly stronger contained-support consequence was also checked below.

## 1. The normalization and its boundary

When \(a=0\), the seed is precisely the complete family in the previously audited `work/casas-alvero-structural/sixterm/LAST_MASK_PROOF.md`. I reread its coefficient-zero cases and ratio equations and reran its standard-library checker. It passed the independent 19-by-19 Sylvester determinant, substituted-remainder, Bezout identity, and denominator checks. Thus this dependency includes all \(b,c,d\), not just a nonzero-coefficient chart.

For \(a\ne0\), \(H_{17}h=9X^3+a\) has a nonzero common root with \(h\). Scaling that root to 1 is allowed and yields \(a=4\). The root equation then gives \(d=-5-b-c\). Direct binomial calculation gives

\[
H_4h=9X^{16}+4X^{13}+b,
\quad H_3h=9X^{17}+3X^{14}+4bX+c,
\]
\[
H_1h=7X^{19}+3X^{16}+4bX^3+3cX^2+d.
\]

All other derivative orders have the common root zero. No condition requires selected witnesses to be distinct.

## 2. The \(b=0\) chart

Choose any common-root witness \(v\) for \(H_3\), and any witness \(w\) for \(H_1\). The identities

\[
c=-9v^{17}-3v^{14},\qquad d=-5-c
\]

are valid even if \(v=0\). The saved three multipliers certify a unit combination of

\[
h(v),\qquad h(w),\qquad H_1h(w).
\]

The checker reconstructs these generators from the original Hasse formula, then multiplies all 680, 694, and 712 saved multiplier terms. The resulting polynomial is exactly 1 in \(\mathbf F_{13}[v,w]\). In particular, the factors \(v\) and \(w\) in the root equations are retained. This closes \(b=0\), including \(c=0\) and \(d=0\), without any saturation or assumption that zero cannot be a witness.

## 3. The rational \(b\ne0\) chart

Let \(u\) witness \(H_4\). Then

\[
b=-9u^{16}-4u^{13},\qquad
0=h(u)/u=5u^{19}+cu^2+d.
\]

The division by \(u\) is legitimate because \(H_4h(0)=b\ne0\). At \(u=1\), the formula for \(b\) gives zero. At \(u=-1\), it gives \(b=8\), while the displayed root equation becomes 8 rather than zero. Therefore \(u\ne0,1,-1\).

Put \(q=u+1\), and define the polynomial

\[
C(u)=\frac{5+b-5u^{19}}{u-1},\qquad
D(u)=q(-5-b)-C(u).
\]

The numerator vanishes at 1, so \(C\) is a polynomial, not an unresolved rational expression. The necessary coefficients are \(c=C/q\) and \(d=D/q\). Both original divisions are now justified; \(q\ne0\).

Let

\[
P=q(h/X),\quad Q_3=qH_3h,\quad Q_1=qH_1h,
\quad R_3=\operatorname{Res}_X(P,Q_3),\quad R_1=\operatorname{Res}_X(P,Q_1).
\]

If \(c\ne0\), its \(H_3\) witness is nonzero, so \(R_3(u)=0\). If \(c=0\), then \(C(u)=0\). Thus \(C(u)R_3(u)=0\) in both cases. Likewise, either a nonzero first-derivative witness forces \(R_1(u)=0\), or \(d=0\) forces \(D(u)=0\). Hence \(D(u)R_1(u)=0\) without deleting that chart.

The saved univariate multipliers satisfy

\[
U(u)C(u)R_3(u)+V(u)D(u)R_1(u)=(u+1)^{17}.
\]

Direct multiplication verifies this identity. At a putative solution the left side is zero, while the right side is nonzero. This closes \(b\ne0\), including every \(c,d\) degeneration.

## 4. Why the 685-point verification is conclusive

As polynomials in \(X\), \(P,Q_3,Q_1\) have degrees \(19,17,19\). Every coefficient has degree at most 18 in \(u\): \(C,D\) have degree 18, and \(qb\) has degree 17. The Sylvester determinant has exactly 17 rows from \(P\) and 19 from \(Q_3\), giving

\[
\deg_u R_3\le17\cdot18+19\cdot18=648.
\]

Similarly, \(\deg_u R_1\le684\). The saved arrays have degrees 359 and 395, within these bounds. Lower actual degrees do not need to be assumed in the verification.

The checker works in \(\mathbf F_{13}[t]/(t^3-t-1)\). It explicitly checks that the cubic has no \(\mathbf F_{13}\) root; since it has degree three, the quotient is a field of size 2,197. Its multiplication formula reduces \(t^3=t+1\) and \(t^4=t^2+t\), as required. The inverse routine verifies each inverse it uses.

It checks the two saved resultant polynomials at 685 distinct field elements, omitting only the element \(-1\). At each point the three leading coefficients are \(q,9q,7q\), all nonzero, so specialization preserves the declared \(X\)-degrees. The Euclidean resultant formula in the checker is therefore applied to exactly those specialized Sylvester resultants. Agreement at 685 distinct points forces equality of polynomials of degree at most 684. This is exact interpolation, not random testing or a search limited to prime-field coefficients.

I additionally rebuilt both Sylvester matrices over the prime field at all 12 points \(u\ne-1\), using separate determinant code without importing producer arithmetic. Every value agrees with the saved arrays. This supplementary check helps audit signs and parameterization; it is not substituted for the complete extension-field interpolation argument.

## 5. Transfer to characteristic zero

For a characteristic-zero CA polynomial with deficiency support contained in \(\{3,10,16,17,19\}\), translate the specified root to zero and extend a 13-adic valuation to a field containing its coefficients and roots. Scale a nonzero root of minimum valuation to 1. All roots become integral.

Write the scaled polynomial as \(\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j}\), with \(a_0=1\). The monic normalized derivative of order \(20-j\) evaluated at an integral common root expresses \(a_j\) using \(a_0,\ldots,a_{j-1}\), integral binomial coefficients, and that root. Induction makes every \(a_j\) integral. This is the step that permits the Lucas support reduction; integrality of ordinary coefficients alone would not suffice.

The deficiency-10 binomial coefficient is divisible by 13, while the relevant deficiencies 3,16,17,19 are visible. Reduction therefore lies in the closed seed proved above, potentially with any coefficients zero. Every original Hasse common-root witness is integral and reduces to a witness. The retained root 1 makes the reduced seed nonmonomial, contradicting the seed theorem. The argument works even if the residue field is larger than \(\overline{\mathbf F}_{13}\), because the certificate identities hold in every extension field.

The identical argument applies to the final proof's larger mask \(T_B=\{3,8,9,10,11,12,16,17,19\}\): all five indices 8 through 12 disappear, and the remaining seed is unchanged. This proves the desired exclusion of support B and the stated larger contained-support consequence. It does not derive characteristic-zero emptiness merely from an arbitrary affine special fiber.

## 6. Reproduction and assurance

- `python3 B/verify_certificate.py`: PASS.
- `python3 -O B/verify_certificate.py`: PASS, same algebraic checks.
- Certificate SHA-256: `981ff911b8493e9a3cb37dea620dd63249e6bd2bff9c93f16aec2670e88179c7`.
- Inherited `verify_last_mask.py`: PASS; input SHA-256 `f906bbcc0a82bd63c1512df41272ea4bedeb3670917fd98eae4d83dd5eb8d82f`.
- Independent supplementary check: `reviews/b_independent_spotcheck.py`, 24 direct Sylvester determinant evaluations, PASS.
- Completed `B/PROOF.md` reviewed at SHA-256 `abcbfdfce2cf942cad7dd071cffd8c1f5ed79c4ecd44829cd697a078095c830e`; no discrepancy with this reconstruction was found. Its right-hand side of equation (5) at \(u=-1\) is 5, consistently opposite to the value 8 of the corresponding zero-form root equation used above.

All results are exact arithmetic/internal mathematical review. No formal proof assistant, external referee, or novelty certification is claimed. The normalized three-variable Gröbner-basis result is useful discovery evidence, but the argument above relies on the replayed identities, not trust in its printed `[1]` alone.

## 7. Tiny method/prior-art addendum

This Family B proof uses resultants, Bezout identities, exact interpolation, and the established CA valuation transfer; it does not use Hensel lifting. Those general techniques should not receive novelty claims here.

A bounded search for `"Casas-Alvero" "Hensel"` and `"Casas-Alvero" "root collision" valuation`, plus text searches in [CLO](https://arxiv.org/html/1208.5404) and [Massri v6](https://arxiv.org/html/1806.09561v6), found no exact named Hensel collision lemma matching an as-yet-unspecified new argument. The relevant public [ProofAtlas overview](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/) mentions Hensel expansion but does not expose its underlying formulas. This unresolved lead was already recorded; it is not evidence that a root-collision technique is new. Any later collision argument needs its own exact hypotheses and source comparison.
