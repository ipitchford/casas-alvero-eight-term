# Row 9: an unramified lifting reduction

23 September 2026. **Independent adversarial audit: PASS**, with the
normalization and scope stated below. This establishes a complete
unramified lifting reduction for row 9; it does not exclude the row.
No analogous conclusion for another residue branch follows automatically.

## Exact input and coefficient elimination

The already audited row-9 consequences give a centered monic polynomial

\[
f=X^{20}-1140X^{17}+
\sum_{j=4}^{16}\binom{20}{j}u_jX^{20-j}
+190a_{18}X^2+20a_{19}X,
\]

with integral binomial-normalized coefficients, an exact triple root at
one, and \(a_2=a_{17}=0,a_3=-1\). Its residue is

\[
h=X^{20}-X^{17}-3X^2+3X.
\]

The mean residue zero is simple; one has multiplicity exactly three;
all other roots are simple. Indeed \(\gcd(h,h')=(X-1)^2\), and
\(H_3h(1)=1\). In an actual row-9 CA polynomial, every root reducing
to one is the exact triple root one, by the previously proved cluster
collapse. Every root reducing to zero is exactly zero.

Put \(C_j=\binom{20}{j}\). Solving only \(f(1)=f'(1)=0\) gives

\[
190a_{18}=18221-\sum_{j=4}^{16}(19-j)C_ju_j,
\qquad
20a_{19}=-17082+\sum_{j=4}^{16}(18-j)C_ju_j.
\tag{1}
\]

The determinant of these two linear equations is \(-3800\), a
17-adic unit. Both denominators 190 and 20 are units. All \(C_j\)
in this range are divisible by 17. Thus the resulting polynomial
\(f_u\) is over \(\mathbb Z_{(17)}[u_4,\ldots,u_{16}]\),
has the same residue \(h\) for **every** integral \(u\), and

\[
\frac{\partial f_u(X)}{\partial u_j}
=C_j\bigl(X^{20-j}-(19-j)X^2+(18-j)X\bigr)
\in17\mathbb Z_{(17)}[X].
\tag{2}
\]

This proves the required vanishing of all coefficient-parameter
derivatives after reduction, rather than assuming it from a fixed
numerical seed. The constants and all 13 derivatives in (1) were
independently checked by `check_row9_etale_constants.py`, normally and
under `python3 -O`.

## Residue assignments and the square subsystem

For \(4\le j\le16\), write

\[
G_j(X)=X^j-\binom j3X^{j-3}
+\sum_{i=4}^j\binom ji u_iX^{j-i}.
\]

This is the monic normalized derivative of degree \(j\), corresponding
to Hasse order \(20-j\). Let \(\rho_j\) be the residue of a selected
common witness. It is a root of the fixed polynomial \(h\).

Let \(E/\mathbb F_{17}\) be a finite splitting field of \(h\).
For any marked assignment \((\rho_4,\ldots,\rho_{16})\), the equations
\(\bar G_j(\rho_j)=0\) determine \(\bar u_j\) successively, because
the coefficient of \(u_j\) is one and only earlier coefficients occur.
Explicitly,

\[
\bar u_j=-\rho_j^j+\binom j3\rho_j^{j-3}
-\sum_{i=4}^{j-1}\binom ji\bar u_i\rho_j^{j-i}.
\tag{3}
\]

Consequently all residue parameters lie in \(E\). This is a proof of
finite-field containment over an arbitrary algebraically closed residue
field, not a finite-field enumeration assumption.

Fix such an assignment. Let \(J\) consist of those indices with
\(\rho_j\notin\{0,1\}\). Introduce an independent root variable
\(r_j\) for each \(j\in J\), even when two indices have the same
residue. Set \(w_j=0\) or 1 for the other indices, as specified by the
assignment, and \(w_j=r_j\) when \(j\in J\). Use the square system

\[
f_u(r_j)=0\quad(j\in J),\qquad
G_j(w_j)=0\quad(4\le j\le16).
\tag{4}
\]

There are \(|J|+13\) equations in that many variables. Every actual
row-9 CA point satisfies one such system. Choosing exact zero or one for
the special residue classes is justified by the already proved simple
mean and triple-cluster collapse. It would not be justified merely by
residue equality in an arbitrary branch.

## The Jacobian

Order variables as the root variables followed by \(u_4,\ldots,u_{16}\),
and order equations as in (4). The reduced Jacobian has block form

\[
\begin{pmatrix}D&0\\ B&L\end{pmatrix},
\qquad
D=\operatorname{diag}(h'(\rho_j))_{j\in J}.
\]

Every diagonal entry of \(D\) is nonzero because the corresponding
root of \(h\) is simple. The upper-right block is zero by (2).
Holding the root variables fixed, \(\partial G_j/\partial u_i=0\)
for \(i>j\), and \(\partial G_j/\partial u_j=1\). Thus \(L\)
is lower triangular with diagonal one. It follows that

\[
\det\bar J=\prod_{j\in J}h'(\rho_j)\ne0.
\tag{5}
\]

Repeated choices of the same residue do not change this conclusion:
each selected witness has its own root equation and variable, giving
another nonzero diagonal entry. The case \(J=\varnothing\) is also
covered, with determinant one.

## Why uniqueness excludes ramified deviations

Let \(K_E/\mathbb Q_{17}\) be the unramified extension with residue
field \(E\), and let \(R_E\) be its integer ring. The coefficients
of (4) lie in \(\mathbb Z_{(17)}\subset R_E\). Its specified residue
point lies in \(E\), and (5) is a unit determinant. Multivariate
Hensel lifting gives a solution in \(R_E\) with that residue point.
Concretely, choose any integral lifts of its coordinates and iterate
Newton's method. The inverse Jacobian stays integral; the equation
errors improve from \(17^n\) to \(17^{2n}\), and completeness
gives the solution.

The crucial uniqueness statement is stronger than uniqueness modulo
\(17R_E\) inside this one unramified ring. Suppose two integral
solutions in any common valued extension have the same residues and
their difference vector \(\Delta\) is nonzero. Set
\(r=\min_i\nu(\Delta_i)>0\). A matrix invertible over the valuation
ring preserves this minimum valuation, so the linear Taylor term
\(J\Delta\) has minimum valuation exactly \(r\). Every remaining
Taylor term has valuation at least \(2r>r\), since the polynomial
coefficients are integral. The linear term cannot cancel, contradicting
that both points solve (4). The two solutions are therefore equal.

For a hypothetical algebraic characteristic-zero counterexample, place
its coefficients and selected witnesses in a finite extension of
\(\mathbb Q_{17}\), and compare with the Hensel lift in a common
extension. They have the same residue point, so uniqueness identifies
them. Hence all \(u_j,r_j,a_{18},a_{19}\) belong to the unramified
field \(K_E\). No fractional coefficient or selected-witness
displacement has been silently discarded. The uniqueness proof itself
does not require a discrete value group or unramified ambient field.

The usual reduction from a complex counterexample to an algebraic
root-incidence point is enough here. One need not assume a prior
finiteness theorem for all CA polynomials.

## The remaining exact condition and scope

The square subsystem used only \(f(1)=f'(1)=0\), not the third
equation making the root triple. The additional condition is

\[
H_2f_u(1)=0,
\qquad\text{equivalently}\qquad
-8037+\sum_{j=4}^{16}\binom{19-j}{2}\frac{C_j}{17}u_j=0.
\tag{6}
\]

The latter equality follows by dividing the exact coefficientwise
17-divisible expression for \(H_2f_u(1)\) by 17. It is an additional
equation on the unique unramified lift, not part of the Jacobian proof.

All other Hasse common-root conditions are already enforced: orders
19 and 18 use zero; order 17 uses one; orders 16 through 4 use (4);
order 3 uses zero because \(a_{17}=0\); order 1 uses one by
\(f'(1)=0\). Thus satisfying (6) would complete the CA incidence
conditions for this row. Conversely every actual row-9 counterexample
must arise from one of these finitely many residue assignments and
its unique unramified lift satisfying (6).

This is a complete lifting reduction for this branch, but not a
completed search or exclusion. There are 18 distinct roots of \(h\),
so the naive marked-assignment bound is \(18^{13}\), with duplicates
and possible further reductions. The Jacobian argument does not make
that search small, does not show that (6) fails, and does not extend
unramifiedness to other rows without a separate proof.
