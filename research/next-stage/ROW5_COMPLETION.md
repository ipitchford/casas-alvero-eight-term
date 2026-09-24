# Completion candidate for the remaining row-5 seven-term support

Research note, 24 September 2026. Pending final proof/jet audit. No paper or review bundle is being produced.

## Exact problem and finite cover

The exact centered deficiency support is S={2,3,4,10,12,19}. Its only possible characteristic-seventeen reductions are rows 5 and 8. Row 8 was excluded by the complete 64-assignment divided-identity check in the previous research stage. Work in row 5, normalized using the common G2 root at one:

    f = X^20 - 190 X^18 +1140 a X^17+4845 A X^16
        +184756 b X^10+125970 c X^8+E X,
    E=189-1140 a-4845 A-184756 b-125970 c.

Here a=a3,A=a4,b=a10,c=a12 are nonzero exactly. Its reduction is X^17(X-1)^2(X+2); f(1)=0. The mean root zero is simple. Let y denote a G3 common witness, w an H1 common witness, and r the simple root reducing to -2.

The complete first-divided census is in ROW5_FIRST_DIVIDED.md. It forces the G4 witness to be r and leaves precisely these cases:

| y residue | w residue | G10 residue | G12 residue | (Abar,bbar,cbar) |
|---|---|---|---|---|
| 1 | 1 | 0 or 1 | -2 | (7,0,9) |
| -2 | 0 | 0 or 1 | 0 | (7,0,0) |
| -2 | 1 | 0 or 1 | 0,1,-2 | (7,0,0),(7,0,2),(7,0,9) |

Every common witness reducing to -2 equals r exactly, by its simple residue class. The double residue class at one contains the exact root one. If w reduces to one, its repeated-root multiplicity exhausts that class, so w=1, and every other selected witness in that class is also exactly one. In particular, if y reduces to one in a surviving row, then y=1 and a=2 exactly. Otherwise

    a(r)=-r^3+3r,
    A(r)=3r^4-6r^2.

When a=2 instead, A(r)=-r^4+6r^2-8r. These formulas follow from G3 and G4, not from identifying distinct roots merely because they reduce alike.

## Implicit analytic identities used below

Consider first the case y=r. For independent integral parameters b,c define f as above with a(r),A(r), and impose f(r)=0. Modulo 17 the resulting equation in r is r(r-1)^2(r+2), so the root r=-2 is simple with derivative16. There is a unique integral analytic solution R(b,c) reducing to -2, including over ramified extensions. All parameter terms in this equation have a factor17. Thus R is an integral convergent series in 17b,17c, with constant R(0,0), and R+2 is coefficientwise divisible by17.

Write H(b,c)=f'(1) after substituting r=R(b,c), and retain E(b,c) for the linear coefficient. Direct finite-precision calculation gives

    R(0,0)=4095 modulo17^3,
    H(0,0)/17^2 =5 modulo17,
    E(0,0)/17^2 =14 modulo17.

Their parameter expansions have linear coefficients

    H_b/17 =9 modulo17,   H_c/17 =0 modulo17,
    E_b/17 =10 modulo17,  E_c/17 =16 modulo17,

and coefficients of every parameter monomial of total degree at least two are divisible by17^2. This last assertion follows from the series in 17b,17c and the explicit linear parameter terms of H and E. The numerical jets are independently checked in row5-jets/.

Consequently H=0 with b,c of positive valuation forces nu(b)>=1: if nu(b)<1, its linear term has uniquely least valuation. If also nu(c)>=1, then

    b/17 =7 modulo the maximal ideal,
    E/17^2 =16+16(c/17) modulo the maximal ideal.

For the second family impose the exact G10 witness one:

    b_*(r)=44-120a(r)-210A(r).

The equation f(r)=0 with b=b_*(r) still has a simple root near -2, now analytic in 17c. At c=0 its root is 49 modulo17^3, and

    b_*/17=12,  E/17^2=15,  H/17^2=11 modulo17.

The linear coefficient of H as a function of c is divisible by17^2, as are all coefficients of degree at least two. Therefore for c of positive valuation H has valuation exactly two. This excludes H=0 in this family, without requiring c to vanish exactly.

All strict error comparisons here take place in the valuation ring, not just in an unramified integer quotient.

## 1. H1 witness at one, both middle witnesses at units

Then the G10 witness is exactly one and the G12 witness is exactly one or r. The four possibilities for the G3 and G12 witnesses in {1,r} are excluded by the integer Bézout identities in row5-unit/EXACT_UNIT_EXCLUSION.md. Their checker reconstructs the coefficient equations, rather than importing the proposed univariate equations. The identities include coefficient-zero boundary values and do not divide by b.

## 2. H1 witness at one, G10 witness at zero, G12 witness at a unit

Here 'at zero' means reducing to zero, not the exact zero. Since b is nonzero, its witness is a nonzero root in the zero cluster.

The G12 witness is exactly one or r. Its normalized derivative equation expresses c as a polynomial in r,b. Use t=(r+2)/17. The two equations f(r)/17=0, f'(1)/17=0 are integral equations in t,b. At their residue solution (t0,0), their Jacobians are

