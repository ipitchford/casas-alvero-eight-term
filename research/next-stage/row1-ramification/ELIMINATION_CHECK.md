# Exact row-1 elimination and its ramification residual

This note certifies the finite arithmetic used in **ROW1_RAMIFICATION.md**. The root-cluster argument that forces the relevant common-root collision is a separate prerequisite. In particular, the equation \(Q=0\) cannot be imposed merely because \(x\) is a common root of \(f\) and \(G_{16}\).

## 1. Reconstructed eliminated polynomials

First discard \(a_6,a_{10}\), whose effects are restored exactly below. Put \(t=a_3\), and impose
\[
u=a_{16}=-x^{16}-560t x^{13}.
\]
The normalized conditions \(H_3f(1)=f(1)=0\) give
\[
f=X^{20}+1140tX^{17}+4845uX^4+DX^3+EX,
\]
\[
D=-1140-775200t-19380u,\qquad
E=-1-1140t-4845u-D.
\]
After substituting \(u\), direct evaluation gives
\[
f(x)/x=P_0(x)+tP_1(x),\qquad
f'(x)-f(x)/x=Q_0(x)+tQ_1(x),
\]
where the exact integer polynomials are
\[
P_0=-4844X^{19}+19380X^{18}-14535X^{16}-1140X^2+1139,
\]
\[
P_1=-2712060X^{16}+10852800X^{15}-8139600X^{13}
     -775200X^2+774060,
\]
\[
Q_0=-14516X^{19}+38760X^{18}-2280X^2,
\]
\[
Q_1=-8121360X^{16}+21705600X^{15}-1550400X^2.
\]
In particular,
\[
Q_1(1)=12033840\equiv16\pmod{17}.
\]
Thus \(Q_1(x)\) is a unit whenever \(x\equiv1\).

Let \(R=P_0Q_1-Q_0P_1\), and write \(R(1+z)=\sum r_kz^k\). Its degree is 35, and its exact order at \(z=0\) is two. The complete coefficient-valuation pattern is

| Powers \(k\) | \(\nu_{17}(r_k)\) |
|---|---:|
| 0, 1 | \(+\infty\), coefficients exactly zero |
| 2 | 1 |
| 3 | 2 |
| 4 through 16 | 1 |
| 17 through 19 | 0 |
| 20 | 1 |
| 21 | 2 |
| 22 through 33 | 1 |
| 34, 35 | 0 |

The leading coefficients for the relevant slope are
\[
r_2/17\equiv7,\qquad r_{17}\equiv16=-1\pmod{17}.
\tag{1}
\]
All expanded integer coefficient arrays, including \(R\) before and after translation, are retained in **row1-elimination-certificate.json**.

## 2. Exact accounting for the omitted coefficients

Now retain \(v=a_6\) and \(b=a_{10}\). The exact equation \(G_{16}(x)=0\) gives
\[
u=-x^{16}-560tx^{13}-8008vx^{10}-8008bx^6.
\tag{2}
\]
Include the ordinary terms \(\binom{20}{6}vX^{14}\) and \(\binom{20}{10}bX^{10}\), and solve \(H_3f(1)=f(1)=0\) again. Linearity gives exact identities
\[
f(x)/x=P_0+tP_1+vP_6+bP_{10},
\]
\[
f'(x)-f(x)/x=Q_0+tQ_1+vQ_6+bQ_{10},
\tag{3}
\]
with all four error polynomials coefficientwise divisible by 17. Their full arrays are included in the certificate and reconstructed by the independent checker.

The intended coefficient bounds are
\[
\nu(v)\ge3,\qquad \nu(b)\ge5,
\tag{4}
\]
Thus, at an integral \(x\), their contributions to (3) have valuation at least four. The discarded part of \(u\) in (2) has valuation at least three, and its ordinary binomial multiplier has valuation one; this yields the same lower bound.

