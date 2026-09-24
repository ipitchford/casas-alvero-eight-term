# A uniform exclusion in the wild characteristic-seventeen row-1 stratum

24 September 2026. The argument and exact-certificate audits have passed; see ROW1_AUDIT.md. This file does not alter the frozen review package. Its intended conclusion is a uniform residue-stratum exclusion, not the exclusion of all of row 1 or degree twenty.

## Statement

Let \(f\) be a nontrivial degree-twenty characteristic-zero CA polynomial, integrally normalized over a valued algebraic extension of \(\mathbf Q_{17}\), with
\[
f=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},\qquad a_0=1,\quad a_1=a_{20}=0.
\]
Normalize \(\nu(17)=1\). Suppose
\[
a_2=a_3=a_4=a_{18}=0,\qquad
\bar f=X^{20}-X^3,
\]
and
\[
\bar a_5=\cdots=\bar a_{15}=0,\qquad \bar a_{16}=-1.
\tag{R1}
\]
**Theorem.** No such polynomial exists. The coefficients at indices 5 through 15 may be arbitrary integral coefficients subject to their residue condition, including zero; there is no bound on their number. Ramification is unrestricted.

For the global exact-support applications below, algebraic specialization is performed before selecting a valuation stratum; it is not asserted to preserve an arbitrarily chosen valuation stratum. It loses no complex exact-support candidate: impose the common-root equations and inverses for required nonzero coefficients, specialize a proper rational ideal to an algebraic point, and then extend the valuation. The integral normalization and its support preservation are proved in the existing manuscript. Its short characteristic-nineteen argument also shows the mean root is simple. Thus the exact linear coefficient below is nonzero.

## 1. Normalization and the small root cluster

Put \(C_j=\binom{20}{j}\), \(u_j=a_j\) for \(5\le j\le16\). The ordinary Hasse third derivative of the residue polynomial is \(X^{17}-1\); its common witness is a unit reducing to one. Scale that exact witness to one. This scaling preserves the residue seed, coefficient zeros, and (R1). Therefore \(f(1)=H_3f(1)=0\), and
\[
f=X^{20}+\sum_{j=5}^{16}C_ju_jX^{20-j}+DX^3+EX,
\]
\[
D=-1140-\sum_{j=5}^{16}\binom{20-j}{3}C_ju_j,
\qquad
E=-1-\sum_{j=5}^{16}C_ju_j-D.
\tag{R2}
\]
Each \(C_j\) in this sum is divisible by 17. Consequently \(D\) is a unit, \(E\in17O\), and \(E\ne0\) by simplicity of the mean. The three-root zero residue cluster consists of zero and two nonzero roots. If \(t\) is either nonzero root and \(\delta=\nu(t)>0\), the equation
\[
0=f(t)/t=E+Dt^2+\sum_{j=5}^{16}C_ju_jt^{19-j}+t^{19}
\]
has all terms other than \(E,Dt^2\) of valuation strictly greater than \(2\delta\). Hence
\[
\nu(t)=\tfrac12\nu(E)\ge\tfrac12.
\tag{R3}
\]
This also follows from the Newton polygon, with exactly two such roots counted with multiplicity.

