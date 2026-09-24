# Unrestricted degree 20 at the prime 2: reduction and a first saturation step

## Scope

All coefficients of the original degree-20 polynomial are allowed. The results
below give a complete classification of its **normalized residue incidence
data**, followed by a genuine integral syzygy that removes some residue data.
Neither residue type is eliminated. This is not a proof of degree 20 or of the
Casas–Alvero conjecture, and the surviving residue assignments are not claimed
to admit characteristic-zero lifts.

The known characteristic-2 obstruction in degree 5 is not new: Chellali and
Salinier explicitly exhibit the binomial seed in their treatment of degree
`5 p^e` ([primary paper](https://arxiv.org/html/1211.2059), §2). The calculations
here keep all degree-20 normalized coefficients, including those invisible in
the ordinary characteristic-2 reduction.

## 1. Integral normalization and notation

Let a nontrivial characteristic-zero Casas–Alvero polynomial be given. Translate
its unique degree-one derivative root to 0 and make it monic. Extend the
2-adic valuation to a field containing its coefficients and roots. Scale by a
nonzero root of smallest valuation. The resulting roots are integral and at
least one is a unit. Write

\[
 f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
 \qquad a_0=1,\quad a_1=a_{20}=0,
\]

and define the monic normalized derivative of degree `j` by

\[
 G_j(X)=\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]

For each `1 ≤ j ≤ 19`, choose a common root `w_j` of `f` and `G_j`.
All normalized coefficients `a_j` are integral: induction in `j` applies to
`G_j(w_j)=0`, whose constant coefficient is `a_j` and whose preceding terms
are integral. This does not follow merely from ordinary coefficient
integrality; the derivative incidence equations are being used.

Let `O` be the valuation ring, `m_O` its maximal ideal, and normalize the
valuation by `ν(2)=1`. No assertion that `m_O=2O` is made. Bars denote reduction
modulo `m_O`. The residue field may be any extension of `F_2`.

## 2. Exactly two ordinary reductions

Lucas's rule gives

\[
 \bar f=X^{20}+\bar a_4X^{16}+\bar a_{16}X^4.
\]

Initially scaling a unit root to 1 gives `ā_4+ā_16=1`. The fourth Hasse
derivative reduces to `X^16+ā_16`. If `r` is a common root of it and `f̄`, then
`r^16=ā_16` and `f̄(r)=ā_4 ā_16`; consequently `ā_4 ā_16=0`. Hence:

| Type | `(ā_4,ā_16)` | Reduced polynomial | Cluster multiplicities at `(0,1)` |
|---|---|---|---|
| A | `(1,0)` | `X^20+X^16` | `(16,4)` |
| B | `(0,1)` | `X^20+X^4` | `(4,16)` |

Both reduced polynomials satisfy all characteristic-2 Hasse common-root
conditions. In type A, order 16 uses root 1 and all other orders can use 0; in
type B, order 4 uses 1 and all others can use 0. Thus ordinary reduction alone
cannot give a contradiction.

Equivalently, the fourth root of `f̄` is a quintic
`X^5+cX^4+dX`; its fourth Hasse derivative is `X+c`, and evaluation at `c`
gives `cd=0`. Translation by 1 exchanges the two ordinary seeds. It does not
preserve the centered condition `a_1=0`, so the centered normalized coefficient
counts below need not be equal.

## 3. Complete normalized residue incidence data

Every common root `w_j` reduces to 0 or 1, because these are all the roots of
either reduced polynomial. The recurrence

\[
 \bar a_j=\begin{cases}
 0,&\bar w_j=0,\\
 \sum_{i<j}\binom ji\bar a_i,&\bar w_j=1
 \end{cases}
\]

shows inductively that every normalized coefficient residue lies in `F_2`,
even when the residue field is larger. Conversely, choose the witness bits
and define the coefficient bits by this recurrence. Then every reduced
normalized derivative incidence holds, and every witness is a root of the
appropriate seed.

The power-of-two degrees force `(w̄_4,w̄_16)=(1,0)` in A and `(0,1)` in B;
`w_1=0` exactly. The other 16 witness bits, for `j=2,...,19` except 4 and 16,
are free. Thus there are exactly `2^16` marked residue assignments per type.
Different marked assignments can have the same coefficient residues.

| Type | Marked residue assignments | Distinct normalized coefficient patterns |
|---|---:|---:|
| A | 65,536 | 873 |
| B | 65,536 | 1,128 |
| Total | 131,072 | 2,001 |

`enumerate_residue_patterns.py` checks the recurrence, every reduced incidence,
the counts, and the multiplicity of each coefficient pattern. A separate
coefficient-first enumeration by another agent reproduces every pattern and
multiplicity; see `../literature/LOCAL_CLASSIFICATION_AUDIT.md`.

This classifies residue **points**, not the nilpotent residue scheme or its
mixed-characteristic deformations. It is invalid to impose exact equations
`w_j^2-w_j=0` on a characteristic-zero lift.

## 4. Normalize an active power-of-two witness

Put `(m,k)=(4,16)` in A and `(m,k)=(16,4)` in B. The common witness of `G_m`
is a unit with residue 1. Make the additional unit scaling that sets this
witness exactly to 1. It preserves integrality, centering, and all residue
bits. Thus

\[
 f(1)=G_m(1)=0.
\]

This extra normalization is essential below; an arbitrary retained unit root
need not itself witness `G_m`.

The equation `G_m(1)=0`, with `m` a power of two, gives `a_m+1 ∈ 2O`.
Eliminating `a_m` between it and `f(1)=0` gives

\[
 1-\binom{20}{m}
 +\sum_{j\ne m}\left(\binom{20}{j}
  -\binom{20}{m}\binom mj\right)a_j=0,
\]

where `binom(m,j)=0` for `j>m`. The coefficient of `a_k` is odd, while the
constant and every other coefficient are even. Therefore `a_k ∈ 2O`.
It follows that

\[
 f\equiv X^{20}-X^k\pmod{2O[X]}.
\]

Here the congruence is genuinely modulo `2O`, stronger than reduction modulo
the maximal ideal. The odd pivots are `4845` in A and `-8813055` in B.

## 5. A coefficientwise integral 2-saturation certificate

Let `w=w_k` be the common witness of `G_k`; it has residue 0. In the integer
polynomial ring in `a_1,...,a_19,w`, write

\[
 F=f(1),\quad P=f(w),\quad g=G_m(1),\quad q=G_k(w).
\]

Then the following numerator has **every integer coefficient even**:

\[
 S=P+w^m q+(g+1)(F+g+q).                 \tag{1}
\]

Indeed, modulo 2 the four polynomials are

\[
 F=1+a_m+a_k,\quad P=w^{20}+a_mw^k+a_kw^m,
 \quad g=1+a_m,\quad q=w^k+a_k.
\]

Since `m+k=20`, substitution makes the right side of (1) zero as a polynomial.
Thus `T=S/2` belongs to `Z[a_1,...,a_19,w]`. At a characteristic-zero incidence
point all four of `F,P,g,q` vanish, so `S=0`, and consequently `T=0` exactly.
This is an actual element of the 2-saturation of the integer incidence ideal.

Reduction of this **already integral** polynomial at a residue point gives

\[
 \boxed{\bar a_8+\bar a_{12}+\bar a_{18}=0}\quad\text{in A},       \tag{2A}
\]
\[
 \boxed{\bar a_2+\bar a_{12}+\bar a_{18}=0}\quad\text{in B}.       \tag{2B}
\]

For a direct check, evaluate its coefficients at the bit representatives
`a_m=1,a_k=0,w=0`. Since `g` and `F` then evaluate to even integers,
`T` reduces to `(F+g)/2`; its odd coefficients are exactly those in (2A) or
(2B), after its constant and `a_m` contribution cancel. This computation is
polynomial evaluation, not a claim that a genuine coefficient differs from
its bit representative by an element of `2O`.

The standard-library checker `check_first_saturation.py` expands (1) over `Z`
with all 19 coefficient variables retained, verifies coefficientwise evenness,
and checks its reduction on every enumerated coefficient pattern. It gives:

| Type | Coefficient patterns remaining | Marked residue assignments remaining |
|---|---:|---:|
| A | 465 | 40,960 |
| B | 603 | 40,960 |
| Total | 1,068 | 81,920 |

Both normal Python and `python -O` replay pass. The proof of (1)–(2) does not
depend on the pattern-count computation.

The parent independently reconstructed the integer polynomials with SymPy,
checked coefficientwise evenness (148 terms in A and 250 in B), checked both
cuts, and re-enumerated the surviving coefficient patterns without using this
producer's enumeration. Its checker is `../check_integral_syzygy.py`, with
receipts `../integral-syzygy-replay.json` and
`../integral-syzygy-replay-optimized.json`.

## 6. Independent valuation interpretation and a further precision consequence

After §4, every root `r` in the zero cluster satisfies

\[
 \nu(r)\ge 1/14\quad(A),\qquad \nu(r)\ge1/2\quad(B),             \tag{3}
\]

unless `r=0`, where the valuation is infinite. To see this, the coefficient of
`X^k` is a unit. For `1≤e<k` its coefficient has valuation at least
`v_2(binom(20,e))`, strengthened to at least 1 at the other visible exponent
`e=m`. The minimum of the ratios of these bounds to `k-e` is respectively
`1/14` and `1/2`. If `ν(r)` were smaller, the `X^k` term would be uniquely of
smallest valuation in `f(r)`, a contradiction. The constant term is zero and
all higher terms have greater valuation. The checker verifies these finitely
many rational inequalities exactly.

Apply `G_k(w)=0` and the binomial coefficient valuations for the power of two
`k`. Every preceding normalized coefficient is integral, so (3) implies

\[
 \nu(a_{16})\ge8/7\quad(A),\qquad \nu(a_4)\ge2\quad(B).         \tag{4}
\]

In particular, the opposite visible coefficient divided by 2 has residue 0.
Dividing the exact linear identity in §4 by 2 and reducing now recovers
(2A)–(2B). This second proof also accommodates arbitrary ramification.

The same root bounds apply after translating to the other exact root 1:
normalized translated coefficients `b_j=G_j(1)` remain integral by the
translation formula. Thus, when a witness lies in a cluster of multiplicity
four, its distance from the chosen exact root of that cluster is at least
`1/2`. For every **even** derivative degree `j`, expansion at that root then
forces the translated normalized constant coefficient into `2O`: for a term
of positive degree `s`, either `s≥2`, or `s=1` and `j` is even. This provides
additional precision facts, not yet a complete second saturation step.

For example, in A, if `ā_2=1`, its degree-two witness belongs to the cluster
at 1. Hence `a_2+1∈2O`. If in addition the degree-8, degree-12 and degree-18
witnesses all belong to that cluster, then their even-degree Taylor equations
force `a_8+a_12+a_18∈2O`; the linear identity of §4 consequently strengthens
`a_16∈4O`. These are conditional refinements; they do not cover all surviving
marked assignments or yield a contradiction.

## 7. Explicit low-precision points and current limitation

Both charts have exact solutions of every normalized incidence equation over
small finite rings:

* Type A modulo 16: take `a_4=-1`, `a_19=3875`, all other `a_j=0`, and choose
  `w_4=w_19=1`, all other witnesses 0. The ordinary polynomial is
  `X^20-4845X^16+77500X`. Both nonzero normalized derivative values vanish
  exactly, while `f(1)=72656=16·4541`.
* Type B modulo 4: take `a_16=-1`, all other `a_j=0`; choose `w_16=1`, all
  other witnesses 0. The ordinary polynomial is `X^20-4845X^4`, and
  `f(1)=-4844=-4·1211`.

The enumerator directly verifies every normalized derivative and root
incidence in the indicated ring. These points are not characteristic-zero
counterexamples and do not establish even infinite 2-adic liftability. They
show that simply imposing a small integer precision cannot remove both charts.

The remaining task is to control the nonreduced residue incidence scheme and
its ramified lifts, using further integral syzygies or stronger cluster
constraints. The first saturation certificate removes 933 coefficient
patterns but leaves both ordinary reduction types and 1,068 coefficient
patterns. There is presently no full degree-20 exclusion in this note.

The companion `CLUSTER_COLLAPSE.md` proves a general separated-cluster lemma
and combines it with the known simple-mean theorem. Its occupancy restriction
further removes 4 A and 4,096 B **marked assignments**, leaving 77,820 total.
It removes no entire additional coefficient residue pattern: 1,068 remain.
The cluster lemma, its degree-3 characteristic-17 instance, and the
prime-19 simple-mean argument received an independent mathematical audit.
That audit did not review the numerical bounds of §6; the exact finite
inequalities for those bounds are checked by `check_first_saturation.py`.

## Replay

From this directory:

```sh
python3 enumerate_residue_patterns.py
python3 -O enumerate_residue_patterns.py
python3 check_first_saturation.py
python3 -O check_first_saturation.py
python3 check_cluster_occupancy.py
python3 -O check_cluster_occupancy.py
```

Saved receipts are `residue-patterns.json`, `residue-patterns-optimized.json`,
`first-saturation.json`, and `first-saturation-optimized.json`. The two copies
of each receipt should be byte-identical. The supplementary occupancy receipts
are `cluster-occupancy.json` and `cluster-occupancy-optimized.json`.
