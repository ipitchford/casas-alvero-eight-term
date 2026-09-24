# Tame characteristic-17 branches: exact normalforms and the remaining obstruction

This bounded investigation does not exclude another complete branch. It gives
exact necessary factor forms and explicit positive-dimensional rational
families satisfying all the forced visible incidences. The selected examples
have the correct characteristic-17 reductions and supports surviving every
previous support filter, but fail the still-unresolved derivative conditions.
Thus they are not Casas--Alvero counterexamples.

All row numbers refer to the complete nine-seed classification. Write

    f(X)=sum_{j=0}^{20} binom(20,j) a_j X^(20-j),
    a_0=1, a_1=a_20=0.

The exact mean root is simple. The restrictions used below are those proved
in `../LIFT_CONSEQUENCES_17.md`. No simple residue value is silently equated
with its integer representative: roots with residues 6, 7, 10, or a quadratic
extension value remain variable unless an explicit construction chooses them.

## Necessary characteristic-zero factor forms

In each formula the remaining factor is monic.

- **Row 4:** a_2=-1 and a_3=a_17=0. There is a simple root 1, a
  simple Hasse-second-derivative witness v with residue 6, and a double root
  r whose residue satisfies Y^2+3Y+3=0. Consequently

      f=X(X-1)(X-v)(X-r)^2 g_15,   H_2 f(v)=0.

  The two quadratic residual clusters each have size two; only one of them
  is required to supply the H_1 witness. The formula does not force both
  clusters to collapse.

- **Row 6:** a_2=-1, a_3=2, a_17=0. The H_17 and H_18 witnesses are
  the same simple root 1. The H_2 witness v has residue 6; the unique
  multiple root r is double and has residue 10. Thus

      f=X(X-1)(X-v)(X-r)^2 g_15,   H_2 f(v)=0.

- **Row 7:** the same three coefficient conditions hold. H_2, H_17,
  and H_18 share the simple root 1. The unique multiple root r is double
  and has residue 7. Thus

      f=X(X-1)(X-r)^2 g_16,   H_2 f(1)=0.

- **Row 9:** a_2=a_17=0, a_3=-1. The cluster-collapse result gives
  an exact triple root 1, which is the only multiple root. Thus

      f=X(X-1)^3 g_16.

  The coefficient restrictions are especially transparent in this factor:

      g_16 = X^16+3X^15+6X^14-1130X^13
             +sum_{i=3}^{12} b_i X^i
             +(3b_1-3b_0)X^2+b_1 X+b_0.

  The twelve b-parameters are free at this stage; the seed reduction fixes
  their residues but not their characteristic-zero values. The simple mean
  root requires b_0 != 0 and in the integral seed chart it is a unit.

These forms encode the visible Hasse orders 1,2,3,17,18,19. They do not
impose the thirteen orders 4 through 16, except when a corresponding zero
coefficient already supplies the mean root as a witness.

## Explicit surviving partial-incidence families

To test whether the displayed conditions already contradict the other known
support requirements, the constructor chooses convenient exact witnesses.
These choices are constructions, not necessary conditions on an arbitrary
lift:

| Row | Convenient imposed factor | Affine dimension after all imposed conditions |
|---|---|---:|
| 4 | X(X-1)(X-6)(X^2+3X+3)^2 | 6 |
| 6 | X(X-1)(X-6)(X-10)^2 | 8 |
| 7 | X(X-1)(X-7)^2 | 9 |
| 9 | X(X-1)^3 | 11 |

The dimensions also incorporate a chosen exact support from the earlier
2,482-survivor inventory. Every chosen support survives all old necessary
criteria and the completed earlier sparse exclusions. The exact branch
constraints leave the following numbers of inventory supports compatible:

| Row | Required deficiency indices | Forbidden indices | Compatible supports |
|---|---|---|---:|
| 4 | 2,18,19 | 3,17 | 198 |
| 6 or 7 | 2,3,18,19 | 17 | 157 |
| 9 | 3,18,19 | 2,17 | 240 |

