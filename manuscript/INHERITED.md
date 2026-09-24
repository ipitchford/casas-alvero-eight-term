# Appendix B. Three additional characteristic-seventeen exclusions

These are finite computational components of the closing table. Their normalized families, complete marking domains, and precision implications are included here so that the global theorem does not depend on a list of successful computations without a mathematical transfer argument.

## The row-8 divided census

In row 8, \(\bar f=X^{17}(X^3-1)\). Normalize a common \(G_3\) root to one, giving \(a_3=-1-3a_2\). Let \(\delta>0\) be the minimum valuation of a nonzero root in the seventeen-root zero cluster. Such a root exists because the mean is simple. The selected witnesses for \(G_2,G_{17},G_{18},G_{19}\) reduce to zero, and their equations give
\[
\begin{aligned}
\nu(a_2)&\ge2\delta,\\
\nu(a_{17})&\ge\min(17\delta,1+\delta),\\
\nu(a_{18})&\ge\min(18\delta,1+2\delta),\\
\nu(a_{19})&\ge\min(19\delta,1+3\delta).
\end{aligned}
\]
At a root attaining \(\delta\), the \(X^{17}\) term has valuation \(17\delta\); every other term has value at least \(\min(20\delta,1+4\delta)\). Thus \(\delta\ge1/13\). Substituting in \(f(1)=0\) and dividing by 17 gives the necessary relation
\[
 \sum_{j=4}^{16}\frac{\binom{20}{j}}{17}\bar a_j=-1.
\]
Indeed the exact equation before division is
\[
0=-17\cdot67-17\cdot190a_2+
\sum_{j=4}^{16}\binom{20}{j}a_j+1140a_{17}+190a_{18}+20a_{19};
\]
the preceding strict bounds remove the last three terms after reduction.

Every active middle witness has residue in \(\{0,1,\zeta,\zeta^2\}\), where \(\zeta^2+\zeta+1=0\). The recurrence
\[
\bar a_j=-\sum_{i<j}\binom ji\bar a_i\rho_j^{j-i}
\]
starts at \(\bar a_0=1,\bar a_1=\bar a_2=0,\bar a_3=-1\). At every inactive index choose \(\rho_j=0\), an exact common witness. Consequently the \(4^{|J|}\) choices for the active indices cover every algebraic residue witness; this is not a restriction to prime-field coefficients. The standard-library checker uses \(\mathbf F_{17}[s]/(s^2-14)\) and the explicit domain
\[
(0,0),\quad(1,0),\quad(8,9),\quad(8,8).
\]
It checks all 1,216 markings for the seven supports in the closing table. None satisfies the divided relation. The source, histogram digests and assignment counts, and normal and optimized receipts are in `new-results/check_row8_seven_term.py` and its companion records.

## Row 4 with middle support \(\{4,10,12\}\)

Normalize \(a_2=-1,a_3=a_{17}=0\) and the simple root one. A common \(H_2\) witness \(s\) reduces to 6. Put \(u_j=a_j\), and eliminate
\[
 a_{18}=-s^{18}+153s^{16}-\sum_j\binom{18}{j}u_js^{18-j},
\qquad
20a_{19}=189-\sum_j\binom{20}{j}u_j-190a_{18}.
\]
Call the resulting polynomial \(F(u,s;X)\). Its fixed reduction is
\[
h=X^{20}-3X^{18}+11X^2+8X.
\]
Its only multiple roots are the two roots \(\alpha,\beta\) of \(X^2+3X+3\), each of multiplicity two. The total \(s\)-derivative of \(F(u,s;s)\) is 9 modulo17 at \(s=6\); the derivative in the critical-root equation is \(h''(\alpha)=6\). Thus the simple implicit equations uniquely determine \(s=S(u)\) and each critical root \(R_\alpha(u)\) in its class.

The critical value \(F(u,S(u);R_\alpha(u))/17\) is integral analytic. Its first residue is obtained coefficientwise by
\[
\sigma(u)=-\frac{F(u,6;6)}{17\cdot9},
\qquad
\ell_\alpha(u)=\frac{F(u,6;\alpha)}{17}+(3+4\alpha)\sigma(u)
\quad\pmod{17}.
\]
For the three active indices it is
\[
\ell_\alpha=(10+14\alpha)+(16+15\alpha)u_4
 +10\alpha u_{10}+(16+15\alpha)u_{12}.
\]
The conjugate orientation replaces \(\alpha\) by \(\beta\), without applying Frobenius to the freely varying \(u_j\). The coefficientwise divisibility and simple implicit derivatives justify evaluation in arbitrary ramified extensions.

