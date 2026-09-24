# Broader coefficient constraint: prior-art boundary

Audit date: 23 September 2026. This addendum supersedes the scope discussion in NOVELTY-ADDENDUM.md, not its identified collisions. The characteristic-13 seed proof and its independent verification are maintained by the other agents. This document audits the proposed statement and its relation to prior work.

## Exact proposed consequence

Put \(q=13^e\), \(N=20q\), and

\[
J=\{1,2,3,5,6,7,13,14,15,16,18\}.
\]

The proposed result says that, for a nontrivial characteristic-zero CA polynomial, after any chosen root has been translated to zero, its nonleading coefficient support contains \(qj\) for some \(j\in J\). Here support index \(m\) denotes the coefficient of \(x^{N-m}\). The hypothesis must explicitly exclude a power of a linear polynomial.

The finite characteristic seed is the exclusion, over \(\overline{\mathbb F}_{13}\), of every Hasse-CA polynomial

\[
h(x)=x^{20}+A x^{16}+C x^3+D x
\]

that has a nonzero root. This includes zero-coefficient degenerations; excluding only \(ACD\ne0\) would not justify the consequence. NOVELTY-ADDENDUM.md gives the smaller chart and witness checks; the root/dependency audits check the remaining seed argument.

Independently recomputing binomial residues gives

\[
C_{13}(20)=\{1,2,3,4,5,6,7,13,14,15,16,17,18,19\}.
\]

Its complement in \(1,\ldots,19\) is \(\{8,9,10,11,12\}\), and deleting \(4,17,19\) from \(C_{13}(20)\) gives exactly \(J\). Lucas's congruence gives \(C_{13}(N)=qC_{13}(20)\). Thus, if the \(qJ\) coefficients vanish, the standard valuation normalization reduces the polynomial to \(h(x^q)\); the retained unit root makes \(h\) nontrivial. Hasse derivatives with orders divisible by \(q\) give the necessary CA conditions on \(h\).

For degree 20 centered at the mean root, the forbidden coefficient mask is

\[
T=\{4,8,9,10,11,12,17,19\}.
\]

Consequently every support contained in this particular eight-index mask is excluded. Such a family allows up to nine total terms. **This is not a lower bound of ten terms and does not exclude every polynomial with at most nine terms.** At degree 20 the assertion at a root other than the mean is automatic from its nonzero index-1 coefficient; its main content is the centered assertion. The separately established six-term bound uses additional support enumeration and prior constraints.

## What the literature already supplies

[Graf von Bothmer–Labs–Schicho–van de Woestijne (2007), Proposition 2.6](https://arxiv.org/html/math/0605090v2) explicitly transfers characteristic-\(p\) CA exclusions from degree \(n\) to \(np^k\) through coefficient vanishing and Frobenius/Hasse descent. Proposition 2.2 supplies characteristic-zero transfer using properness. Their §4 already computes a sparse degree-6 quadrinomial family's bad-prime integer with Gröbner bases. Hence the lifting mechanism, modular transfer, and sparse-family arithmetic approach are established. The proposed support-restricted lifting is a new possible application of those mechanisms, not a new principle.

[CLO, proof of Proposition 15 and §§5–6](https://arxiv.org/html/1208.5404) supplies the relevant binomial-normalized coefficient integrality and computational scenario methodology. Its degree-20 determinant and prime-power derivative restrictions were explicitly checked against the small remaining family. They leave \(S_A=\{4,10,17,19\}\), which lies inside \(T\). The checked list of these restrictions therefore does not, by itself, already imply exclusion of the whole mask.

[Massri, Remark 7.4 and Theorem 7.9 proof](https://arxiv.org/html/1806.09561v6#S7) already eliminates the old final four-term family. This is the substantive collision recorded in REPORT.md. The same pair restrictions, three-recycled-root theorem, and valuation-one mask test do not dispose of the remaining \(S_A\) branch. No full degree-20 case-list certificate establishing this seed or broader mask was retrieved. Massri remains a versioned preprint citation in this audit.

[Marashdeh, §§3–7](https://arxiv.org/html/2608.14726v1) contains support stratification, triangular witness elimination, and exact one- and two-support criteria. In particular, the proposed earlier boundary integer was exactly his integer up to sign. The char13 seed can have three nonleading terms and three distinct active witnesses, so its entire open chart is outside the scope of the paper's completed two-support classification. The published description of its computations does not include degree-20 three-support elimination. An applicable general setup is not evidence that this specific elimination was already performed.

## Bounded novelty assessment

No exact characteristic-13 seed exclusion, the corresponding coefficient mask, or its \(20\cdot13^e\) coefficient-hit consequence was located in the checked primary sources or the additional exact-formula searches. No checked implicit argument in those sources was found to give that full seed exclusion. These are bounded search findings, not a guarantee of originality.

The seed exclusion and its precise coefficient consequence are therefore plausible candidate contributions. The extension to infinitely many degrees strengthens the statement's reach, but it does not solve the Casas–Alvero conjecture in any complete new degree: supports meeting \(qJ\) remain. The six-term degree-20 corollary is separate and narrower in degree, while the mask assertion applies to some polynomials with more terms.

The result's potential value is a concise, independently reproducible arithmetic obstruction and a clear new support restriction. The importance of the full conjecture does not by itself establish the publication importance of this partial result. The earlier five-term collision and exact boundary-integer overlap should remain visible in any research handoff; none should be rebranded as new.

## Search limitations

Searches included exact support strings, polynomial exponent variants, prime 13 with degree 20, quadrinomial terminology, coefficient/support constraints, and Spanish coefficient variants. The de Frutos Marín thesis full text remains a retrieval gap. A ProofAtlas route page surfaced, but the accessible page does not provide the underlying A1/A2/A3 mathematical definitions or certificate files; it is not used as proof or priority evidence for this seed. No private or unindexed calculations were inspected. No author was contacted and no result was published.
