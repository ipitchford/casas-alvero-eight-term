# Characteristic-zero consequences of the nine characteristic-17 seeds

23 September 2026. These results apply to the unrestricted degree-20
problem. They do not exclude all characteristic-zero lifts. Row numbers
refer to `support_frontier/prime17/CLASSIFICATION.md`.

## Normalization and a cross-prime input

It suffices to consider an algebraic counterexample: a nontrivial complex
point of the polynomial root-incidence equations implies an algebraic point
after nontriviality is enforced by an inverse variable. Center the mean
root at zero. Scale a nonzero root of minimum 17-adic valuation to one;
then all roots are integral. Write

\[
f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},\qquad
a_0=1,\quad a_1=a_{20}=0.
\]

The common-root equations for the monic derivatives
\(G_j=\sum_{i=0}^j\binom ji a_iX^{j-i}\) show inductively that all
\(a_j\) are integral. Lucas visibility and the retained unit root put
the reduction into one of the nine nonmonomial seeds. The additional
scalings in that classification use unit derivative witnesses and preserve
integrality.

[CLO, Theorem 2](https://arxiv.org/html/1208.5404#S1.Thm2), applied with
\(20=19+1\), says that the exact mean root of a hypothetical nontrivial
characteristic-zero degree-20 CA polynomial is simple. This statement
is independent of the valuation used subsequently. Hence the exact root
zero remains simple in the 17-adic normalization as well.

For this degree the needed assertion also has a short direct proof. If the
mean root were multiple, its linear coefficient would vanish, so
\(a_{19}=0\). Repeat the integral normalization above at the prime 19.
Every \(\binom{20}{j}\) with \(2\le j\le18\) is divisible by 19;
the centered and constant coefficients vanish as well. The reduction would
therefore be \(X^{20}\), contradicting the retained unit root. This
recovers the cited special case without requiring any stronger part of
the source's theorem.

## Row 3 is entirely excluded

Its reduction is

\[
h=X^{20}+14X^{18}+8X^{17}+16X^3+12X^2.
\]

The exact finite-field computation gives
\(\gcd(h,H_1h)=X\), and zero has multiplicity exactly two in \(h\).
Let \(r\) be a common root of \(f\) and \(f'\). Its reduction must
therefore be zero. The simple-mean theorem gives \(r\ne0\).
Consequently \(X(X-r)^2\) divides \(f\). All roots are integral,
so the remaining monic factor is integral. Reducing this factorization
forces \(X^3\mid h\), a contradiction.

This excludes the whole row, including every invisible normalized
coefficient and every ramified root displacement. It is not a statement
that the corresponding finite-field seed fails the Hasse-CA conditions;
that seed does satisfy them.

Independent review: `literature/PRIME17_ROW3_LIFT_AUDIT.md`.

## Row 9 has an exact triple root and two exact coefficient zeros

Here

\[
h=X^{20}+16X^{17}+14X^2+3X.
\]

Its root at one has multiplicity exactly three. The monic gcds with
\(H_1h,H_2h,H_{17}h\) are respectively
\((X-1)^2,X-1,X-1\). Thus the common witnesses for Hasse orders one
and two lie in that three-root cluster.

The cluster-collapse lemma in `two_adic/CLUSTER_COLLAPSE.md` applies:
if the roots did not all coincide, zooming by the least valuation of a
nonzero difference would produce a nontrivial degree-three Hasse-CA
polynomial in characteristic 17. Such a polynomial cannot exist. Indeed,
after centering it has the form \(Y^3+uY\); its common Hasse-first-
derivative root is nonzero if \(u\ne0\), and then the two equations
\(r^2+u=0\), \(3r^2+u=0\) contradict \(2r^2\ne0\).
The three roots therefore coincide exactly.

Zero is simple in this residue polynomial. The pure-zero gcds for Hasse
orders three and eighteen force the corresponding exact witnesses to be
zero, so the coefficients of \(X^3\) and \(X^{18}\) in \(f\) vanish
exactly: \(a_{17}=a_2=0\). The Hasse-order-seventeen witness is the
triple root. Normalize it to one. Since \(G_3=X^3+a_3\), we obtain
\(a_3=-1\) exactly. Thus this branch satisfies

\[
(X-1)^3\mid f,\qquad a_2=a_{17}=0,\qquad a_3=-1.
\]

In ordinary coefficients, the coefficient of \(X^{17}\) is
\(-\binom{20}{3}=-1140\). These conditions restrict row 9; they do
not exclude it.

## Further exact restrictions

The independent all-nineteen-gcd check in
`literature/PRIME17_CLASSIFICATION_AUDIT.md` yields these restrictions.
The notation here is the binomial-normalized deficiency notation above.

| Rows | Exact conditions after the indicated unit-witness normalization |
|---|---|
| 4 | \(a_2=-1,\ a_3=a_{17}=0\) |
| 6, 7 | \(a_2=-1,\ a_3=2,\ a_{17}=0\) |
| 9 | \(a_2=a_{17}=0,\ a_3=-1\), with an exact triple root at one |

For rows 6 and 7, the Hasse-order-seventeen and eighteen gcds are both
\(X-1\), and one is a simple root of \(h\). Their exact witnesses
must coincide. Normalize that root to one; then \(G_2(1)=G_3(1)=0\)
gives \(a_2=-1,a_3=2\). In row 4 the Hasse-order-seventeen witness
is instead the exact mean root, giving \(a_3=0\). All these rows have
the Hasse-order-three witness at their simple mean root, giving
\(a_{17}=0\).

The remaining rows are 1, 2, 4, 5, 6, 7, 8 and 9. No characteristic-zero
lift has been constructed, and none of these eight complete branches has
been excluded by the arguments in this note.
