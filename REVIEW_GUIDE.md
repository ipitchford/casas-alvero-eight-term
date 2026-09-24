# Guide to the completed eight-term candidate

## Scientific claim and argument

PAPER.pdf is the current scientific manuscript. The main theorem concerns **centered monomial count** for degree twenty. It is not a distinct-root count, a recycled-root count, or a proof of the full conjecture.

The proof first specializes an assumed complex solution while preserving exact support and normalizes it in an arbitrarily ramified extension of Q_17. The support inventory leaves fourteen seven-term supports, and the complete geometric seed classification leaves nineteen compatible support/seed cases. Appendix A excludes fewer terms. The remaining sections give local exclusions for all seven-term cases. Active coefficients may have zero residue; witness residues range over the algebraic closure, not merely the prime field.

Read [the assembly audit](research/next-stage/coverage/EIGHT_TERM_AUDIT.md) alongside the main paper's two coverage tables. It supplies an explicit route for every support/seed pair and checks that the inherited lower-term theorem is complete and noncircular.

## New mechanisms and independent argument audits

- Uniform row-1 second-jet obstruction: [proof](research/next-stage/last-four/boundary/DIRECT_JET_THEOREM.md), [audit](research/next-stage/last-four/boundary/DIRECT_JET_AUDIT.md), [second audit](research/next-stage/last-four/middle/DIRECT_JET_AUDIT.md).
- Mixed middle-coefficient strata: [proof](research/next-stage/last-four/middle/MIXED_STRATA.md), [audit](research/next-stage/last-four/middle/MIXED_AUDIT.md).
- Quadratic family B: [proof](research/next-stage/last-four/quadratic/B/B_EXCLUSION.md), [audit](research/next-stage/last-four/quadratic/B/B_AUDIT.md).
- Quadratic family A, row 1: [proof](research/next-stage/last-four/quadratic/A/A_ROW1_EXCLUSION.md), [audit](research/next-stage/last-four/quadratic/A/A_ROW1_SECOND_AUDIT.md).
- Family A, row 2: [proof](research/next-stage/last-four/row2/ROW2_PROOF.md), [independent audit](research/next-stage/last-four/row2/ROW2_AUDIT.md). The separated-cluster lemma and characteristic-17 quartic argument are written in full.
- Row 5, all six final cases: [proof](research/next-stage/ROW5_COMPLETION.md), [audit](research/next-stage/ROW5_COMPLETION_AUDIT.md).
- Fourteen-support inventory: [independent audit](research/next-stage/coverage/INVENTORY_AUDIT.md).

These are separate internal agent reviews, not independent human refereeing. Source hashes identify the versions audited. The final manuscript transcription and scope reviews are under `review/FINAL_*` and `manuscript/INTEGRATION_REVIEW.md`.

## Replays and assurance limits

`replay_new.py` names the sixteen new checkers explicitly and runs each with and without Python optimization. It includes independent reconstructions of the direct jet and row-2 arithmetic. Its assembly checker checks routing, saved-record consistency and input fingerprints; it does not prove the referenced valuation implications or independently rerun a census.

`replay.py` retains the earlier default replay (twenty-six checks, plus one optional SymPy check when available), which supplies the inherited seed, lower-term, and local certificate dependencies. The full optional m6 census is a separate historical calculation and is not necessary to the present theorem.

Current publication run records are in `verification/publication/`. The earlier `verification/eight-term-new/` and `verification/eight-term-inherited/` records remain historical. `verification/FINAL_PACKAGE_QA.json` records manuscript and archive-preparation checks. The final archive checksum is supplied alongside the ZIP, rather than recursively included in the archive's own manifest.

## Significance and remaining limits

The completed eight-term bound is materially stronger than the earlier partial frontier. The literature comparison attributes the published arithmetic restrictions, missing-index determinant and older sparsity tests to their sources. The bounded search did not find this exact eight-term theorem, but equivalence with some reported work remains unresolved. See [the current assessment](review/EIGHT_TERM_ASSESSMENT.md).

Neither publication nor a research-rating outcome follows from an internal PASS. The conjecture for supports with eight or more centered monomials is not resolved here. No claim is made that the characteristic-positive gap audit of another paper alone proves the underlying characteristic-zero conjecture open.
