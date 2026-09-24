# Exact characteristic-17 branches compared with the 2-adic restrictions

This note keeps all degree-20 coefficients. It excludes one scale/type
subcase of row 9 and proves exact conditional valuation restrictions for
rows 4, 6 and 7. No complete characteristic-17 row is excluded.

The input is `../LIFT_CONSEQUENCES_17.md`; row numbers refer to the complete
classification in `../support_frontier/prime17/CLASSIFICATION.md`.

## 1. Transporting the exact normalization to the prime 2

Write the characteristic-zero polynomial in its characteristic-17-derived
normalization as

\[
 f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
 \qquad a_0=1,\quad a_1=a_{20}=0.
\]

Its distinguished exact root is 1. At the prime 2 choose a nonzero root
`r` of minimum valuation and put

\[
 F(X)=r^{-20}f(rX),\qquad b_j=a_j/r^j,\qquad t=1/r.
\]

All roots and all normalized coefficients of `F` are integral. The
distinguished root is now `t`, with `λ=ν(t)≥0`; **λ need not be zero**.
To make the active degree-4 or degree-16 normalized derivative witness
exactly 1, a subsequent unit scaling replaces `r` by `rs`, `b_j` by
`b_j/s^j`, and `t` by `t/s`, with `s` a unit. It preserves λ and all the
weighted identities below. Absorb `s` into `r` from now on, so
`b_j=a_j/r^j` and `t=1/r` still hold literally.

| Rows | Exact identities after the 2-adic normalization |
|---|---|
| 4 | `b_2=-t^2`, `b_3=b_17=0`, and `t` is simple |
| 6,7 | `b_2=-t^2`, `b_3=2t^3`, `b_17=0`, and `t` is simple |
| 9 | `b_2=b_17=0`, `b_3=-t^3`, and `t` has multiplicity exactly three |

The distinguished roots in rows 4,6,7 are simple because their seed
derivatives at 1 are respectively 13,11,14 in `F_17`. Row 9 has multiplicity
exactly three because its residue multiplicity is three. The exact mean
root 0 is simple in every nontrivial degree-20 counterexample by the
separate prime-19 argument in the input.

In rows 6,7 the identities give

\[
 G_2=(X-t)(X+t),\qquad G_3=(X-t)^2(X+2t).
\]

In row 4, `G_3=X(X^2-3t^2)`; in row 9, `G_3=X^3-t^3`.

## 2. The two types and their scale bounds

The active-witness normalization of
`../two_adic/REDUCTION_AND_LIFTING.md` gives

\[
 A:\quad F\equiv X^{20}-X^{16}\pmod{2O[X]},\quad G_4(1)=0;
\]
\[
 B:\quad F\equiv X^{20}-X^4\pmod{2O[X]},\quad G_{16}(1)=0.
\]

The root-cluster multiplicities at `(0,1)` are `(16,4)` in A and `(4,16)`
in B. The proved valuation bounds, valid with arbitrary ramification, are

| Type and root residue | Bound |
|---|---|
| A, `z̄=0`, `z≠0` | `ν(z)≥1/14` |
| A, `z̄=1` | `ν(z−1)≥1/2` |
| B, `z̄=0`, `z≠0` | `ν(z)≥1/2` |
| B, `z̄=1` | `ν(z−1)≥1/14` |

They apply to `t` without assuming the original distinguished root remains
a unit under the first, possibly nonunit, scaling.

## 3. Row 9 cannot have type B and ν(t)>0

Suppose otherwise. The zero cluster contains exactly four roots counting
multiplicity, already exhausted by the simple root 0 and triple root `t`.
Thus

\[
 F=X(X-t)^3V,
\]

where `V` is monic of degree 16, all its roots are units, and its
coefficients are integral. Write `V=V_0+V_1X+V_2X^2+...`; then `V_0` is
a unit. The exact vanishing `b_17=0` gives

\[
 0=[X^3]F=-3tV_0+3t^2V_1-t^3V_2.
\]

