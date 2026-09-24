# Normalization, support reduction, and residue classification

For \(f=\sum c_iX^i\), let
\[
 H_kf=\sum_{i\ge k}\binom{i}{k}c_iX^{i-k}
\]
be its \(k\)-th Hasse derivative. In characteristic zero the ordinary derivative is \(k!H_kf\), so the common-root conditions agree. A CA polynomial shares a root with \(H_kf\) for every \(1\le k<\deg f\); it is nontrivial if it is not a scalar multiple of a power of a linear polynomial.

Translate the unique zero of \(H_{19}f\) to zero and make the degree-twenty polynomial monic. Its centered form is
\[
 f(X)=X^{20}+\sum_{j\in S}c_jX^{20-j},
 \qquad S\subseteq\{2,\ldots,19\},\quad c_j\ne0.
\]
The elements of \(S\) are deficiencies, not exponents. The number of nonzero terms is \(1+|S|\). A nonzero scaling of the variable preserves exact support.

## Algebraic specialization and integrality

An assumed solution over any characteristic-zero extension with an exact support can first be replaced by an algebraic solution with that support. Encode the common witnesses by polynomial equations over \(\mathbf Q\), and adjoin an inverse to the product of the coefficients required to be nonzero. The resulting ideal is proper if such a solution exists. A maximal ideal over \(\overline{\mathbf Q}\) gives an algebraic point, preserving the exact support. This operation precedes choosing a valuation; it is not asserted to preserve a preselected valuation stratum of a transcendental point.

Fix a prime \(p\), extend its valuation to a number field containing all coefficients and roots, and choose a nonzero root of least valuation. Scale that root to one. All roots are then integral and the reduction has a unit root. Write
\[
 f=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
 \qquad a_0=1,\quad a_1=a_{20}=0.
\]
The normalized derivative of degree \(j\) is monic:
\[
 G_j(X)=\frac{H_{20-j}f(X)}{\binom{20}{j}}
       =\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]
At its integral common witness, the coefficient-one term \(a_j\) is an integral expression in earlier coefficients. Induction proves all \(a_j\) integral. This justifies coefficient reduction even when the binomial multiplier is divisible by \(p\). No exact coefficient is inferred to vanish merely because its residue vanishes.

We use the degree-\(p+1\) mean-root and determinant restrictions of Castryck, Laterveer and Ounaïes [CLO] at \(p=19\). In particular the mean is a simple root, so the ordinary linear coefficient is nonzero. Their determinant condition, with the singleton and two-visible-coefficient tests reproduced in Appendix A, gives the finite support step below. All subsequent local arguments allow arbitrary finite ramification.

## The fourteen possible seven-term supports

Appendix A proves that every nontrivial centered degree-twenty CA polynomial has at least seven terms. To improve that bound, it remains to exclude exact supports with six deficiencies. The nonzero linear coefficient leaves \(\binom{17}{5}=6188\) such supports. The singleton visibility tests at primes \(2,3,5,7,11,13,17,19\) leave 586. The two-visible-coefficient test leaves 348, and the CLO determinant leaves fourteen.

For precision, if \(J\subseteq\{2,\ldots,18\}\) is the complement of a proposed support, the determinant used modulo 19 is that of the matrix with rows
\[
 \bigl(-1,\;j\binom{j-2}{k-2}\ (k\in J)\bigr),\qquad j\in J,
\]
where the binomial entry is zero for \(k>j\), and final row
\[
 \bigl(-1,\;(-1)^k\ (k\in J)\bigr).
\]
It must vanish. The new bounded enumeration forms these matrices directly and performs Gaussian elimination. A separate reconstruction uses exact Bareiss determinants. Both give the same fourteen supports. The extra Massri support filter used in historical code removes none of the 348 and is not a dependency of this enumeration. No previously proved closed mask is needed to obtain the fourteen-entry list.

The following table also records the compatible characteristic-seventeen seeds before the exact-root restriction on row 4 is applied.

