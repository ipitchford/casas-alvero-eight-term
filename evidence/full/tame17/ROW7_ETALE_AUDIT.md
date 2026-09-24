# Row 7: bounded extension of the unramified lifting argument

23 September 2026. **Independent adversarial audit: PASS.** The argument
works after the exact row-7 restrictions already proved in
`../LIFT_CONSEQUENCES_17.md`. It reduces this branch to unramified lifts
with one additional exact obstruction; it does not exclude the branch.

## The exact normalization and fixed residue

Use \(a_2=-1,a_3=2,a_{17}=0\) and the exact root one shared with
Hasse orders 17 and 18. The fixed residue is

\[
h=X^{20}-3X^{18}+2X^{17}-3X^2+3X.
\]

The root one is simple, with \(h'(1)=14\). Its \(H_2\) gcd is
\(X-1\), so the corresponding exact common witness is also one.
Therefore the true polynomial satisfies \(f(1)=H_2f(1)=0\).

Write \(u_j=a_j\) for \(4\le j\le16\) and \(C_j=\binom{20}{j}\).
The polynomial has fixed leading part
\(X^{20}-190X^{18}+2280X^{17}\). Solving the two equations gives

\[
190a_{18}=-281200-\sum_{j=4}^{16}\binom{20-j}{2}C_ju_j,
\]
\[
20a_{19}=279109+
\sum_{j=4}^{16}\left(\binom{20-j}{2}-1\right)C_ju_j.
\tag{1}
\]

Both denominators are 17-adic units. The derivatives of the resulting
polynomial \(f_u\) with respect to its parameters are

\[
\frac{\partial f_u}{\partial u_j}
=C_j\left[X^{20-j}-\binom{20-j}{2}X^2
+\left(\binom{20-j}{2}-1\right)X\right].
\tag{2}
\]

They are coefficientwise divisible by 17. Hence \(\bar f_u=h\) for
every integral parameter vector, and the reduced derivatives with
respect to \(u\) vanish identically. The constants in (1), the
derivatives in (2), and the following local values pass the independent
`check_row7_etale_constants.py` replay, normally and under `python3 -O`.

## Replace the singular root equation by its critical-point equation

The only multiple root of \(h\) is seven:

\[
\gcd(h,H_1h)=X-7,
\qquad (h(7),H_1h(7),H_2h(7))=(0,0,8).
\]

Thus the residue cluster at seven has total multiplicity exactly two.
The characteristic-zero \(H_1\) condition forces a repeated root in
this cluster. Its multiplicity exhausts the cluster, so both roots
coincide exactly at a root \(r\) with \(\bar r=7\). Every middle
derivative witness reducing to seven must equal this same \(r\).
This uses multiplicities, not an inference from equal residues alone.

Introduce one variable \(r\), and impose

\[
G_{19}(r)=f_u'(r)/20=0
\tag{3}
\]

in place of the singular equation \(f_u(r)=0\). The derivative of
(3) with respect to \(r\) is
\(19G_{18}(r)=f_u''(r)/20\), with residue

\[
\frac{2H_2h(7)}{20}=\frac{16}{3}=11\ne0.
\tag{4}
\]

By differentiating (2) and dividing by the unit 20, its partial
derivatives with respect to every \(u_j\) are divisible by 17.
Therefore (3) supplies the needed nonsingular root block.

## The full square subsystem and unramified uniqueness

Fix residues \(\rho_j\) of the common witnesses for \(G_j\),
\(4\le j\le16\). At zero use the exact witness zero, because
\(h'(0)=3\); at one use the exact normalized root one; at seven
use the shared variable \(r\). For every other selected residue,
introduce an independent variable \(r_j\) and the equation
\(f_u(r_j)=0\). Those residue roots are simple. Also impose all
13 equations \(G_j(w_j)=0\), with \(w_j\) chosen as above.

There are as many equations as variables: the critical equation (3),
one equation per additional root variable, and the 13 middle derivative
equations. In residue characteristic 17 the Jacobian has block form

\[
\begin{pmatrix}
\operatorname{diag}(11,h'(\rho_j),\ldots)&0\\ B&L
\end{pmatrix},
\]

where \(L\) is lower triangular with diagonal one. Indeed each
\(G_j\) involves only \(u_i\) with \(i\le j\), and its coefficient
on \(u_j\) is one. Reusing \(r\) for several middle witnesses affects
only the lower-left block, not the determinant. The determinant is a
unit at every actual residue point.

Let \(E\) be a finite splitting field of \(h\). The triangular
middle equations force every \(\bar u_j\) into \(E\), since all
selected residues belong to it. The critical residue is the fixed
prime-field point seven. Consequently the system has a unique Hensel
lift in the integer ring of the unramified extension of \(\mathbb Q_{17}\)
with residue field \(E\).

The minimum-valuation Taylor uniqueness proof in `ROW9_ETALE_AUDIT.md`
applies verbatim: an invertible integral Jacobian preserves the minimum
valuation of a nonzero difference, while quadratic terms have strictly
higher valuation. Thus there cannot be a second solution with the same
residues in a ramified extension. Every actual row-7 CA solution has
unramified coefficients and selected witnesses in this normalization.

## The omitted condition

The equation omitted from the square subsystem is exactly

\[
f_u(r)=0.
\]

It remains an additional exact obstruction, and has not been shown to
fail at every Hensel lift. If it holds, (3) makes \(r\) the required
repeated root; the fixed residue multiplicity ensures it is exactly
double. All common-root conditions are then present: orders 19,3 use
zero; orders 18,17,2 use one; orders 16 through 4 use their chosen
witnesses; and order 1 uses \(r\). Conversely, every actual row-7
counterexample maps to this system and its extra equation.

The preliminary use of an actual repeated root is not circular: it
justifies completeness of the witness substitutions for hypothetical
CA solutions. The square subsystem is allowed to have extra solutions
until \(f_u(r)=0\) is imposed. The conclusion is a complete
unramified lifting reduction for row 7, not an exclusion, and no
corresponding assertion is made here for the other residue rows.
