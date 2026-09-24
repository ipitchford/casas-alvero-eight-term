# Completed row-9 batches: 79 systems excluded, 161 remain

The three completed batches cover all canonical systems with three through
six active middle indices. They account for **1,261,339,055** residue-root
markings, including all extension-field choices and coefficients with
zero residue.

| Active middle size | Systems | Markings | Residue survivors | Frobenius orbits | Result |
|---|---:|---:|---:|---:|---|
| 3 or 4 | 7 | 506,039 | 20 | 7 | All excluded |
| 5 | 21 | 29,816,997 | 113 | 48 | All excluded |
| 6 | 51 | 1,231,016,019 | 686 | 252 | All excluded |

Nine systems have no first-residue solutions. All 819 surviving markings
are excluded by higher-digit certificates: 811 fail modulo 17^2, six
modulo 17^3, and two modulo 17^4. No remaining lift in these completed
batches survives the checked obstruction. Normal and optimized certificate
replays pass and agree.

The verification boundary differs for the last batch. Sizes three through
five were exhaustively enumerated with FLINT and separately with native
integer arithmetic. Size six used the validated native implementation as
producer. Its initial 180-second run timed out after 46 completed cases;
one authorized 60-second continuation completed only the remaining five
in 16.03 seconds. One full native replay then completed in 165.23 seconds
under a 240-second guard and agreed exactly with the combined producer.
That is a repeat of the same exhaustive algorithm, **not an independent
exhaustive FLINT check**. Separate standard-library arithmetic verifies
all stated survivors, their Frobenius coverage, and their precision
certificates; it does not independently establish absence of omitted
survivors from that native enumeration.

The coverage and arbitrary-ramification argument is in `BATCH1_PROOF.md`.
The second-batch addendum is `batch-m5/BATCH2_PROOF.md`; the final batch's
full table, split-run provenance, and verification limits are in
`batch-m6/REVIEW_ADDENDUM.md`. `COVERAGE.json` lists all 79 exclusions and
the 161 systems still unexecuted. No size-seven batch or other branch was
attempted in the final feasibility extension. There are no live jobs.

This is progress through the complete row-9 cover, not an exclusion of
the whole row, unrestricted degree 20, or the Casas-Alvero conjecture.
Novelty and external mathematical review are separate questions. The
proofs and arithmetic replay are not formal verification.

From `/Users/admin/Documents/Codex/2026-09-21/fi`, replay the earlier
batches with:

```sh
python3 work/casas-alvero-full/collective17/exclusions/check_batch.py
python3 work/casas-alvero-full/collective17/exclusions/check_batch.py --directory work/casas-alvero-full/collective17/exclusions/batch-m5
```

The final batch's read-only certificate and preserved-receipt replay is:

```sh
python3 work/casas-alvero-full/collective17/exclusions/batch-m6/check_batch.py
```

For an optional fresh full native enumeration under its 240-second guard,
append `--rerun-native`. That run uses temporary files and preserves the
saved receipts. Regenerating the earlier producer enumerations requires
python-flint; the certificate checkers use Python's standard library and
the available C++ compiler.
