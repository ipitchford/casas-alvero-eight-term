# Devil's Advocate report

**Decision: Minor Revision.**  
**Date:** 24 September 2026.  
**Critical findings:** 0. **Major findings:** 0. **Minor findings:** 2.

## Frozen target and review independence

The reviewed archive is `editorial-submission.zip`, SHA-256:

```text
f536907e982066d2b72ab175b2947dbff10abf080b3edd3e4e21cb7c7d61fa4a
```

Its current manuscript hashes are:

```text
PAPER.md  73d970c269f0420c54bfffb6a39b606920a34a504cf89f335696d5fb86851348
PAPER.pdf 55220014fb8b0be4f514797f7860deb15a2d0f99454b7011697dcf96d199c79a
```

I verified these archive hashes and checked that the working manuscript, assurance/provenance documents, README, environment description, new replay runner, CI configuration and assembly checker read in this round match the archived bytes. I did not edit the submission, read another report in this round, consult old review reports, spawn reviewers, rerun the large censuses, or conduct a new research campaign. This report concerns the mathematical text and selected proof code; it is not a fresh visual audit of the PDF.

**Prior producer conflict:** I previously contributed research arguments, arithmetic audits, the quadratic-family manuscript section, and an integration review within this same project. This is therefore a producer-involved internal adversarial review, not an independent external referee report. The current reading did not rely on prior verdicts as evidence. My involvement nevertheless limits the independence of an absence-of-error judgment and must remain disclosed in any editorial synthesis.

## Strongest counterarguments examined

### Arbitrary ramification has not been replaced by an unramified search

The strongest potential failure would be an inference from an empty finite-precision unramified lift search to absence over arbitrary ramified extensions. I did not find that inference in the inspected proof. Lemma 3 is a minimum-valuation argument: an integral invertible Jacobian preserves the minimum coordinate valuation, while the quadratic remainder has strictly larger valuation. It compares an already assumed exact solution with an approximation; it neither asserts existence of a lift nor assigns the exact solution to the approximation's coefficient field. Its proof does not require integer-valued valuations or completeness.

The applications I checked provide the relevant precision rather than silently applying the lemma to undivided equations. In particular:

- The quadratic-family second-jet argument retains the degree-19 term of the second derivative, establishes the first-order unit-Jacobian bound before passing to the second residue equation, and only then uses the nonsquare discriminant over the forced prime-field residue data.
- The second-seed argument first proves integral-order bounds on its two initially fractionally valued parameters. Its simple outside-root estimates precede the cluster model and the final divided residual calculation.
- The fifth-seed proof uses finite coefficientwise polynomial identities for its starred and perturbed families. It retains a possibly nonzero witness displacement in Case 6 and proves that its contribution has valuation greater than the obstruction precision.
- Appendix A's final characteristic-13 family does not round fractional valuations up to integers. The troublesome triple cluster gives only a half-order bound until an additional simple middle-derivative condition justifies stronger precision.
- Appendix B's fourth- and ninth-seed obstructions attach their saved finite-precision values to square systems with unit Jacobians. Their nonzero residuals are consequently obstructions to any exact solution in the relevant residue class, not just to a selected unramified lift.

### Residue coincidence is not being mistaken for exact collision

The main collision arguments count roots with multiplicity in separated subclusters. In the uniform and mixed first-seed arguments, the selected witness and a repeated root exhaust a size-two cluster. In the second-seed argument, the four-root inner cluster contains every required low derivative witness before the good-characteristic collapse lemma is applied. The separated-cluster lemma uses a greatest internal root distance and an outside factor reducing to a nonzero constant; the Hasse product rule then transfers the required incidences. The existence of a cluster alone would not establish the conclusion, but the manuscript supplies the occupancy conditions where the lemma is used.

I found no missing collision alternative in these inspected arguments. In particular the uniform theorem treats the exact-zero and nonzero cases of its cubic normalized coefficient separately, including the half-order displacement boundary and the exactly normalized witness.

### Coefficient degeneration and algebraic residue fields are retained

The support sieve concerns exact characteristic-zero support. Subsequent reductions retain active coefficients with zero residue. The characteristic-17 classification covers the successive zero-coefficient charts; the all-zero chart is excluded by the retained unit root, not by an assumed generic coefficient. Its resultant identities and the smaller affine-pair gcd arguments are algebraic-closure statements rather than searches over prime-field points.

The fourteen-support cover and nineteen routed seed pairs have compatible scopes. The apparent fourth-seed branch of the thirteenth support is removed by an exact common-witness argument at a simple mean, not by interpreting a zero residue as an exact zero. The assembly checker explicitly labels itself as routing and receipt verification. It does not purport to prove the polynomial exclusions merely by hashing source notes.

### Package success is not presented as mathematical or external validation

The manuscript, README and machine claim distinguish the centered eight-term bound from unrestricted degree twenty, the full conjecture, sharpness and arbitrary translates. Historical partial censuses and the invalid superseded quadratic probe are explicitly separated from the current proof. The replay runner includes the row-8 dependency and describes its arithmetic scope. The assurance document does not authenticate the unavailable third-party audit archive, promote the internal editorial gate to external refereeing, or claim formal certification. These are material safeguards, not reasons to relax scrutiny of the proof.

## Required minor revisions

### DA-1 — Specify the integral valuation ring in Lemma 3

**Location:** `PAPER.md`, Lemma 3, line 195.

The opening phrase is “Let \(\mathcal O\) be a valued ring.” The proof uses nonnegative coefficient valuations, a residue maximal ideal, and an integral inverse to a unit-determinant matrix. Those are clear for the valuation ring of a nonarchimedean valued field, which is the setting of every application. “Valued ring” alone is less precise and can be read as merely a ring equipped with a valuation without the needed nonnegative-value convention.

**Requested change:** say “Let \(\mathcal O\) be the valuation ring of a nonarchimedean valued field,” or explicitly define the equivalent integral convention. The extension sentence should refer to the extended valuation ring. No change to the proof, numerical conclusion, or ramification scope is required. This is a statement-precision issue; I have not found a counterexample in the intended setting.

**Confidence:** high.

### DA-2 — Distinguish configured Linux CI from executed Linux CI

**Locations:** `ASSURANCE.md`, environment-reproducibility bullet; `ENVIRONMENT.txt`, final sentence.

The phrases “with recorded versions and Linux CI” and “CI records additional Linux versions” can be read as reporting completed Linux runs. The inspected frozen target includes an Ubuntu workflow with Python 3.11/3.13, while the environment record identifies a local macOS publication run. A workflow file is a reproducibility provision, not an execution receipt.

**Requested change:** describe the Linux CI as an included/configured workflow unless an actual run receipt is linked. Keep any subsequent successful public CI run as separately dated execution evidence. This does not affect the mathematical result or the reported local checks.

**Confidence:** high that the present wording is ambiguous; no claim is made that an uninspected Linux execution is impossible or absent elsewhere.

## Overall judgment and limits

The strongest anticipated objections—unramified-only reasoning, omitted coefficient-loss charts, unjustified exact collisions, and conflation of saved arithmetic with a global theorem—did not produce a Critical or Major finding in this bounded reading. The two minor revisions improve statement and assurance precision and do not require a new proof campaign.

Confidence is **moderate** in the absence of a substantive gap across the inspected arguments and **high** in the scope of the two identified wording issues. The remaining limitations are the length and computer-assisted nature of the argument, dependence on exact finite certificates not fully regenerated in this role, unresolved priority comparisons already disclosed by the submission, and the prior producer conflict above. Acceptance after these minor corrections would support release as an **unrefereed candidate**; it would not constitute external validation of the theorem.
