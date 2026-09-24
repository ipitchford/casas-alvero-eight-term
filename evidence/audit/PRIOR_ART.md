# Casas–Alvero: bounded status and route audit

**Historical reconnaissance snapshot.** Its proposed pilot has since been completed. Read `NOVELTY_REPORT.md` and `SPARSE_DEGREE20_PROOF.md` for the final conclusions; the original wording below is preserved as a search record.

Audit date: 23 September 2026. Primary-source checks plus explicitly identified unverified leads. No publication or contact with authors was undertaken. This note does not independently certify any cited proof or computation.

## Recommendation

Proceed with the small Proposition 3.3 counterexample and a precise repairability analysis. For positive research, pilot the degree-20 four-term centered case before contemplating an all-degree campaign. A full-conjecture commitment is not justified merely by finding a gap.

## Status corrections

1. **Ghosh's current arXiv proof claim is v2, 21 March 2026.** The live version history lists v1 and v2 only. Proposition 3.3 states equality of local and global minimal generator numbers at every minimal prime under its binomial-product characteristic restriction. Its proof's cancellation argument includes the assertion that inverting a zero divisor makes the quotient zero. Theorem 3.6 and Corollary 3.9 lead onward to Theorem A. The degree indexing there is polynomial degree n+1. [Version history](https://arxiv.org/abs/2501.09272), [v2 text, §3](https://arxiv.org/html/2501.09272v2#S3).

2. **“The only claimed full proof” is too strong.** Zhipeng Lu's arXiv:1707.04754 abstract also claims a full proof. This audit has not assessed that claim. Massri's 2018 v1 also claimed a proof; its subsequent history contains withdrawals and its current v6 is a narrower result. Use “the Ghosh proof claim being audited.” [Lu's record](https://arxiv.org/abs/1707.04754), [Massri's version history](https://arxiv.org/abs/1806.09561).

3. **Do not say no public objection exists.** A MathDB progress summary reports a July objection to Lemma 5.4 of Ghosh's prequel and links to X. This is an unverified lead, not mathematical evidence: the X link failed twice in the web retrieval tool; a direct MathDB retrieval returned HTTP 403. Exact-phrase searches did not recover the original post. Do not attribute an objection to an identifiable person or repeat its proposed counterexample without obtaining the primary material. [Discovery lead](https://mathdb.com/p/315857/casas-alvero-conjecture).

4. **The prequel is separately accepted research.** Its arXiv record currently shows v3, 14 January 2025, and §5 contains Lemma 5.4, a claim about choosing representations with compatible highest T-degree parts. The journal publisher lists *A finiteness result towards the Casas-Alvero conjecture* among American Journal of Mathematics papers accepted on 7 April 2026. This acceptance neither validates the later full-conjecture claim nor disposes of a subsequently alleged defect. [Prequel](https://arxiv.org/abs/2402.18717), [Lemma 5.4 text](https://arxiv.org/html/2402.18717v3), [publisher's accepted-papers list](https://www.press.jhu.edu/journals/american-journal-mathematics).

## Degree 20 versus degree 24: an actual source conflict

Armengol Gasull's *A Primer on Resultants and Their Applications*, published **28 May 2026**, says in §3.4 that “n=24” is “the lowest degree open case.” Its reference [19] is Draisma and de Jong's **2011** EMS article. No new proof of degree 20 is presented or cited in that section; the worked cases are degrees 4 and 5. [Published article](https://doi.org/10.1007/s44425-026-00047-6).

There is a documented reason not to infer a degree-20 theorem from the old reference: Chellali's 2012 manuscript corrects the 2011 determinant argument, explicitly identifying 5 as a bad prime for degree 4. It uses the witness X²(X−1)(X+1) over F5 and gives the corrected exceptional set {3,5,7} for the 4p^e route. Thus that route does not establish degree 20=4·5. The archived PDF was accessible through CiteSeer; HAL itself returned an anti-bot page. [Chellali, §1, primary manuscript mirror](https://citeseerx.ist.psu.edu/document?doi=61ef2169153411ea5589433b19ff05c02e953c35&repid=rep1&type=pdf), [HAL record](https://hal.science/hal-00748843).

**Inference, not an author-confirmed explanation:** Gasull's “24” may inherit the 2011 missing-exception problem. It is not evidence of a new solution of degree 20. In contrast, the recent subject-specific sources below explicitly identify 20 as unresolved. A bounded search found no primary proof settling all degree-20 cases after them. The safest status is: **degree 20 is the smallest open degree in the checked specialist literature, with one conflicting survey sentence that supplies no degree-20 proof.**

## Relevant positive results and exact boundaries

| Source | Result relevant to this campaign | Implication |
|---|---|---|
| [Castryck–Laterveer–Ounaïes, *Mathematics of Computation* 83 (2014), arXiv:1208.5404](https://arxiv.org/html/1208.5404) | Theorem 2: for d=p+1, the mean root c satisfies f'(c)≠0, plus a determinant restriction. Theorem 5 settles degree 12. Section 1.10 records about three weeks and 90GB for each of the five hardest degree-12 scenarios. Theorem 4 records the exceptional primes in degrees 5–7. | Degree 20 centered support must contain 19. Historical computational costs counsel structural reduction; they are not current hardware benchmarks. |
| [Massri, arXiv:1806.09561v6 (2023), §7](https://arxiv.org/html/1806.09561v6#S7) | Theorem 7.10 excludes degree-20 polynomials with three recycled roots. Theorem 7.9 excludes a root of multiplicity at least 11 in degree 20. Remark 7.4 reduces a certain 19-adic binary placement list to 3125 cases. Theorem 7.10 reports checking 3^17 assignments in under 48 hours. | Three-recycled-root exhaustion is prior art. Four-term support is a different invariant and allows four recycled roots. Reported computation was not replayed here. |
| [Marashdeh, arXiv:2608.14726v1 (12 August 2026)](https://arxiv.org/html/2608.14726v1) | Explicitly treats Ghosh as unverified and degree 20 as open. Support reduction and triangular elimination separate coefficient support from recycled roots. Theorem D excludes centered support of size two over characteristic zero. Section 8 identifies multiple-root scenario elimination as unfinished. | A size-three-support exclusion is the next sparse case. The claimed all-degree two-support theorem is an unrefereed dependency unless independently checked. Its reduction can be proved directly in the new note. |
| [Schaub–Spivakovsky, arXiv:2411.13967v1, §§1–3](https://arxiv.org/html/2411.13967v1) | Degree 20 is the first open case. Regularity of the elementary-symmetric root ideals is equivalent to the conjecture. Macaulay matrices yield bad-prime criteria and conditional bounds. | Merely proving the complete-intersection replacement in characteristic zero may restate the hard conjecture. A small ideal certificate is much more bounded. |

## Sparse four-term pilot: derivation without an unrefereed theorem

This is elementary algebra, written here to specify the proposed computation independently.

Write a monic centered polynomial as

f(x)=x^d+Σ_{k=1}^s a_k x^(d−m_k), 2≤m_1<⋯<m_s≤d−1,

with all a_k nonzero. Its root at zero supplies the derivative conditions whose corresponding coefficient is zero. For each remaining condition choose a root r_k common to f and its Hasse derivative H_(d−m_k). Evaluating this derivative gives, with m_0=0 and a_0=1,

a_k = −Σ_{i=0}^{k−1} binom(d−m_i,m_k−m_i) a_i r_k^(m_k−m_i).

The coefficient of a_k is exactly one, so this is an identity-based elimination, not a division by an unknown determinant. Since H_(d−m_k)(0)=a_k≠0, every r_k is nonzero. Scale r_1 to one. For s=3, put r_2=u and r_3=v; the coefficients are explicit integer polynomials in u,v, and impose f(1)=f(u)=f(v)=0. Saturate by uv a_2 a_3; a_1=−binom(d,m_1) is already a nonzero constant in characteristic zero. Collisions u=1, v=1, or u=v remain allowed and therefore need not invoke a separate recycled-root theorem.

For d=20 there are binom(18,3)=816 triples before known pruning. The published d=p+1 constraint forces m_3=19, leaving **binom(17,2)=136** triples. If the parent computation includes all 816 it provides a self-contained stronger replay boundary; if it uses the 136 reduction, Theorem 2 must be cited and its hypotheses checked. A pilot that handles only some triples must list them exactly and state every unhandled triple as unresolved.

**Certificate requirement:** exact emptiness over Qbar must be established by a rational ideal-membership or equivalent exact certificate. A finite-field calculation on this *affine saturated* chart does not automatically prove characteristic-zero emptiness: solutions may specialize onto deleted divisors. Modular calculations are useful as discovery and independent arithmetic checks unless a proper/projective specialization argument or lifted certificate is supplied.

**Useful output:** a proved subset exclusion, an algorithm with independently checked certificates, or a structural identity that explains a family of sparse exclusions. **Not yet justified:** a full degree-20 theorem, an all-degree result, a priority claim, or importance comparable to a complete solution.

## Bounded novelty search

Searches included exact and close variants of:

- Casas-Alvero + Proposition 3.3; local/global minimal number of generators; non-zerodivisor/zero divisor; Ghosh error/gap/erratum/comment;
- Ghosh + Lemma 5.4; Casas-Alvero July 2026 counterexample;
- Casas-Alvero + four terms / four-term / four monomials / quadrinomial(s) / fewnomial / sparse polynomial / three coefficients / three-element support;
- Casas-Alvero + degree 20 / support 20 / four recycled roots; the named papers' current arXiv histories and relevant sections.

No matching primary sparse-four-term theorem or explicit public Proposition 3.3 objection was located in this search. This is **not** a claim that none exists. In particular, non-indexed author material, unpublished work, and the inaccessible social-media objection remain outside coverage. The accessible research that most directly overlaps is Marashdeh's two-support result and Massri's three-recycled-root computation.

No external outreach was attempted. No source-status claim in this note should be silently upgraded to independent proof validation.
