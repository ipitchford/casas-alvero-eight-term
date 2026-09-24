# A valid all-place height bound, and why it does not close a product contradiction

Scope: this establishes a uniform necessary height inequality for a CA
polynomial and tests the proposed product-formula mechanism on exact algebraic
partial-incidence models. It does not prove the full conjecture.

## 1. Keep one number field and one global witness

Let `K` contain all roots of a centered monic algebraic CA polynomial

\[
 f(X)=\sum_{i=0}^n\binom ni a_iX^{n-i},\qquad a_0=1,
 \quad a_1=a_n=0.
\]

Use absolute values extending the usual real/complex modulus and the usual
`p`-adic absolute value, with weights `w_v=[K_v:Q_v]/[K:Q]`. Thus
`sum_v w_v log|x|_v=0` for nonzero `x in K`, and the archimedean weights sum
to 1. In particular, complex moduli are not squared separately from their
weight. Apply each embedding to both the coefficients and the chosen roots.

Write the roots with multiplicity as `alpha_1,...,alpha_n`, and put

\[
 R_v=\max_i|\alpha_i|_v,\qquad
 h_R=\sum_v w_v\log R_v,\qquad H_R=e^{h_R}.
\]

This is the projective height of the root vector. It is invariant under one
global scaling of all roots, by the product formula. The zeros in the root
vector cause no problem because the polynomial is nontrivial.

Let `d>=2` be the first index with `a_d!=0`. Choose **one fixed algebraic
root** `r` which witnesses `G_d=X^d+a_d`; then `a_d=-r^d`.
Let `m_0,m_r` denote the multiplicities of 0 and `r`, and set

\[
 B=d\binom nd-m_r,\qquad M=n-m_0-m_r.
\]

Newton's identity gives the exact equality

\[
 B r^d=\sum_{\alpha_i\ne0,r}\alpha_i^d.
\tag{1}
\]

The sum counts multiplicities. If `M=0`, (1) is already impossible, because
`B>0` and `r!=0`. Assume `M>0` below.

## 2. What the all-place inequality actually says

At an archimedean place, (1) yields

\[
 \frac{R_v}{|r|_v}\ge\left(\frac BM\right)^{1/d}>1.
\tag{2}
\]

At a nonarchimedean place it yields

\[
 \frac{R_v}{|r|_v}\ge |B|_v^{1/d}.
\]

But `B` is an integer, so `|B|_v<=1`. The stronger lower bound there is the
trivial, exact common-root bound `R_v/|r|_v>=1`. Hence multiplying the valid
inequalities gives

\[
 \boxed{\quad H_R\ge\left(\frac BM\right)^{1/d},\qquad
 h_R\ge\frac1d\log\frac BM>0.\quad}
\tag{3}
\]

This is a genuine all-degree necessary condition with the closed incidence
used in both (1) and `R_v>=|r|_v`. It is a **height lower bound**.

One can remove the support and multiplicity parameters to obtain, for `n>=3`,

\[
 H_R\ge
 \left(\frac{n(n-1)-1}{n-2}\right)^{1/(n-1)}>1.
\tag{3a}
\]

Indeed, `d binom(n,d)=n binom(n-1,d-1)>=n(n-1)`. The ratio `B/M` is
minimized, for a fixed value of that numerator before subtracting `m_r`,
by `m_0=m_r=1`. Finally `d<=n-1`, and the base of the power exceeds 1.
No upper bound of the opposite sign follows.

The product formula cancels `prod_v |r|_v^{w_v}`. It does not set
`prod_v R_v^{w_v}` equal to 1. The maximizing root in `R_v` may change with
the place and the embedding. Its local maxima form a projective height,
not the absolute values of one fixed field element.

Equivalently, the product of local contraction ratios is

\[
 \prod_v\left(\frac{|r|_v}{R_v}\right)^{w_v}=H_R^{-1}<1.
\]

That is fully compatible with the product formula. Normalizing by a different
largest root at every place does not create a single global scalar to which
the product formula can be applied.

## 3. All finite-place normalized-coefficient integrality still gives a gap, not a loop

The common-root equations imply, at every nonarchimedean place,

\[
 |a_j|_v\le R_v^j.
\tag{4}
\]

Indeed, induct on `j`, using a common root `beta_j` of `G_j` and `f`:

\[
 a_j=-\sum_{i<j}\binom ji a_i\beta_j^{j-i}.
\]

Every summand has absolute value at most `R_v^j`. No choice of an unramified
normalization is needed.

Define the weighted coefficient radius and height

\[
 Q_v=\max_{1\le i\le n}|a_i|_v^{1/i},\qquad
 H_A=\prod_v Q_v^{w_v}.
\]

At finite places, in fact `Q_v=R_v`. To see the reverse inequality, the
nonarchimedean root-radius formula for the monic polynomial gives

\[
 R_v=\max_i\left|\binom ni a_i\right|_v^{1/i}\le Q_v;
\]

combine this with (4).

At archimedean places, elementary symmetric functions and the `m_0` zero
roots give

\[
 |a_i|_v\le
 \frac{\binom{n-m_0}{i}}{\binom ni}R_v^i.
\]

