# Goncharoff reconstruction: a valid witness bound and a failed contraction

Status: exact partial results and countermodels to weakened contraction
principles. No claim that the characteristic-zero CA conjecture is solved.

## 1. The exact integral system

For a centered monic polynomial

\[
 f(X)=\sum_{i=0}^n\binom ni a_iX^{n-i},\qquad a_0=1,\ a_1=0,
\]

write

\[
 G_j(X)=\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]

Then `G_j'=j G_(j-1)`. Selecting a root `r_j` of `G_j` gives the exact
Goncharoff recursion

\[
 G_j(z)=j\int_{r_j}^{z}G_{j-1}(t)\,dt.
\tag{1}
\]

The polynomial integrals are path independent. The essential additional CA
condition is `f(r_j)=0` for every `j<n`. Replacing it by membership in the
convex hull of the roots loses decisive information, even when every other
incidence remains exact.

## 2. A centered, real-rooted countermodel missing just one incidence

For every integer `n>=4`, let

\[
 f_n(X)=X(X-1)^{n-2}(X+n-2).
\tag{2}
\]

Its roots are 0, simple; 1, of multiplicity `n-2`; and `-(n-2)`, simple.
Their sum is zero. Thus the mean is the exact simple root 0, and there is a
nonzero repeated root. All roots are real.

It shares the root 1 with Hasse derivatives of orders `1,...,n-3`, and the
root 0 with the derivative of order `n-1`. Its remaining normalized
derivative is

\[
 G_2(X)=X^2-\frac{n-2}{n}.
\]

Neither of its roots is a root of `f_n`. Therefore (2) satisfies **exactly
`n-2` of the `n-1` CA conditions**, failing only order `n-2`.

The complete normalized chain has the closed form

\[
 G_1(X)=X,\qquad
 G_j(X)=(X-1)^{j-2}
 \left(X^2+(j-2)X-\frac{(j-1)(n-j)}n\right)\quad(2\le j\le n).
\tag{3}
\]

One can verify (3) directly by `G_j'=jG_(j-1)` and `G_n=f_n`.
Choose the ordered, real integration nodes

\[
 r_1=0,\qquad r_2=\sqrt{(n-2)/n},\qquad r_3=\cdots=r_n=1.
\tag{4}
\]

They all lie in `[0,1]`, hence in the convex hull `[-(n-2),1]` of the final
roots. All except `r_2` are exact roots of the final polynomial. Nevertheless

\[
 \max_{f_n(\alpha)=0}|\alpha|=n-2,
 \qquad \max_j|r_j|=1.
\tag{5}
\]

Thus these hypotheses give neither a root-radius contraction nor even a
degree-independent root-radius bound by a constant times the maximum node
radius. At degree 20 the expansion factor is 18.

This countermodel retains centering, a simple mean root, another repeated
root, real-rootedness, ordered real nodes, convex-hull membership, and every
CA incidence except one. It does not refute an estimate which uses **all**
exact incidences in an essential way. It identifies which relaxation is
invalid. Choosing a largest-modulus final root as `r_n` changes the maximum
node radius and removes this particular comparison; it does not prove a
strict contraction or remove the missing `G_2` incidence.

## 3. A correct bound using exact closed incidence

Suppose now that `f` is a nontrivial centered CA polynomial. Its mean root is
0, so `a_n=0`. Let `d` be the least index for which `a_d!=0`. Then
`2<=d<=n-1`, and `G_d=X^d+a_d`. Select its common root `r` with `f`.
It is nonzero and satisfies `a_d=-r^d`.

Let `m_0` and `m_r` be the multiplicities of 0 and `r` in `f`, and let
`R=max |alpha|` over all roots of `f`. Newton's identity, using the zero
coefficients at indices `1,...,d-1`, is

\[
 \sum_\alpha\alpha^d=d\binom nd r^d.
\]

Crucially, `r` is itself a root of `f`, not just a node in its convex hull.
Remove its `m_r` copies and the zero roots from this identity. The triangle
inequality gives the uniform necessary condition

