# Row 9: complete collective target, final obstruction unevaluated

The thirteen middle common-root conditions can be represented by exact
companion norms of size 18, with one additional linear equation T = 0.
Their completed integral algebra is finite free of rank
**20,822,964,865,671,168** over the 17-adic integers. The row is excluded
exactly when the generic multiplication norm of T is nonzero.
That norm has **not** been computed. No branch exclusion is claimed.

Using the 240 previously verified canonical support masks removes the
simple mean-root choice at active indices. This gives size-17 companion
norms and finite-free ranks whose sum is **813,975,725,115,600**. These
systems preserve coefficients with zero residue and all extension-field
witnesses. Their ranks still prevent any claim of a practical explicit
matrix computation.

The full residue root domain also consists of the point at infinity and
the seventeen roots of y^17 = y^2 - 5, under r = (y+7)/(y-7).
This quadratic Frobenius law has not yet supplied a further obstruction.

`FINITE_FLAT_REDUCTION.md` proves the exact incidence equivalence,
finite-flatness, generic-norm criterion, and complete support coverage.
`presentation.json` contains only affine integer coefficient arrays and
the small companion-matrix prescription; it expands no resultant and
constructs no large norm matrix. `check_presentation.py` independently
replays 182 normalized Hasse coefficient checks, all division/obstruction
identities, squarefreeness, Frobenius conjugacy, and support/rank arithmetic.
Normal and optimized Python replay outputs are identical and pass.
Each replay took under 0.07 seconds within a 20-second external guard.

No additional SMT variants, native CAS jobs, root-assignment enumeration,
or final norm evaluations were run in this subtask. There are no live
processes. The finite-flat argument is an ordinary mathematical proof,
not a formally verified theorem; the checker verifies its exact input
identities and arithmetic. Unrestricted degree 20 and the full
Casas-Alvero conjecture remain unresolved by this result.