| Exact G3 witness | Exact G12 witness | t0 | Jacobian |
|---|---|---|---|
| 1 | r | 0 | [[16,16],[0,1]] |
| r | r | 0 | [[16,16],[9,1]] |
| r | 1 | 8 | [[16,1],[9,0]] |

All determinants are units modulo17. Their defects at the indicated integer point are divisible by17. The unit-Jacobian valuation bound therefore gives b in17O, even in ramified extensions. The corresponding E/17 residues are 8,8,15, so nu(E)=1.

The zero cluster has sixteen nonzero roots, all of valuation1/16: in f(X)/X its constant term has valuation1, the X^16 coefficient is a unit, and all other terms lie strictly above that Newton edge. At a G10 common root q in this cluster,

    0=q^10-45q^8+120a q^7+210A q^6+b.

The coefficient210A is a unit. Hence nu(b)=6/16=3/8, contradicting b in17O.

## 3. H1 witness at one, G10 witness at one, G12 witness reducing to zero

Only y=r occurs in the finite cover. The exact G10 witness one gives b=b_*(r). The implicit analytic identity above shows nu(H)=2 whenever c has positive valuation. But H=f'(1)=0 is required. This excludes the branch.

## 4. H1 witness at one, both middle witnesses reducing to zero

Only y=r occurs. The identities for H=0 first give nu(b)>=1. Put gamma=nu(c)>0.

If gamma<1, the expansion of E gives nu(E)=1+gamma. All sixteen nonzero zero-cluster roots then have valuation (1+gamma)/16<1/8. Indeed the constant and X^16 terms give this Newton edge, and the middle terms lie strictly above it. The G10 equation consequently gives nu(b)=6(1+gamma)/16<3/4, a contradiction. Thus gamma>=1.

The next integral jets now give nu(b)=1 and b/17=7. The G10 equation makes its witness q have valuation1/6. At q, every term of f(q)/q other than E and the unit-coefficient q^16 term has valuation greater than8/3. Therefore nu(E)=8/3.

If gamma>1, the next jet instead says E/17^2=16 modulo the maximal ideal, giving nu(E)=2, a contradiction. Hence gamma=1.

A G12 witness z reducing to zero satisfies

    0=z^12-66z^10+220a z^9+495A z^8+66b z^2+c.

The possible lowest nonconstant values are 8nu(z) and1+2nu(z). Since nu(c)=1, this forces nu(z)=1/8: below1/6 the first is strictly smaller, and at or above1/6 both exceed one. But at valuation1/8, the X^16 term of f(z)/z has value2; its constant has value8/3, and every other term has value greater than2. It cannot vanish. This contradiction closes the branch.

## 5. H1 witness in the zero cluster, G10 witness in the zero cluster

The finite cover forces y=r and the G12 witness also into the zero cluster. Let delta be the least positive valuation of a zero-cluster root. The G10 and G12 equations give

    nu(b)>=6delta,  nu(c)>=8delta.

The H1 witness equation G19(w)=0 gives

    nu(E)>=min(17delta,1+15delta).

At a root attaining delta, the X^17 term has value17delta. Every other term of f has value at least min(18delta,1+16delta). A unique minimum would result if delta<1, so delta>=1. Thus nu(b)>=6, nu(c)>=8, and nu(E)>=16.

The analytic solution R(b,c) differs from R(0,0) by valuation at least seven. The ordinary polynomial and its linear coefficient therefore differ from their b=c=0 values by valuation greater than two. But E(0,0)/17^2=14 modulo17. Hence nu(E)=2, a contradiction.

## 6. H1 witness in the zero cluster, G10 witness reducing to one

Again y=r and c has positive valuation. The G10 witness x need not equal one; no exact collision is assumed here.

The first divided identities at the surviving residues imply nu(f'(1))>1. The coefficient H2f(1) is a unit. If x differs from one, the exact divided-root equation at one shows nu(x-1)>1. The G10 equation then gives

    b=b_*(r)+epsilon,  nu(epsilon)>1.

The first jet of R gives b_*(r)/17=12 modulo17, so nu(b)=1. Let delta again be the least positive zero-cluster root valuation. The G12 equation and the H1 equation give

    nu(c)>=min(8delta,1+2delta),
    nu(E)>=min(17delta,1+15delta,2+9delta).

At a minimum root, the X^17 term has value17delta and the other terms have value at least min(18delta,1+16delta,2+10delta). Thus delta>=2/7. Consequently nu(c)>=11/7 and nu(E)>=32/7.

Compare with the implicit base family b=b_*(r),c=0. Its linear coefficient has valuation two and residue E/17^2=15. The deviations epsilon and c enter the f(r) equation multiplied by17. The unit implicit derivative therefore bounds the change in r, and then in E, strictly above two. Thus the actual E still has valuation two, contradicting nu(E)>=32/7.

## Coverage conclusion pending audit

The six sections exhaust all ten markings in the first divided cover. If the exact jet and argument audits close, row5 is excluded for S={2,3,4,10,12,19}; combined with the previous row8 exclusion this gives a complete global exclusion of that exact support. The other five current seven-term supports are untouched. No eight-term theorem, complete row5 exclusion for arbitrary supports, or completed significance target follows.
