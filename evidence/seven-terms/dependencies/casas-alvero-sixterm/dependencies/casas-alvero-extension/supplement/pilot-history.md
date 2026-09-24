# Five-total-term degree-20 extension

## Outcome

The fixed-degree five-term support filter leaves one family after the published CLO and Massri restrictions and the separately proved visible-support lemma. A modular certificate for that family is independently checked here, together with the exact finiteness hypotheses needed for its characteristic-zero transfer. See CHARACTERISTIC_ZERO_TRANSFER.md.

This is a sparse-degree-20 result. It does not establish the full degree-20 Casas-Alvero conjecture or historical novelty. No publishing action was taken. The original four-term package was not modified.

## Enumeration

For centered support S of four nonleading terms, there are 3060 possible supports before forcing the linear term. CLO Theorem 2 forces 19 in S, leaving 680. Prime-power restrictions from CLO Proposition 15 retain 81; the determinant alone retains 25. Their intersection is exactly:

    (3,4,15,19), (4,10,17,19), (5,15,16,19).

Massri's pair exclusions retain the last two. The visible-support lemma at prime 3 excludes (5,15,16,19): its only visible index is 19, but binomial(20,19)=20 is 2 modulo 3, whereas the singleton case requires residue 1. The remaining support is

    (4,10,17,19), corresponding to {20,16,10,3,1} as polynomial exponents.

The checker evaluates the CLO determinant by exact integer Bareiss elimination and an independent modular triangular Schur complement on all 680 cases. It reproduces the published degree 12 fixture. Both ordinary and optimized Python runs pass. The visible-support lemma is derived in the separate explanation work; it is not presented as a theorem literally quoted from CLO.

Primary sources: [CLO, Theorem 2 and Proposition 15](https://arxiv.org/html/1208.5404), [Massri, Remark 7.4 and Theorem 7.9 proof](https://arxiv.org/html/1806.09561v6#S7). Other checked necessary conditions concerning distinct roots, multiplicities, symmetric root pairs, and rationality did not yield an additional support-only exclusion here.

## Bounded pilot history

All ordinary ideals were generated from triangular Hasse conditions with chosen witnesses 1,u,v,w. No distinctness conditions were imposed.

| Support | Prime | Outcome |
|---|---:|---|
| (4,10,17,19) |31|20-second timeout; inconclusive|
| (4,10,17,19) |37|20-second timeout; inconclusive|
| (4,10,17,19) |41|20-second timeout; inconclusive|
| (5,15,16,19) |31|20-second timeout; inconclusive|
| (5,15,16,19) |37|Proper zero-dimensional ideal,9.38seconds|
| (5,15,16,19) |41|20-second timeout; inconclusive|
| (4,10,17,19) |11|Proper zero-dimensional ideal,0.058seconds|
| (4,10,17,19) |7|Proper zero-dimensional ideal,7.06seconds|
| (4,10,17,19) |13|Root's reduced two-variable computation: unit ideal and certificate,0.25seconds; independently verified here|

The eliminated family's short probes had already progressed before the new support restriction arrived. There are no running CAS jobs and no large queued campaign. Precise times and source/log hashes appear in modular-results.json and small-prime-results.json. A proper ideal in a finite field is not a characteristic-zero counterexample.

## Successful certificate and transfer

The root supplied a modulo 13 lift certificate, reproduced locally as mod13-certificate.txt. Its SHA256 is 23552e44cc926d21e48b0e57e2022d309b91c34df265292a8dc753f61cd000d9. It has 1777 terms across three coefficient polynomials, with maximum total degree 38.

The independent verifier derives the integer equations using four formal Hasse witnesses before normalizing the first. It checks coefficient b vanishes modulo 13, verifies the exact finite polynomial identity and a corruption control, and checks the relevant degree 37 Macaulay matrix has determinant 5 modulo 13. The remaining w relation is monic degree 19. These checks support the written finite-module/Nakayama proof; modular affine emptiness by itself is never treated as sufficient.

## Reproduction

    python3 enumerate_supports.py
    python3 -O enumerate_supports.py
    python3 verify_mod13.py
    python3 -O verify_mod13.py

Both checkers use only the Python standard library. Re-running the modular pilot requires Singular 4.4.1 and is unnecessary to verify the successful finite certificate. Exact normalized coefficients and equations are recorded in mod13-verified-equations.json.

## Assurance

The finite identities and support arithmetic are independently implemented and checked. The normalization, visible-support lemma, Macaulay degree-reduction argument, and characteristic-zero transfer are written mathematics. No independent external review, proof-assistant verification, or priority assurance is claimed.
