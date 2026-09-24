# Excluding family B in characteristic 13

**Lemma.** Over an algebraically closed field of characteristic 13, the only
polynomial
\[
h(X)=X^{20}+aX^{17}+bX^4+cX^3+dX
\]
that shares a root with every Hasse derivative of orders 1 through 19 is the
monomial \(X^{20}\). Coefficients may vanish, and common-root witnesses may
coincide.

The proof uses the previously checked seed lemma for exponents \(20,4,3,1\),
and two explicit algebraic certificates supplied in `certificate.json`.
`verify_certificate.py` checks the new certificates using only the Python
standard library, including an independent determination of the resultants.

## 1. Normalize only a forced nonzero witness

The chart \(a=0\) is exactly the earlier lemma in
`work/casas-alvero-structural/sixterm/LAST_MASK_PROOF.md`, which includes every
coefficient degeneration. Suppose therefore that \(a\ne0\). Since
\[
H_{17}h=9X^3+a,
\]
a common root with \(h\) is nonzero. Scaling this root to 1 makes \(a=4\),
and \(h(1)=0\) gives
\[
d=-5-b-c.\tag{1}
\]
The relevant remaining derivatives are
\[
\begin{aligned}
H_4h&=9X^{16}+4X^{13}+b,\\
H_3h&=9X^{17}+3X^{14}+4bX+c,\\
H_1h&=7X^{19}+3X^{16}+4bX^3+3cX^2+d.
\end{aligned}\tag{2}
\]
These follow directly from the Hasse binomial formula.

## 2. The complete chart b=0

Choose common-root witnesses \(v,w\) for orders 3 and 1. Neither is assumed
nonzero. Equations (1) and (2) force
\[
c=-9v^{17}-3v^{14},\qquad d=-5-c.
\]
The following three polynomials must vanish:
\[
\begin{aligned}
F_3&=h(v)=v(5v^{19}+v^{16}+d),\\
F_0&=h(w)=w(w^{19}+4w^{16}+cw^2+d),\\
F_1&=H_1h(w)=7w^{19}+3w^{16}+3cw^2+d.
\end{aligned}\tag{3}
\]
The certificate contains polynomials \(L_3,L_0,L_1\in\mathbf F_{13}[v,w]\)
with, respectively, 680, 694, and 712 nonzero monomials, such that
\[
L_3F_3+L_0F_0+L_1F_1=1.\tag{4}
\]
Their sparse arrays are the `bZeroMultipliers` field in `certificate.json`;
each row records `[coefficient, exponent_of_v, exponent_of_w]`.
The replay derives (3) independently from the original polynomial and Hasse
formula, then verifies (4) by direct multiplication and coefficient comparison.
Thus this chart is impossible, including \(c=0\) and \(d=0\).

## 3. Parametrize the chart b≠0

A common root \(u\) with \(H_4h\) is nonzero, because its constant term
is \(b\ne0\). Its derivative equation gives
\[
b=b(u):=4u^{13}(u^3-1).
\]
The equation \(h(u)/u=0\), together with (1), becomes
\[
c(u^2-1)=5+b(u)-5u^{19}.\tag{5}
\]
This division by \(u\) is justified only in the present chart. If \(u=1\),
then \(b=0\), a contradiction. If \(u=-1\), then \(b=8\) and the right
side of (5) equals 5, also a contradiction. Consequently
\(u\ne\pm1\).

Put
\[
q=u+1,\qquad
C=\frac{5+b(u)-5u^{19}}{u-1},\qquad
D=q(-5-b(u))-C.\tag{6}
\]
The numerator defining \(C\) vanishes at \(u=1\), so \(C\) is a
polynomial of degree 18. Equation (5) says that the actual coefficients are
\(c=C/q\) and \(d=D/q\). In particular \(q\ne0\); neither \(C\) nor
\(D\) is assumed nonzero.

