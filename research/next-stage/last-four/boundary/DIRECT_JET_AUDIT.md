# Independent audit: direct second-jet obstruction

24 September 2026. Internal adversarial mathematical audit, separate from the producer's arithmetic replay. **PASS for the theorem as stated in DIRECT_JET_THEOREM.md.** This is not an external referee report or a claim about the entire residue row.

## Scope

The audited assertion concerns a nontrivial characteristic-zero degree-20 Casas–Alvero polynomial, centered at its mean, written
\[
 f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
 \qquad a_0=1,\quad a_1=a_{20}=0,
\]
with integral roots and normalized coefficients at a valuation with \(\nu(17)=1\), reduction \(X^{20}-X^3\), exact zeros \(a_2=a_{18}=0\), residues \(\bar a_4=\cdots=\bar a_{15}=0\), and \(\bar a_{16}=-1\). The theorem excludes this entire stratum, whether \(a_3\) vanishes or not. It does not exclude arbitrary coefficients in residue row 1 or either mixed-support family.

The imported simplicity-of-the-mean lemma at prime 19 is essential: it gives an exact simple root at zero and hence a nonzero ordinary linear coefficient \(E\). A common Hasse-third witness reduces to 1, because the reduced Hasse-third derivative is the nonzero constant \(-1\) at zero. Scaling that witness to 1 preserves all stated residues and exact zero coefficients.

## Valuation and collision audit

1. The two other roots in the residue-zero cluster have the same value \(\delta=\nu(E)/2\). In \(f(q)/q\), only \(E\) and \(Dq^2\) can attain the minimum: every other exponent is higher and its coefficient is integral. In \(f'(q)-f(q)/q\), the term \(2Dq^2\) is uniquely lowest. Thus all three roots of the zero cluster are simple.

2. When \(t=a_3\ne0\), the equation \(G_3(q)=q^3+t=0\) forces \(\nu(t)=3\delta\). The expression for \(E\) gives \(2\delta\ge\min(1,3\delta)\), so \(\delta\ge1/2\); the case \(t=0\) gives the same bound directly. Only after obtaining this bound is division of \(E\) by 17 used. Its residue is 11, and consequently \(\delta=1/2\), with \(\nu(t)=3/2\) in the nonzero case. This step does not replace a positive valuation by an integer valuation.

3. For \(4\le j\le15\), the reduced \(G_j\) is \(X^j\), so any selected common witness is in the zero cluster. Induction in the exact normalized derivative recurrence gives \(\nu(a_j)\ge j/2\). If \(a_j=0\), the exact mean is an admissible witness. The discarded ordinary middle terms therefore have value at least 3; their contribution to the \(G_{16}\) equation has value at least 2.

4. For the unit \(G_{16}\) witness \(x\), the substitution
   \(u=-x^{16}-560t x^{13}+e\), with \(\nu(e)\ge2\), has the asserted precision. In the divided equation \(f(x)/(x-1)=0\), the small-displacement balance is between values \(1+\epsilon\) and \(16\epsilon\), and its combined linear coefficient is \(3+7=10\), a unit. It forces \(\epsilon=1/15\) whenever \(\epsilon<1\) in the zero-\(t\) case or \(\epsilon<1/2\) in the nonzero-\(t\) case.

5. The remaining displacement cases are covered. For \(t=0\) and \(\epsilon\ge1\), the Newton polygon gives fifteen simple outer roots and an inner cluster of size two containing the exact root 1 and \(x\). A repeated root can only occupy that inner cluster, so \(x=1\) is forced. For \(t\ne0\), finite \(\epsilon>1/2\) is impossible by a uniquely smallest \(c_1\) term. At \(\epsilon=1/2\), and also at \(x=1\), the coefficient \(c_1\) has exact value \(3/2\): there are fifteen simple outer roots, one further simple inner root, and the simple exact root 1. This contradicts the required repeated root.

6. At \(\epsilon=1/15\), the initial polynomial
   \(L(Y)=Y^{17}+7Y^2+3\xi Y\), with \(\xi^{15}=7\), contains all seventeen unit-cluster roots with multiplicity. A smaller displacement value would give a uniquely lowest term in the divided-root equation. Since \(L'=14Y+3\xi\), its only multiple root is \(\xi\), and its Hasse-second value there is 7. The corresponding cluster has size two and already contains \(x\). The exact repeated root must also lie there, forcing the repeated root to be \(x\), rather than merely to have the same residue.

These arguments use arbitrary fractional valuations and cluster multiplicities; none assumes an unramified ambient field or integral displacement valuations.

## Arithmetic and final contradiction

The producer checker was replayed with ordinary Python and with Python's -O option; both passed and gave identical records. Independently, the polynomials were reconstructed directly from the binomial coefficients in \(f'-f/X\) and the \(G_{16}\) substitution:
\[
\begin{aligned}
Q_0&=-14516X^{19}+38760X^{18}-2280X^2,\\
Q_1&=-8121360X^{16}+21705600X^{15}-1550400X^2.
\end{aligned}
\]
The reconstruction did not import the producer's coefficient arrays. Expanding \(Q_0(1+z)\), the weighted values \(15\nu(q_k)+k\) have minimum 17 exactly at \(k=2,17\). The divided coefficient at \(k=2\) is 1 modulo 17 and the coefficient at \(k=17\) is 2. Using \(\xi^{15}=7\), the initial form is \(15\xi^2\ne0\). Thus \(\nu(Q_0(x))=17/15\), strictly below \(\nu(tQ_1(x))\ge3/2\) and the error bound 3.

For the remaining case \(t=0,x=1\), \(Q_0(1)=17^2\cdot76\) has value 2, again strictly below the error bound. No cancellation is possible in either case.

The error bound was also checked conceptually: discarded middle terms carry their ordinary binomial factor of value at least 1, and the error in \(u\) is multiplied by a coefficient divisible by 17. This avoids treating a numerical coefficient check as a proof of approximation precision.

## Assurance boundary

The finite checker verifies arithmetic identities and the nonzero initial coefficient. The preceding audit supplies the valuation and cluster-coverage reasoning. Together they support the stated uniform stratum exclusion. They do not establish priority, publication significance, the full degree-20 conjecture, or any larger sparse-term bound by themselves.
