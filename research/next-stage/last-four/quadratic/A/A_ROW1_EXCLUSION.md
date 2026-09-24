# Support A: complete exclusion of its row-1 branch

24 September 2026. Research result pending the parent's independent
argument audit. This does not exclude the row-2 branch or the whole
support S={2,4,10,17,18,19}.

The global routing is proved in A_ANALYSIS.md section 1: exact a3=0
retains rows 1,2,4, and row 4 is excluded because its G17 witness must
be the simple exact mean root, contrary to nonzero exact a17. Thus
row 2 is the only other branch, and is still pending separate work.

Use the row-1 normalization and exact formulas in A_ANALYSIS.md,
section 2. Write h=a2, A=a4, b=a10, and let D,K,E be the ordinary
coefficients of X3,X2,X. Thus f(1)=H3f(1)=0, D is a unit with residue
16, h has positive valuation, and E is nonzero exactly. The residue
polynomial is X3(X-1)^17. All coefficients are integral, with arbitrary
ramification allowed and nu(17)=1.

The mean zero is simple. The only other zero-class roots, counted with
multiplicity, are two nonzero roots. Since G2=X2+h and h is nonzero,
its witness is one of these small roots. H1 denotes the first ordinary
derivative; H2,H3 denote the second and third Hasse derivatives.

## 1. Exhaust the derivative occupancies

If the H2 witness is small, the proof in A_ANALYSIS.md section 2 applies:
K=-3Dq+o(q), E=2Dq2+o(q2), and the two small roots are simple. Hence
H1 has a unit witness. The resulting four-marking sieve is empty.

Suppose both H1 and H2 have unit witnesses. Write f(1+Z)=sum c_k Z^k.
We have c0=c3=0, c4,...,c16 in 17O, c17 a unit, and c18,c19,c20
integral. If all seventeen roots in this class equal one, c1=c2=0.
Otherwise let delta be the least positive valuation of a nonzero
displacement. The H2 and H1 equations give respectively

    nu(c2)>=min(1+2delta,17delta),
    nu(c1)>=min(1+3delta,17delta).

At a root attaining delta, c17 Z17 has valuation 17delta and every
other term has valuation at least min(1+4delta,18delta). Thus
delta>=1/13 and nu(c1),nu(c2)>1. The exact identities from A_ANALYSIS
then give

    K/17 =14-bbar =3-Abar-6bbar,
    hence Abar+5bbar=6.

The four complete G4/G10 markings give (Abar,bbar)=(0,0),(0,16),
(16,0),(16,5). Their Abar+5bbar values are 0,12,16,7, never 6.
This rules out both unit derivative witnesses.

Therefore H1 has a small repeated witness r and H2 has a unit witness.
The repeated root r consumes both nonzero roots in the zero class.
The G2 witness must equal r exactly, so

    h=-r2.

In particular both derivatives cannot have small witnesses: a repeated
small root has multiplicity exactly two, so H2 does not vanish there,
and H2(0) is nonzero because a18 is nonzero.

## 2. Integral-scale bound and unique residue marking

Put eta=nu(r). The equations f(r)=f'(r)=0 give

    K=-2Dr+error of valuation >eta,
    E=Dr2+error of valuation >2eta.

Thus nu(K)=eta, nu(E)=2eta, and nu(h)=2eta. If eta<1, the Taylor
coefficients c1,c2 both have valuation eta, while c3=0 and c4,...,c16
are divisible by 17. Every nonzero displacement in the unit cluster
then has valuation eta/16. At every such root, the constant c2 is
uniquely lowest in H2f: the degree-19 Taylor term has valuation
17eta/16>eta, the degree-20 term has valuation 18eta/16>eta, and all
remaining contributions have valuation greater than eta. The exact
root one also has H2f(1)=c2 nonzero. This contradicts the unit H2
witness. Hence eta>=1 and nu(h)>=2.

Now all c1,...,c16 belong to 17O, unit-root displacements have valuation
at least 1/16, and the unit H2 equation implies nu(c2)>1. Also
nu(E)>=2. Dividing the c2 and E identities by 17 gives

    K/17 =3-Abar-6bbar =16+8Abar,
    hence 9Abar+6bbar=4.

Of the same four markings, only (Abar,bbar)=(16,5) survives. It has
K/17=8. Therefore eta=1, and the repeated-root equation gives

    r/17 = -8/(2*16)=4,
    h/17^2 = -(r/17)^2=1

in the residue field. Also c1/17=3+5+8=16, so exact one is simple.
The other sixteen unit-cluster roots all have displacement value 1/16.
For pi16=17 their scaled initial values are precisely F17 nonzero,
the roots of Y16-1.

## 3. The corrected second-jet lemma applies

Use section 3 of ../B/B_EXCLUSION.md, including its corrected
degree-19 contribution. Its proof was independently rederived here.
The ordinary polynomial here differs from that lemma's comparison
polynomial by

    190h [X18-816X3+815X2] - E X(X-1).

The bracket vanishes at X=1 exactly. Since nu(h)=nu(E)=2, after exact
cancellation of X-1 in the root equation and division by 17, its error
has valuation at least one. The H2 equation divided by 17 has the same
error bound. This is strictly larger than the two-jet precision 2/16.

Our normalized high-derivative identities are

    A=-x4^4-6h x4^2,
    b=-x10^10-45h x10^8-210A x10^6.

Their changes from the comparison identities have valuation at least
two and cannot affect those jets. All three selected witnesses
x4,x10,y (where y witnesses H2) are either exact one or simple outer
roots. Their scaled residues t0,u0,v0 lie in F17, with residue zero
meaning exact one. The corrected first and second jet equations are

    2t0+u0+v0=0,
    13t0^2+10t0*u0+2v0^2=0.

Elimination gives 4t0^2+t0*u0+2u0^2=0, whose discriminant 3 is a
nonsquare in F17. Hence t0=u0=v0=0 and

    x4=x10=y=1 exactly.

For clarity, the first equation includes the degree-19 Taylor term:
binom(19,2)*20 is 3 modulo 17, and contributes 3*pi*v17 to H2/17.
An earlier B exploratory script omitted it and is invalid. The
corrected full 4913-marking second-jet enumeration in this directory
also leaves only (0,0,0). The repaired proof uses the unit-Jacobian
valuation bound for every nonzero scaled parameter, including v, so
fractional intermediate corrections are not being excluded by an
assumption about power-series expansions.

## 4. Exact collisions contradict the small-root equation

The exact high-witness collisions give

    A=-1-6h,   b=209+1215h.

Using H2f(1)=0 to eliminate K yields exact integer identities

    D=-4630968420-26921300640h,
    K=12155856290+70665826950h,
    E=-7563497030-43968975970h.

Since nu(h)=2, these give Dbar=16, K/17=8, and

    E/17^2=9+14(h/17^2)=6.

Every term of f(r)/(17^2 r), other than its E,Kr,Dr2 contributions,
has strictly positive valuation. Its residue must therefore be

    6+8*4+16*4^2=5 in F17,

which is nonzero. This contradicts f(r)=0 and excludes row 1 for
support A. Row 2 remains separate; A_ANALYSIS.md records its current
four-oriented-marking reduction. No global exclusion is claimed here.

check_arithmetic.py verifies the first residue sieves, the corrected
4913-marking second-jet system, and these exact final constants with
checks retained under Python optimization. The valuation arguments,
root multiplicity claims, and transfer of the jet lemma require their
separate mathematical review.