After dividing by nonzero `t`, the term `-3V_0` is a unit and the other
terms lie in the maximal ideal. This is impossible at the prime 2.
Therefore **row 9 and type B force ν(t)=0**.

Equivalently, in this case the original characteristic-17 normalization
already has all roots and all normalized coefficients integral at 2:
`ν(t)=0` makes the total factor `r` a 2-adic unit.

This excludes the entire indicated scale/type subcase, including invisible
coefficients and ramified displacements. It does not exclude row 9, which
still has both A scale possibilities and the B unit possibility.

More generally, an isolated cluster consisting of simple 0 and an exact
root `t` of multiplicity `m` cannot have `ν(t)>0` and `[X^m]F=0` when the
residue characteristic does not divide `m`: in `F=X(X-t)^mV`, that
coefficient divided by `t` is `-mV_0` plus terms in the maximal ideal.

## 4. Rows 4,6,7: an exact conditional valuation relation

Suppose one of these rows has type B, `λ=ν(t)>0`, and a first-derivative
common root `u` lies in the zero cluster. Both 0 and `t` are simple, so `u`
is distinct from them. Cluster capacity makes `u` exactly double and gives

\[
 F=X(X-t)(X-u)^2V,\qquad \deg V=16,
\]

where all roots of `V` are units. Put `μ=ν(u)≥1/2`. We prove

\[
 \boxed{\lambda=\mu+1,\qquad\mu>1/2,\qquad\lambda>3/2.}       \tag{1}
\]

Since `V̄=(X-1)^16=X^16+1`, its constant `V_0` is a unit and `ν(V_1)>0`.
Expanding the exact condition `[X^3]F=0` gives

\[
 0=-(t+2u)V_0+(u^2+2tu)V_1-tu^2V_2,
\]

equivalently

\[
 t(V_0-2uV_1+u^2V_2)=u(-2V_0+uV_1).                         \tag{2}
\]

The factor multiplying `t` is a unit. Thus, initially,

\[
 \lambda\ge\mu+\min\{1,\mu+\nu(V_1)\}>1.
\]

This includes `V_1=0`, interpreted with infinite valuation. The monic
quartic

\[
 U=X^4-(t+2u)X^3+(u^2+2tu)X^2-tu^2X
\]

therefore satisfies `U≡X^4 mod 2O[X]`. Combining `F=UV` with the type-B
congruence gives

\[
 X^4V\equiv X^4(X^{16}-1)\pmod{2O[X]},\qquad
 V\equiv X^{16}-1\pmod{2O[X]}.
\]

Cancellation of the monomial is coefficient shifting and is valid even
though `O/2O` need not be a domain. Now `ν(V_1)≥1`, so the terms in
`-2V_0+uV_1` have different valuations: 1 and at least `μ+1>1`.
Equation (2) gives the exact equality `λ=μ+1`.

Because `b_2=-t^2` has positive valuation, the type-B reduction of `G_18` is

\[
 \bar G_{18}=X^{18}+X^2+\bar b_{18}.
\]

Its common root reduces to 0 or 1, and evaluation at either is `b̄_18`.
Therefore `ν(b_18)>0`. On the other hand,

\[
 190b_{18}=[X^2]F=(u^2+2tu)V_0-tu^2V_1.
\]

The term `u^2V_0` has valuation `2μ`, strictly below the others, since
`λ=μ+1` and `ν(V_1)≥1`. Hence

\[
 \nu(b_{18})=2\mu-1>0,
\]

which proves (1). The same factorization gives

\[
 \nu(b_2)=2\mu+2,\qquad
 \nu(b_{18})=2\mu-1,\qquad
 \nu(b_{19})=3\mu-1,                                      \tag{3}
\]

using `20b_19=-tu^2V_0`. In rows 6,7 also `ν(b_3)=3μ+4`; in row 4,
`b_3=0` exactly.

