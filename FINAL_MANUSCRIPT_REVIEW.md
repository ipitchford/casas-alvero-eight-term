# Final assembled-manuscript consistency review

**Outcome: no substantive error or overclaim found within this bounded
consistency review.** The reviewed files are the assembled `REPORT.md`,
`FINAL_COVERAGE.json`, `REVIEW_GUIDE.md`, and `M6_COVERAGE_REVIEW.md` in
`outputs/casas-alvero-review`. This pass compared statements with the packaged
proof notes and recorded JSON. It did not rerun a census, launch new research,
recheck the complete literature, or independently reprove every theorem.

## Batch counts and complete support coverage

The three displayed batches were reconstructed directly from their packaged
`residue-batch.json` and `lift-batch.json` files. For every system, its support,
active indices, marking count, survivor count, Frobenius-orbit count, maximum
recorded precision, exclusion status, and batch label agree with its entry in
`FINAL_COVERAGE.json`.

| Active middle size | Systems | Markings | Residue survivors | Orbits |
|---|---:|---:|---:|---:|
| 3 or 4 | 7 | 506,039 | 20 | 7 |
| 5 | 21 | 29,816,997 | 113 | 48 |
| 6 | 51 | 1,231,016,019 | 686 | 252 |
| Total | 79 | 1,261,339,055 | 819 | 307 |

The 79 support lists are distinct. Their disjoint union with the 161
`remainingSupports` is exactly the 240-support canonical presentation.
Every lifted orbit is recorded as excluded; the orbit sizes sum to its
system's residue-survivor count. The displayed precision counts are correct:
811 markings are excluded at precision 2, six at precision 3, and two at
precision 4. These are powers of 17, not counts of characteristic-zero points.

The m=6 coverage review and main report agree on the 46+5 timeout recovery,
652+34 residue survivors, the full replay's byte equality, and the absence
of a second independent exhaustive implementation for that batch. The report
correctly distinguishes this same-algorithm repeat from independent survivor
and higher-precision arithmetic.

Other displayed census figures were checked against their packaged JSON:
the two-adic initial counts 873/1,128 coefficient patterns and 65,536
markings per type; the saturated counts 465/603 and 40,960 per type; the
occupancy totals 1,068 patterns and 77,820 markings; row 8's 67,108,864
initial markings, 233,310 divided-identity survivors and 180,341 remaining
markings; its 179,765 versus 576 scale partition; the 209 reduced quartic
models; and the cross-prime pattern/marking table. No mismatch was found.

## Mathematical and verification scope

The report consistently retains the following distinctions:

- The proof audit refutes the stated positive-characteristic generality of
  Proposition 3.3. It does not present a characteristic-zero CA counterexample
  or infer that the claimed theorem's conclusion is false.
- The sparse theorem concerns at least seven centered monomials, including
  the leading one. The six-term C argument states its exact nonzero support;
  lower-support degenerations are assigned to preceding results.
- Only row 3 is excluded as an entire characteristic-17 seed. The 79 row-9
  exclusions and the one row-4 exclusion retain their coefficient-support
  scope. The other 161 canonical row-9 systems remain unexecuted.
- Ramification is not removed by a residue search. The prose supplies the
  unit-Jacobian uniqueness or coefficientwise divisibility argument required
  by each lift, and distinguishes the moving root near one in the computational
  row-9 subsystem from the exact triple root of a genuine candidate.
- Row 4's quadratic description retains both signs and an untested scalar
  equation. Its local degree bound is not represented as a whole-row exclusion.
- The row-8 quartic conclusions are confined to `J=L=16`; the next-lift
  exclusion retains the conditions `a17=a18=0` and exact mean witnesses.
  Neither the exceptional markings nor the other quartic placements vanish
  from the stated remaining work.
- Reduced point counts are distinguished from algebra lengths. Finite formal
  covers and finite free algebras are not said to have empty generic fibres.
  The row-9 norm remains unevaluated in general.
- The all-degree section distinguishes proved inequalities, equivalent
  formulations, and countermodels to weakened arguments. Neither unrestricted
  degree 20 nor the full conjecture is claimed proved. Internal AI reviews,
  finite arithmetic checks, novelty, external refereeing, and formal
  verification remain separate assertions.

