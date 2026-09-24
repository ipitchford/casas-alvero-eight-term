# Novelty and significance assessment

Search date: 23 September 2026. Disposition: **no matching positive theorem located; novelty unresolved**. This report applies the novelty-gate skill to the exact normalized claims in `target.yaml`. It does not infer priority from a search failure.

## Positive result under assessment

The proposed contribution is the exclusion of the centered degree-20 family

\[
x^{20}+ax^{15}+bx^4+cx,\qquad abc\ne0,
\]

and its consequence that any nontrivial degree-20 Casas–Alvero polynomial has at least five nonzero centered terms, including the leading term. It is not a statement about arbitrary translations or a bound on distinct roots.

The characteristic-zero proof is complete within this package: published support restrictions, exact determinant arithmetic, a modular membership identity, and a finite-module specialization argument. The package's internal audits found no fatal gap. Mathematical correctness, originality, and significance remain separate assessments.

## Closest results and overlap

| Primary source | Relevant overlap | Difference from the proposed contribution |
|---|---|---|
| [Castryck–Laterveer–Ounaïes, Theorem 2 and Proposition 15](https://arxiv.org/html/1208.5404) | Simple mean root, forbidden derivative coincidences, and a determinant divisibility condition | These supply the reduction to one family. Their application is prior art; the remaining exclusion is the candidate contribution. |
| [Massri, v6, Theorem 7.10 and Remark 7.8](https://arxiv.org/html/1806.09561v6#S7) | Degree-20 exclusion with three recycled roots, and root-placement constraints | Three nonleading terms allow the origin plus three chosen nonzero witnesses. The three-recycled-root theorem does not directly exhaust this case. |
| [Marashdeh, v1, Theorem D / Theorem 5.9 and §8](https://arxiv.org/html/2608.14726v1) | Triangular root-assignment elimination and a claimed all-degree lower bound of four centered terms | The checked text does not state the degree-20 five-term bound. The new proof need not use this unrefereed lower-bound theorem. |
| [Schaub–Spivakovsky, v1](https://arxiv.org/html/2411.13967v1) | Regularity and Macaulay-matrix/bad-prime approaches | Context for certificate methods and the open degree-20 problem, rather than the exact four-term exclusion. |

The final family uses derivative orders 15, 4, and 1. Its support indices in the convention \(x^{20-m}\) are 5, 16, and 19. Searches must account for both index conventions. “Four terms,” “four distinct roots,” and “four recycled roots” are different restrictions.

## Search coverage and fingerprints

The exact-family searches and source-by-source comparisons are preserved in [the sparse addendum](reviews/prior-art-sparse-addendum.md). Searches included the coefficient-index strings `5,16,19`, all four intermediate determinant survivors, several spellings of `x^20 + a*x^15 + b*x^4 + c*x`, degree 20/twenty, five nonzero terms, three-element support, quadrinomial, tetranomial, lacunary, fewnomial, and sparse. We inspected the relevant theorem statements and surrounding scope in the primary sources above.

The arithmetic fingerprints are the six determinant residues `15,7,10,0,12,13`, normalized coefficient `-15504`, univariate leading coefficient `-4844`, and the exact modular certificate at 31. These are recorded for future equivalence checks; their numerical uniqueness is not evidence of novelty. No natural sequence, generating function, or spectral invariant arises here, so an OEIS or eigenvalue search would not test this claim.

No matching primary theorem or exact-family exclusion was found. Search engines index formulas and computational case lists poorly. Older scenario exclusions might imply this theorem without using sparsity language; unpublished or non-indexed material was not covered. No author inquiry was made. The bounded search therefore supports specialist review of a candidate, not a priority announcement.

## Proof-audit claim and source-status corrections

The separate audit reconstructs counterexamples to Proposition 3.3 of [Ghosh v2](https://arxiv.org/html/2501.09272v2), in allowed characteristics 5 and 7. Its potential contribution is an explicit, portable explanation of the failure and the dependency consequences, not a disproof of the characteristic-zero conjecture. We did not locate the same explicit Proposition 3.3 objection in a primary public source.

The [initial status search](PRIOR_ART.md) documents three qualifications to the brief:

- Ghosh v2 is the current version in the checked arXiv history, but “the only claimed full proof” is incorrect: [Lu's 2017 preprint](https://arxiv.org/abs/1707.04754) also claims one. That claim was not adjudicated here.
- An inaccessible social-media objection mentioned by a secondary index prevents a justified “no public comment exists” conclusion. Its mathematics was not used as evidence.
- The checked specialist literature identifies degree 20 as open. [Gasull's 2026 survey](https://doi.org/10.1007/s44425-026-00047-6) instead says 24 while citing a 2011 source; it provides no new degree-20 proof. [Chellali's correction](https://hal.science/hal-00748843) explains a bad-prime omission in that older route. Connecting the survey sentence to the omission is an inference, not an author-confirmed explanation.

Finding a flaw in one proof does not by itself establish that no other proof exists. The campaign's status conclusion combines the specific audit with this bounded literature check.

## Research decision

The audit-first campaign was justified and has produced a precise positive result. The five-term bound is a modest partial advance if new. The current evidence supports a short specialist-facing proof/certificate note; it does not meet the significance of a full solution and does not establish that the full conjecture is now tractable.

Before considering publication, the key unresolved question is whether the exact exclusion is already implicit in prior computational cases or known to specialists. A broader research campaign needs a mechanism that handles denser supports or a useful infinite class, with an explicit finite pilot and a stopping condition. Repeating large searches without such a mechanism is not justified by this result alone.
