# Replay and assurance scope

The proof is `COLLECTIVE_REDUCTION.md`. The independent audit
`COLLECTIVE_REDUCTION_AUDIT.md` covers its prime-19 completed-local
finiteness argument, including nilpotents, normalization, and arbitrary
finite ramification. It does not independently audit the J/L tropical
inequalities or recompute the new stratification.

From the workspace root:

```sh
python3 work/casas-alvero-full/wild17/blowup/check_collective.py
python3 -O work/casas-alvero-full/wild17/blowup/check_collective.py
```

Both saved outputs are identical and report PASS:

- `collective-replay.json`
- `collective-replay-optimized.json`

Their SHA-256 is
`bc39865216a0f9b109bcdc404d6d00d88d24d724f11bd078bd748d7d41ee59d2`.

The checker uses only the Python standard library. It checks exact affine
valuation bounds at all their breakpoints, sparse polynomial identities
for the leading models, their pairwise-coprime leading monomials,
stratification sums, and all 131,072 prime-19 marked residue points.
It does not compute the completed local rings or check whether their
generic fibres are empty.

The already executed complete J/L stratification used `stratify_row8.cpp`
compiled with `c++ -O3 -std=c++17`, with an external 60-second process
timeout. It finished in approximately 1.2 seconds. Its diagnostic output
is `residue-strata.json`; its main output repeats the previously audited
residue census. The only additions to that producer are the two maxima
J and L and their histogram. Its total 180,341 agrees with both earlier
independent census implementations in the parent directory.

Result scope: 179,765 marked assignments have a proved exact first scale
and a finite normalized leading-model algebra. The 576 remaining
assignments have a proved scale interval and remain in the full formal
cover. No whole branch, degree-20, or full Casas–Alvero exclusion follows
from these artifacts.
