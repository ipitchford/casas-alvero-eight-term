# Marked splitting and the limits of the row-9 Frobenius relation

24 September 2026. Bounded algebraic investigation for the argument-review
phase. No new support exclusion, row-9 exclusion, or novelty claim is made.
The main positive result is an exact filtration of the existing resultant
algebra. It preserves marked multiplicities and makes its norm a product
of scalar obstruction values in a fixed unramified field.

## 1. Input and notation

The input is the audited normalization and the explicit integer
polynomials in
[FINITE_FLAT_REDUCTION.md](../evidence/full/collective17/elimination/FINITE_FLAT_REDUCTION.md).
In particular,
\[
f_u=(X-1)^2g_u,\qquad
g_u(1)=17T(u),
\]
where \(g_u\) is monic of degree eighteen and
\[
T=-8037+\sum_{j=4}^{16}
\binom{19-j}{2}\frac{\binom{20}{j}}{17}u_j.
\]
The normalized derivatives are
\[
G_j(X)=X^j-\binom j3 X^{j-3}
+\sum_{i=4}^j\binom ji u_iX^{j-i},
\qquad 4\leq j\leq16.
\]
Set \(R_j=\operatorname{Res}_X(g_u,G_j)\). The complete row-9 incidence
problem is \(R_4=\cdots=R_{16}=T=0\) on integral parameters.
The resultant equations without \(T=0\) are only a square enlargement.

The fixed reduction \(D=\bar g_u\) is squarefree and has factor degrees
\(1,1,1,5,10\). The simple roots are \(0,1,-2\), five roots of \(Q_5\),
and ten roots of \(Q_{10}\), with \(Q_5,Q_{10}\) as in the input.
Consequently all eighteen residue roots lie in \(\mathbb F_{17^{10}}\).
Let \(K/\mathbb Q_{17}\) be the unramified extension of degree ten,
\(\mathcal O\) its integer ring, and \(\pi=17\).

The checked Frobenius identity is
\[
r^{17}=\frac{3r}{r^2+r+1}.
\]
For \(r\ne1\), putting \(y=7(r+1)/(r-1)\) gives
\[
y^{17}=y^2-5.
\]
These are residue-field identities. No exact characteristic-zero
quadratic Frobenius equation is assumed.

## 2. A marked splitting lemma

**Proposition 1.** Let \(\mathcal O\) be a complete discrete valuation
ring with uniformizer \(\pi\), and put
\(S=\mathcal O\langle u_1,\ldots,u_m\rangle\), the restricted power-series
ring. For each \(j\) choose \(d_j\geq1\) elements
\(L_{j,1},\ldots,L_{j,d_j}\) such that
\[
\overline{L}_{j,r}
=u_j+A_{j,r}(u_1,\ldots,u_{j-1}).
\tag{1}
\]
Let \(F_j=\prod_{r=1}^{d_j}L_{j,r}\) and
\(B=S/(F_1,\ldots,F_m)\). Then:

1. \(B\) is finite free over \(\mathcal O\), of rank \(\prod_jd_j\).
2. For each marked tuple \(\mathbf r=(r_1,\ldots,r_m)\),
   \(S/(L_{1,r_1},\ldots,L_{m,r_m})\) is a rank-one unital
   \(\mathcal O\)-algebra and is therefore \(\mathcal O\). Its coordinates
   give a point \(u^{\mathbf r}\in\mathcal O^m\).
3. \(B\) has an \(S\)-module filtration with exactly these rank-one
   quotient modules, one for each marked tuple, including repetitions.
4. For every \(H\in S\),
\[
\det_{\mathcal O}(m_H\mid B)
=\prod_{\mathbf r}H(u^{\mathbf r}).
\tag{2}
\]

Distinct marked tuples need not give distinct coordinate points. The
proposition neither asserts that \(B\) is étale nor replaces \(B\) by
its radical.

