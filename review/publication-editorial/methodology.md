# Methodology specialist review

**Recommendation: Minor Revision.** I found no blocking defect in the
examined replay dependency chain or its connection to the manuscript's
finite arithmetic claims. One factual description of the retained row-8
data should be corrected. This recommendation concerns methodology, not
historical priority, significance, or external mathematical acceptance.

## Submission and scope

Reviewed the frozen submission with SHA-256
`f536907e982066d2b72ab175b2947dbff10abf080b3edd3e4e21cb7c7d61fa4a`.
Its manuscript and PDF hashes match the assigned values:

- `PAPER.md`: `73d970c269f0420c54bfffb6a39b606920a34a504cf89f335696d5fb86851348`.
- `PAPER.pdf`: `55220014fb8b0be4f514797f7860deb15a2d0f99454b7011697dcf96d199c79a`.

I compared all 1,010 archived files with the supplied source copy after
the tests; every file matched. The submission was not edited. I used the
manuscript, executable source, certificate data, reproduction instructions,
and the supplied baseline receipt. I did not consult the other reports in
this editorial round or use earlier mathematical review verdicts as
evidence for this recommendation.

**Prior involvement limits independence.** I previously contributed to
parts of the characteristic-thirteen work, the characteristic-seventeen
classification and row-9 computation, the assembly checker and its
portability changes, and the row-2 arithmetic/typewritten material. I also
performed earlier internal checks of several of these components. This
is therefore a fresh internal methodology inspection of a frozen artifact,
not a blind review by a researcher independent of its production. The
fresh executions below are not newly independent implementations.

## Fresh verification

I ran the documented integrity check, the new replay runner, the inherited
default runner, and the publication mutation controls. All execution that
could write evidence occurred in the runners' temporary copies; logs are
outside the submission.

| Check | Fresh result |
|---|---|
| Top-level manifest | PASS, 1,009 listed files |
| `replay_new.py` | PASS, 16 checkers and 32 normal/optimized executions; each pair's output identical |
| `replay.py` | PASS, 27 top-level inherited checks; no omission on this host; 37.264 seconds of recorded child execution |
| `test_publication.py` | All eight mutation executions rejected their faulty inputs, comprising four fault types in two Python modes |
| Source copy versus frozen ZIP | All 1,010 files identical after execution |

The fresh replay records are under
`methodology-artifacts/new-replay/` and
`methodology-artifacts/inherited-replay/`; the concise record is
[methodology-artifacts/summary.json](methodology-artifacts/summary.json).
SymPy was available for this run. I inspected the unavailable-SymPy branch
and its explicit omission record but did not repeat the entire inherited
suite in a second environment without SymPy.

## Dependency closure and proof-to-code semantics

The essential distinction is maintained: the claimed theorem needs the
lower-term proof, the fourteen-support reduction, and every compatible
local branch. Successful execution alone does not establish the valuation
or case-cover implications.

**Lower-term dependency.** Appendix A.8 names concrete data and scripts
for the characteristic-thirteen mask exclusions, seed classifications,
resultants, and final C jets. The top-level inherited replay reaches
`evidence/seven-terms/replay.py`, which in turn runs its preceding
six-term package and both Python modes of the C checks. I traced its
twenty preceding check entries against the listed Appendix A components.
The support frontier is reconstructed from fresh generated data, and the
six final marked C cases are compared with the inherited gcd data. The
proof does not silently depend on the optional large characteristic-zero
resultant calculation for C.

**Fourteen-support reduction and assembly.** The new inventory enumerates
all `combinations(range(2,19),5)` together with index 19, applies guarded
visibility tests, and forms the CLO matrix directly. It checks the exact
counts 6,188, 586, 348, and 14, plus the complete surviving list. The
separate assembly checker compares that list, reconstructs the compatible
seeds, and binds the nineteen support/seed pairs to their proof routes.
Its file hashing and saved-record checks are expressly described as
assembly checks, not as verification of the mathematical content of those
files. The code does not mistake an active coefficient's zero residue for
an exact zero coefficient.

**Complete characteristic-seventeen classification.** The classification
checker verifies ideal-membership identities coefficientwise and
reconstructs the resultants from the actual Hasse polynomials. Its
interpolation is exact: it bounds each coordinate degree, uses more
distinct field points than that bound, and works in the verified
289-element field. This is materially stronger than testing a selection
of prime-field points. The separate chart cover, denominator conditions,
and coefficient-zero cases remain written mathematical dependencies;
checking the nine displayed seed examples by themselves would not prove
classification completeness.