For each construction, let S be the chosen support and fix the required
coefficients of X^18 and X^17. For every remaining supported coefficient,
write its ordinary value as its prescribed seed residue plus 17z_j. The
root, derivative, and factor-divisibility conditions are a rational linear
system in z. Its coefficient matrix has full row rank modulo 17. Choosing
pivot columns therefore gives an inverse over Z_(17), and the remaining
parameters range freely over Z_(17).

It follows that all members of the resulting affine family have the exact
visible incidences, the stated seed reduction, integral binomial-normalized
coefficients, and a simple mean root. Generic members have the chosen exact
support; a concrete full-support member is supplied for every row. The
directions and origin are saved, and an independent replay checks the whole
affine family by linearity and verifies its dimension from the free-column
coordinate matrix 17I.

Every selected member provably fails additional derivative conditions:
eleven failed orders for each of rows 4, 6, and 7, and twelve for row 9.
For each failure the replay checks a coprime reduction at a prime preserving
degrees and denominators. This proves that the fixed rational polynomial
has nonzero characteristic-zero resultant with that derivative. It is not
an affine-modular-emptiness inference about an unknown family.

For example the row-9 member is the integral polynomial

    X^20-1140X^17-51578X^16+116501X^15-64923X^14
    +17X^13+34X^12+51X^11+68X^10+85X^9+102X^8
    +119X^6+136X^5+153X^4+184X^2+190X.

It has the required exact triple root, coefficient zeros, all six visible
incidences, and the exact row-9 reduction. Nevertheless H_4 already has no
root in common with it (certified modulo 101). No claim of a CA example is
made or intended.

## The extra row-9 lifting equation

Set u_j=a_j for 4<=j<=16 and impose the exact double-root equations at 1.
Solving them gives

    a_18=(18221-sum (19-j) binom(20,j) u_j)/190,
    a_19=(-17082+sum (18-j) binom(20,j) u_j)/20.

The extra triple-root condition is the exact equation

    H_2 f(1)/17 = -8037
        +sum_{j=4}^{16} binom(19-j,2) [binom(20,j)/17] u_j = 0.

Modulo 17 its constant is 4, and its coefficient vector in increasing j is

    (5,15,3,9,9,16,10,16,9,9,3,15,5).

The row-9 seed factors as

    X(X+2)(X-1)^3
    (X^5-3X^4-2X^2-5X-3)
    (X^10+4X^9-X^8+6X^6+X^4-6X^3+4X^2+7X-8).

The factors of degrees five and ten are irreducible over F_17, independently
checked by Frobenius remainders and proper-subfield gcds. The seed has eighteen
distinct roots and splitting-field degree ten. Restricting witnesses to
prime-field roots would therefore omit most allowed cases.

The parent task's separate étale lifting argument may turn this last linear
congruence and higher congruences into finite branch obstructions. This file
does not claim that any residue assignment satisfies those congruences, or
that a partial-incidence family satisfies the remaining CA conditions.

## Replay files

- `construct_partial_families.py` produces the exact rational origins,
  directions, full-support examples, and failed-derivative certificates.
- `partial-families.json` is the saved data; normal and Python `-O` producer
  runs agree exactly.
- `check_partial_families.py` imports no producer code and checks the saved
  data using rational arithmetic, factor division, and modular Euclidean
  gcds. Normal and `-O` replays pass.
- `check_row9_factor_and_obstruction.py` checks the exact factorization,
  irreducibility, and triple-root linear equation independently of the
  partial-family constructor.

No new whole-branch exclusion was obtained. The useful outcome is a precise
limit: the tame visible conditions, even combined with the existing support
filters, admit large exact integral families. Any exclusion needs substantive
information from the unresolved derivative incidences or another prime.

A subsequent bounded test does exclude one five-element marked witness
orbit inside row 9 at the second 17-adic digit. Its exact certificate and
ramification-safe proof are in `ROW9_ONE_SCENARIO_PROOF.md`; this is a
scenario exclusion, not a whole-branch exclusion.
