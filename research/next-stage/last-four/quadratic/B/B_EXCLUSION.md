# Candidate exclusion of support {4,10,16,17,18,19}

Research proof, 24 September 2026. Pending separate argument audit. This is not a manuscript or a claim about unrestricted degree twenty.

We use the established integral CA normalization at 17 and the complete seed classification. Exact zeros leave only the seed \(\bar f=X^{20}-X^3\). Normalize the common Hasse-third root to one; it is a unit, and this scaling preserves the seed. Write \(\nu(17)=1\), and

\[
f=X^{20}+4845aX^{16}+184756bX^{10}+4845uX^4+DX^3+FX^2+EX.
\]

Here \(a=a_4,b=a_{10},u=a_{16}\), and every displayed nonleading coefficient is nonzero. All are integral. The identities \(f(1)=H_3f(1)=0\) give

\[
D=-1140-560(4845)a-120(184756)b-4(4845)u,
\]
\[
E=1139+559(4845)a+119(184756)b+3(4845)u-F.
\]

The coefficient \(D\) is a unit, while \(E,F\) have positive valuation. The residue-zero cluster consists of the simple exact root zero and two nonzero roots, counted with multiplicity. All other roots reduce to one.

## 1. Occupancy of the small cluster

If a common \(H_2\) witness \(q\) is small, its equation is

\[
F+3Dq+\text{terms of larger valuation}=0.
\]

All higher ordinary coefficients below degree 17 are divisible by 17. Therefore \(\nu(F)=\nu(q)=\delta\), and the root equation gives \(E=2Dq^2+o(q^2)\). After scaling by \(q\), the two nonzero small roots have distinct initial values 1 and 2, since the initial quadratic is \(D(X-q)(X-2q)\). They are simple. An \(H_1\) witness therefore cannot also be small.