| Label | Exact deficiency support | Compatible seed rows |
|---|---|---|
| \(S_1\) | \(\{2,3,4,10,12,19\}\) | 5, 8 |
| \(S_2\) | \(\{3,4,9,10,12,19\}\) | 8 |
| \(S_3\) | \(\{3,4,5,10,13,19\}\) | 8 |
| \(S_4\) | \(\{3,4,10,12,15,19\}\) | 8 |
| \(S_5\) | \(\{3,7,9,10,16,19\}\) | 8 |
| \(S_6\) | \(\{3,6,10,16,17,19\}\) | 1, 8 |
| \(S_7\) | \(\{7,8,10,16,17,19\}\) | 1 |
| \(S_8\) | \(\{10,12,13,16,17,19\}\) | 1 |
| \(S_9\) | \(\{6,10,15,16,17,19\}\) | 1 |
| \(S_{10}\) | \(\{9,10,15,16,17,19\}\) | 1 |
| \(S_{11}\) | \(\{2,4,10,12,18,19\}\) | 4 |
| \(S_{12}\) | \(\{3,4,10,13,18,19\}\) | 8, 9 |
| \(S_{13}\) | \(\{2,4,10,17,18,19\}\) | 1, 2, 4 |
| \(S_{14}\) | \(\{4,10,16,17,18,19\}\) | 1 |

The executable enumeration and its independent audit are in `research/next-stage/coverage/`. The list is a necessary-condition cover; it makes no assertion that any listed support is realizable.

## Classification over the full residue-field closure

At 17 the visible model is
\[
 h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX.
\]
The residue-field scaling used below lifts to a unit after a finite extension. The resulting change of variable preserves centering, integrality and exact support. Up to nonzero scaling and monic normalization, every nonmonomial Hasse-CA polynomial in this model over \(\overline{\mathbf F}_{17}\) is represented by the following table:

| Row | \(a\) | \(b\) | \(c\) | \(d\) | \(e\) |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 16 | 0 | 0 |
| 2 | 14 | 0 | 16 | 0 | 3 |
| 3 | 14 | 8 | 16 | 12 | 0 |
| 4 | 14 | 0 | 0 | 11 | 8 |
| 5 | 14 | 2 | 0 | 0 | 0 |
| 6 | 14 | 2 | 0 | 11 | 6 |
| 7 | 14 | 2 | 0 | 14 | 3 |
| 8 | 0 | 16 | 0 | 0 | 0 |
| 9 | 0 | 16 | 0 | 14 | 3 |

The entries lying in \(\mathbf F_{17}\) are a conclusion of the classification, not an assumption about a candidate's residue field. Here is the chart cover and the finite certificate used to establish it. Put
\[
 U=X^{17}+c,\quad V=X^3+aX+b,\quad
 Q=dX^2+(e-ac)X-bc.
\]
Then
\[
\begin{aligned}
h&=UV+Q,& H_3h&=U,&H_{17}h&=V,\\
H_2h&=3XU+d,&H_{18}h&=3X^2+a,&H_{19}h&=3X,\\
H_1h&=(3X^2+a)U+2dX+e-ac.
\end{aligned}
\]
Every other derivative has zero constant coefficient and shares zero with \(h\).

If \(c\ne0\), normalize the common \(H_3\) root to one. Then \(c=-1\), \(e=-a-b-d\), and \(Q=(X-1)(dX-b)\). A common \(H_{17}\) root gives a complete cover by the following extended polynomial charts:
\[
 (a,b,d)=(s,0,t),\quad(-1-s,s,t),\quad(-s^2-t,st,t).
\]
The last chart covers a witness different from one; the required divisions are made only in its nonzero branch, and its polynomial extension includes all boundary overlaps. In each chart form the three resultants of \(h\) with \(H_{18}h,H_2h,H_1h\). Their leading coefficients in \(X\) are nonzero constants, so resultant vanishing is equivalent to existence of a common root in every specialization.

The supplied ideal-membership certificates give the following consequences. In the first chart the ideal contains
\[
 t^{20},\qquad s^{20}-3s^{11}t-2s^2t^2+3s^3-8s^2t-6st^2.
\]
Thus \(t=0\) and \(s^3(s+3)^{17}=0\), yielding rows 1 and 2. The second chart's ideal contains 1. In the third chart it contains
\[
 t^{20}(t+5),\quad t^{20}(s+5),\quad P(s,t),
\]
where the degree-forty target \(P\), with all coefficients supplied in the certificate, satisfies
\[
 P(s,0)=s^{40}-3s^6=s^6(s^2-3)^{17}.
\]
The branch \(t=0\) again gives rows 1 and 2; otherwise \(s=t=-5\), giving row 3.

