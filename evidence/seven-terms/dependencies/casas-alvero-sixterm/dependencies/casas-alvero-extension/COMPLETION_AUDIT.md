# Completion audit for the agreed research round

23 September 2026. This checks the scope of the explicit goal, not completion of the Casas–Alvero conjecture.

| Required work | Evidence | Assessment |
|---|---|---|
| Seek a simpler, reusable explanation of the old four-term exclusion | `reviews/EXPLANATION.md`: valuation support lemma, four disjoint support sets, and constant identity at 3 | Achieved. The old bound is also recognized as prior work. |
| Test extension to all centered five-term degree-20 polynomials | `PROOF.md`, Corollary 2; `check_support_and_lift.py`; independent 680-support enumeration and modular audits | Achieved: all cases are excluded, yielding at least six total centered terms. |
| Find a structurally meaningful broader result or make an evidence-based stop | `PROOF.md`, Theorem 1 and Lemma 3; `reviews/BROAD_SUPPORT_AUDIT.md` | Achieved: a complete finite-field support exclusion yields an explicit restriction for every degree 20 times a power of 13. This is a partial theorem, not a full-degree solution. |
| Check prior computational cases and equivalent formulas | `NOVELTY_REPORT.md` and source-linked `prior-art/` reports; reconstructed Massri masks | Achieved within the stated search boundary. Two collisions are recorded. Priority of the final seed and consequences remains unestablished. |
| Deliver exact proofs and replayable evidence | Integrated proof, compact arithmetic checker, support checker, supplemental independent membership certificate, frozen receipts | Achieved, subject to the archive replay receipt accompanying this package. Finite checks are not substituted for the all-exponent proof. |
| Keep correctness, novelty, significance, and full-conjecture status separate | README, theorem statements, novelty report, correction, and internal review scopes | Achieved. No publication or outreach was performed. |

The original research turn made concrete progress; it was not a wait or a status-only turn. The closing replay checks the extracted artifact against its manifest and frozen arithmetic receipts. All computational probes in this round have terminal results, including recorded timeouts and proper ideals; none is being treated as a successful exclusion.

No additional promise to solve arbitrary degrees, establish absolute historical priority, obtain external refereeing, or publish the result was part of this bounded research-round goal. Those outcomes have not been claimed.