Once the separate collision argument has established \(f(x)=f'(x)=G_{16}(x)=0\), equations (3) and (4) imply
\[
\nu(P_0(x)+tP_1(x))\ge4,\qquad
\nu(Q_0(x)+tQ_1(x))\ge4.
\]
Since the multipliers \(P_1,Q_1\) are integral, \(\nu(R(x))\ge4\).

The finite certificate also records a stronger cancellation. Define
\[
L_j=Q_1P_j-P_1Q_j,\qquad j=6,10.
\]
Both satisfy
\[
L_j(1+z)=17z^2A_j(z),\qquad A_j\in\mathbf Z[z],
\tag{5}
\]
with \(\deg A_6=27\), \(\deg A_{10}=23\). There is a structural reason for the factor \(z^2\): the normalizations give \(P_j(1)=0\) and \(P_j'(1)=Q_j(1)\), also for \(j=0,1\). The value and first derivative of each eliminant therefore vanish at 1. The factor 17 comes from the middle ordinary binomial multipliers. The checker verifies (5) coefficient by coefficient.

When \(z=x-1\ne0\), (3) consequently yields the exact equation
\[
\frac{R(1+z)}{z^2}+17\bigl(vA_6(z)+bA_{10}(z)\bigr)=0.
\tag{6}
\]
The division is justified only in this nonzero-displacement case. Neither (6) nor the factorization of \(R\) itself supplies an exclusion for \(x=1\) before the collision analysis.

## 3. The scaled residual polynomial

Choose \(\pi\) with \(\pi^{15}=17\), so \(\nu(\pi)=1/15\). Because the exact factor \(z^2\) has been cancelled, the expression
\[
\mathcal S(Z)=\frac{R(1+\pi Z)}{17\pi^2Z^2}
 =\sum_{k=2}^{35}\frac{r_k\pi^{k-2}}{17}Z^{k-2}
\]
is a polynomial, not merely a rational function. The coefficient table proves
\[
\nu(r_k)+(k-2)/15-1\ge0,
\]
with equality exactly at \(k=2,17\). Thus \(\mathcal S\) is integral over \(\mathbf Q_{17}(\pi)\), and (1) gives its complete reduction:
\[
\overline{\mathcal S}(Z)=7-Z^{15}.
\tag{7}
\]
There are no additional initial terms. The checker computes every rational coefficient weight and verifies this assertion.

If \(0<\nu(z)\) and the exact error equation (6) holds with \(v,b\in\mathfrak m\), the same table already forces \(\nu(z)=1/15\): below that value the \(z^{15}\) term of \(R(1+z)/z^2\) is uniquely smallest, and above it the constant term is uniquely smallest. The error terms have valuation greater than one. This deduction is conditional on the repeated-root equation in (3); it does not replace the earlier proof that a repeated root coincides with the selected \(G_{16}\) root.

For the intended \(\nu(z)=1/15\), \(Z=z/\pi\) is a unit. The coarse bound \(\nu(R(x))\ge4\) gives
\[
\nu(\mathcal S(Z))\ge4-1-2/15=43/15.
\]
The exact factors (5) actually give the stronger bound \(\nu(\mathcal S(Z))\ge3\) under (4); the proof may retain its weaker sufficient estimate.

Every root of (7) is simple: its derivative is \(-15Z^{14}\), nonzero at any root because the constant 7 is nonzero. Moreover \(5^{15}=7\) in \(\mathbf F_{17}\), and \(15\mid17^4-1\). Hence all fifteen roots lie in \(\mathbf F_{17^4}\). The checker verifies both scalar identities and \(\operatorname{ord}_{15}(17)=4\). These facts support the separate Hensel and value-group step in the proposed proof; they do not establish that step merely by a numerical root calculation.

## 4. The complete eight-choice first-divided check

Assume the separately proved \(\nu(t)=\nu(a_3)\ge3/2\). Then its contribution to \(f'(1)/17\) has positive valuation and disappears in the residue field. The middle active indices are \(J=\{6,10,16\}\); each marked common-root residue is 0 or 1, and inactive indices choose zero. Starting with \(a_0=1\), all coefficient residues are determined by
\[
\bar a_j=-\sum_{i<j}\binom ji\bar a_iw_j^{j-i}.
\]
The necessary divided condition is
\[
W=-133+\sum_{j\in J}
\left((19-j)-2\binom{20-j}{3}\right)
\frac{\binom{20}{j}}{17}\bar a_j=0.
\]
Its three weights modulo 17 are \(15,1,3\). All eight assignments give:

| \((w_6,w_{10},w_{16})\) | \((\bar a_6,\bar a_{10},\bar a_{16})\) | \(W\) |
|---|---|---:|
| \((0,0,0)\) | \((0,0,0)\) | 3 |
| \((0,0,1)\) | \((0,0,16)\) | 0 |
| \((0,1,0)\) | \((0,16,0)\) | 2 |
| \((0,1,1)\) | \((0,16,0)\) | 2 |
| \((1,0,0)\) | \((16,0,0)\) | 5 |
| \((1,0,1)\) | \((16,0,0)\) | 5 |
| \((1,1,0)\) | \((16,5,0)\) | 10 |
| \((1,1,1)\) | \((16,5,12)\) | 12 |

Thus only \(\bar a_{16}=-1,\bar a_6=\bar a_{10}=0\) survives. The checker derives \(W\) independently by constructing the ordinary polynomial, solving its two normalization equations, and differentiating at 1. It also checks the simplified weight formula and every marked normalized derivative.

## Replay and exact scope

The certificate producer used direct formulas and binomial translation. The independent standard-library checker **check_row1_elimination.py** instead constructs \(f\) as a polynomial in \(X\), differentiates it, evaluates at \(x\), and translates \(R\) by Horner composition with \(1+z\). It checks all source arrays, the integer eliminant, every coefficient valuation, the factors \(17z^2\) in both error directions, the scaled initial terms, and all eight markings. A changed eliminant coefficient is rejected. Checks use explicit exceptions and remain active under optimization.

Normal and optimized replay pass with identical receipts:

    python3 -B check_row1_elimination.py
    python3 -B -O check_row1_elimination.py

The files are **row1-elimination-certificate.json**, **verification.json**, and **verification-optimized.json**. Certificate SHA-256:

    68f783490d20f46b0defb1e221e0c16a32e6904e248aeba86dcf11954001e2d4

These certify the finite algebraic ingredients. The global seed coverage, small-root valuation bounds, forced repeated-root collision, and final value-group contradiction remain mathematical arguments to be audited in **ROW1_RAMIFICATION.md**. In particular no condition \(f'(1)=0\) has been added in the exact-\(x=1\) case.
