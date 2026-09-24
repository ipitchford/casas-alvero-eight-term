# Applications and cross-disciplinary editorial report

**Recommendation: Accept as an unrefereed research preprint, within the scope of this role.**

No required revision is identified. Two non-blocking reuse notes are recorded below. This recommendation is one contribution to the editorial synthesis; it does not independently establish mathematical correctness, novelty, external application value, or final publication approval.

## Submission and review scope

Frozen submission: editorial-submission.zip, SHA-256
f536907e982066d2b72ab175b2947dbff10abf080b3edd3e4e21cb7c7d61fa4a.

Manuscript PAPER.md, SHA-256
73d970c269f0420c54bfffb6a39b606920a34a504cf89f335696d5fb86851348.

PDF PAPER.pdf, SHA-256
55220014fb8b0be4f514797f7860deb15a2d0f99454b7011697dcf96d199c79a.

I verified all three hashes and verified that the Markdown and PDF in the frozen source directory are byte-identical to their members of the submission ZIP. The semantic review used the current PAPER.md, CLAIMS.json, README.md, AI_INDEX.md, ASSURANCE.md and LICENSES.md. The PDF's identity was checked; page-by-page visual review is outside this report.

The assigned questions were the meaning of the monomial bound, legitimate implications for future computation, the transfer conditions in the cluster lemma, potential overclaims, and safe reuse of the artifacts. I did not run new research, attempt a new full proof verification, or test an external application. I did not read this round's other reports or earlier review reports, and did not edit the submission.

### Confidence and prior involvement

Confidence is **high for the focused semantic and scope assessment**, and **moderate for practical implications beyond the supplied exact-arithmetic workflow**. No evidence about an external scientific or engineering application was supplied or is claimed.

I previously participated in developing parts of this project, including mixed-stratum arguments, row-5 finite identities, row-2 arithmetic verification, manuscript drafting, and scoped transcription checking. This familiarity helps identify where a local statement could be overextended, but it also creates substantial producer involvement and limits independent challenge. This report is therefore an internal, producer-involved editorial assessment, not a blind or unaffiliated specialist review. It must not upgrade the release's external-review or independent-reproduction status.

## Findings

### A1. The stated monomial bound has the correct semantic boundary

**Assessment: satisfactory; no revision required.**

Theorem 1 and the opening clarification specify degree twenty, characteristic zero, nontriviality, translation to the nineteenth-derivative root, and inclusion of the leading monomial in the count. The support convention then states that deficiencies are indices \(j\), corresponding to exponents \(20-j\), and that the total count is \(1+|S|\). CLAIMS.json and AI_INDEX.md reproduce the same scope.

This prevents three consequential misreadings:

1. The theorem does not assert that a nontrivial example with eight terms exists. The paper explicitly describes a hypothetical counterexample and declines a sharpness claim.
2. It does not assert the same sparsity bound for every translate. A variable translation can change coefficient support; the prescribed centering is part of the theorem.
3. Eight monomials is not a bound on roots, distinct common witnesses, or “recycled roots.” The introduction expressly distinguishes the latter literature from coefficient sparsity.

The introduction, closing support cover, and “Scope, evidence, and remaining problem” section all retain these distinctions. The result is not presented as a proof of the unrestricted degree-twenty or all-degree conjecture.

### A2. The legitimate computational consequence is an exact exclusion filter

**Assessment: satisfactory; non-blocking reuse note below.**

Assuming the theorem's proof is accepted, a search for nontrivial degree-twenty characteristic-zero CA polynomials may exclude all exact centered templates with seven or fewer nonzero monomials. The paper supplies the normalization and support-preservation argument necessary for that use.

The result does not establish the existence, number, complexity, or tractability of the remaining denser solutions. It does not provide a runtime benchmark or a numerical solver guarantee. Nor does the fourteen-support list classify all degree-twenty coefficient patterns: it is the necessary-condition frontier for exactly seven total terms, after the earlier lower-term exclusion.

The manuscript appropriately separates a nonempty characteristic-\(p\) special fibre from a characteristic-zero candidate. It also states that a coefficient which is nonzero but has zero residue must remain in the analysis, and that searching only unramified lifts is not complete. Those are important constraints for computational reuse.

