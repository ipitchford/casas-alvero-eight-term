# Degree 20 at 19: a universal cluster bound and first-jet obstruction

Status: a proved necessary-condition refinement, not an exclusion of degree 20.
All valuations below allow arbitrary ramification. Normalize `v(19)=1`.

## Hypotheses and notation

Let a nontrivial characteristic-zero Casas–Alvero polynomial of degree 20 be
centered, monic, and scaled using a repeated root so that

\[
 f(X)=\sum_{i=0}^{20}\binom{20}{i}a_iX^{20-i},\qquad
 a_0=1,\quad a_1=a_{20}=0,\quad f(1)=f'(1)=0.
\]

Use the usual 19-adic normalization in which the coefficients `a_i` are integral
and `f mod 19 = X^20-X = X(X-1)^19`. Thus 0 is an exact simple root and the other
19 roots reduce to 1. The normalized derivatives are

\[
 G_j(X)=\frac{H_{20-j}f(X)}{\binom{20}{j}}
       =\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]

Put `b_j=G_j(1)`. In particular `b_0=b_1=1` and `b_19=b_20=0`.
The exact divided identity is

\[
 F(a):=\sum_{i=2}^{19}c_i a_i=0,\qquad
 c_i=\frac1{19}\binom{19}{i-1}\in\mathbb Z.
\tag{1}
\]

Indeed, `f(1)-G_19(1)=sum binom(19,i-1)a_i`; divide by 19.
Modulo 19, `c_i=(-1)^i/(i-1)` for `2<=i<=19`.

## 1. Every nonzero displacement has valuation at least 1/17

Taylor expansion gives

\[
 f(1+Y)=\sum_{k=0}^{20}\binom{20}{k}b_{20-k}Y^k.
\]

Let `q(Y)=f(1+Y)/(1+Y)`. This is monic of degree 19 and its roots are exactly
the 19 displacements of the nonzero roots of `f`. Since 1 is repeated,
`q(0)=q'(0)=0`; write `q(Y)=Y^2 P(Y)` with `P` monic of degree 17.
The coefficient of `Y^18` in `q` is 19. Every coefficient below degree 19 is
in `19 O`: recursively compare `(1+Y)q(Y)` with the Taylor expansion, using
`19 | binom(20,k)` for `2<=k<=18`.
Moreover,

\[
 P(0)=\binom{20}{2}b_{18}=190b_{18}.
\]

For any nonzero root `delta` of `P`, `v(delta)<1/17` would make its leading
term the unique term of least valuation, impossible. Hence

\[
 v(\delta)\ge 1/17.
\tag{2}
\]

If `b_18` is a unit, the constant coefficient of `P` has valuation exactly 1;
the same least-term argument gives `v(delta)=1/17` for all 17 roots of `P`.
They are distinct. More precisely, choose one of them `rho`; reducing
`P(rho Z)/rho^17` gives `Z^17-1`. Consequently the 17 residues `delta/rho`
are the 17 distinct 17th roots of unity. Root 1 has multiplicity exactly 2.

This observation already forces `a_18=0` exactly: `G_18` has unit value at 1
and so has no root in the unit cluster; its CA witness must be the exact root 0.
It does not by itself force `b_18=0`.

## 2. A linked first-jet condition when b_18 is a unit

Fix the exact support
`I={j in {2,...,19}: a_j != 0}`; necessarily `19 in I`.
For `j in I`, select a common root `1+delta_j` of `G_j` and `f`.
It cannot be 0, since `G_j(0)=a_j != 0`. Take `delta_19=0`.

Define integer polynomials `A_j(z)` recursively by `A_0=1,A_1=0` and

\[
 A_j=\begin{cases}
 -\sum_{i<j}\binom ji A_i(1+z_j)^{j-i},&j\in I,\\
 0,&j\notin I.
 \end{cases}
\]

Then the actual coefficients satisfy `a_j=A_j(delta)`. Put

\[
 \alpha_j=A_j(0),\qquad
 \mathcal F(z)=\sum_{i=2}^{19}c_iA_i(z),\qquad
 K_j=\left.\frac{\partial\mathcal F}{\partial z_j}\right|_{z=0}\pmod {19}.
\]

