# Bounded prior-art audit of the three remaining six-term supports

23 September 2026. Scope: supports A, B, C in `../fingerprints.json`, and the prospective centered degree-20 lower bound of seven total nonzero monomials. No other family was computed; older outputs remain unchanged. This is a bounded overlap audit, not historical-priority certification or a proof of the proposed bound.

**Finding:** no exact family exclusion or seven-term degree-20 theorem was located in this search. The three families survive the specifically checked Massri binary-placement criteria. A recent public research overview describes other degree-20 support work without exposing the exact supports or certificates; that remains an unresolved overlap lead.

## Exact target and aliases

The deficiency index \(m\) multiplies \(X^{20-m}\). Thus the characteristic-zero families are

\[
\begin{aligned}
A:&\ X^{20}+aX^{17}+bX^{16}+cX^{10}+dX^2+eX,\\
B:&\ X^{20}+aX^{17}+bX^{10}+cX^4+dX^3+eX,\\
C:&\ X^{20}+aX^{16}+bX^{15}+cX^{10}+dX^3+eX.
\end{aligned}
\]

All five nonleading coefficients are nonzero on each exact characteristic-zero support. Reduction modulo 11 or 13 removes the degree-10 coefficient, leaving respectively the seed exponent sets

\[
\{20,17,16,2,1\},\quad\{20,17,4,3,1\},\quad\{20,16,15,3,1\}.
\]

Any modular exclusion used to infer characteristic-zero emptiness must include coefficient-loss and root-collision strata. The seed is a closed family with coefficients allowed to vanish. Merely excluding its full-coefficient affine chart would not exclude the original family.

## Recycled roots, type, and terms are different counts

[CLO, §§1.2–1.4](https://arxiv.org/html/1208.5404) defines polynomial type as the minimum number of roots needed to witness every derivative condition, minus one. A matching scenario need not be the polynomial's canonical scenario. Its general bound on the total number of distinct roots also does not bound the number of monomials.

Our elementary application is as follows. Each target has five active derivative orders; the other fourteen derivative conditions can use the mean root zero. Choosing a witness for each active derivative uses at most six roots altogether, so a hypothetical target polynomial has type at most five. It need not have type two: the five active witnesses have not been proved to collapse to two distinct nonzero roots. Formal patterns with all five active witnesses distinct have matching type five. Those patterns are bookkeeping possibilities, not examples of existing CA polynomials.

[Massri v6, Theorem 7.10](https://arxiv.org/html/1806.09561v6#S7) concerns three recycled roots. This would eliminate branches admitting at most two distinct active witnesses besides the mean root, but its statement does not eliminate the full target families. The [arXiv version record](https://arxiv.org/abs/1806.09561) still identifies v6 as 25 August 2023; no later version was displayed during this check.

## Exact placement comparison

In Massri's normalization, a chosen multiple root becomes 0 and the mean root becomes 1. Starting from a centered polynomial \(f\), choose a nonzero multiple root \(r\) and put

\[
F(z)=(-r)^{-20}f(r-rz).
\]

Then \(F(0)=F'(0)=0\), and
\(F^{(i)}(1)=(-r)^{i-20}f^{(i)}(0)\).
Consequently an absent centered coefficient at deficiency \(m\) supplies mean-root placement \(y_{20-m}=1\). On exact support, the active derivatives cannot use that mean root. This is the concrete mapping needed to compare coefficient sparsity to placement literature.

[Massri, Corollary 7.3 and Remark 7.4](https://arxiv.org/html/1806.09561v6#S7) give a binary-mask test at 19: valuation one of the relevant Goncharoff integer excludes the mask. Remark 7.4 also removes the simultaneous mean placements at derivative pairs \((4,16),(5,10),(10,15)\). Its 3,125 remaining masks are possibilities, not a claim that all have been eliminated.

The standard-library script `replay_three_masks.py` independently forms the monic Goncharoff polynomial using descending coefficient recursion. Every derivative condition is checked by direct evaluation. Only these three masks were computed:

| Family | Active derivative orders | Integer \(G(1;0,0,c_2,\ldots,c_{18},1)\) | 19-adic valuation |
|---|---|---:|---:|
| A | \(1,2,10,16,17\) | 3,397,381,830 | 2 |
| B | \(1,3,4,10,17\) | 17,994,492,640 | 2 |
| C | \(1,3,10,15,16\) | 34,050,015,292 | 2 |

None contains one of the forbidden mean-root pairs. Thus these specific earlier criteria do not provide the requested exclusions. Both normal Python and `python3 -O` replay passed; all checks use explicit exceptions. This is an arithmetic source-implication check, not a CA emptiness certificate.

## Recent and related material

[Marashdeh v1, §8](https://arxiv.org/html/2608.14726v1#S8) distinguishes coefficient support and recycled-root scenarios; its explicit elimination settles two-element support, while general multi-root elimination remains a proposed next step. No listed A/B/C family or seven-term degree-20 result was located there. Its triangular coefficient elimination is relevant method background, not an existing exclusion of five-element supports.

The already inspected 2013 de Frutos thesis and the previous audit's singleton/two-visible-support replay were not searched again. Their established priority and limitations remain recorded in `work/casas-alvero-structural/prior-art/REPORT.md`. The present targets are the three survivors of those earlier checks; this round did not re-enumerate the full support space.

A [ProofAtlas research overview](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/) advertises degree-20 internal supports A1, A2, A3 and an outstanding certificate audit. The accessible page gives no exponent definitions or underlying source package. Its labels must not be equated with this project's independently assigned A, B, C. It is an overlap lead, not a usable mathematical exclusion or independent validation. The underlying comparison remains unresolved.

A [public post by David Naccache](https://www.linkedin.com/posts/david-naccache-4a1350_no-degree-20-counterexample-to-casasalvero-activity-7497623468948148224-4v5V) also announces the three-recycled-root conclusion. No additional support-level theorem or proof package was retrieved through that result. The accessible Massri preprint already states that conclusion; the post does not extend the present overlap boundary.

## Assessment

The prospective seven-term statement remains a reasonable bounded calculation target. No demonstrated prior-art collision was found for A, B, C, but novelty is not established by this search. If all three are excluded, the claim should be a coefficient-sparsity restriction after centering, with the exact inherited filters and proof certificates identified. It would not settle unrestricted degree 20, nor imply a minimum of seven recycled or distinct roots.

The unresolved ProofAtlas source package and non-indexed computations are explicit coverage gaps. No outreach, submission, or publication was attempted. Search details are in `QUERY-COVERAGE.md`.
