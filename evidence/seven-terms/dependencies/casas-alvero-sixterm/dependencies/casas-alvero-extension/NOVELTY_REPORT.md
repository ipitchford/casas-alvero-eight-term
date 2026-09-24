# Novelty and significance: continuation outcome

23 September 2026. The formula-first novelty-gate workflow was applied to the exact claims in `target.yaml`. Outcomes concern different contribution units and should not be merged into a single claim of novelty.

| Contribution unit | Finding |
|---|---|
| Old lower bound of five centered terms in degree 20 | **Collision:** implicit in existing Massri/CLO arguments; also follows from a short standard valuation argument. |
| Proposed general good-prime integer | **Collision:** equals the negative of Marashdeh's existing two-support integer after matching notation. |
| Valuation normalization, modular exclusion, Frobenius degree lifting, and cyclotomic irreducibility | Established methods. |
| Exact characteristic-13 exclusion of \(X^{20}+aX^{16}+cX^3+dX\) | No matching statement or checked implicit proof located; **bounded uncertainty**. |
| Specified coefficient restriction for degrees \(20\cdot13^e\) | No matching restriction located; an application of established lifting to the preceding finite-field exclusion. |
| Six-term lower bound in centered degree 20 | No matching theorem or checked implicit exclusion located; follows here from the preceding result and published constraints. |

## What was checked more deeply this time

The first audit compared headline sparsity and recycled-root theorems. The continuation inspected the actual placement restrictions and the proofs behind multiplicity statements. This revealed that [Massri, Remark 7.4 and proof of Theorem 7.9](https://arxiv.org/html/1806.09561v6#S7) already removed the previous last four-term family. The exact normalization mapping and an independent short 5-adic proof are in [the overlap report](prior-art/REPORT.md).

The new last five-term family, with deficiency support \(\{4,10,17,19\}\), survives the checked CLO determinant, Massri's pair restrictions, and his valuation-one mask test. Its displayed scenario can use the mean root plus four distinct active witnesses; the three-recycled-root theorem does not by itself cover that branch. No full computational case-list certificate eliminating it was retrieved. The relevant binary placement was independently reconstructed, not inferred from a title or an abstract.

[Marashdeh, Theorem E / Theorem 6.1](https://arxiv.org/html/2608.14726v1) contains exactly the integer that appeared during the exploratory boundary calculation, up to a sign and a renaming of the binomial constants. Its completed two-support classification does not cover the full three-support residue family used in the final proof. The paper is treated as a versioned preprint; its claimed inequality theorem is not a dependency of our final proof.

[Graf von Bothmer–Labs–Schicho–van de Woestijne, Propositions 2.2 and 2.6 and §4](https://arxiv.org/html/math/0605090v2) already develop modular exclusion, prime-power degree transfer, and sparse-family calculations. The infinite sequence of degrees therefore does not establish a new lifting principle. The candidate contribution is the particular finite-field exclusion and the explicit restriction it supplies.

## Exact fingerprints and queries

The principal fingerprints are:

- Degree/exponent pattern `20,16,3,1`, with all coefficient degenerations; the original five-term pattern `20,16,10,3,1`.
- Deficiency support `4,17,19`, the original `4,10,17,19`, and the forbidden centered mask `4,8,9,10,11,12,17,19`.
- The prime 13, ratio equation \(t^{19}=4\), and \(\operatorname{ord}_{19}(13)=18\).
- The exact set \(J=\{1,2,3,5,6,7,13,14,15,16,18\}\), and its derivative-order complement.
- “Six nonzero terms,” centered sparse support, quadrinomial/tetranomial, lacunary/fewnomial, Hasse derivatives, coefficient masks, common derivative roots, and Frobenius lifting.

Queries included alternate polynomial spellings, support and derivative-order conventions, degree 20/twenty, English and Spanish coefficient terminology, and the cited papers' computational sections. The query record is retained in [QUERY-COVERAGE.md](prior-art/QUERY-COVERAGE.md). The result is not naturally a sequence or generating-function identification problem; exact polynomial and support fingerprints, rather than an irrelevant OEIS search, were used.

The [broader addendum](prior-art/BROAD-CONSTRAINT-ADDENDUM.md) records the exact mask translation and method overlap. The [formula addendum](prior-art/NOVELTY-ADDENDUM.md) records the sign-equivalent integer collision and the degenerate residue cases.

## Limits and permitted language

The de Frutos Marín thesis full text remains a coverage gap. Unpublished and non-indexed calculations were not inspected. A secondary route page with inaccessible underlying definitions was treated as a lead, not mathematical or priority evidence. No author was contacted.

“No matching result was found in this bounded check” is warranted. “First proof,” “previously unknown,” “new method,” and “the conjecture is now tractable” are not warranted by this record. At degree 20, the theorem's assertion at a root other than the mean is already supplied by the nonzero nineteenth derivative; its substantive coefficient restriction is centered. At higher degrees, the precise scaled index set must be retained.

The allowed nine-term family is one specified mask. This is not a ten-term lower bound for arbitrary polynomials. The universal degree-20 lower bound established here is six.

## Research judgment

The continuation produced more than a faster computation: it explains the finite-field exclusion by a compact algebraic argument, treats every coefficient degeneration, and derives a complete support restriction for an infinite sequence of degrees. Those outcomes satisfy the agreed further-round objective.

If the exact exclusion is new, it is a plausible short-note contribution. Its significance remains that of a partial arithmetic constraint, not a solution of an open degree or a general breakthrough on Casas–Alvero. Specialist assessment is needed before claiming original priority or publication importance. The full conjecture and the unrestricted degree-20 case remain unresolved by this work.
