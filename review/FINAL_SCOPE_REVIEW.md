# Final eight-term manuscript: scope and citation review

24 September 2026. Reviewed outputs/casas-alvero-eight-term-review/PAPER.md against the completed local audits, INVENTORY_AUDIT.md, FINAL_RESEARCH_LITERATURE.md and EIGHT_TERM_ASSESSMENT.md. This is an assembly, scope and citation review, not a new exhaustive arithmetic replay.

**Decision: PASS on mathematical scope, proof-dependency presentation and calibrated novelty claims.** The small presentation fixes listed below should be applied before freezing the final rendering. No new substantive mathematical or attribution issue was found.

## The theorem and complete cover

The title, abstract, introduction, main theorem and conclusion consistently give an eight-total-term lower bound for nontrivial characteristic-zero degree-20 CA polynomials after centering at the mean. They count the leading term, distinguish deficiencies from exponents, and do not claim sharpness or an actual eight-term counterexample. The abstract and conclusion explicitly distinguish this result from unrestricted degree 20 and the all-degree conjecture.

The proof architecture is complete as stated: Appendix A supplies the earlier exclusion of six or fewer total terms; the independent inventory leaves exactly fourteen exact seven-term supports; the seed table covers the full residue-field closure; the closing table assigns every compatible branch to its exclusion. The apparent row-4 branch of \(S_{13}\) is removed by an exact simple-root implication, not by assuming a nonzero coefficient has nonzero residue. The global assembly does not claim that the larger 240-system project is complete.

The arithmetic inventory counts agree with the independently replayed result \(6188\to586\to348\to14\). The text correctly makes the extra Massri filter unnecessary and does not treat fourteen as a fraction of the unrestricted incidence problem.

The integrated quadratic-family presentation combines the separately audited A row-1 and B proofs consistently. Its general occupancy argument proves \(F\in17\mathcal O\) for both; the \(h\)-coefficient precision needed in the small-derivative cases is established before reducing \(E/17\). The three-root unit-Jacobian bound, the essential degree-nineteen term, and the final distinct residues 5 and 8 are retained. The row-2 section preserves its full leading-degeneration analysis and the quartic cluster hypothesis.

The uniform theorem now includes \(a_3=0\) and nonzero \(a_3\), with \(a_4\) allowed. The older controlled-field argument is correctly described as an alternative on a narrower stratum. It is not presented as an additional global theorem or a necessary assumption for the stronger direct proof.

## Citation and originality checks

The imported mean-simplicity and determinant claims are attributed to CLO Theorem 2 with the correct missing-deficiency indexing. The discussion credits its prior ramification argument and does not claim that prime-adic reasoning, Hensel arguments or Newton polygons originate here.

The de Frutos thesis is explicitly credited for the older singleton/two-visible tests and the weaker implicit five-term consequence. The bibliography distinguishes its title-page, defense and repository dates. The implemented two-visible formula and degeneration guards have a direct derivation, so the paper does not rely on an unspecified equation in an unavailable source.

Massri is cited for witness-placement, perturbation and three-recycled-root results, with the distinction between recycled-root count and monomial count maintained. The current v6 scope is used; earlier withdrawn versions are not promoted to a full proof. Marashdeh is credited for triangular support reductions, with its preprint status and exact version retained. Its existence does not become an unsupported novelty or proof-clearance claim.

The references, dates and versions are consistent with the same-day primary-source checks recorded in FINAL_RESEARCH_LITERATURE.md. ProofAtlas's exact-system equivalence and the missing Shih thesis full text remain explicitly unresolved. The manuscript does not turn the bounded negative search into a universal “first” claim. No unverified full-proof claim is used as an input.

The bibliography contains some explanatory research-history annotations that could be shortened for a journal's house style, but they do not create a substantive scope error. The general preparation reference to Berger concerns supporting local material rather than a claimed new preparation theorem.

## Assurance and significance wording

The paper distinguishes exact finite identities from the valuation and coverage arguments that make them applicable. It also distinguishes internal audits, supplied earlier external arithmetic checks, current external peer review, and proof-assistant certification. Its reproduction claims retain the boundary between bounded default replay and a longer optional census.

The paper makes no research-grade claim. Its description is compatible with the updated assessment: a materially stronger specialist result and publication case, with strong-three-star significance and unconditional priority still unconfirmed. It introduces no author, affiliation, funding or competing-interest declaration unsupported by the supplied information.

## Presentation fixes requested before final freeze

These refer to the draft read during this review; line numbers can move during regeneration.

1. In equation Q7, the text near line 680 reads \(H_1,qquad\). Restore the missing backslash so the intended mathematical spacing command is rendered.
2. In the triangular residue recurrence near line 688, remove the spurious comma from the exponent of \(\rho_j\): it should be \(j-i\).
3. Five Markdown evidence links do not resolve from the output paper's directory. Replace their initial relative path with the bundled research path:
   - mixed-stratum checker near line 597;
   - row-5 unit certificate near line 1505;
   - row-5 first-divided, unit and jet checkers near lines 1675, 1677 and 1680.
   All should point within research/next-stage/.
4. The Marashdeh bibliography annotation near line 2475 still contrasts its result with a seven-total-term theorem. Update this to the current eight-term statement, preferably naming its actual four-term theorem for comparison. The existing sentence is not false, but it is stale.

None changes the mathematical result. This review approves the stated scope after these straightforward presentation corrections; it does not independently certify the PDF rendering, archive hashes or a subsequent publication action.

## Resolved final pass

The regenerated PAPER.md was rechecked on 24 September 2026. Its SHA-256 is **7b3cd1c108203dca16118d6af1c81f9dad996db5c51fc8de08ebb4b2971fd0ac**.

Both equation fragments are corrected: Q7 has the intended spacing command, and the residue recurrence has exponent \(j-i\) with valid TeX spacing. All five requested evidence links now resolve within research/next-stage/. A scan of every local Markdown link in the paper found no missing target. The Marashdeh annotation now explicitly contrasts the cited results with the current eight-term lower bound.

README.md, REVIEW_GUIDE.md and FINAL_REVIEW_RESPONSE.md were also read. They consistently identify the current eight-term theorem, fourteen exact supports and nineteen compatible support/seed cases; distinguish obsolete working-note status and the invalid exploratory quadratic probe; and retain the internal-review, replay, priority, significance and nonpublication boundaries. No inconsistent current-status claim was found.

**Final resolved decision: PASS. No outstanding scope, citation or presentation correction remains from this review.** This decision concerns the manuscript source and the listed review documents; PDF visual validation and final artifact-integrity checks remain their separately recorded tasks.
