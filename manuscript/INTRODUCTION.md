# Introduction

The Casas–Alvero condition requires a polynomial to share a root with each of its nonconstant proper derivatives. The conjecture asserts that, in characteristic zero, every such polynomial is a power of a linear polynomial. We study the coefficient support of a hypothetical counterexample of degree twenty.

**Theorem 1 (eight-term bound).** After translating the root of its nineteenth derivative to zero, every nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least eight nonzero monomials, including its leading term.

The centering in the statement is essential: we do not assert the same monomial count for every translate. The theorem is a sparsity restriction, not a proof of the conjecture in degree twenty, and it does not assert that the bound is sharp.

The proof has two parts. Arithmetic restrictions reduce a seven-term candidate to fourteen exact supports. We exclude every compatible residue branch of these supports, using a complete classification of the characteristic-seventeen visible model and local lifting arguments. An earlier stage of the argument excludes six or fewer terms; its full proof is retained in Appendix A, including the characteristic-thirteen calculation for the last six-term family. The final fourteen-support enumeration is reproduced independently and does not require the extra support filter present in historical code.

The local arguments retain coefficients that are nonzero but have zero residue, and they allow arbitrary ramification. This matters because a nonempty special fibre is not itself evidence of a characteristic-zero counterexample, and a search for lifts in an unramified ring need not cover all candidates. The proofs instead control every actual common-root witness through valuations, multiplicities, and exact integer identities.

Three mechanisms are useful beyond the individual support list. First, a uniform theorem excludes a specified residue stratum while allowing all its intermediate coefficient positions to be active. A common derivative root is forced to equal a repeated root; their next nonzero jets are incompatible. Second, a shared second-order calculation excludes two quadratic-coefficient families by a nonsquare discriminant, with the precision justified by a unit Jacobian. Third, in the last residue branch, the first nontrivial cluster model forces all low-order witnesses into a four-root cluster. The characteristic-seventeen quartic CA theorem collapses that cluster, after which a simple-root lift has a nonzero residual. These are local statements with explicit hypotheses, not a degree-uniform exclusion theorem.

Prime-adic constraints and determinant restrictions were developed by Castryck, Laterveer and Ounaïes [CLO]. De Frutos Marín's singleton and two-visible-position criteria [deFrutos] provide part of our support sieve; their combination with the published restrictions already gives the weaker five-term bound, which is not claimed as new. Massri [Massri] gives related witness-placement and perturbation methods, including a theorem about three recycled roots in degree twenty. A bound on the number of recycled roots is distinct from a bound on the number of nonzero coefficients. Marashdeh [Marashdeh] develops related triangular support reductions. Our contribution is the complete exclusion beyond the imported restrictions, not the introduction of reduction modulo a prime, Hensel lifting, or Newton polygons.

Ramification also has a precedent in [CLO]: the remark following Proposition 19 excludes degree-\(p+1\) candidates whose roots lie in an extension unramified at \(p\). Our degree-twenty characteristic-seventeen arguments impose no such condition on the candidate's field. The controlled-field argument retained in the supplement is an alternative proof on a narrower stratum; the direct jet proof in the main text is shorter and covers its missing boundary.

The primary-source comparison found no exact predecessor of the eight-term statement in the inspected material. This is a bounded comparison, not unconditional priority clearance. Two specific source questions remain: the equivalence of the systems behind ProofAtlas's reported degree-twenty work, and the unavailable full text of Shih, Cheng-Pang's 2022 thesis. The comparison and its limits are recorded in the review supplement. Ghosh [Ghosh, version 2, 21 March 2026, Theorem A] claims the full characteristic-zero conjecture in all degrees. That unrefereed claim is not a premise of this paper. The supplementary audit concerns a positive-characteristic auxiliary assertion in that argument; such an objection does not by itself refute its characteristic-zero conclusion. We retain the priority qualifications above.

All finite checks used below have explicit input families, complete residue domains, and precision-transfer arguments. The accompanying archive contains the integer certificates, independent reconstructions, and executable replay. The resulting manuscript is a computer-assisted proof for review; its internal audits are neither external refereeing nor proof-assistant certification.

## Structural dependency map

| Result | Hypotheses and role | Uses |
|---|---|---|
| Theorem 1 | Centered nontrivial degree twenty; at least eight terms | Appendix A for fewer terms; complete fourteen-support cover for seven terms |
| Theorem 2 | Degree twenty, prime seventeen, exact and residue coefficient conditions displayed in its statement | Integral normalization, root multiplicities, exact second jet |
| Lemma 3 | Integral polynomial system, unit Jacobian and residual precision | Transfers finite precision to arbitrarily ramified candidates |
| Lemma 4 | A separated cluster of size \(m\), all derivative witnesses through \(m-1\), and the residue-field CA property in degree \(m\) | Collapses the cluster exactly; applied with \(m=4\), residue characteristic seventeen |

Theorem 2 is uniform in coefficient choices within its stated degree-twenty stratum, not across degrees. Lemmas 3 and 4 isolate standard reusable reasoning; the new contribution is the complete application and resulting support bound. The closing support table supplies the remaining case-specific implications.
