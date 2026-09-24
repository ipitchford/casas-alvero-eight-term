# Final research: eight-term theorem, literature and priority boundary

24 September 2026. Updated after the complete exclusion of the fourteen seven-term supports. This replaces this file's earlier four-support status. FINAL_ASSESSMENT.md remains an unchanged historical assessment; EIGHT_TERM_ASSESSMENT.md gives the current significance judgment. No publication or outreach was performed.

## Current mathematical statement

The strongest completed global result in the internally audited package is:

**Every nontrivial characteristic-zero Casas–Alvero polynomial of degree 20 has at least eight nonzero monomials after translation to its mean and monic normalization.**

The leading monomial counts. In binomial-normalized form
\[
f=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\quad a_0=1,\quad a_1=a_{20}=0,
\]
this says that at least seven of \(a_2,\ldots,a_{19}\) are nonzero. It is a lower bound, not an assertion that an eight-term counterexample exists, and it is not a proof of degree 20 or of the full conjecture. An arbitrary translation need not preserve the term count; the mean-centered form is essential.

The earlier theorem excludes fewer than seven terms. The complete necessary-condition inventory for exactly seven terms has been independently rechecked: \(6188\to586\to348\to14\). The final stage now excludes every one of those fourteen exact supports, including both residue branches of \(\{2,4,10,17,18,19\}\). The inventory uses the older singleton/two-visible tests and the CLO determinant; Massri's additional conditions are not needed. The count fourteen is not a fraction of the unrestricted conjecture.

I independently audited the new direct-jet, mixed-stratum, quadratic-support B, support A row-1, and inventory arguments. The separate row-2 proof and its independent audit were read for this assessment; I did not repeat that producer's entire calculation. All these remain internal mathematical audits and exact replays, not external refereeing or formal verification.

## Main new local content

The direct second-jet theorem now unifies the former zero-\(a_3\) and nonzero-\(a_3\) results and includes their missing boundary. In an integral prime-17 normalization with residue \(X^{20}-X^3\), it excludes
\[
a_2=a_{18}=0,\qquad
\bar a_4=\cdots=\bar a_{15}=0,\qquad
\bar a_{16}=-1,
\]
with no requirement that \(a_3\) vanish, and with \(a_4\) allowed to be nonzero. Root valuations, complete cluster multiplicities and a direct nonzero second jet give the contradiction. This is uniform in the intermediate coefficient choices inside this fixed stratum. It is not uniform in degree or prime.

The previous controlled-field approximation argument remains a valid alternative on narrower hypotheses, but is no longer needed for this stronger theorem. The paper should lead with the direct proof rather than count the old and new proofs as separate advances.

The other decisive additions are the two mixed-unit cluster exclusions; the corrected quadratic second jet with discriminant 3; and the row-2 argument that collapses a separated four-root cluster by the quartic Casas–Alvero theorem in characteristic 17, then contradicts a simple outside lift. In each case the substance is the complete bridge from characteristic-zero candidates through arbitrary ramification and all leading degenerations. A finite-field calculation alone would not suffice.

## Primary comparison

