# Unrestricted degree 20 and full Casas-Alvero: research status

23 September 2026. **Both requested conclusions remain unproved.**
The active target is exactly `target.yaml`: unrestricted degree 20 and
the conjecture in every degree, in characteristic zero. No support bound,
residue classification or audit is being substituted for either target.

## Established so far

- A complete classification of the unrestricted degree-20 visible model
  in characteristic 17 into nine nonmonomial normalized residue seeds,
  over the whole algebraic closure. One seed, row 3, is excluded from
  lifting to a characteristic-zero counterexample using the known
  simple-mean theorem. Eight residue branches remain.
- Exact additional conditions on four of those eight branches, including
  an exact triple root in row 9. See `LIFT_CONSEQUENCES_17.md`.
- Complete unramified lifting reductions for rows 6, 7 and 9, with
  independent proofs in `tame17/ROW6_ETALE_AUDIT.md`,
  `tame17/ROW7_ETALE_AUDIT.md` and `tame17/ROW9_ETALE_AUDIT.md`.
  Each marked residue assignment determines a unique lift of a square
  subsystem. One additional exact scalar equation remains in each case.
  The uniqueness argument covers arbitrary ramified ambient extensions;
  it is not an assumption that an original counterexample is unramified.
- A complete quadratic lifting reduction for row 4. Every actual CA point
  in that normalization, including all its polynomial roots, lies in an
  extension of degree at most two over the unramified degree-four extension
  of Q17. Its local degree is at most eight and its ramification index at
  most two. Signed witness charts cover both roots of the second double
  cluster. One additional scalar equation remains to be excluded across
  the complete chart cover. See
  `tame17/ROW4_QUADRATIC_LIFTING.md` and its independent audit.
- The complete row-4 support {2,4,10,12,18,19} is excluded. Its divided
  critical-value equation leaves only two conjugate orientations among
  9,826 complete residue markings. Their unique lift has critical value
  17^2(9+4 alpha) modulo 17^3, where alpha^2+3 alpha+3=0, hence is nonzero.
  A separate standard-library replay reconstructs the full extension-field
  root domain and both orientations. The argument covers arbitrary ramified
  ambient candidates. See `tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md`.
- All 79 canonical row-9 support systems with at most six active middle
  coefficients are excluded. The complete searches check 1,261,339,055
  marked residue assignments, including all required extension-field
  roots and coefficient degenerations. Their 819 residue survivors form
  307 Frobenius orbits, all excluded by exact lifting through at most
  precision 17^4. The first 28 systems have independent exhaustive FLINT
  and native censuses. The final 51 have a complete repeat of the same
  native algorithm, an independent coverage audit, and independent
  survivor/lift arithmetic; they have no exhaustive FLINT replay.
  The earlier five-assignment result is included in this
  larger complete calculation. There remain 161 of the 240 systems;
  the whole row-9 branch is not excluded. See `collective17/exclusions/`.
- The subcase where every active row-9 middle witness has residue in F17
  reduces to at most three exact recycled roots. It is already covered
  by Massri's Theorem 7.10 (arXiv:1806.09561v6), after an affine change
  of coordinate. This is a cited prior-art corollary, not a new computed
  exclusion; the external theorem's computational proof was not replayed.
  See `collective17/prime-field/PRIOR_ART.md`. Support counts are unchanged.
- A cross-prime exclusion: row 9 cannot have the characteristic-2 type B
  configuration with its distinguished triple root becoming a nonunit.
  Further conditional exact valuations are proved for rows 4, 6 and 7.
  See `cross_prime/CROSS_PRIME_RESTRICTIONS.md` and its separate audit.
- A full-support bound for row 8: every nonzero root in its zero residue
  cluster has valuation at least 1/13, with v(17)=1. Coupled coefficient
  bounds justify a new divided residue identity even with arbitrary
  ramification. The identity leaves 233,310 of the 67,108,864 marked
  residue assignments; exact common-root collision obstructions leave
  180,341. These are necessary-condition counts, not lifts. No whole
  branch is excluded by this result. See
  `wild17/ROW8_BOUND_AND_DIVIDED_IDENTITY.md`.
