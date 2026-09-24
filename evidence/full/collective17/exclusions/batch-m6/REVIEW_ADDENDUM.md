# Review addendum: the complete six-active-index batch

23 September 2026. This addendum concerns exactly the 51 canonical row-9
systems with six active middle indices. No larger batch or other branch
was attempted. All 51 systems pass the completed execution and certificate gates.
`verification-normal.json` and `verification-optimized.json` are identical
PASS results; the original timeout and subsequent completion receipts
remain preserved.

## Mathematical scope

The equations and the completeness argument are those of
`../BATCH1_PROOF.md`: for each support, inactive normalized coefficients
are exactly zero; every active derivative is marked by one of the
seventeen nonzero roots of the fixed squarefree residue polynomial
q=f/[X(X-1)^2]. Those roots include all degree-five and degree-ten choices.
Active coefficients may have zero residue, and witnesses may repeat.
The monic normalized derivative equations determine the coefficients
successively for every marking.

There are 17^6 = 24,137,569 markings per system, hence 1,231,016,019 in
this batch. The complete native output retains 686 residue survivors in
252 Frobenius orbits. Every recorded survivor orbit has a nonzero exact
obstruction after lifting: 680 markings are excluded modulo 17^2, five
modulo 17^3, and one modulo 17^4. The authorized precision cap was six;
no orbit required its fifth or sixth digit.

The Hensel square system again uses one variable per distinct selected
residue root and q_u(r)=0. Its reduced Jacobian is diagonal with entries
q_bar'(r), all nonzero. Since coefficient-parameter derivatives of q are
17-divisible, the coefficient recurrence does not change that diagonal
Jacobian. The finite-precision Taylor argument in the first-batch proof
covers arbitrary ramification: an exact solution with the same reduction
agrees with a precision-n approximate solution modulo valuation n. Thus a
saved value of T with valuation below n cannot vanish in an exact lift.
Frobenius conjugation carries the same conclusion to every member of a
recorded orbit. This is the same proof mechanism, with no stronger
unramified assumption or specialization shortcut added.

## Bounded split execution

The initial native producer had a 180-second external guard. It stopped
at that guard after 46 complete cases had been saved and flushed. Their
652 survivors were checked by separate standard-library field arithmetic.
The original timeout receipt and raw output were preserved.

Based on measured runtime, one continuation was authorized for the five
remaining supports only, with a 60-second guard. It completed in 16.03
seconds. `prefix-recovery.json` identifies the exact split;
`continuation-input.txt` contains no support from the recovered prefix.
`combined-process.json` binds both original receipts and records complete,
nonoverlapping coverage of all 51 systems. The combined output is an
assembly of complete case records, not a claim that the initial run
finished successfully.

One full native replay was then run with a 240-second guard. Its
`replay-process.json` records COMPLETE in 165.23 seconds. The normal and
optimized point/certificate checks completed in 14.84 and 14.62 seconds. The checker
requires that run to be complete and its output to agree byte-for-byte
with the normalized combined producer output before issuing a PASS.

## Verification boundary

Unlike the earlier two batches, this batch has **no exhaustive independent
FLINT enumeration**. Its native source is the previously checked native
enumerator with the active-size bound increased to six and per-case
progress output added. The complete Cartesian-product loop and exact
counter establish its claimed coverage at source level. A second run of
that same source is an execution-consistency check, not an independent
algorithm for ruling out omitted survivors.

`check_batch.py` separately verifies the field's irreducibility, the
complete simple root domain, every recovered survivor, the Frobenius
partition, and every saved precision certificate using standard-library
polynomial arithmetic. It reconstructs f and q and computes H2 f(1)/17
by direct Hasse differentiation at one extra digit, independently of the
producer's saved coefficient template. That arithmetic checks the stated
survivors and lifts; it does not independently prove that an omitted
survivor is absent from the native enumeration.

The checker also validates both split input scopes and run fingerprints,
then compares the combined producer with the complete replay. The normal
and optimized checker outputs must agree. The preserved native receipts
and all hashes remain available for review. This is computer-assisted
mathematics with explicit implementation dependencies, not a formal proof
or an external mathematical review.

## Full system table

Each line accounts for all 24,137,569 markings of that support. Precision
exponent one means that no first-residue survivor exists.

