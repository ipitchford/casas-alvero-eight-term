# Independent audit of the eight-term coverage argument

24 September 2026.

**Verdict: PASS for the mathematical assembly.** The fourteen exact
seven-total-term supports left by the independently audited inventory have
nineteen compatible characteristic-seventeen seed cases. Every case has a
proof of exclusion. Together with the preceding theorem excluding at most
six centered terms, these results imply:

> Every nontrivial characteristic-zero Casas–Alvero polynomial of degree
> twenty has at least eight nonzero monomials after centering, counting the
> leading monomial.

This is an internal review of the written implications and complete case
cover. It is not a new independent replay of all finite identities, an
external referee report, a priority judgment, or a proof of unrestricted
degree twenty. The final assembled manuscript was still being drafted at
the time of this audit; this verdict concerns the source proofs identified
below, not an unread subsequent transcription.

## 1. Normalization and exact support

I checked the indexing and quantifiers before combining the local results.
After translating the unique nineteenth-derivative root to zero and making
the polynomial monic, write
\[
 f=X^{20}+\sum_{j\in S}c_jX^{20-j},\qquad
 S\subseteq\{2,\ldots,19\},\quad c_j\ne0.
\]
Thus the term count is \(1+|S|\), and the indices in the inventory are
deficiencies, not exponents. The mean-root restriction makes the linear
coefficient nonzero, so exactly seven total terms correspond to exactly
six deficiencies including 19.

An assumed complex solution can first be specialized to an algebraic
solution with the same exact support: adjoin the inverse of the product of
the active coefficients to its polynomial common-root equations. This
preserves each stipulated nonzero coefficient. It precedes choosing a
valuation and does not claim to preserve a transcendental point's already
chosen local stratum.

Minimum-root valuation normalization retains a unit root and makes every
root integral. The normalized derivative equations
\[
 G_j(X)=\sum_{i=0}^j\binom ji a_iX^{j-i},\qquad
 f=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\]
then prove the integrality of every \(a_j\) inductively. This is the
needed stronger conclusion; ordinary coefficient integrality alone would
not justify the divided derivatives. Further normalizations used in the
seed proofs are unit scalings and preserve exact support. All finite
ramification remains allowed.

The complete seed classification is over the algebraic closure of the
residue field. Its coefficient-zero charts and possible extension-field
witnesses are included. The monomial seed is impossible because a unit
root was retained. These points are supplied by
`work/casas-alvero-full/support_frontier/prime17/CLASSIFICATION.md` and its
independent audit, rather than by a mere enumeration of prime-field
coefficient tuples.

## 2. Inventory and seed routing

The inventory and its independent integer-determinant reconstruction give
\[
 \binom{17}{5}=6188\longrightarrow586\longrightarrow348
 \longrightarrow14.
\]
The stages are the singleton visibility tests, guarded two-visible tests,
and the CLO missing-index determinant. The matrix uses missing deficiency
indices \(\{2,\ldots,18\}\setminus S\), with derivative order \(20-j\)
at index \(j\). Its interpretation is reviewed in
[INVENTORY_AUDIT.md](INVENTORY_AUDIT.md). No Massri filter or previously
proved closed support mask is needed for this fourteen-entry inventory.

At the visible indices \((2,3,17,18,19)\), the ordinary coefficient
tuples of the nine seeds are
\[
\begin{gathered}
(0,0,16,0,0),\ (14,0,16,0,3),\ (14,8,16,12,0),\\
(14,0,0,11,8),\ (14,2,0,0,0),\ (14,2,0,11,6),\\
(14,2,0,14,3),\ (0,16,0,0,0),\ (0,16,0,14,3).
\end{gathered}
\]
A seed is compatible precisely when each of its nonzero visible
coefficients occurs at an index in the exact support. This is a necessary
routing test: an active characteristic-zero coefficient is allowed to
have zero residue. Applying it independently gives the following complete
table, before applying the stronger exact-zero restriction on row 4.