**Proof.** Consider any system obtained by replacing any of the \(F_j\)
by a nonempty product of a subset of its factors. Its reduced equations,
ordered by increasing \(j\), are monic in successively fresh variables.
They therefore form a regular sequence, and successive monic division
gives a basis whose size is the product of the remaining factor counts.

The elementary lifting argument is as follows. If \(A\) is complete,
separated and \(\pi\)-torsion-free and \(\bar h\) is a nonzerodivisor
in \(A/\pi A\), then \(A/(h)\) is \(\pi\)-torsion-free: an equation
\(\pi x=hy\) first gives \(y=\pi z\), and cancellation gives \(x=hz\).
Also \(hx=0\) successively forces \(x\in\pi^nA\) for every \(n\), so
\(h\) is a nonzerodivisor. Apply this argument to the reduced regular
sequence. The resulting quotient is complete and torsion-free.

Lifting its finite monomial basis modulo \(\pi\), successive
approximation expresses every element as an \(\mathcal O\)-linear
combination of those same monomials. A relation among them has all
coefficients divisible by \(\pi\); torsion-freeness permits division,
and iteration makes the relation zero. Every full intermediate quotient
is thus finite free with the stated rank. In particular each fully
selected system has rank one. Its unit reduces to a basis of its
one-dimensional residue algebra, so the structural map
\(\mathcal O\to S/(L_{1,r_1},\ldots,L_{m,r_m})\) is an isomorphism.

It remains to justify a filtration rather than just a rank count.
Omit equation \(j\), and call the resulting complete quotient \(A\).
Write the current product in that equation as \(ab\), where \(a\)
is one of its factors. The element \(\bar a\) is a nonzerodivisor
in \(\bar A\). To see this, impose the lower-index equations first,
obtaining a possibly nonreduced ring \(C\). In \(C[u_j]\), the
element \(\bar a=u_j+A_{j,r}\) is monic and is a nonzerodivisor.
Adjoining each higher variable subject to its monic equation gives
a finite free extension and preserves this property. The preceding
lifting argument makes \(A\) torsion-free and \(a\) a nonzerodivisor.
Consequently the following sequence is exact:
\[
0\longrightarrow A/(b)
\xrightarrow{\;\cdot a\;}A/(ab)
\longrightarrow A/(a)\longrightarrow0.
\tag{3}
\]
Split each product recursively, then split the other equations.
This produces the asserted filtration. Repeated factors are allowed
in (3); they contribute repeated filtration factors.

Multiplication by \(H\) preserves the filtration. Each quotient is free
of rank one over \(\mathcal O\), and multiplication on it is the scalar
\(H(u^{\mathbf r})\). Choose an \(\mathcal O\)-basis adapted to the
filtration. The multiplication matrix is block triangular, so its
determinant is the product in (2). \(\square\)

## 3. Consequences for the full row-9 algebra

