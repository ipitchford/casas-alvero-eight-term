# Collective first blowups and a finite formal cover

This is a necessary-condition reduction for the unrestricted degree-20
Casas–Alvero problem. It excludes neither row 8 nor all degree 20. Every
coefficient of the original polynomial remains allowed. The count below is
a count of marked residue assignments, not characteristic-zero solutions.

## 1. Setup and collective scales

Retain the setup and already checked identities of
`../ROW8_BOUND_AND_DIVIDED_IDENTITY.md`. In particular

\[
 f(X)=\sum_{j=0}^{20}\binom{20}j a_jX^{20-j},\quad
 a_0=1,\ a_1=a_{20}=0,\quad \bar f=X^{17}(X^3-1),
\]

all roots and normalized coefficients are integral, and the selected
degree-three normalized derivative witness is exactly 1. Write

\[
 G_j(X)=\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]

Let `w_j` be an actual common root of `f,G_j`. The witnesses of
`G_2,G_17,G_18,G_19` lie in the zero residue cluster. The exact root 0 is
simple. The other 16 roots in that cluster give the positive minimum

\[
 \delta=\min\{\nu(r):r\ne0,\ f(r)=0,\ \bar r=0\},\qquad \nu(17)=1.
\]

The earlier divided identity implies that at least one of
`a_4,...,a_16` has nonzero residue. For a marked residue assignment define

\[
 J=\max\{4\le j\le16:\bar w_j\ne0\},\qquad
 L=\max\{4\le j\le16:\bar a_j\ne0\}.
\]

The triangular equation `G_j(w_j)=0` gives `a_j=0` in the residue field
whenever `w_j=0` in that field. Therefore `4<=L<=J<=16`.

For every `J<j<=16`, the common witness has valuation at least δ (or is
exactly zero). Induction on j in its normalized derivative equation gives

\[
 \nu(a_j)\ge(j-J)\delta. \tag{1}
\]

Indeed indices `i<=J` contribute valuation at least `(j-J)δ`; larger
indices do so by the preceding induction bounds. The already proved
`ν(a_2)>=2δ` is more than needed here.

The binomial coefficients in `G_17` with indices 1 through 16 have
valuation one. In `G_18` the indices 2 through 16 have valuation one; in
`G_19` the indices 3 through 16 have valuation one. The end indices are
units, and the index-2 term in `G_19` is controlled by `ν(a_2)>=2δ`.
Using (1), their actual common-root equations give successively

\[
 \nu(a_j)\ge\min\{j\delta,1+(j-J)\delta\},\quad j=17,18,19. \tag{2}
\]

Choose a root attaining δ. Its `X^17` term in f has valuation exactly
`17δ`. Every other term has valuation at least

\[
 \min\{20\delta,1+(20-J)\delta\}.
\]

Here the ordinary middle coefficients `binom(20,j)` have valuation one;
for `j>J`, (1) supplies the missing powers of the root. Equation (2)
handles the final three terms. Unique-minimum cancellation is impossible,
so

\[
 \boxed{\delta\ge\frac1{J-3}.} \tag{3}
\]

Factor `f=UV`, where U is the monic degree-17 zero-cluster factor and V
is the monic degree-three factor containing the unit roots. Every root of
U has valuation at least δ, including its exact zero root. Consequently
its coefficient of `X^r` has valuation at least `(17-r)δ`. V is integral.
The coefficient of `X^(20-L)` in f therefore has valuation at least
`(L-3)δ`. But that coefficient is `binom(20,L)a_L`, of valuation exactly
one. Thus

\[
 \boxed{\frac1{J-3}\le\delta\le\frac1{L-3}.} \tag{4}
\]

In particular, if `J=L`,

\[
 \boxed{\delta=\frac1{J-3}.} \tag{5}
\]

All inequalities are valuation inequalities of exact roots and
coefficients. There is no assumption that a positive valuation is an
integer, or that a residue representative differs by a multiple of 17.

## 2. Finite leading models when J=L

Choose an actual zero-cluster root π with valuation δ and reduce
`-f(πY)/π^17`. This polynomial is integral: equivalently use the factorization
`U(πY)/π^17` times the integral polynomial `V(πY)`. The latter reduces to
the nonzero constant `V(0)=-1`. Its reduction g is monic of degree 17.
It has roots 0 and 1.

Put `m=20-J`. In the case `J=L`, (1), (2), and (5) show that

\[
 g(Y)=Y^{17}+q(Y),\qquad \deg q=m.
\]

Terms with normalized index less than J disappear. The coefficient of
`Y^m` is nonzero: it is the residue of

\[
 -\frac{\binom{20}J}{17}a_J\frac{17}{\pi^{J-3}},
\]