**CLO.** [Castryck–Laterveer–Ounaïes](https://arxiv.org/html/1208.5404), arXiv:1208.5404v1, 27 August 2012, supplies the mean-simplicity and missing-derivative determinant theorem used in the inventory. Theorem 2 was reread against the implemented matrix in this update. Proposition 19 and its following remark already use ramification restrictions in degree \(p+1\). Thus neither valuation normalization nor a ramification obstruction is new here. At degree 20 that argument uses prime 19; the new local exclusions concern degree \(17+3\). No direct implication from the stated CLO results to the eight-term bound was identified.

**de Frutos Marín.** The [2013 thesis and university record](https://uvadoc.uva.es/handle/10324/3602?show=full), *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, DOI 10.35376/10324/3602, was inspected in the preceding same-day primary-source pass, including Theorem 3.5.1 and Propositions 3.5.3 and 3.5.5, printed pp.55–57. The singleton and guarded two-visible-support tests are older results and remain credited as such. The direct derivation in the manuscript also establishes the precise formula being used. Those tests leave the fourteen seven-term supports; they do not themselves close the nonempty prime-17 seeds. In particular the seed \(X^{20}-X^3\) passes the singleton test because \(\binom{20}{17}=1\pmod {17}\). This is an exact comparison of those criteria, not a proof that no other thesis argument could imply a special case.

**Marashdeh.** The [live record](https://arxiv.org/abs/2608.14726) still lists only v1, submitted 12 August 2026. The primary [Theorem 5.9](https://arxiv.org/html/2608.14726v1) gives a four-term lower bound across degrees and the preceding section gives a two-element-support criterion. Neither statement is an eight-term theorem in degree 20. The triangular support/witness reduction is useful prior art but does not prove emptiness of its remaining systems. The overlap of its scalar condition with the older thesis remains documented in NOVELTY.md; this manuscript must not reclaim that condition as new.

**Massri.** The [primary record](https://arxiv.org/abs/1806.09561) remains at v6, 25 August 2023. Its [full text](https://arxiv.org/html/1806.09561v6) proves a degree-20 exclusion for three recycled roots and develops valuation/perturbation restrictions. Number of recycled roots is not number of monomials or number of residue classes. None of the new cluster arguments begins with only three exact witnesses. The eight-term theorem is therefore not justified by relabeling that theorem, nor was a direct implication from its hypotheses found. Massri is a methodological predecessor, not a needed extra filter for the fourteen-support inventory.

**Standard ingredients.** Newton polygons, Hasse differentiation, simple-root uniqueness, a unit-Jacobian precision bound, finite-field nonsquares, and reduction of a separated cluster are established techniques. The new candidate contribution is their specific complete application to these degree-20 strata, together with an exhaustive support theorem. The discriminant value 3 is a calculation, not a new general discriminant theorem. No claim of a new universal lifting method is supported.

## Live status check and remaining priority gaps

[Ghosh's record](https://arxiv.org/abs/2501.09272) still lists v1, 16 January 2025, and v2, 21 March 2026. The metadata continues to claim a full proof; no newer revision is displayed. This observation is not a claim that no correction or objection exists elsewhere. The campaign's corrected Proposition 3.3 audit is separate evidence about the written argument and must retain its characteristic-\(p\) scope. It does not furnish a counterexample to the characteristic-zero conjecture. The old assertion that this is the only claimed full proof is not reinstated.

[Gasull's 2026 resultants article](https://doi.org/10.1007/s44425-026-00047-6) still states that 24 is the smallest open degree. The previously inspected citation chain leads to Draisma–de Jong (2011); their [primary erratum](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf), reread in this update, retracts the degree-20 consequence of Theorem 7. No new verified full degree-20 proof was supplied by that chain. Describing the 2026 sentence as inheritance of the old error is an inference, not a demonstrated account of the author's reasoning.

The [ProofAtlas page](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/), refreshed in this update, still explicitly calls for independent audit of its A3 certificate-backed elimination. Its exposed route uses base-19 extraction and different named support components. No exact equivalence to the present eight-term statement or prime-17 local systems was established. This is an unresolved related-source lead, not either a demonstrated collision or priority clearance.

The 2022 NTHU thesis by Shih, Cheng-Pang, *On the Casas-Alvero Conjecture*, remains a full-text retrieval gap from the earlier check. Its [catalog](https://etd.lib.nycu.edu.tw/cgi-bin/gs32/hugsweb.cgi?o=dnthucdr&s=id%3D%22G021090215100%22.&searchmode=basic) identifies a partial-results section on pp.31–33. No claim about the contents of those unseen pages is justified. The new numerical bound does not erase that access limitation.

## Bounded fresh search and conclusion

This update searched combinations of “Casas-Alvero conjecture” with “eight terms”, “eight-term”, “eight monomials”, “8 nonzero terms”, “seven-term”, “seven monomials”, “nonzero monomials”, “degree 20 sparse”, “twenty terms”, “sparsity”, “second jet”, and “discriminant 17”. Targeted variants used arXiv and the Valladolid repository. The primary records and relevant theorem passages above were refreshed; generic mentions of the surname in singularity theory and search-result mirrors were excluded as mathematical evidence. No further broad survey or outreach was performed.

No exact primary-source match for the eight-term degree-20 theorem or the new local obstructions was found in this bounded pass. That supports a carefully qualified originality claim, not a universal novelty certificate. The previous “four supports remain” statement is superseded. The current result closes the whole seven-term sparsity class and gives a substantially stronger specialist paper; its significance assessment is recorded separately in EIGHT_TERM_ASSESSMENT.md.
