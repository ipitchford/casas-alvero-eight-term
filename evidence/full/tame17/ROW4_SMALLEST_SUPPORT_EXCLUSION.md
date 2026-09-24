# A complete row-4 support exclusion

23 September 2026. This result concerns the canonical middle support
J={4,10,12}, equivalently deficiency support {2,4,10,12,18,19}, in
the characteristic-17 row-4 normalization. It does not exclude row 4
as a whole or prove the degree-20 conjecture.

## Exact family and the first divided critical value

Use normalized coefficients f(X)=sum binom(20,j) a_j X^(20-j).
The row-4 conditions give a2=-1, a3=a17=0, the simple root 1, and
a common root s of f and its second Hasse derivative, with s reducing
to 6. Put u_j=a_j for 4<=j<=16, and eliminate

    a18 = -s^18 +153 s^16 - sum binom(18,j) u_j s^(18-j),
    20 a19 =189 -sum binom(20,j) u_j -190 a18.

Write the resulting polynomial F(u,s;X). Its reduction is independent
of u. At s=6 it is

    h(X)=X^20-3X^18+11X^2+8X.

Its only multiple roots are the two roots alpha,beta of
q2(X)=X^2+3X+3, both of multiplicity two. Its other roots are simple.
Every actual candidate therefore has its H1 common root in one of these
two double residue classes. Both orientations are retained below.

The total s derivative of F(u,s;s) is 9 modulo 17 at s=6, so this
equation has a unique integral analytic solution S(u), reducing to 6.
Similarly F_X(u,S(u);X)=0 has a unique analytic solution R_alpha(u)
reducing to alpha: its X derivative is h''(alpha)=6, a unit modulo 17.
These statements hold over every residue coefficient chart; all Taylor
series used at a chart are evaluated on positive-valuation differences.
The row-4 lifting proof gives the same constructions in detail.

The function E_alpha(u)=F(u,S(u);R_alpha(u))/17 is integral analytic.
Here is an explicit coefficientwise first-order calculation, which
also proves the divisibility without assuming that the ambient field
is unramified. Lift alpha to a root of q2 over the integers. For
F(u,6;X)=f0(X)+sum u_j f_j(X), each f_i(6) and both coordinates of
f_i(alpha) are divisible by 17. In fact

    S(u)=6+17 sigma(u) modulo 17^2,
    sigma(u)= -F(u,6;6)/(17*9) modulo 17.

The partial s derivative of F reduces to X-X^2, whose value at alpha
is 3+4alpha. Moving the critical root changes the critical value only
at order 17^2. Consequently

    E_alpha(u) = F(u,6;alpha)/17 +(3+4alpha) sigma(u) modulo 17.

This is an affine polynomial ell_alpha in u, with coefficients in
F17[alpha]. For J={4,10,12}, it is

    ell_alpha = (10+14alpha) +(16+15alpha)u4
                +10alpha*u10 +(16+15alpha)u12.

The conjugate equation replaces alpha by beta; it does not apply
Frobenius to the independently varying coefficients u_j. A genuine
common critical root must have ell_alpha(ubar)=0 for its orientation.
This last equality is in the residue field. Evaluation of the integral
analytic identity is legitimate in ramified ambient fields as well.

## Complete residue enumeration

The polynomial h splits over F_(17^4). Its factorization over F17 is

    X(X+7)(X+11)(X+16)(X^2+3X+3)^2
      (X^4+3X^3+4X^2+2)
      (X^4+12X^3+14X^2+5X+14)
      (X^4+13X^3+16X^2+4X+11).

There are exactly seventeen distinct nonzero residue roots. An active
coefficient cannot have a witness in the zero residue class: h has a
simple root there, and f has the exact root zero, so that residue class
contains no other root. A witness at zero would force the exact
coefficient to vanish. Active coefficients with zero residue are,
however, retained throughout the enumeration.

For each choice of three witnesses rho4,rho10,rho12 among these seventeen
roots, the normalized derivative equations recursively determine

    u_j=-rho_j^j +binom(j,2)rho_j^(j-2)
        -sum_{i in J, i<j} binom(j,i)u_i rho_j^(j-i).

The complete census checks all 2*17^3=9,826 oriented markings. Exactly
two satisfy the appropriate ell_alpha=0, one for each conjugate
orientation. Both have

    (rho4,rho10,rho12)=(10,1,6),
    (ubar4,ubar10,ubar12)=(1,4,9).

No selected middle witness belongs to a double residue class. Thus the
quadratic signed-chart machinery is unnecessary for the survivors.
The optional first-jet filter in the producer is not used by this proof.

## Unique lift and nonzero critical value

All three surviving witness classes are simple. Write the exact witness
near 10 as t. The witness near 1 must be the already fixed exact root 1;
the witness near 6 must be the already selected root s. The derivative
equations therefore give the exact formulas

    a4=-t^4+6t^2,
    a10=44-210a4,
    a12=-s^12+66s^10-495a4*s^8-66a10*s^2.

Substitute these into F and impose f(t)=f(s)=0. The Jacobian in (t,s),
at (10,6) modulo 17, is [[2,12],[0,9]]. Its determinant is a unit.
There is a unique unramified solution with these residues, and every
solution over an arbitrary ramified extension is this same solution.
For completeness, if a solution and an approximate solution differ
at minimum valuation gamma>0, the invertible reduced Jacobian preserves
gamma in the linear Taylor term. All nonlinear terms have valuation
at least 2gamma. If the approximate residual is divisible by 17^n,
cancellation forces gamma>=n. This proves the finite-precision
uniqueness implication needed here without an ambient-field assumption.

The successive lifts are

| Modulus | t | s | a4 | a10 | a12 |
|---|---:|---:|---:|---:|---:|
| 17^2 | 95 | 91 | 86 | 191 | 9 |
| 17^3 | 2696 | 1536 | 1531 | 2792 | 2610 |

Over (Z/17^3)[alpha]/(alpha^2+3alpha+3), the unique critical root
reducing to alpha is 2788+3707alpha. Direct substitution gives

    f'(2788+3707alpha)=0 modulo 17^3,
    f(2788+3707alpha)=17^2(9+4alpha) modulo 17^3.

The latter is nonzero, since q2 is irreducible over F17. Conjugation
gives the same exclusion for beta. Hence no characteristic-zero CA
candidate can have this row-4 canonical support.

## Reproducibility and scope

`row4_first_obstruction.py` produces the complete residue census and
`lift_row4_smallest_support.py` produces the finite-precision certificate.
Their JSON receipts retain the field, witnesses, coefficients and critical
value. The separate standard-library checker `check_row4_smallest_support.py`
passes under normal and optimized Python, and `ROW4_SMALLEST_SUPPORT_AUDIT.md`
records the completed independent mathematical audit of this support.
The exclusion is computer assisted; it is not proof-assistant certified
or externally peer reviewed. The remaining row-4 supports are untouched
by this individual certificate.