In \(\mathcal O\langle u_4,\ldots,u_{16}\rangle[X]\), the polynomial
\(g_u\) has a unique analytic root function \(\rho_r(u)\) reducing to
each residue root \(r\) of \(D\). Indeed, a constant lift of \(r\)
has \(g_u\)-value divisible by \(17\), while the derivative reduces
to the nonzero constant \(D'(r)\). The complete-ring Hensel iteration
therefore constructs \(\rho_r\). Distinct root functions have unit
differences. Monicity and the degree give the exact factorization
\[
g_u(X)=\prod_{r\in Z(D)}(X-\rho_r(u)).
\]
Thus, without an omitted leading-coefficient factor,
\[
R_j(u)=\prod_{r\in Z(D)}G_j(\rho_r(u)).
\tag{4}
\]
The reduction of a factor is
\[
\overline{G_j(\rho_r(u))}
=u_j+r^j-\binom j3r^{j-3}
+\sum_{i=4}^{j-1}\binom ji u_i r^{j-i}.
\]
It has precisely form (1). Proposition 1 applies with thirteen
variables and eighteen factors per equation.

**Corollary 2.** After base change to \(\mathcal O\), the completed
row-9 resultant algebra has a filtration with \(18^{13}\) rank-one
factors. Its obstruction norm satisfies
\[
N=\prod_{\mathbf r\in Z(D)^{13}}\tau_{\mathbf r},
\qquad
\tau_{\mathbf r}=T(u^{\mathbf r})\in\mathcal O.
\tag{5}
\]
Every integral geometric solution of the square resultant system
has all its coordinates in \(K\). Every genuine row-9 CA polynomial,
if one exists, has all its roots in \(K\) after this normalization.

For the last assertion, an integral solution in any valued extension
chooses a vanishing factor of each product (4). The selected quotient
is \(\mathcal O\), so its parameters equal the corresponding
\(u^{\mathbf r}\). Then \(g_u\) splits into the displayed analytic
roots in \(\mathcal O\), and \(f_u=(X-1)^2g_u\) adds only the root one.
This treats arbitrary ramification; it does not assume it away.

The same result applies to every fixed active support \(J\), with
zero removed from the domain and \(g_u/X\) in place of \(g_u\).
Its rank is \(17^{|J|}\). Nominally active coefficients with zero
residue remain included.

This fixed unramified field conclusion was already implicit in the
marked Hensel proof of the existing batch exclusions. The additional
point here is the filtration of the potentially nonreduced resultant
algebra and the exact multiplicity-preserving norm identity (5).

Let \(\sigma\) be the Frobenius automorphism of \(K/\mathbb Q_{17}\).
Uniqueness of the marked lifts gives
\[
u^{\sigma\mathbf r}=\sigma(u^{\mathbf r}),\qquad
\tau_{\sigma\mathbf r}=\sigma(\tau_{\mathbf r}).
\tag{6}
\]
The residue-domain cycles have lengths \(1,5,10\); hence so do marked
tuple orbits. If an orbit has length \(d\), its representative value
belongs to the degree-\(d\) unramified subfield \(K_d\), and its
contribution to (5) is
\[
\operatorname{Norm}_{K_d/\mathbb Q_{17}}(\tau_{\mathbf r}).
\]
If every factor is nonzero, then
\[
v_{17}(N)=\sum_{\text{marked orbits }[\mathbf r]}
 d_{\mathbf r}\,v_{17}(\tau_{\mathbf r}).
\tag{7}
\]
All valuations in this sum are integers. This avoids any determinant
cancellation issue, but not the need to establish nonvanishing on
every relevant marked orbit.

## 4. Why the quadratic Frobenius law alone does not close the branch

The coefficients of the equations lie in \(\mathbb Z_{17}\); the
coefficients of an individual solution need not. Equation (6) transports
a solution to its conjugate. It does not say that it fixes that
solution. The following compact example shows the issue within the
actual complete first-residue incidence equations.

Let \(r\) have irreducible polynomial
\[
Q_5(r)=r^5-3r^4-2r^2-5r-3=0
\quad\text{over }\mathbb F_{17}.
\]
Use the active set \(J=\{4,9,10,14\}\) and witnesses
\[
r_4=-2,\qquad r_9=r,\qquad r_{10}=1,\qquad r_{14}=-2.
\]
At inactive indices choose zero. The derivative recurrences give
\[
\begin{aligned}
u_4&=-7,\\
u_9&=-5r^4+5r^3+8r^2+7r-3,\\
u_{10}&=-r^4+r^3+5r^2-2r+4,\\
u_{14}&=-4r^4+4r^3+3r^2-8r-4,
\end{aligned}
\]
and all other middle \(u_j\) vanish. Every marked witness is a root
of \(h=X^{20}-X^{17}-3X^2+3X\), every marked normalized derivative
vanishes, and direct reduction gives \(\bar T=0\). Nevertheless,
\[
u_9^{17}-u_9
=7r^4+r^3-8r^2-7r+7\ne0.
\tag{8}
\]
The last inequality follows from irreducibility and the nonzero
degree-four remainder. The transformed \(y=7(r+1)/(r-1)\) also
satisfies \(y^{17}=y^2-5\), exactly as required.

Thus all first-residue constraints and the quadratic Frobenius law
are consistent with non-Frobenius-fixed coefficients. Taking traces
is legitimate, but cannot turn (6) into equality of the individual
coefficient values. This is the already known degree-five residue
fixture, here reconstructed symbolically; it is not a new surviving
characteristic-zero candidate.

The residue obstruction itself has a compact expression:
\[
\bar T=4+\sum_{j=4}^{16}
\frac{3(-1)^j}{j(j-3)}u_j.
\tag{9}
\]
For \(4\leq j\leq16\), cancelling the unique factor \(17\) in
\(\binom{20}{j}\) gives
\[
\frac{\binom{20}{j}}{17}
\equiv\frac{6(-1)^j}{j(j-1)(j-2)(j-3)}\pmod{17}.
\]
Multiplication by \(\binom{19-j}{2}\) proves (9).
The weights are symmetric under \(j\mapsto20-j\). Example (8) shows
that this smaller formula is not itself a nonvanishing invariant.

## 5. Even the first three obstruction digits can vanish

There is a small exact example inside the true marked square system,
not only a residue-field construction. Use
\(J=\{4,5,8,10,11\}\), initially put every active witness equal to one,
and solve the normalized derivative equations recursively. This gives
\[
(u_4,u_5,u_8,u_{10},u_{11})
=(3,-6,181,-7144,50665).
\]
All those normalized derivative incidences at one hold exactly, and
\[
T=11294240224=17^3\cdot2298848,\qquad 17\nmid2298848.
\tag{10}
\]
For \(q_u=g_u/X\), the exact identity \(q_u(1)=17T\) makes the
single marked root equation vanish modulo \(17^4\).

The derivative equations express the \(u_j\) as integer polynomials
of the one common witness \(x\). The marked root equation
\(q_{u(x)}(x)=0\) has a unit derivative modulo \(17\): parameter
dependence disappears modulo \(17\), and \(\bar q'(1)\ne0\).
Its exact root therefore differs from one by an element of
\(17^4\mathbb Z_{17}\). All corresponding \(u_j\), and hence \(T\),
change by multiples of \(17^4\). Its exact square-system obstruction
has valuation precisely three.

Consequently no uniform claim that all marked obstruction values
are units, or have valuation at most one or two, can hold. This does
not disprove a larger uniform bound. No such bound was established
in this investigation.

## 6. Verification and unresolved implication

The small standalone standard-library script
[check_structural_argument.py](check_structural_argument.py) checks:

- irreducibility of \(Q_5\) by the degree-five Frobenius criterion;
- the displayed coefficient formulas, all residue root incidences,
  the vanishing of \(\bar T\), and nonvanishing in (8);
- the quadratic Frobenius identity and all weights in (9);
- the integer recursion and exact valuation in (10).

It imports no producer modules and performs no census. Normal and
optimized runs have matching output. Proposition 1 also received a
separate algebraic audit: the auditor identified the need to justify
torsion-freeness of the omitted-equation quotient and confirmed the
monic-extension argument after that justification. This is an internal
mathematical review, not external refereeing or formal verification.

The exact remaining assertion is:
\[
\tau_{\mathbf r}\ne0
\quad\text{for every marking needed by the complete row-9 cover}.
\tag{11}
\]
It remains unproved here. The filtration does not reduce the number
of marked tuples; the Frobenius relation does not force a candidate
to be Frobenius fixed; and the small examples rule out several
low-digit shortcuts. Neither the product formula (5) nor the field
degree bound is a new exclusion theorem.

No conjectural step is used in Proposition 1 and Corollary 2 or the examples.
Statement (11) is the unresolved target, not a theorem. This bounded
route supplies a reusable algebraic decomposition and precise limits
on two proposed shortcuts, but it does not yet supply the consequential
new CA result sought by the parent task.
