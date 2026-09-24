# Independently checked row-5 jet identities

This is a research note for the specified row-5 branches, not a full support exclusion.

Let \(O\) be a valuation ring of characteristic zero with residue characteristic 17, with \(\nu(17)=1\), and let \(\mathfrak m\) be its maximal ideal. All valuation deductions below allow arbitrary ramification.

## 1. General parameters after the common root near −2 is fixed

Put
\[
a_3=-r^3+3r,\qquad a_4=3r^4-6r^2,\qquad b=a_{10},\quad c=a_{12},
\]
and
\[
f=X^{20}-190X^{18}+1140a_3X^{17}+4845a_4X^{16}
 +184756bX^{10}+125970cX^8+EX,
\]
\[
E=189-1140a_3-4845a_4-184756b-125970c.
\]
Define \(F(r;b,c)=f(r)\) and \(H(r;b,c)=f'(1)\). In particular
\[
H=-3211+18240a_3+72675a_4+1662804b+881790c.
\]
Suppose \(F=0\), \(r\equiv-2\pmod{\mathfrak m}\), and \(b,c\in O\). Then \(r+2\in17O\). Indeed \(F(-2;b,c)\in17O\), while the derivative with respect to \(r\) is a unit, reducing to 16. If \(0<\nu(r+2)<1\), Taylor expansion has its linear term uniquely smallest. Hence write \(r=-2+17t\), \(t\in O\).

The substitutions make \(F,H,E\) coefficientwise divisible by 17 in \(\mathbf Z[t,b,c]\). Their first divided reductions are
\[
\begin{array}{c|l}
F/17&3+16t+13b+11c\\
H/17&7+9t+11b+3c\\
E/17&7+9t+12b+2c.
\end{array}
\tag{1}
\]
Thus \(t\equiv3+13b+11c\), and, on \(F=0\),
\[
H/17\equiv9b,\qquad E/17\equiv10b+16c\pmod{17}.
\]
Here congruence modulo \(17O\), not merely modulo \(\mathfrak m\), is justified by the following stronger exact identities. There are integer polynomials \(K_H,K_E\) with
\[
H+9F-153b=17^2K_H(t,b,c),
\]
\[
E+9F-17(10b+16c)=17^2K_E(t,b,c).
\tag{2}
\]
The checker constructs these polynomials by exact coefficientwise division. Their complete coefficient arrays are included in the replay receipt. Their relevant values are
\[
K_H(3,0,0)\equiv5,\qquad K_E(3,0,0)\equiv14\pmod{17}.
\tag{3}
\]

Consequently \(F=H=0\) implies \(b\in17O\): the first identity in (2) gives \(9b=-17K_H\). If in addition \(b,c\in\mathfrak m\), (1) gives \(t\equiv3\pmod{\mathfrak m}\). If moreover \(c\in17O\), write \(b=17B,c=17C\). Equations (2)–(3) give
\[
9\bar B+5=0,\qquad \bar B=7,
\]
\[
\overline{E/17^2}=14+10\bar B+16\bar C=16+16\bar C.
\tag{4}
\]
These are direct polynomial deductions; they do not assume that positive valuation means divisibility by 17.

As a separate check of the implicit description, the unique root at \(b=c=0\) satisfies
\[
r\equiv4095\pmod{17^3},\qquad
H/17^2\equiv5,\quad E/17^2\equiv14.
\]
Implicit differentiation, using the unit denominator \(F_r\), gives
\[
\frac1{17}(H_b^{\mathrm{eff}},H_c^{\mathrm{eff}})\equiv(9,0),
\qquad
\frac1{17}(E_b^{\mathrm{eff}},E_c^{\mathrm{eff}})\equiv(10,16)
\pmod{17}.
\]
The checker also computes the quadratic Taylor coefficients modulo \(17^4\); all are divisible by \(17^2\). These finite derivative checks are supplementary: the exact identities (2) supply the required all-orders justification.

## 2. The exact \(G_{10}(1)\) branch

The exact normalized derivative equation \(G_{10}(1)=0\) is equivalent to
\[
b=b_*(r):=44-120a_3-210a_4.
\]
Use a star to denote substitution of this expression into \(F,H,E\). With \(r=-2+17t\), there are integer polynomials \(K_H^*,K_E^*\) such that
\[
H^*+9F^*=17^2K_H^*(t,c),
\]
\[
E^*+9F^*-272c=17^2K_E^*(t,c).
\tag{5}
\]
Their checked reductions at the relevant residue point are
\[
K_H^*(3,0)\equiv11,\qquad K_E^*(3,0)\equiv15.
\tag{6}
\]
The first divided root equation is
\[
F^*/17\equiv3+16t+11c.
\]
If \(c\in\mathfrak m\) and \(F^*=0\), then \(t\equiv3\), so (5)–(6) prove
\[
\nu(H^*)=2.
\tag{7}
\]
Thus the branch with exact first-derivative witness 1, exact \(G_{10}\) witness 1, the stated \(a_3,a_4\), and residue-zero \(G_{12}\) witness is impossible: the latter makes \(c\in\mathfrak m\), whereas the first requires \(H^*=0\).

At \(c=0\), the independent baseline computations give
\[
r\equiv49\pmod{17^3},\qquad
H^*/17^2\equiv11,\quad E^*/17^2\equiv15,\quad b_*/17\equiv12.
\]
The effective coefficient of \(c\) in \(H^*\), computed modulo \(17^4\), is \(578=2\cdot17^2\). The exact identities (5), rather than extrapolation from this one derivative, show that all perturbations with \(c\in\mathfrak m\) preserve (7).

There is also a useful stability statement for a \(G_{10}\) witness \(x\) merely near 1 when \(b,c\in\mathfrak m\). The general identity (2), with \(F=0\), gives \(\nu(H)>1\). The checked residue derivatives are
\[
H_2f(1)\equiv3,\qquad G_{10}'(1)\equiv1.
\]
If \(x\ne1\), the divided-difference equation
\[
0=\frac{f(x)-f(1)}{x-1}
 =H+H_2f(1)(x-1)+H_3f(1)(x-1)^2+\cdots
\]
therefore gives \(\nu(x-1)=\nu(H)>1\): the terms after the unit linear term have strictly higher valuation. If \(H=0\), it instead forces \(x=1\). The \(G_{10}\) divided difference then gives, in either case,
\[
b=b_*(r)+\eta,\qquad \nu(\eta)>1,
\]
where \(\nu(0)=+\infty\). Indeed \(G_{10}(1)=b-b_*(r)\), and its divided-difference factor at \(x,1\) is a unit. Since
\[
F-F^*=184756(r^{10}-r)\eta,\quad
H-H^*=1662804\eta,\quad E-E^*=-184756\eta,
\]
all three differences have valuation greater than 2. More directly, (5) holds for the actual \(H,E\) with correction terms
\[
\bigl(1662804+9\cdot184756(r^{10}-r)\bigr)\eta
\]
and
\[
\bigl(-184756+9\cdot184756(r^{10}-r)\bigr)\eta.
\]
Their coefficients lie in \(17O\). Therefore for \(c\in\mathfrak m\), \(\nu(H)=2\) still holds; if \(\nu(c)>1\), also
\[
\nu(E)=2,\qquad \overline{E/17^2}=15.
\]
Thus the required displacement bound follows from the root equations and the displayed units in this specified branch. It is not inferred merely from congruence modulo the maximal ideal.

## 3. Unit \(G_{12}\), residue-zero \(G_{10}\), and exact \(H_1\) witness 1

Now \(b=a_{10}\) is free, the \(G_3\) witness is either 1 or \(r\), and the \(G_{12}\) witness is either 1 or \(r\). The \(G_4\) witness is \(r\). Set
\[
a_3=2\ \text{or}\ -r^3+3r,\qquad
a_4=-r^4+6r^2-4a_3r.
\]
The \(G_{12}\) condition gives
\[
c=-z^{12}+66z^{10}-220a_3z^9-495a_4z^8-66bz^2,
\qquad z=1\ \text{or}\ r.
\]
For the three requested pairs, substitution \(r=-2+17t\) makes \(F,H,E\) coefficientwise divisible by 17. The reductions of \(F/17,H/17\) are affine in \((t,b)\), with the following data:

| \(G_3\) witness | \(G_{12}\) witness | Constant vector | Coefficient matrix | Unique \((\bar t,\bar b)\) | \(\overline{E/17}\) |
|---|---|---|---|---|---:|
| 1 | \(r\) | \((0,0)\) | \(\begin{pmatrix}16&16\\0&1\end{pmatrix}\) | \((0,0)\) | 8 |
| \(r\) | \(r\) | \((0,0)\) | \(\begin{pmatrix}16&16\\9&1\end{pmatrix}\) | \((0,0)\) | 8 |
| \(r\) | 1 | \((8,13)\) | \(\begin{pmatrix}16&1\\9&0\end{pmatrix}\) | \((8,0)\) | 15 |

The determinants are 16, 8, and 8. Since the divided equations are integral polynomials with these affine reductions, invertibility gives
\[
t-t_0,\ b\in17O,
\]
where \(t_0=0,0,8\) respectively. This conclusion is stronger than \(\bar b=0\) and is valid in ramified rings. The displayed nonzero \(E/17\) values give \(\nu(E)=1\).

For clarity, the resulting contradiction with a nonzero residue-zero \(G_{10}\) witness can be checked directly. In all three rows \(a_3,a_4\) are units, with \(\bar a_3=2,\bar a_4=7\). If \(x\ne0\) is any root with \(\lambda=\nu(x)>0\), the equation \(f(x)/x=0\) has its possible minimum among \(16\lambda\), from the unit \(X^{17}\) coefficient, and 1, from \(E\). All other terms are strictly larger than their minimum: the middle coefficients are divisible by 17, and \(b\in17O\). Hence \(\lambda=1/16\).

The normalized derivative
\[
G_{10}(x)=x^{10}-45x^8+120a_3x^7+210a_4x^6+b
\]
then has its \(x^6\) term uniquely smallest among nonconstant terms, of valuation \(6/16=3/8\). If \(G_{10}(x)=0\), it follows that \(\nu(b)=3/8\), contradicting \(b\in17O\). In the exact support under investigation \(b\ne0\), so a \(G_{10}\) witness cannot be the exact root zero. Thus these three specified branches are excluded.

## Verification files and limits

Run the standalone standard-library checker normally or with optimization:

    python3 -B check_row5_jets.py
    python3 -B -O check_row5_jets.py

Both runs pass and give identical **verification.json** and **verification-optimized.json**. The checker constructs the source polynomials from binomial coefficients, checks every coefficientwise division in (2) and (5), retains the resulting polynomial arrays, computes the baseline roots by exact Hensel steps, and computes the displayed implicit derivatives by modular inversion of a unit. A mutated polynomial identity is rejected. No assertion statement is used as a proof check.

The note certifies the stated jet identities, the near-unit displacement bound under its stated hypotheses, and the explicitly deduced subcase exclusions. It does not classify every residue assignment or exclude the entire row-5 support.