If \(c=0,a\ne0\), normalize an \(H_{18}\) common root to one, so \(a=-3\), \(b=s,d=t,e=2-s-t\). The ideal of the resultants with \(H_{17}h,H_2h,H_1h\) contains
\[
 [s(s-2)]^{19},\quad [st+6s-2t+5]^{19},\quad
 [t(t-11)(t-14)]^{18}.
\]
These force \((s,t)=(0,11),(2,0),(2,11),(2,14)\), giving rows 4–7.

If \(c=a=0,b\ne0\), normalize an \(H_{17}\) common root to one. Then \(b=-1,e=-d\). For \(d=0\) we obtain row 8. Otherwise an \(H_2\) witness \(r\ne0\) gives \(d=-3r^{18}\) and
\[
-r^{16}(r-1)^2(2r+1)=0.
\]
The two possibilities give \(d=14,12\). The latter has \(\gcd(h,H_1h)=1\); the former is row 9. If \(c=a=b=0,d\ne0\), normalization gives \(d=-3,e=2\). A common \(H_1\) root must satisfy \(3r-4=0\), hence \(r=7\), but \(h(7)/7=1\). Finally \(c=a=b=d=0,e\ne0\) is excluded by \(H_1h-3h/X=-2e\). The all-zero tuple is the monomial, already excluded by the retained unit root.

All ideal-membership identities are checked coefficientwise in `evidence/full/support_frontier/prime17/check_classification.py`. The resultants themselves are independently verified by exact interpolation over \(\mathbf F_{17}[\alpha]/(\alpha^2-3)\), using explicit bidegree bounds. The maximum bounds are \((78,39)\); all coordinate grids fit within the 289-element field. The 12,895 evaluations on complete rectangular grids establish polynomial identity, rather than merely testing rational points. Direct gcd checks confirm that all retained representatives satisfy the required conditions. The certificate arrays and complete degree table are included in the same directory.

## Exact zeros forced by a simple mean

A useful restriction is stronger than a residue coefficient being zero. If the reduced mean is simple, the only actual root reducing to zero is the exact root zero: write \(f=Xq\) with \(q(0)\) a unit. If \(\gcd(\bar f,H_k\bar f)\) is a power of \(X\), its actual common witness is therefore zero, and the ordinary coefficient of \(X^k\) vanishes exactly.

In row 4 the mean is simple and the common \(H_3\) residue is only zero. Thus \(a_{17}=0\) exactly. This removes row 4 from \(S_{13}\), which has \(a_{17}\ne0\). It does not remove \(S_{11}\), whose row-4 lifting obstruction is treated separately. This distinction prevents a zero residue from being used as an unjustified exact-zero condition.

## A recurring precision principle

**Lemma 3 (unit-Jacobian precision).** Let \(\mathcal O\) be the valuation ring of a nonarchimedean valued field, let \(F\in\mathcal O[X_1,\ldots,X_n]^n\), and let \(x,x_0\in\mathcal O^n\) have the same residue. Suppose \(F(x)=0\), \(\det DF(x_0)\) is a unit, and every coordinate of \(F(x_0)\) has valuation at least \(q>0\). Then every coordinate of \(x-x_0\) has valuation at least \(q\). The conclusion remains valid over the extended valuation ring in any valued field extension.

**Proof.** If the minimum coordinate valuation \(r\) of \(x-x_0\) were less than \(q\), then \(r>0\). Multiplication by the integral matrix \(DF(x_0)\) with integral inverse preserves that minimum valuation. In the Taylor equation, the constant term has valuation at least \(q\), and all terms of degree at least two in the difference have valuation at least \(2r>r\). They cannot cancel a linear coordinate of valuation \(r\). This contradiction proves the claim without assuming an integer-valued valuation. \(\square\)

Whenever this principle is used below, the local argument supplies the polynomial system, common residue, unit Jacobian and required residual precision. It does not assert that an arbitrary candidate belongs to an unramified coefficient field.
