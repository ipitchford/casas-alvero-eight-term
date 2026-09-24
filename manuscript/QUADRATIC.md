## The two configurations with a quadratic coefficient

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

### The two nonzero roots in the zero residue class

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

### A complete divided residue calculation

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

### A quadratic obstruction for the three unit witnesses

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

### The final small-root residues

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
