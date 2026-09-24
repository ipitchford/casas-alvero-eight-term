# Literature and significance assessment for the upgrade

24 September 2026. Bounded primary-source comparison in the academic-paper literature/citation phase. Only this note was written; frozen evidence was not changed, and nobody was contacted.

## Decision

The centered degree-20 lower bound of **seven total nonzero terms** remains a plausible new specialist result. No exact prior theorem or direct implication eliminating its final family was found in the sources checked. This is stronger evidence than a title search because the actual older modular criterion and the closest recent support theorem were compared algebraically.

It is nevertheless **not yet defensible to certify this result as a strong three-star advance** merely because its proof and replay are extensive. The present evidence supports a potentially publishable, technically nontrivial, but narrow improvement on one unresolved degree. A strong specialist paper is plausible if its main contribution is a reusable, precisely stated exclusion mechanism for bad-prime lifts, with complete applications demonstrating what earlier methods cannot do. General Hensel lifting, finite completed local algebras, valuation comparisons, and Weierstrass preparation are established tools. Packaging them more carefully does not make them new theory.

Two source-access limits remain, now described more precisely below. Neither is evidence that the seven-term theorem has been anticipated. Conversely, neither has been cleared by the available material.

## 1. The exact target and the correct old baseline

The target is:

\[
f=X^{20}+\sum_{m\in S}c_mX^{20-m},\qquad
S\subseteq\{2,\ldots,19\},\quad c_m\ne0
\]

in characteristic zero, after translating the mean root to zero. A nontrivial CA polynomial must have \(|S|\ge6\), hence at least seven monomials including \(X^{20}\). This is a coefficient-support statement, not a statement about distinct roots or the minimum number of recycled derivative witnesses.

The campaign's five-term bound is already an implicit consequence of earlier arguments. The correction identifying Massri's shared-derivative restrictions together with the CLO determinant criterion remains binding. Neither that weaker theorem nor the general visible-support criterion should be reintroduced as new in the upgraded manuscript.

The new mathematical burden is the certified finite-support reduction and the exclusions beyond that older baseline, culminating in

\[
X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,\qquad ABCDE\ne0.
\tag{C}
\]

The campaign's proof treats all six geometric marked configurations in the final characteristic-13 residue classification, including ramified lifts. The literature comparison here assesses originality and significance; it does not replace the separate proof audit.

## 2. de Frutos Marín: the actual Proposition 3.5.5

