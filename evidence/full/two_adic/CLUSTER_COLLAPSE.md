# A separated-cluster collapse lemma

This is a conditional local lemma. It does **not** assert that the required
derivative witnesses lie in a given cluster. That occupancy must be established
independently in every application.

## Statement

Let `K` be an algebraically closed characteristic-zero valued field, with
residue characteristic `p`, and let `f` be a monic polynomial over `K`. Let `C`
be a multiset of `m` roots of `f`, counting multiplicity. Suppose it is a
separated cluster: if `C` contains more than one distinct root, there exist a
root `r_0∈C` and an element `δ∈K*` such that

\[
 \nu(r-r_0)\ge\nu(\delta)\quad(r\in C),
\]

at least one of these inequalities is equality for a root distinct from
`r_0`, while

\[
 \nu(s-r_0)<\nu(\delta)\quad(s\notin C).
\]

Suppose also:

1. For each Hasse derivative order `1≤j<m`, there is a common root of
   `f` and `H_j f` lying in `C`.
2. Every degree-`m` Hasse–Casas–Alvero polynomial over the algebraic closure of
   the residue field is a scalar multiple of an `m`th power of a linear
   polynomial.

Then all `m` roots in `C` coincide exactly. In particular `f` has a root of
multiplicity at least `m` at that point.

For an ordinary residue cluster of an integral polynomial, every root outside
the cluster has distance valuation 0 from its roots, and every difference
inside has positive valuation. If there are distinct roots inside, choose
`δ` to be a difference of minimum valuation inside the cluster. Thus the
separation hypothesis is automatic in the degree-20 residue applications.

## Proof

Assume two roots of `C` are distinct, and choose `r_0,δ` as in the statement.
Factor

\[
 f(X)=U(X)V(X),\qquad
 U(X)=\prod_{r\in C}(X-r),\quad V(X)=\prod_{s\notin C}(X-s).
\]

After changing variables, define

\[
 A(Y)=\delta^{-m}U(r_0+\delta Y)
     =\prod_{r\in C}\left(Y-\frac{r-r_0}{\delta}\right),
\]
\[
 B(Y)=\frac{V(r_0+\delta Y)}{V(r_0)}
     =\prod_{s\notin C}\left(1+\frac{\delta}{r_0-s}Y\right).
\]

All roots of `A` are integral, so `A∈O[Y]` is monic of degree `m`. Its
reduction has both the root 0 and a nonzero root, by the equality condition in
the separation hypothesis. Every nonconstant coefficient of `B` is in the
maximal ideal, because each `δ/(r_0-s)` has positive valuation. Thus `B∈O[Y]`
and `B̄=1`.

The integral polynomial

\[
 Q(Y)=\frac{f(r_0+\delta Y)}{\delta^mV(r_0)}=A(Y)B(Y)
\]

therefore reduces to `Ā`. If `w_j∈C` witnesses order `j<m`, its scaled
coordinate `t_j=(w_j-r_0)/δ` is integral, and the Hasse chain rule gives

\[
 H_jQ(t_j)
 =\frac{\delta^j}{\delta^mV(r_0)}H_jf(w_j)=0,
 \qquad Q(t_j)=0.
\]

Reduction commutes with Hasse differentiation. Hence `Ā` and `H_jĀ` have
the common root `t̄_j` for every `1≤j<m`. By hypothesis, `Ā` is an `m`th power
of a linear polynomial. Since it is monic and has root 0, it equals `Y^m`.
This contradicts its nonzero root. Therefore the roots of `C` all coincide.

No unramifiedness, discrete value group, completeness, Hensel lifting, or
assumption that root differences lie in `pO` enters this argument.

## Two elementary residue degrees usable here

### Degree `m=p^s` in characteristic `p`