| Label | Exact deficiency support | Compatible rows | Exclusions covering every row |
|---|---|---|---|
| \(S_1\) | \(\{2,3,4,10,12,19\}\) | 5, 8 | Row-5 completion; row-8 divided identity |
| \(S_2\) | \(\{3,4,9,10,12,19\}\) | 8 | Row-8 divided identity |
| \(S_3\) | \(\{3,4,5,10,13,19\}\) | 8 | Row-8 divided identity |
| \(S_4\) | \(\{3,4,10,12,15,19\}\) | 8 | Row-8 divided identity |
| \(S_5\) | \(\{3,7,9,10,16,19\}\) | 8 | Row-8 divided identity |
| \(S_6\) | \(\{3,6,10,16,17,19\}\) | 1, 8 | Nonzero-\(a_3\) row-1 obstruction; row-8 divided identity |
| \(S_7\) | \(\{7,8,10,16,17,19\}\) | 1 | Unit-\(a_{16}\) row-1 obstruction |
| \(S_8\) | \(\{10,12,13,16,17,19\}\) | 1 | Unit-\(a_{16}\) and mixed row-1 obstructions |
| \(S_9\) | \(\{6,10,15,16,17,19\}\) | 1 | Unit-\(a_{16}\) row-1 obstruction |
| \(S_{10}\) | \(\{9,10,15,16,17,19\}\) | 1 | Unit-\(a_{16}\) and mixed row-1 obstructions |
| \(S_{11}\) | \(\{2,4,10,12,18,19\}\) | 4 | Complete row-4 \(J=\{4,10,12\}\) exclusion |
| \(S_{12}\) | \(\{3,4,10,13,18,19\}\) | 8, 9 | Row-8 divided identity; complete row-9 \(J=\{4,10,13\}\) exclusion |
| \(S_{13}\) | \(\{2,4,10,17,18,19\}\) | 1, 2, 4 | Quadratic-family A row 1; new row-2 proof; row-4 exact \(a_{17}=0\) restriction |
| \(S_{14}\) | \(\{4,10,16,17,18,19\}\) | 1 | Quadratic-family B exclusion |

There are nineteen support/seed pairs. Rows 3, 6, and 7 are incompatible
with every support on this list. No argument excluding those entire rows
is needed here.

## 3. The inherited row-8, row-4, and row-9 implications

### Row 8

`research/SEVEN_TERM_FRONTIER.md` supplies the seven row-8 exclusions in
the table. Its 1,216 markings cover the full root domain
\(\{0,1,\zeta,\zeta^2\}\subset\mathbf F_{17^2}\), including zero
residues for active coefficients and witnesses. Inactive derivatives
may canonically use the exact common witness zero. Their coefficients
are then exactly zero; the triangular recurrence retains every possible
active marking.

The necessary divided identity is established by valuation bounds in the
seventeen-root zero cluster, including the lower bound
\(\delta\ge1/13\). It is not an assumption that arbitrary positive
valuations are integral. All seven finite domains are empty under that
identity, so the whole row-8 branch for each listed exact support is
excluded. The old note's references to other rows as unresolved were
accurate at that earlier stage; the new proofs below supply precisely
those missing branches.

### Row 4 for \(S_{11}\)

The global bridge in `research/GLOBAL_SUPPORT_COROLLARY.md` puts this
exact support into
`work/casas-alvero-full/tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md`, with
active middle indices \(J=\{4,10,12\}\). The independent audit of that
proof establishes complete coverage of both double-cluster orientations
and all \(2\cdot17^3=9826\) markings in the full algebraic root domain.
Present coefficient residues are not required to be nonzero.

The two surviving residue markings have a unit Jacobian. The subsequent
precision bound is valid after adjoining an arbitrarily ramified
candidate: a hypothetical difference of least valuation below the
required precision cannot cancel against the higher-valuation nonlinear
terms when the linear Jacobian is a unit. The same argument fixes the
critical-root precision. The recorded obstruction
\(17^2(9+4\alpha)\bmod17^3\) is nonzero; its residue has norm 4.
Thus this is a whole exact-support exclusion, not merely a computation
over unramified coefficients or prime-field root choices.

### Row 9 for \(S_{12}\)

`work/casas-alvero-full/collective17/exclusions/BATCH1_PROOF.md` contains
the complete case \(J=\{4,10,13\}\). The underlying quotient is
\(q=f/[X(X-1)^2]\), whose reduction has seventeen distinct nonzero
roots in the certified degree-ten residue extension. The complete
domain has \(17^3=4913\) markings, with one survivor and one Frobenius
orbit. The saved residue and lift records identify the exact global
support \(\{3,4,10,13,18,19\}\).

This square system permits the root near one to move; it does not
incorrectly force that root to equal one before imposing the remaining
equation \(T=0\). Its root Jacobian is diagonal with unit entries. The
minimum-valuation argument therefore transfers the saved precision to
any ramified candidate. The remaining equation has
\[
 T\equiv3179=11\cdot17^2\pmod {17^3},
\]
which excludes that survivor. Only this small complete case is required
for the eight-term theorem. The much larger, incomplete whole-row-9
coverage program and the later m6 native census are not dependencies.

