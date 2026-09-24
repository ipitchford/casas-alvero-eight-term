---
title: "An eight-term bound for degree-twenty Casas–Alvero polynomials"
subtitle: "Wild root clusters and exact lifting obstructions — unrefereed preprint"
date: "24 September 2026"
author: "Anonymous"
lang: en-GB
---

# Abstract {.unnumbered}

We prove that a nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least eight nonzero monomials after centering at the common root of its nineteenth derivative. Published arithmetic restrictions reduce the seven-term case to fourteen exact coefficient supports. A complete characteristic-seventeen seed classification and ramification-safe lifting arguments exclude every compatible branch. The new local arguments include a uniform second-jet obstruction, forced collisions in a seventeen-root cluster, a quadratic residue obstruction with controlled precision, and a separated-cluster reduction to the quartic Casas–Alvero theorem in characteristic seventeen. The proof retains coefficient degeneration and arbitrary ramified extensions. Exact certificates and independent arithmetic reconstructions accompany the finite calculations, while the earlier exclusion of six or fewer terms is included in full. This is a completed sparsity theorem; it does not prove the unrestricted degree-twenty case or the general conjecture.

**Keywords:** Casas–Alvero conjecture; sparse polynomials; Hasse derivatives; nonarchimedean root clusters; exact computation.

# Introduction

The Casas–Alvero condition requires a polynomial to share a root with each of its nonconstant proper derivatives. The conjecture asserts that, in characteristic zero, every such polynomial is a power of a linear polynomial. We study the coefficient support of a hypothetical counterexample of degree twenty.

**Theorem 1 (eight-term bound).** After translating the root of its nineteenth derivative to zero, every nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least eight nonzero monomials, including its leading term.

The centering in the statement is essential: we do not assert the same monomial count for every translate. The theorem is a sparsity restriction, not a proof of the conjecture in degree twenty, and it does not assert that the bound is sharp.

The proof has two parts. Arithmetic restrictions reduce a seven-term candidate to fourteen exact supports. We exclude every compatible residue branch of these supports, using a complete classification of the characteristic-seventeen visible model and local lifting arguments. An earlier stage of the argument excludes six or fewer terms; its full proof is retained in Appendix A, including the characteristic-thirteen calculation for the last six-term family. The final fourteen-support enumeration is reproduced independently and does not require the extra support filter present in historical code.

The local arguments retain coefficients that are nonzero but have zero residue, and they allow arbitrary ramification. This matters because a nonempty special fibre is not itself evidence of a characteristic-zero counterexample, and a search for lifts in an unramified ring need not cover all candidates. The proofs instead control every actual common-root witness through valuations, multiplicities, and exact integer identities.

Three mechanisms are useful beyond the individual support list. First, a uniform theorem excludes a specified residue stratum while allowing all its intermediate coefficient positions to be active. A common derivative root is forced to equal a repeated root; their next nonzero jets are incompatible. Second, a shared second-order calculation excludes two quadratic-coefficient families by a nonsquare discriminant, with the precision justified by a unit Jacobian. Third, in the last residue branch, the first nontrivial cluster model forces all low-order witnesses into a four-root cluster. The characteristic-seventeen quartic CA theorem collapses that cluster, after which a simple-root lift has a nonzero residual. These are local statements with explicit hypotheses, not a degree-uniform exclusion theorem.

Prime-adic constraints and determinant restrictions were developed by Castryck, Laterveer and Ounaïes [CLO]. De Frutos Marín's singleton and two-visible-position criteria [deFrutos] provide part of our support sieve; their combination with the published restrictions already gives the weaker five-term bound, which is not claimed as new. Massri [Massri] gives related witness-placement and perturbation methods, including a theorem about three recycled roots in degree twenty. A bound on the number of recycled roots is distinct from a bound on the number of nonzero coefficients. Marashdeh [Marashdeh] develops related triangular support reductions. Our contribution is the complete exclusion beyond the imported restrictions, not the introduction of reduction modulo a prime, Hensel lifting, or Newton polygons.

Ramification also has a precedent in [CLO]: the remark following Proposition 19 excludes degree-\(p+1\) candidates whose roots lie in an extension unramified at \(p\). Our degree-twenty characteristic-seventeen arguments impose no such condition on the candidate's field. The controlled-field argument retained in the supplement is an alternative proof on a narrower stratum; the direct jet proof in the main text is shorter and covers its missing boundary.

The primary-source comparison found no exact predecessor of the eight-term statement in the inspected material. This is a bounded comparison, not unconditional priority clearance. Two specific source questions remain: the equivalence of the systems behind ProofAtlas's reported degree-twenty work, and the unavailable full text of Shih, Cheng-Pang's 2022 thesis. The comparison and its limits are recorded in the review supplement. Ghosh [Ghosh, version 2, 21 March 2026, Theorem A] claims the full characteristic-zero conjecture in all degrees. That unrefereed claim is not a premise of this paper. The supplementary audit concerns a positive-characteristic auxiliary assertion in that argument; such an objection does not by itself refute its characteristic-zero conclusion. We retain the priority qualifications above.

All finite checks used below have explicit input families, complete residue domains, and precision-transfer arguments. The accompanying archive contains the integer certificates, independent reconstructions, and executable replay. The resulting manuscript is a computer-assisted proof for review; its internal audits are neither external refereeing nor proof-assistant certification.

## Structural dependency map

| Result | Hypotheses and role | Uses |
|---|---|---|
| Theorem 1 | Centered nontrivial degree twenty; at least eight terms | Appendix A for fewer terms; complete fourteen-support cover for seven terms |
| Theorem 2 | Degree twenty, prime seventeen, exact and residue coefficient conditions displayed in its statement | Integral normalization, root multiplicities, exact second jet |
| Lemma 3 | Integral polynomial system, unit Jacobian and residual precision | Transfers finite precision to arbitrarily ramified candidates |
| Lemma 4 | A separated cluster of size \(m\), all derivative witnesses through \(m-1\), and the residue-field CA property in degree \(m\) | Collapses the cluster exactly; applied with \(m=4\), residue characteristic seventeen |

Theorem 2 is uniform in coefficient choices within its stated degree-twenty stratum, not across degrees. Lemmas 3 and 4 isolate standard reusable reasoning; the new contribution is the complete application and resulting support bound. The closing support table supplies the remaining case-specific implications.


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


# A uniform obstruction in the first residue stratum

Write \(\nu(17)=1\), and use the binomial-normalized coefficients \(a_j\). All residue statements in this section concern an algebraic closure of \(\mathbf F_{17}\).

**Theorem 2 (uniform obstruction with unit coefficient \(a_{16}\)).** There is no nontrivial degree-twenty CA polynomial satisfying
\[
 \bar f=X^{20}-X^3,\qquad a_2=a_{18}=0,\qquad
 \bar a_4=\cdots=\bar a_{15}=0,\qquad \bar a_{16}=-1.
\]
The coefficient \(a_3\), which necessarily has zero residue, may vanish or be nonzero. Any or all of the intermediate coefficients may be nonzero. The statement permits arbitrary ramification.

## Small roots and coefficient precision