**Repaired row-8 dependency.** `replay_new.py` explicitly includes
`../../new-results/check_row8_seven_term.py`. The repair is substantive:
the theorem's seven small censuses now run in the advertised new replay,
rather than merely being present as files. Source inspection confirms
that the field polynomial is checked irreducible, the four distinct
domain entries exhaust zero and the three cube roots of unity, and the
full Cartesian products total 1,216 assignments. Inactive coefficients
use the exact witness zero; every active marking retains zero as a
possible residue. The triangular recurrence and divided sum match
Appendix B. The nonzero survivor test is an exact test, with no random
sampling or collision filter. The 17-adic bound that permits division by
17 is in the manuscript; the code does not purport to prove it.

**Required row-4 and row-9 finite lifts.** The inherited runner actually
recomputes the required small residue domains. The row-9 native code
checks its finite field, verifies seventeen distinct simple roots, visits
the complete domain, and compares the entire survivor list. Its Python
checker reconstructs the polynomial from the derivative recurrence,
checks the exact quotient by `X*(X-1)^2`, checks every saved root equation
at its claimed precision, and recomputes the divided Hasse-second value
at one additional digit before division. Thus the nonzero obstruction is
not accepted solely because a receipt says `EXCLUDED`. The manuscript
separately explains why the square system retains the root near one until
the remaining equation is imposed, and why a unit Jacobian transfers the
precision to arbitrarily ramified solutions. The code and stated
mathematical model agree on these boundaries.

**New local constants.** The new runner includes independent direct
coefficient reconstructions alongside producer checks for the direct jet
and row-2 calculation. The row-2 reconstruction explicitly retains
`comb(19,2) % 17 == 1` and checks the final modulo-289 data. The corrected
quadratic-family checker is executed; the superseded exploratory probe is
not. These are checks of polynomial identities and finite conditions,
not a replacement for the proofs of cluster multiplicity, valuation
bounds, or derivative-witness collisions.

## Omissions and negative controls

The only dependency-sensitive optional Python check is correctly exposed
as an omission when SymPy is unavailable. It concerns a historical
integral-syzygy cross-check outside the eight-term proof's dependency map.
The default m6 action checks saved execution records and survivor/lift
arithmetic; `m6FreshCensusIncluded` is false in this fresh receipt. The
source explicitly identifies the earlier full native runs as executions
of the same algorithm. It does not claim that survivor verification
independently proves the absence of omitted survivors.

This limitation does not obstruct the stated theorem: Appendix B uses the
complete row-9 system with middle support `{4,10,13}`, which was freshly
re-enumerated here. Neither the remaining whole-row-9 systems, the fresh
m6 census, the unrestricted row-8 census, nor the optional exploratory
resultants enter that dependency. The manuscript states this restricted
use. I did not launch any of those larger optional computations.

The new mutation tests exercise a duplicate root-domain entry, an altered
quadratic nonsquare assertion, an altered final residue target, and a
missing support in the inventory. Each is rejected in normal and
optimized Python. The inherited replay additionally alters a resultant
coefficient and a normalization coefficient and requires arithmetic
rejection. These are useful checks that failure paths and optimized-mode
guards operate. They are selected fault injections, not evidence of
exhaustive test coverage or formal correctness. In particular, eight
executions here mean four faults tested twice, not eight independent
fault types.

## Concrete finding requiring a minor correction

**M1 — retained row-8 histograms are overstated.** At `PAPER.md:2391`,
Appendix B says that the source, “full histograms,” and normal and
optimized receipts are retained. The referenced checker constructs the
histograms in memory, but its output stores `attainedSumCount` and
`sumHistogramSha256`, not the histogram entries. The companion normal and
optimized records have these same digest fields. Consequently the stated
data availability is not accurate as written.

The smallest correction is to replace “full histograms” with “histogram
digests and assignment counts.” Alternatively, actually export the full
histograms and update the records and manifest. The existing complete
census already reruns successfully, so this finding is a documentation
correction and does not invalidate the exclusion or require new
mathematical research.

## Confidence and limits

Confidence is **high for the bounded replay results and repaired row-8
dependency**, and **moderately high for the inspected proof-to-code
interfaces and dependency closure**. No missing essential finite check,
accepted failed run, unexplained optional omission, or domain restriction
was found in this pass. I have not reconstructed every proof or certificate
from scratch, formally verified the software, checked the publication
priority, or supplied independence from the earlier producer team. The
methodological evidence supports proceeding after M1 is corrected; it
does not itself supply an external mathematical endorsement.