All these quantities are determined by `I` through integer arithmetic. The
constant necessary condition is `mathcal F(0)=0 mod 19`. In the unit-`b_18`
case, divide `mathcal F(delta)=0` by `rho`. Its constant term has valuation
at least 1 and every term of total degree at least two has valuation at least
`2/17`; reduction therefore yields the additional condition

\[
 \boxed{\quad\sum_{j\in I}K_j\zeta_j=0,\qquad
 \zeta_j\in\{0\}\cup\mu_{17},\qquad \zeta_{19}=0.\quad}
\tag{3}
\]

Here `zeta_j` is exactly the residue of `delta_j/rho`; in particular
`zeta_j=0` implies `delta_j=0` exactly, because every nonzero displacement
has valuation `1/17`.

The scale root `1+rho` need not be selected as a derivative witness. In
particular, this lemma does not assert that any selected `zeta_j` is nonzero:
the all-zero assignment satisfies (3). Excluding a configuration in which
every selected nonzero-support witness is exactly 1 requires a separate
argument about the resulting exact integer triangular system. The unit
condition on `b_18` alone does not supply that argument.

There is also the useful identity

\[
 \sum_{j\in I}K_j=\overline{b}_{18}\ne0.
\tag{4}
\]

To prove it, set every `z_j=s`. The recursion gives
`A_i(s,...,s)=alpha_i(1+s)^i`, so the left side of (4) is
`sum c_i i alpha_i mod 19`. Subtract `mathcal F(0)=0 mod 19`.
The remainder is `sum (-1)^i alpha_i`, over `2<=i<=19`. Since
`binom(18,i)=(-1)^i mod 19` and `alpha_19=-1 mod 19`, this is `b_18 mod 19`.
Although `z_19` is fixed to zero in the application, including it in this
calculation changes nothing: `K_19=-19 B_18=0 mod 19`.

For reproducible computation, the derivative matrix satisfies

\[
 L_{im}=-\sum_{l<i}\binom il L_{lm}
        -\mathbf1_{i=m}\,i\sum_{l<i}\binom{i-1}{l}\alpha_l
 \quad(i\in I),
\]

and `L_im=0` for `i notin I`; then `K_m=sum c_i L_im mod 19`.

## 3. Why this does not yet exclude the unit-b_18 case

A concrete surviving constant scenario is

\[
 I=\{12,13,15,16,17,19\}.
\]

Its nonzero constant coefficients are

\[
 (\alpha_{12},\alpha_{13},\alpha_{15},\alpha_{16},\alpha_{17},\alpha_{19})
 =(-1,12,-806,7995,-48672,3424616).
\]

Here `mathcal F(0)=2107898=19*110942`, `b_18=5 mod 19`, and

\[
 (K_{12},K_{13},K_{15},K_{16},K_{17},K_{19})=(9,0,15,0,0,0).
\]

Equation (3) forces `delta_12=delta_15=0` exactly: if both corresponding
phases were nonzero their ratio would be `-9/15=7` in `F_19`, whereas
`mu_17 intersect F_19^*={1}`. If just one were nonzero, (3) also fails.
Thus the first jet yields two exact root collisions for this scenario.
It leaves the phases at 13, 16, and 17 unconstrained. For instance the
assignment `zeta_13=1` and all other phases zero satisfies (3). This is only
a surviving first-jet assignment, not an actual lift or CA polynomial.

The obstruction to a global proof is therefore precise. One must exclude all
surviving support scenarios, including `b_18=0`, and then control the higher
jets of witnesses whose linear weights vanish. Those jets must be coupled
to the common cluster polynomial; arbitrary unramified lifting does not do
this. Nothing above proves such a universal higher-jet exclusion.

## Verification boundary

`verify_p19_first_jet.py` checks the displayed constant scenario, the derivative
matrix, the divided identity modulo 19, and the phase-ratio obstruction using
standard-library exact arithmetic. It does not test or prove the existence
of a characteristic-zero lift. The valuation and recurrence arguments above
are proofs, not conclusions inferred from the finite computation.
