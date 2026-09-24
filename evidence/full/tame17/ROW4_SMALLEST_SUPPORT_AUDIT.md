# Independent audit of the row-4 smallest-support exclusion

23 September 2026. **PASS within the stated scope:** in the established
characteristic-17 row-4 normalization, the exact deficiency support
`{2,4,10,12,18,19}` is excluded. This is the canonical active middle support
`{4,10,12}`. The audit does not exclude the remaining row-4 supports, prove
unrestricted degree 20, establish novelty, or constitute external peer review
or proof-assistant certification.

The audited proof is `ROW4_SMALLEST_SUPPORT_EXCLUSION.md`. Its producer inputs
are `row4_first_obstruction.py`, `row4-first-obstruction.json`,
`lift_row4_smallest_support.py`, and `row4-smallest-support-lift.json`.
The broader `ROW4_QUADRATIC_LIFTING.md` and `ROW4_QUADRATIC_AUDIT.md` were also
read to check the normalization and local analytic assertions. The present
exclusion does not need their signed quadratic charts once its residue census
has finished.

## Independent computation

`check_row4_smallest_support.py` uses only Python's standard library. It neither
imports the producer modules nor uses FLINT. Its arithmetic routines implement
the quartic field and the quadratic coefficient ring directly; its checks use
explicit exceptions and therefore remain active under optimized Python.

The checker independently performs the following operations before comparing
against the producer receipts:

1. Verifies irreducibility of `T^4+3T^3+4T^2+2` by the degree-four Frobenius
   criterion, then evaluates the residue polynomial on all `17^4=83,521`
   field elements. It finds 18 distinct roots, doubles exactly the two roots
   of `T^2+3T+3`, and multiplies all 20 linear factors to recover the entire
   degree-20 polynomial. This product identity proves completeness over the
   algebraic closure, not merely the absence of further roots in the chosen
   finite field.
2. Reconstructs the exact ordinary polynomial from the binomial-normalized
   coefficients, eliminating `a18` using the normalized second derivative
   and the linear coefficient using `f(1)=0`. At `s=6`, it checks the required
   coefficientwise divisibility for the constant direction and every middle
   coefficient direction `a4,...,a16`, including the derivative at the
   quadratic root. It derives the affine divided critical value.
3. Exhausts all `17^3=4,913` nonzero-root witness triples and checks each of
   the two critical-root orientations separately: 9,826 oriented markings.
   It retains zero residues of active coefficients. Precisely two markings
   survive, both with witnesses `(10,1,6)` and coefficients `(1,4,9)`.
4. Reconstructs the exact surviving two-variable system by the triangular
   normalized derivative equations. It computes the Jacobian through an
   exact finite-difference congruence, rather than supplying the producer's
   Jacobian, and solves the two Newton corrections generically.
5. Lifts the critical root in both quadratic orientations, computing the
   inverse of the critical derivative in the quadratic field. It verifies
   the nonzero critical values and their norms independently.

Normal and optimized replay commands are:

```sh
python3 work/casas-alvero-full/tame17/check_row4_smallest_support.py
python3 -O work/casas-alvero-full/tame17/check_row4_smallest_support.py
```

Their saved receipts are `row4-smallest-support-audit-verification.json` and
`row4-smallest-support-audit-verification-optimized.json`. They both report
`PASS`, agree byte for byte, and fingerprint the producer files and final proof.
No optional quadratic first-jet filter is invoked or required by this checker.

## Division by 17 is valid before ramified evaluation

The significant issue is not just whether a single numerical critical value
is divisible by 17. That would not justify division in a coefficient chart
whose varying coefficients can have fractional positive valuation.

Here `F(u,6;X)=f0(X)+sum u_j f_j(X)` is affine in all middle coefficients.
The checker verifies that every `f_i(6)`, both coordinates of `f_i(alpha)`,
and both coordinates of `f_i'(alpha)` are divisible by 17 in the integer
quadratic ring, where `alpha^2+3alpha+3=0`. Thus the divisibility is
coefficientwise. The phrase "over the integers" in the proof means the
integer ring of this quadratic extension, not an element of ordinary `Z`.

