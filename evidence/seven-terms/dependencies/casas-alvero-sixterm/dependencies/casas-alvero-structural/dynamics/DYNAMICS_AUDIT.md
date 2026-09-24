# Audit of the fixed-degree Frobenius obstruction

Status: the proposed elimination gives a valid finite exceptional-prime
obstruction. This is a theorem about a specific sparse family in positive
characteristic. It is not a proof of the Casas–Alvero conjecture, and a prime
in the exceptional set is only a possible exception, not a constructed
counterexample.

## Precise statement

Let `H,C in Z[z]` be the explicitly defined polynomials below, and put

\[
\mathcal R=\operatorname{Res}_z(H,C),\qquad
K=51^7-17^2 35^7=-17696646119024.
\]

Then `R != 0`. Let `p>7` be a prime other than 17, and let `k` be an
algebraically closed field of characteristic `p`. If

\[
h(X)=X^{p+7}+aX^{p+3}+cX^3+dX
\]

has a common root with each of its Hasse derivatives of orders
`1,...,p+6`, then either `h=X^(p+7)` or `p` divides `K R`.
If `a != 0`, the sharper necessary condition is `p | R`.

More practically, for any such prime, if the reductions of `H` and `C`
have gcd 1, the entire chart `a != 0` is excluded. This test has fixed
degrees 72 and 432 independent of `p`. If also `K != 0 mod p`, all
coefficient charts except the pure power are excluded.

Only the common-root conditions for Hasse orders `p+3,3,1` are used.
Therefore the conclusion also holds for polynomials satisfying just those
three conditions. Necessity, rather than equivalence to the full CA
system, is all that is needed.

## 1. Normalization and the rational map

Assume first `a != 0`. The Hasse derivative of order `p+3` is
`35X^4+a`, by Lucas's formula, or directly by comparing the base-`p`
digits of `p+7,p+3`. A common root is nonzero, so scaling it to 1
normalizes `a=-35`. Because `h(1)=0`,

\[
c+d=34.
\]

The Hasse derivative of order 3 is

\[
35X^{p+4}-35X^p+c.
\]

If `c != 0`, its common root `v` with `h` is nonzero. If `c=0`, we
may choose `v=1`, since both polynomials vanish there. In either case,

\[
c=35v^p(1-v^4),\quad d=34v^{p+6},\quad
v^p[34v^6+35(1-v^4)]=34.                 \tag{1}
\]

In particular `d != 0` because `p != 2,17`. Thus the first-derivative
common root `w` is also nonzero. Write

\[
P(X)=h(X)/X=X^{p+6}-35X^{p+2}+cX^2+d.
\]

The identity `3P(w)-h'(w)=0` yields

\[
w^{p+6}=17v^{p+6}.
\]

Set `t=w/v`. Then

\[
t^p=17/t^6.                                            \tag{2}
\]

Substituting (1) into `P(w)=0` gives

\[
(51-35t^2)v^4=35(17-t^6)/t^4.                          \tag{3}
\]

The denominator `51-35t^2` cannot vanish. If it did, (3) would give
`t^6=17`, and (2) would give `t^p=1`. Frobenius is injective in a
field, so `t=1`; this contradicts `51-35t^2=16 != 0`. In particular
there is no omitted denominator-zero chart and no additional prime
exception from solving (3).

Let

\[
z=t^2,\qquad \psi(z)=\frac{17^2}{z^6},\qquad
T(z)=\frac{35(17-z^3)}{z^2(51-35z)}.
\]

Then `z != 0`, `z^p=psi(z)`, and `T(z)=v^4`. Frobenius preserves
the nonvanishing of every denominator at successive orbit points,
because all coefficients of these rational functions lie in `F_p`.

## 2. A fixed polynomial vanishing along the Frobenius orbit

Put `y=v^2`, so `y^2=T`, and define

\[
A=34T,\quad B=35(1-T),\quad U=T(\psi(z)),
\]
\[
E=A^4T^2+6A^2B^2T+B^4,\qquad
O=4AB(A^2T+B^2).
\]

Equation (1), raised to the fourth power, becomes

\[
U(Ay+B)^4=34^4.
\]

Reducing the fourth power modulo `y^2=T` gives `(Ay+B)^4=E+Oy`.
Consequently

