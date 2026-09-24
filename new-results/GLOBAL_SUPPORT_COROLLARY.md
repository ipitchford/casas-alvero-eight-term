# Global exclusion of the centered support {2,4,10,12,18,19}

24 September 2026. This corollary assembles the existing complete
characteristic-17 seed classification and the existing row-4 support
exclusion. It introduces no new census or lifting computation.

**Corollary.** No nontrivial characteristic-zero degree-20 Casas–Alvero
polynomial has exact centered deficiency support
\[
S=\{2,4,10,12,18,19\}.
\]
Equivalently, after centering the mean root at zero and making the
polynomial monic, there is no CA polynomial of the form
\[
X^{20}+c_2X^{18}+c_4X^{16}+c_{10}X^{10}
+c_{12}X^8+c_{18}X^2+c_{19}X,
\qquad \prod_{j\in S}c_j\ne0.
\]
The leading term is not counted in the deficiency set: this is one exact
seven-monomial support. The assertion is not conditional on already
belonging to row 4.

## Proof

Write
\[
f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\quad a_0=1,\quad a_1=a_{20}=0.
\]
The condition \(a_1=0\) is centering. The CA condition for the nineteenth
derivative makes its root zero a root of \(f\), giving \(a_{20}=0\).
Ordinary and binomial-normalized coefficients have the same exact zero
pattern in characteristic zero.

First reduce to algebraic coefficients. The coefficients and nineteen
chosen common-root witnesses satisfy polynomial equations over
\(\mathbb Q\). Add the equations \(a_j=0\) for every \(j\notin S\),
apart from \(a_0=1\), and
\[
v\prod_{j\in S}a_j=1.
\]
A solution over any characteristic-zero extension makes this ideal
proper; the weak Nullstellensatz supplies a point over
\(\overline{\mathbb Q}\). This retains exact support, not only containment.
It therefore suffices to exclude algebraic points.

Choose a valuation above 17, extend to a field containing all roots,
and divide the variable by a nonzero root of minimum valuation:
explicitly replace \(f(X)\) by \(f(\lambda X)/\lambda^{20}\).
All roots are now integral and one root is exactly one. This operation
sends \(a_j\) to \(a_j/\lambda^j\), so it preserves every exact zero
and nonzero coefficient. No translation is made after centering.

The normalized monic derivatives are
\[
G_j(X)=\frac{H_{20-j}f(X)}{\binom{20}{j}}
=\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]
Every \(G_j\) has a common root \(w_j\) with \(f\); the witness \(w_j\)
is integral. Induction in \(j\), using the coefficient one on \(a_j\),
proves \(a_j\) integral. This step is necessary because ordinary
coefficient integrality alone would not justify Lucas visibility.

For \(4\le j\le16\), the integer \(\binom{20}{j}\) is divisible by
17. All other nonleading coefficients absent from \(S\) vanish exactly.
Thus the reduction has the visible form
\[
h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX
\quad\text{with }b=c=0.
\]
Reducing the ordinary Hasse common-root equations proves that \(h\)
is Hasse–CA. In particular the visible derivatives retain their
common-root identities; the Hasse orders 4 through 16 vanish identically
on the visible model. The reduction is not \(X^{20}\), because the
retained exact root one reduces to a nonzero root.

The complete algebraic-closure classification has nine nonmonomial rows
up to nonzero variable scaling. Only row 4 has both \(b=c=0\).
This remains true if \(a_2,a_{18}\), or \(a_{19}\) initially has positive
valuation; none of those coefficient residues was assumed nonzero.
Indeed, the coefficient-zero boundary charts are included in the
classification, and their only additional all-zero tuple is the already
excluded monomial.

Lift a classification scaling to a unit, extending the local field if
necessary. The resulting reduction is
\[
h=X^{20}-3X^{18}+11X^2+8X.
\]
Centering and exact support are still unchanged. At this stage
\(\bar a_2=-1\). Choose an actual common root \(z\) of \(f\) and
\(G_2=X^2+a_2\). Its reduction is \(1\) or \(-1\). In the row-4 seed,
\[
h(1)=0,\qquad h(-1)=1.
\]
Therefore \(z\) reduces to one and is a unit. Scaling by this actual
witness leaves the residue seed unchanged and gives
\[
a_2=-1,\qquad a_3=a_{17}=0
\]
exactly. The active middle indices are precisely \(J=\{4,10,12\}\).

This is the exact family excluded by the existing row-4 smallest-support
theorem. Its complete residue census retains all seventeen nonzero
witness residues, both critical-root orientations, and active
coefficients whose residues vanish. Its two residue survivors have
simple selected witness classes and a unit lifting Jacobian. The final
critical-value certificate is
\[
f(R)=17^2(9+4\alpha)\pmod{17^3},
\qquad \alpha^2+3\alpha+3=0,
\]
which is nonzero. The theorem's analytic division and uniqueness
arguments permit arbitrary ramified valued extensions. Thus the
normalization above falls within its proved scope and is impossible.
This excludes the algebraic specialization and hence the original
characteristic-zero point. \(\square\)

## Exact dependencies and verification boundary

1. [Complete seed classification](../evidence/full/support_frontier/prime17/CLASSIFICATION.md):
   classification over the whole algebraic closure, with coefficient-zero
   charts and monomial retained separately. Its certificate checker and
   [independent mathematical audit](../evidence/full/literature/PRIME17_CLASSIFICATION_AUDIT.md)
   validate completeness; checking only the nine displayed examples
   would not suffice.
2. [Normalization and integrality](../evidence/full/LIFT_CONSEQUENCES_17.md):
   the recurrence proof is reproduced above. The general simple-mean
   argument is not an extra bridge needed to select row 4, whose mean
   residue root is already simple.
3. [Row-4 smallest-support exclusion](../evidence/full/tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md):
   the local computational theorem for \(J=\{4,10,12\}\), together with
   its [separate audit](../evidence/full/tame17/ROW4_SMALLEST_SUPPORT_AUDIT.md)
   and standard-library checker.

The corollary's normalization and support-preservation bridge received
a separate bounded algebraic audit. No existing evidence files were
modified and no large computation was rerun.

This does not exclude the whole row-4 branch, every seven-term support,
or degree 20. It does not assert the same conclusion merely from support
containment, and makes no claim about priority or an assessment grade.
