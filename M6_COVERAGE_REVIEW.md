# Review of the m=6 canonical census coverage

**PASS for the reviewed coverage and implementation change.** This is a
bounded code and provenance audit of
`evidence/full/collective17/exclusions/batch-m6`. It is not an independent
exhaustive implementation of the census or a new proof of the conjecture.
No full census was rerun for this review. The accompanying
`M6_COVERAGE_REVIEW.json` records the checked counts and fingerprints.

## Source change and exact arithmetic

The new `replay_residues.cpp` was compared byte for byte with the previously
validated parent at `evidence/full/collective17/exclusions/replay_residues.cpp`.
Its only changes are the `m<=5` to `m<=6` guard, a `chrono` include and timing
variable, and case-level output flush/progress messages. There is no change to
the finite-field arithmetic, coefficient recursion, obstruction, or leaf test.
The parent source fingerprint matches the one recorded in `CONFIG.json`.

The extension of the guard is safe for the actual inputs. All 51 active lists
have six strictly increasing indices in `{4,...,16}`. The parameter, marking,
weight, and transition containers are dynamically sized in `m`; recursion has
one level per index. The fixed arrays of 17 powers are indexed only by `j`,
`j-3`, and `j-active[i]`, all between 0 and 16. Field-coordinate arrays remain
dimension 10, independently of `m`. Every loop selects each of the 17 witness
indices once, so recursion enumerates every ordered six-tuple exactly once.
The checked leaf count is `17^6=24,137,569` per support.

The arithmetic ranges are well within the declared integer types. A matrix
dot product is at most `10*16^2=2,560`, within `int`. Before reduction a field
product coefficient is at most 2,560 in absolute value; the nine descending
reductions add at most `9*16*8=1,152` for the supplied modulus coefficients.
These accumulators are `int64_t`. All binomial computations have `n<=20`,
with largest pre-division intermediate 1,847,560; the largest unreduced
obstruction weight is 444,600. Scalar multiplication uses `int64_t`.
The field order `17^10=2,015,993,900,449` and all enumeration counters fit
`uint64_t`. No numerical approximation or floating-point arithmetic affects
the census; floating point is used only for elapsed-time reporting.

These bounds concern the validated input files. The native program is not a
general malformed-input validator: it does not itself assert every active
index ordering or field-coordinate bound. This review checked those
conditions directly in the actual inputs, which are hash-bound to the run
receipts and checked by the surrounding certificate pipeline. No change to
the frozen census was needed.

## Canonical support completeness

The supports were independently reconstructed from
`evidence/full/support_frontier/inventory.json`: take its `finalSurvivors`
containing `{3,18,19}`, omitting `{2,17}`, and of total size nine. The inventory
fingerprint agrees with the dependency in `elimination/presentation.json`.
This yields exactly the same 51 distinct ordered supports as the
presentation, `CONFIG.json`, native input, and residue certificate. Each has
exactly six active middle indices. Both native input files were parsed into
integers and compared in full with their expected dimensions, field
polynomial, 17 root vectors, and support lists; there are no trailing inputs.

The field-domain validation is unchanged from the parent. Its degree-ten
Rabin tests establish a field; its root checks exhibit 17 distinct nonzero
simple roots of the monic degree-17 quotient of
`X^20-X^17-3X^2+3X` by `X(X-1)^2`. Thus the witness domain is complete over
the algebraic closure. A repeated witness index is permitted, and zero
residues of active coefficients are not filtered out.

## Timeout recovery and completed replay

The first producer reached its 180-second wall guard after 46 complete case
records. Recovery was checked against the raw output, not inferred from a
progress count. Each accepted `CASE` header specifies the correct local
index, six active indices, `17^6` leaves, and a survivor count. Every declared
survivor line is present, has six indices in `{0,...,16}`, and is unique and
in lexicographic order. The recovered output ends after a complete survivor
block with a newline; no partial header or survivor block was accepted.
It contains 652 survivors.

The continuation input contains exactly canonical supports 46 through 50.
It completed with exit code zero, five complete case records, 34 survivors,
and `ALL_PASS`. Its local indices 0 through 4 map to global indices 46 through
50. The combined record has 51 cases, 686 survivors, and
`51*17^6=1,231,016,019` markings. The concatenated case/support/survivor data
agree exactly with `residue-batch.json`. The two segments have neither a gap
nor an overlap. Source, input, output, segment-receipt, presentation, and
combined-output hashes were checked.

During this review, the already-running full replay completed with exit code
zero. Its entire output is byte-identical to `combined-producer.log`; its
source, input and output fingerprints also match. This is a second execution
of the **same** native algorithm. It adds a successful unsplit execution and
checks recovery consistency, but is not independent exhaustive enumeration.

## Checker scope and conclusion

The Python `check_batch.py` binds the cases to the canonical presentation and
inputs, checks the segment continuity and raw records, requires the complete
same-algorithm replay, and compares the two full outputs. Its separate
arbitrary-precision polynomial arithmetic checks surviving coefficient
recursions, witness equations, Frobenius orbit coverage, and precision
certificates. In particular it recomputes the divided `H2` value from direct
Hasse differentiation at one extra digit. A nonzero final obstruction is
required for an exclusion; a zero value through the precision limit is
explicitly retained as unresolved. Its checks use explicit exceptions, not
Python assertions disabled by `-O`.

The code-level audit found no blocking issue in extending the validated
census from five to six active indices, or in the 46+5 recovery. The
arithmetically independent survivor checks and the same-algorithm complete
replay should remain described separately. This coverage review alone does
not establish the local lifting theorem or independently recertify every
higher-precision value; those remain the roles of the existing mathematical
proof and certificate checker.