\[
(UE-34^4)^2-T(UO)^2=0.                                \tag{4}
\]

This norm step may introduce extra roots, which is harmless because
only a necessary equation is claimed. It divides by neither `c` nor
`1-T` and therefore remains valid when `c=0`.

Here is a definition of `H` entirely in integer polynomial arithmetic.
Set

\[
P=35(17-z^3),\quad Q=z^2(51-35z),
\]
\[
R=35(z^{18}-17^5),\quad
S=17^3(51z^6-35\cdot17^2)=17^4(3z^6-595),
\]

so that `T=P/Q` and `U=R/S`. The letters `P,R` in this displayed
construction denote polynomials in `z`, not the earlier polynomial
`h(X)/X` or the resultant `mathcal R`. Define

\[
A_0=34P,\quad B_0=35(Q-P),
\]
\[
E_0=A_0^4P^2+6A_0^2B_0^2PQ+B_0^4Q^2,
\quad O_0=4A_0B_0(A_0^2P+B_0^2Q),
\]
\[
N=(R E_0-34^4S Q^6)^2-PQ R^2O_0^2,\qquad H=N/17^8.
\]

Exact integer expansion independently verifies that `N` has content
exactly `17^8`, and `H` has degree 72 and integral primitive
coefficients. The rational expression on the left side of (4) is
exactly

\[
\frac{H(z)}{z^{24}(35z-51)^{12}(3z^6-595)^2}.           \tag{5}
\]

At a valid point the first two denominator factors are already
nonzero. The last is nonzero because

\[
51-35\psi(z)=\frac{17(3z^6-595)}{z^6}
\]

is the Frobenius image of the nonzero element `51-35z`. Hence (4)
implies `H(z)=0` in every characteristic under consideration. The
primitive-content division introduces no exception besides 17,
which was excluded at the outset.

Since `H` has integer coefficients, `H(z^p)=H(z)^p=0`. Using
`z^p=psi(z)`, the same point is a root of

\[
C(z)=z^{432}H(17^2/z^6)\in\mathbb Z[z].                \tag{6}
\]

This one Frobenius step suffices; there is no need to assert
irreducibility, squarefreeness, or eventual stabilization of an
iterated gcd sequence.

## 3. Why only finitely many primes can survive

The standard-library checker reconstructs the integer polynomial `H`
from the displayed definition and checks an explicit identity

\[
U_{11}(z)H(z)+V_{11}(z)C(z)=1\quad\text{in }\mathbb F_{11}[z].
\]

The full coefficient lists for `U_11,V_11` are saved in
`bezout-mod11.json`; their degrees are 431 and 71. It additionally
checks that neither degree 72 nor degree 432 drops modulo 11.
Therefore the fixed-degree Sylvester determinant `mathcal R` is
nonzero modulo 11 and, in particular, is a nonzero integer.

If a valid characteristic-`p` point existed, its common zero of
`H mod p` and `C mod p` would force `mathcal R=0 mod p`. This
implication is valid even when a leading coefficient vanishes modulo
`p`: evaluation at the common finite root makes the fixed-degree
Sylvester linear map singular. Thus no separate leading-coefficient
exception needs to be added to the prime divisors of `mathcal R`.

Equivalently, the integral resultant identity places `mathcal R` in
the ideal `(H,C)`, so evaluating at a common root forces its
reduction to vanish. The explicit 26,185-digit resultant computed
by the parent is optional evidence; the theorem needs only its
defining determinant and the independent mod-11 certificate.

## 4. Remaining coefficient charts

Suppose `a=0,c != 0`. Normalize a common root of the Hasse derivative
of order 3 to 1. Then `c=-35`, and the root condition gives `d=34`.
A common root `w` with the first derivative is nonzero. Its two
equations are

\[
w^{p+6}-35w^2+34=0,\qquad
7w^{p+6}-105w^2+34=0.
\]

Subtracting seven times the first equation from the second yields
`w^2=51/35`, and substitution gives `w^(p+6)=17`. Set `b=51/35`,
which belongs to the prime field. Squaring the last equation gives
`b^(p+6)=17^2`; since `b^p=b`, this is `b^7=17^2`. Therefore

\[
p\mid K=51^7-17^2 35^7.
\]

For reference, exact factorization gives

