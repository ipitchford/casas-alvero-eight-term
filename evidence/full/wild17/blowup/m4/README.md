# Bounded quartic-model round

Main derivation: `LIFT_CONSEQUENCES.md`.

Independent reviews:

- `INDEPENDENT_MODEL_AUDIT.md`: complete algebraic-closure classification
  of B4, local lengths, unique repeated-root geometry, and the conditional
  characteristic-zero cluster/valuation bridge.
- `NEXT_LIFT_AUDIT.md`: the coefficient-linked first correction and the
  uniform next-lift exclusion, with arbitrary finite ramification.

Exact replay, from this directory:

```sh
python3 check_independent_model.py
python3 -O check_independent_model.py
python3 check_lift_consequences.py
python3 -O check_lift_consequences.py
```

The normal and optimized outputs agree. SHA-256 values are recorded in
`receipt-hashes.json`. Both scripts use only the Python standard library;
the first uses explicit finite-extension polynomial arithmetic. No
long-running process remains.

The complete B4 algebra has length 289 and exactly 209 reduced marked
points. Every hypothetical original polynomial in J=L=16 would have one
multiple root globally, of multiplicity 2,3,or4, and its original mean
would have a simple leading root. This gives exact alternatives for
a2,a17,a18 and the exact value nu(a19)=16/13.

A new lifting obstruction excludes, uniformly across the stratum, the
configuration a17=a18=0 with every zero-residue middle witness at the
exact mean. It is not just a failed lift of one numerical example.
Other configurations survive the proved necessary conditions. The full
J=L=16 stratum, row 8, degree 20, and the full conjecture remain unresolved.
