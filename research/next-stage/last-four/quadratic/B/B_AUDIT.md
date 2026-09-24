# Independent audit of the quadratic-coefficient support B

24 September 2026. **PASS for exclusion of the exact centered deficiency support \(\{4,10,16,17,18,19\}\)**, conditional on the preserved complete characteristic-17 seed classification and the established simplicity of the mean in characteristic zero. This is an internal adversarial argument audit, not an external review or a full-degree theorem.

Audited source fingerprints:

- B_EXCLUSION.md: 4fbbf6b96fd2e800428bd480ad726a17add7df39cffcbf39913efc8d00cdc62b.
- check_B.py: cdd1088cf338fd86a3ed6708524399a62d85248b2fc3a004e8679ae52bae941e.

The earlier probe that omitted the degree-nineteen Hasse-second contribution is invalid and is not a dependency of this audit. The corrected source and checker retain it.

## 1. Coverage and the first divided sieve

The exact zeros \(a_2=a_3=0\) leave only row 1 in the complete nonmonomial seed classification. The retained unit root prevents monomial reduction. A common \(H_3\) root can therefore be scaled to 1 by a unit with residue 1. This supplies both exact normalization equations used for \(D\) and \(E\).

The simple mean is a necessary dependency: \(E\ne0\), so exact zero consumes one simple root in the residue-zero cluster. The two small-root occupancy arguments are correct. If an \(H_2\) witness \(q\) is small, the leading equations give \(F=-3Dq+o(q)\), \(E=2Dq^2+o(q^2)\); the other two roots have distinct initial values 1 and 2 after scaling by \(q\). If an \(H_1\) witness \(r\) is small, it is repeated and consumes both remaining multiplicities; the leading value of \(H_2f(r)\) is \(Dr\ne0\). Thus at least one of the two derivative witnesses must be a unit.