Since `a_1=0`, only `i>=2` matter. The successive factors in the binomial
ratio decrease, so

\[
 Q_v\le\kappa R_v,\qquad
 \kappa=\sqrt{\frac{(n-m_0)(n-m_0-1)}{n(n-1)}}<1.
\]

Thus a CA polynomial satisfies the strict height comparison

\[
 H_A\le\kappa H_R.
\tag{5}
\]

It is not a contradiction: these are heights of different objects. Dividing
all roots by the common witness `r` leaves `H_R` unchanged. The corresponding
weighted scaling of the coefficients also leaves `H_A` unchanged. No new
CA polynomial of smaller projective height has been produced.
In that normalization `a_d=-1`, so every `Q_v>=1` and `H_A>=1`;
the strict comparison simply requires the root height to be larger.

For completeness, root-difference height makes the normalization issue even
more explicit. Put `D_v=max_(i,j)|alpha_i-alpha_j|_v`. Its product is exactly
invariant under translation and global scaling. Since 0 is a root,
`D_v=R_v` at finite places and `R_v<=D_v<=2R_v` at infinite places. Moving
the origin to another root therefore cannot supply a strict descent of this
translation-invariant height.

## 4. Exact near-CA model satisfying all these finite-place conditions

Consider

\[
 F(X)=X^6-15X^4+20X^3-6X
     =X(X-1)^2(X^3+2X^2-12X-6).
\tag{6}
\]

Its normalized coefficients are

\[
 (a_0,\ldots,a_6)=(1,0,-1,1,0,-1,0).
\]

They are rational integers, and every nonzero one has modulus 1 at every
archimedean place. Its mean root 0 is simple; 1 is exactly double. The
normalized derivatives are

\[
 G_1=X,\quad G_2=X^2-1,\quad G_3=X^3-3X+1,
\]
\[
 G_4=X^4-6X^2+4X,\quad
 G_5=X^5-10X^3+10X^2-1.
\]

They share roots with `F` at 0, 1, no root, 0, and 1, respectively. In
particular, `gcd(F,G_3)=1`, checked exactly in the replay. Hence (6) meets
four of the five CA conditions, including the **first-nonzero-coefficient
witness** and the ordinary-derivative condition. It is not a CA polynomial.

Let `K` be its splitting field. At every finite place, all roots are integral
because `F` is monic integral, and the exact root 1 gives `R_v=1`. Also
`Q_v=1` everywhere. All of the local normalized-coefficient integrality
conditions therefore hold without any further scaling.

The cubic factor has roots in `(-5,-4)`, `(-1,0)`, and `(2,3)`: evaluate it
at the six integer endpoints. Thus its root radius `R` lies in `(4,5)`.
Every embedding of the splitting field permutes the roots of this rational
polynomial, so `R_v=R` at all archimedean places. Consequently

\[
 H_A=1,\qquad H_R=R>4.
\]

The true first witness is `r=1`, with `d=2,m_0=1,m_r=2`. Bound (3) is
`H_R>=sqrt(28/3)`, which is satisfied. The local ratio `|r|_v/R_v` equals
1 at every finite place and is strictly below 1 at every infinite place.
Its product is `1/R`, exactly as projective height requires.

Thus replacing the final missing incidence by all finite-place coefficient
integrality, even while retaining all the other incidences, does not make
the product-formula argument valid. A purported proof using only those
weaker facts would incorrectly exclude this explicit algebraic polynomial.

## 5. No height upper bound follows from the same data

There is an unbounded-height integer family retaining the first witness,
the ordinary-derivative witness, and all the finite-place conditions:

\[
 F_t(X)=X(X-1)^2(X^3+2X^2-12X-6+60t),\qquad t\in\mathbb Z.
\tag{7}
\]

Its normalized coefficients are

\[
 (1,0,-1,1+3t,-8t,-1+10t,0).
\]

The root 0 is simple and the root 1 is exactly double for every integer `t`.
It has exact witnesses for `G_1` at 0, `G_2` at 1, and `G_5` at 1; the two
remaining conditions are not asserted. Every finite root radius is again 1.
The three roots of the cubic factor have product `6-60t`, so

\[
 H_R(F_t)=R_t\ge |60t-6|^{1/3}\longrightarrow\infty.
\]

Therefore neither an upper height bound nor a contradiction follows from
the global first-witness identity, centering, a simple mean root, a repeated
nonzero root, and all the finite normalized-coefficient inequalities. Full
CA incidence would need to contribute an additional ingredient not present
in this family.

## Conclusion of this bounded attempt

The product-formula calculation is valid and produces (3). The finite-place
coefficient equalities produce (5). They do not close into a globally
decreasing height: normalization preserves the relevant projective heights,
and the explicit algebraic model (6) realizes the purported contradictory
pattern of local inequalities. Family (7) rules out an upper bound from the
same weakened hypotheses. No all-degree proof has been obtained.

`verify_height_models.py` replays the coefficient identities, common-root
claims, simple/double multiplicities, exact missing gcd, and interval signs
using rational arithmetic. The statements about all finite places follow
from monicity and the exact root 1, not from sampling primes.
