# Twenty-one further canonical systems are excluded

23 September 2026. This is the complete second batch of the row-9 cover:
all 21 canonical systems with five active middle indices. It uses the
exact equations, root-domain coverage, unit-Jacobian lifting, and
ramification-safe finite-precision argument proved in `../BATCH1_PROOF.md`.
No new lifting assumption is introduced.

Each system has 17^5 = 1,419,857 nonzero residue-root markings. All
29,816,997 markings were enumerated by the FLINT producer and independently
by the standalone native checker. Both implementations returned exactly
the same complete survivor lists. There are 113 surviving markings,
partitioned into 48 Frobenius orbits; three systems have no residue
survivors at all.

| Active middle indices | Residue survivors | Frobenius orbits | Required precision exponent |
|---|---:|---:|---:|
| 4,5,7,10,13 | 2 | 2 | 2 |
| 4,5,8,10,11 | 2 | 2 | 4 |
| 4,5,9,12,15 | 3 | 3 | 2 |
| 4,5,9,14,15 | 3 | 3 | 2 |
| 4,6,8,10,13 | 19 | 6 | 2 |
| 4,6,8,10,16 | 17 | 4 | 2 |
| 4,7,8,10,16 | 2 | 2 | 2 |
| 4,7,9,10,15 | 2 | 2 | 2 |
| 4,7,10,11,13 | 2 | 2 | 2 |
| 4,7,10,13,15 | 18 | 5 | 2 |
| 4,9,10,14,15 | 1 | 1 | 2 |
| 4,10,11,14,15 | 3 | 3 | 2 |
| 4,10,12,14,15 | 2 | 2 | 2 |
| 5,6,9,15,16 | 1 | 1 | 2 |
| 5,6,10,13,16 | 17 | 4 | 2 |
| 5,11,13,15,16 | 1 | 1 | 2 |
| 5,12,14,15,16 | 0 | 0 | 1 |
| 6,10,11,15,16 | 0 | 0 | 1 |
| 7,10,12,14,16 | 0 | 0 | 1 |
| 8,10,13,15,16 | 1 | 1 | 2 |
| 10,11,14,15,16 | 17 | 4 | 2 |

The exponent one denotes exclusion by the first residue alone. Every
one of the 112 surviving markings outside the final exceptional orbit
is excluded by a nonzero divided-H2 obstruction modulo 17^2.

## The fourth-digit orbit

For the remaining marking, the active set is {4,5,8,10,11} and all
selected residue roots are one. The exact integer recurrence at the
approximate root one gives

    (u4,u5,u8,u10,u11) = (3,-6,181,-7144,50665),
    T = 11,294,240,224 = 17^3 * 2,298,848.

The final quotient is 6 modulo 17, so T is 29,478 modulo 17^4 and
has valuation exactly three. At this integer approximation,
q(1)=17*T has valuation four. The square system has just one root
variable and its reduced Jacobian is q_bar'(1)=1. Thus the approximate
root satisfies the square equation modulo 17^4 and the unit-Jacobian
valuation argument identifies every exact solution with it to that
precision. Its T cannot vanish. In particular, zero obstructions at
precisions 17^2 and 17^3 were not treated as evidence of an exact lift.

The main precision certificate includes this fourth digit. The separate
`fourth-digit-integer-check.json` records the compact integer calculation.
The independent replay computes the same obstruction by direct Hasse
differentiation at one extra digit and exact coordinatewise division by
17; it does not assume the saved value of T.

## Verification and scope

`residue-batch.json` and `lift-batch.json` contain the complete marking
lists, orbit partition, root approximations, normalized coefficients,
Jacobian entries, and obstruction digits. `verification-normal.json`
and `verification-optimized.json` are identical PASS results. Each
replay rebuilds the native source, independently enumerates all markings,
and checks every precision certificate with separate standard-library
polynomial arithmetic. No mathematical assertion rests on solver SAT,
UNSAT, a timeout, or affine specialization from a finite field.

The producer completed in 86.74 seconds inside a 90-second external
wall guard. The first native enumeration completed in 2.65 seconds
inside its own 90-second guard. Each full independent replay, including
compilation, native enumeration, and precision checks, completed in
under 5.3 seconds. No native CAS or SMT solver was used.

Together with batch one, these calculations exclude 28 of the 240
canonical systems. The other 212 systems were not executed here. This
is actual progress within the full row-9 cover, not an exclusion of
the whole row, unrestricted degree 20, or the Casas-Alvero conjecture.