whose three factors are units. For every `1<=k<m`, the selected witness
of `H_k f` has normalized degree `20-k>J` and lies in the zero cluster.
Its ratio to π is integral. Scaling the exact Hasse derivative identity
and reducing therefore proves

\[
 \gcd(g,H_k g)\ne1\quad(1\le k<m). \tag{6}
\]

These are necessary equations involving the actual witnesses. The order
`m` condition is missing, since `H_m g` is a nonzero constant.

Translate a chosen common root of `g,H_(m-1)g` to 0. In characteristic
17 the term `Y^17` contributes only a constant under translation, while
`H_(m-1)q` is linear with nonzero leading coefficient. The translation
therefore sets both the constant and the `Y^(m-1)` coefficient to zero.
A nonzero scaling then sets the leading coefficient of q to -1. Over the
algebraic closure every resulting model has the form

\[
 g(Y)=Y^{17}-Y^m+\sum_{i=1}^{m-2}c_iY^i. \tag{7}
\]

The translated root 0 here need not be the original mean root. The
original mean is another marked root, with no simplicity assertion on its
residue after this blowup. In particular (7) does not force q to be a
translated power and does not contradict known multiplicity bounds.

For each `1<=k<=m-2`, introduce its common-root variable `z_k`. Solve
`H_k q(z_k)=0` in descending k:

\[
 c_k=\binom mk z_k^{m-k}
       -\sum_{i=k+1}^{m-2}\binom ik c_i z_k^{i-k}. \tag{8}
\]

Thus `c_k` is homogeneous of total degree `m-k` in the z variables. The
remaining equations `g(z_k)=0` have the form

\[
 E_k=z_k^{17}+\text{a homogeneous polynomial of degree }m=0. \tag{9}
\]

For any graded monomial order, their leading monomials are
`z_1^17,...,z_(m-2)^17`, which are pairwise coprime. The product criterion
for Gröbner bases then proves that the E_k form a Gröbner basis. The finite
algebra

\[
 B_m=\mathbb F_{17}[z_1,\ldots,z_{m-2}]/(E_1,\ldots,E_{m-2}) \tag{10}
\]

has the exact vector-space dimension `17^(m-2)`, with standard monomial
basis `product(z_k^e_k)`, `0<=e_k<17`. This conclusion retains nilpotents.
For reference, the coprime-leading-monomial argument is elementary: each
S-polynomial is the difference of two multiples of lower tails, and
division by the two original polynomials cancels it to zero.

This is a finite algebra of normalized *leading* models. It is not a
finite list of lifts, and not a proof that these models cannot occur.
Recovering the marked original mean or another marked root requires only
adjoining a root of the monic degree-17 g, hence preserves finiteness.

## 3. Exact residue stratification and the exceptional cases

`residue-strata.json` refines the already audited full residue census by
the two maxima J and L; `stratify_row8.cpp` is its bounded producer. It
uses the same complete `4^13` traversal, divided equation, and two proven
common-root filters, with no new exclusion criterion.

| Last unit degree J | Assignments with J=L | Assignments with L<J |
|---:|---:|---:|
| 7 | 3 | 0 |
| 9 | 19 | 0 |
| 10 | 53 | 0 |
| 11 | 185 | 0 |
| 12 | 728 | 4 |
| 13 | 2,741 | 10 |
| 14 | 10,772 | 27 |
| 15 | 41,196 | 122 |
| 16 | 124,068 | 413 |
| Total | 179,765 | 576 |

Thus (10), for the finite set of degrees `m=20-J`, covers all 179,765
nondegenerate marked assignments. It allows many models that need not be
compatible with the original unit witnesses; such compatibility is an
additional condition, not an assumed consequence of (10).

The 576 assignments with `L<J` remain. Their last unit witness can have
zero normalized coefficient residue. It cannot simply be changed to a
zero-cluster witness. Only the interval (4) has been established for their
first scale; no list of possible first scales is asserted for them.
The full characteristic-zero lifting problem, including these assignments,
has the separate finite formal cover in the following section.

## 4. A finite formal cover for all unrestricted degree-20 lifts

This argument uses the simpler prime 19 and does not depend on row 8 or
the nine-seed classification at 17. It is a standard commutative-algebra
reduction; no novelty claim is made for it.

Start with any nontrivial degree-20 CA polynomial, translate the mean root
to zero, and scale by a root of largest absolute value at 19. Its roots
and all binomial-normalized coefficients are integral, by induction from
the equations `G_j(w_j)=0`. The reduction is

\[
 \bar f=X^{20}+\bar a_{19}X.
\]

The retained unit root implies `a_19` has nonzero residue. Thus the mean
root is exactly simple and is the only root in the zero residue cluster.
Every repeated root is a unit. Select an actual repeated root (a common
root of `f,G_19`) and scale it exactly to 1, preserving integrality.