The primary thesis was retrieved live through the repository's file link. **Use the uppercase filename**:
[2013 thesis PDF](https://uvadoc.uva.es/bitstream/handle/10324/3602/TESIS367-130927.pdf?isAllowed=y&sequence=1),
[metadata and DOI 10.35376/10324/3602](https://uvadoc.uva.es/handle/10324/3602?show=full).
The old lowercase PDF URL failed in this round.

On printed p.57, Proposition 3.5.5 gives a sufficient condition for an allowed exponent set \(I\): its visible subset \(I_p=\{i,j\}\), \(i<j\), must satisfy

\[
a,b\not\equiv1,\qquad
a^\rho(b-c)^\rho(b-ac)^\sigma
-(-1)^\sigma(a-1)^{\rho+\sigma}(b-1)^\rho\not\equiv0\pmod p,
\]

where \(a=\binom ni,\ b=\binom nj,\ c=\binom{n-i}{n-j}\),
\(\rho=(n-j)/g,\ \sigma=(j-i)/g,\ g=\gcd(n-j,j-i)\).
The proof invokes Theorem 3.5.1(b) and Corollary 3.3.6. Thus this is an actual prior theorem, not a conjectural suggestion. The preceding singleton result is Proposition 3.5.3. The author's [2015 conference abstract](https://www.singacom.uva.es/JTN2015/contribuciones/ordinarias/frutos.pdf) independently restates the corresponding four-monomial modular criteria.

Here is the exact comparison in the campaign's deficiency notation. Put

\[
r<s,\quad B=\binom nr,\quad D=\binom ns,\quad
C=\binom{n-r}{s-r},\quad
u=(s-r)/\gcd(r,s),\quad v=r/\gcd(r,s).
\]

The campaign's previously derived boundary integer

\[
N=B^{u+v}(C-1)^u(D-C)^v-(B-1)^v(D-1)^{u+v}
\]

is the same discriminant up to sign after \(i=n-s,\ j=n-r\), because \(c=BC/D\). This symbolic identification was recorded and arithmetically cross-checked in the earlier structural audit. It is not a new elimination principle.

The distinction matters for C. Let \(V_p=S\cap\{m:p\nmid\binom{20}{m}\}\), with \(S=\{4,5,10,17,19\}\). The direct older visibility test has the following obstruction to applicability:

| Prime | Visible deficiencies | Why the singleton/two-visible test does not exclude the whole family |
|---:|---|---|
| 2 | \(\{4\}\) | \(\binom{20}{4}\equiv1\) |
| 3 | \(\{10,19\}\) | \(\binom{20}{10}\equiv1\) |
| 5 | \(\{5,10\}\) | \(\binom{20}{10}\equiv1\) |
| 7 | all five | More than two visible positions |
| 11 | \(\{4,5,17,19\}\) | More than two |
| 13 | \(\{4,5,17,19\}\) | More than two |
| 17 | \(\{17,19\}\) | \(\binom{20}{17}\equiv1\) |
| 19 | \(\{19\}\) | \(\binom{20}{19}\equiv1\) |

For \(p>20\), none of these binomial coefficients vanishes, so all five positions remain visible. This comparison exhausts primes for this particular direct test. It does not exhaust every possible consequence of the thesis.

One cannot bypass the entries congruent to 1 by applying an exact two-coefficient finite-field criterion: a nonzero characteristic-zero coefficient can disappear after valuation normalization. The allowed reduced family includes singleton degenerations, and those are precisely why the hypothesis must be retained. The campaign's C argument goes beyond this direct test by using the lost middle derivative after division by 13 and controlling its possible lifts.

## 3. Marashdeh and Massri: precise overlap and non-overlap

[Marashdeh, arXiv:2608.14726v1](https://arxiv.org/html/2608.14726v1), 12 August 2026, was reread at Theorems A–E and Section 5. Its explicit centered term-count consequence is at least four terms in arbitrary degree. Its complete two-element-support criterion is not the degree-20 seven-term result. Its general scenario reduction eliminates coefficients but leaves a multiroot system, not a proof of its emptiness.

Under \(C_1=B,C_2=D,E=C\), the integer in its Theorem E is exactly \(-N\) above. Thus citing only this 2026 preprint as the origin of that arithmetic obstruction would miss the thesis predecessor. No Hensel-lift exclusion matching the final C calculation was found in the inspected argument. These comparisons do not certify all claims of the preprint.

[Massri, arXiv:1806.09561v6](https://arxiv.org/html/1806.09561v6), 25 August 2023, has a different principal degree-20 target: exclusion of three recycled roots. Its Remark 7.4 and the proof of Theorem 7.9 already contain the restrictions responsible for the five-term novelty correction. Theorem 7.10 reports exhaustive three-witness elimination, not arbitrary coefficient sparsity. No complete public replay was retrieved here.

There is a concrete reason not to identify this theorem with C's last obstruction. In the campaign's difficult \((\bar v,\bar u,\bar w)=(2,2,1)\) branch, the required witnesses for orders 19, 16, 3, and the divided order-10 condition occupy four distinct residue classes \(0,1,2,4\). A three-recycled-root theorem does not directly close that branch. The campaign closes it by a second-precision contradiction. This is an exact hypothesis distinction, not a claim that every indirect implication of Massri has been excluded.

## 4. ProofAtlas and the unavailable thesis

The live [ProofAtlas page](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/) still describes an unaudited A3 certificate route and unresolved A1/A2 systems involving base-19 extraction, an affine mean equation, and finite algebras. Its source/status date is 15 August 2026. It explicitly separates bounded degree-20 work from an all-degree theorem. The public material does not supply support exponents, defining integer ideals, complete certificates, or an exact equivalence between its A-labels and this campaign's C. It even records that no source-package attachment was executed in that collection.

**Finding:** related techniques are reported; neither an exact collision nor non-overlap is established. The public page is a research map, not a sufficiently specified prior theorem. It should be acknowledged as an unresolved source lead, not treated as an automatic bar to originality or as proof of priority. No contributor action, sign-in, or outreach was attempted.

The [NTHU catalog](https://etd.lib.nycu.edu.tw/cgi-bin/gs32/hugsweb.cgi?o=dnthucdr&s=id%3D%22G021090215100%22.&searchmode=basic) identifies the 2022, 35-page master's thesis *On the Casas-Alvero Conjecture* by **Shih, Cheng-Pang (施政邦)**, supervised by Jow, Shin-Yao. Earlier wording “Shih Cheng Pang” should not be parsed as surname Pang. Chapters 3–5 cover established predecessors; Chapter 6, pp.31–33, contains the author's attempt and partial results. No electronic full-text link was exposed in the retrieved record, the new-catalog link failed, and exact English/Chinese author and record-ID searches yielded no primary full text. The abstract and contents do not establish overlap. The missing pages remain a bounded source-access limitation.

## 5. What a local-method contribution can honestly claim

The useful distinction is between excluding a geometric special fibre and excluding all characteristic-zero lifts of a **nonempty** special fibre. The latter is what makes the campaign's bad-prime work potentially valuable. To establish it one must cover every geometric residue point, all coefficient degenerations and witness assignments, and possibly ramified lifts. A count of prime-field points or a failed unramified lift does not suffice.

The general ingredients remain standard:

- The \(p\)-adic normalization, integrality induction, and valuation restrictions already have CA predecessors in [CLO](https://arxiv.org/html/1208.5404) and Draisma–de Jong.
- Finiteness of a normalized degree-20 characteristic-zero locus is not itself new: Massri's Sections 5–6 already address finiteness/algebraicity in degrees including \(20=19+1\). A new explicit completed algebra may improve effectivity without establishing a new finiteness phenomenon.
- An invertible Jacobian, simple-root uniqueness, and the implicit/Hensel function argument are standard. Being valid under ramification is an essential hypothesis check, not alone a new theorem.
- Preparation of a series congruent to \(Z^r\) into a monic degree-\(r\) polynomial is classical. [Berger's primary exposition](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf), Corollary 1.2, supplies the complete-ring formulation used here.
- A complete local algebra finite over a DVR need not be flat or torsion-free. A zero generic fibre can coexist with a nonempty special fibre because the algebra is torsion. These distinctions must remain explicit in any general criterion.

The plausible new content is consequently **support- or residue-family-specific**: complete geometric classifications, proved bounds on cluster splitting, divided-derivative congruences that cannot lift, and exact finite certificates covering all admissible local charts. The C theorem is an example with a completed conclusion. The general characteristic-17 finite-chart constructions and whole-branch exclusions could be a stronger organizing contribution, but only to the extent that their exact statements, coverage, and genuinely new consequences are separately proved.

## 6. Significance judgment and upgrade requirements

The seven-term theorem has a legitimate specialist audience. It treats the first persistently difficult degree and deals with a real limitation of simple reduction: bad-prime solutions that need not lift. The proof's arbitrary-ramification coverage and the nontrivial second-precision branch give more substance than a bare enumeration of supports.

The limitation is equally material. It resolves no new unrestricted characteristic-zero degree, no uniform family of unrestricted degrees, and no new general obstruction currently known to force the conjecture. A seven-term lower bound excludes sparse counterexamples; it does not describe the remaining dense locus. More certificate files, stronger wording, or another nearby term-count increment would not by themselves establish high significance.

For a defensible strong specialist submission, I recommend:

1. State one precise reusable local exclusion theorem with checkable input hypotheses, including nonreduced algebra and ramified-point coverage. Explain which part is an application of standard machinery.
2. Give the seven-term result as a full application, with an explicit comparison against the older visible-support test above.
3. Include a second mathematically distinct complete application if already proved, preferably an unrestricted residue branch. Avoid substituting a partially exhausted scenario list for a theorem.
4. Keep the Ghosh criticism in a separate audit note or tightly delimited appendix; it does not add originality to the positive theorem.
5. Describe the two access gaps without claiming either a collision or universal novelty. Correct the thesis author and working PDF URL in the manuscript bibliography.

**Assessment:** plausible specialist advance; significance presently moderate; a “strong three-star” label is not established by the evidence examined. A coherent local-lifting theorem with substantive completed applications could support a stronger assessment. This is a research judgment, not a promise about a journal or an external grading outcome.

## Search boundary

The pass directly inspected the de Frutos thesis's relevant proposition and its 2015 companion, Marashdeh's exact support theorems, Massri's placement/three-root/finiteness claims, CLO's relevant framework, Berger's preparation statement, ProofAtlas's exposed route record, and the NTHU metadata. Targeted searches included the exact seven-term phrase, the deficiency tuple \(4,5,10,17,19\), ramification/Hensel with Casas–Alvero, the unavailable thesis's English and Chinese author, and its catalog ID. Unrelated and secondary search hits were not used as mathematical evidence. No exact seven-term collision was retrieved. The bounded search is not an exhaustive novelty certification.