| Active middle indices | Residue survivors | Frobenius orbits | Required precision exponent |
|---|---:|---:|---:|
| 4,5,6,7,10,16 | 2 | 2 | 2 |
| 4,5,6,7,12,15 | 21 | 8 | 2 |
| 4,5,7,8,12,15 | 5 | 5 | 3 |
| 4,5,7,8,15,16 | 0 | 0 | 1 |
| 4,5,7,10,12,13 | 1 | 1 | 2 |
| 4,5,7,11,12,15 | 54 | 15 | 2 |
| 4,5,7,11,14,15 | 23 | 10 | 2 |
| 4,5,7,12,15,16 | 1 | 1 | 2 |
| 4,5,8,9,14,15 | 3 | 3 | 3 |
| 4,5,8,10,11,12 | 20 | 7 | 2 |
| 4,5,8,10,11,13 | 39 | 13 | 2 |
| 4,5,8,10,11,14 | 4 | 4 | 2 |
| 4,5,10,11,12,13 | 4 | 4 | 2 |
| 4,5,10,11,13,14 | 3 | 3 | 2 |
| 4,5,10,11,14,15 | 5 | 5 | 2 |
| 4,5,11,13,15,16 | 3 | 3 | 2 |
| 4,6,7,9,10,12 | 4 | 4 | 2 |
| 4,6,7,9,10,14 | 2 | 2 | 2 |
| 4,6,7,10,13,14 | 19 | 6 | 2 |
| 4,6,8,9,10,13 | 2 | 2 | 2 |
| 4,6,8,9,10,16 | 3 | 3 | 2 |
| 4,6,9,10,12,13 | 2 | 2 | 2 |
| 4,6,9,10,12,14 | 2 | 2 | 2 |
| 4,7,8,10,15,16 | 3 | 3 | 2 |
| 4,7,9,10,11,13 | 5 | 5 | 2 |
| 4,7,9,10,13,15 | 18 | 5 | 3 |
| 4,7,10,11,13,15 | 1 | 1 | 2 |
| 4,9,10,11,12,13 | 6 | 6 | 2 |
| 4,9,10,11,12,14 | 308 | 43 | 2 |
| 4,9,10,11,12,16 | 3 | 3 | 2 |
| 4,10,11,12,14,15 | 5 | 5 | 2 |
| 4,10,11,13,14,16 | 2 | 2 | 2 |
| 5,6,7,9,15,16 | 2 | 2 | 2 |
| 5,6,9,14,15,16 | 4 | 4 | 2 |
| 5,7,8,13,15,16 | 3 | 3 | 2 |
| 5,7,9,13,15,16 | 23 | 10 | 2 |
| 5,7,10,13,15,16 | 1 | 1 | 2 |
| 5,8,9,10,13,16 | 7 | 7 | 2 |
| 5,9,11,13,15,16 | 7 | 7 | 2 |
| 5,10,11,13,15,16 | 0 | 0 | 1 |
| 5,11,13,14,15,16 | 3 | 3 | 2 |
| 6,7,10,12,14,16 | 0 | 0 | 1 |
| 6,8,10,13,15,16 | 3 | 3 | 3 |
| 6,10,11,14,15,16 | 23 | 10 | 2 |
| 7,8,9,10,12,16 | 2 | 2 | 2 |
| 7,10,12,13,15,16 | 1 | 1 | 4 |
| 8,9,10,11,14,16 | 4 | 4 | 3 |
| 8,9,10,12,14,16 | 1 | 1 | 2 |
| 8,10,11,13,15,16 | 5 | 5 | 2 |
| 8,10,12,13,14,16 | 21 | 8 | 2 |
| 8,10,13,14,15,16 | 3 | 3 | 2 |

## Replay without changing the saved package

From `/Users/admin/Documents/Codex/2026-09-21/fi`, the command

```sh
python3 work/casas-alvero-full/collective17/exclusions/batch-m6/check_batch.py
```

checks the preserved complete native receipts and independently replays
all survivor/precision arithmetic. It does not rerun the billion-marking
enumeration. To repeat that enumeration under its 240-second native guard
as well, use

```sh
python3 work/casas-alvero-full/collective17/exclusions/batch-m6/check_batch.py --rerun-native
```

The optional run compiles and executes in a temporary directory and
compares its output, preserving the saved completion receipts. Neither
command turns the repeated native algorithm into an independent
exhaustive implementation. The original standalone runner writes new
receipts and is therefore not the suggested command for reviewing a
frozen package.