- A collective first-scale reduction for row 8: 179,765 of the 180,341
  marked assignments have an exact scale and a finite algebra of normalized
  leading models. The other 576 assignments remain with proved scale bounds;
  none is silently discarded. This does not exclude any entire residue branch.
  See `wild17/blowup/COLLECTIVE_REDUCTION.md`.
- In the row-8 stratum J=L=16, the quartic leading algebra has 209
  distinct reduced models and total length 289. Its repeated cluster
  collapses exactly, so a hypothetical candidate has just one multiple
  root, of multiplicity two, three or four. All other nonzero roots in
  its original zero cluster have valuation 1/13. A further uniform
  obstruction excludes a17=a18=0 when every zero-residue middle witness
  equals the exact mean. This does not exclude the whole stratum or the
  J=16,L<16 cases. Proof and separate audits are in `wild17/blowup/m4/`.
- A prime-19 finite formal cover for every normalized degree-20 CA candidate.
  Its special fibre has exactly 2^17 marked geometric points. The completed
  local rings are finite over Z19, including nilpotents and ramified points.
  Their lengths and generic fibres have not been computed, so this is not an
  explicit candidate list or an emptiness result. The standard finiteness
  argument received independent review in
  `wild17/blowup/COLLECTIVE_REDUCTION_AUDIT.md`.
- A collective row-9 resultant presentation with a finite free completed
  algebra of rank 18^13. Branch exclusion is equivalent to nonvanishing of
  the generic multiplication determinant of the extra scalar T. Canonical
  support systems give smaller finite free algebras of total rank
  813,975,725,115,600. The determinant remains unevaluated. Compact companion
  norm circuits are in `collective17/elimination/presentation.json`; the
  proof is `collective17/elimination/FINITE_FLAT_REDUCTION.md`.
- Complete two-shape reductions at primes 2 and 5. The modulo-2
  normalized-coefficient census has 2,001 patterns before lifting cuts.
  A coefficientwise integral syzygy, divided by 2, cuts this to 1,068
  patterns. The identity is valid with arbitrary ramification.
- A conditional 19-adic first-jet constraint beyond the constant support
  determinant. It yields some exact witness collisions, but leaves both
  surviving first-jet assignments and an untreated degenerate-slope case.
- The proposed contraction repair of the claimed all-degree proof is
  equivalent to the missing lower-degree CA step under the surrounding
  hypotheses. General commutative-algebra assumptions do not repair it;
  explicit characteristic-zero countermodels and an authentic CA-family
  nilpotent example demonstrate this limitation.
- An explicit family of positive-characteristic CA polynomials shows
  why cluster occupancy and derivative-root counts alone cannot force
  a useful collapse: arbitrary-depth cluster trees can have maximal
  witness occupancy while every nontrivial cluster has a bad local degree.
  `cluster_tree/COUNTERMODEL_AND_COUNTS.md` proves this obstruction to
  that proposed all-degree route. It is not a characteristic-zero
  counterexample or a proof that stronger approaches cannot work.
- The characteristic-zero family X(X-1)^(n-2)(X+n-2) satisfies every CA
  condition except one and disproves the proposed relaxed contraction
  for Goncharoff reconstruction. Exact incidence gives a valid Newton
  moment bound, but no iterable descent or contradictory upper bound.
  See `global_analytic/INTEGRAL_OBSTRUCTION.md`. This rules out the
  relaxed argument, not every possible analytic approach.
- An all-place argument gives a positive lower bound for the projective
  height of a hypothetical CA root vector. It does not give a product-formula
  contradiction: local maximum root magnitudes do not form the absolute
  values of one fixed algebraic number. An exact degree-six polynomial
  satisfying all but one CA incidence retains every finite-place integrality
  condition and demonstrates the gap. See `global_height/ALL_PLACE_BOUND.md`.
- The normal-matrix derivative representation extends to a complete nested
  orthogonal compression flag, but shared eigenvalues do not force inherited
  eigenvectors. An exact all-degree family satisfies every spectral incidence
  except the first-derivative one and disproves that shortcut. A universal
  root-independent quadratic compression is impossible in degree at least
  five. No all-incidence matrix obstruction has been proved. See
  `global_matrix/COMPRESSION_AUDIT.md`.

## Evidence and locations