The common \(H_3\) root is a unit reducing to one. Scale it exactly to one. Put \(t=a_3\), \(u=a_{16}\), and \(C_j=\binom{20}{j}\). The equalities \(f(1)=H_3f(1)=0\) give
\[
\begin{aligned}
f={}&X^{20}+1140tX^{17}
 +\sum_{j=4}^{15}C_ja_jX^{20-j}
 +4845uX^4+DX^3+EX,\\
D={}&-1140-775200t
 -\sum_{j=4}^{15}\binom{20-j}{3}C_ja_j-19380u,\\
E={}&-1-1140t-\sum_{j=4}^{15}C_ja_j-4845u-D.
\end{aligned}
\]
The mean is simple by the degree-\(19+1\) mean-root restriction [CLO], so \(E\ne0\). The residue-zero cluster consists of zero and two nonzero roots. Since \(D\) is a unit and every other nonconstant term of \(f(q)/q\) has valuation greater than \(2\nu(q)\), both nonzero small roots have valuation
\[
\delta=\tfrac12\nu(E).
\]
They are not repeated: in \(f'(q)-f(q)/q\), the term \(2Dq^2\) is uniquely lowest. Every repeated root therefore belongs to the seventeen-root cluster at one.

If \(t=0\), the formula for \(E\) gives \(\delta\ge1/2\). If \(t\ne0\), a common root of \(G_3=X^3+t\) is nonzero and small, so \(\nu(t)=3\delta\). The same formula for \(E\) implies
\[
2\delta\ge\min(1,3\delta),
\]
which again forces \(\delta\ge1/2\). In both cases \(\nu(t)\ge3/2\), with \(\nu(0)=+\infty\). The specified residues now give
\[
\overline{E/17}=11,
\qquad \delta=1/2.
\]
If \(t\ne0\), its valuation is exactly \(3/2\).

For \(4\le j\le15\), the common root selected by \(G_j\) reduces to zero. If \(a_j=0\), choose zero itself. Otherwise choose a nonzero small root. Induction in the triangular equations for \(G_j\) yields
\[
\nu(a_j)\ge j/2\qquad(4\le j\le15).
\]
Since \(\nu(C_j)=1\) on these indices, their contributions to \(f\), \(D\), \(E\), and the ordinary derivatives have valuation at least three.

## A forced repeated-root collision

Choose a common root \(x\) of \(f\) and \(G_{16}\). Its residue is one, and
\[
u=-x^{16}-560t x^{13}+e,\qquad \nu(e)\ge2.
\]
Write \(f(1+Y)=\sum c_kY^k\). Direct expansion gives
\[
\begin{aligned}
c_1&=17(-133-1425u)-1532160t+e_1,\\
c_2&=17(-190-1710u)-2170560t+e_2,\\
c_3&=0,\\
c_4&=4845(1+u)+2713200t+e_4,
\end{aligned}
\]
where each error has valuation at least three. Further,
\[
c_k\in17\mathcal O\ (5\le k\le16),\qquad
(c_{17},c_{18},c_{19},c_{20})=(1140(1+t),190,20,1).
\]
In particular \(\nu(c_2)=1\) and \(\overline{c_2/17}=7\).

First suppose \(t=0\), and put \(\epsilon=\nu(x-1)\). If \(0<\epsilon<1\), the only possible lowest terms in \(f(x)/(x-1)\) have valuations \(1+\epsilon\) and \(16\epsilon\). Their initial coefficients are respectively 10 and 1 after the indicated scaling. They must cancel, giving \(\epsilon=1/15\). If \(\epsilon\ge1\), including \(x=1\), then \(\nu(c_1)\ge2\). There are fifteen simple outer roots of displacement valuation \(1/15\), with nonzero initial roots satisfying \(Y^{15}+7=0\), and an inner cluster of multiplicity two containing one and \(x\). A repeated root must belong to that inner cluster. Counting multiplicities forces it to equal \(x=1\).

Now suppose \(t\ne0\). The same balance applies when \(0<\epsilon<1/2\), because \(\nu(t)=3/2>1+\epsilon\), and again forces \(\epsilon=1/15\). For finite \(\epsilon>1/2\), the term \(-1532160t\) gives \(\nu(c_1)=3/2\), uniquely lowest in the divided-root equation. This is impossible. If \(\epsilon=1/2\), that equation forces \(\nu(c_1)=3/2\); the Newton polygon then has fifteen simple outer roots, the simple exact root one, and one simple inner root of displacement valuation \(1/2\). There is no repeated root. The same description holds at \(x=1\), where again \(\nu(c_1)=3/2\).

It remains to consider \(\epsilon=1/15\). Choose \(\pi^{15}=17\), and set \(\xi=\overline{(x-1)/\pi}\). The initial polynomial is
\[
L(Y)=Y^{17}+7Y^2+3\xi Y,
\qquad \xi^{15}=7.
\]
This describes the entire seventeen-root cluster: a root with smaller positive displacement valuation would make the degree-seventeen term uniquely lowest in the divided-root equation. The only multiple root of \(L\) is \(\xi\), and it has multiplicity two, since \(L'=14Y+3\xi\) and \(H_2L=7\). Its cluster already contains \(x\) and must contain the repeated root of \(f\). Thus that repeated root equals \(x\) exactly.

## The second-jet contradiction

Substituting the \(G_{16}\) equation into \(f'(x)-f(x)/x=0\) gives
\[
Q_0(x)+tQ_1(x)+e_Q=0,\qquad \nu(e_Q)\ge3,
\]
where
\[
\begin{aligned}
Q_0(X)&=-14516X^{19}+38760X^{18}-2280X^2,\\
Q_1(X)&=-8121360X^{16}+21705600X^{15}-1550400X^2.
\end{aligned}
\]
The error from substituting \(u\) acquires the ordinary binomial multiplier \(4845\), of valuation one. This explains why its precision is three, not two.

Write \(Q_0(1+z)=\sum q_kz^k\). Exact binomial expansion yields
\[
\begin{gathered}
\nu(q_0)=\nu(q_1)=2,\qquad
\nu(q_2)=1,\quad \overline{q_2/17}=1,\\
\nu(q_k)\ge1\quad(3\le k\le16),\qquad
\bar q_{17}=2.
\end{gathered}
\]
The coefficients \(q_{18},q_{19}\) are integral. At \(\nu(z)=1/15\), only \(q_2z^2\) and \(q_{17}z^{17}\) can be lowest. Dividing their sum by \(\pi^{17}\) gives
\[
\xi^2+2\xi^{17}=\xi^2(1+2\cdot7)=15\xi^2\ne0.
\]
Hence \(\nu(Q_0(x))=17/15\), strictly below both \(\nu(tQ_1(x))\ge3/2\) and \(\nu(e_Q)\ge3\). Cancellation is impossible. In the remaining case \(t=0,x=1\), instead
\[
Q_0(1)=21964=17^2\cdot76
\]
has valuation two, again strictly below the error. This proves Theorem 2.

The finite identities are reconstructed using integer arithmetic in `research/next-stage/last-four/boundary/check_direct_jet.py`; a separate reconstruction is in the adjoining evidence. Neither checker supplies the root-cluster argument in place of the proof above. The earlier Bézout and controlled-ramification proofs in the supplement remain alternative proofs on narrower hypotheses.


# Two mixed middle-coefficient configurations

This section excludes the two centered deficiency supports
\[
S_A=\{10,12,13,16,17,19\},\qquad
S_B=\{9,10,15,16,17,19\}.
\]
The characteristic-seventeen seed classification, applied to the exact zeros
\(a_2=a_3=a_{18}=0\), leaves only the seed
\[
\bar f=X^{20}-X^3=X^3(X-1)^{17}.
\]
We give the local argument completely. Together with the unit-\(16\)
obstruction proved earlier, it excludes both supports.

Write \(\nu(17)=1\), let \(\mathcal O\) be the valuation ring, and put
\(\nu(0)=+\infty\). All coefficients and roots have been made integral by the
valuation normalization. We may extend the field whenever necessary; no
assumption on its ramification is imposed. The selected common root for the
third Hasse derivative has residue \(1\), because
\(H_3\bar f=X^{17}-1\). Scaling this unit root to \(1\) preserves the residue
configuration.

Put \(C_j=\binom{20}{j}\). For
\[
J_A=\{10,12,13,16\},\qquad J_B=\{9,10,15,16\},
\]
the normalized polynomial has the form
\[
f(X)=X^{20}+\sum_{j\in J}C_ja_jX^{20-j}+DX^3+EX.
\]
The equations \(H_3f(1)=f(1)=0\) give the exact identities
\[
\begin{aligned}
D&=-1140-\sum_{j\in J}\binom{20-j}{3}C_ja_j,\\
E&=-1-\sum_{j\in J}C_ja_j-D.
\end{aligned}                                                    \tag{M1}
\]
Throughout, \(G_j=\sum_{i=0}^j\binom ji a_iX^{j-i}\), so \(G_j\) is a
nonzero scalar multiple of \(H_{20-j}f\) in characteristic zero.

## The finite residue cover

Every selected middle-derivative witness reduces to \(0\) or \(1\). Starting
from \(\bar a_0=1\), with all unspecified coefficients below index \(17\)
equal to zero, the recurrence
\[
\bar a_j=-\sum_{i<j}\binom ji\bar a_i\rho_j^{\,j-i},
\qquad \rho_j\in\{0,1\},                                      \tag{M2}
\]
therefore describes every possible residue configuration. This conclusion
holds over an algebraic closure of the residue field, since the seed has
only the two indicated root locations.

Set \(f(1+Z)=\sum c_kZ^k\). Formula (M1) gives
\[
c_0=c_3=0,\qquad
c_1=-2261+\sum_{j\in J}h_ja_j,\qquad
h_j=\left(19-j-2\binom{20-j}{3}\right)C_j.                       \tag{M3}
\]
Each \(c_k\), \(1\leq k\leq16\), is an integer polynomial in the \(a_j\)
whose coefficients are divisible by \(17\). For its constant part this
follows by expanding \(X^{20}-1140X^3+1139X\); each variable part has the
factor \(C_j\). In particular \(c_k\in17\mathcal O\).
This is coefficientwise divisibility, rather than an inference from
vanishing residue in a possibly ramified extension.

We first justify the necessary condition \(\nu(c_1)>1\).
The mean root \(0\) is simple. A nonzero root \(q\) reducing to zero cannot
be repeated: in \(f'(q)-f(q)/q\), the term \(2Dq^2\) has uniquely least
valuation, since \(D\) is a unit and every other low ordinary coefficient
has a factor \(17\) and exponent at least four. A repeated root must
therefore reduce to one. Every nonzero displacement \(z\) in that cluster
satisfies \(\nu(z)\geq1/16\), by the minimum-term comparison in
\(f(1+z)/z\). At a repeated root \(1+z\), every term of
\(f'(1+z)-f'(1)\) has value greater than one. For orders \(2,\ldots,16\)
this uses \(c_k\in17\mathcal O\); order \(17\) has the extra derivative
factor \(17\); orders at least \(18\) have value at least \(17/16\).
Thus \(\nu(c_1)>1\), also when the repeated root is exactly one.

Consequently the recurrence (M2) must satisfy
\[
-133+\sum_{j\in J}\frac{h_j}{17}\bar a_j=0.                      \tag{M4}
\]
There are sixteen markings for each \(J\). Substituting them in (M2) and
(M4) gives exactly the following two survivors:
\[
\begin{array}{c|c|c}
J&(\rho_j)_{j\in J}&(\bar a_j)_{j\in J}\\ \hline
J_A&(0,0,0,1)&(0,0,0,16)\\
J_A&(1,1,1,0)&(16,14,1,0)\\
J_B&(0,0,0,1)&(0,0,0,16)\\
J_B&(1,1,1,0)&(16,9,9,0).
\end{array}                                                   \tag{M5}
\]
For example, the divided weights \(h_j/17\) modulo \(17\) are
\((1,6,16,3)\) for \(J_A\) and \((9,1,11,3)\) for \(J_B\);
these and (M2) give a direct finite verification of the table.
The first marking for either support is excluded by the unit-\(16\)
obstruction. It remains to exclude the two mixed patterns in (M5).

## The small-root equations

In the mixed patterns, (M1) gives
\[
\overline{E/17}=
\begin{cases}
6,&J=J_A,\\
7,&J=J_B.
\end{cases}                                                   \tag{M6}
\]
Thus \(E\) has value one. The three-root cluster at zero consists of the
exact root zero and two nonzero roots of value \(1/2\). Indeed, in \(f/X\)
the constant coefficient has value one, the coefficient of \(X^2\) is
the unit \(D\), and the other terms lie strictly above the corresponding
Newton segment. After \(X=\sqrt{17}\,Y\), the initial equation is
\(-Y^2+\overline{E/17}=0\). Its two roots are distinct, so both small
nonzero roots are simple.

Reduction gives \(\bar G_{16}(1)=13\) in case \(A\) and \(2\) in case
\(B\). If \(a_{16}\neq0\), its selected witness is therefore a nonzero
small root \(q\). In case \(A\), the uniquely least nonconstant term of
\(G_{16}(q)\) is \(\binom{16}{13}a_{13}q^3\); in case \(B\), it is
\(16a_{15}q\). Both coefficients are units. Hence
\[
\nu(a_{16})=
\begin{cases}
3/2,&A,\\
1/2,&B.
\end{cases}                                                   \tag{M7}
\]
For later use, the argument also permits \(a_{16}=0\), interpreted as
infinite valuation. Its impossibility follows from the final equations.

## The leading model of the unit cluster

In the two mixed patterns, direct substitution in (M1) gives
\[
\nu(c_1)>1,\qquad
\overline{c_2/17}=\kappa,\qquad
\kappa=
\begin{cases}5,&A,\\3,&B.\end{cases}                            \tag{M8}
\]
Also \(c_{17}\equiv1\), while \(c_{18},c_{19},c_{20}\) are integral.
Choose an exact repeated root \(w\) in the unit cluster. If \(w\neq1\),
write \(z=w-1\), \(\epsilon=\nu(z)>0\). Subtraction of
\(f(1+z)/z\) from \(f'(1+z)\) gives
\[
0=\sum_{k\geq2}(k-1)c_kz^{k-1}.
\]
Only \(c_2z\) and \(16c_{17}z^{16}\), of values \(1+\epsilon\)
and \(16\epsilon\), can attain the minimum. Thus
\(\epsilon=1/15\), and the root equation gives
\(\nu(c_1)\geq16/15\). The same bound is immediate if \(w=1\).
It then follows from \(f(1+z)/z\) that every nonzero displacement in
the unit cluster has value at least \(1/15\).

Choose \(\pi^{15}=17\), and put
\(\lambda=\overline{c_1/(17\pi)}\). The reduction of
\(f(1+\pi Y)/\pi^{17}\) is
\[
g(Y)=Y^{17}+\kappa Y^2+\lambda Y.                              \tag{M9}
\]
This captures all seventeen roots of the unit cluster with multiplicity:
the three roots outside it contribute a unit factor, and the normalized
degree-seventeen factor has reduction (M9). In particular a root of
\(g\) of multiplicity \(m\) represents precisely \(m\) roots, counted
with multiplicity, in the corresponding next cluster.

The repeated root has a leading location \(\eta\) common to \(g\) and
\(g'=2\kappa Y+\lambda\). It is unique. If it is nonzero, then
\[
\eta^{15}=\kappa,\qquad \lambda=-2\kappa\eta,
\]
and, after dividing all leading locations by \(\eta\), they are roots of
\[
R(T)=T^{17}+T^2-2T.                                          \tag{M10}
\]
If it is zero, then \(\lambda=0\) and
\(g=Y^2(Y^{15}+\kappa)\), with a double root at zero and fifteen
simple nonzero roots.

Let \(w_j\) be the selected witness for one of the first three active
middle indices. Its coefficient is a unit, so \(w_j\) reduces to one.
Write \(Y_j=\overline{(w_j-1)/\pi}\). The coefficient baselines obtained
by putting all three witnesses exactly at one are
\[
(a_{10}^*,a_{12}^*,a_{13}^*)=(-1,65,-560)
\]
in case \(A\), and
\[
(a_9^*,a_{10}^*,a_{15}^*)=(-1,9,-22023)
\]
in case \(B\). The triangular recurrence for \(G_j(w_j)=0\) proves
\(\nu(a_j-a_j^*)\geq1/15\). For
\(A_j=\overline{(a_j-a_j^*)/\pi}\), its first variation gives
\[
\begin{array}{c|ccc}
A&A_{10}=7Y_{10}&A_{12}=14Y_{10}+Y_{12}
&A_{13}=9Y_{10}+4Y_{12}\\
B&A_9=8Y_9&A_{10}=5Y_9&A_{15}=8Y_9+8Y_{15}.
\end{array}                                                   \tag{M11}
\]
The absent \(Y_{13}\) and \(Y_{10}\) reflect vanishing first
derivatives at the respective baselines, not assumptions about those
witnesses. In (M3), the baseline value of \(c_1\) lies in
\(17^2\mathbf Z\), and the \(a_{16}\) contribution vanishes after
division by \(17\pi\), by (M7). Consequently (M11) gives
\[
\lambda=14Y_{10}+2Y_{12}\quad(A),\qquad
\lambda=12Y_9+3Y_{15}\quad(B).                                \tag{M12}
\]

## Exclusion of a nonzero repeated leading location

If \(\eta\neq0\), divide (M12) by \(\eta\) and use
\(\lambda/\eta=-2\kappa\). Two roots of (M10) would then satisfy
\[
t_{12}=12+10t_{10}\quad(A),\qquad
t_{15}=15+13t_9\quad(B).
\]
Neither affine pair exists over the algebraic closure. In
\(\mathbf F_{17}[T]\), direct division gives
\[
\begin{aligned}
R(12+10T)-10R(T)&=5T^2+2T+13=:Q_A,\\
R\bmod Q_A&=2T+11,& Q_A\bmod(2T+11)&=13,
\end{aligned}
\]
and
\[
\begin{aligned}
R(15+13T)-13R(T)&=3T^2+16T+6=:Q_B,\\
R\bmod Q_B&=3T+4,& Q_B\bmod(3T+4)&=7.
\end{aligned}                                                 \tag{M13}
\]
The nonzero constant remainders prove geometric emptiness, rather
than merely the absence of prime-field points. Hence \(\eta=0\)
and \(\lambda=0\).

Equations (M12) now give \(Y_{12}=10Y_{10}\) in case \(A\) and
\(Y_{15}=13Y_9\) in case \(B\). A nonzero root of (M9) has
fifteenth power \(-\kappa\), but
\(10^{15}=12\) and \(13^{15}=4\), neither equal to one.
Thus both paired locations are zero. The corresponding inner cluster
has multiplicity two and contains the exact root one and a repeated
root. It must consist of the exact double root one. Therefore
\[
\begin{array}{ll}
A:&w_{10}=w_{12}=1,\quad a_{10}=-1,\quad a_{12}=65,\\
B:&w_9=w_{15}=1,\quad a_9=-1,\quad a_{15}=5004-3003a_{10},
\end{array}                                                   \tag{M14}
\]
and \(f'(1)=0\) in both cases. This is a multiplicity argument; equal
residues alone would not justify these exact collisions.

## The critical derivative and the final contradiction

In case \(A\), substituting (M14) into \(f'(1)=0\) gives
\[
0=1961247925-4961280(a_{13}+560)-24225a_{16}.                   \tag{M15}
\]
The constant has value two and both variable coefficients have value
one. Hence (M7) implies \(\nu(a_{13}+560)\geq1\). Exactly,
\[
G_{13}(1+Z)=(a_{13}+560)-780Z^2+O(Z^3),
\]
where the linear term vanishes and all higher coefficients are integral.
The coefficient \(-780\) is a unit. At an outer root of displacement
value \(1/15\), its quadratic term would have uniquely least value
\(2/15\). The selected \(G_{13}\) witness must therefore belong to
the inner two-root cluster, so it equals one and \(a_{13}=-560\).

In case \(B\), the corresponding equation is
\[
0=5132750687+702257556(a_{10}-9)-24225a_{16}.                   \tag{M16}
\]
Again the constant has value two and both variable coefficients have
value one. Thus \(\nu(a_{10}-9)\geq1/2\). The exact expansion
\[
G_{10}(1+Z)=(a_{10}-9)+45Z^2+O(Z^3)
\]
has zero linear term and unit quadratic coefficient. The same
minimum-term argument forces its witness into the inner cluster.
Consequently \(a_{10}=9\) and \(a_{15}=-22023\).

Equations (M15) and (M16) now force respectively
\[
a_{16}=\frac{242879}{3},\qquad
a_{16}=\frac{15890869}{75}.                                   \tag{M17}
\]
Both numbers have value one, contrary to the values \(3/2\) and
\(1/2\) in (M7). If \(a_{16}=0\), the bounds on the critical
constants only improve, and (M17) still gives a contradiction.
This proves the two local exclusions and, by the residue cover (M5),
the stated exact-support exclusions.

The supplementary program
[check_mixed_strata.py](research/next-stage/last-four/middle/check_mixed_strata.py)
reconstructs (M1)–(M17) from binomial coefficients, checks every marking
in (M5), and verifies the polynomial divisions and rational constants.
Its role is to certify these finite identities. The valuation estimates,
complete cluster counts and exact collision deductions are the
mathematical arguments given above.


# The two configurations with a quadratic coefficient

We exclude the row-one configurations for the two deficiency supports
\[
\mathcal S_A=\{2,4,10,17,18,19\},\qquad
\mathcal S_B=\{4,10,16,17,18,19\}.
\]
The seed classification leaves only row one for \(\mathcal S_B\). The additional row-two configuration for \(\mathcal S_A\) is treated separately.

Let \(\mathcal O\) be a valuation ring in an algebraic extension of \(\mathbf Q_{17}\), with valuation \(\nu\) normalized by \(\nu(17)=1\). A bar denotes reduction in its residue field. We use
\[
H_kf=\frac{f^{(k)}}{k!},\qquad
G_j=\frac{H_{20-j}f}{\binom{20}{j}}
   =\sum_{i=0}^{j}\binom ji a_iX^{j-i}
\]
for the Hasse derivatives and their monic normalizations. All roots and normalized coefficients are integral. The seed in this section is
\[
\bar f=X^{20}-X^3=X^3(X-1)^{17}.
\]
Since \(H_3\bar f=X^{17}-1\), its common root with \(\bar f\) is one. Scaling a corresponding common root of \(f,H_3f\) to one preserves the seed. Consequently
\[
f(1)=H_3f(1)=0.
\]

Write the two families together as
\[
f=X^{20}+190hX^{18}+4845AX^{16}+184756BX^{10}
   +4845UX^4+DX^3+FX^2+EX. \tag{Q1}
\]
For \(\mathcal S_A\), \(h=a_2\ne0\) and \(U=0\); for \(\mathcal S_B\), \(h=0\) and \(U=a_{16}\ne0\). In both cases \(A=a_4\), \(B=a_{10}\), and \(D,F,E\) are nonzero. The seed gives \(\bar h=\bar F=\bar E=0\), while \(D\) is a unit. The normalization yields
\[
\begin{aligned}
D={}&-1140-155040h-2713200A-22170720B-19380U,\\
E={}&1139+154850h+2708355A+21985964B+14535U-F.
\end{aligned} \tag{Q2}
\]

## The two nonzero roots in the zero residue class

The exact mean root zero is simple because \(E\ne0\). There are two other roots reducing to zero, counted with multiplicity. We call these roots small and call roots reducing to one unit roots.

Suppose first that a common root \(q\) of \(f,H_2f\) is small. It is nonzero because \(H_2f(0)=F\ne0\). Its derivative equation and root equation give
\[
F=-3Dq+o(q),\qquad E=2Dq^2+o(q^2). \tag{Q3}
\]
Here \(o(q^m)\) denotes a term of valuation strictly greater than \(m\nu(q)\). Indeed every remaining term in the derivative equation has higher degree and integral coefficient. On scaling by \(q\), the initial quadratic of \(f(X)/X\) is a unit multiple of
\[
(X-1)(X-2).
\]
The two nonzero small roots are therefore simple. A common root of \(f,f'\) must then be a unit root.

Conversely, if a common root \(r\) of \(f,f'\) is small, subtraction of \(f(r)/r\) from \(f'(r)\) gives
\[
F=-2Dr+o(r),\qquad E=Dr^2+o(r^2). \tag{Q4}
\]
The repeated root \(r\) exhausts the two nonzero small roots. Moreover \(H_2f(r)=Dr+o(r)\ne0\), so a common root of \(f,H_2f\) must be a unit root. Thus at least one of the first two derivatives has a unit common root.

We claim that
\[
\nu(F)\geq1. \tag{Q5}
\]
Write \(f(1+Y)=\sum_{k=1}^{20}c_kY^k\). In particular \(c_3=0\), and direct expansion gives
\[
\begin{aligned}
c_1={}&-2261-306850h-5353725A-42678636B-24225U+F,\\
c_2={}&-3230-436050h-7558200A-58198140B-29070U+F.
\end{aligned} \tag{Q6}
\]
All the displayed coefficients other than that of \(F\) are divisible by 17. Also \(c_4,\ldots,c_{16}\in17\mathcal O\), whereas \(c_{17},\ldots,c_{20}\) are units.

If \(s=\nu(F)<1\), both \(c_1,c_2\) have value \(s\). The divided-root equation shows that every nonzero unit-root displacement has value \(s/16\). At such a root, \(c_1\) is uniquely smallest in \(f'\): differentiation gives a factor 17 to the degree-seventeen term, and the subsequent contributions have value at least \(17s/16>s\). Similarly, \(c_2\) is uniquely smallest in \(H_2f\). The degree-nineteen and degree-twenty contributions to the latter have values \(17s/16\) and \(18s/16\), respectively, and every other contribution also has value greater than \(s\). At the exact root one the two derivative values are \(c_1,c_2\ne0\). Neither derivative could have a unit common root, contradicting the preceding occupancy argument. This proves (Q5).

It follows that \(c_1,\ldots,c_{16}\in17\mathcal O\), and every nonzero unit-root displacement has value at least \(1/16\). Evaluation at a unit common root therefore gives
\[
\overline{c_1/17}=0\quad\text{for }H_1,\qquad
\overline{c_2/17}=0\quad\text{for }H_2. \tag{Q7}
\]
If either derivative has a small common root, (Q3) or (Q4) gives \(\nu(E)=2\nu(F)\geq2\). In family \(\mathcal S_A\), its nonzero \(G_2=X^2+h\) witness is small, so both nonzero small roots having the same value also gives \(\nu(h)=2\nu(F)\geq2\). These inequalities hold trivially for \(h=0\) in family \(\mathcal S_B\).

## A complete divided residue calculation

The witnesses for \(G_4,G_{10},G_{16}\) have residues in \(\{0,1\}\). In family \(\mathcal S_A\), take the exact mean as the \(G_{16}\) witness because \(U=0\). The triangular recurrence
\[
\bar a_j=-\sum_{i<j}\binom ji\bar a_i\rho_j^{\,j-i}
\]
therefore requires eight binary markings for family \(\mathcal S_B\) and four, with \(\rho_{16}=0\), for family \(\mathcal S_A\).

Let \(W_1,W_2,E_0\) be the residues of \(c_1/17,c_2/17,E/17\) obtained by setting \(h=F=0\), and let \(k=\overline{F/17}\). Since \(\bar h=0\), the actual first two residues are \(W_1+k,W_2+k\). Whenever a small derivative witness is present, the preceding bound \(\nu(h)\geq2\) also makes the actual third residue \(E_0-k\). Consequently the three possible occupancies impose
\[
\begin{array}{c|c}
(H_1,H_2)&\text{necessary equations}\\ \hline
(\mathrm{unit},\mathrm{unit})&W_1+k=W_2+k=0\\
(\mathrm{unit},\mathrm{small})&W_1+k=E_0-k=0\\
(\mathrm{small},\mathrm{unit})&W_2+k=E_0-k=0.
\end{array} \tag{Q8}
\]
All eight markings are displayed below; the four with \(\rho_{16}=0\) cover family \(\mathcal S_A\).

| \((\rho_4,\rho_{10},\rho_{16})\) | \((\bar A,\bar B,\bar U)\) | \((W_1,W_2,E_0)\) |
|---|---|---|
| \((0,0,0)\) | \((0,0,0)\) | \((3,14,16)\) |
| \((0,0,1)\) | \((0,0,16)\) | \((0,7,11)\) |
| \((0,1,0)\) | \((0,16,0)\) | \((2,8,16)\) |
| \((0,1,1)\) | \((0,16,0)\) | \((2,8,16)\) |
| \((1,0,0)\) | \((16,0,0)\) | \((3,13,8)\) |
| \((1,0,1)\) | \((16,0,0)\) | \((3,13,8)\) |
| \((1,1,0)\) | \((16,5,0)\) | \((8,9,8)\) |
| \((1,1,1)\) | \((16,5,12)\) | \((10,8,0)\) |

The unique survivor of (Q8) is
\[
(\rho_4,\rho_{10},\rho_{16})=(1,1,0),\quad
(\bar A,\bar B,\bar U)=(16,5,0),\quad k=8,
\]
with \(H_1\) small and \(H_2\) unit. Thus the small repeated root \(r\) has
\[
\nu(r)=1,\quad \nu(E)=2,\quad \nu(h)\geq2,\quad
\overline{c_1/17}=16. \tag{Q9}
\]
In family \(\mathcal S_A\), its \(G_2\) witness is exactly \(r\), so \(h=-r^2\). In family \(\mathcal S_B\), its nonzero \(G_{16}\) witness is exactly \(r\), and
\[
U=-r^{16}-1820Ar^{12}-8008Br^6,
\]
which gives \(\nu(U)=6\). Hence \(\nu(U)\geq6\) holds in both families, interpreting \(\nu(0)=\infty\).

The unit cluster now consists of exact one and sixteen simple outer roots of displacement value \(1/16\). For \(\pi^{16}=17\), the scaled initial polynomial is \(Y^{17}-Y\). Its roots are precisely \(\mathbf F_{17}\); zero corresponds to exact one, and the other sixteen residues correspond to the outer roots.

## A quadratic obstruction for the three unit witnesses

Let \(x_4,x_{10}\) be the common roots for \(G_4,G_{10}\), and let \(y\) be the unit common root for \(H_2\). Write
\[
x_4=1+\pi t,\qquad x_{10}=1+\pi s,\qquad y=1+\pi z.
\]
Their residues \(t_0,s_0,z_0\) belong to \(\mathbf F_{17}\). A zero residue means that the corresponding root is exactly one. We will prove that all three residues vanish.

Define a comparison polynomial
\[
f_0=X^{20}+4845AX^{16}+184756BX^{10}+D_0X^3+F_0X^2,
\]
where
\[
D_0=-1140-2713200A-22170720B,\qquad
F_0=1139+2708355A+21985964B.
\]
Its exact difference from (Q1) is
\[
\begin{aligned}
f-f_0={}&190h(X^{18}-816X^3+815X^2)\\
&+4845UX^2(X-1)(X-3)-EX(X-1).
\end{aligned} \tag{Q10}
\]
The first bracket vanishes at one. After cancelling \(X-1\) exactly, the root equation divided by \(17(X-1)\) therefore has error of valuation at least one. The Hasse-second equation divided by 17 has the same error bound. Both errors are strictly beyond the precision \(2\nu(\pi)=1/8\) used below.

The exact high-derivative identities are
\[
A=-x_4^4-6hx_4^2,\qquad
B=-x_{10}^{10}-45hx_{10}^8-210Ax_{10}^6.
\]
Because \(\nu(h)\geq2\), the terms containing \(h\) do not affect the first two \(\pi\)-orders. Modulo terms of value at least \(3/16\), binomial expansion gives
\[
\begin{aligned}
A&=-1-4\pi t-6\pi^2t^2,\\
B&=209+\pi(7t+9s)+\pi^2(2t^2+8ts+11s^2).
\end{aligned} \tag{Q11}
\]
Only residues of the displayed coefficients are needed.

Let \(17L_j(A,B)\), for \(1\leq j\leq16\), be the Taylor coefficients of \(f_0(1+Y)\). Direct expansion gives
\[
\bar L_1=2+8\bar A+\bar B,\qquad
\bar L_2=13+9\bar A+6\bar B,\qquad L_3=0,
\]
and at \((A,B)=(-1,209)\),
\[
\bar L_1=16,\qquad \bar L_2=0,\qquad \bar L_4=14.
\]
The remaining Taylor coefficients, in degrees 17 through 20, are \(1140,190,20,1\).

The first \(\pi\)-order of the Hasse-second equation is
\[
6t_0+3s_0+3z_0=0. \tag{Q12}
\]
The last summand comes from the degree-nineteen Taylor term:
\[
\frac{20\binom{19}{2}(\pi z)^{17}}{17}
   =3420\pi z^{17},\qquad 3420\equiv3\pmod {17}.
\]
The degree-seventeen and degree-eighteen terms first contribute at \(\pi\)-orders 15 and 16, respectively.

We justify the next-order calculation over arbitrary ramification. For every nonzero parameter among \(t,s,z\), its divided root equation has unit diagonal derivative \(16t_0^{15}\), \(16s_0^{15}\), or \(16z_0^{15}\). The off-diagonal derivatives vanish in the residue field. At integer lifts of the leading residues, the equation defects lie in \(\pi\mathcal O\). If a coordinate displacement had valuation smaller than \(\nu(\pi)\), the invertible linear part would have strictly smaller valuation than the defects and the nonlinear part, which is impossible. Thus
\[
t-t_0,\ s-s_0,\ z-z_0\in\pi\mathcal O,
\]
with zero parameters omitted since their roots are exactly one. Reducing the next root equations gives
\[
\begin{aligned}
t&=t_0+\pi t_1+o(\pi),&t_1&=12t_0^2+9t_0s_0,\\
s&=s_0+\pi s_1+o(\pi),&s_1&=9t_0s_0+12s_0^2.
\end{aligned} \tag{Q13}
\]
For a zero leading parameter its correction is zero, as the same formulas prescribe. For nonzero parameters, (Q13) follows from
\[
16t_1/t_0+12t_0+9s_0=0,\qquad
16s_1/s_0+9t_0+12s_0=0.
\]

Substituting (Q13) into (Q11), the second coefficient of \(L_2\) is
\[
6t_1+3s_1+9t_0^2+14t_0s_0+15s_0^2
=13t_0^2+10t_0s_0.
\]
The degree-nineteen term has no contribution at the second order: the first variation of \(z^{17}\) vanishes in characteristic 17. The remaining contributions at that order are
\[
6\bar L_4z_0^2+190z_0^{18}=16z_0^2+3z_0^{18}=2z_0^2.
\]
This identity also holds for \(z_0=0\); otherwise it uses \(z_0^{16}=1\). The second equation is therefore
\[
13t_0^2+10t_0s_0+2z_0^2=0. \tag{Q14}
\]
Eliminating \(z_0=-2t_0-s_0\) from (Q12) gives
\[
4t_0^2+t_0s_0+2s_0^2=0.
\]
Its discriminant is \(1-32=3\) in \(\mathbf F_{17}\), a nonsquare. Hence \(t_0=s_0=z_0=0\), and the cluster description implies the exact collisions
\[
x_4=x_{10}=y=1. \tag{Q15}
\]

## The final small-root residues

The collisions (Q15) imply
\[
A=-1-6h,\qquad B=209+1215h,
\]
and \(H_2f(1)=0\). Substituting into (Q2) and the Hasse-second equation gives
\[
\begin{aligned}
D={}&-4630968420-26921300640h-19380U,\\
F={}&12155856290+70665826950h+29070U,\\
E={}&-7563497030-43968975970h-14535U.
\end{aligned} \tag{Q16}
\]
Since \(\nu(h)\geq2\) and \(\nu(U)\geq6\), these yield
\[
\bar D=16,\qquad \overline{F/17}=8,\qquad
\overline{E/17^2}=9+14\overline{h/17^2}.
\]
The repeated-root equation (Q4) gives \(\overline{r/17}=4\). Therefore the residue of \(f(r)/(17^2r)\) must be
\[
9+14\overline{h/17^2}+8\cdot4+16\cdot4^2
=8+14\overline{h/17^2}. \tag{Q17}
\]
Every omitted term has strictly positive valuation after this division. For family \(\mathcal S_B\), \(h=0\), so (Q17) is \(8\ne0\). For family \(\mathcal S_A\), \(h=-r^2\) gives \(\overline{h/17^2}=1\), and (Q17) is \(5\ne0\). Both contradict \(f(r)=0\). This excludes both row-one configurations, and hence excludes \(\mathcal S_B\) globally.

The complete eight-row residue table, the 4,913 possible triples of second-jet residues, and the final integer constants are reproducible with [the quadratic-family checker](research/next-stage/last-four/quadratic/B/check_B.py) and [the support-A arithmetic checker](research/next-stage/last-four/quadratic/A/check_arithmetic.py). The finite calculations certify the stated arithmetic identities; the occupancy, multiplicity, and unit-Jacobian arguments above establish their validity for arbitrary ramification.


# Exclusion of the second residue configuration

**Proposition.** A nontrivial centered characteristic-zero Casas–Alvero
polynomial of degree twenty with exact deficiency support
\[
S=\{2,4,10,17,18,19\}
\]
cannot have the characteristic-seventeen reduction
\[
h(X)=(X^{17}-1)X(X^2-3).
\]

Write \(H_kf=f^{(k)}/k!\) and
\[
f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\qquad
G_j(X)=\frac{H_{20-j}f(X)}{\binom{20}{j}}.
\]
We use the integral normalization in which the mean root is zero,
\(a_0=1\), \(a_1=a_{20}=0\), and the nonzero nonleading normalized
coefficients have precisely the indices in \(S\). Let \(O\) be the
valuation ring of a field containing the coefficients and roots, with
valuation normalized by \(\nu(17)=1\) and \(\nu(0)=+\infty\).
No unramifiedness assumption is imposed on this field. A bar denotes
reduction in its residue field.

## Normalization and integral divided equations

The residue roots \(0\) and \(\pm\sqrt3\) of \(h\) are simple,
whereas the root \(1\) has multiplicity seventeen. The common root of
\(f\) and \(G_2\) reduces to \(1\). Scaling this actual root to
\(1\) gives
\[
a_2=-1,\qquad f(1)=0.
\]
Put \(a=a_4\), \(b=a_{10}\), \(T=H_3f(1)\), and let \(F\) be
the ordinary coefficient of \(X^2\). Then
\[
\begin{aligned}
f(X)={}&X^{20}-190X^{18}+4845aX^{16}+184756bX^{10}
       +DX^3+FX^2+EX,\\
D={}&153900-2713200a-22170720b+T,\\
E={}&189-4845a-184756b-D-F.
\end{aligned}
\tag{R2.1}
\]
All coefficients are integral, and \(\nu(T),\nu(F)>0\).

The selected common roots for \(H_1,H_2,H_3\) all lie in the residue
class of \(1\). For \(H_1\), every other residue class is simple.
For \(H_2\), the only common residue locations are \(0\) and \(1\),
but the zero class contains only the exact mean root, and
\(H_2f(0)=F\ne0\) by the exact-support assumption. For \(H_3\),
the only common residue location is \(1\).

Expand
\[
f(1+Y)=\sum_{k=0}^{20}c_kY^k.
\]
We have
\[
c_0=0,\quad c_3=T,\quad c_{17}=-2280,\quad c_{18}=0,
\quad c_{19}=20,\quad c_{20}=1,
\]
and \(c_4,\ldots,c_{16}\in17O\). Direct expansion gives
\[
\begin{aligned}
c_1&=-5353725a-42678636b+304589+2T+F,\\
c_2&=-7558200a-58198140b+432820+3T+F,\\
c_2-c_1&=T+17(7543-129675a-912912b).
\end{aligned}
\tag{R2.2}
\]

We first prove that \(T,F\in17O\). Suppose that
\[
\mu=\min\{\nu(T),\nu(F)\}<1.
\]
If \(\nu(c_1)=\mu\), every nonzero displacement \(z\) of a root
in the class of \(1\) has \(\nu(z)\ge\mu/16\): a smaller value
would make \(c_{17}z^{16}\) uniquely smallest in
\(f(1+z)/z\). At a repeated root, however, the constant term
\(c_1\) of \(f'(1+z)\) is then uniquely smallest. The terms from
\(c_2,c_3\) have larger value; the terms from degrees four through
sixteen have value at least one; the degree-seventeen term has an
additional factor of seventeen; and the degree-nineteen term has value
at least \(18\mu/16>\mu\). The same contradiction is immediate
if the repeated root is exactly \(1\).

Consequently \(\nu(c_1)>\mu\). Equation (R2.2) forces
\(\nu(T)=\nu(F)=\mu\) and cancellation of \(2T+F\). Let
\(1+z\) be the selected \(H_3\) common root. Its displacement is
nonzero, and its derivative equation forces
\[
\nu(z)=\frac{\mu}{17}.
\]
Indeed, only the constant term \(T\) and the degree-twenty
contribution \(1140z^{17}\) can have least value: all intervening
coefficients in the \(H_3\) equation are divisible by seventeen.
But in \(f(1+z)/z\), the term \(c_{17}z^{16}\) then has value
\(16\mu/17\), strictly smaller than every other term. This is
impossible, proving \(T,F\in17O\).

Every nonzero root displacement in the class of \(1\) now has value
at least \(1/16\). Applying the three derivative equations at their
selected roots gives
\[
\nu(c_1)>1,\qquad \nu(c_2)>1,\qquad \nu(T)>1.
\tag{R2.3}
\]
Here the degree-nineteen term of \(H_2\) must be retained:
\(\binom{19}{2}=171\) is a unit modulo seventeen, and its displacement
exponent is seventeen, so its value is at least \(17/16>1\).
A zero displacement makes the corresponding constant coefficient zero
and is included in these inequalities. Dividing (R2.2) by seventeen
therefore yields
\[
7543-129675\bar a-912912\bar b=0.
\tag{R2.4}
\]

## Residue coverage and simple outside witnesses

Since \(a,b\ne0\), the selected \(G_4\) and \(G_{10}\) common
roots cannot be the exact mean. Their residues belong to
\(\{1,s,-s\}\), where \(s^2=3\). The equations
\[
G_4(X)=X^4-6X^2+a,
\qquad
G_{10}(X)=X^{10}-45X^8+210aX^6+b
\]
give the complete table

| \(\bar a\) | \(\bar b\) | Left side of (R2.4), modulo \(17\) |
|---:|---:|---:|
| \(5\) | \(14\) | \(2\) |
| \(5\) | \(8\) | \(6\) |
| \(9\) | \(7\) | \(5\) |
| \(9\) | \(6\) | \(0\) |

Thus
\[
(\bar a,\bar b)=(9,6),
\]
and both selected roots reduce to one of \(s,-s\).

Choose the exact comparison roots \(r_0=\pm\sqrt3\) in the
unramified quadratic extension. The coefficients of \(f\) differ
from those of the integer representative
\((X^{17}-1)X(X^2-3)\) by elements of \(17O\). Indeed,
\(T,F\in17O\), and the relevant middle binomial coefficients are
divisible by seventeen. Hence \(\nu(f(r_0))\ge1\), while
\(f'(r_0)\) is a unit. Every actual root \(r\) in the corresponding
simple residue class satisfies \(\nu(r-r_0)\ge1\): otherwise the
linear Taylor term would be uniquely smallest. This argument also
applies in a ramified ambient extension.

At the selected \(G_4\) root,
\[
a=9-(r^2-3)^2,
\]
so \(\nu(a-9)\ge2\). The \(G_{10}\) equation at its selected
root then gives \(\nu(b+47628)\ge1\). Equation (R2.2) consequently
improves to
\[
c_2-c_1-T\in17^2O.
\tag{R2.5}
\]
At these residues, \(\overline{c_4/17}=8\). In particular,
\(\nu(c_4)=1\), so the seventeen roots in the class of \(1\)
cannot all coincide exactly at \(1\).

## The first nontrivial unit-cluster model

Let \(\delta\) be the least valuation of a nonzero displacement
from \(1\) among the roots in its residue class. By (R2.3),
\(\delta>1/16\). Descending through the three witness equations
gives
\[
\begin{aligned}
\nu(T)&\ge\min\{1+\delta,17\delta\}=1+\delta,\\
\nu(c_2)&\ge\min\{1+2\delta,17\delta\},\\
\nu(c_1)&\ge\min\{1+3\delta,18\delta\}.
\end{aligned}
\tag{R2.6}
\]
The term \(17\delta\) in the second bound comes from the
degree-nineteen contribution to \(H_2\). Combining (R2.5) and
(R2.6) improves the first bound to
\[
\nu(T)\ge\min\{1+2\delta,17\delta,2\}.
\]
If \(\delta<1/13\), a root attaining this value would make
\(c_{17}z^{16}\) uniquely smallest in \(f(1+z)/z\). Each
lower-degree contribution has value greater than \(16\delta\)
by these inequalities, as do the degree-nineteen and degree-twenty
contributions. Therefore \(\delta\ge1/13\), and
\[
\nu(c_1)\ge\frac{16}{13},\qquad
\nu(c_2)\ge\frac{15}{13},\qquad
\nu(T)\ge\frac{15}{13}.
\tag{R2.7}
\]

Choose \(\pi\) with \(\pi^{13}=17\). The reduction of
\(\pi^{-17}f(1+\pi Y)\) is
\[
L(Y)=-2Y^{17}+8Y^4+\lambda_2Y^2+\lambda_1Y.
\tag{R2.8}
\]
There is no cubic term because \(\nu(T)>14/13\). All seventeen
roots in the class are captured by this scaling, since their
displacements have value at least \(1/13\); the other three roots
contribute a unit local factor. The selected \(H_1,H_2,H_3\)
witnesses reduce to common roots of \(L\) with its corresponding
Hasse derivatives. Put \(\kappa=8\), so that
\(H_3L=4\kappa Y\).

We first show that \(\lambda_1=0\). Otherwise zero is a simple
root of \(L\). Its subcluster contains only one exact root, already
the root \(1\), and must contain the \(H_3\) witness. Thus that
witness is exactly \(1\) and \(T=0\). Equation (R2.5) then forces
\(\lambda_2=0\). Now \(H_2L=6\kappa Y^2\), so the \(H_2\)
witness also lies in this single-root subcluster and equals \(1\).
It follows that \(c_2=0\), and (R2.5) gives \(c_1\in17^2O\),
contrary to \(\lambda_1\ne0\).

Suppose next that \(\lambda_2\ne0\). The zero root of \(L\)
has multiplicity two. Let \(\eta\) be the scaled residue of a
repeated root of \(f\). If \(\eta=0\), that repeated root must
equal \(1\): a distinct repeated root together with \(1\) would
require at least three roots in this size-two subcluster. All roots
of the subcluster therefore equal \(1\). The \(H_3\) witness is
there too, so \(T=0\). But then (R2.5) contradicts
\(\nu(c_2)=15/13\), since \(\nu(c_1)>16/13\).

If \(\eta\ne0\), the equations \(L(\eta)=L'(\eta)=0\) imply
\[
\eta^2=-\frac{\lambda_2}{2\kappa},
\qquad
\eta^{13}=-\frac{\kappa}{2}.
\]
The \(H_2\) common witness has a nonzero scaled location \(v\),
and its equations give
\[
v^2=-\frac{\lambda_2}{6\kappa},
\qquad
v^{13}=-\frac{5\kappa}{2}.
\]
Consequently \(\rho=v/\eta\) satisfies
\[
\rho^2=\frac13,
\qquad \rho^{13}=5.
\]
In characteristic seventeen,
\[
\rho^{13}=\rho\left(\frac13\right)^6=8\rho,
\]
so \(\rho=7\). Its square is \(15\), whereas \(1/3=6\), a
contradiction over the full algebraic closure. Hence \(\lambda_2=0\).

We have proved
\[
L(Y)=Y^4(-2Y^{13}+\kappa).
\tag{R2.9}
\]
Its thirteen nonzero roots are simple, and \(H_1L,H_2L,H_3L\)
vanish only at zero. All three selected derivative witnesses therefore
belong to the size-four inner subcluster containing the exact root \(1\).

## A good-characteristic cluster lemma

**Lemma 4 (separated-cluster collapse).** Let a separated cluster contain \(m\) roots of a
polynomial, counted with multiplicity. Suppose the cluster contains a
common root of \(f\) and \(H_kf\) for every \(1\le k<m\).
If every degree-\(m\) Hasse–Casas–Alvero polynomial over the
algebraic closure of the residue field is a power of a linear
polynomial, then all roots of the cluster coincide exactly.

**Proof.** If the cluster is not already collapsed, center at a root
and scale by a greatest distance between roots in the cluster. The
normalized cluster polynomial is integral and has degree \(m\),
with at least two distinct residue roots. Every outside root is
strictly farther away. After normalization, the outside factor thus
reduces to a nonzero constant, and its nonconstant coefficients have
positive valuation. The Hasse product rule transfers the selected
incidences to the residue cluster polynomial. It is a nontrivial
degree-\(m\) Hasse–Casas–Alvero polynomial, contradicting the
hypothesis. A greatest internal distance exists because the cluster
is finite. The argument permits arbitrary ramification. \(\square\)

For \(m=4\) in characteristic seventeen, the hypothesis has an
elementary proof. Center the \(H_3\) common root and make the
polynomial monic, obtaining
\[
q(X)=X^4+AX^2+BX.
\]
If \(A=0\) and \(B\ne0\), a common root of \(q\) and \(q'\)
cannot be zero, and the two nonzero-root equations contradict
\(3B\ne0\). If \(A\ne0\), an \(H_2\) common root is nonzero;
scaling it to one gives \(A=-6\) and then \(B=5\). However,
\[
\operatorname{disc}(X^4-6X^2+5X)=4725\not\equiv0\pmod{17},
\]
so this polynomial has no repeated root. It cannot satisfy the
\(H_1\) condition. Thus every quartic Hasse–Casas–Alvero
polynomial in characteristic seventeen is a fourth power of a
linear polynomial.

Apply Lemma 4 to the inner cluster in (R2.9). All four roots
coincide at \(1\), giving
\[
c_1=c_2=T=0.
\]
Equation (R2.2) now yields
\[
b=\frac{7543-129675a}{912912}.
\tag{R2.10}
\]
The denominator is a seventeen-adic unit. Since
\(\nu(a-9)\ge2\), we also have \(\nu(b-B)\ge2\), where
\[
B=\frac{7543-129675\cdot9}{912912}.
\tag{R2.11}
\]

## The final simple-root lift obstruction

Evaluate the exact family determined by \(c_1=c_2=T=0\) at
\(a=9\), \(b=B\). Modulo \(X^2-3\), its relevant values
modulo \(17^2\) are
\[
\begin{aligned}
f(r_0)&\equiv170r_0,&
f'(r_0)&\equiv283r_0+130,\\
G_{10}(r_0)&\equiv204,&
G_{10}'(r_0)&\equiv92r_0.
\end{aligned}
\pmod{17^2}
\tag{R2.12}
\]
The actual parameters differ from \(9,B\) by elements of
\(17^2O\). Their effect on \(f\) belongs to \(17^3O[X]\),
and their effect on \(G_{10}\) belongs to \(17^2O[X]\).

The actual simple root selected by \(G_{10}\) has the form
\(r=r_0+17h\), with \(h\in O\). Reducing \(f(r)/17=0\)
gives
\[
0=10\bar r_0+11(\bar r_0+1)\bar h,
\qquad \bar r_0^2=3.
\]
The equation \(G_{10}(r)/17=0\) would therefore require
\[
0=12+7\bar r_0\bar h
 =\frac{12\bar r_0-4}{\bar r_0+1}.
\tag{R2.13}
\]
The denominator is nonzero. The numerator forces \(\bar r_0=6\),
whose square is \(2\), not \(3\), in characteristic seventeen.
This contradiction covers both signs of \(\sqrt3\), and hence all
four oriented choices of the \(G_4\) and \(G_{10}\) outside
witnesses. It proves the proposition. \(\square\)


# The support \(\{2,3,4,10,12,19\}\): the row-\(5\) reduction

The complete seed classification allows rows \(5\) and \(8\) for the exact
centered deficiency support
\[
S=\{2,3,4,10,12,19\}.
\]
The row-\(8\) alternative is excluded by the residue argument in Appendix B.
We prove here that the row-\(5\) alternative is also impossible.

Normalize the selected \(G_2\) witness to one. With
\(\nu(17)=1\), the resulting integral polynomial is
\[
\begin{aligned}
f(X)={}&X^{20}-190X^{18}+1140aX^{17}+4845AX^{16}\\
&+184756bX^{10}+125970cX^8+EX,\\
E={}&189-1140a-4845A-184756b-125970c,
\end{aligned}                                                   \tag{R1}
\]
where \(a=a_3,A=a_4,b=a_{10},c=a_{12}\) are all nonzero.
In particular \(f(1)=0\), \(a_2=-1\), and
\[
\bar f=X^{17}(X-1)^2(X+2),\qquad \bar a=2.                      \tag{R2}
\]
The mean root zero is simple, so \(E\neq0\).
All arguments take place in a finite extension of \(\mathbf Q_{17}\),
enlarged to contain the roots when necessary, with unrestricted
ramification. We use \(\nu(0)=+\infty\).

Let \(y\) be a selected \(G_3\) common root and \(w\) a selected repeated
root. Their possible residues are
\[
\bar y\in\{1,-2\},\qquad \bar w\in\{0,1\}.
\]
The residue class \(-2\) contains exactly one root; denote it by \(r\).
If \(\bar w=1\), the two-root residue cluster already contains the exact
root one and a repeated root. Its multiplicity forces \(w=1\), and
every other root or selected witness in that class is also exactly one.

## The complete first-divided cover

Put \(J=\{4,10,12\}\), \(u_4=A,u_{10}=b,u_{12}=c\), and
\(C_j=\binom{20}{j}\). We first derive the two divided conditions used
to enumerate the possible markings.

Suppose \(y=1+z\). The equation \(G_3(y)=0\) gives
\[
a=2-3z^2-z^3.
\]
Also
\[
f'(1)=17\cdot1957+18240(a-2)
       +\sum_{j\in J}(19-j)C_ju_j,\qquad
\overline{H_2f(1)}=3.                                         \tag{R3}
\]
If \(0<\nu(z)<1\), the first expression has value at least
\(\min(1,2\nu(z))>\nu(z)\). In the divided root equation
\[
0=f'(1)+H_2f(1)z+\sum_{k\geq3}H_kf(1)z^{k-1},
\]
the linear term would then be uniquely smallest. Thus
\[
\nu(y-1)\geq1,\qquad \nu(a-2)\geq2.                            \tag{R4}
\]
For this branch put \(\tau=0\).

If \(\bar y=-2\), substitute \(a=-y^3+3y\) into \(f(y)=0\).
The value at \(y=-2\) is coefficientwise divisible by \(17\), and
the total derivative there is \(16\) modulo \(17\). Taylor expansion
therefore forces \(y+2\in17\mathcal O\). Writing \(y=-2+17t\) gives
\[
\bar t=2+5\bar A+13\bar b+11\bar c,\qquad
\overline{(a-2)/17}=-9\bar t.                                 \tag{R5}
\]
For this branch put \(\tau=\bar t\). For completeness, the exact
value underlying the first congruence is
\[
\frac{f_{\;a=2}(-2)}{17}
=-20446986+18678330A+11150568b+1911780c.
\]
The derivative \(16\) includes the derivative of the substituted
coefficient \(a=-y^3+3y\); its extra contribution is zero in the
residue field.

If \(\bar w=1\), then \(w=1\) exactly. Dividing (R3) by \(17\)
gives
\[
1957+\sum_{j\in J}(19-j)\frac{C_j}{17}\bar u_j+9\tau=0.          \tag{R6}
\]
If \(\bar w=0\), let \(\delta\) be the least valuation of a
nonzero root in the zero cluster. The equation \(G_{19}(w)=0\)
gives
\[
\nu(E)\geq\min(17\delta,1+7\delta).
\]
At a root of value \(\delta\), the unit \(X^{17}\) term has value
\(17\delta\), whereas every other term has value at least
\(\min(18\delta,1+8\delta)\). It follows that
\(\delta\geq1/9\), and hence \(\nu(E)\geq16/9>1\).
Dividing the expression for \(E\) in (R1) now gives
\[
-123-\sum_{j\in J}\frac{C_j}{17}\bar u_j+9\tau=0.                \tag{R7}
\]

Every middle witness has residue in \(\{0,1,-2\}\).
Starting with
\(\bar a_0=1,\bar a_1=0,\bar a_2=-1,\bar a_3=2\), use
\[
\bar a_j=-\sum_{i<j}\binom ji\bar a_i\rho_j^{\,j-i},
\qquad j=4,10,12,                                             \tag{R8}
\]
with all inactive intermediate coefficients zero.
There are \(3^3=27\) assignments. Substitution in (R5)–(R7)
leaves the following complete list:
\[
\begin{array}{c|c|c|c|c}
\bar y&\bar w&(\rho_4,\rho_{10},\rho_{12})
 &(\bar A,\bar b,\bar c)&\tau\\ \hline
1&0&\text{none}&-&-\\
1&1&(-2,0,-2),\,(-2,1,-2)&(7,0,9)&0\\
-2&0&(-2,0,0),\,(-2,1,0)&(7,0,0)&3\\
-2&1&(-2,0,0),\,(-2,1,0)&(7,0,0)&3\\
-2&1&(-2,0,1),\,(-2,1,1)&(7,0,2)&8\\
-2&1&(-2,0,-2),\,(-2,1,-2)&(7,0,9)&0.
\end{array}                                                   \tag{R9}
\]
This is a cover of ten witness markings; distinct markings need not
represent distinct polynomials. It is complete over the algebraic
closure of the residue field, since the only seed root locations are
the three used in (R8). In particular the \(G_4\) witness is always
the exact root \(r\).

When \(y=r\), the exact normalized derivative equations give
\[
a(r)=-r^3+3r,\qquad A(r)=3r^4-6r^2.                           \tag{R10}
\]
When \(y=1\), the surviving markings have \(\bar w=1\), so the
collision above makes this equality exact. Then
\[
a=2,\qquad A(r)=-r^4+6r^2-8r.                                \tag{R11}
\]

## Finite polynomial identities

We record the identities needed in the remaining cases, retaining
their exact divisibility rather than using truncated analytic series.
First use (R10), with \(b,c\) free, and define
\[
\mathcal F(r;b,c)=f(r),\qquad
H(r;b,c)=f'(1)
=-3211+18240a+72675A+1662804b+881790c.
\]
For an integral solution of \(\mathcal F=0\) reducing to \(r=-2\),
the total \(r\)-derivative is a unit of residue \(16\), while
\(\mathcal F(-2;b,c)\in17\mathcal O\). Taylor expansion gives
\(r+2\in17\mathcal O\). Put \(r=-2+17t\).

After this substitution, \(\mathcal F,H,E\) are integer polynomials
divisible coefficientwise by \(17\), and
\[
\begin{array}{c|l}
\mathcal F/17&3+16t+13b+11c\\
H/17&7+9t+11b+3c\\
E/17&7+9t+12b+2c
\end{array}
\qquad\pmod {17\mathbf Z[t,b,c]}.                            \tag{R12}
\]
Consequently the following quotients are integer polynomials:
\[
\begin{aligned}
K_H&=\frac{H+9\mathcal F-153b}{17^2},\\
K_E&=\frac{E+9\mathcal F-17(10b+16c)}{17^2}.
\end{aligned}                                                \tag{R13}
\]
Direct substitution gives
\[
K_H(3,0,0)\equiv5,\qquad K_E(3,0,0)\equiv14\pmod {17}.         \tag{R14}
\]
These assertions concern exact finite polynomials: (R12) proves
coefficientwise integrality of (R13), and the two values in (R14)
are ordinary evaluations modulo \(17\).

If \(\mathcal F=H=0\) and \(b,c\) have positive valuation, (R12)
gives \(\bar t=3\), while (R13) gives
\[
b=-\frac{17}{9}K_H,\qquad
\nu(b)=1,\qquad \overline{b/17}=7.                            \tag{R15}
\]
If \(0<\nu(c)<1\), then \(\nu(E)=1+\nu(c)\).
If \(\nu(c)\geq1\), the second identity gives
\[
\overline{E/17^2}=16+16\overline{c/17}.                        \tag{R16}
\]

The exact equation \(G_{10}(1)=0\) is
\[
b=b_*(r):=44-120a(r)-210A(r).
\]
Put a star on \(\mathcal F,H,E\) after this substitution. The
integer polynomials
\[
K_H^*=\frac{H^*+9\mathcal F^*}{17^2},\qquad
K_E^*=\frac{E^*+9\mathcal F^*-272c}{17^2}                      \tag{R17}
\]
satisfy
\[
K_H^*(3,0)\equiv11,\qquad K_E^*(3,0)\equiv15\pmod {17}.        \tag{R18}
\]
Here
\[
\mathcal F^*/17\equiv3+16t+11c,\qquad
b_*(-2+17t)/17\equiv15+16t.
\]
In particular \(\mathcal F^*=0\) and \(\nu(c)>0\) imply
\(\nu(H^*)=2\).

We will also use these identities when \(b=b_*(r)+\eta\) with
\(\nu(\eta)>1\). Exactly,
\[
\begin{aligned}
\mathcal F-\mathcal F^*&=184756(r^{10}-r)\eta,\\
H-H^*&=1662804\eta,\qquad E-E^*=-184756\eta.
\end{aligned}                                                \tag{R19}
\]
All displayed multipliers are in \(17\mathcal O\).
Thus the correction to either identity in (R17) has value greater
than two. If \(\mathcal F=0\), \(\bar t=3\), and \(\nu(c)>1\),
the second identity gives
\[
\nu(E)=2,\qquad \overline{E/17^2}=15.                         \tag{R20}
\]
This stability statement follows from exact polynomial identities
and applies to fractionally valued \(\eta,c\).

## Case 1: repeated witness one and both middle witnesses units

Here the \(G_{10}\) witness is exactly one, and the \(G_{12}\)
witness is exactly one or \(r\). Write \(s,z\in\{1,r\}\) for
the exact \(G_3,G_{12}\) witnesses. Their equations force
\[
\begin{aligned}
a&=-s^3+3s,\\
A&=-r^4+6r^2-4ar,\\
b&=44-120a-210A,\\
c&=-z^{12}+66z^{10}-220az^9-495Az^8-66bz^2.
\end{aligned}                                                \tag{R21}
\]
These are integer polynomials in \(r\); no coefficient or witness
difference has been divided out.

For each pair \((s,z)\), define
\[
\begin{aligned}
P_{s,z}(r)={}&r^{20}-190r^{18}+1140ar^{17}+4845Ar^{16}\\
&+184756br^{10}+125970cr^8+Er,\\
Q_{s,z}(r)={}&-3211+18240a+72675A+1662804b+881790c,
\end{aligned}                                                \tag{R22}
\]
where (R21) and (R1) define every coefficient. These are exactly
\(f(r)\) and \(f'(1)\). The supplementary integer coefficient
arrays supply polynomials \(U_{s,z},V_{s,z}\) and nonzero integers
\(D_{s,z}\) with the exact identities
\[
U_{s,z}P_{s,z}+V_{s,z}Q_{s,z}=D_{s,z}.                        \tag{R23}
\]
Their degrees and constant valuations are
\[
\begin{array}{c|rrrr|rr}
(s,z)&\deg P&\deg Q&\deg U&\deg V&
\nu_{17}(D)&D/17^{\nu_{17}(D)}\bmod17\\ \hline
(1,1)&20&4&3&19&1&12\\
(1,r)&20&12&11&19&2&13\\
(r,1)&20&4&3&19&2&2\\
(r,r)&20&12&11&19&2&10.
\end{array}                                                  \tag{R24}
\]
The complete ascending-degree arrays, including the exact integers
\(D_{s,z}\), are in
[row5-unit-certificates.json](research/next-stage/row5-unit/row5-unit-certificates.json).
Identity (R23) is verified coefficient by coefficient by integer
convolution. Evaluating it at a common zero of \(P,Q\) would give
\(D_{s,z}=0\) in characteristic zero, a contradiction.
Thus all four exact choices are impossible; three occur in (R9).

## Case 2: repeated witness one, small \(G_{10}\) witness, and unit \(G_{12}\) witness

The \(G_{10}\) witness is a nonzero small root, because \(b\neq0\).
The \(G_{12}\) witness \(z\) is exactly one or \(r\), so its equation
expresses
\[
c=-z^{12}+66z^{10}-220az^9-495Az^8-66bz^2.                    \tag{R25}
\]
There are three surviving choices for the pair of exact
\(G_3,G_{12}\) witnesses. Substitute (R10) or (R11), then (R25),
and set \(r=-2+17t\). The equations
\(\mathcal F/17=H/17=0\) are integral polynomial equations.
Their reductions are the affine systems recorded below:
\[
\begin{array}{c|c|c|c|c}
G_3&G_{12}&\text{constant vector}&
\text{coefficient matrix in }(t,b)&
(\bar t,\bar b),\ \overline{E/17}\\ \hline
1&r&(0,0)&\begin{pmatrix}16&16\\0&1\end{pmatrix}&(0,0),\ 8\\
r&r&(0,0)&\begin{pmatrix}16&16\\9&1\end{pmatrix}&(0,0),\ 8\\
r&1&(8,13)&\begin{pmatrix}16&1\\9&0\end{pmatrix}&(8,0),\ 15.
\end{array}                                                  \tag{R26}
\]
The determinants are \(16,8,8\). The coefficientwise affine
congruences modulo \(17\) imply
\(t-t_0,b\in17\mathcal O\), where \(t_0=0,0,8\).
Equivalently, the usual unit-Jacobian minimum-valuation argument
proves this without assuming a discrete integer-valued valuation:
a least displacement value below one cannot cancel the invertible
linear term against either the defect in \(17\mathcal O\) or
the higher-order terms.

In each case \(\nu(E)=1\). Every nonzero small root then has value
\(1/16\), by the Newton segment of \(f/X\) between its constant
and its unit \(X^{16}\) coefficient. But at a small \(G_{10}\)
witness \(q\),
\[
0=q^{10}-45q^8+120aq^7+210Aq^6+b.
\]
Its least nonconstant term is \(210Aq^6\), with unit coefficient,
so \(\nu(b)=6/16=3/8\). This contradicts \(b\in17\mathcal O\).

## Case 3: repeated witness one, \(G_{10}\) witness one, and small \(G_{12}\) witness

The cover (R9) forces \(y=r\). Here \(b=b_*(r)\) exactly and
\(\nu(c)>0\). Equations (R17)–(R18), with
\(\mathcal F^*=0\), give \(\nu(f'(1))=2\), whereas the repeated
witness requires \(f'(1)=0\). This is impossible.

## Case 4: repeated witness one and both middle witnesses small

Again \(y=r\). Equations (R13)–(R15) give \(\nu(b)=1\).
Put \(\gamma=\nu(c)>0\).
If \(\gamma<1\), then \(\nu(E)=1+\gamma\). The Newton segment
of \(f/X\) makes every nonzero small root have value
\((1+\gamma)/16<1/8\). Its \(G_{10}\) equation would give
\(\nu(b)=6(1+\gamma)/16<3/4\), contrary to \(\nu(b)=1\).
Hence \(\gamma\geq1\).

The \(G_{10}\) equation now forces its selected small root \(q\)
to have value \(1/6\). In \(f(q)/q\) the unit \(q^{16}\) term has
value \(8/3\); every other nonconstant term has greater value.
Thus \(\nu(E)=8/3\). If \(\gamma>1\), equation (R16) instead
gives \(\nu(E)=2\), so necessarily \(\gamma=1\).

At a selected small \(G_{12}\) root \(z\),
\[
0=z^{12}-66z^{10}+220az^9+495Az^8+66bz^2+c.                   \tag{R27}
\]
The only possible least nonconstant values are
\(8\nu(z)\) and \(1+2\nu(z)\). Matching the constant value
\(\nu(c)=1\) forces \(\nu(z)=1/8\): below \(1/6\) the first
value is smaller, and at or above \(1/6\) both exceed one.
But the unit \(z^{16}\) term in \(f(z)/z\) then has value two,
strictly below the constant value \(8/3\) and every other
nonconstant term. It cannot vanish.

## Case 5: repeated witness small and \(G_{10}\) witness small

The cover gives \(y=r\) and a small \(G_{12}\) witness as well.
Let \(\delta>0\) be the least valuation of a nonzero root in
the zero cluster. The normalized derivative equations imply
\[
\nu(b)\geq6\delta,\qquad \nu(c)\geq8\delta.
\]
Using these in the first-derivative equation at its selected
small repeated root gives
\[
\nu(E)\geq\min(17\delta,1+15\delta).                           \tag{R28}
\]
At a root attaining \(\delta\), the unit \(X^{17}\) term of
\(f\) has value \(17\delta\). Every other term has value at
least \(\min(18\delta,1+16\delta)\). Therefore \(\delta\geq1\);
otherwise that term would be uniquely least. In particular
\[
\nu(b)\geq6,\quad \nu(c)\geq8,\quad \nu(E)\geq16.
\]
On the other hand \(\mathcal F=0\) and (R12) give \(\bar t=3\).
The exact second identity (R13) becomes
\[
E=17(10b+16c)+17^2K_E.
\]
Its first summand has value at least seven, whereas
\(K_E\equiv14\pmod{\mathfrak m}\) by (R14). Thus
\(\nu(E)=2\), contradicting (R28).

## Case 6: repeated witness small and \(G_{10}\) witness near one

The cover again gives \(y=r\), \(\nu(c)>0\), and \(\nu(b)>0\).
The selected \(G_{10}\) root \(x\) need not be exactly one.
From \(\mathcal F=0\) and (R13),
\[
H=153b+17^2K_H,
\]
so \(\nu(H)>1\). Moreover
\[
\overline{H_2f(1)}=3,\qquad \overline{G_{10}'(1)}=1.
\]
The divided equation \((f(x)-f(1))/(x-1)=0\) therefore implies
either \(x=1\) or \(\nu(x-1)>1\). Applying the corresponding
divided difference of \(G_{10}\) gives
\[
b=b_*(r)+\eta,\qquad \nu(\eta)>1.
\]
No exact collision has been assumed. Since (R12) gives
\(\bar t=3\), the displayed reduction of \(b_*/17\) gives
\(\overline{b/17}=12\), and in particular \(\nu(b)=1\).

For the least small-root value \(\delta\), equation (R27) and
the first-derivative equation now yield
\[
\begin{aligned}
\nu(c)&\geq\min(8\delta,1+2\delta),\\
\nu(E)&\geq\min(17\delta,1+15\delta,2+9\delta).
\end{aligned}                                                \tag{R29}
\]
At a root attaining \(\delta\), every term except the unit
\(X^{17}\) term has value at least
\(\min(18\delta,1+16\delta,2+10\delta)\).
Thus \(\delta\geq2/7\), giving
\[
\nu(c)\geq11/7>1,\qquad \nu(E)\geq32/7.
\]
But (R19) and the starred finite identity (R17) apply with
\(\nu(\eta)>1\). Equation (R20) gives \(\nu(E)=2\), a final
contradiction.

## Coverage and finite certificates

The six cases account for the ten markings in (R9), with respective
counts
\[
3,\ 3,\ 1,\ 1,\ 1,\ 1.
\]
Every exact candidate admits a selected witness marking, so their
exclusion proves that the normalized row-\(5\) alternative cannot
occur for \(S\). Combined with the separate row-\(8\) exclusion and
the complete seed classification, this excludes the entire exact
support \(\{2,3,4,10,12,19\}\).

The finite identities have three supplementary components:
the complete \(27\)-assignment residue reconstruction in
[check_row5_first_divided.py](research/next-stage/check_row5_first_divided.py);
the four integer identities (R23) in
[check_row5_unit.py](research/next-stage/row5-unit/check_row5_unit.py);
and the coefficientwise identities (R12)–(R19), evaluations, and
matrices in
[check_row5_jets.py](research/next-stage/row5-jets/check_row5_jets.py).
Each uses exact arithmetic and retains its acceptance checks under
optimized Python execution. Their finite calculations supply the
displayed identities; the valuation inequalities and root-count
deductions establishing complete case coverage are proved above.


# Completion of the seven-term support cover

We now assemble the local exclusions into the global theorem. The labels \(S_i\) refer to the complete fourteen-support table. The residue classification is always applied after integral normalization with a retained unit root; the monomial special fibre is therefore unavailable.

## The first divided condition in row 1

For \(S_6,S_7,S_9\), the exact coefficients \(a_2,a_4,a_{18}\) vanish. Normalize the common \(H_3\) root to one. The argument at the start of Theorem 2, before imposing the middle residue conditions, shows that the two nonzero small roots have valuation at least \(1/2\), that neither is repeated, and that \(\nu(a_3)\ge3/2\). Thus the common \(H_1\) witness lies in the unit cluster. All first sixteen Taylor coefficients at one are in \(17\mathcal O\), and a nonzero unit-root displacement has valuation at least \(1/16\). The derivative equation therefore forces \(f'(1)/17\) to have zero residue. Explicitly,
\[
-133+\sum_{j=4}^{16}
 \left(19-j-2\binom{20-j}{3}\right)
 \frac{\binom{20}{j}}{17}\bar a_j=0.
\]
The \(a_3\) contribution disappears because \(\nu(a_3)>1\).

For each active middle index, its witness reduces to zero or one. At an inactive index we may choose the exact root zero, since \(G_j(0)=a_j=0\). The triangular recurrence reconstructs every coefficient residue. The complete small censuses are

| Support | Active middle indices | Binary markings | Survivors of the divided equation |
|---|---|---:|---|
| \(S_6\) | \(6,10,16\) | 8 | only \(\bar a_{16}=-1\), earlier residues zero |
| \(S_7\) | \(7,8,10,16\) | 16 | the same |
| \(S_9\) | \(6,10,15,16\) | 16 | the same |

Theorem 2 excludes all these survivors. The analogous sixteen-marking censuses for \(S_8,S_{10}\), proved in the mixed-stratum section, leave the unit-16 pattern and exactly one mixed pattern each. Theorem 2 removes the first; the mixed-stratum theorem removes the second. Every active coefficient with zero residue is retained in these enumerations.

## Other residue branches

The row-8 divided condition and the complete small census in Appendix B exclude that row for \(S_1,S_2,S_3,S_4,S_5,S_6,S_{12}\). The respective marking counts are \(64,256,256,256,256,64,64\), totalling 1,216. Each census is already empty after the necessary divided condition.

The row-5 theorem excludes the other branch of \(S_1\). Appendix B excludes row 4 for \(S_{11}\) and row 9 for \(S_{12}\). The quadratic-coefficient theorem excludes \(S_{14}\) and the row-1 branch of \(S_{13}\). The row-2 theorem excludes its other possible nontrivial branch. Its apparent row-4 alternative is impossible by the exact-root restriction \(a_{17}=0\), conflicting with this exact support.

For reference, the complete closing table is:

| Support | Exclusion of every compatible branch |
|---|---|
| \(S_1\) | row 5 theorem; row 8 divided census |
| \(S_2,S_3,S_4,S_5\) | row 8 divided census |
| \(S_6\) | row 1 Theorem 2 and eight-marking sieve; row 8 census |
| \(S_7,S_9\) | row 1 Theorem 2 and sixteen-marking sieves |
| \(S_8,S_{10}\) | row 1 unit-16 and mixed-stratum exclusions |
| \(S_{11}\) | complete row-4 critical-value certificate |
| \(S_{12}\) | row 8 census; complete row-9 certificate for \(J=\{4,10,13\}\) |
| \(S_{13}\) | row 1 and row 2 theorems; row 4 exact-zero contradiction |
| \(S_{14}\) | row 1 quadratic-coefficient theorem |

**Theorem 1 (restated).** A nontrivial characteristic-zero polynomial of degree twenty sharing a root with each of its nonconstant proper derivatives has at least eight nonzero monomials after translating the zero of its nineteenth derivative to zero.

**Proof.** Appendix A excludes fewer than seven terms. The complete necessary-condition enumeration leaves precisely \(S_1,\ldots,S_{14}\) for seven terms. Integral normalization sends any such candidate to one of the compatible nonmonomial seeds listed in the table. Each corresponding branch is excluded above, including all coefficient-zero residue charts and arbitrary ramified lifts. Thus seven terms are impossible. Algebraic specialization transfers the exclusion back to every characteristic-zero candidate with that exact support. \(\square\)

The proof does not identify a realizable eight-term support. It gives a lower bound, not a sharpness statement. The unrestricted degree-twenty problem includes denser supports and is not settled by this theorem.


# Scope, evidence, and remaining problem

The completed theorem excludes every centered exact support with seven or fewer total terms in degree twenty. It combines the arithmetic support sieve with complete exclusions of every compatible seed branch. The uniform unit-16 theorem additionally covers denser polynomials satisfying its exact-zero and residue hypotheses. These conclusions do not settle the other dense strata, the unrestricted degree-twenty conjecture, or arbitrary degree.

The separated-cluster argument explains one way to use a good small degree inside a bad larger degree: when all relevant derivative witnesses are forced into the same separated cluster, a nontrivial splitting would induce a forbidden small-degree CA polynomial in the residue field. Its application here depends on the complete valuation and occupancy analysis. The existence of a cluster alone would not suffice.

The supplementary marked-resultant factorization and the previously checked 79-of-240 row-9 systems remain partial results at their original scopes. They are retained for review but are not needed to claim completion of all 240 systems, which has not been achieved. The eight-term theorem uses only the complete row-9 system with middle support \(\{4,10,13\}\), together with the other explicitly listed branches.

The new finite checkers reconstruct small identities and enumerations using exact arithmetic. The inherited computations include larger finite certificates and native residue replays. Default replay checks their recorded evidence and bounded calculations; it does not regenerate the largest optional census. The archive documents a longer fresh-census mode separately. A file hash proves that bytes were preserved, not that a theorem is true. Likewise, a successful replay establishes the specified arithmetic claims and does not replace the mathematical coverage and lifting arguments.

# Data, code, and declarations

**Data and code availability.** The review archive contains the PDF, editable Markdown, standalone LaTeX, proof notes, certificate data, executable checkers, audit records, and a SHA-256 manifest. The README identifies the current proof and reproduction commands. The versioned research archive is identified by DOI [10.5281/zenodo.22943640](https://doi.org/10.5281/zenodo.22943640); source and exact replay are available at [https://github.com/ipitchford/casas-alvero-eight-term](https://github.com/ipitchford/casas-alvero-eight-term). This archival identity does not constitute external refereeing.

**Review provenance.** A supplied arithmetic-review report concerns earlier identities. Its third-party source files are retained privately and are not redistributed in this release; they are not dependencies of the theorem. The latest supplied review reports additional reruns, but its linked audit archive was not available at publication intake. The new theorem has separate internal argument audits, independent arithmetic reconstructions, and a final coverage audit. These do not constitute external peer review of the present manuscript.

**Ethics.** This mathematical study involves no human participants, animal experiments, or personal-data analysis.

**Authorship and contributions.** The scholarly creator is Anonymous under the Evidence Press publication protocol. AI assistance is disclosed below; no named human contribution or CRediT assignment is inferred from account ownership.

**Funding.** No funding was received for this work.

**Competing interests.** No competing interests are declared.

**AI use.** Codex assisted the mathematical investigation, exact computation, drafting, source comparison, and internal adversarial checks. The evidence distinguishes generated arguments, arithmetic replay, internal review, and external validation. The manuscript makes no assessment-grade claim.


# Appendix A. Excluding six or fewer terms

This appendix proves the intermediate seven-term bound used in the main theorem. The finite identities needed in that proof are specified below, including their defining polynomials, coefficient-zero charts, verification bounds, and supplemental files. Earlier dossiers are not additional mathematical assumptions. The result concerns a restricted class of hypothetical counterexamples; it does not settle degree 20 or the Casas–Alvero conjecture.

## A.1. Statement, conventions, and specialization {.unnumbered}

For a polynomial \(f=\sum c_iX^i\), write
\[
H_kf=\sum_{i\ge k}\binom{i}{k}c_iX^{i-k}.
\]
In characteristic zero, \(f^{(k)}=k!H_kf\), so the ordinary and Hasse common-root conditions agree. Say that \(f\) has the CA property if \(f\) and \(H_kf\) have a common root for every \(1\le k<\deg f\). Roots are taken in an algebraic closure. The polynomial is nontrivial if it is not a scalar multiple of a power of a linear polynomial.

Let \(\alpha\) be the unique root of \(H_{19}f\). The CA property implies \(f(\alpha)=0\). Translate \(\alpha\) to zero and make the polynomial monic. Its centered form is
\[
F(X)=X^{20}+\sum_{j\in S}c_jX^{20-j},
\qquad S\subseteq\{2,\ldots,19\},\quad c_j\ne0.
\tag{S1}
\]
The indices \(j\) are **deficiencies**, not exponents or derivative orders. There are exactly \(1+|S|\) nonzero monomials. Changing scale \(X\mapsto rX\), \(r\ne0\), does not change \(S\).

**Proposition A.** Every nontrivial characteristic-zero degree-20 polynomial with the CA property has at least seven nonzero monomials in its centered form.

We first record the specialization argument used throughout. Extend the \(p\)-adic valuation to a field containing the coefficients and all roots. Choose a nonzero root \(\rho\) of minimum valuation, and replace \(F(X)\) by \(\rho^{-20}F(\rho X)\). All roots are integral and a root equals 1. In binomial normalization write
\[
F(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\qquad a_0=1,\quad a_1=a_{20}=0.
\]
The monic normalized derivative of degree \(j\) is
\[
G_j(X)=\frac{H_{20-j}F(X)}{\binom{20}{j}}
      =\sum_{i=0}^{j}\binom ji a_iX^{j-i}.
\]
At an integral common root \(\beta_j\), its equation expresses \(a_j\) as an integral polynomial in \(a_0,\ldots,a_{j-1},\beta_j\). Induction proves \(a_j\) integral. Therefore reduction deletes every ordinary coefficient whose binomial multiplier is divisible by \(p\). It preserves common-root witnesses for the Hasse derivatives and retains a nonzero root. In particular, the reduction is not \(X^{20}\).

No assertion about an arbitrary affine special fiber is used here: integrality and the retained unit root are established before reduction. The argument permits ramification, coefficient degeneration, and coincident witnesses. A valuation extension of the coefficient field is sufficient; the elementary minimum-valuation arguments below also work in an ordered value group. Alternatively, for this finite algebraic existence question one may first specialize an assumed exact-support solution to an algebraic characteristic-zero solution, encoding the nonzero coefficients by inverse variables, and then work over a finite extension of \(\mathbf Q_p\).

## A.2. Published restrictions and the complete finite support step {.unnumbered}

The proof uses two published arithmetic restrictions. The first is reproduced here as an elementary support test. The second is the determinant theorem of Castryck, Laterveer, and Ounaïes.

For a prime \(p\), put
\[
V_p=\{j\in\{2,\ldots,19\}:p\nmid\binom{20}{j}\}.
\]
The normalization above shows that \(S\cap V_p\ne\varnothing\). If \(S\cap V_p=\{r\}\), the reduction is \(X^{20}+aX^{20-r}\), with \(a\ne0\). A common root with \(H_{20-r}\) is nonzero, and the root and derivative equations imply
\[
\binom{20}{r}\equiv1\pmod p.
\tag{S2}
\]
This test includes coefficient loss: the remaining visible coefficient cannot also disappear because a unit root was retained.

For completeness, the two-visible test is stated with the necessary degeneration guards. It is the deficiency-index form of de Frutos Marín's two-support criterion [deFrutos]: *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, Theorem 3.5.1 and Proposition 3.5.5, printed pp. 55–57 ([thesis and repository record](https://uvadoc.uva.es/handle/10324/3602?show=full), DOI 10.35376/10324/3602). If \(S\cap V_p=\{r,s\}\), \(r<s\), define in \(\mathbf F_p\)
\[
B=\binom{20}{r},\quad D=\binom{20}{s},\quad
C=\binom{20-r}{s-r},\quad g=\gcd(r,s),
\]
\[
N=B^{s/g}(C-1)^{(s-r)/g}(D-C)^{r/g}
 -(B-1)^{r/g}(D-1)^{s/g}.
\tag{S3}
\]
If \(B,D\notin\{0,1\}\), a necessary condition is \(N=0\). The guard excludes singleton degenerations; it must not be omitted.

Here is a direct derivation. Both reduced coefficients must be nonzero by (S2). Normalize the common root for order \(20-r\) to 1. The two coefficients then become \(-B\) and \(B-1\). For a nonzero common root \(v\) for order \(20-s\), subtraction of the root and derivative equations gives
\[
(D-C)v^s=(C-1)(B-1),\qquad
B(D-C)v^{s-r}=(D-1)(B-1).
\]
The second equality rules out \(D=C\), and the first then rules out \(C=1\). Taking powers after division gives (S3). Thus this finite support test can be checked without relying on an unquoted source formula.

The other imported restriction is [Castryck–Laterveer–Ounaïes, Theorem 2](https://arxiv.org/html/1208.5404) [CLO]. For degree \(p+1=20\), the centered root is simple, and, with
\[
Z=\{j:2\le j\le18,\ j\notin S\},
\]
the following determinant is zero modulo 19:
\[
\Delta(Z)=
\det\begin{pmatrix}
\bigl[-1,\ (j\binom{j-2}{k-2}\mathbf1_{k\le j})_{k\in Z}\bigr]_{j\in Z}\\
-1,\ ((-1)^k)_{k\in Z}
\end{pmatrix}.
\tag{S4}
\]
The rows and columns indexed by \(Z\) are in increasing order. The indices in this formula are the **missing deficiency indices**. In particular, simplicity gives \(19\in S\). This is the only determinant theorem imported here.

The elementary tests already give four disjoint required sets:
\[
\{19\},\qquad\{4,16\},\qquad
\{5,10,15\},\qquad\{2,3,17,18\}.
\tag{S5}
\]
They come from primes \(19,2,5,17\), respectively; at 17 a singleton at 19 is forbidden by \(20\not\equiv1\). Hence \(|S|\ge4\), without importing an earlier sparsity result.

Apply (S2) and (S3) at \(p=2,3,5,7,11,13,17,19\), then (S4), to all subsets of \(\{2,\ldots,19\}\) of size 4 or 5. This is the entire finite support calculation:

| Number of nonleading terms | All subsets | After visible/singleton tests | After guarded two-visible test | After determinant |
|---:|---:|---:|---:|---:|
| 4 | 3060 | 8 | 4 | 1 |
| 5 | 8568 | 100 | 54 | 5 |

The size-four survivor is \(\{4,10,17,19\}\). The five size-five survivors, named here once and for all, are:

| Family | Deficiency support \(S\) | Ordinary exponent support |
|---|---|---|
| A | \(\{3,4,10,18,19\}\) | \(\{20,17,16,10,2,1\}\) |
| B | \(\{3,10,16,17,19\}\) | \(\{20,17,10,4,3,1\}\) |
| C | \(\{4,5,10,17,19\}\) | \(\{20,16,15,10,3,1\}\) |
| D | \(\{4,10,12,17,19\}\) | \(\{20,16,10,8,3,1\}\) |
| E | \(\{8,10,16,17,19\}\) | \(\{20,12,10,4,3,1\}\) |

All operations in this sieve are explicit small integer or finite-field operations in (S2)–(S4). Supplemental code verifies the determinants both by integer Bareiss elimination and modular Gaussian elimination; the degree-12 example printed after CLO Theorem 2 is an indexing control. No search for polynomial coefficients enters this step.

The archived implementation additionally applies the restrictions \(S\cap\{5,10\}\ne\varnothing\) and \(S\cap\{10,15\}\ne\varnothing\), available from the degree-20 characteristic-5 calculation in the proof of [Massri, Theorem 7.9](https://arxiv.org/html/1806.09561v6) [Massri]. They remove no support after the preceding two-visible tests: the counts remain 4 and 54. They can therefore be omitted from this proof dependency. Neither Massri's three-recycled-root theorem nor any claimed full proof of the conjecture is needed.

## A.3. The characteristic-13 lemma excluding D and the size-four survivor {.unnumbered}

**Lemma A.3.** Over any algebraically closed field of characteristic 13, the only CA polynomial
\[
h=X^{20}+aX^{16}+cX^3+dX
\]
is \(X^{20}\). Coefficients are allowed to vanish.

If \(a=0,c\ne0\), normalize an \(H_3\) common root to 1. Then \(c=4,d=8\). A common \(H_1\) root \(w\ne0\) satisfies
\[
w^{19}+4w^2+8=7w^{19}+12w^2+8=0,
\]
so \(w^2=10,w^{19}=4\). Since \(10^9=-1\), this forces \(w=9\), inconsistent with \(9^2=3\). If \(a=c=0,d\ne0\), the root and first-derivative equations give \(-d=w^{19}\) and \(-d=7w^{19}\), also impossible.

If \(a\ne0\), normalize an \(H_{16}\) common root to 1, giving \(a=4\). Choose a nonzero \(H_3\) common root \(v\). This is forced when \(c\ne0\); when \(c=0\), \(v=1\) is available because \(H_3h(1)=9+4=0\). The equations yield
\[
c=4v^{17}-4v^{13},\qquad d=-5v^{19},
\qquad F(v)=5v^{19}-4v^{17}+4v^{13}-5=0.
\]
Thus \(v,d\ne0\). For an \(H_1\) common root \(w\ne0\), subtracting \(h'(w)\) from \(3h(w)/w\) gives \(w^{19}=4v^{19}\). With \(t=w/v\), \(T=v^4\),
\[
M(t)=t^{19}-4=0,\qquad
(4t^2-1)T=4(t^2-t^{15}).
\]
The zeros 6 and 7 of \(D(t)=4t^2-1\) have nineteenth powers 7 and 6, so \(D\ne0\). Put \(B(t)=4(t^2-t^{15})\), so \(T=B/D\). Substituting \(v^4=T\) in \(F(v)=0\) gives
\[
5T^4v^3+4T^3(1-T)v=5.
\]
Squaring, using \(v^4=T\), and squaring once more yields the necessary equation
\[
R(T)=(T^9-T^8-1)^2-T^{13}(-T^3+3T^2-6T+3)^2=0.
\]
No factor in this expression has been divided out. The remainder of \(D^{19}R(B/D)\) modulo \(M\) is
\[
\begin{aligned}
H={}&5t^{18}-6t^{17}-3t^{16}+3t^{15}-2t^{14}-6t^{13}
+t^{11}+3t^{10}\\
&-t^8+t^7-t^6+3t^5+6t^4+5t^3-4t^2+6.
\end{aligned}
\tag{S6}
\]
But \(M=(t-4)Q\), where \(Q=\sum_{j=0}^{18}4^jt^{18-j}\) is irreducible: its roots are 4 times the primitive nineteenth roots of unity, and \(\operatorname{ord}_{19}(13)=18\). The latter order follows from \(13^6=11\) and \(13^9=-1\pmod{19}\). Now \(H(4)=8\), and \(H\ne5Q\), since their \(t^{16}\) coefficients are 10 and 2. Thus \(M,H\) are coprime, a contradiction.

At 13 the invisible deficiency indices are 8 through 12. Lemma A.3 and A.1 therefore exclude the entire characteristic-zero closed support mask
\[
T_D=\{4,8,9,10,11,12,17,19\}.
\tag{S7}
\]
This removes D and the size-four survivor, proving already that a nontrivial centered polynomial needs at least six terms. Notice that this implication does not require every allowed coefficient to be nonzero.

## A.4. The characteristic-13 lemma excluding E {.unnumbered}

**Lemma A.4.** The only characteristic-13 CA polynomial
\[
h=X^{20}+aX^4+cX^3+dX
\]
is \(X^{20}\).

The case \(a=0\) is the first boundary argument of A.3. If \(a\ne0\), normalize an \(H_4\) common root to 1; then \(a=4,d=-5-c\). If \(c=0\), the first-derivative common-root equations imply \(w^3=9,w^{19}=8\), hence \(w=8\), inconsistent with \(8^3=5\).

Choose an \(H_3\) witness \(v\ne0\), and put \(T=v^{16}\). The equations give
\[
c=v(4T-3),\qquad d=-v^3(5T+1),\qquad
Q(v,T)=(5T+1)v^3+(3-4T)v-5=0.
\]
If \(d=0\), then \(T=5,c=8,v=2\), inconsistent with \(2^{16}=3\). Thus a first-derivative witness \(w\) is nonzero. Set \(t=w/v\). Subtracting seven times \(h(w)/w\) from \(h'(w)\) and then using the root equation gives
\[
D(t)T=B(t),\quad D=10t^2+4,\quad B=-t^3+t^2-6,
\]
\[
U(t)=B(t)(t^{19}+4t^2-5)+D(t)(4t^3-3t^2-1)=0.
\]
At the two zeros 6 and 7 of \(D\), the values of \(B\) are 9 and 12, so \(D\ne0\). Explicitly,
\[
U=-t^{22}+t^{21}-6t^{19}-3t^5-5t^3+t^2.
\]
Define
\[
R(T)=\operatorname{Res}_v(v^{16}-T,Q(v,T)),\qquad
H(t)=D^{19}R(B/D)\bmod U.
\]
Here and below arrays list coefficients in ascending degree in \(\mathbf F_{13}\). The complete small certificate is

    R  = [1,11,0,11,9,1,5,9,0,10,8,4,11,10,4,0,12,4,8,12]
    H  = [6,0,10,0,3,4,1,9,2,9,7,12,9,1,8,4,4,3,11,2,10,5]
    CU = [2,4,0,1,6,9,7,10,2,10,8,8,0,5,2,7,0,7,2,1,4]
    CH = [11,0,3,1,8,7,9,1,9,8,2,0,2,7,7,6,4,9,0,10,3,6].

Direct multiplication gives \(C_UU+C_HH=1\). A putative solution has \(U=H=0\), contradiction. The resultant is independently checked as the determinant of the full \(19\times19\) Sylvester matrix, rather than by the producer's reduced \(5\times5\) determinant.

Valuation reduction now excludes the closed characteristic-zero deficiency mask
\[
T_E=\{8,9,10,11,12,16,17,19\},
\]
and hence family E.

## A.5. The larger characteristic-13 exclusion for B {.unnumbered}

**Lemma A.5.** The only characteristic-13 CA polynomial
\[
h=X^{20}+aX^{17}+bX^4+cX^3+dX
\tag{S8}
\]
is \(X^{20}\).

The chart \(a=0\) is Lemma A.4. If \(a\ne0\), normalize an \(H_{17}\) common root to 1, so \(a=4,d=-5-b-c\). The remaining active Hasse derivatives are
\[
H_4h=9X^{16}+4X^{13}+b,\quad
H_3h=9X^{17}+3X^{14}+4bX+c,
\]
\[
H_1h=7X^{19}+3X^{16}+4bX^3+3cX^2+d.
\]
For the whole chart \(b=0\), choose arbitrary witnesses \(v,w\) for orders 3 and 1 and substitute \(c=-9v^{17}-3v^{14},d=-5-c\). In \(\mathbf F_{13}[v,w]\), define
\[
F_3=v(5v^{19}+v^{16}+d),\quad
F_0=w(w^{19}+4w^{16}+cw^2+d),\quad
F_1=7w^{19}+3w^{16}+3cw^2+d.
\]
The supplemental sparse polynomials \(L_3,L_0,L_1\), with respectively 680, 694, and 712 terms, satisfy
\[
L_3F_3+L_0F_0+L_1F_1=1.
\tag{S9}
\]
This is ordinary ideal membership, with no saturation and no assumption \(c,d,v,w\ne0\).

For \(b\ne0\), an \(H_4\) witness \(u\) is nonzero and
\[
b=4u^{13}(u^3-1),\qquad c(u^2-1)=5+b-5u^{19}.
\]
The case \(u=1\) would give \(b=0\); at \(u=-1\) the second equation is inconsistent. Thus put
\[
q=u+1,\quad C=\frac{5+b-5u^{19}}{u-1},\quad D=q(-5-b)-C.
\]
The quotient defining \(C\) is a polynomial, of degree 18. The actual coefficients are \(c=C/q,d=D/q\), and \(q\ne0\). Define
\[
P=q(X^{19}+4X^{16}+bX^3)+CX^2+D,
\]
\[
J_3=q(9X^{17}+3X^{14}+4bX)+C,\quad
J_1=q(7X^{19}+3X^{16}+4bX^3)+3CX^2+D,
\]
and \(R_i=\operatorname{Res}_X(P,J_i)\), \(i=3,1\).
A zero common root for order 3 forces \(C=0\); a nonzero one forces \(R_3=0\). Therefore the necessary equation is \(CR_3=0\), and similarly \(DR_1=0\). The supplemental univariate multipliers satisfy
\[
A(u)C(u)R_3(u)+B(u)D(u)R_1(u)=(u+1)^{17}.
\tag{S10}
\]
Its left side vanishes at a solution and its right side does not. This proves the lemma.

The saved resultant degrees are 359 and 395. The coefficient degrees of \(P,J_3,J_1\) in \(u\) are at most 18, so the Sylvester bounds are 648 and 684. Independent exact evaluation at 685 distinct elements of \(\mathbf F_{13^3}\), excluding \(u=-1\) to preserve leading degrees, certifies the entire two resultant polynomials. Multiplication then checks (S9) and (S10) coefficient by coefficient. This is an identity check over an extension field with a proved degree bound, not a search for the absence of rational points.

The resulting characteristic-zero closed mask is
\[
T_B=\{3,8,9,10,11,12,16,17,19\}.
\]
It contains family B.

## A.6. Family A: a nonempty reduction that forces exact collisions {.unnumbered}

Family A needs a different argument because its reduced coefficient family does contain a nontrivial CA polynomial.

Consider
\[
h=X^{20}+aX^{17}+bX^{16}+cX^2+dX
\]
in characteristic 13. Its active derivatives are
\[
H_{17}=9X^3+a,\quad H_{16}=9X^4+4aX+b,
\]
\[
H_2=8X^{18}+6aX^{15}+3bX^{14}+c,\quad
H_1=7X^{19}+4aX^{16}+3bX^{15}+2cX+d.
\]
The following complete algebraic classification includes every degeneration.

If \(a=0,b\ne0\), normalize an \(H_{16}\) witness to 1: \(b=4,d=-5-c\). With an \(H_2\) witness \(v\), substitute \(c=-8v^{18}-12v^{14}\). The supplied identity expresses 1 in the ordinary ideal
\[
\bigl(h(v),h(w),7w^{19}+12w^{15}+2cw+d\bigr)
\subset\mathbf F_{13}[v,w].
\tag{S11}
\]
If \(a=b=0,c\ne0\), normalization gives \(c=5,d=7\). Then \(H_1h-7h/X=X+10\), so its common nonzero root would be 3, whereas \((h/X)(3)=12\). The remaining binomial \(X^{20}+dX\), \(d\ne0\), is excluded as in A.3.

Thus \(a\ne0\). Normalize an \(H_{17}\) witness to 1, giving \(a=4,d=-5-b-c\), and put \(P=h/X\). The conditions for orders 2 and 1 imply
\[
c\,\operatorname{Res}_X(P,H_2h)=0,\qquad
d\,\operatorname{Res}_X(P,H_1h)=0.
\tag{S12}
\]
Multiplication by \(c,d\) retains zero-coefficient charts. There are three univariate cases:

| Case | Parameter and coefficient substitution | Gcd of the two polynomials in (S12) |
|---|---|---|
| \(b=0\) | \(c,\ d=-5-c\) | \(1\) |
| \(H_{16}\)-witness \(u=1\) | \(b=1,\ d=-6-c\) | \(c-4\) |
| \(b\ne0,\ u\ne1\) | \(b=4u^4-3u,\ c=(5+b-5u^{19}-u^{16})/(u-1),\ d=-5-b-c\) | \(1\) |

The last numerator is divisible by \(u-1\); it is a degree-18 polynomial after division. The witnesses there also satisfy \(u\ne0\), since \(b\ne0\). The supplied resultants are exact Sylvester determinants; the checked parameter-degree bounds for the multiplied resultants are \(38,39\) in the first two cases and \(684,702\) in the last. Evaluation at more than each bound over \(\mathbf F_{13^3}\), followed by exact polynomial gcd, proves the table.

Consequently the unique normalized nonmonomial seed is
\[
h_A=X^{20}+4X^{17}+X^{16}+4X^2+3X.
\]
Exact gcds are
\[
\gcd(h_A,H_{17}h_A)=\gcd(h_A,H_{16}h_A)
=\gcd(h_A,H_2h_A)=X-1,
\]
and \(h_A'(1)=11\ne0\).

Now take a characteristic-zero polynomial whose support is contained in A's exponent mask. Apply A.1 at 13; the \(X^{10}\) coefficient disappears, and the preceding classification shows that the \(X^{17}\) coefficient is a unit. Its \(H_{17}\) witness is therefore a unit and may be scaled to 1 while preserving integrality. The other two witnesses reduce to the simple root 1. They equal 1 exactly: the polynomial divided difference
\[
\frac{F(r)-F(1)}{r-1}
\]
is integral and reduces to \(h_A'(1)\), so is a unit; its product with \(r-1\) is zero. This proves exact equality without a completeness or unramified-lifting assumption.

Writing \(t\) for the ordinary \(X^{10}\) coefficient, the exact equations at 1 give
\[
F=X^{20}-1140X^{17}+14535X^{16}+tX^{10}
  +(-1589350-45t)X^2+(1575954+44t)X.
\tag{S13}
\]
Let \(Q=F/X\), and define the exact integer polynomials
\[
R_{10}(t)=\operatorname{Res}_X(Q,H_{10}F),\qquad
R_1(t)=\operatorname{Res}_X(Q,H_1F).
\]
Their degrees are 19 and 28; reduction modulo 101 preserves both degrees and gives gcd 1. Hence they are coprime over \(\mathbf Q\). For \(t\ne0\), an \(H_{10}\) witness is nonzero, forcing \(R_{10}(t)=0\). The \(H_1\) condition always forces \(R_1(t)=0\): if its witness is zero, the linear coefficient vanishes and zero is then also a root of \(Q\). This contradicts coprimality. For \(t=0\), the separately checked value \(R_1(0)\ne0\) supplies the contradiction.

The integer resultants are certified at 30 and 39 distinct integer parameter values by exact Sylvester determinants: the a priori parameter-degree bounds are 29 and 38. This certifies the resultant identities before the degree-preserving modular gcd check. Family A is thus excluded as a closed support, including the \(t=0\) boundary.

## A.7. Family C: reduction, all six residue rows, and ramified precision {.unnumbered}

It remains to exclude exact support C:
\[
F=X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\qquad ABCDE\ne0.
\tag{S14}
\]
Normalize integrally at 13. An \(H_{10}\) witness gives
\[
184756z^{10}+8008Az^6+3003Bz^5+C=0.
\]
The first three numerical coefficients are divisible by 13; hence \(C\in13O\). The reduced shape is \(h=X^{20}+aX^{16}+bX^{15}+dX^3+eX\).

We must justify normalizing an \(H_{16}\) witness. If \(a=e=0\) in a nonmonomial seed, \(b=0\) gives an immediate root/\(H_3\) contradiction. For \(b\ne0\), normalize an \(H_{15}\) witness to 1; then \(b=5,d=7\), and an \(H_3\) witness would satisfy \(v^{17}=5,v^5=-1\). These imply \(v^2=8,v=1\), a contradiction. Thus \(a=0\) would require \(e\ne0\). But \(\overline{H_{16}F}=9X^4\) would force its witness into the simple residue root zero. Divided-difference uniqueness would make that exact witness zero, contrary to \(A\ne0\). Therefore \(A\) is a unit. Normalize its witness to 1:
\[
A=-4845,\qquad F(1)=0,\qquad E=-1-A-B-C-D.
\tag{S15}
\]

### A.7.1. Exact algebraic classification of the reduced seeds {.unnumbered}

Write the seed now as \(h=X^{20}+4X^{16}+bX^{15}+cX^3+dX\). Lemma A.3 excludes \(b=0\), so an \(H_{15}\) witness \(u\) is nonzero. At \(u=-1\) the equations give \(h(-1)=10\); treat \(u=1\) separately. For \(u\ne0,\pm1\),
\[
b=5u^5+u,\quad N=5+b-6u^{19}-5u^{15},\quad
C_n=N/(u-1),\quad q=u+1,\quad D_n=q(8-b)-C_n,
\]
\[
c=C_n/q,\qquad d=D_n/q.
\]
Again \(C_n\) is a polynomial of degree 18. Set
\[
P=q(X^{19}+4X^{15}+bX^{14})+C_nX^2+D_n,
\]
\[
J_3=q(9X^{17}+4X^{13})+C_n,\quad
J_1=q(7X^{19}+12X^{15}+2bX^{14})+3C_nX^2+D_n,
\]
and \(R_i=\operatorname{Res}_X(P,J_i)\). The necessary conditions are \(C_nR_3=D_nR_1=0\), including coefficient loss. The exact supplemental identity is
\[
UR_3C_n+VR_1D_n=(u+1)^{17}(u-1)(u-2)(u^2+4u-2).
\tag{S16}
\]
It leaves \(u=2\), giving \((b,c,d)=(6,3,12)\), or \(u^2+4u-2=0\), giving \((6,2,0)\).

For \(u=1\), \(b=6,d=2-c\). Use \(P=X^{19}+4X^{15}+6X^{14}+cX^2+2-c\) and the corresponding unscaled derivatives
\[
J_3=9X^{17}+4X^{13}+c,\quad
J_1=7X^{19}+12X^{15}+12X^{14}+3cX^2+2-c.
\]
A second identity has left side \(UcR_3+V(2-c)R_1\) and right side
\[
(c-2)(c-3)(c-10).
\tag{S17}
\]
Thus the complete list is \((6,3,12),(6,2,0),(6,10,5)\). The generic resultants have degree bounds 648 and 684 and are certified at 685 extension-field points; the special bounds are 36 and 38 and require 39 points. These identities prove completeness over every algebraically closed characteristic-13 field; there is no restriction to base-field coefficients or witnesses.

For the seed \((6,2,0)\), \(\gcd(h,h')=X^2\). In characteristic zero, an \(H_1\) witness \(w\ne0\) must therefore have positive valuation; it cannot be zero because \(E\ne0\). Yet
\[
F'(w)-F(w)/w
=19w^{19}+15Aw^{15}+14Bw^{14}+9Cw^9+2Dw^2=0
\]
has its last term of uniquely least valuation, as \(D\) is a unit. This excludes that entire coefficient point, including its extension-field marked witnesses.

Put
\[
h_3=X^{20}+4X^{16}+6X^{15}+3X^3+12X,\qquad
h_{10}=X^{20}+4X^{16}+6X^{15}+10X^3+5X.
\]
The exact monic gcds that determine the marked roots are
\[
\begin{array}{c|ccc}
 &H_{15}&H_3&H_1\\ \hline
h_3&(X-1)^2(X-2)&X-2&(X-1)(X-4)^2\\
h_{10}&X-1&X-11&(X-3)(X-11).
\end{array}
\]
The relevant multiplicities in \(h_3\) are 1 at 0 and 2, 2 at 1, and 3 at 4; in \(h_{10}\) they are 1 at 0 and 1, and 2 at 3 and 11. These are checked by division and evaluation of Hasse derivatives.

Let \(u,v,w,z\) denote the common-root witnesses for Hasse orders \(15,3,1,10\). The gcds give precisely the six rows below:

| Row | Seed | \(\bar v\) | \(\bar u\) | \(\bar w\) | Exact consequences |
|---:|---|---:|---:|---:|---|
| 1 | \(h_3\) | 2 | 1 | 1 | \(u=w=1\) |
| 2 | \(h_3\) | 2 | 1 | 4 | none initially |
| 3 | \(h_3\) | 2 | 2 | 1 | \(u=v,\ w=1\) |
| 4 | \(h_3\) | 2 | 2 | 4 | \(u=v\) |
| 5 | \(h_{10}\) | 11 | 1 | 3 | \(u=1\) |
| 6 | \(h_{10}\) | 11 | 1 | 11 | \(u=1,\ v=w\) |

The exact consequences use only cluster multiplicity. A simple residue root has a unique exact root above it. A double residue cluster containing an exact repeated root is exhausted by that repeated root; if it also contains the already fixed root 1, the repeated root equals 1. Root counting here is valid because the monic polynomial factors into integral linear factors, whose reductions record the cluster multiplicities.

### A.7.2. Two precision lemmas {.unnumbered}

Normalize \(\nu(13)=1\). Suppose integral polynomial equations have a zero \(x\) congruent to an integral base point \(b\), their Jacobian at \(b\) is invertible over \(O\), and their defects at \(b\) and any external parameter errors have valuation at least \(\lambda>0\). Then every coordinate of \(x-b\) has valuation at least \(\lambda\). Indeed, if their minimum \(\gamma\) were \(0<\gamma<\lambda\), the linear term would have minimum valuation \(\gamma\), preserved by an invertible integral matrix. Constant errors and all terms quadratic in the deviations have larger valuation. The equations cannot vanish. We call this the **unit-Jacobian bound**.

A second observation is needed at the triple residue root 4 of \(h_3\). Once the coefficients agree with an integer lift modulo \(13O\), \(F'(4),H_2F(4)\in13O\), while \(3H_3F(4)\) is a unit. If \(w\equiv4\) and \(F'(w)=0\), Taylor expansion forces \(\nu(w-4)\ge1/2\); otherwise its quadratic term has uniquely least valuation. If also \(F(w)=0\), Taylor expansion of \(F\) then shows \(\nu(F(4))>1\). Consequently \(\overline{F(4)/13}=0\). This does **not** claim \(w-4\in13O\).

### A.7.3. The exact \(u=1\) cases {.unnumbered}

The order-15 equation gives \(B=B_0=62016\). At \((v,D)=(2,3)\) and \((11,10)\), the Jacobians of \((F(v),H_3F(v))\) in \((v,D)\) are respectively
\[
\begin{pmatrix}9&6\\4&1\end{pmatrix},\qquad
\begin{pmatrix}0&7\\4&1\end{pmatrix}
\pmod{13},
\]
both of determinant 11. Since \(C\in13O\), the bound proves
\[
v=v_0+13t,\qquad D=d_0+13l,\qquad C=13k,\qquad t,l,k\in O.
\]
Dividing the exact equations by 13 gives, for \((v_0,d_0)=(2,3)\),
\[
9t+6l+8k+12=0,\qquad 4t+l+7k+6=0;
\tag{S18}
\]
for \((11,10)\), it gives
\[
7l+12k+2=0,\qquad 4t+l+6k+3=0.
\tag{S19}
\]
All equations in the following table are residue equations.

| \((\bar v,\bar w)\) | Additional equation and reason | \((\bar t,\bar l,\bar k)\) |
|---|---|---|
| \((2,1)\) | \(2l+9k+7=0\), from \(F'(1)=0\) | \((1,3,0)\) |
| \((2,4)\) | \(8l+5k+1=0\), by the triple-cluster bound | \((5,7,12)\) |
| \((11,3)\) | \(11l+9=0\), from \(F(w)=0\) | \((8,11,1)\) |
| \((11,11)\) | \(t+11l+k+7=0\), from \(F'(v)=0\) | \((0,6,5)\) |

For the third row, \(h_{10}'\) has a simple root at 3, so first apply the one-variable bound to obtain \(w-3\in13O\); its displacement contributes zero to \(F(w)/13\) because 3 is a double root of \(h_{10}\). In the fourth row, \(v=w\) is an exact collision.

The integral monic middle derivative \(H_{10}F/184756\) reduces to
\[
g_\lambda=X^{10}+11X^6+7X^5+\lambda,\qquad \lambda=9\bar k.
\]
Exact Euclidean gcds are
\[
\gcd(h_3,g_0)=X,\quad\gcd(h_3,g_4)=1,\quad
\gcd(h_{10},g_9)=\gcd(h_{10},g_6)=1.
\tag{S20}
\]
The last three cases are impossible. In the first, the middle witness reduces to the simple root zero and hence is exactly zero; this would give \(C=H_{10}F(0)=0\), contrary to exact support. This excludes rows 1, 5, 6 and the \(u=1\) part of row 2.

### A.7.4. Row 2 without an assumed exact collision {.unnumbered}

Here the order-15 equation gives \(B(u)=77520u-15504u^5\). For \(s=u-1\),
\[
B(u)-B_0=-15504s^2(10+10s+5s^2+s^3).
\tag{S21}
\]
If \(r=\nu(s)>0\), this has valuation \(2r\). The same two-variable bound now gives
\[
\min\{\nu(v-2),\nu(D-3)\}\ge\min\{1,2r\}.
\]
Moreover
\[
F'(1)=13\cdot61198+14(B-B_0)+9C+2(D-3),
\qquad H_2F(1)\equiv9.
\]
If \(r<1\), the exact divided-difference equation
\[
0=\frac{F(u)-F(1)}{u-1}
 =F'(1)+H_2F(1)s+H_3F(1)s^2+\cdots
\]
has a uniquely smallest term \(H_2F(1)s\): the first term has valuation at least \(\min\{1,2r\}>r\), and the remaining terms have valuation at least \(2r\). Thus \(r\ge1\). It follows that \(B-B_0\in13^2O\) and \(v-2,D-3\in13O\). These conclusions also hold if \(s=0\). The \((2,4)\) first-jet calculation in A.7.3 is unchanged and again gives \(\gcd(h_3,g_4)=1\), excluding all of row 2.

### A.7.5. Rows 3 and 4: the collision \(u=v\) {.unnumbered}

Substitute \(B(u)=77520u-15504u^5\) in \(F(u)=H_3F(u)=0\). The Jacobian in \((u,D)\) at \((2,3)\), including differentiation of \(B(u)\), is
\[
\begin{pmatrix}10&6\\4&1\end{pmatrix}\pmod{13},
\qquad\det=12.
\]
Hence \(u=2+13r,D=3+13l,C=13k\), with integral \(r,l,k\). The first two divided equations reduce to
\[
10r+6l+8k+7=0,\qquad4r+l+7k+6=0.
\tag{S22}
\]
In row 4, the triple-cluster bound supplies \(10r+8l+5k+3=0\). Together they give \((\bar r,\bar l,\bar k)=(5,7,12)\), so (S20) excludes the row.

In row 3, \(w=1\), and \(F'(1)=0\) gives \(11r+2l+9k+4=0\). The solution is \((12,3,3)\). Here
\[
\gcd(h_3,g_1)=X-4,\qquad g_1'(4)=3,
\]
so the middle witness \(z\) reduces to 4, but a further precision argument is essential. After substitution, the three exact expressions \(F(u),H_3F(u),F'(1)\) are coefficientwise divisible by 13 in \(\mathbf Z[r,l,k]\). Their divided polynomials reduce to the three affine equations above, whose coefficient matrix has determinant 3. Apply the bound again at \((12,3,3)\), obtaining
\[
r-12,\ l-3,\ k-3\in13O.
\tag{S23}
\]
It follows that the monic middle derivative evaluated at 4 lies in \(13O\); its derivative there is a unit. The one-variable bound gives \(z-4\in13O\). But the exact expansion is
\[
\overline{F(4)/13}
=10\bar r+8\bar l+5\bar k+3=6.
\]
Since \(F'(4),H_2F(4)\in13O\), Taylor expansion implies \(F(z)-F(4)\in13^2O\), contradicting \(F(z)=0\). This excludes row 3, completing the proof for C and hence Proposition A.

## A.8. Exact certificate dependencies and their scope {.unnumbered}

For the accompanying evidence tree, let \(E\) denote `evidence/seven-terms`.
Within \(E\), let \(P\) denote `dependencies/casas-alvero-sixterm`.
Within \(P\), let \(Q\) denote `dependencies/casas-alvero-structural`
and \(R\) denote `dependencies/casas-alvero-extension`.
These aliases locate coefficient data; they do not introduce additional proof assumptions.

| Mathematical item | Exact data / replay, relative to the indicated directory |
|---|---|
| Support sieve (S2)–(S4), five A–E supports | \(Q\): sixterm/old-baseline-and-groups.json; sixterm/old_baseline_and_groups.py; sixterm/enumerate_sixterm.py; sixterm/apply_two_visible.py |
| Lemma A.3 remainder (S6) | \(R\): check_mod13_explanation.py |
| Lemma A.4 resultant and displayed Bézout identity | \(Q\): sixterm/last-mask-probe.json; sixterm/verify_last_mask.py |
| Lemma A.5 identities (S9), (S10) and resultant arrays | \(P\): B/certificate.json; B/verify_certificate.py |
| A boundary ideal identity (S11) | \(P\): A/seed13-a-zero-certificate.txt; A/check_seed_certificates.py zero |
| A univariate classification (S12) | \(P\): A/seed13-univariate.txt; A/check_seed_univariate.py |
| A characteristic-zero resultants of (S13) | \(P\): A/collision-resultants.log; A/check_collision_resultants.py |
| C classification identities (S16), (S17) | \(P\): C/univariate-certificate.json; C/verify_univariate.py |
| C exact jets and gcds (S18)–(S23) | \(E\): u_one/check_jets.py; cluster/check_jets.py; u_equals_v/check_jets.py |
| Separate C arithmetic reconstructions | \(E\): u_one/check_u_equals_v_audit.py; structural_audit/check_independent_jets.py |
| Complete package and six-row coverage replay | \(E\): replay.py; case_coverage.json; MANIFEST.json |

The B certificate has SHA-256
981ff911b8493e9a3cb37dea620dd63249e6bd2bff9c93f16aec2670e88179c7.
The package manifest fixes the other certificate bytes. The B and C resultant replays share a finite-field arithmetic implementation; their independence is from the Singular producer, not from each other. The C jet computations have additional separately written reconstructions.

The theorem depends on the written normalization, denominator, degeneration, root-cluster, and precision arguments, as well as the finite identities. A PASS receipt alone does not establish those arguments. Conversely, the elementary implications do not excuse an unchecked resultant identity. The optional large characteristic-zero resultant proof of C, exploratory Gröbner outputs, and older modular finite-module certificates are not dependencies of this proof.

This is a proof dependency consolidation of an existing result. It makes no assertion of historical novelty, publication significance, external refereeing, proof-assistant verification, or a solution in unrestricted degree 20.



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


# References

**[CLO]** W. Castryck, R. Laterveer and M. Ounaïes, *Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12*, Mathematics of Computation **83** (2014), no. 290, 3017–3037. [DOI: 10.1090/S0025-5718-2014-02809-3](https://doi.org/10.1090/S0025-5718-2014-02809-3). Proposition numbering here follows [arXiv:1208.5404v1](https://arxiv.org/abs/1208.5404v1), 27 August 2012; the mean-root and determinant input is Theorem 2.

**[deFrutos]** R. M. de Frutos Marín, *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, doctoral thesis, Universidad de Valladolid, 2013. [DOI: 10.35376/10324/3602](https://doi.org/10.35376/10324/3602). The singleton and two-visible-position criteria are discussed in Sections 2.3 and 3.5, particularly Proposition 3.5.5.

**[Massri]** C. Massri, *The Casas-Alvero conjecture for three recycled roots in degree 20*, [arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6), 25 August 2023. Unrefereed preprint; recycled-root count differs from monomial count.

**[Marashdeh]** M. F. Marashdeh, *A descent-set obstruction for the Casas–Alvero conjecture*, [arXiv:2608.14726v1](https://arxiv.org/abs/2608.14726v1), 12 August 2026. Unrefereed preprint.

**[Ghosh]** S. Ghosh, *Proof of the Casas-Alvero conjecture*, [arXiv:2501.09272v2](https://arxiv.org/abs/2501.09272v2), 21 March 2026. Unrefereed all-degree proof claim, cited for context and not used as a premise.

**[Bothmer-et-al]** H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. van de Woestijne, *The Casas-Alvero conjecture for infinitely many degrees*, Journal of Algebra **316** (2007), 224–230. [DOI: 10.1016/j.jalgebra.2007.06.017](https://doi.org/10.1016/j.jalgebra.2007.06.017); [arXiv:math/0605090v2](https://arxiv.org/abs/math/0605090v2).

**[Berger]** L. Berger, *The Weierstrass preparation theorem and resultants of p-adic power series*, [arXiv:1910.05319v2](https://arxiv.org/abs/1910.05319v2), 4 November 2019, Section 1 and Corollary 1.2.

**[Draisma–de Jong]** J. Draisma and J. P. de Jong, *Erratum/addition for On the Casas-Alvero conjecture*, August 2011. [Author-hosted erratum](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf). It retracts the earlier degree-twenty consequence; this does not adjudicate later proof claims.

**[ProofAtlas]** *Casas–Alvero conjecture*, [collaboration page](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/), accessed 24 September 2026. Equivalence of its reported systems to the present theorem was not established.

**[Shih]** C.-P. Shih, *On the Casas-Alvero Conjecture*, master's thesis, National Tsing Hua University, 2022. [Catalog record](https://etd.lib.nycu.edu.tw/cgi-bin/gs32/hugsweb.cgi?o=dnthucdr&s=id%3D%22G021090215100%22.&searchmode=basic). Full text unavailable in the bounded comparison.

