# Independent audit of support A in residue row 1

24 September 2026. **PASS for the row-1 exclusion in `A_ROW1_EXCLUSION.md`.** The support is \(\{2,4,10,17,18,19\}\). Its row-2 branch is not covered by this conclusion. This is an internal proof audit, not an external referee report.

I independently checked the occupancy and valuation arguments, the transfer of the corrected second-jet lemma, and the final exact constants. The arithmetic checker was inspected and replayed normally and under `-O` from `/private/tmp`; both outputs were identical and PASS. Details and fingerprints are saved in `parent-audit-replay.json`.

## Routing and complete occupancy split

The seed table alone retains rows 1, 2 and 4. Row 4 is excluded by an exact-root argument: its reduced \(G_{17}\) is \(X^{17}\), its residue mean is simple, and its exact mean is zero. Thus the selected common witness must be exactly zero, forcing the active coefficient \(a_{17}\) to vanish. It is correct not to infer this solely from a zero residue.

In row 1, exact \(E\ne0\) makes the mean simple; the other two small roots are counted with multiplicity. A small Hasse-second witness gives \(K=-3Dq+o(q)\), \(E=2Dq^2+o(q^2)\), so these roots have distinct scaled residues 1 and 2. A repeated witness must then be a unit. Since \(G_2=X^2+h\), its nonzero small witness forces \(\nu(h)=2\nu(q)\). For \(\nu(q)<1\), both low unit-cluster Taylor coefficients have value \(\nu(q)\); every unit root has displacement \(\nu(q)/16\), at which the derivative cannot vanish. Thus \(\nu(q)\geq1\), and the stated four-marking sieve rules out the case.

If both Hasse-first and Hasse-second witnesses are units, let \(\delta\) be the least nonzero unit-root displacement value. The bounds

\[
\nu(c_2)\geq\min(1+2\delta,17\delta),\qquad
\nu(c_1)\geq\min(1+3\delta,17\delta)
\]

are valid: the degree-nineteen contribution to the Hasse-second derivative has value \(17\delta\) and is included. Since \(c_3=0\), a minimum root would have a uniquely lowest \(c_{17}Z^{17}\) term if \(\delta<1/13\). Hence both \(c_1,c_2\) have value greater than one, giving the stated empty residue sieve. The case of seventeen exact coincident roots makes both coefficients zero and obeys the same sieve.

The only remaining occupancy is a small repeated root \(r\) and a unit Hasse-second witness. The repeated root exhausts the two nonzero small roots, so the \(G_2\) witness is exactly \(r\) and \(h=-r^2\). Its multiplicity is exactly two; consequently it cannot also be a Hasse-second common root. This proves the coverage without assuming automatic simplicity of the small cluster.

## Forced scale and residue marking

The repeated-root identities give \(\nu(K)=\nu(r)=\eta\), \(\nu(E)=2\eta\). If \(\eta<1\), the two lowest Taylor coefficients at one both have value \(\eta\). Unit-root displacements have value \(\eta/16\), and the Hasse-second constant term is uniquely lowest there. Its degree-nineteen and degree-twenty contributions have values \(17\eta/16,18\eta/16>\eta\). Thus \(\eta\geq1\) and \(\nu(h)\geq2\).

The unit Hasse-second equation and \(\nu(E)\geq2\) leave only \((\bar A,\bar b)=(16,5)\), with \(K/17=8\). This forces \(\eta=1\), \(r/17=4\), \(h/17^2=1\). Also \(c_1/17=16\). The cluster is therefore exact one plus sixteen simple outer roots of displacement \(1/16\), with scaled residues in \(\mathbf F_{17}^{\times}\).

## Corrected jet transfer and final contradiction

The ordinary error relative to the comparison polynomial is exactly

\[
190h(X^{18}-816X^3+815X^2)-EX(X-1).
\]

The first bracket is divisible by \(X-1\) in \(\mathbf Z[X]\). Thus after exact cancellation and division by 17, the unit-root error has value at least one. The divided Hasse-second error has the same bound. Corrections to the \(G_4,G_{10}\) coefficient identities have value at least two. These errors are strictly above the required \(2/16\) precision.

I independently rederived the repaired jet equations

\[
2t_0+u_0+v_0=0,\qquad
13t_0^2+10t_0u_0+2v_0^2=0.
\]

The degree-nineteen contribution is essential to the first equation. Eliminating \(v_0\) gives the binary quadratic form \(4t_0^2+t_0u_0+2u_0^2\), of nonsquare discriminant 3 over \(\mathbf F_{17}\). All three residues vanish, and the known root cluster forces all three exact witnesses to equal one. The unit-Jacobian argument is applied to every nonzero root parameter; no integrality assumption about arbitrary ramified expansions is introduced.

The exact collisions give \(A=-1-6h\), \(b=209+1215h\). The reconstructed linear coefficient is

\[
E=-7563497030-43968975970h,
\]

so \(E/17^2=9+14(h/17^2)=6\). Since \(r/17=4\), the small-root equation has residue \(6+8\cdot4+16\cdot16=5\ne0\). Every omitted term is strictly higher. This completes the row-1 contradiction over arbitrary ramification.

Reviewed source SHA-256: `336a587c43501633de0400a3cd552f6c5ef12558ceb9bf01977ca0798e29f7df`. Reviewed arithmetic checker SHA-256: `433add7d46fd9743921b3d36b66b8be4c461021f7ed504ae1b4748ae1f102705`. The earlier erroneous exploratory B jet script is not evidence for this result. The corrected jet proof and its independent reconstruction replace that step.
