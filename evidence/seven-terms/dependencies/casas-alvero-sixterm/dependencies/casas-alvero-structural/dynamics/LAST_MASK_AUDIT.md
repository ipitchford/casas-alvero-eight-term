# Independent audit of the last characteristic-13 support mask

23 September 2026. Internal mathematical audit; no novelty or publication
claim. **Result: the proposed exclusion is valid**, including every
coefficient-zero chart. It excludes the previously surviving centered
degree-20 six-term support `{8,10,16,17,19}` (deficiency indexing), leaving
three supports from the preceding four-support list. The remaining three
are not excluded by this result.

## Seed statement

Over an algebraic closure of `F_13`, the only CA polynomial of the form

\[
h(X)=X^{20}+aX^4+cX^3+dX
\]

is `X^20`. CA here uses all Hasse derivative orders 1 through 19.
The only orders not automatically witnessed at zero are 4, 3, and 1,
and their Hasse derivatives are

\[
H_4h=9X^{16}+a,\quad H_3h=9X^{17}+4aX+c,
\quad H_1h=7X^{19}+4aX^3+3cX^2+d.
\]

All computations below are in characteristic 13.

## All coefficient-zero cases

If `a=c=0,d!=0`, a common nonzero root with `H_1` would imply both
`w^19=-d` and `7w^19=-d`, impossible. If all three vanish, the
polynomial is the pure power.

If `a=0,c!=0`, normalize a nonzero common root with `H_3` to 1.
Then `c=4,d=8`. For a common root `w` with `H_1`, the root and
derivative equations imply `w^2=10` and `w^19=4`. But
`w^18=10^9=-1`, so `w=-4=9`, contradicting `9^2=3!=10`.

Suppose now `a!=0`. Normalize a nonzero common root with `H_4`
to 1; this gives `a=4` and `c+d=8`. If `c=0`, then `d=8`.
The equations for a common root `w` with `H_1` give
`w^3=9,w^19=8`. Hence `w^18=9^6=1`, so `w=8`, whereas
`8^3=5!=9`. Thus `c!=0`.

Choose a common root `v` with `H_3`; because its constant term is
`c!=0`, this root is nonzero. Put `T=v^16`. Then

\[
c=v(4T-3),\qquad d=-v^3(5T+1),
\]
\[
(5T+1)v^3+(3-4T)v-5=0.                              \tag{1}
\]

If `d=0`, then `T=5`, while `c=8` gives `v=2` from the first
equation. But `2^16=3!=5`. Therefore `d!=0` and
`5T+1!=0`. This explicitly justifies the factor removal in the
producer; it is not an assumption that coefficients survive reduction.

## Ratio equations and the second denominator

Let `w` be a common root with `H_1`. Since `d!=0`, `w!=0`.
Define `t=w/v`. Dividing `h(w)=0` by `v^3 w` yields

\[
T(t^{19}+4t^2-5)+4t^3-3t^2-1=0.                     \tag{2}
\]

Subtracting seven times `h(w)/w` from `H_1h(w)` gives

\[
(10t^2+4)T=-t^3+t^2-6.                              \tag{3}
\]

Set `D=10t^2+4`, `E=-t^3+t^2-6`. The two roots of `D` in the
algebraic closure are 6 and 7, where `E` is respectively 9 and 12.
Thus (3) implies `D!=0`. There is no excluded denominator-zero
chart. Substituting `T=E/D` into (2) gives the necessary degree-22
polynomial

\[
U(t)=E(t^{19}+4t^2-5)+D(4t^3-3t^2-1)=0.             \tag{4}
\]

## Independent elimination and exact unit certificate

The equation (1), together with `v^16=T`, implies

\[
R(T)=\operatorname{Res}_v\big((5T+1)v^3+(3-4T)v-5,
                             v^{16}-T\big)=0.       \tag{5}
\]

I computed this full cubic/degree-16 resultant independently using
SymPy. Its reduction modulo 13 has degree 19 and matches every
coefficient of the producer's saved `R`. This calculation differs
from the producer's pseudo-reduction and 5-by-5 determinant. It
also bypasses reliance on dividing the latter determinant by
`(5T+1)^34`, although that division is justified above.

Write `R(T)=sum r_i T^i`, and define

\[
F(t)=\sum_{i=0}^{19}r_i E(t)^iD(t)^{19-i}.
\]

At a solution, `F(t)=D(t)^19 R(E(t)/D(t))=0`. The independently
computed remainder `H=F mod U` agrees with the saved degree-21
polynomial. The saved certificate consists of two polynomials
`B_U,B_H` of degrees 20 and 21 satisfying

\[
B_U(t)U(t)+B_H(t)H(t)=1\quad\text{in }\mathbb F_{13}[t].
\]

Direct multiplication independently verifies this exact identity.
Therefore no algebraic extension of `F_13` contains a common root
of the necessary equations, and the final nonzero chart is empty.
The stored coefficient arrays have lengths 21 and 22, totaling
43 coefficients; describing this as a “42-entry certificate” is
an inessential count error.

## Characteristic-zero support consequence

For degree 20, Lucas's theorem in characteristic 13 says that the
nonleading nonconstant visible deficiencies are
`{1,...,7,13,...,19}`. On the support `{8,10,16,17,19}`, the
deficiencies 8 and 10 disappear after the established integral
binomial-normalized valuation reduction. The other three yield
the exponents 4, 3, and 1. A root scaled to 1 survives, so reduction
cannot be the monomial. The seed theorem contradicts this.

This consequence uses the already audited minimum-valuation
normalization and normalized-derivative integrality argument. No
claim is made that an arbitrary integral polynomial has the same
coefficient-vanishing property without that CA integrality argument.

## Reproduction

`check_last_mask_independent.py` independently reconstructs the direct
resultant (5), equation (4), the homogenized substitution remainder,
and the Bezout multiplication, and checks the constants in every
zero chart. Its explicit checks remain active under `python -O`.
The producer's input is `../sixterm/last-mask-probe.json`.

No new proof gap was found. This audit establishes the additional
mask exclusion and supports changing the surviving six-term count
from four to three; it does not solve any of those three cases.
