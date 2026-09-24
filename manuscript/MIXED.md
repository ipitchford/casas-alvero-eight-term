## Two mixed middle-coefficient configurations

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

### The finite residue cover

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

### The small-root equations

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

### The leading model of the unit cluster

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

### Exclusion of a nonzero repeated leading location

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

### The critical derivative and the final contradiction

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
[check_mixed_strata.py](../next-stage/last-four/middle/check_mixed_strata.py)
reconstructs (M1)–(M17) from binomial coefficients, checks every marking
in (M5), and verifies the polynomial divisions and rational constants.
Its role is to certify these finite identities. The valuation estimates,
complete cluster counts and exact collision deductions are the
mathematical arguments given above.
