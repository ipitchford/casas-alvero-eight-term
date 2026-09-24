# Degree-20 sparse candidate: independent pruning and novelty audit

23 September 2026. This addendum supersedes the earlier note's 816-to-136 pilot recommendation: published constraints reduce the four-term centered case to **one polynomial family**. It independently verifies that reduction. It does not certify the parent's subsequent elimination of that family.

## Exact indexing and determinant replay

Let a hypothetical degree-20 counterexample be translated and scaled to

\[
f(x)=x^{20}+\sum_{m=2}^{19}a_m x^{20-m},\qquad f(0)=0,
\]

and define its coefficient support by \(S=\{m:a_m\ne0\}\). The vanishing of \(f^{(20-j)}(0)\) is equivalent to \(a_j=0\). Thus the indices in Castryck–Laterveer–Ounaïes (CLO), Theorem 2, are the **missing coefficient indices**, not the active support and not the derivative orders themselves. The binomial normalization of coefficients in CLO does not change their vanishing in characteristic zero. [CLO, Theorem 2 and §3.5](https://arxiv.org/html/1208.5404).

For \(J=\{j_1<\cdots<j_t\}\), the independently transcribed matrix has first column \(-1\), lower triangular block

\[
D_{rs}=j_r\binom{j_r-2}{j_s-2}\quad(s\le r),
\]

and final row \((-1,(-1)^{j_1},\ldots,(-1)^{j_t})\). The necessary condition is \(\det\Delta_J\equiv0\pmod {19}\).

`prior_art_determinant_check.py` implements exact integer Bareiss elimination and a separate finite-field Gaussian elimination. It first reproduces CLO's five degree-12 pairs \((3,8),(5,6),(6,8),(6,9),(7,9)\), and then agrees by both methods on all 136 supports \(S=\{m_1,m_2,19\}\). The surviving supports are exactly

\[
\{4,17,19\},\quad\{5,16,19\},\quad
\{10,11,19\},\quad\{10,12,19\}.
\]

The full exact determinants and their residues are stored in `prior-art-determinant-results.json`. The script was rerun after review and passed. This is an independent transcription and arithmetic replay, not an independent proof of CLO's theorem.

## Published constraints reduce six supports to one

CLO Proposition 15 forbids a common root for the specified equally spaced derivatives of a counterexample of degree \(np^k\); its stronger clause applies when \(n=p^r+1\). [CLO, Proposition 15](https://arxiv.org/html/1208.5404).

Applying it at the centered root zero gives the following consequences:

| Degree decomposition | Derivatives that cannot all vanish at zero | Required support intersection |
|---|---|---|
| \(20=(19+1)19^0\) | orders 1 and 19 | \(19\in S\), since the order-19 derivative already vanishes |
| \(20=(2^2+1)2^2\) | orders 4 and 16 | \(S\cap\{4,16\}\ne\varnothing\) |
| \(20=4\cdot5\) | orders 5, 10 and 15 | \(S\cap\{5,10,15\}\ne\varnothing\) |

These three sets are disjoint. Therefore \(|S|\ge3\) already follows from published work in degree 20; the candidate needs **no dependency on Marashdeh's unrefereed two-support theorem**. If \(|S|=3\), exactly six supports are possible. Applying the same determinant gives:

| Support \(S\) | \(\det\Delta_{\{2,\ldots,18\}\setminus S}\bmod19\) |
|---|---:|
| \(\{4,5,19\}\) | 15 |
| \(\{4,10,19\}\) | 7 |
| \(\{4,15,19\}\) | 10 |
| \(\{5,16,19\}\) | 0 |
| \(\{10,16,19\}\) | 12 |
| \(\{15,16,19\}\) | 13 |

Hence the only remaining centered four-term family is

\[
\boxed{f(x)=x^{20}+a x^{15}+b x^4+c x,\qquad abc\ne0.}
\]

Its exclusion would prove that a degree-20 counterexample has at least **five nonzero terms after centering at the mean root**. No statement about the number of terms before centering follows. This would not settle degree 20 or the full conjecture.

The three support restrictions are also reflected by Massri's degree-20 placement constraints in Remark 7.8. Their use, the determinant condition, and triangular coefficient elimination should all be attributed; the mathematical contribution under consideration is the remaining family's exclusion and its certificate. [Massri, current v6, §7](https://arxiv.org/html/1806.09561v6#S7).

## Closest checked literature and novelty boundary

Marashdeh's Theorem D / Theorem 5.9 proves a lower bound of four centered terms in arbitrary degree. The introduction expressly limits its multi-root elimination to two-element support; §8 leaves the broader elimination problem open. The paper does not state the degree-20 five-term bound or exclude the family above in the checked text. It also explicitly separates the number of terms from the known lower bound of five distinct roots. Its root-assignment triangular reduction is relevant prior art even though the present degree-20 theorem need not depend on its unrefereed inequality proof. [Marashdeh, v1, Theorem D, Remark 5.10 and §8](https://arxiv.org/html/2608.14726v1).

Massri's current Theorem 7.10 excludes degree-20 counterexamples with three recycled roots. A three-element coefficient support permits the origin plus three chosen nonzero common roots, so it need not be covered by that theorem. Likewise, a four-term polynomial can have many distinct roots. These three invariants must remain separate. [Massri, v6, Theorem 7.10](https://arxiv.org/html/1806.09561v6#S7).

Searches on 23 September 2026 included Casas–Alvero combined with:

- the exact support strings `5,16,19`, `4,17,19`, `10,11,19`, `10,12,19`;
- the polynomial spellings `x^{20}`, `x^20`, `x20`, combined with `x^{15}`, `x15`, `x^4`, and `x^{20}+a`;
- `at least five terms`, `five nonzero terms`, `four nonzero terms`, `four-term`, `four monomials`, `three-element support`, degree `20` and `twenty`;
- `quadrinomial`, `quadrinomials`, `quadrinómios`, `quadrinôme`, `quatrinomial`, `tetranomial`, `lacunary`, `fewnomial`, and `sparse`.

No primary result matching the exact single-family exclusion or the centered degree-20 five-term conclusion was located. This is a **bounded no-hit result**, not proof of novelty. Formula indexing is weak, older computational case lists may subsume it without stating a term bound, and non-indexed or unpublished material remains outside coverage. No author was contacted.

## Publication assessment

Conditional on a checked elimination certificate and its characteristic-zero transfer, this is a precise positive result worth preserving as a short mathematical note or reproducible certificate artifact. Its contribution is a stronger sparse constraint in the smallest degree treated as open in the checked specialist literature. The earlier status note records the conflicting survey sentence about degree 24.

It is a modest partial advance, not a result comparable in importance to resolving the full conjecture. Most of the reduction follows quickly from established theorems; novelty would reside in the last family's exclusion. A compact explanatory identity, an extensible sparse-support argument, or an independently checked certificate would strengthen its publication case. A finite-field unit ideal on an affine saturated chart alone is insufficient; the proposed unsaturated finite-algebra/Nakayama transfer must be stated and checked separately. The parent reports that this check is underway, and this addendum does not substitute for it.
