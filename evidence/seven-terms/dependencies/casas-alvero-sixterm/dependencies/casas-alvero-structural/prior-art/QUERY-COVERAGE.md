# Search coverage

Search date: 23 September 2026. Primary sources were used for factual mathematical comparisons. Search-result absence is a bounded negative finding, never proof that no prior result exists. This round supplements previous audits; it does not replace their recorded gaps.

## Thesis and sparse-priority retrieval

Queries included:

- `"Perspectivas aritméticas" "Casas-Alvero"`
- `"Frutos Marín" "Casas-Alvero" tesis`
- `"Un problema sobre números combinatorios" Frutos pdf`
- `"JTN 2015" "Frutos" Casas`
- `"Perspectivas" "Casas-Alvero" "cuatro" monomios`

These located the university thesis metadata, working alternate PDF URL, and official 2015 conference abstract. Within the thesis, targeted searches/readbacks covered the trinomial determinant, modular singleton/two-support criteria, discriminants/resultants, degree 20, propagation, condensation, and expansion. No characteristic-13 seed or centered degree-20 six-term theorem was identified in those inspected portions.

## Moving-family and method aliases

Queries combined `Casas-Alvero` with:

- `"p+7" "p+3"`, `"p + 7"`, `"p+7"`, `"p+3"`, `"p + k"`
- `"Frobenius" sparse`, `"Frobenius" "gcd"`, `"Frobenius" "rational"`
- `"dynamical"`, `"exceptional primes"`, `"prime" "quadrinomials"`
- `"p+7" "35"`, `"p+3" "35"`
- `"289"`, `"35" "17" Frobenius`, `"51" "35"`
- `"rational map"`, `"dynamical gcd"`, `"Frobenius compatibility"`
- `"finite" "support" "p+7"`

No exact primary-source match to the family, rational map, or uniform finite-characteristic theorem was located. Related results include fixed-degree bad-prime/discriminant arguments, prime-power transfer, and Kreidl's other sparse families. The gap between a fixed-degree statement and one fixed integer for degrees varying with the characteristic was checked directly against the de Frutos propagation/condensation discussion.

A final bounded search for the second characteristic-13 seed used `"Casas-Alvero" "x^{20}" "x^4"`, `"Casas-Alvero" "20" "13" "four monomials"`, and `"Casas-Alvero" "8,10,16,17,19"`. No exact match was located. This search also returned Gasull's 2026 published resultant primer, which repeats the previously recorded smallest-open-degree-24 claim. This audit does not resolve the earlier degree-20/24 status conflict or infer a full degree-20 proof from that sentence.

## Replay boundary

`check_known_criteria.py` verifies formula aliases and applications of the older support criteria. It is not a literature search, a proof of nonexistence outside those criteria, or a theorem of historical priority. Results are in `known-criteria-results.json`.

Only the ten displayed degree-20 supports were independently replayed here. Broader support enumeration, the characteristic-13 seed proof, the Frobenius norm construction, and exceptional-prime boundary computations belong to the other agents' audits.

## Claims deliberately not made

- No assertion that all public literature or all thesis pages have been searched.
- No assertion that no correction, comment, proof, or alternative treatment exists.
- No inference that an unrefereed preprint establishes current acceptance.
- No statement that the resultant's divisors are exactly the exceptional primes.
- No claim of a new proof of an unrestricted characteristic-zero degree.
