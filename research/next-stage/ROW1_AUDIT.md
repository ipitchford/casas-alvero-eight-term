# Independent argument audit of the row-1 unit-index-16 exclusion

24 September 2026. **Mathematical verdict: PASS under the exact hypotheses
of ROW1_UNIT16.md**, with the full-cluster coverage argument supplied
explicitly below. This is an internal research audit, not external
refereeing, formal verification, or an assessment of significance.

The reviewed draft of ROW1_UNIT16.md has SHA-256

    7d9b69d47f6f0fe2f11e4efea43c6aedb2be6e51175ad6a7ce50f73ad2bea372

The certificate reviewed has SHA-256

    e43bd1bf6710a1ae682e1603d82137ed26e43b2d83e47a25a38b5aa8868d928e

The audit covers the uniform theorem, the first divided condition in
Section 4, and its two specified support applications. It does not
exclude every row-1 lift.

## 1. Exact hypotheses and normalization

The assumptions are exact
\(a_2=a_3=a_4=a_{18}=0\), row-1 ordinary reduction
\(\bar f=X^{20}-X^3\), and residue conditions
\(\bar a_5=\cdots=\bar a_{15}=0,\bar a_{16}=-1\).
The coefficients at indices 5 through 15 may be zero or nonzero;
no hidden support-size bound is needed.

The Hasse-third witness is a unit with residue one because the
common-root polynomial in the residue field is \(X^{17}-1\).
Scaling that actual witness to one is a unit scaling, preserves all
coefficient zero patterns and residue conditions, and justifies both
\(f(1)=0\) and \(H_3f(1)=0\) simultaneously.
The displayed eliminations of the cubic and linear coefficients
follow directly. Every \(C_j\) for \(5\le j\le16\) is divisible by
17, so \(D\) is a unit and \(E\in17O\).

The exact mean is simple by the previously proved prime-19 argument;
thus \(E\ne0\). In the two exact support applications this also follows
directly from the stipulated nonzero linear coefficient.
Algebraic specialization preserves exact support by a product-inverse
equation. It need not preserve a previously selected valuation stratum:
the global applications instead specialize first and then rederive
row 1 and its residue constraints. This is the correct order.

## 2. The zero cluster and strict perturbation bounds

For a nonzero root \(t\) reducing to zero, put \(\delta=\nu(t)>0\).
In \(f(t)/t\), the unit quadratic term \(Dt^2\) has valuation
\(2\delta\); all terms except it and \(E\) have greater valuation.
The equality therefore forces
\[
2\delta=\nu(E)\ge1.
\]
Thus both nonzero roots in that three-root cluster have valuation
at least \(1/2\), without assuming integral valuations.