Conversely, if an \(H_1\) witness \(r\) is small, subtracting \(f(r)/r\) from \(f'(r)\) gives

\[
F=-2Dr+o(r),\qquad E=Dr^2+o(r^2).
\]

The repeated root \(r\) consumes both nonzero roots in the small cluster. In particular an \(H_2\) witness cannot be small, since its value at \(r\) has nonzero initial term \(Dr\). Thus at least one of the \(H_1,H_2\) common witnesses is a unit.

We next prove \(\nu(F)\geq1\). Suppose \(s=\nu(F)<1\). In \(f(1+Y)\) the coefficients \(c_1,c_2\) both equal \(F\) plus a multiple of 17; \(c_3=0\), \(c_4,\ldots,c_{16}\in17\mathcal O\), and \(c_{17},\ldots,c_{20}\) are units. Every nonzero displacement of a unit root then has value \(s/16\). At such a root the constant term \(c_1\) is uniquely smallest in \(f'\): the term arising from \(c_{17}Y^{17}\) acquires a factor 17, and subsequent terms have value at least \(17s/16>s\). Likewise \(c_2\) is uniquely smallest in \(H_2f\); the unweighted degree-nineteen and degree-twenty contributions have values \(17s/16\) and \(18s/16\), both above \(s\). The exact root one also has both these derivative values nonzero. Neither derivative can have a unit common witness, a contradiction. Hence \(\nu(F)\geq1\).

Now all \(c_1,\ldots,c_{16}\) lie in \(17\mathcal O\), and unit-root displacements have value at least \(1/16\). Evaluation of the derivatives shows that a unit \(H_1\) witness implies \(\overline{c_1/17}=0\), and a unit \(H_2\) witness implies \(\overline{c_2/17}=0\). These statements include the exact root one. A small witness for either derivative implies \(\nu(E)=2\nu(F)\geq2\), so \(\overline{E/17}=0\).

## 2. Complete first-divided sieve

Let \(k=\overline{F/17}\). Reconstruct \(\bar a,\bar b,\bar u\) from the eight binary markings of \(G_4,G_{10},G_{16}\), whose witnesses reduce to zero or one. Write \(W_1,W_2,E_0\) for the residues of \(c_1/17,c_2/17,E/17\) with \(F=0\). The possible derivative occupancies give respectively

\[
\begin{array}{c|c}
(H_1,H_2)&\text{necessary equations}\\ \hline
(\mathrm{unit},\mathrm{unit})&W_1+k=W_2+k=0\\
(\mathrm{unit},\mathrm{small})&W_1+k=E_0-k=0\\
(\mathrm{small},\mathrm{unit})&W_2+k=E_0-k=0.
\end{array}
\]

The exact checker reconstructs all eight markings and these divided equations. The only surviving row is

\[
(w_4,w_{10},w_{16})=(1,1,0),\qquad
(\bar a,\bar b,\bar u)=(16,5,0),
\]

with \((W_1,W_2,E_0)=(8,9,8)\), \(k=8\), and \((H_1,H_2)=(\mathrm{small},\mathrm{unit})\).

Consequently \(\nu(F)=1\), the small repeated root \(r\) has valuation one, and \(\nu(E)=2\). The \(G_{16}\) witness is nonzero because \(u\ne0\), so it is exactly \(r\). Its equation gives

\[
u=-r^{16}-1820ar^{12}-8008br^6,\qquad \nu(u)=6.
\]

Moreover \(\overline{c_1/17}=8+8=16\). Thus the unit cluster consists of exact one and sixteen simple outer roots of displacement value \(1/16\). Upon choosing \(\pi^{16}=17\), their initial values are all sixteen roots of \(Y^{16}-1\), precisely \(\mathbf F_{17}^{\times}\). In particular no nonzero unit-root displacement has value greater than \(1/16\).

## 3. A second-jet nonsquare obstruction

Let \(x_4,x_{10}\) be the two unit witnesses, and \(y\) the unit \(H_2\) witness. Each is either exactly one or an outer root. Put

\[
x_4=1+\pi t,\qquad x_{10}=1+\pi u_*,\qquad y=1+\pi v.
\]

We use \(u_*\) for this root parameter to distinguish it from \(a_{16}=u\). Its leading residue, and those of \(t,v\), belong to \(\mathbf F_{17}\). A zero leading residue means the corresponding root is exactly one. The high derivative equations give exactly

\[
a=-x_4^4,\qquad b=-x_{10}^{10}-210a x_{10}^6.
\]

For the low-order unit-root computations, replace \(f\) by

\[
f_0=X^{20}+4845aX^{16}+184756bX^{10}+D_0X^3+F_0X^2,
\]

where \(D_0=-1140-560(4845)a-120(184756)b\) and
\(F_0=1139+559(4845)a+119(184756)b\). The exact difference is

\[
f-f_0=4845uX^2(X-1)(X-3)-EX(X-1).
\]

It follows that the unit-root equation after division by \(17(X-1)\), and the Hasse-second equation after division by 17, have errors of valuation at least one. This is strictly above the two-jet precision \(2\nu(\pi)=1/8\). There is no division by a possibly tiny unbounded root separation: the factor \(X-1\) was cancelled exactly first.

Write the first sixteen Taylor coefficients of \(f_0(1+Y)\) as \(17A_j(a,b)\). Modulo 17,

\[
A_1=2+8a+b,\qquad A_2=13+9a+6b,
\quad A_3=0,
\]

and at \((a,b)=(-1,209)\), their values are \(A_1=16,A_2=0,A_4=14\). All these formulas are checked coefficientwise from the binomial family.

The first parameter expansions are

\[
a=-1-4\pi t-6\pi^2t^2+O(\pi^3),
\]
\[
b=209+\pi(7t+9u_*)
       +\pi^2(2t^2+8tu_*+11u_*^2)+O(\pi^3),
\]

where only residues of the displayed coefficients are used. The Hasse-second equation at any unit witness forces, at first order,

\[
6t_0+3u_0+3v_0=0,\qquad v_0=-2t_0-u_0.
\]

The last term is essential: the degree-nineteen Taylor term contributes
\(\binom{19}{2}20\pi^{17}v^{17}/17=3420\pi v^{17}\), whose first residue is \(3v_0\). The coefficients of degree seventeen and eighteen contribute only at orders fifteen and sixteen respectively.

For each nonzero leading witness parameter, its normalized root equation has unit diagonal derivative \(16t_0^{15}\), \(16u_0^{15}\), or \(16v_0^{15}\). The off-diagonal derivatives vanish in the residue field. Residual errors at integer leading values are in \(\pi\mathcal O\). The unit-Jacobian valuation bound therefore gives \(t-t_0,u_*-u_0,v-v_0\in\pi\mathcal O\), with zero parameters omitted because their roots equal one exactly, even over an arbitrarily ramified extension. It also determines the high-witness first corrections:

\[
t=t_0+\pi t_1+o(\pi),\qquad
u_*=u_0+\pi u_1+o(\pi),
\]
\[
t_1=12t_0^2+9t_0u_0,\qquad
u_1=9t_0u_0+12u_0^2.
\]

Here the symbols \(u_*\) and \(u_1\) are the root parameter and its correction. If a leading residue is zero, its root is exactly one and its correction is zero; the same displayed formulas remain valid. For nonzero parameters they follow from

\[
16t_1/t_0+12t_0+9u_0=0,\qquad
16u_1/u_0+9t_0+12u_0=0.
\]

Substitution into the expansion of \(A_2\) gives second coefficient

\[
6t_1+3u_1+9t_0^2+14t_0u_0+15u_0^2
=13t_0^2+10t_0u_0.
\]

At an outer \(H_2\) witness, the degree-nineteen contribution has no second coefficient: in characteristic 17 the first variation of \(v^{17}\) vanishes. The remaining second-order terms are

\[
6A_4v_0^2+190v_0^{18}
=16v_0^2+3v_0^{18}=2v_0^2,
\]

because \(v_0^{16}=1\). At exact one these contributions vanish. Thus the second equation, valid in both cases, is

\[
13t_0^2+10t_0u_0+2v_0^2=0.
\]

Eliminating \(v_0=-2t_0-u_0\) gives

\[
4t_0^2+t_0u_0+2u_0^2=0.
\]

This binary quadratic form has discriminant \(1-32=3\) in \(\mathbf F_{17}\), which is a nonsquare. It has no nonzero zero. Therefore \(t_0=u_0=v_0=0\), and the root-cluster description gives the exact collisions

\[
x_4=x_{10}=y=1.
\]

The calculation uses only forced residues and a unit-Jacobian bound. It does not assume that arbitrary candidate roots have unramified or integral-power Puiseux expansions. Terms denoted \(o(\pi)\) have strictly larger valuation; their contributions to the second coefficient have strictly larger value than \(\pi^2\).

## 4. Final small-root contradiction

The exact collisions give \(a=-1,b=209,H_2f(1)=0\). The latter fixes \(F\) as an integer affine expression in \(u\); all terms involving \(u\) have valuation at least seven. At \(u=0\), direct exact arithmetic gives

\[
\bar D=16,\qquad \overline{F/17}=8,\qquad
\overline{E/17^2}=9.
\]

The repeated-root identity at \(r\), with \(\nu(r)=1\), gives

\[
\overline{r/17}=-\frac{8}{2\cdot16}=4.
\]

But the residue of \(f(r)/(17^2r)\) is

\[
9+8\cdot4+16\cdot4^2=8\ne0\quad\text{in }\mathbf F_{17}.
\]

All other terms have strictly larger valuation. This is the contradiction. Subject to independent audit, it excludes the exact support globally using the inherited normalization and seed-classification bridge.

## 5. Transferable precision statement

The second-jet argument in section 3 remains valid if the ordinary polynomial and the normalized \(G_4,G_{10}\) equations acquire perturbations of valuation at least two, provided their normalized unit-root equations after cancellation of \(X-1\) and division by 17 have error of valuation at least one. This exceeds \(2/16\). The same first residues, unit-root cluster, and derivative occupancy must have been proved separately; this precision observation by itself does not establish them.

`check_B.py` replays the complete first sieve, reconstructs the Taylor coefficients, checks every second-jet residue, verifies the nonsquare, and checks the last exact constants. The exploratory `probe_jets.py` omitted the degree-nineteen contribution to the Hasse-second derivative and is invalid evidence. It is retained only as a superseded diagnostic; this corrected proof and checker do not rely on it. The correction was found in the independent argument review. All arbitrary-ramification and root-count arguments are above and remain separate from the finite arithmetic checks.