Write a monic degree-`m` polynomial as `Y^m+Σ_{i<m}c_iY^i`. Lucas gives
`binom(m,j)=0` in the residue field for `1≤j<m`. The derivative `H_{m-1}` is
the constant `c_{m-1}`, so its common-root condition forces `c_{m-1}=0`.
Descending induction makes each `H_j` the constant `c_j` and forces `c_j=0`.
The polynomial is `Y^m+c_0`, a linear `m`th power over the algebraic closure.

Thus the lemma applies to clusters of size 4 or 16 in characteristic 2,
provided the relevant orders `1,...,m−1` all have witnesses in that cluster.

### Degree 3 in characteristic 17

Translate the common root of `H_2` to 0 and make the polynomial monic. It has
the form `Y^3+bY`. If `b≠0`, a common root `r` with `H_1=3Y^2+b` cannot be 0;
then `r^2=-b`, so `H_1(r)=-2b≠0`. Therefore `b=0`. This proves the required
degree-3 residue assertion at 17. The same argument works in every
characteristic other than 2 or 3, and characteristic 3 follows by the
power-of-`p` argument above.

Consequently, a separated size-3 cluster at the prime 17 containing common
witnesses for both `H_1` and `H_2` must be one exact triple root.

## Degree-20 characteristic-2 consequences

Under the notation and normalization of `REDUCTION_AND_LIFTING.md`:

* In A, the size-4 cluster is at 1. If its witness residues for Hasse orders
  1, 2, 3 are all 1, the cluster is one exact root. Since the normalization
  already makes 1 an exact root, `(X−1)^4` divides `f`.
* In B, the size-4 cluster is at 0. If its witnesses for orders 1, 2, 3 all
  have residue 0, then `X^4` divides `f`. In centered normalized coefficient
  notation this gives the exact equations `a_17=a_18=a_19=0`.

Remember that order `j` corresponds to normalized derivative degree `20−j`.
Thus the relevant witness labels in the normalized residue enumeration are
17, 18, and 19. After the first saturation cuts, 4,096 of the 40,960 marked
assignments in each type have all three of these witnesses in the size-4
cluster. This occupancy count is supplementary computation; the lemma and
its multiplicity conclusion do not rely on the count.

The remaining 36,864 marked assignments per type do not satisfy this
sufficient size-4 occupancy condition. The lemma alone makes no exclusion
claim for them.

## Combining collapse with the simple mean root

For a nontrivial characteristic-zero degree-20 CA polynomial, the centered
root 0 is simple. This is the degree `19+1` case of
[Castryck–Laterveer–Ounaïes, Proposition 15 and the following paragraph](https://arxiv.org/html/1208.5404).
Here is the short proof for this degree. If it were multiple, centered
normalized coefficients would have `a_1=a_19=a_20=0`. Perform the usual
integral root normalization at the prime 19, obtaining integral normalized
coefficients and a unit root. All `binom(20,j)` for `2≤j≤18` are divisible by
19, so the reduced polynomial would be `X^20`, contradicting that unit root.
The argument uses a separate 19-adic normalization; simplicity of the root
is invariant under it.

Therefore any collapsed cluster containing the exact mean root is impossible:

* In A, the cluster at 0 has size 16. If all Hasse orders 1 through 15 have
  witnesses there, collapse would make the mean root multiple. Thus the
  normalized witness labels 5 through 19 cannot all be 0.
* In B, the cluster at 0 has size 4. The normalized witness labels 17, 18,
  and 19 cannot all be 0.

`check_cluster_occupancy.py` re-enumerates all marked assignments and applies
the first saturation cut before these occupancy restrictions. The counts are:

| Type | Marked assignments removed | Coefficient patterns affected | Whole coefficient patterns removed | Marked assignments left |
|---|---:|---:|---:|---:|
| A | 4 | 3 | 0 | 40,956 |
| B | 4,096 | 345 | 0 | 36,864 |

The total is 77,820 marked assignments. There are still 465 A and 603 B
coefficient patterns: every affected coefficient pattern also has an
assignment that avoids the forbidden occupancy. Thus this step prunes marked
incidence data but does not remove any additional coefficient residue point.
