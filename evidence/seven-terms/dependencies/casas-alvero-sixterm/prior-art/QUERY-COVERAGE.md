# Bounded search record

23 September 2026, started 11:32 UTC. Task limit: ten minutes. The search was restricted to the three specified families, a seven-total-term degree-20 bound, and recent type/recycled-root computations. The previous thesis and general sparse-method audit was not repeated.

## Exact and formula-oriented queries

- `"Casas-Alvero" "six monomials"`
- `"Casas-Alvero" "seven" "terms"`
- `"Casas-Alvero" "20" "17" "16" "2" "support"`
- `"Casas-Alvero" "20" "17" "4" "3" "sparse"`
- `"Casas-Alvero" "x^{20}" "x^{17}" "x^{16}"`
- `"Casas-Alvero" "x^{20}" "x^{17}" "x^4"`
- `"Casas-Alvero" "x^{20}" "x^{16}" "x^{15}"`
- `"Casas-Alvero" "six terms" OR "seven terms" OR "five-element support"`
- `"Casas-Alvero" "3,4,10,18,19"`
- `"Casas-Alvero" "3,10,16,17,19"`
- `"Casas-Alvero" "4,5,10,17,19"`
- `"Casas-Alvero" "pentanomial" OR "hexanomial" OR "six-term" OR "seven-term"`
- `"Casas-Alvero" "Hermite-Birkhoff" "20"`

No matching exact family theorem was found. Mathematical strings are imperfectly indexed; irrelevant results were not treated as evidence. Absence from these query results is not proof of absence from the literature.

## Recent/type queries

- `"Casas-Alvero" "degree 20" "type"`
- `"Casas-Alvero" "degree 20" "four recycled"`
- `"Casas-Alvero" "six" "monomials" "20"`
- `"Casas-Alvero" "five" "coefficients" "20"`
- `"Casas-Alvero" Naccache "certificate" "degree 20"`
- `"Casas-Alvero" "degree 20" 2026 sparse`
- `"Casas-Alvero" "type" "20" 2025 2026`

The relevant newly refreshed leads were Massri's v6, the public three-recycled-root announcement, and the ProofAtlas research overview. The latter did not expose its internal support definitions or source certificate packet. No comparison to unseen formulas was attempted.

## Primary documents inspected in this round

- [CLO text](https://arxiv.org/html/1208.5404): type/scenario definitions, matching versus canonical scenario, relevant computational scope.
- [Massri v6 §7](https://arxiv.org/html/1806.09561v6#S7): binary mask criteria, placement exclusions, three-recycled-root statement; [version record](https://arxiv.org/abs/1806.09561).
- [Marashdeh v1 §8](https://arxiv.org/html/2608.14726v1#S8): remaining scope of multi-root elimination and support versus witness count.

No full-source package or supplementary computation was downloaded in this round. Massri's reported exhaustive three-root computation was not rerun. Only the three target binary masks were independently recomputed in `replay_three_masks.py`, with results in `three-mask-results.json`.

## Boundaries

This is neither a full literature review nor a certification of primary-source proofs. No unrelated polynomial families were tested. No new claim about unrestricted degree-20 status follows. Prior audit notes on the degree-20/24 survey discrepancy remain unchanged.
