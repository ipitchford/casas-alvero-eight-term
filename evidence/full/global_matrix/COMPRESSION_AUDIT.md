# Derivative compression flags: exact representation and two structural obstructions

Status: the derivative representation is justified at every step. The lemmas
below rule out specific matrix shortcuts; they do not prove the all-degree
Casas–Alvero conjecture.

## 1. An exact nested orthogonal compression flag exists

Let `f(z)=prod_(i=1)^n(z-alpha_i)` and `D=diag(alpha_1,...,alpha_n)`.
For a matrix `A` of size `m`, a unit vector `v` is a trace vector when

\[
 v^*A^k v=\frac1m\operatorname{tr}(A^k)\quad(0\le k<m).
\]

Pereira proves that every complex matrix has a trace vector, and that its
orthogonal-complement compression has characteristic polynomial `p_A'/m`.
See [*Differentiators and the geometry of polynomials* (2003)](https://doi.org/10.1016/S0022-247X(03)00465-7);
the existence statement and equivalence are also explicitly restated in
[Pereira (2005), Definitions 3–4 and Proposition 5](https://www.numdam.org/item/CRMATH_2005__341_11_651_0.pdf).
This theorem applies to nonnormal matrices as well.

The characteristic-polynomial identity itself follows from the cofactor
resolvent formula

\[
 p_{A|v^\perp}(z)=p_A(z)\,v^*(zI-A)^{-1}v.
\]

The trace-vector moments and Cayley–Hamilton identify the last factor with
`tr((zI-A)^(-1))/m=p_A'(z)/(m p_A(z))`.

Apply the existence theorem repeatedly, including after normality has been
lost. It gives nested subspaces

\[
 S_1\subset S_2\subset\cdots\subset S_n=\mathbb C^n,
 \qquad \dim S_j=j,
\]

whose compressions have characteristic polynomials

\[
 G_j(z)=\frac{f^{(n-j)}(z)}{n!/j!}.
\tag{1}
\]

Nested orthogonal compression is associative, so each matrix is also a direct
compression of the original `D`. Choose an orthonormal basis adapted to the
flag. The resulting `A=U^*DU` is normal and its leading principal blocks
`A_j` satisfy (1). If `f` is centered, all `tr(A_j)=0`, hence **every diagonal
entry of `A` is zero**.

Consequently CA is exactly the condition

\[
 \operatorname{spec}(A_j)\cap\operatorname{spec}(A_n)\ne\varnothing
 \quad(1\le j<n)
\tag{2}
\]

for this derivative flag. This is an exact reformulation. It supplies no
normality assumption for the blocks `A_j`.

## 2. When the first compression remains normal

For the original diagonal `D`, take the flat trace vector
`v=(1,...,1)/sqrt(n)`, let `P=I-vv*`, and let `B=P D|v^perp`.

**Lemma.** `B` is normal if and only if all the roots of `f` lie on an affine
line in the complex plane (including the scalar case).

**Proof.** Put `mu=tr(D)/n` and write `D` in the orthogonal decomposition
`v^perp plus Cv` as

\[
 D=\begin{pmatrix}B&b\\c^*&\mu\end{pmatrix},\qquad
 b=(D-\mu I)v,\quad c=(D^*-\bar\mu I)v.
\]

Normality of `D` gives

\[
 BB^*-B^*B=cc^*-bb^*.
\]

Thus `B` is normal precisely when `cc*=bb*`. If `b=0`, all roots equal `mu`.
Otherwise this is equivalent to `c=eta b` with `|eta|=1`, or

\[
 \overline{\alpha_i-\mu}=\eta(\alpha_i-\mu)\quad\hbox{for every }i.
\]

Those points lie on one real line through the origin. The converse follows
from the same identities. This proof does not infer anything about the
original roots from normality of an unrelated later block.

In particular, replacing the complex derivative blocks by normal blocks
changes the problem. Even the collinear case still requires the exact
derivative/incidence equations; interlacing alone is not a full proof.

## 3. No root-independent universal quadratic compression for n>=5

The first compression can use a fixed flat vector. Higher derivatives cannot
in general use one fixed flag independent of the roots.

**Theorem.** For `n>=5`, no fixed `n by 2` isometry `V` can satisfy

\[
 \det(zI_2-V^*\operatorname{diag}(\alpha_1,\ldots,\alpha_n)V)
 =\frac{f^{(n-2)}(z)}{n!/2!}
\tag{3}
\]

for every choice of the complex numbers `alpha_i`.

**Proof.** Cauchy–Binet gives

\[
 \det(zI_2-V^*DV)
 =\sum_{i<j}|\det V_{\{i,j\}}|^2(z-\alpha_i)(z-\alpha_j).
\]

Comparison of each constant-term monomial `alpha_i alpha_j` with the
normalized derivative forces

\[
 |\det V_{\{i,j\}}|^2=\frac1{\binom n2}.
\]

Let `v_i` be row `i` of `V`. Since `V*V=I_2`, summing these minor squares
over `j!=i` gives `||v_i||^2=2/n`. The determinant of each two-row Gram
matrix then gives

\[
 |\langle v_i,v_j\rangle|^2
 =\frac4{n^2}-\frac{2}{n(n-1)}.
\]

Normalize each row to a unit vector `u_i`. Their rank-one Hermitian
projectors `E_i=u_i u_i*` have Hilbert–Schmidt Gram matrix with diagonal 1
and every off-diagonal entry

\[
 t=\frac{n-2}{2(n-1)}<1.
\]

That Gram matrix is `(1-t)I+tJ`, positive definite, so the `n` projectors
are real-linearly independent. But Hermitian `2 by 2` matrices form a
real vector space of dimension 4. Hence `n<=4`, a contradiction.

This is an obstruction to a **universal root-independent compression**, not
to the root-dependent flag established in Section 1. It rules out using a
fixed Fourier flag to represent all derivatives in arbitrary degree.

## 4. Shared spectrum does not force inherited eigenvectors

There is an exact all-degree derivative flag which demonstrates this failure
at arbitrarily many consecutive levels. Let `n>=3`, and start with the normal
operator `0 direct-sum C_(n-1)`, where `C_(n-1)` cyclically permutes an
orthonormal basis `u_1,...,u_(n-1)` and annihilates a separate vector `e_0`.
Its characteristic polynomial is

\[
 f(z)=z(z^{n-1}-1)=z^n-z.
\]

Put

\[
 b=1/\sqrt n,\quad a=\sqrt{(n-1)/n},\quad
 w=ae_0+bu_{n-1},\quad v=-be_0+au_{n-1},
\]

and use the ordered orthonormal basis
`u_1,...,u_(n-2),w,v`. The leading block of order `n-1` is a weighted
cycle whose product of edge weights is `b^2=1/n`. Every smaller leading
block is a nilpotent shift. Therefore

\[
 p_{A_n}(z)=z^n-z,\qquad
 p_{A_{n-1}}(z)=z^{n-1}-1/n,\qquad
 p_{A_j}(z)=z^j\quad(1\le j\le n-2).
\tag{4}
\]

These are exactly all the normalized derivatives of `f`, including the
correct derivative relation between every adjacent pair. No arbitrary
compression has been substituted for a derivative.

The original eigenvalue 0 is simple, and its eigenvector is
`e_0=aw-bv`. It is orthogonal to every `S_j` for `j<=n-2`. Nevertheless all
those compressed matrices have 0 as their only eigenvalue. Thus the shared
original eigenvalue is **not inherited through an original eigenvector**.
For `j>=2`, its algebraic multiplicity in the compression is `j`, despite
being simple in the original normal matrix.

The single remaining block `A_(n-1)` has no eigenvalue in the original
spectrum: its eigenvalues satisfy `z^(n-1)=1/n`, whereas the original
nonzero eigenvalues satisfy `z^(n-1)=1`. Thus this is a derivative-flag
countermodel satisfying all but one condition in (2), not a CA polynomial.

For `n=4`, the matrix is particularly explicit:

\[
 A=\begin{pmatrix}
 0&0&1/2&\sqrt3/2\\
 1&0&0&0\\
 0&1/2&0&0\\
 0&\sqrt3/2&0&0
 \end{pmatrix}.
\]

It is normal, while its leading `3 by 3` and `2 by 2` blocks are not.
Their characteristic polynomials are `z^3-1/4` and `z^2`; the leading
`1 by 1` block is zero. The exact kernel vector of `A` is
`(0,0,sqrt3/2,-1/2)`, orthogonal to the first two coordinate subspaces.

## 5. What remains unproved

Every polynomial admits the exact normal-matrix derivative flag. Enforcing
all the spectral incidences (2) is therefore equivalent to CA itself.
The representation is sound; the proposed automatic invariant-subspace
inheritance is false, and a fixed universal flag is impossible in degree
at least five. The first-compression normality lemma additionally identifies
precisely when Hermitian-type reasoning could apply.

A full matrix proof would need a new argument coupling **all** incidences
in (2) with the trace-vector equations. Neither normality of the original
matrix nor isolated shared eigenvalues forces that coupling. No such
all-incidence obstruction is established here.

## Exact replay

`verify_compressions.py` checks the displayed `4 by 4` matrix in the exact
quadratic field `Q(sqrt(3))`: normality, nonnormality of the intermediate
blocks, every characteristic polynomial, every trace-vector moment, and the
kernel vector. It also checks the shared-spectrum gcds over the rationals.
The arbitrary-degree statements above are proved algebraically.
