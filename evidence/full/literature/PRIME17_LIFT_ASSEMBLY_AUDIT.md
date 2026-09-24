# Final bounded audit of the characteristic-17 lift consequences

23 September 2026. **PASS for the mathematical claims in
`../LIFT_CONSEQUENCES_17.md`.** Read together with
`../two_adic/CLUSTER_COLLAPSE.md` and the previously audited gcds.
No further branch exploration or new literature search was performed.

The row-3 exclusion remains correct for the reasons in
`PRIME17_ROW3_LIFT_AUDIT.md`.

For row 9, direct Hasse evaluation at one gives

\[
(h(1),H_1h(1),H_2h(1),H_3h(1))=(0,0,0,1).
\]

Hence its residue root one has multiplicity exactly three. The independently
computed monic gcds with \(H_1,H_2,H_{17}\) are respectively
\((X-1)^2,X-1,X-1\). Both required low-order witnesses therefore lie
in that residue cluster. The cluster-collapse proof is sound: rescaling by
the least nonzero root difference produces an integral monic degree-three
factor with at least two residue roots; all outside factors reduce to a
nonzero constant after their normalization. The Hasse chain rule then
transfers both low-order common-root conditions. The elementary degree-three
theorem in characteristic 17 contradicts that nontrivial reduced factor.
This argument allows arbitrary ramification and does not infer exact root
equality from residue equality alone.

The three cluster roots consequently coincide. Its total multiplicity is
three, so this is an exact triple root, not a root of unspecified higher
multiplicity. The \(H_{17}\) witness must be this root because its residue
is forced to one and there are no other exact roots in the cluster.

The mean residue zero is simple. The pure-\(X\) gcds for \(H_3,H_{18}\)
force their exact witnesses to be zero, so the ordinary coefficients of
\(X^3,X^{18}\) vanish. In binomial-normalized deficiency notation these
are \(a_{17}=a_2=0\), respectively. Normalizing the actual triple witness
to one gives \(G_3(1)=1+a_3=0\); hence \(a_3=-1\) and the ordinary
\(X^{17}\) coefficient is \(-\binom{20}{3}=-1140\). Every index in the
assembled note is correct.

For rows 6 and 7, the residue derivatives at one are 11 and 14, respectively,
so that root is simple. The \(H_{17}\) and \(H_{18}\) gcds both force
their witnesses into its size-one cluster. They are therefore the same
exact root. Normalizing it to one yields
\(1+a_2=0\) and \(1+3a_2+a_3=0\), giving \(a_2=-1,a_3=2\).
Their \(H_3\) witnesses lie at the simple mean and give \(a_{17}=0\).
In row 4, the \(H_{17}\) witness is instead the exact mean, so
\(a_3=0\), while the \(H_{18}\) normalization gives \(a_2=-1\).
Its \(a_{17}=0\) conclusion is also valid.

The small direct arithmetic receipt is
`prime17-lift-assembly-arithmetic.json`; the general gcd data and source
audit are recorded separately. The conclusions retain their conditional
branch scope. Rows 4,6,7,9 are constrained, not excluded. The assembled
note and `../STATUS.md` correctly retain eight unresolved residue branches
and state that both unrestricted degree 20 and the all-degree conjecture
remain unproved.

This review does not certify the separate first-saturation valuation bounds
or all-degree algebra audit, which were outside this final bounded task.
