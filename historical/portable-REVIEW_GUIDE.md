# Review guide

**Neither unrestricted degree 20 nor the full Casas--Alvero conjecture is
proved.** This is an unpublished report of partial results and audited
obstructions, supplied for mathematical review. No publication decision or
novelty claim follows from the package.

## Start here

1. Read `REPORT.pdf` (or its editable source `REPORT.md`). It consolidates
   the mathematical statements, proofs, qualifications, and references.
2. Consult the table below for the full proof of a particular claim.
3. Use `PROOF_INDEX.md` for the complete index of preserved notes, including
   historical dependencies and failed approaches.
4. Read `CHECKS.md` for what was actually replayed during this closeout.
   `MANIFEST.json` is only a file-integrity manifest.

## Principal evidence

| Claim or issue | Main evidence |
|---|---|
| Positive-characteristic defect in Ghosh Proposition 3.3 | `evidence/audit/COUNTEREXAMPLE_PROOF.md`, `DEPENDENCY_AUDIT.md` |
| At least seven centered monomials in degree 20 | `evidence/seven-terms/PROOF.md`, `case_coverage.json`, `structural_audit/AUDIT.md` |
| Nine characteristic-17 seeds over the algebraic closure | `evidence/full/support_frontier/prime17/CLASSIFICATION.md` and `check_classification.py` |
| Whole row-3 exclusion and further exact constraints | `evidence/full/LIFT_CONSEQUENCES_17.md` |
| Complete tame and quadratic lifting descriptions | `evidence/full/tame17/ROW4_QUADRATIC_LIFTING.md`, `ROW4_QUADRATIC_AUDIT.md`, `ROW6_ETALE_AUDIT.md`, `ROW7_ETALE_AUDIT.md`, `ROW9_ETALE_AUDIT.md` |
| Completed row-9 support exclusions | `evidence/full/collective17/exclusions/REPORT.md`, `COVERAGE.json`, and batch proofs |
| Complete row-4 support exclusion | `evidence/full/tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md` and `ROW4_SMALLEST_SUPPORT_AUDIT.md` |
| Row-8 valuation bound and full residue census | `evidence/full/wild17/ROW8_BOUND_AND_DIVIDED_IDENTITY.md`, `AUDIT.md` |
| Row-8 leading algebras and prime-19 formal cover | `evidence/full/wild17/blowup/COLLECTIVE_REDUCTION.md`, `COLLECTIVE_REDUCTION_AUDIT.md` |
| Quartic leading models and conditional exclusion | `evidence/full/wild17/blowup/m4/LIFT_CONSEQUENCES.md`, `INDEPENDENT_MODEL_AUDIT.md`, `NEXT_LIFT_AUDIT.md` |
| Finite free row-9 algebra; determinant still unevaluated in general | `evidence/full/collective17/elimination/FINITE_FLAT_REDUCTION.md` |
| Characteristic-2, characteristic-5 and cross-prime constraints | `evidence/full/two_adic/`, `five_adic/`, `cross_prime/` |
| Conditional prime-19 first jet | `evidence/full/global/P19_CLUSTER_FIRST_JET.md` |
| All-degree repair, cluster, analytic, height and matrix results | `evidence/full/global/REPAIR_EQUIVALENCE.md`, `cluster_tree/`, `global_analytic/`, `global_height/`, `global_matrix/` |

## Corrections and historical status

The original audit package's claim that its five-term lower bound might be
new is superseded by `evidence/AUDIT_NOVELTY_CORRECTION.md`: that lower bound
is already an implicit consequence of earlier work. The correction's own
statement that no six-term theorem was then claimed is also historical.
The later seven-term package gives the stronger bound and includes the
earlier support exclusions as unchanged dependencies.

The nested six-term package describes family C as unresolved. The seven-term
package's proof resolves that family. Its novelty assessment remains
qualified by an unavailable-source overlap. The current report makes no
priority claim for the seven-term theorem or the later local results.

The initial brief's assertion that Ghosh was the only author to claim a full
proof was corrected in the audit. A bounded literature search does not prove
that no public objection or correction exists. The reviewed version and the
precise search scope are recorded in the report and source-identity notes.

Counts of residue points or marked assignments are not counts of genuine
characteristic-zero counterexamples. The report distinguishes reduced points
from scheme length, and coefficient-support exclusions from whole-branch
exclusions. Every remaining branch is retained explicitly.

## Replay

From the extracted package directory, run:

```sh
python3 replay.py --output /path/to/new/replay-results
```

The default runner checks file integrity and runs the selected arithmetic
and coverage checks in a temporary evidence copy. It requires Python 3.10+
on Linux or macOS, and a C++17 compiler (`CXX`, `--cxx`, or the default `c++`
found on `PATH`). Process-group cleanup and file locking use POSIX interfaces. SymPy enables an additional independent
integral-syzygy check; its inclusion is recorded. The native executables
preserved in the evidence are historical artifacts; the relevant replay
rebuilds its executable from source.

If the final m=6 batch is complete and `M6_REPLAY.json` is present, include
its longer exhaustive native rerun with:

```sh
CXX=g++ python3 replay.py --include-m6 --timeout-scale 4 --output /path/to/new/full-replay-results
```

The scale multiplies the default checker, compiler and native limits by four:
for example, the m6 native guard becomes 960 seconds and its outer checker
guard becomes 1200 seconds. The unscaled defaults remain 240 and 300 seconds.
`--compile-timeout`, `--native-timeout` and `--check-timeout` accept explicit
positive finite limits in seconds. An explicit limit overrides its scaled
default. Without an explicit `--check-timeout`, the runner adds outer headroom
when a compiler/native override requires it; an explicit outer limit is the
user's complete-check budget and must leave time for compilation, enumeration
and certificate arithmetic. `--cxx 'ccache g++'` supports compiler wrappers;
the string is parsed as arguments, never passed to a shell. Quote compiler
paths containing spaces inside the option value.

The fresh m6 mode repeats the same native algorithm, not a second independent
exhaustive implementation. A timeout is incomplete evidence, not an arithmetic
contradiction or a successful census. Use a new output directory for each
replay to retain its logs. The standalone `batch-m6/run_native.py` additionally
requires `--output` and refuses to replace existing role receipts.

No open-ended solver is launched by these commands. Each child has an
external wall limit. The optional large integer-resultant proof in the
seven-term package and discovery Singular jobs are not needed by the compact
main proof and are not run by default. Independent native implementations
of the original row-8 census and their historical receipts are preserved;
the default runner checks its bound and leading-model arithmetic rather
than re-enumerating that entire census.

A successful replay supports the finite calculations it lists. The
normalization, valuation, coverage and finite-algebra arguments still require
mathematical review. No checker here formally verifies the full conjecture,
and independent AI-agent reviews are not external human refereeing.