The seed splits over \(\mathbf F_{17^4}\), with factorization
\[
\begin{aligned}
h={}&X(X+7)(X+11)(X+16)(X^2+3X+3)^2\\
 &\cdot(X^4+3X^3+4X^2+2)\\
 &\cdot(X^4+12X^3+14X^2+5X+14)\\
 &\cdot(X^4+13X^3+16X^2+4X+11).
\end{aligned}
\]
There are seventeen distinct nonzero root residues. The mean class contains only the exact root zero, so an active coefficient cannot select it. Every one of the \(2\cdot17^3=9826\) oriented markings is retained, including coefficients of zero residue. The triangular recurrence and \(\ell_\alpha=0\) leave exactly two markings, one per orientation, both with
\[
(\rho_4,\rho_{10},\rho_{12})=(10,1,6),\qquad
(\bar u_4,\bar u_{10},\bar u_{12})=(1,4,9).
\]
These selected root classes are simple. Let the witness near10 be \(t\). The exact formulas are
\[
 u_4=-t^4+6t^2,\quad u_{10}=44-210u_4,
\quad u_{12}=-s^{12}+66s^{10}-495u_4s^8-66u_{10}s^2.
\]
The Jacobian of \(f(t)=f(s)=0\) in \((t,s)\) reduces to
\(\left(\begin{smallmatrix}2&12\\0&9\end{smallmatrix}\right)\).
The lift modulo \(17^3\) is
\[
(t,s,u_4,u_{10},u_{12})=(2696,1536,1531,2792,2610).
\]
At the critical point \(R=2788+3707\alpha\), direct substitution gives
\[
f'(R)=0\pmod{17^3},\qquad
f(R)=17^2(9+4\alpha)\pmod{17^3}.
\]
The last residue is nonzero; conjugation handles the other orientation. A unit Jacobian also controls ramified solutions: if an exact solution differs from a precision-\(17^n\) approximation at minimum valuation \(\gamma>0\), the linear term preserves \(\gamma\), whereas the residual has value at least \(n\) and nonlinear terms at least \(2\gamma\). Cancellation forces \(\gamma\ge n\). Therefore the nonzero saved critical value excludes all exact solutions. The full residue enumeration and lift identities are checked in `evidence/full/tame17/check_row4_smallest_support.py`.

## Row 9 with middle support \(\{4,10,13\}\)

The row-9 seed is \(X^{20}-X^{17}-3X^2+3X\). Its simple mean forces \(a_2=a_{17}=0\). A common \(G_3\) root can be normalized to one, giving \(a_3=-1\). The low derivative witnesses lie in the triple residue cluster at one. The separated-cluster lemma from the row-2 section, applied to a cubic in characteristic17, makes that cluster collapse: a centered cubic \(X^3+BX\) cannot have the CA property with \(B\ne0\), since its nonzero-root derivative equations differ by \(2B\). Thus one is an exact triple root.

After solving only \(f(1)=f'(1)=0\), retain the remaining triple-root condition separately. Write \(C_j=\binom{20}{j}\) and
\[
\begin{aligned}
f_u={}&X^{20}-1140X^{17}+\sum_{j=4}^{16}C_ju_jX^{20-j}\\
 &+\left(18221-\sum_{j=4}^{16}(19-j)C_ju_j\right)X^2\\
 &+\left(-17082+\sum_{j=4}^{16}(18-j)C_ju_j\right)X.
\end{aligned}
\]
Let \(q_u=f_u/[X(X-1)^2]\), a monic polynomial of degree17. The residual condition is
\[
T(u)=-8037+\sum_{j=4}^{16}\binom{19-j}{2}\frac{C_j}{17}u_j=0,
\qquad H_2f_u(1)=17T(u).
\]
Only indices \(4,10,13\) are active. Modulo17, \(q_u\) is fixed and squarefree. It splits over the degree-ten residue field defined by
\[
Z^{10}+4Z^9-Z^8+6Z^6+Z^4-6Z^3+4Z^2+7Z-8.
\]
The checker verifies irreducibility and seventeen distinct nonzero roots, which exhaust its algebraic roots. For each of the \(17^3=4913\) markings the recurrence is
\[
u_j=-\rho_j^j+\binom j3\rho_j^{j-3}
 -\sum_{i\in J,\,i<j}\binom ji u_i\rho_j^{j-i}.
\]
The complete first-residue census leaves one marking, with witness residues \((1,1,15)\) and coefficient residues \((3,16,16)\). These entries refer to the actual prime-field values in the stored field basis.

Use one variable for each distinct selected residue root and impose \(q_u(x_r)=0\), with coefficients reconstructed by the recurrence. This square system has diagonal reduced Jacobian, with entries 1 and9: every parameter-dependent coefficient of \(q_u\) is divisible by17. Its unique precision-\(17^3\) lift has roots \(1,2174\) and
\[
(u_4,u_{10},u_{13})=(3,4402,2770),
\qquad T=3179=11\cdot17^2\pmod{17^3}.
\]
The same unit-Jacobian precision argument excludes every ramified exact lift. It is essential that the root of \(q_u\) near one was not fixed to one before imposing \(T=0\); the square system is an enlargement of the CA equations until that last condition is checked. The source and independent residue/precision replay are in `evidence/full/collective17/exclusions/check_batch.py`. Only this one complete canonical system is used for the eight-term theorem; no claim about all 240 systems is needed.
