# Completed row-9 batches: 28 systems excluded, 212 remain

Two complete batches have now excluded all canonical systems with three,
four, or five active middle indices. They account for **30,323,036**
residue-root markings, including all extension-field roots and allowing
active coefficients to have zero residue.

| Batch | Systems | Markings | Residue survivors | Lifted Frobenius orbits | Result |
|---|---:|---:|---:|---:|---|
| Middle size 3 or 4 | 7 | 506,039 | 20 | 7 | All excluded |
| Middle size 5 | 21 | 29,816,997 | 113 | 48 | All excluded |

Six systems have no first-residue solutions. The remaining systems are
excluded by explicit higher-digit certificates: 131 residual markings
fail modulo 17^2, one modulo 17^3, and one modulo 17^4. The independent
normal and optimized replays pass and agree in both batches.

The proof of coverage and ramification-safe lifting is in
`BATCH1_PROOF.md`; the second batch and fourth-digit integer calculation
are in `batch-m5/BATCH2_PROOF.md`. `COVERAGE.json` lists all 28 excluded
systems and the 212 systems still unexecuted. This is progress through
the full cover, not a completed row-9 exclusion or a solution of degree 20.

The two enumeration implementations use FLINT and standalone C++ integer
arithmetic respectively. The precision checker uses separate
standard-library polynomial arithmetic and recomputes H2/17 directly.
All workers had external wall guards. There are no live processes and
no further batch was started.

To replay the existing certificates from this workspace:

```sh
python3 work/casas-alvero-full/collective17/exclusions/check_batch.py
python3 work/casas-alvero-full/collective17/exclusions/check_batch.py --directory work/casas-alvero-full/collective17/exclusions/batch-m5
```

The checker requires the available C++ compiler and Python's standard
library; it rebuilds the native replay automatically. Regenerating the
producer enumeration additionally requires python-flint. Internal replay
and the written proof are not formal verification or independent external
mathematical review.