| Result | Proof / audit | Replay |
|---|---|---|
| Nine characteristic-17 seeds | `support_frontier/prime17/CLASSIFICATION.md`; `literature/PRIME17_CLASSIFICATION_AUDIT.md` | `support_frontier/prime17/check_classification.py` |
| Whole row-3 lift exclusion | `LIFT_CONSEQUENCES_17.md`; `literature/PRIME17_ROW3_LIFT_AUDIT.md` | Seed gcds in the preceding replay and `literature/check_prime17_seed_gcds.py` |
| Unramified reductions for rows 6, 7, 9 | `tame17/ROW6_ETALE_AUDIT.md`, `ROW7_ETALE_AUDIT.md`, `ROW9_ETALE_AUDIT.md` | Corresponding `check_row*_etale_constants.py` scripts; the general Jacobian/uniqueness arguments are proofs |
| Row-9 complete exclusions for 79 canonical support systems | `collective17/exclusions/BATCH1_PROOF.md`, `collective17/exclusions/batch-m5/BATCH2_PROOF.md`, `collective17/exclusions/batch-m6/REVIEW_ADDENDUM.md` | `collective17/exclusions/check_batch.py` and `batch-m6/check_batch.py`; verification methods differ as stated above |
| Cross-prime restrictions | `cross_prime/CROSS_PRIME_RESTRICTIONS.md`; `CROSS_PRIME_AUDIT.md` | `cross_prime/check_cross_prime.py` |
| Quadratic lifting reduction for row 4 | `tame17/ROW4_QUADRATIC_LIFTING.md`; `tame17/ROW4_QUADRATIC_AUDIT.md` | `tame17/check_row4_quadratic_constants.py`; full ramified coverage is proved separately |
| Complete row-4 support {2,4,10,12,18,19} exclusion | `tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md`; `tame17/ROW4_SMALLEST_SUPPORT_AUDIT.md` | `tame17/check_row4_smallest_support.py`; independent residue census and exact lift |
| Row-8 radius bound and divided identity | `wild17/ROW8_BOUND_AND_DIVIDED_IDENTITY.md`; `wild17/AUDIT.md` | `wild17/enumerate_row8.cpp`; independently reproduced residue census only |
| Row-8 collective leading models and whole-degree-20 formal finiteness | `wild17/blowup/COLLECTIVE_REDUCTION.md`; separate audit of the formal cover | `wild17/blowup/check_collective.py` |
| Row-8 quartic models, exact cluster consequences and a uniform next-lift exclusion | `wild17/blowup/m4/LIFT_CONSEQUENCES.md`, `INDEPENDENT_MODEL_AUDIT.md`, `NEXT_LIFT_AUDIT.md` | `check_independent_model.py`, `check_lift_consequences.py` in the same directory |
| Collective row-9 resultant algebra | `collective17/elimination/FINITE_FLAT_REDUCTION.md` | `collective17/elimination/check_presentation.py`; final generic norms unevaluated |
| Cluster collapse | `two_adic/CLUSTER_COLLAPSE.md` | Proof by valuation rescaling; it is not inferred from finite sampling |
| Two-adic reduction and integral cut | `two_adic/REDUCTION_AND_LIFTING.md` | `two_adic/check_first_saturation.py`; independent `check_integral_syzygy.py` |
| Five-adic classification | `five_adic/REDUCTION.md`; `literature/LOCAL_CLASSIFICATION_AUDIT.md` | `five_adic/check_reduction.py` |
| 19-adic cluster and first jet | `global/P19_CLUSTER_FIRST_JET.md` | `global/verify_p19_first_jet.py` |
| All-degree repair obstruction | `global/REPAIR_EQUIVALENCE.md` | Exact Singular scripts and receipts in `global/` |
| Limitation of cluster-occupancy induction | `cluster_tree/COUNTERMODEL_AND_COUNTS.md` | `cluster_tree/verify_digit_blocks.py` |
| Analytic contraction countermodel and moment bounds | `global_analytic/INTEGRAL_OBSTRUCTION.md` | `global_analytic/verify_integral_countermodels.py` |
| All-place height bound and obstruction to product-formula descent | `global_height/ALL_PLACE_BOUND.md` | `global_height/verify_height_models.py` |
| Derivative compression representation and structural obstructions | `global_matrix/COMPRESSION_AUDIT.md` | `global_matrix/verify_compressions.py` |

