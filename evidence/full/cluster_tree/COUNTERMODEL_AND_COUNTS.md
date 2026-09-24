# Cluster occupancy: exact root counts and a maximal-occupancy countermodel

Scope: this gives an unconditional local derivative-count lemma and an explicit
positive-characteristic obstruction to an occupancy-only induction. It does
not construct a characteristic-zero CA counterexample, settle degree 20, or
rule out an argument using characteristic-zero lifting and several primes.

## 1. A separated cluster forbids the derivative of its own size

Use the setup of `../two_adic/CLUSTER_COLLAPSE.md`. A separated cluster `C`
contains `m` roots with multiplicity, and the affine rescaling gives an
integral polynomial

\[
 Q(Y)=A(Y)B(Y),\qquad \bar B=1,\qquad \bar Q=\bar A,
\]

where `A` is monic of degree `m` and the integral scaled coordinates are
exactly the roots in `C`.

**Lemma.** The Hasse derivative `H_m f` has no root in the closed disk of
`C`. For `0<=j<m`, if `p` does not divide `binom(m,j)`, the derivative
`H_j f` has exactly `m-j` roots in that disk, counting multiplicity.
More generally, if `H_j Abar` is nonzero of degree `d`, the count is exactly
`d`. If `H_j Abar` is zero, this reduction gives no count.

**Proof.** Reduction commutes with Hasse differentiation. Thus
`H_m Q mod m = 1`, which cannot vanish at an integral argument.
For the count, `H_j Q` has integral coefficients and reduction of degree `d`.
An integral polynomial with at least one unit coefficient has exactly `d`
integral roots when its reduction has degree `d`. To see this directly over
the algebraic closure, write its factors as `Y-beta` for integral roots and
`1-Y/beta` for nonintegral roots. The latter factors reduce to 1; the scalar
has valuation zero because the original polynomial has Gauss norm 1. Its
reduction therefore has degree equal to the number of integral roots.
The Hasse chain rule transfers this count to the original disk. If
`binom(m,j)` is a unit, the reduction has degree `m-j`. No assumption of
unramifiedness is used.

These are derivative-root counts. The counted derivative roots need not be
roots of `f`. In particular, they do not establish common-root occupancy.

## 2. Digit-block CA polynomials with arbitrary root positions

Let `K` be any field of characteristic `p`. Choose distinct nonnegative
integers `e_i`, integers `1<=d_i<p`, and distinct elements `a_i` of `K`. Put

\[
 n=\sum_i d_i p^{e_i},\qquad
 f(X)=\prod_i(X-a_i)^{d_i p^{e_i}}.
\tag{1}
\]

Thus there is one root location for each nonzero base-`p` digit of `n`.
Write `j=sum_e j_e p^e` in base `p`, and set unused degree digits to zero.
Then

\[
 H_j f(X)=
 \begin{cases}
 \displaystyle\prod_i\binom{d_i}{j_{e_i}}
       (X-a_i)^{(d_i-j_{e_i})p^{e_i}},
       &j_e\le d_e\text{ for every }e,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{2}
\]

**Proof.** In the Taylor product, the factor belonging to `i` is

\[
 ((X-a_i)+T)^{d_i p^{e_i}}
  =\sum_{k=0}^{d_i}\binom{d_i}{k}
    (X-a_i)^{(d_i-k)p^{e_i}}T^{kp^{e_i}}.
\]

The choices `0<=k<=d_i<p` produce unique base-`p` expansions without carries.
Taking the coefficient of `T^j` proves (2).

For every `0<j<n`, either the derivative is zero or at least one factor
`(X-a_i)` remains. Therefore `f` and `H_j f` have a common root. Polynomial
(1) is Hasse–CA for **arbitrary root positions**. It is nontrivial whenever
there are at least two nonzero digits and the positions are distinct.

This is an elementary Lucas/Frobenius construction. No novelty claim is made.

## 3. Every cluster has the maximum possible initial occupancy

Take any nonempty proper subset `S` of the root locations, and let

\[
 m_S=\sum_{i\in S}d_i p^{e_i}.
\]

For every `1<=j<m_S`, the polynomial `H_j f` has a common root with `f`
among the locations in `S`. Indeed, a nonzero derivative which removes all
their factors would have `j>=m_S`. A zero derivative has every root available.
In contrast, `H_{m_S}f` has **no** root at those locations: its derivative
digits remove exactly all factors indexed by `S`, leaving just the factors
outside `S`.

Consequently, every separated cluster in this model has all the initial
common-root occupancies required by the collapse lemma, and the forbidden
occupancy at its own size is absent exactly as the lemma in Section 1 requires.
When `binom(m_S,j)` is a unit, the number of derivative roots there is exactly
`m_S-j`, also matching Section 1.

Nevertheless, a cluster containing two distinct root positions never has a
good residue degree: its own local polynomial

\[
 \prod_{i\in S}(X-a_i)^{d_i p^{e_i}}
\]