The earlier manuscript defects in the polynomial-unit expression and the
integral-family fraction are corrected in the assembled report. A scan found
no remaining nonprinting control characters other than ordinary newlines and
tabs in the three reviewed Markdown files.

## References and assembly state

All 60 explicit local Markdown destinations or fully qualified backtick
`evidence/...` references checked in the requested Markdown files exist in
the package. The original row-9 `REPORT.md` and `COVERAGE.json` in the evidence
have been updated to the same 79/161 endpoint, so the guide does not send the
reader to a conflicting earlier batch total. This was an existence and
consistency check, not a fresh external-link or bibliographic audit.

At the review snapshot, the guide's top-level `REPORT.pdf` and `CHECKS.md`
were still being generated by the parallel rendering/replay work. They were
not yet present. Their final existence and agreement with this source remain
an assembly check for the parent task before packaging; this review does not
claim to have inspected the rendered PDF or the unfinished replay summary.
`PROOF_INDEX.md`, `MANIFEST.json`, `M6_REPLAY.json`,
`M6_COVERAGE_REVIEW.json`, and `replay.py` were present.

Reviewed source fingerprints:

| File | SHA-256 |
|---|---|
| `REPORT.md` | `7ab1494deac78179b173ffcadd68e21f6d80c72b2f363a27fab7c9781b2aa21e` |
| `FINAL_COVERAGE.json` | `e62025e1a557de21a6ea375a2bf496ada17eaa6c267c5ea75d7e1a4a3e4dc52a` |
| `REVIEW_GUIDE.md` | `c41fbd0c2a9514ed6aff8638102ac90e4487c3fdb101755d15a6743be30d1d2a` |
| `M6_COVERAGE_REVIEW.md` | `72921deae999c6b64b7b35fc20cb8f831f75017428418fd2447ce12de2a8a808` |

No mathematical correction is requested by this pass. Final rendering,
replay-summary completion, manifest regeneration, and archive integrity
remain separate closeout operations.

## Final-assembly addendum — 23 September 2026

**PASS.** `REPORT.pdf` and `CHECKS.md` now exist, resolving the two outstanding
file-existence checks above. The PDF has a valid PDF header and is 235,825
bytes. This addendum does not substitute for the parent's rendered-page
inspection and does not claim a second visual review.

The final `REPORT.md` SHA-256 is
`beb7c080b3b27f27e29c8cd0f3ce09a42f4a4990040fd83a6816200b5de21612`.
Its sole change since the reviewed fingerprint above is four inline-math
wrappers around the existing powers of 17 in the precision-count paragraph.
Removing exactly those wrappers reproduces the previously reviewed SHA-256
byte for byte. The mathematical text and counts are therefore unchanged.
The control-character scan still passes. The other three requested files
retain their previously recorded fingerprints.

`CHECKS.md` was reconciled with `verification/replay/REPLAY.json`: there are
exactly 27 distinct listed top-level checks, all `PASS` with exit code zero.
Each table name, recorded duration, and output path agrees with the receipt.
All 27 output-log hashes match their recorded values. The child durations
sum exactly to 47.411 seconds. The receipt confirms inclusion of the optional
SymPy integral-syzygy check and the saved m=6 certificate check, while
`m6FreshCensusIncluded` is false. The prose correctly says this default
replay did not perform a third exhaustive m=6 census and preserves the
same-algorithm qualification for its earlier complete repeat.

Final assembly fingerprints additionally checked:

| File | SHA-256 |
|---|---|
| `REPORT.pdf` | `23bf8e98a06fe8e47d08f0bdb598d097a5006823a939054eb4af04eff696e294` |
| `CHECKS.md` | `a2d1b0745c939b2332208513364f746789ff1184ecc7e4876f4eef565660c897` |

No checker, census, rendering, or proof computation was rerun for this
addendum. ZIP extraction/CRC and final manifest checks remain the parent's
last packaging step; this addendum does not attest to an archive not yet
created.