The expression \(f'(t)-f(t)/t\) has unique lowest term \(2Dt^2\).
Consequently both nonzero roots are simple. The exact root zero is
also simple, so every repeated root of \(f\) belongs to the unit
cluster. This is an essential bridge before the later cluster count.

For \(5\le j\le15\), the normalized derivative reduces to \(X^j\).
Its witness therefore reduces to zero. At an inactive coefficient
one may choose the exact witness zero. At every other index the
witness has valuation at least \(1/2\). Induction in the full
normalized derivative equations yields
\[
\nu(u_j)\ge j/2.
\]
This proves the strict estimate needed later:
every contribution of these parameters to an ordinary coefficient
of \(f\), its derivative, \(D\), or \(E\) has valuation at least
\(1+5/2=7/2>3\).

Hence, coefficientwise up to an error of valuation at least \(7/2\),
\[
F_u=X^{20}+4845uX^4-(1140+19380u)X^3+(1139+14535u)X.
\]
The \(G_{16}\) witness \(x\) reduces to one: its residue derivative
is \(X^{16}-1\), and the row-1 seed has only zero and one as roots.
The recurrence gives \(u=-x^{16}+e\), with \(\nu(e)\ge5/2\).

The first Taylor coefficients at one were independently reconstructed:
\[
\begin{array}{c|rrrrr}
k&0&1&2&3&4\\ \hline
\text{constant part}&0&-2261&-3230&0&4845\\
\text{coefficient of }u&0&-24225&-29070&0&4845.
\end{array}
\]
They agree with (R6). The exact vanishing of \(c_3\) follows from
the selected Hasse-third witness, not a truncation.

## 3. The full seventeen-root cluster is captured

Write \(z=x-1\). If \(0<\epsilon=\nu(z)<1\), the two potentially
lowest contributions to \(f(x)/z\) have valuations \(1+\epsilon\)
and \(16\epsilon\). Their coefficients are respectively
\(17\cdot10z\) and \(1140z^{16}\) at leading order.
All discarded terms have strictly greater valuation than the
smaller of these two values. Therefore
\[
\epsilon=1/15.
\]
For \(\pi^{15}=17\), \(\xi=\overline{z/\pi}\ne0\) satisfies
\(\xi^{15}=7\).

The final draft includes the full-cluster coverage bridge. Its detailed
justification, checked in this audit, is as follows.
For any other unit-cluster root \(r\ne1\), let
\(\eta=\nu(r-1)>0\). If \(\eta<1/15\), the term
\(c_{17}(r-1)^{17}\) is uniquely lowest in \(f(r)\):

- \(c_1\) has valuation \(16/15\), so its term has value
  \(16/15+\eta>17\eta\);
- \(c_2\) has valuation one, so its term has value
  \(1+2\eta>17\eta\);
- \(c_3=0\), and \(c_4\) has valuation \(16/15\);
- for \(5\le k\le16\), the term has value at least
  \(1+k\eta>17\eta\);
- the terms of degree at least eighteen have greater value.

Thus every root of the unit cluster satisfies
\(\nu(r-1)\ge1/15\). Scaling captures all seventeen roots, with
multiplicity, not merely the selected witness \(x\). The three
roots from the original zero cluster give a factor whose reduction
at \(1+\pi Y\) is the constant one. The remaining monic degree-seventeen
factor therefore has initial polynomial
\[
L(Y)=Y^{17}+7Y^2+3\xi Y.
\]
Its unique critical root is \(\xi\), and \(H_2L=7\ne0\), so this
root has multiplicity exactly two. Every other root is simple.
Any exact repeated root \(w\) must reduce to this double root.
The same cluster already contains \(x\). If \(w\ne x\), their
multiplicities would total at least three, contradicting the
initial multiplicity two. Therefore \(w=x\) exactly.

If \(z=0\) or \(\nu(z)\ge1\), the analogous coefficient bounds give
\[
L(Y)=Y^{17}+7Y^2=Y^2(Y^{15}+7).
\]
The same unique-lowest-term argument excludes displacements of
valuation less than \(1/15\). Its fifteen nonzero roots are simple.
The two roots in the zero scaled-residue class have displacement
valuation at least one: a value strictly between \(1/15\) and one
would make \(c_2(r-1)^2\) uniquely lowest, since \(\nu(c_1)\ge2\).
This also covers \(c_1=0\), with the exact root one counted at its
actual multiplicity.

Thus a repeated root must lie in this two-root inner cluster.
If \(x\ne1\), the distinct roots one and \(x\), together with any
repeated root in that cluster, would require at least three roots
counted with multiplicity. Hence \(x=1\), and the same count forces
\(w=1\). In both cases \(f(x)=f'(x)=G_{16}(x)=0\).

These arguments use only valuations, polynomial factorization and
root multiplicities. No unramified-field assumption or integer
displacement valuation is present.

There is an optional simplification in the second case: \(x=1\)
gives \(\nu(u+1)\ge5/2\), whence
\(f'(1)=17^2\cdot76+\text{error of valuation at least }7/2\ne0\).
The general certificate argument below already suffices.

## 4. Exact certificate and valuation contradiction

I independently formed \(P\) from \(F_u(X)/X\) at \(u=-X^{16}\),
and \(Q\) from \(F_u'(X)-F_u(X)/X\) with the same substitution.
Both agree coefficientwise with (R10). The strict perturbation
bound proves \(\nu(P(x)),\nu(Q(x))\ge7/2>3\).

Without using polynomial division or a symbolic gcd result, I read
the supplied integer coefficient arrays and multiplied them by
direct integer convolution. The resulting identity is exactly
\[
AP+BQ=D_0,
\]
with
\[
D_0=
2347990055314667642830371373680474152955750087350688785027939089482846402772.
\]
Repeated integer division gives
\(\nu_{17}(D_0)=3\) and \(D_0/17^3\equiv13\pmod{17}\).
Both multiplier degrees are eighteen. Evaluating at the integral
root \(x\) makes \(A(x)\) and \(B(x)\) integral. The left side then
has valuation greater than three, in contradiction with the
right side. This completes the exclusion under (R1).

## 5. Section 4 and the two support corollaries

The preliminary divided condition without (R1) is also valid.
The ordinary reduction at one makes \(c_1,\ldots,c_{16}\in17O\)
and \(c_{17}\) a unit. Since one is an exact root, another
unit-cluster root has displacement valuation at least \(1/16\);
below that radius the seventeenth-degree term is uniquely lowest.
At a repeated unit root \(w\), every summand in
\(f'(w)-f'(1)\) has valuation greater than one:
orders 2 through 16 contain a coefficient divisible by 17,
order 17 contains its derivative factor 17, and orders at least
18 have displacement valuation at least \(17/16\).
The case \(w=1\) makes the assertion immediate.

The zero-cluster roots remain simple without (R1), so such a unit
repeated root exists. It follows that \(f'(1)/17\) reduces to zero.
Substituting the two eliminated low coefficients gives exactly
the weights in (R12), including the constant \(-133\).

I independently enumerated all sixteen binary assignments for each
of \(J=\{7,8,10,16\}\) and \(J=\{6,10,15,16\}\), using the full
normalized derivative recurrence and the displayed divided weights.
Each leaves only the label vector \((0,0,0,1)\), with nonzero
residue coefficient \(a_{16}=16=-1\). The other middle residues
are zero, so the hypotheses of the uniform theorem follow.

An inactive exact coefficient can choose the exact zero witness;
an active coefficient must retain both residue labels zero and
one. These binary checks do so. They therefore cover every
candidate rather than only nonzero residue coefficients.

For both exact full supports
\[
\{7,8,10,16,17,19\},\qquad
\{6,10,15,16,17,19\},
\]
the visible indices 2,3,18 are absent exactly. Among the complete
nine-seed table, only row 1 has those three ordinary coefficients
zero and is nonmonomial. The retained unit root excludes monomial
reduction. Scaling preserves exact support. Consequently the two
support corollaries are global, conditional on the already audited
classification dependency. No other support is removed by this audit.

## 6. Optional uniform two-residue consequence

Under the same exact zeros \(a_2=a_3=a_4=a_{18}=0\) and row-1
reduction, at least two of the middle coefficient residues
\(\bar a_5,\ldots,\bar a_{16}\) must be nonzero.

If all vanish, (R12) becomes \(-133=3\ne0\) in the residue field.
If exactly one, \(\bar a_j\), is nonzero, the first such normalized
derivative is \(X^j+\bar a_j\). Its common witness cannot reduce
to zero, so it reduces to one and \(\bar a_j=-1\).
This argument does not assume that all other derivative witnesses
are in the zero cluster; it only uses the coefficient zero pattern.
Substitution into (R12), for \(j=5,\ldots,16\), gives respectively
\[
16,\ 5,\ 16,\ 12,\ 11,\ 2,\ 7,\ 14,\ 4,\ 5,\ 9,\ 0.
\]
I independently checked these twelve integers. Only \(j=16\)
remains, and it is exactly the residue stratum excluded by the
uniform theorem. This proves the stated consequence.

## Closure

No mathematical defect was found. The final readback includes the
explicit full-cluster coverage in Section 3; the audited source
fingerprint is recorded above. The argument audit is closed as PASS.
The theorem is a uniform
exclusion of the stated residue stratum, and its two support corollaries
reduce the current eight-support list to six. It does not prove the
eight-term lower bound or the degree-twenty conjecture.
