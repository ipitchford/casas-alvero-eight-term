# Second independent audit: support A, row 1 only

24 September 2026. **PASS for the row-1 exclusion in A_ROW1_EXCLUSION.md.** The row-2 branch is a separate obligation and is not covered by this signoff.

Audited fingerprints:

- A_ROW1_EXCLUSION.md: 336a587c43501633de0400a3cd552f6c5ef12558ceb9bf01977ca0798e29f7df.
- A_ANALYSIS.md: 1b4aee5f88d4ead8633cee4bc6d705721aa192b875b1f47aebe70d820b694733.
- check_arithmetic.py: 433add7d46fd9743921b3d36b66b8be4c461021f7ed504ae1b4748ae1f102705.

The audit inherits only the separately approved second-jet lemma from B_EXCLUSION.md, with its corrected degree-nineteen term and the explicit arbitrary-ramification justification in B_AUDIT.md. The new occupancy, valuation bounds and perturbation transfer were checked independently here.

## Routing and exhaustive occupancies

Exact \(a_3=0\) leaves seed rows 1, 2 and 4. In row 4, the \(G_{17}\) witness reduces to the simple root zero, whose unique exact lift is the mean zero. It would force \(a_{17}=0\) exactly, contradicting the support. This is a valid exact-root argument; the zero residue of \(a_{17}\) alone would not suffice.

In row 1, \(h=a_2\) is nonzero with positive valuation. Its \(G_2=X^2+h\) witness is a nonzero root in the three-root zero cluster. The exact mean is simple. If an \(H_2\) witness is small, the two remaining roots have distinct initial locations 1 and 2 after scaling by that witness. They are simple. The proof in A_ANALYSIS.md then forces a unit repeated root, upgrades the small-root scale to at least 1, and obtains the empty four-marking sieve. All those implications survive arbitrary positive fractional valuations.

If both \(H_1,H_2\) witnesses are units, let \(\delta\) be the minimum nonzero unit displacement. The displayed bounds on \(c_2,c_1\) follow in that order from their derivative equations and apply also when a selected witness is exactly 1. At a root of minimum displacement, every term other than \(c_{17}Z^{17}\) has value at least \(\min(1+4\delta,18\delta)\). Thus \(\delta<1/13\) would make the seventeenth term uniquely lowest. It follows that both \(c_1,c_2\) have value greater than 1. The resulting four-marking sieve is empty.

These arguments cover the all-roots-equal-one case separately by \(c_1=c_2=0\). The coefficient \(190hX^{18}\) does not spoil \(c_4,\ldots,c_{16}\in17\mathcal O\): the relevant binomial coefficients \(\binom{18}{k}\), \(4\le k\le16\), are divisible by 17. The low Taylor coefficient identities also have their stated coefficientwise divisibility.

The only remaining occupancy has a small repeated root \(r\) and a unit \(H_2\) witness. The repeated root consumes both nonzero multiplicities in the zero cluster, so the \(G_2\) witness is exactly \(r\), giving \(h=-r^2\).

## Integral scale and transfer to the corrected jet lemma

The repeated-root equations give \(\nu(K)=\nu(r)=\eta\), \(\nu(E)=2\eta\), and \(\nu(h)=2\eta\). If \(\eta<1\), the unit displacements all have value \(\eta/16\), while the constant term \(c_2\) is uniquely smallest in \(H_2f\) at each unit root. The degree-nineteen term has value \(17\eta/16>\eta\); it has not been dropped on a false divisibility claim. This contradicts the unit witness. Hence \(\eta\ge1\) and \(\nu(h)\ge2\).

The divided \(c_2\) and \(E\) equations select only \((\bar A,\bar b)=(16,5)\), with \(\overline{K/17}=8\). They force \(\eta=1\), \(\overline{r/17}=4\), and \(\overline{h/17^2}=1\). The unit-root cluster is therefore exactly the same one required in the corrected B jet lemma: exact 1 is simple, and its sixteen other roots have scaled initial values \(\mathbf F_{17}^{\times}\).

The difference from the B comparison polynomial is the stated
\[
190h(X^{18}-816X^3+815X^2)-EX(X-1).
\]
The bracket vanishes exactly at 1. After canceling \(X-1\) in a nonzero-displacement root equation and dividing by 17, both perturbations have value at least 1. The Hasse-second equation has the same bound. The changes to \(G_4,G_{10}\) have value at least 2. These errors exceed the two-jet precision \(2/16\), so the previously audited square unit-Jacobian bound and both corrected jet equations apply. In particular no fractional intermediate correction is assumed absent.

The nonsquare obstruction forces the exact collisions \(x_4=x_{10}=y=1\). It follows that \(A=-1-6h\), \(b=209+1215h\).

## Final constants and result

Normal and optimized executions of check_arithmetic.py pass. The exact \(D,K,E\) formulas at the collisions give \(\bar D=16\), \(\overline{K/17}=8\), and
\[
\overline{E/17^2}=9+14\overline{h/17^2}=6.
\]
The residue of the small-root equation divided by \(17^2r\) is \(6+8\cdot4+16\cdot4^2=5\ne0\). Every other monomial has strictly greater valuation, including the \(hX^{18}\) term. This proves the contradiction.

No gap was found in the row-1 argument. Neither the local checker nor this audit resolves row 2, the full support A, unrestricted degree 20, or an eight-term bound.
