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