### Row 4 for \(S_{13}\)

Here row 4 is excluded before any lifting enumeration. Its mean is a
simple reduced root and the only common residue root with the third
Hasse derivative is zero. The actual common witness is consequently the
exact mean zero, so \(a_{17}=0\) exactly. This contradicts the exact
support \(S_{13}\). The argument is root uniqueness at a simple reduced
root, not an inference from \(\bar a_{17}=0\).

## 4. The newly completed cases

The following source proofs and their independent argument audits supply
the remaining cases. I checked their hypotheses against the exact
supports and their preliminary finite covers; this assembly review does
not substitute a new numerical run for those proof reviews.

- **\(S_6\), row 1:** `next-stage/ROW1_RAMIFICATION.md` and
  `ROW1_RAMIFICATION_AUDIT.md`. The active \(a_3\) is nonzero exactly.
  The preliminary valuation argument justifies the first divided sieve;
  its eight binary markings leave only the unit-\(a_{16}\) pattern.
  The ensuing value-group obstruction compares an approximation in the
  proved \((1/15)\mathbf Z\) field with a parameter of value \(3/2\),
  without placing the actual candidate in that field. The later direct
  jet theorem is an alternative strengthened route, not a missing
  dependency needed to make this earlier proof work.
- **\(S_7,S_9\), row 1:** `next-stage/ROW1_UNIT16.md` and
  `ROW1_AUDIT.md`. The preliminary sixteen-marking sieves for each support
  leave only the unit-\(a_{16}\) residue pattern. Their exact absent
  coefficients satisfy the uniform theorem's hypotheses, in particular
  \(a_2=a_3=a_4=a_{18}=0\). The displacement argument covers the
  entire wild cluster, including the boundary scales and exact root one.
- **\(S_8,S_{10}\), row 1:**
  `next-stage/last-four/middle/MIXED_STRATA.md` and `MIXED_AUDIT.md`.
  The complete sixteen-marking sieve in each support leaves the
  unit-\(a_{16}\) pattern and one mixed pattern. The former satisfies
  the preceding uniform theorem; the latter is excluded by the mixed
  proof. The corrected argument allows the leading active coefficient
  to have the small fractional valuation forced by its actual lowest
  derivative term. Algebraic-closure polynomial identities and cluster
  multiplicities cover both nonzero and zero leading-position cases.
- **\(S_1\), row 5:** `next-stage/ROW5_COMPLETION.md` and
  `ROW5_COMPLETION_AUDIT.md`. Its complete first divided sieve leaves ten
  markings, treated in six cases. The proof either uses a unit-Jacobian
  precision argument or a separately justified valuation comparison.
  No division by a potentially vanishing parameter discards a case.
  The already excluded row 8 is the only other seed for this support.
- **\(S_{14}\), row 1:**
  `next-stage/last-four/quadratic/B/B_EXCLUSION.md` and `B_AUDIT.md`.
  The proof covers all small/unit occupancies of the low-derivative
  witnesses before applying its finite marking sieve. The eventual
  scaled witness residues lie in \(\mathbf F_{17}\) by the proved
  residual polynomial, rather than by assumption. The audited second
  jet retains the degree-nineteen Hasse-second-derivative contribution.
- **\(S_{13}\), row 1:**
  `next-stage/last-four/quadratic/A/A_ROW1_EXCLUSION.md` and its two
  audits. Its small/unit occupancy cover is complete. The only surviving
  occupancy reduces to the corrected B jet argument with error terms of
  value at least one, strictly beyond the required \(2/16\) precision.
  This transfer is proved by estimates and unit-Jacobian control, not
  inferred from coinciding prime-field residues.
- **\(S_{13}\), row 2:**
  `next-stage/last-four/row2/ROW2_PROOF.md` and `ROW2_AUDIT.md`.
  I separately audited the complete proof and independently reconstructed
  its finite coefficient identities. The proof includes the preliminary
  \(\mu<1\) contradiction, the unit degree-nineteen term in the
  second Hasse derivative, both vanishing leading-parameter cases, and
  the full local quartic-cluster collapse lemma. The resulting exact
  quadruple root yields the rational parameter relation and the final
  simple-root contradiction modulo \(17^2\). It applies to arbitrary
  ramification and both exterior quadratic roots. The reviewed source
  hash is
  `d6bc0338a391347061745e57a9559dd745bd63d1c2c6c9f918426a7c38645ea0`.

## 5. The lower-term dependency is complete and noncircular

