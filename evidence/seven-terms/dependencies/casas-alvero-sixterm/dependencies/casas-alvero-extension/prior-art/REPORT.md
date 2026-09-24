# Prior-art collision and the next sparse degree-20 case

Audit date: 23 September 2026. All writes are confined to this extension directory; the earlier frozen output was not edited. This report concerns mathematical overlap and support bookkeeping, not a certification of the full Casas–Alvero conjecture.

## Finding

**The earlier degree-20 lower bound of five centered terms is already an implicit corollary of arguments in the available literature. It should not be promoted as a new theorem.** The missing overlap is in Massri's *placement restrictions*, not merely the headline three-recycled-root theorem. The previous bounded title/formula searches missed this implication.

For a prospective six-term bound, the same prior argument eliminates one of the three CLO-surviving five-term supports. The two cases still requiring exclusion are

\[
\begin{aligned}
S_A&=\{4,10,17,19\},& f_A(x)&=x^{20}+a x^{16}+b x^{10}+c x^3+d x,\\
S_B&=\{5,15,16,19\},& f_B(x)&=x^{20}+a x^{15}+b x^5+c x^4+d x,
\end{aligned}
\]

with all four displayed coefficients nonzero. No direct exclusion of either complete family was located in this bounded audit. That is an unresolved novelty check, not a priority claim.

## Exact source collision

