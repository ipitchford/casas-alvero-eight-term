# Exclusion of the exact u=1 branch by ramification-safe first jets

23 September 2026. Research proof under internal review; not a full exclusion of Family C.

## Hypotheses and conclusion

Use the already established normalization and residue classification in
`work/casas-alvero-sixterm/C/ROOT_CLUSTER_NOTE.md` and its independent review
`work/casas-alvero-sixterm/reviews/C_AUDIT.md`.

Let f be a characteristic-zero CA polynomial of exact support
{20,16,15,10,3,1}, in the valuation normalization where all roots and all
binomial-normalized coefficients are integral, an H16 common root is exactly1,
and A=-4845. Assume an H15 common root u is also exactly1. Then

    f=X^20-4845X^16+62016X^15+CX^10+DX^3+EX,
    E=-57172-C-D.

In particular C!=0. Write the valuation additively with val(13)=1. Since
13 divides binom(20,10)=184756 exactly once, integrality of the normalized
coefficient gives val(C)>=1. The previous residue classification leaves

    (Dbar,Ebar)=(3,12) or (10,5).

Write v for an H3 common root and w for an H1 common root. The surviving marked
patterns, specialized to exact u=1, are

    (vbar,wbar)=(2,1),(2,4),(11,3),(11,11).

For the first pattern the cluster count forces w=1; for the last it forces v=w.
These equalities also follow directly because w is a repeated exact root and
the relevant residue cluster has multiplicity two. All four patterns are
impossible, as proved below. Thus the exact u=1 branch is excluded.

## 1. A valuation lemma that permits first jets in ramified extensions

Suppose x,y have positive valuation, C has valuation at least1, and two
integral polynomial equations around x=y=C=0 have constants in13R and a
Jacobian in (x,y) whose determinant is a unit. Then val(x),val(y)>=1.

Indeed, otherwise let gamma=min(val(x),val(y))<1. Taylor expansion and
multiplication by the integral inverse Jacobian express both x and y as sums
of terms with valuation at least min(1,2gamma)>gamma. This contradicts the
definition of gamma. The argument uses no discrete or unramified hypothesis.

Apply this to f(v)=H3f(v)=0, with x=v-r, y=D-d0, where

    (r,d0)=(2,3) or (11,10).

Here C has valuation at least1. Set C=0,D=d0 in the base polynomial f0. The
two equations have constants divisible by13 at v=r. Their Jacobians modulo13
are respectively

    [[9,6],[4,1]] and [[0,7],[4,1]],

and both determinants equal11 modulo13. Consequently

    C=13S,    D=d0+13T,    v=r+13R,

with S,T,R integral. This integrality is proved; it is not assumed from the
prime-field residue computation.

## 2. The order-10 normalized derivative

Dividing H10f by its leading coefficient184756 gives the monic integral
polynomial

    G10=X^10-210X^6+1008X^5+a10,    a10=C/184756.

Since 184756/13=14212 is3 modulo13, its reduction is

    G10bar=X^10+11X^6+7X^5+9*Sbar.

Any H10 common root is integral and its reduction must be a common root of
this polynomial and the reduced f. The possible constant coefficients will be
determined by the first jets below.

## 3. The two patterns with vbar=11

Here d0=10 and

    h10=fbar=X^20+4X^16+6X^15+10X^3+5X.

Dividing f(v)=0 and H3f(v)=0 by13 and reducing gives

    2+12S+7T=0,
    3+4R+6S+T=0.                         (11-jet)

In the pattern wbar=3, the residue H1 root3 is simple as a root of H1:
(H1h10)'(3)=6. Since C and D-10 are in13R, the one-variable version of the
valuation lemma gives val(w-3)>=1. The root3 of h10 is double, so the term
depending on w-3 disappears from f(w)/13 modulo the maximal ideal. This gives

    9+11T=0.

Together with (11-jet), this yields

    (R,S,T)=(8,1,11),    a10bar=9.

In the pattern wbar=11, the residue root11 has multiplicity two in h10. Since
w is a repeated exact root and v is an exact root in the same cluster, v=w.
The additional equation H1f(v)=0 gives

    7+R+S+11T=0.

The three linear equations give

    (R,S,T)=(0,5,6),    a10bar=6.

Exact Euclidean identities over F13 establish

    gcd(h10,X^10+11X^6+7X^5+9)=1,
    gcd(h10,X^10+11X^6+7X^5+6)=1.

Both patterns are therefore impossible over any residue-field extension.

## 4. The pattern vbar=2,wbar=4

Here d0=3 and

    h3=fbar=X^20+4X^16+6X^15+3X^3+12X.

The first two jets give

    12+9R+8S+6T=0,
    6+4R+7S+T=0.                         (2-jet)

The residue H1 polynomial has a double root at4, while h3 has a triple root
there. Set delta=w-4. In the Taylor expansion of H1f(4+delta), the constant
and linear coefficients have valuation at least1, and the coefficient of
delta^2 is2 modulo13. If 0<val(delta)<1/2, the quadratic term has uniquely
smallest valuation, contradicting H1f(w)=0. Thus val(delta)>=1/2.

In f(4+delta), all nonconstant terms then have valuation strictly greater
than1: the first and second Taylor coefficients lie in13R, and powers of
delta of order at least3 have valuation at least3/2. Dividing f(w)=0 by13 and
reducing therefore gives the legitimate first-jet equation

    1+5S+8T=0.

Combining it with (2-jet) yields

    (R,S,T)=(5,12,7),    a10bar=4.

But

    gcd(h3,X^10+11X^6+7X^5+4)=1,

so this pattern is impossible. The half-integral valuation estimate explicitly
retains possible ramification; no integer-step lifting assumption is used.

## 5. The pattern vbar=2,wbar=1

The residue root1 has multiplicity two in h3. Since f(1)=0 and w is a repeated
root reducing to1, the cluster count forces w=1 exactly. Therefore H1f(1)=0.
For the same variables as in (2-jet), this is

    7+9S+2T=0,

because H1f(1)=13*61198+9C+2(D-3) and61198 is7 modulo13. Together with (2-jet),
the equation gives

    (R,S,T)=(1,0,3),    a10bar=0.

Here the derivative gcd is

    gcd(h3,X^10+11X^6+7X^5)=X.

Thus every H10 common root z must reduce to0. However h3'(0)=12 is a unit, so
zero is the only exact root of f that reduces to0: the polynomial divided
difference between z and0 reduces to that unit. Consequently z=0, and
H10f(0)=C=0. This contradicts the exact-support hypothesis C!=0.

## 6. Verification boundary

`check_jets.py` reconstructs all derivative and Taylor coefficients from the
integer polynomial and binomial formula, verifies the two unit Jacobians,
solves each linear system by modular row reduction with full rank, and checks
the four polynomial gcds using exact Bezout identities. It also checks the
double/triple multiplicities needed for the valuation arguments. These are
finite exact checks; the valuation lemmas above supply the transfer to every
ramified extension.

This proves exclusion of exact u=1 only. In the residue pattern (vbar,ubar,wbar)
=(2,1,4), the audit did not force u=1; the possibility u!=1 but ubar=1 remains
outside the present argument. The separate u=v branch likewise remains to be
settled. No unrestricted degree-20 or seven-term result is claimed here.
