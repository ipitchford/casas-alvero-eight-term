# A collective finite algebra for the remaining row-9 branch

23 September 2026. This is a complete algebraic reduction of this one
17-adic branch, conditional on the already audited row-9 normalization.
It does **not** exclude the branch. In particular, the final norm below
has not been evaluated, and its nonvanishing is not asserted.

## 1. Exact input, with the triple condition kept separate

Write \(C_j=\binom{20}{j}\), \(u=(u_4,\ldots,u_{16})\), and

\[
\begin{aligned}
f_u(X)={}&X^{20}-1140X^{17}+\sum_{j=4}^{16}C_ju_jX^{20-j}\\
 &+\left(18221-\sum_{j=4}^{16}(19-j)C_ju_j\right)X^2\\
 &+\left(-17082+\sum_{j=4}^{16}(18-j)C_ju_j\right)X.
\end{aligned}\tag{1}
\]

This is the row-9 polynomial after solving \(f(1)=f'(1)=0\).
Its binomial-normalized coefficients satisfy

\[
a_0=1,\quad a_1=a_2=a_{17}=a_{20}=0,\quad a_3=-1,
\quad a_j=u_j\ (4\le j\le16).
\]

The remaining \(a_{18},a_{19}\) are obtained by dividing the two low
coefficients in (1) by 190 and 20. Those denominators are 17-adic units.
Every \(C_j\), \(4\le j\le16\), is divisible by 17. Consequently the
reduction is independent of every integral parameter:

\[
h=X^{20}-X^{17}-3X^2+3X.
\]

Define the exact monic polynomial of degree eighteen

\[
g_u=f_u/(X-1)^2\in\mathbb Z[u][X].
\tag{2}
\]

It has \(g_u(0)=0\). The linear expression

\[
T(u)=-8037+\sum_{j=4}^{16}\binom{19-j}{2}\frac{C_j}{17}u_j
\tag{3}
\]

satisfies the **integer polynomial identity**

\[
g_u(1)=H_2f_u(1)=17T(u).
\tag{4}
\]

Here \(H_k\) is the Hasse derivative of order \(k\). For \(4\le j\le16\),

\[
G_j(X)=\frac{H_{20-j}f_u(X)}{\binom{20}{j}}
=X^j-\binom j3X^{j-3}+\sum_{i=4}^j\binom ji u_iX^{j-i}.
\tag{5}
\]

The division in (5) is an exact coefficient identity over the integers,
even though its scalar denominator is divisible by 17.

Let

\[
R_j(u)=\operatorname{Res}_X(g_u,G_j),\qquad 4\le j\le16.
\tag{6}
\]

These are polynomials over the integers. No expansion of them is needed
for the presentation in `presentation.json`.

## 2. Exact incidence equivalence

Over any characteristic-zero algebraically closed valued field with
integral \(u\), the equations

\[
R_4=\cdots=R_{16}=T=0
\tag{7}
\]

are equivalent to the complete CA common-root conditions for (1).

Indeed, \(T=0\) implies \(g_u(1)=0\), so \(f_u=(X-1)^2g_u\)
and \(g_u\) have the **same set of roots**. Since \(g_u\) and each
\(G_j\) are monic, \(R_j=0\) means exactly that they share a root.
These are the required orders 16 through 4. The remaining orders have
explicit witnesses: orders 19 and 18 use zero, order 17 uses one,
order 3 uses zero, and orders 2 and 1 use one. This uses respectively
\(a_1=a_2=0\), \(G_3(1)=1-1=0\), \(a_{17}=0\), (4), and
\(f'_u(1)=0\). The reverse implication follows from the same identities.

The polynomial is nontrivial because its reduction has both the roots
zero and one. Roots of \(g_u\) are integral because it is monic.

One must keep \(T=0\) in this equivalence. Without it, the exact root
one of \(f_u\) need not be a root of \(g_u\). Instead, \(g_u\) has
a simple root reducing to one. Thus the square system of resultants is
a useful uniform enlargement before the last equation, not an already
complete incidence system.

## 3. Finite flatness without a specialization shortcut

Set

\[
S=\mathbb Z_{17}\langle u_4,\ldots,u_{16}\rangle,
\qquad B=S/(R_4,\ldots,R_{16}).
\tag{8}
\]

Here \(S\) is the 17-adic completion of the polynomial ring over
\(\mathbb Z_{17}\), equivalently its restricted power-series ring.
It is Noetherian, 17-torsion-free, complete and separated. Quotients by
its finitely generated ideals are complete and separated. Thus (8)
denotes the complete quotient, not an assertion about all nonintegral
points of the uncompleted affine scheme.

Modulo 17, \(g_u\) becomes the fixed monic squarefree polynomial

\[
D=h/(X-1)^2=X(X+2)(X-1)Q_5Q_{10},
\tag{9}
\]

where

\[
\begin{aligned}
Q_5&=X^5-3X^4-2X^2-5X-3,\\
Q_{10}&=X^{10}+4X^9-X^8+6X^6+X^4-6X^3+4X^2+7X-8.
\end{aligned}
\]

The already checked factors are irreducible of degrees five and ten.
Only monicity and independence from \(u\) are needed for finite
flatness. Since \(G_j=u_j+\text{a polynomial in }X,u_4,\ldots,u_{j-1}\),
the reduction

\[
\bar R_j=\operatorname{Res}_X(D,\bar G_j)
\]

is monic of degree eighteen in \(u_j\), and contains no \(u_i\) with
\(i>j\). Successive monic division therefore gives the special-fiber
basis

\[
\prod_{j=4}^{16}u_j^{e_j},\qquad 0\le e_j<18.
\tag{10}
\]

In particular, the reductions form a regular sequence: at each stage
the next polynomial is monic in a fresh variable, hence is a
nonzerodivisor even if the coefficient ring has zero divisors.

For clarity, the flatness lifting needed here has a short direct proof.
Suppose \(A\) is a complete separated 17-torsion-free quotient already
constructed, and \(r\in A\) has nonzerodivisor reduction modulo 17.
If \(17x=ry\), reduction gives \(\bar r\bar y=0\), hence
\(y=17z\). Cancellation in \(A\) then gives \(x=rz\). Thus
\(A/(r)\) is 17-torsion-free. Also \(rx=0\) implies successively
\(x\in17^nA\) for every \(n\), so \(r\) is itself a
nonzerodivisor. Apply this argument to \(R_4,\ldots,R_{16}\) in
that order. It proves that \(B\) is 17-torsion-free.

Lift the finitely many monomials (10) to \(B\). Reduction modulo 17
expresses every element in their span, with a remainder in \(17B\).
Repeating this and using completeness expresses every element as a
\(\mathbb Z_{17}\)-linear combination of those same monomials.
Any relation between them has all coefficients divisible by 17 after
reduction; torsion-freeness permits division by 17. Repetition and
separatedness in \(\mathbb Z_{17}\) force every coefficient to vanish.
Consequently

\[
\boxed{B\text{ is finite free of rank }18^{13}
=20\,822\,964\,865\,671\,168\text{ over }\mathbb Z_{17}.}
\tag{11}
\]

The exact \(R_j\) may involve later parameters and higher-degree terms
with coefficients divisible by 17. We have not assumed that they are
triangular or monic in \(u_j\) over the integers. The proof uses their
triangular reductions, completion, and torsion-freeness instead.

## 4. The collective obstruction that remains unevaluated

Multiplication by \(T\) is an endomorphism of the finite free module
\(B\). Let

\[
N=\det(m_T:B\longrightarrow B)\in\mathbb Z_{17}.
\tag{12}
\]

Then the integral characteristic-zero incidence system (7) is empty
if and only if

\[
\boxed{N\ne0\text{ in }\mathbb Q_{17}.}
\tag{13}
\]

To see this, multiplication by \(T\) is invertible on the finite
\(\mathbb Q_{17}\)-algebra \(B[1/17]\) exactly when \(N\ne0\).
This is equivalent to \(T\) being a unit and to
\(B[1/17]/(T)=0\). Otherwise this nonzero finite algebra has a
closed point over a finite extension of \(\mathbb Q_{17}\).
Every coordinate at that point is integral over \(\mathbb Z_{17}\)
because \(B\) is finite over it. Conversely any integral valued-field
solution evaluates restricted power series and gives such a point.
This proves the equivalence without inferring characteristic-zero
emptiness from an affine special fiber.

There is no requirement that \(N\) be a unit in \(\mathbb Z_{17}\).
Known solutions of the first-residue equations already prevent that
simple criterion. A nonzero \(N\) could be highly divisible by 17.
Nilpotents and collisions of different marked root assignments are
retained throughout; no radical or squarefree replacement of the
resultant algebra is used in (12).

Neither the enormous matrix \(m_T\) nor its determinant was built.
No complexity guarantee for evaluating (12) follows from its finite
description. Arbitrarily increasing finite precision would detect a
nonzero \(N\) eventually, but an all-zero finite prefix does not prove
\(N=0\). This is an exact target, not a completed decision algorithm
with an established practical or a priori termination bound.

## 5. Canonical supports give smaller complete algebras

The previously checked support inventory contains 240 eligible supports
\(S\) satisfying the row-9 requirements

\[
\{3,18,19\}\subset S,\qquad S\cap\{2,17\}=\varnothing.
\]

For one such support, let \(J=S\cap\{4,\ldots,16\}\), set
\(u_i=0\) for \(i\notin J\), and use only the equations

\[
R_j^*=\operatorname{Res}_X(g_u/X,G_j)=0\quad(j\in J),
\qquad T=0.
\tag{14}
\]

This loses no genuine candidate with that exact support. For an active
coefficient \(u_j\ne0\), a common witness cannot be zero. It cannot
even reduce to zero: the mean residue class is simple and contains only
the exact root zero. For an inactive coefficient, zero is an available
witness. The resultant identity is exact:

\[
R_j=G_j(0)\operatorname{Res}_X(g_u/X,G_j)=u_jR_j^*.
\]

No condition \(\bar u_j\ne0\) is imposed. An exact nonzero
coefficient may have zero residue, and those cases remain in (14).
The closed systems may also include zero values of nominally active
coefficients. After imposing \(T=0\), any such point still satisfies
all CA common-root conditions. It is simply represented redundantly.

The constant term of \(g_u/X\) reduces to \(h'(0)=3\), so deleting
zero removes exactly one simple residue root. The same proof as above
now gives a finite free completed algebra of rank \(17^{|J|}\).
For the eligible supports the size histogram is

| \(m\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Supports | 1 | 6 | 21 | 51 | 71 | 45 | 27 | 11 | 6 | 1 |

The sum of these ranks is **813,975,725,115,600**. This remains far too
large to present as a practical explicit matrix computation. The 240
lists and their source fingerprint are included in `presentation.json`;
the support criteria themselves remain a dependency on the earlier
audited inventory. Taking the product of their generic norms of \(T\)
would give another equivalent exclusion target. None was evaluated.

## 6. A low-degree Frobenius description of the full residue domain

The identity

\[
(X-1)D=X^{17}(X^2+X+1)-3X
\]

shows that every residue root \(r\) obeys

\[
r^{17}=\frac{3r}{r^2+r+1}.
\tag{15}
\]

The denominator is nonzero on the root domain: otherwise (15) before
division would force \(r=0\), where that denominator is one. For
\(r\ne1\), the invertible change of coordinate

\[
y=7\frac{r+1}{r-1},\qquad r=\frac{y+7}{y-7}
\]

conjugates (15) to

\[
y^{17}=y^2-5.
\tag{16}
\]

The polynomial \(Y^{17}-Y^2+5\) is separable because its derivative
is \(-2Y\) and its constant term is nonzero. It does not vanish at
seven, so the inverse map has no exceptional finite point. Thus the
eighteen residue roots consist of the point \(r=1\), represented by
infinity, and the seventeen roots of (16). This gives a quadratic
Frobenius action on the domain. It has not yet produced a reduction in
the number of combined coefficient states or an obstruction at the
next 17-adic digit.

## 7. Compact presentation and verification boundary

`presentation.json` stores affine integer coefficient vectors for
\(f,g,g/X,G_4,\ldots,G_{16},T\). For a monic polynomial
\(q=X^d+\sum_{k<d}q_kX^k\), its companion matrix is the matrix of
multiplication by \(X\) on \(1,X,\ldots,X^{d-1}\): it has subdiagonal
ones and final column \((-q_0,\ldots,-q_{d-1})^t\). Therefore

\[
\operatorname{Res}_X(q,G_j)=\det G_j(C_q).
\]

Only matrices of size eighteen, or seventeen for (14), occur in this
determinant-circuit presentation. It does not expand the resultants or
construct the much larger matrix (12).

The standalone `check_presentation.py` imports no producer code. It
independently solves the two low-coefficient equations in each of the
fourteen affine directions, checks every normalized Hasse identity by
direct differentiation, verifies division and (4) coefficientwise,
checks squarefreeness and factorization of the residue domain, verifies
the Frobenius conjugacy by polynomial remainders, and rechecks the
support-list fingerprint and rank arithmetic. Normal and optimized
Python runs have the same output. The finite-flat argument is a
mathematical proof above, not a machine-checked formal proof. The final
generic norms are unevaluated, so this branch and the full conjecture
remain unresolved by this subtask.