[Massri, arXiv:1806.09561v6, Remark 7.4](https://arxiv.org/html/1806.09561v6#S7) removes the placements \(y_5=y_{10}=1\) and \(y_{10}=y_{15}=1\). The proof of Theorem 7.9 supplies the corresponding characteristic-five coefficient obstruction. These restrictions are stronger than the three-equal-root condition in Remark 7.8.

The arXiv record dates **v6 to 25 August 2023** and lists no journal reference. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4935880) posted the same-titled preprint on **24 August 2024**. This search did not verify journal publication. Cite the versioned preprint, not the withdrawn earlier full-proof claim or a supposed refereed theorem. [Version record](https://arxiv.org/abs/1806.09561).

Here is the exact affine mapping, which avoids a terminology-based inference. Let the centered polynomial have mean root zero. Choose a multiple root \(r\ne0\), as supplied by the first derivative condition; the mean root is simple by CLO. Set

\[
F(z)=(-r)^{-20}f(r-rz).
\]

Then \(F(0)=F'(0)=0\), and its mean root is \(z=1\). For every derivative order \(i\),

\[
F^{(i)}(1)=(-r)^{i-20}f^{(i)}(0).
\]

Thus a missing coefficient \(a_m\) becomes a placement \(y_{20-m}=1\) in Massri's normalization. The earlier sole four-term family, with support \(\{5,16,19\}\), satisfies \(y_5=y_{10}=1\). It is among the placements already removed in Remark 7.4. The five-term family with support \(\{3,4,15,19\}\) similarly has \(y_{10}=y_{15}=1\).

## Independent proof of the applicable restriction

The following reconstruction checks the source implication without relying on the large resultant enumeration or the rest of Massri's paper. It uses the standard valuation induction in [CLO, proof of Proposition 15](https://arxiv.org/html/1208.5404).

**Lemma.** A nontrivial characteristic-zero degree-20 CA polynomial cannot have a common root with both derivatives of orders 5 and 10, or with both derivatives of orders 10 and 15.

Translate a putative common root to zero. Choose a 5-adic valuation extending the usual valuation on the rationals and scale a nonzero root of least valuation to one. Every root now belongs to the valuation ring \(R\), and one root is exactly 1. Write

\[
F(x)=\sum_{i=0}^{20}\binom{20}{i}b_i x^i,
\qquad b_{20}=1,\quad b_0=0.
\]

All \(b_i\) belong to \(R\). To check this rather than assume it, put \(a_j=b_{20-j}\). The monic multiple of \(F^{(20-j)}\) is

\[
x^j+\binom j1a_1x^{j-1}+\cdots+a_j.
\]

It vanishes at a root of \(F\), which is integral. Induction on \(j=1,\ldots,19\) therefore makes \(a_j\), and hence \(b_i\), integral. Reduction into the characteristic-five residue field gives

\[
\overline F(x)=g(x^5),\qquad
g(y)=y^4-\bar b_{15}y^3+\bar b_{10}y^2-\bar b_5y.
\]

The binomial coefficients outside indices divisible by 5 vanish in the residue field. Hasse derivatives commute with reduction, and
\(\overline{H_{5k}(F)}(x)=H_k(g)(x^5)\) for \(k=1,2,3\). Every common-root witness for \(F\) and a derivative is integral, so its residue must be a common root of the reduced polynomials.

If \(F^{(5)}(0)=F^{(10)}(0)=0\), then \(b_5=b_{10}=0\). The condition \(F(1)=0\) forces \(\bar b_{15}=1\), giving \(g=y^3(y-1)\). Its third Hasse derivative is \(H_3(g)=4y-1\), nonzero at both roots 0 and 1 of \(g\). This contradicts the order-15 CA condition.

If \(F^{(10)}(0)=F^{(15)}(0)=0\), then \(b_{10}=b_{15}=0\), and \(F(1)=0\) gives \(\bar b_5=1\). Now \(g=y^4-y\) and \(H_1(g)=4y^3-1\). At the zero root the latter equals \(-1\); at any nonzero root of \(g\), it equals \(4-1=3\). This contradicts the order-5 CA condition. ∎

The dependency agent separately checked this normalization, coefficient integrality, reduction and Hasse-derivative argument. It is an internal mathematical cross-check, not external peer review.

## Consequences for supports

Let \(S=\{m:a_m\ne0\}\) for the monic polynomial centered at its mean root. The lemma forces

\[
S\cap\{10,15\}\ne\varnothing,
\qquad S\cap\{5,10\}\ne\varnothing.
\]

Equivalently, \(10\in S\), or both \(5,15\in S\). Combine this with the already used CLO restrictions \(19\in S\), \(S\cap\{4,16\}\ne\varnothing\), and the determinant on missing indices \(\{2,\ldots,18\}\setminus S\).

| Size of \(S\) | CLO intersection candidates | Candidates after added pair restrictions | Survivors after the CLO determinant |
|---:|---:|---:|---|
| 3 | 6 | 2 | none |
| 4 | 81 | 31 | \(S_A,S_B\) above |

For size three, the two intermediate supports are \(\{4,10,19\}\) and \(\{10,16,19\}\); their determinant residues are 7 and 12 modulo 19. No computer algebra certificate is needed for the final four-term family once this source overlap is recognized. The old certificate remains a valid independent verification artifact, but that does not create theorem-level novelty.

`replay_support_overlap.py` independently regenerates this table and writes `support-overlap-results.json`; it neither imports nor changes the old code. Its Goncharoff recurrence also checks every derivative equation of each generated binary polynomial.

## What the three-recycled-root result does and does not cover

In a polynomial with \(|S|=s\), choose zero for every inactive derivative and choose one nonzero common root for each active derivative. This uses at most \(s+1\) roots. The bound is on a chosen cover, not automatically on the minimal cover.

With all chosen active witnesses distinct, the two remaining five-term patterns match the following CLO scenarios, in order of derivative orders 1 through 19:

\[
\begin{aligned}
s_A&=(0,1,2,1,1,1,1,1,1,3,1,1,1,1,1,4,1,1,1),\\
s_B&=(0,1,1,2,3,1,1,1,1,1,1,1,1,1,4,1,1,1,1).
\end{aligned}
\]

Here label 1 denotes the mean root; labels 0,2,3,4 denote the four chosen nonzero witnesses. These are **matching scenarios**, not a claim that they are the lexicographically canonical scenarios. CLO explicitly warns in §3.6 that those notions need not agree. The active derivative orders are respectively \(\{1,3,10,16\}\) and \(\{1,4,5,15\}\).

Massri's Theorem 7.10 concerns a cover by three recycled roots. It handles the subcases with at most two distinct active witnesses besides the mean root; it does not, by its statement alone, eliminate the branches using four or five total witnesses. Neither remaining support forces such a collision. [Massri, Theorem 7.10](https://arxiv.org/html/1806.09561v6#S7).

For the corresponding 19-adic binary placement masks, independent evaluation gives

| Support | Indices \(i\in\{2,\ldots,18\}\) with \(c_i=0\) | Integer \(G(1;0,0,c_2,\ldots,c_{18},1)\) | 19-adic valuation |
|---|---|---:|---:|
| \(S_A\) | 3,10,16 | \(-8914483460\) | 2 |
| \(S_B\) | 4,5,15 | \(-448715780\) | 3 |

Thus neither is removed by the valuation-one test of Corollary 7.3, or by the equal-placement exclusions listed in Remark 7.4. The paper describes the 3125 masks as surviving possibilities, not solved cases. The checked text and search did not supply an independently downloadable full computation/certificate list. This audit reconstructed only the relevant masks, not the \(3^{17}\) computation.

## Sparse and specialization methods already in the literature

Marashdeh's [Theorem D and §8](https://arxiv.org/html/2608.14726v1) treat two-element supports in all degrees and leave broader multi-root elimination unfinished. Its support stratification and triangular coefficient elimination overlap with the general method used in the current pilot. The five-term and six-term degree-20 conclusions were not found explicitly there. Absence of an explicit statement does not undo the implicit collision above.

CLO's [§§5.2, 5.3 and 6.1–6.3](https://arxiv.org/html/1208.5404) already provide linear coefficient elimination and finite-field exclusion through projective scenario varieties. Their descendant closure handles points omitted by a normalized affine chart, using the same prime for a scenario and its descendants. Hence finite specialization is established methodology. A finite algebra over \(\mathbb Z_{(p)}\) supplies another standard sufficient condition: if it is finite as a module and its special fiber is zero, [Nakayama's lemma](https://stacks.math.columbia.edu/tag/00DV) makes the algebra zero. Any claimed methodological advance should concern a new useful finiteness certificate or structural reduction, not Nakayama or modular exclusion itself.

For the next pilot, keep collision strata, zero coefficients, and normalized-root boundary points explicit. A modular unit ideal on an affine saturated chart alone does not prove the characteristic-zero stratum empty.

## Recommendation and status correction

Do not publish the previous five-term lower bound as an original research result. A transparent corrected note may record it as a consequence of CLO plus Massri's placement restriction, with the independently checked valuation proof above and the old certificate as supplementary reproduction.

The two remaining families are a concrete next calculation. A complete exclusion would imply a six-term lower bound in centered degree 20, subject to another overlap review. It would still be a sparse partial result, not degree 20 solved. The present audit found no prior elimination of these families, but did not inspect every unpublished or inaccessible computation.

An additional primary status source was located: Draisma and de Jong's own [August 2011 erratum](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf) explicitly restores the exceptional prime 5 and says their earlier claim for degree 20 was incorrect. This is a stronger source for the older degree-20/24 discrepancy than the indirect correction previously located.