Define polynomials in \(X\), with coefficients in \(\mathbf F_{13}[u]\),
\[
\begin{aligned}
P&=q(X^{19}+4X^{16}+bX^3)+CX^2+D,\\
J_3&=q(9X^{17}+3X^{14}+4bX)+C,\\
J_1&=q(7X^{19}+3X^{16}+4bX^3)+3CX^2+D.
\end{aligned}\tag{7}
\]
At a fixed admissible \(u\), these equal \(qh/X,qH_3h,qH_1h\),
respectively. Set
\[
R_3=\operatorname{Res}_X(P,J_3),\qquad
R_1=\operatorname{Res}_X(P,J_1).\tag{8}
\]
If a common root with order 3 is zero, then \(C=0\). If it is nonzero,
then \(R_3=0\). Thus in all cases \(CR_3=0\). Likewise the order-1
condition implies \(DR_1=0\). Keeping these factors explicitly covers both
\(c=0\) and \(d=0\); no common-root witness was divided out in this step.

## 4. An exact univariate contradiction

The resultants have degrees 359 and 395. The arrays `R3` and `R1` in the
certificate list their coefficients in ascending powers of \(u\). The arrays
`bezoutC` and `bezoutD` give polynomials \(A,B\), of degrees 395 and 359,
satisfying
\[
\boxed{A(u)C(u)R_3(u)+B(u)D(u)R_1(u)=(u+1)^{17}.}\tag{9}
\]
This is an identity in \(\mathbf F_{13}[u]\), checked by direct polynomial
multiplication. At any hypothetical CA solution, its left side vanishes and
its right side does not, because \(u\ne-1\). This contradiction completes
the proof of the lemma.

## 5. How the resultants are independently certified

The initial resultants were produced by Singular. The replay does not call
Singular, import the producer, or assume those outputs are correct.

Every coefficient in each polynomial of (7) has \(u\)-degree at most 18:
\(\deg q=1\), \(\deg b=16\), and \(\deg C=\deg D=18\). Their
\(X\)-degrees are 19, 17, and 19. The Sylvester determinant therefore gives
the following bounds, whether or not cancellation occurs:
\[
\deg_u R_3\le17\cdot18+19\cdot18=648,
\qquad
\deg_u R_1\le19\cdot18+19\cdot18=684.\tag{10}
\]

The polynomial \(T^3-T-1\) has no root in \(\mathbf F_{13}\), hence is
irreducible. The checker constructs
\(K=\mathbf F_{13}[T]/(T^3-T-1)\) explicitly. It chooses 685 distinct
elements of \(K\), avoiding \(u=-1\). At each, all three leading
\(X\)-coefficients remain nonzero, and the checker computes both resultants
over \(K\) by the exact Euclidean resultant recurrence. These equal the
evaluations of the supplied arrays at all 685 points. The bounds (10) imply
that the supplied arrays are the exact resultant polynomials. This method is
independent of the producer's polynomial-ring resultant computation.

The checker then multiplies (9) and (4) directly. Mutation controls confirm that
altering a multiplier causes the checked identity to fail. Normal and optimized
Python replay both pass. The certificate SHA-256 is
`981ff911b8493e9a3cb37dea620dd63249e6bd2bff9c93f16aec2670e88179c7`.
The handwritten implications and normalization remain mathematics to be
reviewed separately from these exact arithmetic checks.

## 6. Characteristic-zero support consequence and scope

Apply the established valuation-normalization and Lucas-reduction lemma from
the preceding package. After translating a common root to zero and scaling,
the roots and binomial-normalized coefficients are integral and a unit root
is retained. For a deficiency support contained in
\[
T_B=\{3,8,9,10,11,12,16,17,19\},
\]
reduction in characteristic 13 kills the coefficient indices 8 through 12,
and the reduced polynomial has the closed seed shape in this lemma. The
retained unit root prevents the reduction from being \(X^{20}\), a
contradiction. In particular the centered six-term support
\(\{3,10,16,17,19\}\) is excluded.

This transfer uses valuation normalization; it is not based on affine modular
emptiness alone. The other two remaining six-term supports are not addressed
by this proof. No claim of a seven-term lower bound, a complete degree-20
solution, historical priority, or publication readiness is made.
