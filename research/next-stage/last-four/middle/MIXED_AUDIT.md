# Independent audit of the two mixed-stratum exclusions

24 September 2026. **PASS for the two local exclusions and the stated exact-support corollaries**, conditional on the preserved complete characteristic-17 seed classification and the already audited unit-16 exclusion. This is an internal adversarial argument audit; it is not an external referee report, a formal proof, or a novelty certification.

Reviewed files and SHA-256 fingerprints:

- MIXED_STRATA.md: 9f0e1ff062f320c0de94aca3d8237681ac4e0bb656ee69c5c4050df4d7bbc083.
- check_mixed_strata.py: 090b820edc1a069e18d7f2e605da0fec6676e544c4c4f1d1b13577de2329b8c9.

## 1. Exact scope and normalization

The two local patterns are
\[
\begin{array}{c|c|c}
&J&(\bar a_j)_{j\in J}\\ \hline
A&\{10,12,13,16\}&(16,14,1,0)\\
B&\{9,10,15,16\}&(16,9,9,0).
\end{array}
\]
The ordinary polynomial has only the leading term, the displayed middle terms, and the terms \(DX^3+EX\); its reduction is \(X^{20}-X^3\). It is normalized by an actual common \(H_3\) root at 1, giving both \(f(1)=0\) and \(H_3f(1)=0\). That witness is a unit with residue 1, so the scaling preserves all displayed residues and exact coefficient zeros.

The normalized derivative \(G_j=\sum_{i\le j}\binom ji a_iX^{j-i}\) has degree \(j\); its Hasse order is \(20-j\). Thus, for example, the critical \(G_{13}\) in A is not the Hasse-thirteenth derivative. The proof and checker maintain this indexing consistently.

The local theorem includes the boundary \(a_{16}=0\). It does not assume this coefficient nonzero at a step that is later used for that boundary: equations requiring its exact finite valuation are stated conditionally, and the final collision argument also treats the zero case.

## 2. Ramification and leading-cluster coverage

The precision of each divided identity is justified by an integer identity. In particular, the statement \(c_k\in17\mathcal O\) for \(1\le k\le16\), where \(f(1+Z)=\sum c_kZ^k\), follows coefficientwise from the exact normalization formula. It is not inferred merely from vanishing residue. This is crucial in a ramified extension.

