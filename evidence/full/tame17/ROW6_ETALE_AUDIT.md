# Row 6: bounded independent audit of the unramified reduction

23 September 2026. **PASS.** The proposed derivative 7 and the complete
square-system argument are correct. This is the last extension examined
in this bounded audit. It does not exclude row 6.

The previously proved exact data are \(a_2=-1,a_3=2,a_{17}=0\), with
the shared \(H_{18},H_{17}\) root normalized to one. The fixed residue is

\[
h=X^{20}-3X^{18}+2X^{17}+11X^2+6X.
\]

Its \(H_2\) gcd is \(X-6\), and \(h'(6)=3\), so the actual
\(H_2\) witness lies in a simple residue class; call it \(s\).
Its \(H_1\) gcd is \(X-10\), with \(H_2h(10)=5\ne0\).
Thus the only multiple residue cluster is at ten and has size two.
The first-derivative common witness exhausts this cluster as one exact
double root \(r\). All selected witnesses reducing to six must equal
\(s\), and those reducing to ten must equal \(r\). The roots zero
and one are simple, with derivatives 6 and 11, respectively.

Put \(u_j=a_j\), \(4\le j\le16\). Solving \(G_{18}(s)=0\)
for its constant coefficient gives the polynomial

\[
A(s,u):=a_{18}
=-s^{18}+153s^{16}-1632s^{15}
-\sum_{j=4}^{16}\binom{18}{j}u_js^{18-j}.
\tag{1}
\]

Then solve \(f(1)=0\):

\[
a_{19}=-\frac{2091+\sum_{j=4}^{16}\binom{20}{j}u_j+190A(s,u)}{20}.
\tag{2}
\]

The denominator 20 is a 17-adic unit. Both \(\binom{18}{j}\) and
\(\binom{20}{j}\) are divisible by 17 throughout the middle range.
Thus every partial derivative of \(a_{18},a_{19}\), and consequently
of \(f\), with respect to a middle parameter \(u_j\) is divisible
by 17. This statement holds with \(s\) treated as an independent
variable. The residue polynomial varies with \(\bar s\) in the
parameterized system, but at the relevant residue point \(\bar s=6\)
it is exactly the displayed \(h\). Fixed residue for all values of
\(s\) is neither true nor needed.

Holding \(u\) fixed, differentiation of (1) gives
\(A_s=-18G_{17}(s)\). At the residue point,

\[
\bar A_s=-6,\qquad
\overline{(a_{19})_s}=-(190/20)\bar A_s=6.
\]

Therefore the **total** derivative of the equation \(f_{u,s}(s)=0\)
with respect to \(s\) is

\[
h'(6)+190(-6)6^2+20(6)6
\equiv3-18\cdot36+18\cdot6
\equiv7\pmod{17}.
\tag{3}
\]

For the double-root variable impose the critical equation
\(G_{19}(r)=f_{u,s}'(r)/20=0\), leaving \(f_{u,s}(r)=0\) aside.
Its \(r\) derivative has residue

\[
h''(10)/20=2\cdot5/3=9\ne0.
\tag{4}
\]

Its partials with respect to middle parameters vanish modulo 17.
Its \(s\) partial need not vanish (it is 5), but this occupies only
a lower-triangular root-block position.

For each \(G_j\), \(4\le j\le16\), choose a witness residue among
the roots of \(h\). Use the exact constants zero and one for those
two classes, \(s\) for residue six, and \(r\) for residue ten.
Introduce a separate root variable \(z_j\) with equation
\(f_{u,s}(z_j)=0\) for every other selected class, all of which
are simple. Impose also all 13 equations \(G_j(w_j)=0\).

Together with \(f_{u,s}(s)=0\) and \(G_{19}(r)=0\), this is a
square system. Order variables as \(s,r,(z_j),u_4,\ldots,u_{16}\).
Its reduced Jacobian has a zero upper-right block. Its root block is
lower triangular with diagonal

\[
7,\quad9,\quad h'(\bar z_j),\ldots,
\]

all nonzero. Its lower-right block is lower triangular with diagonal
one, since the coefficient of \(u_j\) in \(G_j\) is one and
later parameters do not occur. Shared occurrences of \(s\) or \(r\)
in middle witnesses affect only the lower-left block. Distinct variables
for repeated selections of another simple residue cause no difficulty.

The triangular equations force all middle coefficient residues into a
finite splitting field \(E\) of \(h\), starting from the fixed
residues \(s=6,r=10\). The unit Jacobian then gives an unramified
Hensel lift for each marked residue assignment. The minimum-valuation
Taylor uniqueness argument in `ROW9_ETALE_AUDIT.md` excludes a different
solution with those residues in any ramified extension. Every actual
row-6 counterexample therefore belongs to this unramified lifting
description after the stated normalization.

The remaining condition is \(f_{u,s}(r)=0\). No proof that it fails
has been given. If it holds, all Hasse common-root conditions are present:
orders 19 and 3 use zero; orders 18 and 17 use one; orders 16 through 4
use the chosen middle witnesses; order 2 uses \(s\); and order 1 uses
\(r\). Equations (1) and (2) impose the first two required incidences
at \(s\) and one; the square system and the remaining condition impose
the rest. Thus no derivative order is missing from the reduction.

`check_row6_etale_constants.py` independently verifies (1)–(4), the
binomial divisibilities, and the local multiplicities. Ordinary and
optimized Python runs both pass. The conclusion is a complete unramified
parameter reduction for this branch, with one untested exact obstruction.
