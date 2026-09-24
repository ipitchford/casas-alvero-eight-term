# Complete-domain bit-vector prototype: bounded search remains unresolved

The integer/linear-programming encoding was replaced by a pure QF_BV
encoding with no integer variables and no modular-division operator. It
correctly verifies the known extension-field SAT fixture in 0.35 seconds.
**No new residue point or exclusion was found:** all four unrestricted or
partially pruned search pilots returned `unknown` because of their time
limits. No UNSAT result is claimed.

## Exact coverage of the encoding

The fixed row-9 seed is h=X^20-X^17-3X^2+3X. Its eighteen distinct roots
lie in K=F_(17^10): three roots in F_17, five of degree five, and ten of
degree ten. The complete root domain is saved in each full-field receipt
and independently checked. The irreducibility checks, root evaluations,
and the triple multiplicity at one prove that no algebraic-extension root
is missing.

For every j=4,...,16, the encoder has one root-choice variable taking all
eighteen root indices and ten coordinate variables for a_j in K. Each
coordinate has the exact domain 0,...,16. Conditional on a root choice,
the equation

    a_j+r_j^j-binom(j,3)r_j^(j-3)
      +sum_{i=4}^{j-1}binom(j,i)a_i r_j^(j-i)=0

is a system of ten linear equations over F_17. Multiplication by each
fixed root power is encoded by its exact F_17-linear coordinate matrix.
The triangular equations determine every a_j uniquely for every marked
root assignment. Finally the ten coordinate equations for

    T=-8037+sum_{j=4}^{16}binom(19-j,2)[binom(20,j)/17]a_j=0

are imposed. These conditions are equivalent to the complete first-residue
problem for the selected domain. They are only necessary conditions for
the characteristic-zero lifting problem.

To encode an F_17 linear congruence, all scalar coefficients are first
reduced to 0,...,16. The positive integer sum is placed in a bit-vector
wide enough for its maximum possible value. There can be no overflow,
because each input coordinate is at most 16. If the hexadecimal digits
of that sum are d_0,d_1,..., the sum is congruent modulo 17 to

    d_0-d_1+d_2-d_3+...,

since 16=-1 modulo 17. The encoder tests this small signed sum against
all multiples of 17 in its proven range. Eight-bit arithmetic represents
that range without signed aliasing. The largest actual positive-sum
width is fifteen bits. The independent replay exhaustively checks the
fold predicate for every value at widths five through fifteen, totaling
65,504 checks.

This is a complete finite encoding, not a completed enumeration. Its
model-blocking clause removes only the returned marked root assignment,
so unbounded repeated SAT queries would enumerate the selected finite
domain in principle. No performance bound or independently checkable
UNSAT certificate is supplied by that statement.

## Complete field-domain partition

The assignment domain can be partitioned without losing any case:

1. Every witness belongs to F_(17^5): eight root choices and five field
   coordinates per coefficient.
2. At least one witness is a degree-ten root: retain the full eighteen-root
   domain and require one such choice.

The flags `--subfield5` and `--degree10` implement these two parts. The
first part has 8^13 assignments before further constraints; the unsplit
domain has 18^13 assignments. The `--nonprime` flag is an optional pilot
restriction and is not part of the proof of complete coverage. The bounded
searches below used it explicitly; they do not cover the all-prime-field
subcase, and no claim of full execution of this partition is made.

## Safe use of the 240 old support masks

Row 9 forces exact a_2=a_17=0, with a_3,a_18,a_19 nonzero. Exactly 240
supports in the previously verified necessary-criterion inventory satisfy
those restrictions.

The mean-root residue class contains only the exact root zero. Therefore
an exact nonzero a_j cannot have a derivative witness reducing to zero:
that witness would be exactly zero and G_j(0)=a_j would vanish. Conversely,
when exact a_j=0, we may choose zero as the witness. Thus every genuine
row-9 counterexample has a marking whose zero-choice positions agree
exactly with its zero-coefficient positions.

The flag `--old-support-filter` restricts the nonzero-choice pattern to
those 240 support masks. It preserves at least one marking of every
potential characteristic-zero counterexample. It is not a claim to keep
every redundant marking of every first-residue solution. Crucially, a
nonzero-choice position is **not** required to have nonzero coefficient
residue: an exact nonzero coefficient may be divisible by 17.

## Bounded performance receipts

| Pilot | Domain | Build time | Solver time | Result |
|---|---|---:|---:|---|
| Fixed known fixture | Full F_(17^10) encoding, all choices fixed to fixture | 1.07 s | 0.35 s | SAT, independently replayed |
| Unseeded nonprime | Full eighteen-root domain | 1.09 s | 28.74 s | unknown / timeout |
| Initial fixture hints only | Full domain; hints do not constrain choices | 1.35 s | 17.37 s | unknown / timeout |
| Subfield component | Eight-root domain, nonprime witness required | 0.18 s | 25.24 s | unknown / timeout |
| Subfield + 240 support masks | Same eight-root domain and safe support pruning | 0.28 s | 25.18 s | unknown / timeout |

Every search had an independent external process deadline of thirty or forty
seconds. The internal timeout was fifteen, twenty, or twenty-five seconds,
depending on the recorded command. Some internal deadlines overshot during
native solver work; the external guard remained in place. No large queue,
18^13 enumeration, or unbounded native job was launched.

The fixed SAT fixture is the degree-five marked orbit already excluded at
the next 17-adic digit in `../tame17/ROW9_ONE_SCENARIO_PROOF.md`. Verifying
its first-residue SAT status is a consistency check, not a new surviving
characteristic-zero candidate.

A cvc5 finite-field alternative was also inspected. The installed binary
rejects even a one-variable field equation because it was built without
CoCoA; its exact error is recorded in `cvc5-capability.json`. No dependency
installation or field-solver run was attempted after that capability check.
The official [finite-field documentation](https://cvc5.github.io/docs/latest/theories/finite_field.html)
describes the prime-field theory; extension fields would still require
coordinate encoding or a separate algebraic representation.

## Files and conclusion

- `residue_bv.py`: guarded encoder and optional bounded model enumeration.
- `bv-*.json` and matching progress logs: all five unaltered search results.
- `verify_outputs.py`: independent standard-library replay of saved SAT
  points, complete root domains, finite-field irreducibility, and digit folds.
- `verification.json` and `verification-optimized.json`: matching normal
  and Python `-O` verification results.
- `RUN_RECEIPTS.json`: exact commands and performance/status summary.

The replacement fixes the unbounded integer-LP failure mode and gives a
mathematically complete finite-domain encoding with explicit extension-field
coverage. It does **not** yet make the collective search tractable. The safe
240-mask reduction is available for further mathematical compression, but
the present timeout receipts cannot justify any additional exclusion.
