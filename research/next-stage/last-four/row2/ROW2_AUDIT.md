# Independent adversarial audit of the row-2 exclusion

24 September 2026. **PASS: no mathematical gap found in the stated exact-support exclusion.**

Reviewed file: `ROW2_PROOF.md`, SHA-256
`d6bc0338a391347061745e57a9559dd745bd63d1c2c6c9f918426a7c38645ea0`.
The producer proof was not edited. This is an internal mathematical audit,
not formal verification, external refereeing, a novelty assessment, or a
claim that all characteristic-17 row-2 candidates are excluded.

The result reviewed is precisely the exclusion of the row-2 reduction for
the centered exact deficiency support `{2,4,10,17,18,19}`. In particular,
the ordinary quadratic coefficient is exactly nonzero. The conclusion
does not alone exclude the support's separate row-1 branch or prove an
eight-term bound.

## Main adversarial questions

The most serious possible failure would be an unsupported change from a
residue witness to an exact witness, or applying the quartic CA lemma to
a cluster without all three required derivative witnesses. I checked both
points, including the degenerate leading models. The proof establishes the
necessary root counts before every exact collision. It retains both signs
of the two outside roots and never equates their exact lifts by negation.

No argument assumes that the candidate's coefficient field is unramified.
The unramified quadratic field is used only to choose comparison roots
of `X²−3`. All distances of actual roots are bounded using valuations,
and the final equations are reduced in the full algebraic residue field.

## 1. Normalization and the initial valuation bounds

The seed is `X(X²−3)(X−1)^17`. Its classes at zero and the two roots of
`X²−3` contain a single root each, counted with multiplicity. The G2
witness has residue one, so normalizing it to the exact root one gives
`a2=−1` without changing the support or integrality.

The H1 witness must be in the 17-root class. H3 has only the residue-one
common location. H2 has possible common residues zero and one, but the
zero class contains only the exact mean; the nonzero exact quadratic
coefficient excludes it. This use of exact support is necessary and valid.

I checked the first `mu<1` argument separately. If `nu(c1)=mu`, a root
displacement of value below `mu/16` makes the `c17 z^16` term uniquely
smallest in the divided root equation. Thus all nonzero displacements
have value at least `mu/16`. At a repeated root, every term in the first
derivative other than `c1` has larger value, a contradiction. Cancellation
of `2T+F` therefore forces both `T,F` to have value `mu` and `c1` to have
larger value. The H3 equation then forces value `mu/17` for its nonzero
displacement, contradicting its root equation. This includes a zero value
of T as an infinite valuation; that alternative cannot supply the required
cancellation when `mu<1`.

Once `T,F` belong to `17O`, every nonzero displacement has value at least
`1/16`. The actual H1, H2 and H3 witnesses then give strict values above
one for `c1,c2,T`. The H2 contribution from degree 19 is correctly retained:
`binom(19,2)=171` is a unit, and its value is at least `17/16>1`.
Witness displacement zero simply makes the corresponding constant
coefficient exactly zero and causes no exception.

## 2. All outside-witness markings are covered

The independent residue calculation gives exactly

| `a mod17` | `b mod17` | Divided relation |
|---:|---:|---:|
| 5 | 14 | 2 |
| 5 | 8 | 6 |
| 9 | 7 | 5 |
| 9 | 6 | 0 |

The surviving residues force both active middle witnesses into the two
simple outside classes. For either comparison root `r0²=3`, the exact
seed representative vanishes at r0, the perturbation is in `17O`, and
the derivative is a unit. A hypothetical displacement of value between
zero and one would have a uniquely smallest linear Taylor term. Thus
each actual root differs from its comparison root by an element of `17O`,
without any unramifiedness assumption on that root.

The exact G4 identity `a=9−(r²−3)²` consequently gives
`nu(a−9)>=2`; the G10 equation gives `nu(b+47628)>=1`. Their combination
with the divided coefficient identity gives `c2−c1−T in17²O`.
The independent calculation confirms `c4/17=8 mod17`, so the cluster
cannot consist of seventeen copies of the exact root one.

## 3. Complete leading-model degeneration analysis

The descending witness bounds and the improved bound on T are valid
for arbitrary positive fractional displacement values. If
`1/16<delta<1/13`, the degree-17 contribution is uniquely smallest in
the divided root equation, giving the required contradiction. Hence
`nu(c1)>=16/13`, `nu(c2)>=15/13`, and `nu(T)>=15/13`.

