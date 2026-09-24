# Centered six-term degree-20 support frontier

For a centered monic polynomial, write its nonleading support in deficiency indices as
\(f=X^{20}+\sum_{m\in S}a_mX^{20-m}\), with \(S\subseteq\{2,\ldots,19\}\).
Six total nonzero terms means \(|S|=5\). This bounded investigation leaves exactly
three supports after the stated necessary conditions. It does not settle any of
those three families, the whole six-term case, or the Casas–Alvero conjecture.

## Counts and provenance

The old criteria are applied before the two characteristic-13 masks, so their
contribution is explicit. All primes at most 20 are used where applicable.

| Successive filter | Five total terms | Six total terms |
|---|---:|---:|
| All centered supports | 3060 | 8568 |
| Lucas visibility and singleton conditions | 8 | 100 |
| de Frutos two-visible criterion | 4 | 54 |
| Massri common-root restrictions | 4 | 54 |
| Castryck–Laterveer–Ounaïes determinant | 1 | 5 |
| First characteristic-13 mask | 0 | 4 |
| Second characteristic-13 mask, this probe | 0 | 3 |

The two-visible criterion is **previous work**, specifically de Frutos Marín,
Proposition 3.5.5, printed page 57 of her thesis
([primary PDF](https://uvadoc.uva.es/bitstream/10324/3602/1/tesis367-130927.pdf)).
Its coefficient-degeneration guards are retained. The source-index formula and
the deficiency-index formula agree in all 1224 checked pair/prime cases.
The determinant enumeration uses exact integer Bareiss determinants and an
independent modular computation; the published degree-12 fixture is reproduced.
Normal and optimized Python runs agree.

The five old-only six-term survivors are
\(\{3,4,10,18,19\}\), \(\{3,10,16,17,19\}\),
\(\{4,5,10,17,19\}\), \(\{4,10,12,17,19\}\), and
\(\{8,10,16,17,19\}\). The first characteristic-13 mask
\(\{4,8,9,10,11,12,17,19\}\) excludes the fourth.
The old-only five-term survivor is \(\{4,10,17,19\}\), so these old
criteria alone do not reproduce the earlier six-term lower bound.

## The bounded additional exclusion

The only additional algebraic probe considered
\(h=X^{20}+aX^4+cX^3+dX\) over \(\overline{\mathbf F}_{13}\).
The necessary common-root equations for Hasse orders 4, 3, and 1 exclude every
nonmonomial polynomial in this closed coefficient family. The proof treats all
zero-coefficient cases before normalizing. Its main chart reduces to univariate
polynomials \(U,H\) with an exact Bézout identity \(C_UU+C_HH=1\).
The multipliers have degrees 20 and 21, with 43 coefficient slots in total.

The standard-library producer completed in approximately 0.005 seconds. Its
elapsed-time receipt is frozen. The separate read-only replay independently
computes the degree-19 resultant with a 19-by-19 Sylvester determinant and exact
polynomial Bareiss elimination, whereas the producer used a 5-by-5 reduced
determinant. It reconstructs the substitution, multiplies the Bézout identity
directly, checks the exceptional charts, and rejects an intentionally altered
coefficient. Both normal and optimized replay pass. An independent mathematical
audit also passed the normalization and denominator checks and independently
recomputed the resultant.

The valuation/Lucas transfer in [LAST_MASK_PROOF.md](LAST_MASK_PROOF.md) consequently
excludes the full characteristic-zero deficiency mask
\(\{8,9,10,11,12,16,17,19\}\), removing
\(S=\{8,10,16,17,19\}\). This is a written reduction argument together with
an exact arithmetic certificate, not an inference from affine modular emptiness
alone.

## Remaining frontier and limits

The three remaining centered six-term supports are:

1. \(\{3,4,10,18,19\}\);
2. \(\{3,10,16,17,19\}\);
3. \(\{4,5,10,17,19\}\).

For each, the reduction masks at primes 2, 3, 5, 7, 17, and 19 contain an
explicit nontrivial binomial Casas–Alvero degeneration. Excluding the entire
closed reduction family at any of those primes is therefore impossible by
that method. Among primes at most 20, only 11 and 13 avoid this particular
obstruction; each remaining model has four lower coefficients there. This is
a concrete reason that the remaining frontier is harder than the completed
three-coefficient probe. No further eliminations were launched.

These are internally checked candidate results. The exact historical novelty
of the characteristic-13 exclusions remains unassessed. The calculations do not
establish publication importance or independent external validation. Nothing
was published.

## Reproduction files

- `enumerate_sixterm.py`, `enumeration.json`: original exhaustive support sieve.
- `apply_two_visible.py`, `two-visible-results.json`: old two-visible filter.
- `old_baseline_and_groups.py`, `old-baseline-and-groups.json`: old-first counts
  and the prime-dependent degeneration analysis.
- `LAST_MASK_PROOF.md`: complete proof of the additional exclusion.
- `probe_last_mask.py`, `last-mask-probe.json`: producer and frozen receipt.
- `verify_last_mask.py`: read-only exact replay; run with ordinary Python or
  `python -O` from any directory. It does not rewrite the producer receipt.
- `last-mask-verification.json`, `last-mask-optimized-verification.json`:
  successful replay records.
- `frontier.json`: machine-readable three-support frontier.

Frozen producer receipt SHA-256:
`f906bbcc0a82bd63c1512df41272ea4bedeb3670917fd98eae4d83dd5eb8d82f`.
