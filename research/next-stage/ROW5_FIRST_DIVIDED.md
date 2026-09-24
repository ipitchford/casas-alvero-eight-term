# Complete first-divided residue sieve for the remaining row-5 support

24 September 2026. Research note. The valuation arguments and all
27 middle-witness assignments have been independently checked.
Ten marked branch assignments survive. This is not a row-5 exclusion
or a characteristic-zero existence result.

## 1. Exact family and branch cover

Use the exact centered deficiency support
\[
S=\{2,3,4,10,12,19\}.
\]
In the row-5 normalization the common \(G_2\) root is exactly one,
so \(a_2=-1\). Put \(u_j=a_j\) for \(j\in J=\{4,10,12\}\) and
\(C_j=\binom{20}{j}\). Then
\[
\begin{aligned}
f(X)={}&X^{20}-190X^{18}+1140a_3X^{17}\\
&+4845u_4X^{16}+184756u_{10}X^{10}
+125970u_{12}X^8+EX,
\end{aligned}
\tag{1}
\]
where all normalized coefficients are integral and
\[
E=189-1140a_3-\sum_{j\in J}C_ju_j,\qquad f(1)=0.
\tag{2}
\]
The exact support assumption makes \(E\ne0\), so zero is simple.
The reduction is
\[
h=X^{20}-3X^{18}+2X^{17}
=X^{17}(X-1)^2(X+2),
\qquad \bar a_3=2.
\tag{3}
\]
The exact coefficients at indices 17 and 18 vanish.

Choose a common root \(y\) of \(f\) and \(G_3\), and a repeated
root \(w\) of \(f\), equivalently an \(H_1\) common witness.
Since
\[
G_3=X^3-3X+a_3,
\]
the possible residues of \(y\) are one and \(-2\). The repeated
witness has residue zero or one; the residue \(-2\) is simple.
These four marked choices give a complete cover. A candidate may
admit more than one witness choice, so the branches need not be
disjoint as sets of exact polynomials.

All valuations below are normalized by \(\nu(17)=1\), with arbitrary
ramification allowed.

## 2. The \(G_3\) witness near one

Suppose \(y=1+z\) with \(\nu(z)>0\), allowing \(z=0\).
The exact normalized derivative equation gives
\[
a_3=-y^3+3y=2-3z^2-z^3.
\tag{4}
\]
Direct differentiation of (1)–(2) yields
\[
f'(1)=17\cdot1957+18240(a_3-2)
+\sum_{j\in J}(19-j)C_ju_j.
\tag{5}
\]
Moreover,
\[
\overline{H_2f(1)}=3.
\tag{6}
\]
The latter identity follows either by Hasse differentiation of (3)
or coefficientwise: all parameter directions in \(H_2f(1)\) vanish
modulo 17.

If \(z\ne0\) and \(0<\epsilon=\nu(z)<1\), equation (5) has valuation
at least \(\min(1,2\epsilon)>\epsilon\). Dividing \(f(1+z)=0\) by
\(z\) gives
\[
0=f'(1)+H_2f(1)z+\sum_{k=3}^{20}H_kf(1)z^{k-1}.
\]
The second term has valuation exactly \(\epsilon\), whereas the
first and all remaining terms have greater valuation. This is
impossible. Thus
\[
\nu(y-1)\ge1,\qquad \nu(a_3-2)\ge2,
\tag{7}
\]
with infinite valuation allowed. This argument does not assume
that the repeated witness \(w\) is in the unit cluster.

In the divided residue formulas below, this branch therefore has
correction parameter \(\tau=0\). This notation does not assert
that \(y=1\) in the subbranch where \(w\) reduces to zero.

## 3. The \(G_3\) witness near \(-2\)

For an integral parameter vector \(u\), write \(F_u(X,a_3)\) for
the polynomial (1) with (2), and set
\[
\Psi_u(Y)=F_u(Y,-Y^3+3Y).
\]
At \(Y=-2\), the substituted parameter equals two. Define
\(F_{\mathrm{base},u}(X)=F_u(X,2)\). A coefficientwise calculation
gives
\[
\begin{aligned}
\frac{F_{\mathrm{base},u}(-2)}{17}
={}&-20446986+18678330u_4\\
&+11150568u_{10}+1911780u_{12}.
\end{aligned}
\tag{8}
\]
In particular the numerator belongs to \(17O\) for every integral
parameter vector, including ramified ones.

