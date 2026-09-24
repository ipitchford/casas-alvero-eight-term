# Quartic first models: exact cluster collapse and a next-lift exclusion

This concerns all 124,068 marked row-8 assignments with `J=L=16`.
Their first scale is `delta=1/13`. It does not cover the 413 assignments
with `J=16,L<16`, and it does not exclude the whole nondegenerate stratum.
All original coefficients remain allowed.

## 1. The exact finite leading model

The preceding collective reduction gives, after translating the Hasse-
order-three common root and scaling,

    g(Y)=Y^17-Y^4+bY^2+cY.

Let u and v be its marked Hasse-order-two and order-one common roots.
Their derivative equations give

    b=6u^2, c=4v^3-12u^2v,
    Eu=u^17+5u^4+4uv^3-12u^3v=0,
    Ev=v^17+3v^4-6u^2v^2=0.

The two leading monomials are `u^17,v^17`, so the full quotient algebra
has dimension 289, with nilpotents retained. Its reduced points are
classified exactly as follows.

* `u=v=0`: one point.
* `u=0,v!=0`: `v^13=-3`, giving 13 points.
* `v=0,u!=0`: `u^13=-5`, giving 13 points.
* `uv!=0`: set `t=v/u` and `q(t)=-5-4t^3+12t`. Then
  `u^13=q(t)` and `R(t)=t^15 q(t)+3t^2-6=0`.

Over F17,

    R=-4(t+8)^2(t-7)^2(t-1)^3 F5(t) F6(t),
    F5=t^5+t^4-8t^3+6t+6,
    F6=t^6+t^4-4t^3+7t^2+8t-8.

Both F5 and F6 are irreducible, and R has no common root with t or q.
Thus its 14 distinct roots each give 13 choices of u, and there are
exactly `1+13+13+14*13=209` reduced marked models. This is a description
over the entire algebraic closure, not merely a search over F17.

`check_independent_model.py` verifies the factorization, irreducibility,
boundary cases, and all derivative gcds by exact polynomial arithmetic
over F17 and its explicit quotient fields. The independent report is
`INDEPENDENT_MODEL_AUDIT.md`; the 289-dimensional algebra is not replaced
by its 209-point reduction when a later lifting argument needs nilpotents.

## 2. Every repeated first cluster collapses exactly

The checked gcds show that every g has just one repeated-root location.

| Model | Repeated root | Multiplicity | Hasse witnesses there |
|---|---|---:|---|
| `u=v=0` | 0 | 4 | orders 1,2,3 |
| `uv!=0,t=1` | u=v | 3 | orders 1,2 |
| every other model | v | 2 | order 1 |

Every other root is simple. The marked order-two common root is unique
as a location and equals u. The order-three common root is unique and
equals 0. Repeated factors of R at t=7 or t=9 do not give additional
repeated roots of g.

The cluster-collapse lemma in `../../../two_adic/CLUSTER_COLLAPSE.md`
applies to this unique repeated cluster. Its residue size r is 2,3,or4;
the exact common witnesses of all orders below r are in that cluster.
Hasse-CA polynomials of these degrees in characteristic 17 are pure
powers:

* For degree two, center the common first-derivative root.
* For degree three, center its second-derivative root, obtaining
  `X^3+bX`; a common root with `3X^2+b` forces b=0.
* For degree four, centering its third-derivative root gives
  `X^4+aX^2+bX`. If a=0, the first derivative forces b=0. Otherwise
  normalize a common second-derivative root to 1. The polynomial becomes
  `X^4-6X^2+5X`, whose gcd with `4X^3-12X+5` is 1 over F17.

Consequently the repeated cluster is one **exact** root of multiplicity
r. Its multiplicity is exactly r because no other root has that first
residue. This conclusion uses the actual Hasse witnesses, not just
occupancy or the shape of q.

Every other first cluster contains one root, and the three original unit
roots were already simple. Thus a hypothetical polynomial in this entire
stratum has exactly one multiple root globally, of multiplicity 2,3,or4.
This statement alone is not treated as a contradiction to CA.

The exact original mean is simple. It cannot lie in this repeated
cluster. Therefore its marked root gamma in the normalized g is simple.
All other first residues differ from gamma. Returning to the original
centered row-8 coordinate proves that all 16 nonzero roots in the
17-root zero cluster have valuation exactly `1/13`. The three outside
roots remain units.

## 3. Exact coefficient alternatives across the whole J=L=16 stratum

The ordinary coefficient of X is the product of the other 19 roots, up
to sign. Its binomial factor 20 is a 17-adic unit, so

    nu(a19)=16/13.

The degree-two normalized equation is `a2=-w2^2`. Its witness is either
the exact mean or one of the other zero-cluster roots. Hence

    a2=0, or nu(a2)=2/13.

For the low ordinary Hasse orders use the unique common-root locations
in g. If the leading `Y^k` coefficient about the marked mean gamma
vanishes, gamma is a common root of `g,H_k g`. Since gamma is simple,
the actual order-k common witness must equal the exact mean: its first
residue has only one root above it. The corresponding original
coefficient is then exactly zero. If that leading coefficient is
nonzero, its valuation is fixed by the scaling. This gives

    a17=0, or nu(a17)=14/13;
    a18=0, or nu(a18)=15/13.

In the canonical model these exact-zero alternatives have a precise
meaning:

    a17=0 iff gamma=0;
    a18=0 iff gamma=u;
    gamma is never the repeated-root location v.