\[
K=-2^4\cdot17^2\cdot1229\cdot3114019.
\]

Only the nonvanishing of this displayed integer is required by the
theorem. This necessary condition is not asserted to be sufficient.

If `a=c=0,d != 0`, a nonzero common root of `X^(p+7)+dX` and its
first derivative would give simultaneously `w^(p+6)=-d` and
`7w^(p+6)=-d`, implying `6d=0`, impossible for `p>7`. If also
`d=0`, the polynomial is the pure power, as stated.

## 5. Verification and interpretation

`check_fixed_dynamics.py` uses only Python standard-library integer
arithmetic. It reconstructs the norm numerator, checks its exact
content, compares all 73 coefficients of `H` to the parent's file,
forms (6), computes the mod-11 extended Euclidean algorithm, and
independently multiplies the resulting Bezout polynomials to verify
the identity. The checks use explicit exceptions and remain active
under `python -O`.

The modular gcd degrees independently found are:

| Prime | deg H | deg C | gcd degree |
|---:|---:|---:|---:|
| 11 | 72 | 432 | 0 |
| 13 | 72 | 432 | 0 |
| 19 | 72 | 432 | 4 |
| 23 | 72 | 432 | 4 |
| 29 | 72 | 432 | 0 |
| 31 | 72 | 432 | 0 |

The nonzero gcds at 19 and 23 are consistent with supplied examples;
they do not independently prove that examples exist. Conversely,
the gcd-one entries exclude the sparse chart without any search
over extension fields or finite-field point enumeration.

This is a uniform finite exceptional-prime result for a family whose
degree varies with `p`. It supplies a reusable necessary-condition
mechanism and a fixed-size per-prime test. Its novelty and importance
must still be assessed against prior work, separately from this
validity audit. It does not classify the finite exceptional set or
prove the full conjecture in any previously open degree by itself.

## 6. Audit of the integrated characteristic-zero consequence

The 23 September integrated `../PROOF.md`, Sections 1–5, passes this
independent audit. In particular, with `q=p^e`, the visible deficiencies
in degree `(p+7)q`, apart from the leading and constant terms, are

\[
q\{1,2,3,4,5,6,7,p,p+1,p+2,p+3,p+4,p+5,p+6\}.
\]

Deleting
`q J_p`, where `J_p={1,2,3,5,6,7,p,p+1,p+2,p+3,p+5}`,
leaves exactly `q{4,p+4,p+6}`. Those deficiencies reduce to the
three displayed nonleading monomials after substituting `X^q`.

For clarity, the normalized-derivative induction used in the transfer
has the explicit form

\[
\frac{H_{n-j}f}{\binom nj}
=X^j+\sum_{i=1}^{j}\binom ji a_iX^{j-i},
\qquad
f=\sum_{i=0}^{n}\binom ni a_iX^{n-i},\quad a_0=1.
\]

At a common integral root this monic equation expresses `a_j` as a
sum of integral elements involving earlier `a_i`. It proves the
integrality needed before reduction, rather than assuming that
ordinary integral polynomial coefficients are enough. Translating
any selected root to zero and scaling a nonzero root of minimum
valuation to 1 preserves every exact coefficient vanishing, all
common-root conditions, and nontriviality on reduction. Reduction
then commutes with every Hasse derivative `H_(qk)` as stated. The
argument applies to every chosen root and every `e>=0`.

For `e=0`, the invisible ordinary monomials have exponents
`8,...,p-1`, precisely `X^8 Q_0(X)` with `deg Q_0<=p-9`.
Their number is `p-8`, giving the stated maximum of `p-4` terms
after the other four monomials are included. This is an exclusion
of that particular ambient family, not a universal term bound.

The accompanying boundary note `../uniform/STRUCTURAL_BOUNDARIES.md`
also passes a written check: the coprime-exponent arguments place
the relevant boundary witnesses in the prime field, and the
compatibility equations are sufficient as well as necessary.
Running its standard-library checker confirms the integer factors,
primality checks, and displayed witnesses, including the fully
nonzero example at 19. This verifies the boundary statements used
in Section 6 of the integrated proof. The six-term enumeration in
that section is a separate result; its saved receipt lists four
survivors, but this dynamics audit did not rederive its prior-art
input criteria.