The separate assertion excluding at most six total terms is supplied by
`outputs/casas-alvero-review/evidence/seven-terms/PROOF.md` and its
integrated audit. Its dependency chain is as follows.

1. The elementary visibility conditions force at least five total terms.
   For exactly five, the prime-3 test and published CLO determinant leave
   only \(\{4,10,17,19\}\). The complete characteristic-thirteen
   closed-mask exclusion in the earlier extension proof removes it,
   yielding at least six total terms.
2. The exact six-total-term sieve leaves five supports before the two
   characteristic-thirteen masks. The masks remove
   \(\{4,10,12,17,19\}\) and \(\{8,10,16,17,19\}\).
   The remaining exact supports are
   \(\{3,4,10,18,19\}\), \(\{3,10,16,17,19\}\), and
   \(\{4,5,10,17,19\}\).
3. The preceding A and B exclusions remove the first two. The later
   completed C proof removes the third. That C proof covers every
   algebraic-closure coefficient chart and all six final marked
   configurations, with the arbitrary-ramification implications checked
   in its integrated audit.

Accordingly the old six-term frontier note's statement that C was still
open is a preserved historical stage, expressly superseded by the later
complete C proof. It is not the endpoint of the dependency chain. None
of these lower-term arguments assumes the present eight-term conclusion
or the later characteristic-seventeen support exclusions.

The lower-bound chain imports the published CLO determinant theorem and
the indicated established visibility methods; the computer-assisted
mask and exact-family exclusions retain their written proof and internal
review dependencies. Their prior-art or external-refereeing status is not
changed by this assembly audit.

## 6. Independent assembly check and conclusion

[check_eight_term_assembly.py](check_eight_term_assembly.py) independently
reconstructs the seed routing from the displayed coefficient tuples and
the fourteen exact supports. It checks equality with both saved inventory
receipts, verifies every compatible pair has exactly a listed proof
route, and checks the older row-9 record's exact support, complete domain
size, unique orbit, and recorded nonzero obstruction. It hashes the
reviewed source proofs and audits so this verdict can be tied to those
inputs.

Normal and optimized Python produced identical receipts:
[eight-term-assembly-normal.json](eight-term-assembly-normal.json) and
[eight-term-assembly-optimized.json](eight-term-assembly-optimized.json).
The script is intentionally an assembly and saved-record consistency
check; it does not prove a cited theorem, re-enumerate a finite domain, or
turn the existence of an audit file into mathematical evidence.

The lower-term theorem excludes at most six terms. The complete
fourteen-support, nineteen-case argument excludes exactly seven terms.
These disjoint conclusions give the stated bound of at least eight
centered terms. I found no uncovered support, seed, coefficient-zero
residue case, or ramification restriction in this assembly.

## Portability addendum

The read-only assembly checker now resolves its inputs relative to its own
location in either the workspace or an extracted review bundle. The bundle
mapping is explicit:

| Original logical source prefix | Bundle location |
|---|---|
| `work/casas-alvero-upgrade/next-stage/` | `research/next-stage/` |
| `work/casas-alvero-upgrade/research/` | `new-results/` |
| `work/casas-alvero-full/` | `evidence/full/` |
| `outputs/casas-alvero-review/evidence/seven-terms/` | `evidence/seven-terms/` |

The `new-results/` choice preserves the bundle's existing layout. A missing
packaged input causes failure; the bundled checker does not fall back to a
workspace copy. The keys in `inputSHA256` remain the original logical
source names in both layouts, while their values hash the actual local
bytes being reviewed.

Normal and optimized runs pass in both locations and are byte-identical
within each location. The workspace and bundle mathematical receipt data
also agree exactly. Of the 34 input hashes, 32 agree across locations.
The two exceptions are `research/GLOBAL_SUPPORT_COROLLARY.md` and
`research/SEVEN_TERM_FRONTIER.md` under the upgrade source prefix. Their
packaged copies replace only the relative link prefix
`../../casas-alvero-full/` with `../evidence/full/`; direct byte comparison
after precisely that replacement confirms no other change. Their source
and packaged hashes also match the bundle's `PACKAGING_TRANSFORMS.json`.
The differences are preserved and reported, not normalized out of the
receipt.

The four run receipts and the exact comparison are retained as
`eight-term-assembly-normal.json`, `eight-term-assembly-optimized.json`,
`eight-term-assembly-bundle-normal.json`,
`eight-term-assembly-bundle-optimized.json`, and
`assembly-portability.json`. This revision changes path resolution only;
the mathematical checks, coverage conclusion, and proof-verification
boundary are unchanged. It launches no census or proof computation.