The characteristic-17 replay verifies twelve resultants through 12,895
exact evaluations over a sufficiently large extension field, and checks
nine ideal-membership identities by coefficient multiplication. The
classification and the whole-row lift exclusion received separate internal
review. The integral modulo-2 syzygy was checked independently using SymPy
and by the producer's exact arithmetic. Normal and optimized Python runs
pass. These are internal mathematical and computational checks, not
external peer review or proof-assistant certification.

## Outstanding mathematical obligations

For degree 20, an exclusion must still cover all eight remaining
characteristic-17 branches, every normalized coefficient invisible in the
ordinary residue polynomial, and all admissible common-root witnesses.
The finite residue table does not give a finite list of characteristic-zero
polynomials. Rows 6, 7 and 9 now have separately proved finite marked-point
lifting descriptions, but these have not been exhausted. In row 9 alone,
the naive bound is 18 to the power 13 marked assignments. The extension
field has degree ten over F17. Tests restricted to prime-field witnesses
would omit required cases. Unramified lifting is justified for these
three rows only. Row 4 has a complete signed-chart description with local
degree at most eight and ramification index at most two. Its additional
scalar obstruction has not been excluded across the charts. Other branches
retain unresolved ramification issues.

The broad residue-SMT pilot produced no mathematical result: it remained
CPU-active beyond the requested internal timeout and was explicitly
terminated. Its receipt is `tame17/row9-residue-smt-pilot.json`. The
prototype now has an independently tested external wall-clock guard.
No unsatisfiability, enumeration completeness, or proof claim rests on
this unsuccessful experiment. The targeted five-assignment exclusion
uses a separate standard-library finite certificate.

A replacement exact bit-vector encoding in `collective17/` replays the
known extension-field fixture quickly, but bounded searches still return
unknown on timeout. Its complete-domain formulation and subfield split
do not justify an unsatisfiability claim. Canonical zero-witness choices
permit restriction to the 240 eligible row-9 coefficient supports without
losing a possible counterexample. Subsequent complete direct enumeration
and exact lifting exclude 79 of them; 161 systems remain unresolved.
These computations use no SMT unsatisfiability claim.

The row-8 census is complete only for its finite residue conditions. The
remaining 180,341 assignments may have fractional-valuation parameters
and unresolved lifts. They are not a finite list of characteristic-zero
counterexamples or a verified unramified lifting description. The collective
blowup analysis now handles 179,765 of their leading models by finite algebras,
while 576 exceptional assignments retain only a first-scale interval.
Within the 124,068 assignments with J=L=16, the leading quartic models and
one next-lift configuration have now been treated as described above.
Neither the model count nor that conditional exclusion resolves the stratum.

Formal finiteness at prime 19 covers every normalized algebraic degree-20
point, with no unramified assumption or lost nilpotents. It does not compute
the local algebras or prove their generic fibres vanish. Likewise, the exact
finite-flat norm criterion for row 9 has not been evaluated. Neither result
reduces the number of eight unresolved residue branches.

For the full conjecture, there is still no proved uniform obstruction or
valid induction step. The all-degree audit identifies the exact missing
bridge; it does not supply it. Progress at degree 20 alone would not settle
the full conjecture.

The full support diagnostic in `support_frontier/REPORT.md` records 2,482
supports surviving its stated criteria. This remains a diagnostic, not a
list of actual CA polynomials or a completion milestone. Later local
restrictions are recorded separately and are not silently included in
that frozen count.

No complete solution, novelty priority, external validation, or publication
claim is made. At the user's request, the feasible completed work is being
consolidated into a review report. Neither original target is achieved.

## Literature status check

`literature/DEGREE20_STATUS_RECHECK.md` records a fresh primary-source
check of a 2026 article calling 24 the smallest open degree. Its citation
points to the uncorrected Draisma-de Jong 2011 theorem; the authors'
August 2011 erratum explicitly retracts the degree-20 consequence. The
2026 article provides no replacement degree-20 proof. Ghosh's arXiv
record still lists v2 of 21 March 2026 as latest in this bounded check.
This does not constitute a universal search for every public correction
or an independent resolution of the claimed proof.
