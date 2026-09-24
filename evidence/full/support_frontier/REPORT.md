# Full centered degree-20 support coverage

The existing criteria leave **2,482 exact supports**, across total term counts
7 through 17. The old criteria alone leave 2,490. The current closed masks,
A/B exclusions, and exact C exclusion remove eight of those supports. This
is a coverage diagnostic, not another sparsity-bound objective; no surviving
support is asserted to contain a CA polynomial.

| Total nonzero terms, including leading term | Old-criteria survivors | Current survivors |
|---:|---:|---:|
| 2–4 | 0 | 0 |
| 5 | 1 | 0 |
| 6 | 5 | 0 |
| 7 | 14 | 14 |
| 8 | 68 | 67 |
| 9 | 213 | 212 |
| 10 | 367 | 367 |
| 11 | 523 | 523 |
| 12 | 514 | 514 |
| 13 | 417 | 417 |
| 14 | 241 | 241 |
| 15 | 101 | 101 |
| 16 | 22 | 22 |
| 17 | 4 | 4 |
| 18–19 | 0 | 0 |
| **Total** | **2490** | **2482** |

Support means the nonzero deficiency indices \(S\subseteq\{2,\ldots,19\}\)
in \(f=X^{20}+\sum_{j\in S}a_jX^{20-j}\), after translating the root of
the nineteenth derivative to zero. The monomial is the permitted trivial
case and is excluded from this counterexample inventory.

The old tests are Lucas visibility and singleton restrictions at all primes
at most 20, de Frutos's two-visible condition with its coefficient-degeneration
guards, the previously checked Massri conditions, and CLO's degree-\(p+1\)
mean-root theorem. The last theorem forces the linear term to be nonzero,
at least two further missing coefficients, and its determinant condition.
The exact theorem and determinant were rechecked against
[CLO, Theorem 2](https://arxiv.org/html/1208.5404#S1.Thm2).

The determinant computation uses a triangular Schur complement. If \(J\)
is the list of missing indices and \(T_{jk}=j\binom{j-2}{k-2}\), solve
\(Tz=\mathbf1\) modulo 19. The original determinant is
\((-1)^{|J|}(\prod_{j\in J}j)(\sum_{j\in J}(-1)^jz_j-1)\).
An independent modular Gaussian elimination agreed on **all 48,750 eligible
determinants**. The published degree-12 fixture also passed. Normal and
optimized/direct enumerations have identical inventory hashes.

The masks were used at their proved scopes: the characteristic-13 masks
\(\{4,8,9,10,11,12,17,19\}\) and
\(\{3,8,9,10,11,12,16,17,19\}\); A's characteristic-zero closed support
\(\{3,4,10,18,19\}\); and C's exact support
\(\{4,5,10,17,19\}\). A's characteristic-zero proof was not extended
to additional invisible coefficients without a new argument.

## Reusable full-coverage models

| Prime | Distinct visible support patterns among survivors | Maximal closed models needed | Largest number of lower coefficients |
|---:|---:|---:|---:|
| 2 | 3 | 1 | 2 |
| 3 | 30 | 1 | 6 |
| 5 | 5 | 1 | 3 |
| 7 | 2482 | 214 | 16 |
| 11 | 2432 | 74 | 16 |
| 13 | 1401 | 1 | 13 |
| 17 | 13 | 1 | 5 |
| 19 | 1 | 1 | 1 |

“Maximal” is inclusion-maximal among the observed visible masks. A closed
model includes all coefficient degenerations; its covering count may overlap
with another maximal model. These reductions do not establish emptiness.

Characteristic 17 gives a particularly compact model covering the entire
unrestricted degree-20 problem:
\[
h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX.
\]
Writing \(U=X^{17}+c\), \(V=X^3+aX+b\), it satisfies
\[
h=UV+dX^2+(e-ac)X-bc,\quad H_3h=U,\quad H_{17}h=V,
\]
\[
H_2h=3XU+d,\quad H_1h=(3X^2+a)U+2dX+e-ac,\quad
H_{18}h=3X^2+a.
\]
Thus this model can be classified using low-degree incidence conditions
despite the original degree 20. It contains genuine CA seeds, so the next
full-coverage task is **complete seed and marked-root classification followed
by valuation lifting obstructions**, not a search for an empty modular mask.
The separate `prime17` subdirectory is the bounded attempt at this task.

Characteristic 19 is smaller but highly singular: after unit-root normalization
the reduction is \(X^{20}-X=X(X-1)^{19}\). All nonzero exact roots reduce
to one cluster, so the simple-root rigidity used for A does not by itself
settle this model. At 2 and 5, Frobenius reduces the problem to bad-characteristic
degree-5 and degree-4 seed models. Nonempty binomial degenerations already
prevent wholesale closed-mask exclusion at every listed prime.

## Files and limits

`inventory.json` records every survivor, every new exclusion, every prime-mask
group, and all counts. `summary.json` is the shorter inventory.
`enumerate_frontier.py` is read-only by default; `--write` explicitly saves
an inventory, and `--direct` checks every determinant independently.
`run.json` and `direct-replay.json` contain the matching replay fingerprints.

The inventory concerns degree 20 only. It gives no uniform all-degrees
reduction and does not solve the unrestricted degree-20 conjecture. No
publication, outreach, or historical-priority claim is involved.