is a nontrivial Hasse–CA polynomial of degree `m_S`, by the same formula.
Single-location clusters are already exact powers, so collapsing them gives
no additional information.

This disproves the following proposed inference in positive characteristic:

> Full CA witness occupancy, compatible derivative-root counts, and repeated
> passage to separated clusters force some cluster containing distinct roots
> to have a good Hasse–CA degree.

The countermodel satisfies maximal initial occupancy at every cluster, but
there is no such good-degree cluster anywhere in its tree.

## 4. Arbitrarily many scales, and the degree-20 reductions

Work over an algebraic closure of `F_p((t))`. For any `r>=1`, choose root
positions

\[
 a_0=1,\quad a_1=t,\quad \ldots,\quad a_r=t^r,\quad a_{r+1}=0
\]

and multiplicities `p^i` at `a_i`. The subsets
`{t^k,t^{k+1},...,t^r,0}` give `r` nested separated clusters containing
distinct roots. Every such cluster has complete initial witness occupancy,
yet every such cluster degree is bad at `p`. Thus an arbitrary number of
blowups does not cure the countermodel.

For degree 20 the two-location versions apply at the following primes:

| p | Digit blocks of 20 | A corresponding Hasse–CA polynomial |
|---|---|---|
| 2 | 4+16 | `X^4 (X-1)^16` |
| 3 | 2+18 | `X^2 (X-1)^18` |
| 7 | 6+14 | `X^6 (X-1)^14` |
| 11 | 9+11 | `X^9 (X-1)^11` |
| 13 | 7+13 | `X^7 (X-1)^13` |
| 17 | 3+17 | `X^3 (X-1)^17` |
| 19 | 1+19 | `X (X-1)^19 = X^20-X` |

Each has only one cluster containing distinct root locations, namely the
whole root set, whose degree is bad. Its proper residue clusters are already
single locations with multiplicity. This explains why an occupancy count
alone cannot turn these reductions into a good-degree collapse.

The construction as stated does not cover degree 20 at 5, because 20 has only
one nonzero base-5 digit. It does not claim that 5 is good or that changing
primes cannot help.

## 5. The missing characteristic-zero input is exact

The positive-characteristic formulas use vanishing binomial coefficients.
Those vanishings are divisibility statements in characteristic zero, not
exact zeros. For example,

\[
 F(X)=X(X-1)^{19}\in\mathbb Q[X]
\]

shares a root with every Hasse derivative of order `1,...,18`, but
`H_19 F=20X-19` shares neither root. Its reduction at 19 is the full CA model
in the last row of the table. Thus even a characteristic-zero model satisfying
18 of the 19 derivative conditions and the same two-cluster geometry need not
satisfy the remaining condition.

Similarly `X^16(X-1)^4` over characteristic zero satisfies orders `1,...,15`
and fails all of `16,...,19`. At those last four orders, its values at roots
0 and 1 respectively are

\[
 (1,1820),\quad(-4,560),\quad(6,120),\quad(-4,16).
\]

The reduction at 2 recovers the Hasse–CA digit-block model, because the
coefficients lost on reduction determine the remaining obstructions.

Therefore an unrestricted proof needs additional exact information coupling
the witnesses across scales: for example, divided derivatives or identities
which prevent these residue occupancies from lifting, or information obtained
at different primes. The cluster-collapse lemma and derivative root counts
alone cannot supply that information. The countermodels isolate this failure;
they do not show that a characteristic-zero counterexample exists.

## 6. Only finitely many primes provide a proper nontrivial cluster

There is also an elementary characteristic-zero limitation. Fix a polynomial
whose roots are algebraic numbers, and work in one number field containing
all its distinct roots `r_1,...,r_s`. Outside finitely many prime ideals,
every nonzero difference `r_i-r_j` is a unit: there are only finitely many
prime divisors of the finitely many differences and their denominators.
At each remaining prime all pairwise distances between distinct roots are
the same. A ball containing two distinct root locations then contains all
root locations. Hence the only separated clusters are single-location
clusters (with their full multiplicities) and the entire root set.

Thus, for any fixed algebraic candidate, only finitely many primes can yield
a **proper** separated cluster containing distinct roots. At other primes,
using the collapse lemma requires good residue degree for the full degree
itself. Choosing successively larger primes does not by itself produce
smaller useful clusters. This does not say that none of the finitely many
exceptional primes works; it identifies exactly where a proof must obtain
further arithmetic information.

## Verification

`verify_digit_blocks.py` expands explicit examples over polynomial rings
`F_p[t][X]`, computes every Hasse derivative directly from binomial coefficients,
and compares with (2). It checks all subset-prefix occupancy and forbidden-size
claims for the examples, including a four-level nested degree-31 model at 2
and all seven displayed degree-20 models. It also checks the two characteristic-
zero partial examples. This finite replay supports the formulas; the proofs
above apply to arbitrary exponents, root positions, and cluster depths.
