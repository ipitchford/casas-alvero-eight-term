# Exclusion of both u=v branches by two valuation steps

This proof concerns the two remaining marked residue assignments
\((\bar v,\bar u,\bar w)=(2,2,1),(2,2,4)\) from the audited C
classification. It does not assert an exclusion of the other C assignments.
Here \(u,v,w\) are common-root witnesses for Hasse orders 15, 3, and 1.
The order-16 witness has been normalized to 1.

Let \(\mathcal O\) be the valuation ring already supplied by the
characteristic-zero normalization. Write the valuation additively and denote
\(v(13)\) by 1; inequalities below are comparisons in its ordered value
group and do not assume that the group is discrete or rank one. All roots and
binomial-normalized coefficients are integral. The prior classification gives
the residual polynomial
\[
h_0=X^{20}+4X^{16}+6X^{15}+3X^3+12X.
\]
Its root 2 is simple, so the two integral roots reducing to 2 are equal:
\(u=v\). Its roots 1 and 4 have multiplicities two and three respectively.

Write
\[
f=X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\quad A=-4845,\quad E=-1-A-B-C-D.
\]
Thus \(f(1)=0\). We have \(\bar u=2,\bar D=3\), and
\(C\in13\mathcal O\), because \(13\mid\binom{20}{10}\).
The exact order-15 equation gives
\[
B=B(u)=-15504u^5+77520u.\tag{1}
\]

## 1. A unit-Jacobian precision lemma

Suppose an integral polynomial vector \(F\) in \(n\) variables vanishes
at \(a+\delta\), where every component of \(\delta\) has positive
valuation. Suppose \(F(a)\in13\mathcal O^n\) and the Jacobian at \(a\)
has unit determinant. Then each component of \(\delta\) lies in
\(13\mathcal O\).

Indeed, if the least component valuation \(t\) were below 1, Taylor expansion
and multiplication by the integral inverse Jacobian would express \(\delta\)
as a vector whose components have valuation at least \(\min(1,2t)>t\), a
contradiction. The same argument allows extra perturbation terms lying in
\(13\mathcal O^n\). This is an exact valuation argument and requires no
completeness or unramified hypothesis.

Apply it first to \((f(u),H_3f(u))\), viewed as polynomials in \((u,D)\),
with \(B\) given by (1), \(E\) given above, and \(C\in13\mathcal O\)
as an integral perturbation. At \((u,D,C)=(2,3,0)\), both constants are
divisible by 13, and the Jacobian in \((u,D)\), modulo 13, is
\[
\begin{pmatrix}10&6\\4&1\end{pmatrix},\qquad\det=12.
\]
Consequently
\[
u=2+13r,\qquad D=3+13l,\qquad C=13k,
\quad r,l,k\in\mathcal O.\tag{2}
\]
In particular the coefficients of \(f-h_0\) belong to \(13\mathcal O\),
a stronger statement than merely having positive valuation.

## 2. Exact first jets and the divided middle derivative

Substitution of (2) gives the following exact residues. The displayed linear
expressions are the reductions of the corresponding quotients by 13:
\[
\begin{array}{c|c}
\text{expression}&\text{residue modulo the maximal ideal}\\\hline
f(u)/13&7+10r+6l+8k\\
H_3f(u)/13&6+4r+l+7k\\
H_1f(1)/13&4+11r+2l+9k\\
f(4)/13&3+10r+8l+5k.
\end{array}\tag{3}
\]
Each quotient is an integer-coefficient polynomial in \(r,l,k\). The
constant term before division is divisible by 13, and all other terms contain
an explicit factor 13. These facts matter when the precision lemma is applied
again below.

The exact middle derivative is
\[
H_{10}f=184756X^{10}+8008AX^6+3003BX^5+C.
\]
After dividing by 13 its leading coefficient is
\(\lambda=184756/13=14212\), a unit with residue 3. Hence the monic
polynomial \(G=H_{10}f/184756\) is integral and has reduction
\[
\bar G=X^{10}+11X^6+7X^5+\bar k/3.\tag{4}
\]
Every integral common-root witness for \(f,H_{10}f\) reduces to a common
root of \(h_0,\bar G\).

## 3. The branch with w reducing to 4

