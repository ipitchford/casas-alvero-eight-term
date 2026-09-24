# Final proof transcription review: DIRECT, ROW2, and MIXED

24 September 2026.

**Result: PASS for the mathematical transcription of the three assigned sections. No blocking proof-transcription error was found.** This is a scoped comparison with the audited sources, including a fresh check of the critical valuation and cluster deductions. It is not a new audit of the complete global support cover, Appendix A, row 5, novelty, or the final rendered bundle.

Reviewed manuscript: outputs/casas-alvero-eight-term-review/PAPER.md. The assigned sections are “A uniform obstruction in the first residue stratum,” “Two mixed middle-coefficient configurations,” and “Exclusion of the second residue configuration.” Their global normalization context was also read, including algebraic specialization, integral normalized coefficients, and the imported simple-mean theorem.

## 1. Uniform unit-16 obstruction

The final statement retains every essential hypothesis: degree twenty, nontriviality, centering, integral roots and normalized coefficients; reduction \(X^{20}-X^3\); exact zeros \(a_2=a_{18}=0\); residue zeros for \(a_4,\ldots,a_{15}\); and \(\bar a_{16}=-1\). It allows both \(a_3=0\) and \(a_3\neq0\), with unrestricted finite ramification.

The simple-mean theorem is supplied by the normalization section and cited again locally. It ensures \(E\neq0\), so the small-root divisions and repeated-root cover retain the exact mean.

The order of valuation deductions is correct. The proof obtains \(\delta\geq1/2\) and \(\nu(a_3)\geq3/2\) before dividing \(E\) by 17 and computing residue 11. The induction \(\nu(a_j)\geq j/2\), \(4\leq j\leq15\), covers zero coefficients using the exact mean and nonzero coefficients using the two nonzero small roots. It therefore justifies ordinary error bound three and normalized \(G_{16}\) error bound two, including nonzero \(a_4\).

All collision cases are retained: zero \(a_3\) with displacement below or at least one; nonzero \(a_3\) with displacement below, equal to, or above \(1/2\); exact \(x=1\) in each branch; and the remaining displacement \(1/15\). The balance coefficient 10, the fifteen simple outer roots, and the complete seventeen-root initial polynomial are present.