No repeated root lies in this cluster. A nonzero repeated root \(t\) would satisfy
\[
0=f'(t)-f(t)/t
=2Dt^2+\sum_{j=5}^{16}(19-j)C_ju_jt^{19-j}+19t^{19},
\]
whose first term has uniquely least valuation. Zero is simple. Thus every common witness for \(f,f'\) lies in the seventeen-root cluster reducing to one.

For \(5\le j\le15\), the monic normalized derivative
\[
G_j=\sum_{i=0}^{j}\binom ji a_iX^{j-i}
\]
reduces to \(X^j\). Its common witness reduces to zero. If \(a_j=0\), choose zero as its exact witness; otherwise its witness is a nonzero root covered by (R3). Induction in \(j\), using the coefficient one on \(a_j\), proves
\[
\nu(u_j)\ge j/2\ge5/2\quad(5\le j\le15),
\tag{R4}
\]
with the usual convention \(\nu(0)=+\infty\).

## 2. A forced exact collision in the large cluster

Write \(u=u_{16}\). Let \(x\) be a common root of \(f,G_{16}\). Since \(\bar G_{16}=X^{16}-1\), necessarily \(x\equiv1\). Equation (R4) gives
\[
u=-x^{16}+e,\qquad \nu(e)\ge5/2.
\tag{R5}
\]

Expand \(f(1+Y)=\sum_{k=1}^{20}c_kY^k\). Direct substitution in (R2) gives
\[
\begin{aligned}
c_1&=17(-133-1425u)+e_1,\\
c_2&=17(-190-1710u)+e_2,\\
c_3&=0,\\
c_4&=4845(1+u)+e_4,
\end{aligned}
\tag{R6}
\]
where every \(e_i\) has valuation at least \(7/2\). Further,
\[
c_k\in17O\ (5\le k\le16),\quad
(c_{17},c_{18},c_{19},c_{20})=(1140,190,20,1).
\]
In particular \(\nu(c_2)=1\), with \(\overline{c_2/17}=7\).

Let \(z=x-1\). If \(0<\epsilon=\nu(z)<1\), (R5) gives
\[
u+1=-16z+O(z^2)+e.
\]
Using \(-133+1425=17\cdot76\), \(-1425\equiv3\), and \(-16\equiv1\pmod{17}\), the first two terms of \(f(x)/z\), divided by 17, have leading sum \(10z\). The degree-seventeen term has valuation \(16\epsilon-1\); every other term has greater valuation than the smaller of these two values. Cancellation forces
\[
\epsilon=1/15.
\tag{R7}
\]
Choose \(\pi\) with \(\pi^{15}=17\), extending the field if necessary, and put \(\xi=\overline{z/\pi}\ne0\). The initial polynomial of \(f(1+\pi Y)/\pi^{17}\) on the seventeen-root cluster is
\[
L(Y)=Y^{17}+7Y^2+3\xi Y,
\qquad \xi^{15}=7.
\tag{R8}
\]
The equality for \(\xi\) follows by substituting the known root \(x\). Every other displacement in the seventeen-root cluster has valuation at least \(1/15\): at a smaller positive valuation the degree-seventeen term would be uniquely least. Thus the initial polynomial captures the entire cluster, not merely its already selected root. The only root of \(L'\) is \(Y=\xi\), since \(14=-3\) in characteristic 17. It is a double root of \(L\): \(H_2L=7\ne0\). All other roots of \(L\) are simple. These multiplicities describe actual root clusters, with the three roots originally reducing to zero contributing units to this local factor.

An exact repeated root \(w\) of \(f\) must lie in the double cluster reducing to \(\xi\). That cluster already contains the root \(x\), so its multiplicity two forces \(w=x\) exactly.

If instead \(\nu(z)\ge1\), including \(z=0\), equations (R5)–(R6) give \(\nu(c_1)\ge2\), \(\nu(c_2)=1\). The Newton polygon has fifteen roots with displacement valuation \(1/15\), whose nonzero scaled residues satisfy \(Y^{15}+7=0\). They are simple, as the initial polynomial \(Y^{17}+7Y^2\) has derivative \(14Y\). The remaining two roots in the unit cluster have displacement valuation at least one, counted with multiplicity; one is exactly one and the other includes \(x\). A repeated root must belong to this two-root inner cluster. Root counting forces \(w=x=1\). Thus in every case
\[
f(x)=f'(x)=G_{16}(x)=0.
\tag{R9}
\]
The case distinction exhausted all positive valuations and the exact root one. No discreteness assumption on displacements was used.

## 3. Integral identity contradiction

By (R4), the contributions from indices 5 through 15 to \(f\), \(f'\), \(D\), and \(E\) have valuation at least \(7/2\). Replacing \(u\) by \(-x^{16}\) changes those equations by terms of valuation at least \(7/2\), since its ordinary multiplier \(C_{16}=4845\) has valuation one. Evaluating (R9) therefore gives
\[
\nu(P(x))>3,\qquad\nu(Q(x))>3,
\]
where
\[
\begin{aligned}
P(X)&=-4844X^{19}+19380X^{18}-14535X^{16}-1140X^2+1139,\\
Q(X)&=-14516X^{19}+38760X^{18}-2280X^2.
\end{aligned}
\tag{R10}
\]
Here \(P\) is \(f(x)/x\) after the replacement, and \(Q\) is \(f'(x)-f(x)/x\). The independently checked integer polynomial identity
\[
A(X)P(X)+B(X)Q(X)=D_0,
\quad A,B\in\mathbf Z[X],\quad \nu_{17}(D_0)=3
\tag{R11}
\]
is supplied in `row1-certificate.json`. Since \(x\) is integral, both terms on the left have valuation strictly greater than three, whereas the right has valuation three. This is impossible and proves the theorem.

## 4. A necessary first divided condition without (R1)

For applications take the same exact coefficient zeros, but allow arbitrary middle residues. Normalize the Hasse-third witness to one as in (R2). The zero-cluster argument excluding repeated roots still applies. The coefficients \(c_1,\ldots,c_{16}\) of \(f(1+Y)\) lie in \(17O\), and \(c_{17}\) is a unit. Because one is an exact root, every other root in its residue cluster has displacement valuation at least \(1/16\). At any repeated root \(w\equiv1\), every term of \(f'(w)-f'(1)\) has valuation greater than one: for orders 2 through 16 this follows from \(c_k\in17O\), for order 17 from the extra factor 17, and for orders at least 18 from \(17/16>1\). Hence
\[
0=\overline{f'(1)/17}
=-133+\sum_{j=5}^{16}\left(19-j-2\binom{20-j}{3}\right)
\frac{C_j}{17}\bar u_j.
\tag{R12}
\]
For each active middle index its witness reduces to zero or one; inactive indices may choose exact zero. The triangular normalized derivative recurrence reconstructs every coefficient residue from these binary choices.

For \(J=\{7,8,10,16\}\) and \(J=\{6,10,15,16\}\), the complete sixteen-choice check in each case leaves only \(\bar u_{16}=-1\) and every earlier middle residue zero. The uniform theorem excludes it. The complete characteristic-seventeen seed classification permits only row 1 for the exact centered supports
\[
\{7,8,10,16,17,19\},\qquad\{6,10,15,16,17,19\}.
\]
Thus, conditional only on the already audited global seed classification and the new checked proof above, both exact seven-term supports are globally excluded. This would reduce the current eight-support frontier to six, without establishing an eight-term lower bound.

## Verification boundary

The integral identity, the small binary census, and the valuation/collision proof are separate obligations. This theorem is not accepted on the basis of a symbolic resultant being nonzero alone. It uses the exact valuation-three identity and the strict perturbation estimate above it. The argument audit is closed and the exact identity and census pass normal and optimized replay. This research result has not been incorporated into the delivered paper, in accordance with the instruction to finish the research before producing another manuscript.