**Optional note A2-N1:** Any downstream search implementation or public explainer should retain the words “exact,” “centered,” “degree twenty,” and “characteristic zero.” A floating-point threshold that deletes small coefficients is not justified by the theorem. This is reuse guidance, not a missing premise of the submitted theorem or a required manuscript change.

### A3. The cluster-collapse transfer is stated with the conditions needed for reuse

**Assessment: satisfactory; no revision required.**

Lemma 4 requires:

- a separated cluster with \(m\) roots counted with multiplicity;
- actual common witnesses for \(f\) and every \(H_kf\), \(1\leq k<m\), in that same cluster;
- the degree-\(m\) Hasse–Casas–Alvero property over the algebraic closure of the residue field.

Its proof explains why scaling by a greatest internal root distance makes the cluster factor integral with at least two distinct residue roots, while the outside factor reduces to a nonzero constant. The Hasse product rule then transfers the required incidences. These are precisely the semantic links needed between a local root configuration and a smaller-degree obstruction.

A cluster's existence, apparent multiplicity in a reduction, or possession of only some derivative witnesses would not suffice. The paper makes that limitation explicit both in the structural dependency map and in its closing discussion. Its row-2 application places all three low derivative witnesses in the four-root cluster before invoking the lemma and proves the quartic input in characteristic seventeen.

The use of Hasse derivatives is also appropriate: one should not replace this residue-field argument by high-order ordinary differentiation in positive characteristic. The submitted definitions and lemma retain the Hasse convention.

Theorem 2's “uniform” scope is likewise calibrated. It permits all intermediate coefficient positions within the stated degree-twenty stratum, but retains its exact zeros and residue hypotheses. The paper expressly declines a degree-uniform or whole-residue-row conclusion.

### A4. Broader application value is not overstated

**Assessment: satisfactory; no revision required.**

The submission is a pure-mathematical, computer-assisted sparsity result. Its claimed practical value is methodological and computational: explicit exclusions, reusable valuation reasoning, and exact certificates. It does not report validation in control theory, statistical modeling, cryptography, numerical conditioning, or another application area. No such implication follows merely from the title or from the polynomial degree.

The descriptions of reusable mechanisms are tied to explicit hypotheses. The structural dependency map calls the precision and cluster principles standard reusable reasoning and attributes the contribution to their complete application. The paper therefore does not turn the use of Newton polygons, Hensel-style precision, or modular reduction into an unsupported claim to have introduced those general methods.

I find no applications-based reason to require empirical experiments. Conversely, this report provides no basis for promising external impact, software speedups, or a significance grade. Those would require separate evidence.

### A5. Artifact reuse is adequately separated from proof and historical status

**Assessment: satisfactory; one non-blocking reuse note.**

The README and AI_INDEX identify the current manuscript and replay entry points. They distinguish the current theorem from earlier seven-term versions, historical partial computations, and working notes whose dated “open” labels have been superseded. The invalid exploratory quadratic probe is specifically labelled and excluded from authoritative replay.

The scope discussion does not convert the historical 79-of-240 row-9 work into a completed 240-system classification. It identifies the complete smaller row-9 system actually needed by the eight-term argument. It also states that the default replay does not regenerate the largest optional census and that file hashes and successful checker exits do not replace the mathematical coverage or lifting arguments.

The license map separates original prose/data from original code and does not infer rights to third-party review material. The assurance documents retain unrefereed status and distinguish internal editorial review from external peer review.

**Optional note A5-N1:** Reusers should treat the current entry points and explicitly named certificate families as authoritative for this version, rather than execute every historical script indiscriminately. A successful run of a checker for one frozen polynomial family does not certify a new family, degree, prime, support mask, or witness assignment. The existing README warnings are sufficient; no additional packaging work is required by this report.

## Required revisions and recommendation

- Critical findings: none in this role's scope.
- Major findings: none.
- Required minor revisions: none.
- Optional notes: A2-N1 and A5-N1, concerning downstream exact-computation and artifact reuse.

I recommend **Accept**, with the existing unrefereed-candidate assurance language preserved. The semantic meaning and prospective computational uses are suitably bounded. The editorial synthesis should consider this recommendation alongside the separately assigned methodology, domain, and adversarial reports; my prior producer role means it supplies no independent external validation.
