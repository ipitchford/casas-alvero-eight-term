# Exact univariate classification of the normalized family-C seed

This replaces reliance on the three-variable Groebner computation in
`ROOT_CLUSTER_NOTE.md`. It proves that the only CA polynomials with
a=4 and h(1)=0 in the seed family

    h=X20+4X16+bX15+cX3+dX

have (b,c,d)=(6,3,12),(6,2,0),(6,10,5). The conclusion holds over
the algebraic closure of F13 and includes every coefficient degeneration.
The same certificate identities apply over every algebraically closed
field of characteristic 13, including transcendental extensions of the
prime field. This does not assert that all three points lift to
characteristic zero.

## Generic H15 witness

The separately verified characteristic-13 exclusion of
X20+aX16+cX3+dX in
`../../casas-alvero-extension/explanation/MOD13_EXPLANATION.md`
(with its `check_mod13_explanation.py` replay) covers b=0.
Hence an H15 common root u is
nonzero. If u=-1, h(-1)=10, impossible. Handle u=1 separately.
For u!=0,1,-1, the H15 condition and h(u)/u=h(1)=0 give

    b=5u5+u,
    N=5+b-6u19-5u15,
    cn=N/(u-1), q=u+1, dn=q(8-b)-cn,
    c=cn/q, d=dn/q.

The division of N by u-1 is exact. Define polynomials in X over
F13[u]:

    P=q(X19+4X15+bX14)+cn X2+dn,
    D3=q(9X17+4X13)+cn,
    D1=q(7X19+12X15+2bX14)+3cn X2+dn.

Here P=q h(X)/X, while D3,D1 are q times the relevant Hasse
derivatives. Put R3=Res_X(P,D3), R1=Res_X(P,D1). If c!=0, an
H3 common root is nonzero, so R3=0; if c=0, then cn=0. Similarly
d!=0 forces R1=0, while d=0 implies dn=0. Every solution therefore
satisfies cn R3=dn R1=0, without discarding zero-coefficient charts.

The saved coefficient certificate contains polynomials U,V such that

    U cn R3 + V dn R1 = (u+1)^17 (u-1)(u-2)(u2+4u-2).

Thus u=2 or u2+4u-2=0 under the current guards. Exact polynomial
remainders give b=6,c=3,d=12 in the first case and b=6,c=2,d=0
in the second. The quadratic is coprime to u+1, so its coefficient
formulas are defined.

## The u=1 chart

Here b=6,d=2-c. Use the univariate parameter c and

    P=X19+4X15+6X14+cX2+2-c,
    D3=9X17+4X13+c,
    D1=7X19+12X15+12X14+3cX2+2-c.

The same common-root argument gives cR3=(2-c)R1=0. The saved
Bezout identity has right side

    (c-2)(c-3)(c-10).

Therefore the three coefficient points listed above are the complete
possibilities. Direct witnesses already verified in
`check_counterexamples.py` and the cluster calculations show that they
do occur; completeness is supplied by the identities here.

## Exact replay

The producer `seed_univariate.sing` computes resultants in Singular.
`export_univariate.py` retains their coefficients and constructs the
Bezout polynomials in `univariate-certificate.json`.

`verify_univariate.py` reconstructs the defining polynomials directly
from the Hasse binomial coefficients. It independently verifies each
saved resultant by exact evaluation at sufficiently many points of
F_(13^3). In the generic chart, every coefficient as a polynomial in u
has degree at most 18. The Sylvester determinant bounds are

    deg R3 <= 17*18+19*18 = 648,
    deg R1 <= 19*18+19*18 = 684.

Agreement at 685 distinct field points proves both identities. The
special chart has coefficient-degree bound 1 and resultant bounds 36
and 38, so 39 points suffice. The field is F13[t]/(t3-t-1); its
irreducibility is checked by absence of a base-field root. Generic
points with q=0 are skipped to preserve specialization degrees; there
remain more points than the degree bound. This is exact polynomial
interpolation, not an absence-of-points search.

The replay then checks both Bezout identities by direct coefficient
multiplication, their displayed factorizations, the branch coefficient
remainders, and mutation controls. All checks remain active under
`python -O`. Normal and optimized runs pass.

The standard-library finite-field and resultant helpers are explicitly
shared with B's `verify_certificate.py`, with its source hash recorded
in the receipts. Thus this is independent of Singular's producer, but
is not claimed as an independent implementation from B's replay.

Artifacts: `seed-univariate.log`, `univariate-certificate.json`,
`univariate-verification.json`, and
`univariate-verification-optimized.json`. The generic resultant degrees
are 359 and 395; the special degrees are 19 and 21.

Combining this classification with the exact valuation argument in
`ROOT_CLUSTER_NOTE.md` removes the d=0 point from possible
characteristic-zero full-support lifts. The six marked residue points
and four grouped cluster classes in that note are therefore exhaustive.
They have not all been excluded in characteristic zero.
