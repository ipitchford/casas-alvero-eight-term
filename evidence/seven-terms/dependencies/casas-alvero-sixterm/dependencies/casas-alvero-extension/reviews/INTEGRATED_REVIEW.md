# Adversarial review of the integrated proof

Date: 23 September 2026.

Target: `outputs/casas-alvero-extension/PROOF.md`.

Reviewed SHA256: `f0a128b12e5e594b05c88023af48b79aba725dc66262e25881b2ee61ee774fdb`.

## Verdict

**No fatal or major mathematical issue found.** Theorem 1, including every exponent e and every chosen root, follows from the stated valuation argument, Lucas reduction, and the fully covered characteristic 13 lemma. The six-centered-term corollary follows from the support lemma and the checked sixteen-case CLO determinant table.

This is an internal adversarial audit. I did not construct the integrated compact remainder proof, but I participated in the earlier sparse computational pilot and its independent certificate checks. This is not external referee review, formal verification, or a novelty opinion.

## Quantifiers and arithmetic transfer

1. The valuation normalization is valid at an arbitrary chosen root: translation first makes its constant coefficient zero; nontriviality guarantees a nonzero root for scaling. A minimum among the finitely many root valuations exists even when the value group is not discrete. All scaled roots are integral and the retained root 1 survives reduction.
2. The induction concerns binomial-normalized coefficients and uses actual characteristic-zero common roots. Its monic normalized derivative equation proves integrality of each next coefficient. Hasse derivatives of the integral polynomial commute with reduction; no factorial is inverted in the residue field.
3. For N=20*13^e, Lucas's digit criterion leaves deficiency indices q*j with j in {0,...,7,13,...,20}. Removing J, the leading term, and the zero constant term leaves exactly 4q,17q,19q. Thus the reduction is h(X^q) for the stated three-lower-term h. This argument is symbolic in e.
4. The Hasse identity H_(qk)(h(X^q))=(H_k h)(X^q) is exact in characteristic 13. Reducing the original common witnesses and taking their qth powers supplies every required common witness for h. There is no assumption that these reduced witnesses remain distinct or nonzero.
5. Since h(1)=0, the reduction is not the trivial monomial. Lemma 3 therefore contradicts the hypothetical vanishing of all prescribed coefficients. The derivative-index conversion K=20-J is correct, and every order q*k lies between 1 and N-1.

## Zero-coefficient charts in Lemma 3

- For a=0,c!=0, normalization gives c=4,d=8. The two displayed root equations imply w²=10 and w¹⁹=4, hence w=9 and the contradiction w²=3. These calculations are valid over the algebraic closure, not merely F13-rational points.
- For a=c=0,d!=0, the first derivative gives the stated immediate contradiction. The all-zero lower coefficients give the allowed monomial.
- For a!=0, H16 forces a nonzero witness and normalization a=4. When c=0, choosing v=1 is valid because H3(h)(1)=9+4=0. Thus the argument does not inadvertently delete the c=0 chart.
- The derived identity d=-5*v¹⁹ and v!=0 rules out d=0 before division by a first-derivative witness. The divisions by v and v¹⁵ are therefore justified.
- Neither denominator root 6 nor 7 satisfies t¹⁹=4. No division by the cubic factor in the subsequent squared equations occurs.

## Compact polynomial calculation

I independently recomputed the remainder of D¹⁹R(B/D) modulo t¹⁹-4 using fresh standard-library polynomial arithmetic, without calling a computer-algebra system or importing the campaign checkers. It agrees coefficient by coefficient with the printed H. The arithmetic also verifies H(4)=8, both denominator-root exclusions, and the coefficient disagreement H!=5Q.

The derivation of R from the squared equation is correct: with A=5T⁴ and B=4T³(1-T), squaring Av³+Bv=5 and using v⁴=T gives exactly the printed cubic-factor relation. Squaring again gives the necessary condition R(T)=0. Extra roots from squaring do not threaten an exclusion.

The order argument for irreducibility is sufficient: every proper divisor of 18 divides 6 or 9; the two displayed powers exclude both. Since 19 is prime and distinct from 13, Q has precisely the scaled primitive nineteenth roots as its roots and is irreducible of degree 18.

## Six-term corollary

The visible-index sets at primes 19, 2, 5, 17, 3 are correct. The singleton obstruction at index 19 excludes reliance on that index alone for primes 17 and 3. The first four required sets are pairwise disjoint, so four nonleading monomials are necessary before using the new characteristic 13 argument.

For exactly four lower monomials, the Cartesian choices give 24 supports, and the prime 3 condition leaves precisely the sixteen printed rows. I independently regenerated those sixteen supports and all determinant residues by modular Gaussian elimination from the primary CLO matrix. Every table entry agrees. The only zero residue is the support {4,10,17,19}, which is contained in T and therefore excluded by Theorem 1.

This proves the lower bound in the centered normal form. The proof does not accidentally claim the same monomial count before translation.

## Minor wording suggestion

The final paragraph calls the retained 1,777-term certificate a second route to the finite-field exclusion. Its direct scope is the normalized a!=0 chart; the a=0 cases still use the separate elementary arguments. For maximal assurance precision, consider saying “a second route for the normalized a!=0 chart, with the same elementary treatment of a=0.” The main proof already covers all charts correctly, so this is not a mathematical blocker.

## Reproduction

`python3 work/casas-alvero-extension/review_integrated.py`

The exact receipt is `work/casas-alvero-extension/integrated-review-arithmetic.json`. The checker verifies the compact remainder, scalar irreducibility checks, denominator exclusions, sixteen-support coverage and residues, theorem derivative indexing, and the base 13 visible indices. It does not claim to formalize the valuation extension or written infinite-family argument.
