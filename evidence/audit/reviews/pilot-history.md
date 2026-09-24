# Bounded sparse pilot report

## Result

The informative support (5,16,19), meaning f=x^20+a*x^15+b*x^4+c*x with a*b*c nonzero, is excluded over characteristic zero by an exact finite-field certificate together with a proved finite-module lifting lemma. See NORMALIZATION.md and LIFTING_LEMMA.md for the mathematical proof, and mod31-verification.json for the portable checker receipt.

This is a sparse-class result, not a solution of degree20 or the Casas-Alvero conjecture in full. No publication was attempted.

## Research trajectory and limits

1. The initial fixed ten supports from {2,3,4,5,6} all gave unit ideals over Q even before saturation. Exact rational Nullstellensatz certificates were exported and independently verified by standard-library rational polynomial arithmetic. Singular also returned unit bases for the corresponding Rabinowitsch saturation ideals. These are controls only: prior results already exclude these supports.
2. Theorem2 of Castryck-Lauter-Ounaies forces a degree20 centered counterexample to have a nonzero linear term. The independent Schur-complement audit in clo-audit.py checks all136 remaining support pairs and reproduces the published degree12 fixture. It leaves four triples: (4,17,19), (5,16,19), (10,11,19), (10,12,19). This is an application of known prior art.
3. A direct rational Rabinowitsch Gröbner computation for (4,17,19) reached its90-second cap without a conclusion. Its source and timeout receipt remain. Other obsolete high-degree probes were cancelled after stronger prior-art pruning; their incomplete logs are not success receipts. No all816 Gröbner campaign was launched.
4. The root/prior-art audit reported that Proposition15 further leaves only (5,16,19). A rational two-variable computation on that support was started and then cancelled when the root found a fast modulo31 route. No uncompleted rational computation is represented as a proof.
5. This agent independently regenerated the modulo31 system from the binomial Hasse formulas, obtained a lift certificate, and wrote a standalone exact verifier. The identity has1800 certificate terms and maximum total degree39. Both ordinary and optimized Python runs passed, including an altered-coefficient negative control.
6. The finite-module lifting lemma uses the univariate degree19 u relation with leading coefficient -4844, invertible modulo31, and a monic degree19 v relation. It converts the mod31 unit identity into absence of all characteristic-zero solutions of the unsaturated equations.

## Reproduction

From this directory:

    python3 verify_mod31.py
    python3 -O verify_mod31.py
    python3 clo-audit.py
    python3 verify_certificates.py

Generating the successful finite-field certificate requires Singular4.4.1, but checking it requires only Python's standard library. To regenerate without appending duplicate terms, remove only the generated mod31-m-5-16-19.certificate.txt file before running Singular on mod31-m-5-16-19.sing. The ordinary control runner deletes each of its own output files before regeneration.

The main certificate SHA256 is e63069da3f19151f84cd44ec9f5c46e55d6d806e743c0ccbd25827c6214020a0.

## Files

- NORMALIZATION.md: full equivalence and quantifier boundaries.
- LIFTING_LEMMA.md: explicit finite-module proof and application.
- verify_mod31.py: independent modular identity and integer integrality checker.
- mod31-m-5-16-19.sing / .log / .certificate.txt: generator, unit-basis receipt, explicit identity.
- mod31-verification.json and mod31-optimized-verification.json: exact verification receipts.
- clo-audit.py / .json / .md: independently derived support filter using published Theorem2.
- run_pilot.py / results.json / m-*.certificate.txt: ten rational control certificates.
- verify_certificates.py: independent rational sparse-polynomial certificate checker.
- high-results.json: bounded timeout evidence, not an exclusion claim.

## Assurance

Two distinct symbolic generation/checking implementations were used, with a separate internal audit of normalization and published determinant indexing. These are internal checks. No external referee, formal proof, or historical novelty assessment is implied. Sparse support pruning beyond Theorem2 is owned by the root/prior-art audit and must be stated with its exact published hypotheses in any integrated theorem.
