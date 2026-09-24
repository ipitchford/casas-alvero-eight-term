# Family C: exact obstruction to the proposed modular exclusion

The family under consideration has degree-20 deficiency support
`{4,5,10,17,19}`, hence has the form

\[
f=X^{20}+A X^{16}+B X^{15}+C X^{10}+D X^3+E X.
\]

**Result of this bounded attempt:** the proposed characteristic-11 and
characteristic-13 seed exclusions are false. Neither reduction can exclude
this characteristic-zero support merely by dropping the middle term. The
support remains unresolved. No characteristic-zero counterexample follows.

## Explicit witnesses

The binomial-normalized coefficient of `X^10` disappears modulo 11 or
13 because `binom(20,10)=184756` is divisible by these primes. But the
remaining seed

\[
h=X^{20}+aX^{16}+bX^{15}+cX^3+dX
\]

admits the following CA examples:

| Characteristic | `(a,b,c,d)` | Witnesses for orders `(16,15,3,1)` |
|---:|---|---|
| 11 | `(6,10,0,5)` | `(1,5,0,3)` |
| 13 | `(4,6,3,12)` | `(1,1,2,1)` |
| 13 | `(4,6,10,5)` | `(1,1,11,3)` |

Every other derivative order is witnessed at zero. The two
characteristic-13 examples have all four retained coefficients nonzero,
so this obstruction is not confined to coefficient degeneration.

`check_counterexamples.py` independently constructs each Hasse derivative
from the integer binomial formula and verifies both root conditions at
every order from 1 through 19. This replay is independent of the bounded
prime-field search used to find the examples and remains active under
`python -O`.

## Every prime that kills the middle coefficient has the same obstruction

The exact factorization is

\[
\binom{20}{10}=2^2\cdot11\cdot13\cdot17\cdot19.
\]

The remaining prime divisors also admit CA polynomials inside the same
seed family:

| Characteristic | Polynomial | Only active derivative order; witness |
|---:|---|---|
| 2 | `X^20+X^16` | 16; 1 |
| 17 | `X^20-X^3` | 3; 1 |
| 19 | `X^20-X` | 1; 1 |

The checker verifies all 19 Hasse conditions for these examples too.
Consequently there is no prime at which simply deleting the `X^10`
term by binomial valuation reduction makes this entire seed family empty.

This does not rule out a stronger valuation argument constraining which
modular examples can lift, or another characteristic-zero argument. It
does rule out a unit-ideal certificate for either proposed full seed
system: an ideal containing any of the explicit assignments is proper.
No Groebner unit-ideal computation was run after this obstruction was
found. A subsequently authorized bounded classification of the nonempty
seed scheme is recorded in `ROOT_CLUSTER_NOTE.md`.

## Search scope

`prime_field_probe.py` was a bounded witness search in characteristics
11 and 13. It normalized the highest nonzero coefficient's common-root
witness to 1 and checked the finitely many resulting prime-field
coefficient choices. Search absence would not have proved an exclusion
over algebraic closures; the conclusion here uses only explicit positive
examples and their exact replay. The saved search output is
`prime-field-probe.json`; the theorem-level replay is
`counterexample-verification.json`.

No frozen earlier artifacts were modified. No publication or novelty
claim is made. The root-cluster follow-up restricts possible lifts but
does not exclude family C or establish a seven-term bound.