The divided constant \(E/17\) has residue 6 in A and 7 in B. Consequently \(E\) has exact value 1, zero is a simple root, and the other two roots in its residue cluster have exact value \(1/2\). Their initial quadratic has two distinct nonzero roots in characteristic 17, so both are simple. Equivalently, the term \(2Dq^2\) is uniquely lowest in \(f'(q)-f(q)/q\). Every exact repeated root must therefore lie in the seventeen-root unit cluster.

Since \(\bar G_{16}(1)\) is respectively 13 and 2, a nonzero \(a_{16}\) forces its witness into the small cluster. The uniquely lowest nonconstant term there has degree 3 in A and degree 1 in B. Thus the necessary values are \(3/2\) and \(1/2\), respectively. Higher preceding unit coefficients cannot be dropped from this computation.

For an exact repeated root \(1+z\ne1\), subtracting \(F(z)/z\) from \(F'(z)\) removes \(c_1\). The only possible lowest terms are \(c_2z\) and \(16c_{17}z^{16}\); all remaining terms have strictly larger value than their minimum. Because \(c_2\) has exact value 1, this gives \(\nu(z)=1/15\). It also gives \(\nu(c_1)\ge16/15\). If the repeated root is exactly 1, the latter assertion follows from \(c_1=0\).

Every unit-cluster displacement has value at least \(1/15\). With \(\pi^{15}=17\), the reduction of \(F(\pi Y)/\pi^{17}\) is
\[
 g(Y)=Y^{17}+\kappa Y^2+\lambda Y,
 \qquad \kappa=5\text{ or }3.
\]
The three roots outside the unit cluster contribute a unit factor; the degree-seventeen cluster factor accounts for all seventeen remaining roots with multiplicity. Hence no branch of that cluster is omitted by the leading polynomial. The argument applies in arbitrary finite ramified extensions after adjoining \(\pi\).

The derivative \(g'=2\kappa Y+\lambda\) has exactly one zero, so the repeated leading location is unique. It is either zero, giving a double root at zero and fifteen simple nonzero roots, or nonzero, giving \(\eta^{15}=\kappa\) and \(\lambda=-2\kappa\eta\). These cases exhaust every possible repeated root.

## 3. First variations and geometric finite-field exclusion

All three unit-coefficient witnesses reduce to 1. The exact triangular recurrence gives deviations of their coefficients from the all-at-one baselines of value at least \(1/15\). Linearization modulo \(\pi\) is consequently legitimate: quadratic deviations have strictly greater value, while the \(a_{16}\) contribution has value at least \(1/2\), or is zero. The baseline \(c_1\) has value 2. Dividing \(c_1\) by \(17\pi\) therefore yields precisely the displayed linear relations for \(\lambda\).

If the repeated leading location is nonzero, every divided marked location is a root of \(R(T)=T^{17}+T^2-2T\). The affine pairs in the proof are excluded by exact polynomial division with nonzero final constant. These are polynomial identities over \(\mathbf F_{17}\), not a census of its rational points, so the conclusion holds over the whole algebraic closure. The checker correctly uses \(R(\alpha+\beta T)-\beta R(T)\), not an expression involving \(R'\).

When the repeated leading location is zero, the relevant paired leading locations have ratio 10 or 13. Their fifteenth powers are 12 and 4, respectively, rather than 1. Since every nonzero root of \(g\) has fifteenth power \(-\kappa\), both paired locations must therefore be zero.

## 4. Exact collision and degenerate derivative equations

The zero leading cluster has multiplicity exactly two and contains the exact root 1 and an exact repeated root of \(f\). A repeated root already consumes its entire multiplicity. It follows that the repeated root is exactly 1 and that every selected witness in that cluster is also exactly 1. This uses root counts, rather than the invalid inference that two roots with the same residue are necessarily equal.

Thus A has \(a_{10}=-1,a_{12}=65\). In B, \(a_9=-1\) and \(a_{15}=5004-3003a_{10}\). In both cases \(f'(1)=0\).

The remaining derivative equation has a vanishing exact linear term at 1. It is not treated by a simple-root Hensel argument:

- In A, the exact \(f'(1)\) equation gives \(\nu(a_{13}+560)\ge1\). The quadratic coefficient of \(G_{13}(1+Z)\) is \(-780\), a unit.
- In B, the same equation after eliminating \(a_{15}\) gives \(\nu(a_{10}-9)\ge1/2\). The quadratic coefficient of \(G_{10}(1+Z)\) is 45, a unit.

All outer roots have displacement value \(1/15\). At such a root, the quadratic term has value \(2/15\), strictly below the constant bound and every higher integral term. Neither derivative can vanish there. Its witness must be in the inner cluster, hence exactly 1. This reasoning also covers \(a_{16}=0\), when the constant bounds improve.

The resulting exact coefficient equations force
\[
 a_{16}=242879/3\quad\hbox{or}\quad a_{16}=15890869/75.
\]
Each has value 1. This contradicts the independently necessary values \(3/2\) and \(1/2\), and also excludes the zero boundary. The local proofs are complete.

## 5. Global exact-support coverage

For either displayed exact support, \(a_2=a_3=a_{18}=0\). Comparing these exact zeros with the complete visible-seed table in the preserved characteristic-17 classification leaves only row 1 among its nine nonmonomial representatives. The monomial reduction is unavailable after minimum-root valuation normalization, because a unit root is retained. The table's coefficients are ordinary visible coefficients; their nonzero binomial multipliers at 17 ensure that the exact zeros used here are preserved.

For each row-1 support, the only possible residue witnesses are 0 and 1. The triangular recurrence therefore makes the sixteen binary markings complete over the algebraic closure, not merely over \(\mathbf F_{17}\). The first-divided condition used to filter them is necessary: all zero-cluster roots are simple, while variation of \(f'\) from 1 to any unit-cluster root has value greater than 1. The proof supplies the preliminary displacement bound \(1/16\) needed for orders 18 and above.

The complete marking census leaves the unit-16 pattern and the mixed pattern, with no additional marking. The former is excluded by the preserved unit-16 theorem (also strengthened by DIRECT_JET_THEOREM.md and its independent audit); the latter is excluded above. Thus the exact centered deficiency supports
\[
 \{10,12,13,16,17,19\},\qquad
 \{9,10,15,16,17,19\}
\]
are excluded. The finite-type specialization argument with inverse variables for nonvanishing coefficients transfers any hypothetical complex exact-support point to an algebraic one, to which the local valuation argument applies.

## 6. Verification and limits

Normal and optimized replays of check_mixed_strata.py both passed and matched their saved receipts byte for byte. A separate direct-binomial reconstruction, without importing the checker, reproduced both all-at-one coefficient baselines, both complete sixteen-marking survivor lists, the values of \(E/17\) and \(c_2/17\), the exact baseline \(c_1\) values, both critical quadratic jets, and both final rational \(a_{16}\) values.

The arithmetic replay does not by itself certify Newton polygons or root-count implications. Those are the distinct argument obligations checked above. No remaining mathematical gap was found in these two exclusions. The result does not prove unrestricted degree 20, the full conjecture, or an eight-term bound while other seven-term supports remain.