In particular `a17=a18=0` occurs only in the boundary `u=0,v!=0`, with
the original mean at its simple root 0. No assumption of residue
simplicity was made before the cluster-collapse argument established it.

## 4. A coefficient-linked first correction

The next equation retains information from the original marked unit
witnesses; it is not a condition on an arbitrary quartic model alone.
Write `rho_j` for the original middle witness residue, and set
`beta_j=binom(20,j)/17 mod17`. Let A_j be the exact unramified constants
obtained from the triangular normalized equations by setting a2=0,
a3=-1, every zero-residue witness to 0, and each unit witness to its
corresponding exact cube root of unity. These constants reduce to the
already specified `abar_j`.

Choose an actual root pi attaining `nu(pi)=delta`. Unit roots differ
from their exact cube-root representatives by valuation at least
`2delta`: the a2 and a3 perturbations have that valuation, while every
other relevant ordinary coefficient perturbation has valuation at least
one. Simplicity of the unit residue roots transfers this bound to the
roots themselves.

For a zero-residue middle witness put `x_j=bar(w_j/pi)`, and let
`x_17=bar(w_17/pi)` be the actual Hasse-order-three witness. Then
`nu(a_j-A_j)>=delta`. Its first coefficient
`d_j=bar((a_j-A_j)/pi)` is computed by the exact linear recurrence

    d0=d1=d2=d3=0;
    d_j=-j*abar_(j-1)*x_j,                  if rho_j=0;
    d_j=-sum_(i=4)^(j-1) binom(j,i)*d_i*rho_j^(j-i), otherwise.

The equation for G17 at its actual witness gives

    bar(a17/(17*pi))=-abar16*x_17.

In the divided f(1) identity, the a2, a18/17, and a19/17 terms start at
orders `2delta,2delta,3delta`. Its constant part in the unramified base
has valuation at least one by the already imposed residue cut. Dividing
the next term by pi is therefore legitimate and yields

    sum_(j=4)^16 beta_j*d_j - abar16*x_17 = 0.       (F)

Write the first sum as `sum lambda_j*x_j` over the zero middle labels.
After the canonical translation/scaling of g, let z_j be the marked
g-root corresponding to that zero witness, and let gamma be the marked
original mean. Equation (F) becomes

    sum lambda_j*(z_j-gamma) + abar16*gamma = 0.     (F')

Every z_j and gamma is an actual marked root of g, and gamma must be
simple. Thus (F') is a finite algebraic compatibility test tied to the
original residue assignment. It is invariant under the unused common
scaling. It is only a necessary first correction.

Indeed the model `u=0,v=12`, with `gamma=z_j=0` for every zero middle
label, satisfies (F') for every set of lambda_j. This exact example
prevents interpreting (F') alone as a whole-stratum obstruction. The
following higher-precision argument does exclude that configuration.

## 5. A uniform next-lift exclusion

**Claim.** In the stratum `J=L=16`, it is impossible to have both
`a17=a18=0` and every zero-residue middle witness equal to the exact mean.
Equivalently, when the original mean is the common simple H2/H3 root of
the quartic model, at least one middle zero-cluster witness must be a
different exact root.

Suppose otherwise, and set T=a2. Every middle coefficient whose witness
has zero residue is exactly zero. The others are determined by their
selected exact unit roots through the triangular normalized derivative
equations. By section 3, T is either zero or has valuation `2/13`, and

    nu(a19/17)=3/13.

Work over the complete unramified quadratic base containing the three
cube roots of unity. The three simple roots of

    Q_T(X)=(X-1)(X^2+X+1+3T)

are integral power series in T over that base: the derivative at each
of their three T=0 roots is a unit. The actual unit roots of f differ
from the matching roots of Q_T by elements of `17O`. Indeed
`f-X^17 Q_T` has every coefficient in `17O`, and the unit-root derivative
is a unit. This argument is valid after arbitrary ramified base change.

Recursively substituting these three power series into the exact
normalized equations gives power series A_j(T), with unramified integral
coefficients, such that

    a_j-A_j(T) lies in 17O,       4<=j<=16.

For zero witnesses put A_j(T)=0. The initial data are
`a2=T,a3=-1-3T`; no unramifiedness of T is assumed. The divided f(1)
identity, using a17=a18=0, now implies

    F(T) + 20*a19/17 lies in 17O,
    F(T)=-67-190T+sum_(j=4)^16 (binom(20,j)/17)*A_j(T).

Here F has integral coefficients in the unramified base and F(0) is
divisible by 17, by the original residue cut. Thus F(T) must have
valuation exactly `3/13`. This is impossible:

* If T=0, its valuation is at least one.
* If `nu(T)=2/13` and the linear coefficient of F is a unit, that
  linear term is uniquely smallest, and `nu(F(T))=2/13`.
* If the linear coefficient is a nonunit, all terms have valuation at
  least `min(1,4/13)=4/13`.

This proves the claim without a discretization assumption on the original
coefficient valuations. Only the fixed power-series coefficients lie in
the unramified base.

The claim includes the case of no middle zero-residue labels: then its
condition on such witnesses is vacuous. It does not exclude cases with
other zero-cluster witnesses, the other quartic models, or the complete
J=L=16 stratum.

## Status

The finite leading models are classified over the algebraic closure,
and the actual witness geometry yields new exact coefficient alternatives
throughout the entire nondegenerate J=16 stratum. Equation (F') retains
the original unit coefficient data, and section 5 excludes one uniform
class of its otherwise universal first-order survivors. Other compatible
marked models and their further lifting constraints remain unresolved.