Scaling by `pi^13=17` therefore gives the integral initial polynomial

`L(Y)=−2Y^17+8Y^4+lambda2 Y²+lambda1 Y`.

All seventeen roots of the class are integral in this coordinate; the
three outside roots supply a unit local factor. Consequently residue
multiplicities of L count the full subclusters. Hasse differentiation
commutes with this integral scaling, so the three actual low-order
witnesses transfer to L. In particular, the H3 common location is zero.

* If `lambda1` is nonzero, the zero subcluster contains exactly one
  root, already the exact root one. H3 therefore vanishes exactly at
  one. The divided relation first forces `lambda2=0`; the H2 witness
  then also equals one, forcing `c2=0` and contradicting `lambda1`.
* If `lambda1=0` and `lambda2` is nonzero, the zero subcluster has size
  two. If a repeated root is there, it must equal the already present
  exact root one: a different repeated root would require at least three
  roots counted with multiplicity. Thus the H3 witness also equals one,
  and the divided relation contradicts the value of c2.
* Otherwise a repeated location eta is nonzero. The equations imply
  `eta²=−lambda2/(2kappa)` and `eta^13=−kappa/2`, while the H2 common
  location v is necessarily nonzero and satisfies
  `v²=−lambda2/(6kappa)` and `v^13=−5kappa/2`. Their ratio would obey
  `rho²=1/3` and `rho^13=5`. Since `(1/3)^6=8 mod17`, this forces
  `rho=7`, whose square is 15 rather than 6. This contradiction works
  over the entire algebraic closure.

These alternatives exhaust the leading degeneracies. The remaining
polynomial is `Y^4(−2Y^13+8)`. Its thirteen nonzero roots are simple and
all three derivative witnesses must be in its size-four zero subcluster.

## 4. The quartic cluster step is justified

The size-four subcluster contains the exact root one. Its other roots,
if distinct, have positive valuation of displacement after the first
scaling; every outside root is strictly farther away. Taking a greatest
internal distance and scaling produces an integral degree-four cluster
factor with at least two distinct residue roots. The normalized outside
factor reduces to a nonzero constant. The actual witnesses for H1,H2,H3
therefore make the residue factor a nontrivial quartic Hasse-CA polynomial.

The good-characteristic assertion used to rule this out is correct.
After centering its H3 witness, a monic quartic is `X^4+A X²+B X`.
For `A=0`, a nonzero B contradicts the common first-derivative root.
For `A!=0`, normalizing an H2 witness to one gives `A=−6,B=5`.
The discriminant is `4725`, nonzero modulo 17, so this quartic has no
repeated root and cannot satisfy H1. Thus all four roots collapse exactly
at one. The proof needs no full classification of the earlier 209 wild
leading models and does not discard a nilpotent case by counting only
reduced points.

## 5. Final exact obstruction and independent arithmetic

After collapse, `c1=c2=T=0`. The denominator `912912` is a 17-adic unit,
and `a−9 in17²O` yields `b−B in17²O` for the stated rational B.
All resulting changes in f have value at least three, because their
parameter multipliers are divisible by 17. The changes in G10 have
value at least two. These are sufficient precision margins for the
subsequent divided equations.

The separate standard-library checker reconstructs the family using
Hasse differentiation, rather than importing producer formulas. It
confirms the four modulo-289 values:

| Expression at `r0²=3` | Remainder mod289 |
|---|---|
| f | `170 r0` |
| f' | `130+283 r0` |
| G10 | `204` |
| G10' | `92 r0` |

The two divided equations give the necessary residual value
`(12r0−4)/(r0+1)=0`. The denominator is nonzero, and the numerator
forces `r0=6`, whose square is 2, not 3. Both signs and all four oriented
outside-witness markings are thereby excluded.

`check_row2_independent.py` passed normally and with `-O`; the receipts
`independent-normal.json` and `independent-optimized.json` are identical.
The checker verifies affine coefficient identities on a spanning parameter
basis, the complete four-entry residue table, the geometric ratio
contradiction, the quartic discriminant, and the exact mod289 remainders.
It does not purport to execute the valuation proof; the reasoning above
is the separate audit of that part.

## Decision and limitations

No blocking or major issue was found. A later integrated theorem must
continue to state the exact-support assumption, cite the normalization
and seed-classification dependency, and separately close the row-1
possibility. No unrestricted-degree or all-degree conclusion follows
from this audit alone.
