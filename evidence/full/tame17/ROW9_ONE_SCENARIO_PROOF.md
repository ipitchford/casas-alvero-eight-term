# One row-9 witness orbit is obstructed at the second 17-adic digit

This excludes one explicitly specified marked residue scenario, comprising
five Frobenius-conjugate assignments. It does not exclude row 9, the entire
support, or unrestricted degree 20.

Let f be a hypothetical characteristic-zero CA polynomial in row 9, with
integral binomial-normalized coefficients

    f(X)=sum_j binom(20,j) a_j X^(20-j),
    a_0=1, a_1=a_2=a_17=a_20=0, a_3=-1.

Its mean root is 0 and its only multiple root is the exact triple root 1.
The reduction is

    h=X^20-X^17-3X^2+3X.

Use G_j(X)=sum_{i=0}^j binom(j,i)a_i X^(j-i), whose common-root
condition is the Hasse-order-(20-j) condition on f. Suppose the middle
witness residues are

    r_4=r_14=-2,  r_9=eta,  r_10=1,
    r_j=0 for j=5,6,7,8,11,12,13,15,16,

where eta is any root of the irreducible polynomial

    Q(Y)=Y^5-3Y^4-2Y^2-5Y-3 over F_17.

The corresponding deficiency support is {3,4,9,10,14,18,19}. It survives
the earlier support filters; that fact alone supplies no CA polynomial.

## Exact reduction to two variables

The seed roots -2 and eta are simple. Therefore every exact witness
reducing to -2 is the same exact root s, and every witness reducing to eta
is the same exact root t. The zero class contains only the exact mean root,
and the class at 1 has already collapsed to the triple root 1. Thus the
assigned residues force the exact witnesses s,t,0,1 used here; they are
not merely chosen approximations.

The triangular G_j equations give a_j=0 at all the listed zero witnesses,
and exactly

    a_4 = -s^4+4s,
    a_9 = -t^9+84t^6-126a_4t^5,
    a_10 = 119-210a_4-10a_9,
    a_14 = -s^14+364s^11-1001a_4s^10-2002a_9s^5-1001a_10s^4.

Let J={4,9,10,14} and C_j=binom(20,j). Solving f(1)=H_1f(1)=0
gives the ordinary coefficients

    [X^2]f = 18221-sum_{j in J}(19-j)C_j a_j,
    [X]f   = -17082+sum_{j in J}(18-j)C_j a_j.

Hence f=f_{s,t} is an integral polynomial expression in s,t; no
denominators need be introduced. The square subsystem is

    F(s,t)=(f_{s,t}(s), f_{s,t}(t))=(0,0).

The remaining triple-root equation is T(s,t)=0, where

    T = H_2f(1)/17
      = -8037+sum_{j in J} binom(19-j,2)(C_j/17)a_j.

This too is an integral polynomial in s,t. For all parameter values,
f_{s,t} reduces identically to h, since each C_j for j in J is divisible
by 17. The Jacobian of F modulo 17 is consequently diagonal, with entries
h'(s),h'(t).

## Exact finite-precision certificate

Work in R=(Z/17^2 Z)[eta]/(Q(eta)); Q is the same monic polynomial with
its displayed integer coefficients. Polynomial expressions are written in
the basis 1,eta,eta^2,eta^3,eta^4. The certificate gives

    sigma = 202+187eta+255eta^2+51eta^3+238eta^4,
    tau   = 272+222eta+255eta^2+153eta^3+187eta^4.

Direct exact arithmetic proves

    sigma=-2 mod17,  tau=eta mod17,
    F(sigma,tau)=(0,0) mod17^2,

and the Jacobian diagonal modulo 17 is

    8,  13+9eta+5eta^2+4eta^3+eta^4.

Both entries are units. Finally,

    T(sigma,tau)
      =17(13+11eta+13eta^2+8eta^3+3eta^4) mod17^2.

The parenthesized element is nonzero in F_(17^5), hence is a unit.
Thus T vanishes at the first digit but not at the second.

The independent replay derives the a_j from the general binomial G_j
equations instead of importing the four recurrence formulas. It evaluates
H_2f(1) at precision 17^3 and divides by 17 to recover T modulo 17^2;
it does not assume the producer's divided-obstruction formula. It also
checks irreducibility of Q, the Jacobian units, and all five nonzero
Frobenius-conjugate obstruction digits. Normal and Python `-O` runs pass.

## Why this excludes ramified as well as unramified lifts

Embed the algebraic coefficient field in an algebraic extension of Q_17
and use the valuation normalized by v(17)=1. Adjoin the unramified lift
of eta satisfying Q if necessary; this does not change the argument.
View sigma,tau as the displayed integral polynomials in that lift.

If an exact solution (s,t) with the prescribed residues existed, put
delta=(s-sigma,t-tau), and let gamma be the minimum of its two component
valuations. If delta is nonzero then gamma>0. Taylor expansion has the form

    0=F(sigma,tau)+DF(sigma,tau)delta+R(delta),

where the first term has valuation at least 2 componentwise and the
remainder at least 2gamma. The inverse Jacobian is integral because its
determinant is a unit. Therefore

    gamma >= min(2,2gamma).

This forces gamma>=2; the same conclusion is immediate if delta=0.
No integrality of the value group is assumed. Since T is an integral
polynomial, T(s,t)-T(sigma,tau) has valuation at least 2. But the certified
value T(sigma,tau) has valuation exactly 1. Therefore T(s,t) cannot be
zero, contradicting the triple root.

All expressions have rational integer coefficients, so Frobenius conjugation
of eta gives the same argument for each of the five roots of Q. The whole
five-element marked orbit is excluded, including every ramified lift.

## Reproducibility and limit

- `lift_row9_one_scenario.py` is the bounded certificate producer. It tests
  at most eight digits and stops at the first nonzero obstruction; this run
  stopped at precision two.
- `row9-one-scenario.json` contains the exact vectors above.
- `check_row9_one_scenario.py` independently reconstructs the general
  derivative equations and verifies the finite certificate using only the
  Python standard library.
- `row9-one-scenario-replay.json` and the optimized replay contain the
  passing results.

Other supports, witness assignments, and the degree-ten residue-root orbit
remain untested here. The significance of this bounded example is that the
finite-precision obstruction method works beyond the first residue equation;
it does not establish full coverage of any previously unresolved branch.