The root count precedes the exact equality \(f'(x)=0\): a double leading cluster already containing \(x\) is exhausted by the exact repeated root. The manuscript does not impose the repeated-root equation prematurely.

The \(Q_0,Q_1\) coefficients match the independent reconstructions. The text explains why the normalized-substitution error gains an additional factor 17 in the ordinary equation. At displacement \(1/15\), only shifted coefficients two and seventeen of \(Q_0\) attain value \(17/15\), and their combined residue is \(15\xi^2\neq0\). Both perturbations have strictly greater value. The exceptional \(a_3=0,x=1\) case is separately contradicted by \(Q_0(1)=17^2\cdot76\).

No scope change, precision loss, or omitted case was found relative to DIRECT_JET_THEOREM.md and its independent audits.

## 2. Mixed middle-coefficient configurations

After accounting for assembly's heading-level change, this section is an exact body match to final-manuscript/MIXED.md. Its mathematics was also compared with MIXED_STRATA.md and MIXED_AUDIT.md.

The two exact supports, their exact coefficient zeros restricting them to row 1, and normalization at an actual unit \(H_3\) witness are retained. The first-divided argument precedes the residue sieve and establishes that a repeated root cannot be in the zero cluster.

The assertion \(c_1,\ldots,c_{16}\in17\mathcal O\) is explicitly coefficientwise, derived from the integer normalized family. It is not inferred from residue zero. Both sixteen-marking covers and their divided weights are present. The uniform theorem is used only for the unit-16 marking; the mixed marking is analyzed separately.

The necessary values of \(\nu(a_{16})\) remain \(3/2\) and \(1/2\), obtained from the least nonconstant powers three and one in \(G_{16}\) at its small witness. The invalid estimate \(\nu(a_{16})\geq8\) has not reappeared.

The repeated-root equation establishes the displacement \(1/15\) before scaling. The complete seventeen-root factor and its multiplicities are accounted for. The first-variation formulas correctly retain the critical \(G_{13}\) or \(G_{10}\) witness even though its first derivative vanishes. Neither witness is treated by a simple-root Hensel argument.

A nonzero repeated leading location is excluded by explicit polynomial divisions with nonzero constant remainders, valid over the residue-field algebraic closure. The zero location is treated separately using the fifteenth-power ratios 10 and 13. This forces the paired witnesses into a size-two cluster containing the exact root one and an exact repeated root; multiplicity then proves the exact collision.

The remaining critical derivative is excluded from all outer roots by its exact zero linear term, unit quadratic term, and the proved constant-term bound. Its witness must therefore also equal one. The final rational \(a_{16}\) values both have valuation one and contradict the required values. The optional \(a_{16}=0\) boundary is retained without using a finite valuation for it.

No missing hypothesis, leading-model degeneration, or arbitrary-ramification precision was found.

## 3. Row-2 exact-support exclusion

The exact support \(\{2,4,10,17,18,19\}\) is stated. In particular, the ordinary quadratic coefficient \(F\) is exactly nonzero. This is explicitly used to exclude the mean as the selected \(H_2\) witness. The three low derivative witnesses are consequently placed in the seventeen-root cluster by valid residue and exact-root arguments.

The initial two-stage divisibility proof is preserved. If \(\mu=\min(\nu(T),\nu(F))<1\), either \(c_1\) has value \(\mu\), contradicting the repeated-root equation, or cancellation forces both \(T,F\) to have value \(\mu\). The \(H_3\) displacement \(\mu/17\) then contradicts its root equation. After \(T,F\in17\mathcal O\), the actual derivative witnesses give strict values above one for \(c_1,c_2,T\). The unit degree-nineteen term of \(H_2\), with coefficient \(\binom{19}{2}=171\), is explicitly retained.

The residue table covers all nine oriented choices for the two nonzero middle witnesses. Its only surviving pair retains all four independent sign choices in the two simple outside classes. No equality or opposite-sign relation is assumed between actual witnesses.

The comparison roots \(\pm\sqrt3\) are chosen in an unramified quadratic field only as reference points. Actual roots may be ramified. Their precision follows from a Taylor minimum argument, giving \(a-9\in17^2\mathcal O\) through the exact \(G_4\) identity. Together with \(b+47628\in17\mathcal O\), the manuscript correctly obtains \(c_2-c_1-T\in17^2\mathcal O\).

The descending witness bounds and improved bound on \(T\) establish displacement at least \(1/13\). The leading polynomial captures all seventeen roots, and the actual \(H_1,H_2,H_3\) incidences transfer under integral scaling. Every leading degeneration is treated:

- nonzero \(\lambda_1\);
- zero \(\lambda_1\), nonzero \(\lambda_2\), with repeated location zero;
- nonzero \(\lambda_2\) with nonzero repeated location;
- \(\lambda_1=\lambda_2=0\).

The ratio contradiction \(\rho^2=1/3,\rho^{13}=5\) holds over the full algebraic closure. The surviving size-four cluster contains all three required witnesses before the cluster lemma is applied. Its proof preserves the outside-factor precision, Hasse product rule, and arbitrary ramification. The quartic input and discriminant 4725 are proved explicitly.

After exact collapse, the parameter relation has unit denominator and preserves second-order precision. The four quotient-ring values modulo 289 match both independent checkers. The ordinary-polynomial perturbation lies in \(17^3\mathcal O[X]\), while the \(G_{10}\) perturbation lies in \(17^2\mathcal O[X]\). The divided equations therefore preserve the required residues. The final nonzero residual handles both signs and all four outside-witness markings.

No hypothesis, precision, or coverage was lost relative to ROW2_PROOF.md and ROW2_AUDIT.md.

## 4. Integration item and limits

One nonmathematical integration defect was found in the reviewed snapshot: the mixed-section checker link had target ../next-stage/last-four/middle/check_mixed_strata.py, which does not resolve from the final output directory. It was reported promptly. The assembly owner confirmed that the builder now rewrites this prefix to research/next-stage/; link resolution should be checked after the next rebuild. This does not change any mathematical assertion.

No new census was needed for this transcription review. The formulas were compared with the existing exact receipts and previously reconstructed identities; the valuation and root-count deductions were read separately. Matching arithmetic output is not treated as a substitute for those arguments.

The scoped conclusion is that the three final sections preserve their audited local theorems. The global eight-term theorem also depends on the remaining sections and the complete support/seed cover assigned to the other reviewers.

## Reviewed snapshot fingerprints

- outputs/casas-alvero-eight-term-review/PAPER.md: 7b3cd1c108203dca16118d6af1c81f9dad996db5c51fc8de08ebb4b2971fd0ac
- work/casas-alvero-upgrade/next-stage/last-four/boundary/DIRECT_JET_THEOREM.md: 74cc777678becfc182571550fe82e87cedd4bf00ee792d4518fc31d26855dc48
- work/casas-alvero-upgrade/next-stage/last-four/row2/ROW2_PROOF.md: d6bc0338a391347061745e57a9559dd745bd63d1c2c6c9f918426a7c38645ea0
- work/casas-alvero-upgrade/next-stage/last-four/middle/MIXED_STRATA.md: 9f0e1ff062f320c0de94aca3d8237681ac4e0bb656ee69c5c4050df4d7bbc083
- work/casas-alvero-upgrade/final-manuscript/MIXED.md: b3a4af9c8aaf0fda8db67649e606ce8084c7aaab76115c9b5b5a8e03abccb679

## Final rebuilt-paper readback

The rebuilt PAPER.md was read back on 24 September 2026. The reported mixed-section link now points to research/next-stage/last-four/middle/check_mixed_strata.py, and its target exists. All 7 local Markdown file-link occurrences in the rebuilt paper resolve from the output directory. The integration item above is resolved.

Final PAPER.md SHA-256: 7b3cd1c108203dca16118d6af1c81f9dad996db5c51fc8de08ebb4b2971fd0ac.

The original reviewed snapshot and its fingerprints are preserved above. This final readback confirms the link correction and identifies the rebuilt artifact; it does not broaden the scoped proof review.