The total `s` derivative of `F(u,s;s)` is 9 modulo 17. The implicit solution
therefore satisfies `S(u)-6` coefficientwise divisible by 17, with

`(S(u)-6)/17 = -[F(u,6;6)/17]/9 (mod 17)`.

Likewise `F_X(u,S(u);alpha)` is coefficientwise divisible by 17 and the
ordinary second derivative at the residue critical root is 6. The lifted
critical root differs from alpha by a coefficientwise multiple of 17.
Moving the critical root changes the value only by a coefficientwise
multiple of `17^2`: its linear term is a product of two multiples of 17,
and its quadratic and higher terms have the same or higher divisibility.
These observations justify the integral analytic quotient and its reduction
before any substitution of ramified coefficient values.

The recomputed active affine equation is

`ell_alpha=(10+14alpha)+(16+15alpha)u4+10alpha*u10+(16+15alpha)u12`.

For the second orientation one substitutes the conjugate of alpha in this
equation while keeping the independently varying `u_j` unchanged. The checker
does exactly this; it does not incorrectly conjugate the whole marking.

## Why the residue census is exhaustive

The exact active coefficients need not be units. Their witnesses cannot,
however, reduce to zero: zero is already an exact simple root and is the
unique root in its residue class. A witness equal to zero forces its exact
normalized coefficient to vanish, contrary to the active-support assumption.
Consequently all active witnesses lie in the 17 nonzero residue classes
enumerated by the checker. The normalized derivative equations recursively
determine their residue coefficients in the same splitting field. There are
no additional choices over a larger algebraic residue extension.

Both surviving markings select simple residue roots. In particular, the
witness reducing to 1 equals the fixed exact root 1, and the witness reducing
to 6 equals the already selected exact second-derivative witness `s`. Writing
the witness near 10 as `t` therefore gives the exact triangular formulas in
the proof. No assumption that two roots in a double residue class coincide
enters this step.

## Why the two-variable lift exhausts arbitrary ramification

The recomputed Jacobian of `(f(t),f(s))` at `(10,6)` is

`[[2,12],[0,9]] (mod 17)`,

whose determinant is 1 modulo 17. Hensel lifting supplies an unramified
solution of this square subsystem. This does not assume that the roots of
the original polynomial lie in an unramified extension.

Indeed, let an actual solution in any valued extension differ from an
approximate solution by a vector of minimum valuation `gamma>0`, with
`v(17)=1`. An integral matrix with integral inverse preserves this minimum
valuation. The linear Taylor term thus has minimum valuation gamma, while
all nonlinear terms have valuation at least `2 gamma`. If the approximate
residual has valuation at least `n` and `gamma<n`, the linear term cannot
cancel. Hence every actual solution agrees with the approximate one to
valuation at least `n`. This proves precisely the finite-precision uniqueness
needed by the obstruction, for arbitrary rational or real positive gamma.

The critical equation has unit ordinary second derivative 6 at either
quadratic residue root. The same argument applies to its lift after the
square subsystem is fixed. Thus a ramified candidate cannot evade the
calculated critical value by selecting a different critical point in that
residue class.

## Replayed obstruction and conclusion

The independent lift gives `(t,s)=(95,91)` modulo `17^2`, followed by
`(2696,1536)` modulo `17^3`. The latter normalized active coefficients are
`(a4,a10,a12)=(1531,2792,2610)`.

In the quadratic ring modulo `17^3`, the critical point in the alpha
orientation is `2788+3707alpha`. Its derivative value is zero, whereas

`f(2788+3707alpha)=17^2(9+4alpha) (mod 17^3)`.

The norm of `9+4alpha` is `81-108+48=21`, hence 4 modulo 17. The conjugate
orientation gives the divided value `14+13alpha`, also with norm 4. Neither
critical point can be an exact root of f. This contradicts the necessary
first-derivative common-root condition for every surviving marking.

The exclusion of this one exact support therefore passes both the independent
arithmetic replay and the mathematical exhaustiveness audit. No remaining
gap was found within this scope.