\[
 \boxed{\quad
 \left(d\binom nd-m_r\right)|r|^d
 \le (n-m_0-m_r)R^d.
 \quad}
\tag{6}
\]

The coefficient on the left is positive and exceeds the coefficient on the
right. Thus `0<|r|<R`. In particular, a centered CA polynomial cannot have
all its nonzero roots on a single circle centered at the mean. If equality
holds in (6), every remaining nonzero root has modulus `R`, and their `d`th
powers have the same argument as `r^d`.

This is an exact linked-coefficient consequence; no novelty claim is made.
It is stronger than treating the node as an arbitrary point in the hull.

It does not yield an iterative contraction. Centering is essential to the
first-index argument. After translating by `r`, the first coefficient is
nonzero at index 1 and the normalized linear derivative selects the original
mean 0. Hence the purported next step can simply return to a previously used
root. The radii are now measured from different centers; no strictly
decreasing global quantity has been proved.

## 4. The normalization G_2=X^2-1, G_3=(X-1)^2(X+2)

This forces `a_2=-1,a_3=2`, so Newton's identities give

\[
 \sum\alpha=0,\quad
 \sum\alpha^2=n(n-1),\quad
 \sum\alpha^3=-n(n-1)(n-2).
\]

If 0 and 1 are exact simple roots, remove them. The remaining `n-2` roots
satisfy

\[
 \sum\alpha^2=n(n-1)-1,\qquad
 \sum\alpha^3=-n(n-1)(n-2)-1.
\]

Consequently,

\[
 R^2\ge\frac{n(n-1)-1}{n-2},\qquad
 R^3\ge\frac{n(n-1)(n-2)+1}{n-2}.
\tag{7}
\]

For degree 20 these are `R^2>=379/18` and `R^3>=6841/18`.
These are lower bounds, not a contradiction: there is no corresponding
upper bound on the remaining complex roots from the normalization alone.

Indeed the exact polynomial

\[
 F(X)=X(X-1)(X^3+X^2-9X+11)
     =X^5-10X^3+20X^2-11X
\]

has simple roots 0 and 1 and exactly these `G_2,G_3`. It satisfies the CA
conditions of derivative orders 2, 3, and 4, but is squarefree and therefore
fails the order-1 condition. Its cubic factor has discriminant `-2096`, so
the final polynomial has a nonreal conjugate pair. Real-rootedness of `G_3`
does not propagate to the original polynomial.

A correct geometric restriction is available: if all roots of the original
polynomial were collinear, the double root 1 of `G_3` would force multiplicity
at least `n-1` at 1 in `f`. For a real-rooted polynomial, every derivative
root which is not inherited from a multiple original root is simple: away
from the roots, the derivative of `P'/P=sum m_i/(x-r_i)` is strictly negative.
Iterate this observation backward `n-3` times; rotation and translation give
the collinear case. Hence the stated simple-root normalization requires a
noncollinear configuration. It does not exclude a general complex CA
configuration.

## 5. Exact limitation of this route

The integral representation (1) is correct, and (6) is a genuine uniform
restriction using the closed incidence. The missing conclusion would be a
single global quantity that strictly decreases while applying these
identities to new roots, or an upper radius bound contradicting (6)/(7).
Neither follows from the integral representation, convexity, or critical-point
interlacing. Family (2) explicitly falsifies the proposed norm relaxation;
the translated first-coefficient calculation explains why the available
strict interior bound does not close a descent.

For primary-source context, [Draisma–de Jong, *On the Casas–Alvero conjecture*](https://math.univ-angers.fr/~tanlei/papers/english-reading/Casa-conj-pages29-33.pdf)
explicitly distinguish real-root interlacing from the additional equations
needed beyond degree four. The deductions and countermodels here are proved
directly; that source is not used as a substitute for their proofs.

## Replay boundary

`verify_integral_countermodels.py` builds (2) from its factors and checks its
normalized derivatives independently of (3), for degrees 4 through 40. It
checks the integral differential recurrence, all claimed incidences and the
single failed condition. It separately verifies the degree-five example and
its squarefreeness by exact rational polynomial arithmetic. The symbolic
proofs above establish the arbitrary-degree statements.
