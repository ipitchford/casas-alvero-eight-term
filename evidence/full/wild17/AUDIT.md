# Independent audit of the row-8 valuation and residue reduction

23 September 2026. **PASS for the necessary conditions and finite residue census stated below.** No row-8 exclusion or finite classification of characteristic-zero lifts follows.

Reviewed `ROW8_BOUND_AND_DIVIDED_IDENTITY.md` and `enumerate_row8.cpp`. The inherited setup is the proved row-8 seed classification, integrality of all roots and binomial-normalized coefficients after valuation normalization, and the separate characteristic-zero simple-mean theorem. Those dependencies are not new assertions of this note.

## Valuation proof, including ramification

The ordinary Hasse orders 18, 3, 2, 1 reduce respectively to `3X^2, X^17, 3X^18, 3X^19`; hence witnesses for normalized degrees 2, 17, 18, 19 lie in the zero cluster. Order 17 has reduction `X^3-1`, so the degree-3 witness is a unit and can be scaled exactly to 1. This preserves the seed and integrality. The identity `a3=-1-3a2` follows.

Every nonzero zero-cluster root has positive valuation, and there are finitely many roots. The exact simple root zero cannot exhaust its multiplicity-17 residue cluster, so the minimum delta is well defined. A zero witness itself has infinite valuation, which also satisfies every lower bound used.

The displayed bounds (2)–(5) follow from the actual common-root equations. In particular, the exceptional unit binomial coefficient for index 2 in `G19` is covered by `nu(a2)>=2 delta`; it is not silently treated as divisible by 17. The index-17 and index-18 terms are controlled by the preceding two inequalities.

At a root attaining delta, the `X^17` summand has value exactly `17 delta`. All other nonzero summands have value at least `min(20 delta,1+4 delta)`. When `delta<1/13`, this is strictly larger. The contradiction proves `delta>=1/13`. Consequently `16 delta>1`, giving the stronger bounds `nu(a17)>=1+delta`, `nu(a18)>=1+2 delta`, `nu(a19)>=1+3 delta`.

No step assumes that a positive valuation is an integer, that the coefficient field is unramified, or that a root differs from its residue representative by a multiple of 17. The inequalities work with arbitrary fractional valuations (and more generally the stated real-valued valuation setup).

The exact constants in (8) check: `1-1140=-17*67` and `190-3*1140=-17*190`. Each term is legitimately divisible by 17 in the valuation ring. The last three terms divided by 17 have strictly positive valuation, as does `a2`. Thus the divided residue identity (9) is valid.

## Completeness of the residue domain and recurrence

The only witness residues are `0,1,zeta,zeta^2`. The polynomial `zeta^2+zeta+1` is irreducible over F17: there is no nontrivial cube root in its multiplicative group of order 16. All four choices are retained for each of the 13 middle degrees.

Starting from `a0=1,a1=a2=0,a3=-1` in residue, `G_j(rho_j)=0` determines `a_j` with coefficient 1. At a nonzero residue, `rho_j^3=1` yields exactly formula (10); at zero it gives `a_j=0`. This proves all coefficient residues lie in the displayed copy of F289, even if the original algebraically closed residue field is larger. It does not prove the characteristic-zero coefficients or witnesses are unramified.

The C++ recursion visits all `4^13=67,108,864` marked assignments exactly once. Higher stale coefficient-array entries are never read before being replaced. The accumulated sum implements (9), using encoded `16` for the scalar -1. No unproved rational-prime-field restriction is imposed.

## Collision filters

Each nonzero residue root of `X^17(X^3-1)` has multiplicity one. Therefore any two exact roots reducing to the same nonzero residue coincide, irrespective of ramification. The code correctly filters equality only for nonzero witness classes; multiple witnesses reducing to zero are not identified.

The pair of normalized degrees `{4,16}` corresponds to Hasse orders `{16,4}`. Their exact equality is forbidden by [Castryck–Laterveer–Ounaies, Proposition 15](https://arxiv.org/html/1208.5404#S3): take `p=2,k=2,n=5=2^2+1`. The triple `{5,10,15}` maps to the same set of Hasse orders and is forbidden with `p=5,k=1,n=4`.

These specializations also have direct proofs: translate the alleged shared root to zero and valuation-normalize at the indicated prime. Normalized CA integrality still applies. The assumed derivative vanishings set every Lucas-visible nonleading coefficient to zero (indices 4,16 at 2; indices 5,10,15 at 5), making the reduction `X^20`, contrary to the retained unit root. Thus both collision filters are necessary for every characteristic-zero lift. They are not asserted to be all available restrictions.

## Arithmetic and replay evidence

Independently checked the encoded field rotations by polynomial multiplication modulo `zeta^2+zeta+1`. All intermediate integer magnitudes and array indices are within the C++ types and bounds. The compiler's conversion warnings concern provably bounded integers, not an arithmetic error.

Compiled `enumerate_row8.cpp` independently with clang++ C++17, optimization and warnings enabled; the native replay completed successfully and its entire JSON equals the producer receipt. Stored it in `audit-native-replay.json`. Counts are:

- 67,108,864 marked assignments initially;
- 233,310 after the divided identity;
- 180,341 after the two unit-root collision filters.

The separate `check_audit_arithmetic.py` checks the field rotations, binomial divisibility ranges, exact divided constants, full versus simplified normalized derivative recurrence on 1,024 deterministic samples, and all 39 single-unit assignments. It passes under ordinary Python and `python3 -O`, using explicit failures rather than assertions. The single-unit survivor is exactly degree `j=11`, residue witness 1, coefficient residue 11. No 67-million-case Python replay was run.

The replay counts marked witness choices, not distinct coefficient patterns, exact polynomials, or characteristic-zero solutions. The optional stronger single-unit radius claim is outside this audit. The general row-8 lifting problem remains unresolved.