Here \(w\) is a repeated exact root of \(f\), so \(f(w)=f'(w)=0\).
Put \(\delta=w-4\). If \(\delta=0\), then \(f(4)=0\). Otherwise set
\(t=v(\delta)>0\). Since \(f-h_0\in13\mathcal O[X]\) and the
residue root 4 has multiplicity three,
\[
v(f'(4))\ge1,\quad v(H_2f(4))\ge1,\quad v(H_3f(4))=0.
\]
In the Taylor expansion of \(f'(4+\delta)\), the quadratic term
\(3H_3f(4)\delta^2\) would have uniquely least valuation if \(2t<1\).
Thus \(2t\ge1\). Every nonconstant term of \(f(4+\delta)\) then has
valuation strictly greater than 1: the first two have valuations at least
\(1+t\) and \(1+2t\), and the remaining terms have valuation at least
\(3t>1\). It follows that \(v(f(4))>1\).

Therefore the first, second, and fourth rows of (3) all vanish in the residue
field. Their coefficient matrix has determinant 5, and their unique solution is
\[
(\bar r,\bar l,\bar k)=(5,7,12).
\]
Equation (4) becomes
\(\bar G=X^{10}+11X^6+7X^5+4\). Exact Euclidean division gives
\[
\gcd(h_0,\bar G)=1.
\]
This contradicts the required order-10 common root and excludes the branch.

## 4. The branch with w reducing to 1

There is already an exact root at 1. If the repeated root \(w\ne1\) also
reduced to 1, that residue cluster would contain at least three exact roots,
counting multiplicity. Its residue multiplicity is only two. Thus \(w=1\).
The first three quotients in (3) vanish exactly. Their residue matrix is
\[
M=\begin{pmatrix}10&6&8\\4&1&7\\11&2&9\end{pmatrix},
\qquad\det M=3,
\]
and its unique residue solution is
\[
(\bar r,\bar l,\bar k)=(12,3,3).\tag{5}
\]

Merely knowing these residues would not be enough for the next step in an
arbitrarily ramified field. Apply the precision lemma a second time to the
three exact integral polynomials
\((f(u),H_3f(u),H_1f(1))/13\) in \((r,l,k)\). At the integer point
\((12,3,3)\), their values lie in \(13\mathbb Z\), since (5) solves
their residue equations; their Jacobian modulo 13 is \(M\). We obtain
\[
r-12,\quad l-3,\quad k-3\ \in13\mathcal O.\tag{6}
\]

Now \(G\) is congruent modulo \(13\mathcal O[X]\) to
\[
G_1=X^{10}+11X^6+7X^5+1.
\]
For the coefficient involving \(B\), this follows from (1) and (2); for
the constant coefficient, it uses \(k-3\in13\mathcal O\) and
\(\lambda\equiv3\pmod{13}\). The remaining coefficient is a fixed
rational 13-adic integer. Exact polynomial arithmetic gives
\[
\gcd(h_0,G_1)=X-4,\qquad G_1'(4)=3.
\]
Let \(z\) be an order-10 common root. Then \(\bar z=4\),
\(G(4)\in13\mathcal O\), and \(G'(4)\) is a unit. The one-variable
case of the precision lemma forces
\[
z-4\in13\mathcal O.
\]
Taylor expansion of \(f\) at 4 now shows
\(f(z)-f(4)\in13^2\mathcal O\): the first derivative already lies in
\(13\mathcal O\), and each term of order at least two contains
\((z-4)^2\). Since \(f(z)=0\), this would give
\(f(4)\in13^2\mathcal O\). But the last row of (3), evaluated at (5),
gives
\[
f(4)/13\equiv3+10\cdot12+8\cdot3+5\cdot3=6\ne0\pmod{13}.
\]
This contradiction excludes the second branch.

## 5. Exact checks and scope

`check_jets.py` reconstructs the integer Hasse equations and differentiates
the integer coefficient expressions before reducing. It verifies every row
and constant in (3), all three unit determinants, the two linear solutions,
the Hasse multiplicities of the relevant residue roots, both middle-derivative
gcds, \(G_1'(4)=3\), and the final residue 6. It uses only Python's
standard library. The precision and cluster arguments above remain written
mathematics, separate from the arithmetic replay.

An independent larger route is also retained: rational parametrization in
\(u\), integer resultants, and a degree-preserving modular coprimality check.
Its independent replay passed 1,544 exact integer Sylvester determinants.
The compact proof above does not depend on that route or on affine modular
emptiness. Both arguments exclude precisely the assigned \(u=v\) cases;
other C branches require their own arguments.