The total \(Y\)-derivative satisfies
\[
\overline{\Psi_u'(-2)}=16.
\tag{9}
\]
Indeed, its partial \(X\)-derivative is \(h'(-2)=16\); the additional
term from the substituted \(a_3\) contains
\(1140(Y^{17}-Y)\), which vanishes modulo 17 at \(-2\).
All middle parameter directions are divisible by 17.

If \(0<\nu(y+2)<1\), the linear term in the Taylor expansion of
\(\Psi_u(y)=0\) has that valuation, whereas the constant has
valuation at least one and all higher terms have greater valuation.
Hence \(y+2\in17O\), proved without an unramified assumption.
Write \(y=-2+17t\). Equations (8)–(9) give
\[
\bar t=-16^{-1}\overline{F_{\mathrm{base},u}(-2)/17}
=2+5\bar u_4+13\bar u_{10}+11\bar u_{12}.
\tag{10}
\]
Here \(-16^{-1}=1\) in characteristic 17. The exact cubic expansion
\[
a_3=2-9(17t)+6(17t)^2-(17t)^3
\]
then gives
\[
\overline{(a_3-2)/17}=-9\bar t.
\tag{11}
\]
For this branch put \(\tau=\bar t\).

## 4. The repeated witness near one

The residue class one contains exactly two roots, counted with
multiplicity. It already contains the known exact root one. If a
distinct repeated root \(w\) lay in this class, it would require
at least three roots there. Consequently
\[
w=1,\qquad f'(1)=0.
\]
Dividing (5) by 17 and using (7) or (11) gives the necessary equation
\[
1957+\sum_{j\in J}(19-j)\frac{C_j}{17}\bar u_j+9\tau=0
\quad\text{in characteristic }17.
\tag{12}
\]
The correction sign follows from \(18240\equiv16\) and
\(-9\cdot16=9\pmod{17}\).

If \(y\) also reduces to one, the same two-root count additionally
forces \(y=1\) exactly. This strengthens (7) but is not needed for
the first residue test.

## 5. The repeated witness in the zero cluster

Let
\[
\delta=\min\{\nu(r):f(r)=0,\ r\ne0,\ \bar r=0\}.
\]
This positive minimum exists: the residue cluster has seventeen roots
and the exact root zero is simple. An \(H_1\) witness in this cluster
is nonzero, so its valuation is at least \(\delta\).

The normalized derivative equation \(G_{19}(w)=0\) implies
\[
\nu(a_{19})\ge\min(17\delta,1+7\delta).
\tag{13}
\]
In detail, its \(a_2w^{17}\) coefficient is a unit; the coefficients
at indices \(3,4,10,12\) are divisible by 17; and the two low
parameters \(a_{17},a_{18}\) vanish exactly. The smallest exponent
among those middle terms is seven. A zero coefficient only improves
the bound.

At a root \(r\) attaining \(\delta\), the ordinary \(X^{17}\) term
of \(f(r)\) has valuation exactly \(17\delta\), since \(1140a_3\)
is a unit. Every other term has valuation at least
\[
\min(18\delta,1+8\delta),
\]
where the linear term uses \(E=20a_{19}\) and (13). If
\(\delta<1/9\), the \(X^{17}\) term is uniquely lowest. Therefore
\[
\delta\ge1/9,\qquad
\nu(E)=\nu(a_{19})\ge1+7\delta\ge16/9>1.
\tag{14}
\]
No integer-valuation assumption is used. This zero-cluster argument
received a separate bounded adversarial audit.

Equations (2), (7) and (11), divided by 17, now yield the necessary
condition
\[
-123-\sum_{j\in J}\frac{C_j}{17}\bar u_j+9\tau=0.
\tag{15}
\]
This differs from the unit repeated-witness condition (12).

## 6. Complete middle-witness residue enumeration

At each active middle index \(j\in J\), a common witness residue
belongs to the complete domain
\[
\rho_j\in\{0,1,-2\}.
\]
The zero label is retained even when \(u_j\ne0\) exactly: neither
an exact coefficient nor a nonzero root is required to have
nonzero residue. At an inactive middle index the exact zero
coefficient can choose the exact common root zero.

Starting from
\(\bar a_0=1,\bar a_1=0,\bar a_2=-1,\bar a_3=2\), reconstruct
successively
\[
\bar a_j=-\sum_{i=0}^{j-1}\binom ji\bar a_i\rho_j^{j-i}.
\tag{16}
\]
This proves containment of the coefficient residues in
\(\mathbb F_{17}\); it is not an initial assumption about a larger
residue field or a lift. There are exactly \(3^3=27\) assignments.
Each is tested in all four marked branches using (10), (12), and (15).

The complete survivors are:

| \(\bar y\) | \(\bar w\) | Middle witness residues \((\rho_4,\rho_{10},\rho_{12})\) | Middle coefficient residues \((\bar u_4,\bar u_{10},\bar u_{12})\) | \(\tau\) |
|---:|---:|---|---|---:|
| 1 | 0 | none | — | — |
| 1 | 1 | \((-2,0,-2),(-2,1,-2)\) | \((7,0,9)\) | 0 |
| \(-2\) | 0 | \((-2,0,0),(-2,1,0)\) | \((7,0,0)\) | 3 |
| \(-2\) | 1 | \((-2,0,0),(-2,1,0)\) | \((7,0,0)\) | 3 |
| \(-2\) | 1 | \((-2,0,1),(-2,1,1)\) | \((7,0,2)\) | 8 |
| \(-2\) | 1 | \((-2,0,-2),(-2,1,-2)\) | \((7,0,9)\) | 0 |

The branch counts are \(0,2,2,6\), respectively. The ten survivors
are marked necessary configurations, not ten distinct polynomials
or ten characteristic-zero solutions.

## 7. Independent arithmetic and scope

[check_row5_first_divided.py](check_row5_first_divided.py) imports no
producer or prior checker. It reconstructs the integer family, obtains
the affine value (8) and total derivative (9), verifies the Taylor
and binomial constants, and independently traverses all 27 assignments
using the full recurrence (16). Its receipts retain all 27 records,
all four divided values for each, and every survivor.

The ordinary and optimized Python receipts are
[row5-first-divided-normal.json](row5-first-divided-normal.json) and
[row5-first-divided-optimized.json](row5-first-divided-optimized.json).
No large census, PDF, or publication bundle was produced.

This note closes the first-divided sieve only. It excludes the
\((\bar y,\bar w)=(1,0)\) marked branch and restricts the other three.
It neither excludes the complete support nor proves that any surviving
configuration lifts. The exact support, its characteristic-17
normalization, and the predecessor seed classification remain explicit
inputs to this local analysis.
