# Row 8: a root-radius bound and a divided coefficient identity

This concerns the full characteristic-zero row-8 branch, with every invisible
coefficient allowed. It proves a positive lower bound for every nonzero root
in its 17-root zero cluster, followed by a new necessary residue equation.
It does not exclude the branch or assume unramified lifting.

## Setup

Use a valuation over 17 with `ν(17)=1` and the centered monic normalization

\[
 f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
 \quad a_0=1,\quad a_1=a_{20}=0,
\]

in which every root and every normalized coefficient is integral and

\[
 \bar f=X^{17}(X^3-1).
\]

The three unit residue roots are simple, while the cluster at zero contains
17 roots counted with multiplicity. The exact mean root zero is simple by
the separate prime-19 argument. Thus that cluster contains nonzero roots.

The normalized derivative of degree `j` is

\[
 G_j(X)=\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]

The common witness of `G_3` is a unit; scale that witness exactly to 1.
This is a unit scaling and preserves all integrality properties. It gives

\[
 f(1)=G_3(1)=0,\qquad a_3=-1-3a_2.
\tag{1}
\]

The witnesses of `G_2,G_17,G_18,G_19` all lie in the zero cluster. Indeed,
the ordinary Hasse derivatives of orders 18,3,2,1 reduce respectively to
`3X^2,X^17,3X^18,3X^19`. Each can share only residue zero with the seed.
The mean witness of `G_1` is exactly zero. Orders 4 through 16 have zero
ordinary Hasse reduction; their witnesses can lie in either cluster.

Let

\[
 \delta=\min\{\nu(r): f(r)=0,\ r\ne0,\ \bar r=0\}>0.
\]

This finite minimum exists. A chosen common witness in the zero cluster
either has valuation at least δ or equals zero, interpreted with infinite
valuation.

## Coupled bounds for the low ordinary coefficients

The equation `G_2(w_2)=0` gives

\[
 \nu(a_2)\ge2\delta.
\tag{2}
\]

In particular `a_3` in (1) is a unit. The binomial coefficients in `G_17`
are divisible by 17 except for its leading and constant coefficients.
Its common-root equation therefore gives

\[
 \nu(a_{17})\ge\min\{17\delta,1+\delta\}.
\tag{3}
\]

In `G_18`, the terms indexed by `2≤i≤16` have binomial coefficient
divisible by 17; the index-17 coefficient is a unit. Consequently

\[
 \nu(a_{18})\ge
 \min\{18\delta,1+2\delta,\nu(a_{17})+\delta\}
 \ge\min\{18\delta,1+2\delta\}.
\tag{4}
\]

In `G_19`, the index-2 coefficient is a unit, but (2) makes that term's
valuation at least `19δ`. The coefficients indexed by `3≤i≤16` are
divisible by 17; the indices 17 and 18 have unit coefficients. Equations
(3)–(4) yield

\[
 \nu(a_{19})\ge\min\{19\delta,1+3\delta\}.
\tag{5}
\]

These bounds use only integral coefficients and valuations of actual common
roots. No difference from a residue representative is divided by 17.

## The uniform radius bound

Choose a root `r` attaining δ. The ordinary `X^17` term of `f(r)` has
valuation exactly `17δ`, since its coefficient `1140a_3` is a unit.
The leading and `X^18` terms have valuations at least `20δ`. For every
middle deficiency `4≤j≤16`, the ordinary coefficient is divisible by 17,
so the corresponding term has valuation at least `1+4δ`. Finally,
(3)–(5) show that each of the ordinary terms of degrees 3,2,1 has
valuation at least

\[
 \min\{20\delta,1+4\delta\}.
\]

If `δ<1/13`, the `X^17` term is uniquely of smallest valuation. It cannot
cancel in `f(r)=0`. Hence

\[
 \boxed{\delta\ge1/13.}
\tag{6}
\]

Since `16δ>1`, the simpler consequences of (3)–(5) are now

\[
 \boxed{\nu(a_{17})\ge1+\delta,\quad
 \nu(a_{18})\ge1+2\delta,\quad
 \nu(a_{19})\ge1+3\delta.}
\tag{7}
\]

In particular all three coefficients lie in `17m_O`, where `m_O` is the
maximal ideal. This is stronger than their mere positive residue valuation.

## A divided exact equation

Substitute (1) into `f(1)=0`. With `C_j=binom(20,j)`, the exact identity is

\[
 0=-17\cdot67-17\cdot190a_2
   +\sum_{j=4}^{16}C_ja_j
   +1140a_{17}+190a_{18}+20a_{19}.
\tag{8}
\]

Every term belongs to `17O`; (7) places the last three terms in `17m_O`.
Divide (8) by 17 and reduce. Since `ν(a_2)>0`, this proves

\[
 \boxed{\sum_{j=4}^{16}\frac{\binom{20}{j}}{17}\bar a_j
       =67=-1\quad\text{in characteristic }17.}
\tag{9}
\]

This excludes the assignment in which all middle witnesses lie in the zero
cluster. It is stronger than the cluster-occupancy assertion: it specifies
the residues of a nonzero linear combination of their coefficients.

## Finite residue reduction and a single-unit consequence

Let ζ be a primitive cube root in `F_(17^2)`; the unit roots of the seed are
`1,ζ,ζ^2`, and the other possible witness residue is 0. For each degree
`4≤j≤16`, choose `ρ_j` among these four roots. The normalized common-root
equation determines `ā_j` successively:

\[
 \bar a_j=0\quad(\rho_j=0),
\]
\[
 \bar a_j=(\binom j3-1)\rho_j^j
  -\sum_{i=4}^{j-1}\binom ji\bar a_i\rho_j^{j-i}
  \quad(\rho_j^3=1).
\tag{10}
\]

This proves residue-field containment, without assuming rational
coefficients or unramified lifts. There are at most `4^13` marked residue
assignments before (9), with 13-step triangular determination of the
coefficient residues. This remains a residue reduction, not a finite
classification of characteristic-zero solutions.

If exactly one middle witness is a unit, at degree `j`, all other middle
coefficient residues vanish. Condition (9) becomes

\[
 \frac{\binom{20}{j}}{17}(\binom j3-1)\rho_j^j=-1.
\]

Checking the 13 integers in this equation gives exactly one possibility:

\[
 \boxed{j=11,\quad\rho_{11}=1,\quad\bar a_{11}=11.}
\]

Thus a single outside witness, if it occurs, must be the Hasse-order-nine
witness at the normalized unit root 1. This case is not excluded here.

## Common-root obstructions and complete residue census

Two established common-root obstructions, specialized from
[CLO, Proposition 15](https://arxiv.org/html/1208.5404), give extra finite
filters. Their short proofs are included to make the linkage explicit.

* No exact root can be shared by `f,H_4f,H_16f`. If there were one,
  translate it to 0 and perform integral root normalization at the prime 2.
  The coefficients of `X^4` and `X^16` vanish exactly. Lucas visibility for
  degree 20 at 2 has only exponents 0,4,16,20, so the reduction is `X^20`,
  contrary to the retained unit root.
* No exact root can be shared by `f,H_5f,H_10f,H_15f`. Translate that root
  to 0 and normalize at 5. The three visible nonleading coefficients at
  exponents 5,10,15 vanish, again leaving `X^20` and contradicting a unit
  root.

Normalized coefficient integrality in these arguments comes from the
common-root equations for all normalized derivatives. It holds after
translation to any root; the translated mean coefficient need not vanish.

In row 8 each unit residue root is simple, so common witnesses with the
same unit residue are the same exact root. Therefore the residue labels
for normalized degrees 4 and 16 cannot be the same unit label. Nor can
those for normalized degrees 5,10,15 all be the same unit label. This
argument uses the nontrivial common-root obstructions, not simplicity
alone.

The complete finite enumeration gives:

| Stage | Marked middle-witness residue assignments |
|---|---:|
| All 13 labels in `{0,1,ζ,ζ²}` | 67,108,864 |
| After divided identity (9) | 233,310 |
| After the two common-root obstructions | 180,341 |

These counts refer only to the 13 middle witness residues. The zero-cluster
witnesses retain unresolved ramified displacements; the table does not
enumerate characteristic-zero candidates or their lifts. Its nonempty
outcome does not establish consistency of all higher-precision conditions.

The producer `enumerate_row8.cpp` uses the basis `1,ζ` with
`ζ²+ζ+1=0` and the simplified triangular recurrence (10). The independently
written `check_row8_census.cpp` uses the different field presentation
`s²=14`, cube roots `1,8+9s,8+8s`, and the full normalized derivative
recurrence including its leading and index-3 terms. Both traverse all
`4^13` assignments and agree on both counts and every histogram bin for
the number of unit witnesses. Each execution was externally capped at
90 seconds; they finished in approximately 1.4 and 2.1 seconds respectively.

## Exact replay

`check_row8_bound.py` checks all nineteen seed Hasse gcds, the binomial
valuations, the coupled valuation-bound arithmetic, the integer identity
(8), every single-unit possibility, and every displayed sample in the
census receipt. It also checks agreement of the two independent complete
census receipts. Normal Python and `python -O` pass with identical output.

```sh
clang++ -O3 -std=c++17 enumerate_row8.cpp -o enumerate_row8
clang++ -O3 -std=c++17 check_row8_census.cpp -o check_row8_census
./enumerate_row8 > row8-residue-enumeration.json
./check_row8_census > row8-independent-census.json
python3 check_row8_bound.py
python3 -O check_row8_bound.py
```

The saved Python receipts are `row8-bound-replay.json` and
`row8-bound-replay-optimized.json`. The census receipts contain the complete
unit-count histograms and one surviving sample for each attainable count.

Independent adversarial review is recorded as PASS in `AUDIT.md`. It
checks the general valuation/division argument, arbitrary ramification,
the residue-field containment and complete marked-assignment coverage,
and the exact-root collision filters. The reviewer independently compiled
the native enumerator and reproduced its receipt, and its separate small
arithmetic checker passes normally and under `-O`. No stronger optional
radius bound is included in that audit.

## Boundary

Neither a multiplicity bound nor the cluster-collapse lemma alone settles
the remaining branch. In particular, one missing middle Hasse order does
not automatically force the blowup polynomial to be a binomial: lower
coefficients can survive and their derivative roots can move. No such
unproved reduction is used above.

The proved results are the root bound (6), coefficient bounds (7), divided
identity (9), and triangular finite residue test (10). The characteristic-
zero lifting problem, including its possible ramification, remains open.
The known global multiplicity bound is not needed for these conclusions;
no additional branch contradiction from that bound is asserted. Rows 1,2,5
are not classified or excluded by this row-8 calculation.