Define the following finite-type algebra over `A=Z_(19)`:

\[
 T=A[a_2,\ldots,a_{19},w_2,\ldots,w_{18}]/I,
\]

where `a_0=1,a_1=a_20=0,w_19=1`, and I consists of the 36 exact equations

\[
 f(w_j)=G_j(w_j)=0\quad (2\le j\le19). \tag{11}
\]

In its special fibre, `G_19(1)=0` forces `a_19=-1`; therefore

\[
 \bar f=X^{20}-X=X(X-1)^{19}.
\]

Every `w_2,...,w_18` is 0 or 1 at a geometric point. For every choice of
these 17 labels, the equations `G_j(w_j)=0`, in increasing j, determine
`a_2,...,a_18` uniquely in F19. Conversely those assignments satisfy
all special-fibre equations. There are exactly `2^17` marked geometric
points, all F19-rational. No assertion of reducedness is made.

Since the special fibre is a finite-type algebra with finite geometric
support, it is zero-dimensional and Artinian, including all its
nilpotents. For each of these points q, let

\[
 R_q=\widehat{(T\otimes_A\mathbb Z_{19})_q}
\]

be the completion at its maximal ideal. `R_q/19R_q` is finite-dimensional
over F19. Its radical is the maximal ideal, so some power of that maximal
ideal is contained in `19R_q`. Hence the maximal-ideal topology and the
19-adic topology agree. The ring R_q is therefore 19-adically complete.

Choose a vector-space basis of `R_q/19R_q` and lift its elements. Successive
19-adic approximation expresses every element of R_q as a convergent
Z19-linear combination of those finitely many lifts. Consequently

\[
 \boxed{R_q\text{ is a finite }\mathbb Z_{19}\text{-module}.} \tag{12}
\]

This proof does not require R_q to be reduced, flat, or torsion-free.
In particular, if `d_q=dim_F19(R_q/19R_q)`, then

\[
 \dim_{\mathbb Q_{19}} R_q[1/19]\le d_q<\infty. \tag{13}
\]

Every algebraic geometric point of the normalized generic fibre is
integral; the following no-escape argument is useful here. Suppose
`w_19=1` already, and scale by a root η of minimum valuation. The scaled
roots and normalized coefficients are integral and the scaled reduction
is `X^20+abar_19 X` with `abar_19!=0`. Its normalized degree-19 derivative
has reduction `X^19+abar_19`, which does not vanish at 0. The selected
common root `1/η` must therefore be a unit. Thus `ν(η)=0`, and the original
roots and coefficients were already integral.

Any such point is defined over a finite extension of Q19. Its local map
extends to R_q after completing that field: the images of the finitely
many maximal-ideal generators have a strictly positive minimum valuation.
This permits arbitrary finite ramification and uses no unramified-lift
assumption. All algebraic geometric generic points are consequently
covered by the finite product of these completed algebras. A hypothetical
complex solution of the rational incidence equations would also give an
algebraic solution, by the weak Nullstellensatz, so this is an exhaustive
cover for the counterexample-existence problem.

In fact the normalized generic fibre itself is finite: it is of finite
type over Q19 and has finitely many geometric points by (12). A
finite-type algebra over a field with this property is a finite-dimensional
algebra, retaining its nilpotents. These standard zero-dimensional
algebra facts are also recorded in the Stacks Project's
[quasi-finite maps](https://stacks.math.columbia.edu/tag/02MK).

Thus the finite product of the `R_q` is a full formal cover for all
normalized degree-20 CA possibilities, including every remaining row-8
case and all 576 degenerate assignments. A reduced field factor of
`R_q[1/19]` has degree, and hence ramification index, at most d_q. None of
the d_q have been computed here. No reduced field factors, defining
polynomials, or lift list have been computed either.

The global affine algebra T is not claimed finite over A merely from its
finite special fibre. Components such as `19x-1=0` illustrate why that
inference would be invalid. The unit-root normalization and integral
local completions are essential to the coverage statement.

## 5. Replay and remaining work

`check_collective.py` checks the valuation recurrences coefficient by
coefficient on their exact breakpoints, the leading-model formulas and
their homogeneous degrees for every `4<=m<=13`, the standard-monomial
dimensions, all residue-stratum sums, and the complete prime-19 triangular
special-fibre construction. It checks explicit failure controls for the
leading-degree and stratum invariants. Its scope is algebraic replay,
not formal verification of the valuation or completion arguments.

The first-blowup reduction is finite for 179,765 marked assignments, and
the formal cover includes all 180,341 and all other degree-20 branches.
To exclude the row or degree, one must still prove that every relevant
generic formal algebra is zero, or exclude every compatible leading
model and subsequent lift. No such exhaustion is supplied here.
