# Final manuscript integration review

**Review date:** 24 September 2026.  
**Disposition:** PASS within the scope below; no unresolved mathematical integration blocker found.

## Reviewed snapshot and scope

The reviewed assembled source is
`outputs/casas-alvero-eight-term-review/PAPER.md`, with SHA-256

```text
7b3cd1c108203dca16118d6af1c81f9dad996db5c51fc8de08ebb4b2971fd0ac
```

This review compared the foundations, the two quadratic-coefficient configurations, the inherited exclusions in Appendix B, and the final assembly with their exact source proofs and evidence. It checked the integration of hypotheses, valuation arguments, finite enumerations and support routing. A separate bounded review of the foundations and assembly independently recomputed the routing and the stated row-1 binary censuses. This was not a fresh proof review of every other manuscript section, a rerun of the full computational package, formal verification, or external peer review.

## Mathematical findings

1. **The global quantifiers and normalization are preserved.** The polynomial-equation specialization retains the exact zero and nonzero coefficient pattern. Scaling a minimum-valuation nonzero root gives integral roots and a retained unit root, so the reduction cannot be monomial. The triangular normalized-derivative recurrence gives integral binomial-normalized coefficients. The rebuilt text now explicitly covers a solution over any characteristic-zero extension and states that the residue-field scaling lifts to a unit after a finite extension. These statements justify the transition from the theorem's field quantifier to the local arguments without asserting preservation of a preselected valuation stratum.

2. **The support and residue-case assembly is complete within the stated reduction.** The fourteen displayed supports match the inventory. Their seed routing gives nineteen support/seed pairs before the exact-zero removal of the fourth seed for support \(\{2,4,10,17,18,19\}\). That removal uses the simple mean root and the exact \(G_{17}\) witness condition; it does not infer an exact zero merely from a zero residue. The three row-1 binary censuses have respectively 8, 16 and 16 markings and give the displayed sole unit-16 patterns. The closing table assigns every remaining routed case to an exclusion proved in the paper or its inherited appendix.

3. **The unified quadratic argument retains the hypotheses of both source proofs.** The shared proof that the ordinary quadratic coefficient has valuation at least one uses the first- and second-derivative witness occupancy and remains valid with the positive-valuation \(a_2\) term. The stronger \(\nu(a_2)\geq2\) bound is invoked only after a small witness is known to exist. The first divided sieve retains all eight binary markings for the larger family and the four canonical markings for its exact-zero subfamily. The second-jet argument includes the degree-19 contribution to the second Hasse derivative. It establishes the unit Jacobian and residue-field restriction before using the nonsquare discriminant. The final exact evaluations give residues 8 and 5 in the two families. The manuscript does not rely on the superseded exploratory jet computation that omitted the degree-19 contribution.

4. **The inherited eighth-seed exclusion transfers correctly over ramified extensions.** The lower bounds on the small-root coefficients justify coefficientwise division by 17. All four residue witness choices are retained, including active coefficients with zero residue. The seven support-specific enumerations contain 1,216 markings in total and are empty already after the divided identity. No collision filter is needed for this exclusion.

5. **The inherited fourth-seed exclusion has the stated exhaustive scope.** For middle indices \(\{4,10,12\}\), the two critical orientations and \(17^3\) witness choices give 9,826 oriented markings. The two conjugate survivors have the recorded common coefficient data. The identification of the simple witnesses, the square system with unit Jacobian, and the critical-value calculation agree with the source proof. The nonzero residue \(9+4\alpha\) after division by \(17^2\) excludes arbitrary ramified lifts; the argument does not assume unramified roots or integer-valued valuations.

6. **The inherited ninth-seed exclusion preserves the cluster and lifting conditions.** The simple mean forces the relevant coefficients to vanish exactly. The low-derivative witnesses occupy the triple cluster at 1, and the good-characteristic cubic collapse gives the exact triple root. The enlarged square model retains the root near 1 as a variable until the additional divided condition is checked. The complete 4,913-marking enumeration has the recorded single survivor; its divided obstruction is \(3179=11\cdot17^2\pmod{17^3}\). The unit-Jacobian argument provides the precision comparison needed for arbitrary ramified solutions.

The conclusion is the centered **at-least-eight-nonzero-terms** statement. The assembly neither proves unrestricted degree 20 nor the full Casas–Alvero conjecture, and it does not assert sharpness.

## Transcription and assembly corrections

Two mathematical typesetting corruptions were reported during review: a missing backslash in `\qquad` and a missing backslash in the thin space inside a witness exponent. Both are corrected in the reviewed snapshot. Five stale relative links to the mixed-configuration and fifth-seed reproduction files were also reported; all local Markdown links in the reviewed snapshot resolve. The two normalization clarifications described in item 1 are present in the final text.

No remaining substantive correction is requested for the reviewed sections.

## Principal comparison sources

- `work/casas-alvero-upgrade/final-manuscript/FOUNDATIONS.md`, `ASSEMBLY.md`, `QUADRATIC.md`, and `INHERITED.md`.
- `work/casas-alvero-upgrade/next-stage/last-four/quadratic/B/B_EXCLUSION.md`, `B_AUDIT.md`, and `check_B.py`.
- `work/casas-alvero-upgrade/next-stage/last-four/quadratic/A/A_ROW1_EXCLUSION.md`, `A_ROW1_AUDIT.md`, and the corrected arithmetic/second-jet evidence.
- `work/casas-alvero-upgrade/research/SEVEN_TERM_FRONTIER.md`.
- `work/casas-alvero-full/tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md` and `ROW4_SMALLEST_SUPPORT_AUDIT.md`.
- `work/casas-alvero-full/collective17/exclusions/BATCH1_PROOF.md`, `lift-batch.json`, and `check_batch.py`.
- The characteristic-17 classification, its audit, and the support-frontier inventory, together with their packaged copies under `evidence/full/`.

The computational checks reported elsewhere in the bundle have their own receipts. This integration review does not replace those receipts or enlarge their scope.
