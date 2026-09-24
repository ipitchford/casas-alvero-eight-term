## The support \(\{2,3,4,10,12,19\}\): the row-\(5\) reduction

The complete seed classification allows rows \(5\) and \(8\) for the exact
centered deficiency support
\[
S=\{2,3,4,10,12,19\}.
\]
The row-\(8\) alternative is excluded by the preceding residue argument.
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

### The complete first-divided cover

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

### Finite polynomial identities

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

### Case 1: repeated witness one and both middle witnesses units

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
[row5-unit-certificates.json](../next-stage/row5-unit/row5-unit-certificates.json).
Identity (R23) is verified coefficient by coefficient by integer
convolution. Evaluating it at a common zero of \(P,Q\) would give
\(D_{s,z}=0\) in characteristic zero, a contradiction.
Thus all four exact choices are impossible; three occur in (R9).

### Case 2: repeated witness one, small \(G_{10}\) witness, and unit \(G_{12}\) witness

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

### Case 3: repeated witness one, \(G_{10}\) witness one, and small \(G_{12}\) witness

The cover (R9) forces \(y=r\). Here \(b=b_*(r)\) exactly and
\(\nu(c)>0\). Equations (R17)–(R18), with
\(\mathcal F^*=0\), give \(\nu(f'(1))=2\), whereas the repeated
witness requires \(f'(1)=0\). This is impossible.

### Case 4: repeated witness one and both middle witnesses small

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

### Case 5: repeated witness small and \(G_{10}\) witness small

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

### Case 6: repeated witness small and \(G_{10}\) witness near one

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

### Coverage and finite certificates

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
[check_row5_first_divided.py](../next-stage/check_row5_first_divided.py);
the four integer identities (R23) in
[check_row5_unit.py](../next-stage/row5-unit/check_row5_unit.py);
and the coefficientwise identities (R12)–(R19), evaluations, and
matrices in
[check_row5_jets.py](../next-stage/row5-jets/check_row5_jets.py).
Each uses exact arithmetic and retains its acceptance checks under
optimized Python execution. Their finite calculations supply the
displayed identities; the valuation inequalities and root-count
deductions establishing complete case coverage are proved above.