The Hasse-order-two witness must be in the unit cluster. Otherwise the
zero cluster would contain witnesses for orders 1,2,3, with the last
provided by the exact mean root. The size-4 cluster-collapse lemma would
make the mean root multiple. In particular, **if 0<ν(t)≤3/2, every
first-derivative common root must lie in the unit cluster**.

The degree-4 normalized derivative witness lies in the zero cluster, so
it is one of `0,t,u`. Its equation consequently restricts `b_4` to

\[
 \begin{cases}
 \{0,\;5t^4,\;-u^4+6t^2u^2\},&\text{row 4},\\
 \{0,\;-3t^4,\;-u^4+6t^2u^2-8t^3u\},&\text{rows 6,7}.
 \end{cases}
\]

The corresponding valuations are infinite, `4μ+4`, and `4μ`. These are
conditional necessary restrictions, not constructions of a CA polynomial.

In the original characteristic-17 normalization, where the distinguished
root is exactly 1, the repeated root is `u_original=r u`. Since
`ν(r)=-λ`, (1) gives the particularly simple invariant conclusion

\[
 \boxed{\nu_2(u_{\rm original})=-1.}
\]

Transporting (3) and the three degree-4 possibilities back by
`a_j=r^j b_j` gives

\[
 \nu_2(a_4)\in\{\infty,0,-4\},\qquad
 \nu_2(a_{18})=-16\lambda-3,\qquad
 \nu_2(a_{19})=-16\lambda-4.
\]

In particular `ν_2(a_19/a_18)=-1`; the two coefficients are nonzero.
These values refer to the original exact normalization, so they do not
hide a unit-scaling assumption. In the middle degree-4 possibility the
coefficient is exactly `a_4=5` in row 4 or `a_4=-3` in rows 6,7.

## 5. Exact finite residue intersection

Put `ε=t̄`, equal to 0 for `λ>0` and 1 for `λ=0`. The exact
characteristic-17 constraints prescribe normalized witness residues:

| Rows | Prescribed residues |
|---|---|
| 4 | `w̄_2=ε`, `w̄_3=w̄_17=0` |
| 6,7 | `w̄_2=w̄_3=ε`, `w̄_17=0` |
| 9 | `w̄_2=w̄_17=0`, `w̄_3=w̄_18=w̄_19=ε` |

Apply the proved first-saturation cuts and simple-mean zero-cluster
occupancy restriction. Reconstructing all witness assignments gives:

| Rows | Type | ε | Coefficient patterns | Marked assignments |
|---|---|---:|---:|---:|
| 4 or 6,7 | A | 0 | 50 | 4,095 |
| 4 or 6,7 | A | 1 | 58 | 6,143 |
| 4 or 6,7 | B | 0 | 145 | 4,608 |
| 4 or 6,7 | B | 1 | 97 | 3,584 |
| 9 | A | 0 | 22 | 1,535 |
| 9 | A | 1 | 24 | 512 |
| 9 | B | 0 | 0 | 0 |
| 9 | B | 1 | 161 | 1,536 |

The equal counts for rows 4 and 6,7 do not identify their exact families:
their `b_3` values differ, but reduction does not distinguish 0 from
`2t^3`. Fixing their different degree-3 witness labels happens to give
the same counts. Every nonempty case has a sample necessary residue
assignment in the receipt. These are points of the finite necessary
system, **not** characteristic-zero lifts. The valuation conditions in §4
are additional information; these counts do not enumerate their valued
solutions.

## Replay and boundary

`check_cross_prime.py` reconstructs the normalized derivative
factorizations, expands the local coefficient identities over `Z`, checks
the exact valuation gaps in (3), verifies simplicity of the three
characteristic-17 distinguished roots, and independently enumerates the
residue intersections.

```sh
python3 check_cross_prime.py
python3 -O check_cross_prime.py
```

The receipts `cross-prime-replay.json` and
`cross-prime-replay-optimized.json` pass and are byte-identical.
The substantive results are §§3–4. No complete characteristic-17 row is
excluded, and no surviving row is asserted to lift. Degree 20 remains open
within this investigation.