The proof of \(\nu(F)\ge1\) is ramification-safe. For \(0<s=\nu(F)<1\), all sixteen nonzero unit-cluster displacements have value \(s/16\). In \(f'\) and \(H_2f\), the terms \(c_1\) and \(c_2\) respectively have unique smallest value \(s\). In particular the degree-nineteen Hasse-second contribution has value \(17s/16>s\), even though its binomial multiplier is a unit. This proves the contradiction without assuming that positive valuations are integers.

Once \(F\in17\mathcal O\), the lower displacement bound \(1/16\) is sufficient to justify both divided derivative conditions at unit witnesses. The same degree-nineteen term now has value at least \(17/16>1\), so it does not affect the first divided sieve. It does affect the later finer jet calculation.

The eight binary markings are complete because every residue root is either 0 or 1. The three listed occupancy alternatives exhaust the possibilities, including a witness exactly equal to 1. The unique surviving marking forces a small repeated root \(r\) with \(\nu(r)=1\), \(\nu(E)=2\), and \(\nu(F)=1\). The nonzero \(G_{16}\) coefficient forces its selected small witness to be \(r\) exactly. Its leading term \(8008br^6\) is a unit multiple of \(r^6\), hence \(\nu(a_{16})=6\).

## 2. Why the residue parameters really lie in \(\mathbf F_{17}\)

The first divided \(c_1\) residue is 16. Thus the exact root 1 is simple and the other sixteen roots in the unit cluster have displacement value \(1/16\). After adjoining \(\pi\) with \(\pi^{16}=17\), their leading equation is \(Y^{16}-1=0\).

All sixteen roots of this polynomial are exactly \(\mathbf F_{17}^{\times}\), even in a larger algebraically closed residue field. Consequently the three marked displacement parameters have residues in \(\mathbf F_{17}\). A zero residue means the selected root is exactly 1, since there is no further inner root. This is the required justification for applying a nonsquare obstruction over \(\mathbf F_{17}\); the proof does not assume that arbitrary residue coefficients or roots belong to that field.

## 3. Precision of the three-root system

The identity
\[
 f-f_0=4845a_{16}X^2(X-1)(X-3)-EX(X-1)
\]
was checked against the two normalization equations. For a nonzero displacement, canceling \(X-1\) before dividing by 17 gives an error with value at least 1. The Hasse-second equation after division by 17 has the same error bound. Both exceed the required two-jet value \(2/16\).

The unit-Jacobian claim can be made explicit as follows. Keep the actual \(E,a_{16}\) fixed, express \(a,b\) by the exact \(G_4,G_{10}\) equations, and use the normalized root equation for each of the marked roots whose leading parameter is nonzero. Omit zero parameters and their equations, since the corresponding root is exactly 1. In this square system the reduction of each equation is its own variable to the sixteenth power minus 1. Thus the Jacobian is diagonal modulo the maximal ideal, with entries \(16s_0^{15}\ne0\). Repeated choices of the same root cause no problem: they may be represented by separate variables with separate diagonal equations.

At the tuple of integer lifts of the leading residues, the equation defects have value at least \(1/16\). If any actual parameter deviation had a smaller positive value, the invertible linear part would have that value in at least one component, while the constant defect and all quadratic terms had larger value. This is impossible. Hence every deviation is in \(\pi\mathcal O\), including over an arbitrarily ramified extension. The resulting first corrections are then determined by linear equations over the residue field. No unramified-lift theorem is being assumed.

For the two high-derivative witnesses, expansion of their normalized root equations gives
\[
16t_0^{15}t_1+12t_0+9u_0=0,\qquad
16u_0^{15}u_1+9t_0+12u_0=0.
\]
Using \(s_0^{16}=1\) for nonzero parameters yields the stated corrections
\(t_1=12t_0^2+9t_0u_0\) and \(u_1=9t_0u_0+12u_0^2\).
When a leading parameter is zero, its exact parameter and correction are zero and the same polynomial formulas remain valid.

## 4. The corrected second jet

The degree-nineteen term in \(H_2f_0/17\) is
\[
20\binom{19}{2}\pi v^{17}=3420\pi v^{17},
\]
whose first residue is \(3v_0\). It must not be discarded. It supplies the corrected first equation
\[
6t_0+3u_0+3v_0=0.
\]

Its next contribution has value strictly greater than \(2/16\): the first variation of \(v^{17}\) has its extra factor 17, and the seventeenth-power endpoint also has sufficiently large value once \(v-v_0\in\pi\mathcal O\). Thus there is no \(v_1\) term at the second order. The degree-twenty contribution does remain at that order.

Reconstructing the other second-order terms gives
\[
13t_0^2+10t_0u_0+2v_0^2=0.
\]
Substituting \(v_0=-2t_0-u_0\) gives \(4t_0^2+t_0u_0+2u_0^2=0\). Its discriminant is 3, a nonsquare in the now-justified field \(\mathbf F_{17}\). The only triple is zero. The cluster description then forces all three marked roots to equal 1 exactly; equality is not inferred from a residue congruence alone.

## 5. Final contradiction and verification

The exact collisions give \(a=-1,b=209,H_2f(1)=0\). Terms involving \(a_{16}\) have value at least 7, so they do not affect the three final residues \(D=16\), \(F/17=8\), and \(E/17^2=9\). The small repeated root has \(r/17=4\), but the divided root equation has residue
\[
9+8\cdot4+16\cdot4^2=8\ne0.
\]
All higher terms have strictly greater value. This closes the exact-support exclusion.

The producer checker passes under normal and optimized Python, with identical results matching the saved receipt. A separate calculation, without importing it, reconstructed the integer binomial Taylor coefficients and both jet orders before residue reduction. Exhaustion of all \(17^3=4913\) triples left only \((0,0,0)\), agreeing with the nonsquare proof. The extra computation is an arithmetic cross-check; the field restriction, coverage and precision arguments are the distinct proof obligations audited above.

The transferable precision observation in the source is valid with its stated additional hypotheses on normalized equations and already-established occupancy. It is not by itself an exclusion for other supports. This audit excludes B only and does not count the remaining support A as resolved.
