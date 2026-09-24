# Independent classification of the characteristic-17 m=4 model

23 September 2026. **PASS: 209 distinct reduced marked points over the algebraic closure of F17.** This classifies a leading model and its derivative witnesses. It is not a characteristic-zero lift exclusion. The coordinate called zero below is the translated Hasse-third-derivative root; it is not automatically the original mean root.

## Equations and complete parameter cover

Write

    g=X^17-X^4+bX^2+cX.

Its relevant Hasse derivatives are

    H1g=-4X^3+2bX+c,  H2g=-6X^2+b,  H3g=-4X.

If u witnesses H2 and v witnesses H1, their derivative equations give

    b=6u^2,  c=4v^3-12u^2v.

The two remaining root equations are exactly

    Eu=u^17+5u^4+4uv^3-12u^3v=0,
    Ev=v^17+3v^4-6u^2v^2=0.

H3 is already witnessed at zero. The following disjoint cases cover the whole algebraic closure:

| Case | Parameters | Number of reduced marked points |
|---|---|---:|
| Origin | u=v=0 | 1 |
| u=0, v nonzero | v^13=-3 | 13 |
| v=0, u nonzero | u^13=-5 | 13 |
| u,v nonzero | t=v/u, R(t)=0, u^13=q(t) | 182 |

Here

    q(t)=-5-4t^3+12t,
    R(t)=t^15 q(t)+3t^2-6.

In the last case the exact factorization in F17[t] is

    R=-4(t+8)^2(t-7)^2(t-1)^3 F5(t) F6(t),
    F5=t^5+t^4-8t^3+6t+6,
    F6=t^6+t^4-4t^3+7t^2+8t-8.

F5 and F6 are irreducible. The displayed factors are distinct, and

    gcd(R,R')=(t+8)(t-7)(t-1)^2.

Thus R has exactly 14 distinct roots. The gcds of R with t, q(t), and t^3-3t are all 1. In particular every parameter has t nonzero, q nonzero, and c nonzero. For each t there are exactly 13 choices of u, because 13 is invertible in characteristic 17. This proves the count 1+13+13+14*13=209 without restricting to rational points over F17.

## Root and witness multiplicities

In the both-nonzero chart put X=uY. Up to the nonzero scalar u^4 the polynomial is

    H_t(Y)=q(t)Y^17-Y^4+6Y^2+4(t^3-3t)Y.

The monic gcds are exactly

    gcd(H_t,H1H_t)=Y-t,              if t!=1,
    gcd(H_t,H1H_t)=(Y-1)^2,          if t=1,
    gcd(H_t,H2H_t)=Y-1,              for every t,
    gcd(H_t,H3H_t)=Y,                for every t.

These identities were checked over each of the five irreducible parameter factors, in the fields F17[t]/(factor). They apply to all their conjugate roots. In particular there is exactly one location shared with each relevant Hasse derivative; there is no unlisted repeated root.

Since H3g=-4X, the root u=v at t=1 has multiplicity exactly three. For t!=1 the root v has multiplicity exactly two: H2g(v)=6u^2(1-t^2), and the only root of R with t^2=1 is t=1. The root u is simple when t!=1, since H1g(u)=4u^3(t-1)^2(t+2), and the only common factor of R with t^3-3t+2 is (t-1)^2. Zero is simple throughout the both-nonzero chart because c is nonzero.

The boundary gcds give the complete table:

| Parameters | Multiplicity of g at marked H3 root 0 | At marked H2 root u | At marked H1 root v | Only repeated-root location |
|---|---:|---:|---:|---|
| u=v=0 | 4 | 4 | 4 | 0, multiplicity 4 |
| u=0, v^13=-3 | 1 | 1 | 2 | v, multiplicity 2 |
| v=0, u^13=-5 | 2 | 1 | 2 | 0=v, multiplicity 2 |
| t=1, u^13=3 | 1 | 3 | 3 | u=v, multiplicity 3 |
| Other roots of R | 1 | 1 | 2 | v, multiplicity 2 |

At the origin the derivative gcds are X^3, X^2 and X. In the u=0 nonzero-v case they are X-v, X and X. In the v=0 nonzero-u case they are X, X-u and X. Therefore all roots outside the indicated repeated location are simple in every case. In particular the repeated parameter factors t=7 and t=-8 do not create additional repeated polynomial roots.

Uniqueness of each H1 and H2 shared-root location also shows that two distinct marked parameter points cannot represent the same pair (b,c). Consequently there are 209 distinct normalized polynomial models as well as 209 reduced marked points.

## Optional local-length accounting

The reduced count is not the scheme length. The leading monomials of Eu and Ev in a graded order are u^17 and v^17, so the quotient algebra has basis u^i v^j, 0<=i,j<17, and total length 289. The following local lengths give the same total without a further computer-algebra computation.

- At u=v=0 the degree-four initial forms have no common projective zero. Indeed the second form is 3v^2(v^2-2u^2); v=0 does not annul the first at a projective point, and t^2=2 would require 5-4t=0, which is incompatible. The local intersection multiplicity is therefore 4*4=16.
- At u=0,v nonzero the Jacobian is invertible (its diagonal entries are 4v^3 and 12v^3), so each of the 13 points has length 1.
- At v=0,u nonzero, Eu has nonzero u derivative 3u^3 and Ev is v^2 times a local unit. Each of the 13 points has length 2.
- With u,v nonzero, the change to (u,t) is invertible, and the equations are equivalent up to units to u^13-q(t)=0 and R(t)=0. The u derivative 13u^12 is a unit. The local length is thus the multiplicity of the corresponding root of R: three at t=1, two at t=7,-8, and one at the other eleven t values, for each of the thirteen u choices.

The total is 16+13+26+13*(3+2+2+11)=289. None of these nilpotent lengths is a characteristic-zero lifting certificate.

## Conditional bridge to the J=L=16 first blowup

Assume the preceding collective blowup construction and its cluster-collapse lemma, with J=L=16 and delta=1/13. The classification above gives one repeated leading-root location, of multiplicity r in {2,3,4}. All common witnesses of orders 1 through r-1 lie at that location. If the characteristic-17 Casas–Alvero statement is used in these small degrees, cluster collapse makes the corresponding exact cluster a single root of multiplicity r.

For r=4 the required small-degree assertion can be checked directly: center the shared H3 root to get X^4+aX^2+bX. If a=0, the common H1 condition forces b=0. If a is nonzero, normalize its H2 common root to 1, obtaining X^4-6X^2+5X, which is coprime to its first derivative in characteristic 17. Degrees 2 and 3 are immediate by the same elementary derivative argument.

The exact original mean is simple, so its leading root cannot be the repeated location. Its leading root is therefore simple. In the original, untranslated blowup coordinates this says that zero is a simple root of the leading polynomial: every one of the other sixteen roots in the original zero cluster has valuation exactly delta. This conclusion does not identify the translated H3 root with the original mean.

Consequently nu(a19)=16/13, by the product formula for the linear coefficient. For a17 and a18, either the original mean's leading root is the unique shared H3 or H2 root, respectively, or it is not. In the first case the actual witness shares that simple leading class with the exact mean and must equal it; the corresponding coefficient vanishes exactly. In the second case the leading coefficient at that order is nonzero. Thus

    a17=0 or nu(a17)=14/13,
    a18=0 or nu(a18)=15/13.

Finally G2(w2)=w2^2+a2=0 gives a2=0 or nu(a2)=2/13. The a18 alternative relies on uniqueness of the shared H2 root; a bare minimum-valuation estimate would allow cancellation and would not prove it.

These implications are conditional on the stated collective blowup and cluster-collapse inputs and apply to J=L=16. They do not cover J=16,L<16 or exclude any lift.

## Replay boundary

`check_independent_model.py` imports only the Python standard library. It checks the factorization, all irreducibility and degeneration gcds, and each root-multiplicity gcd in the required finite extensions. Ordinary and optimized Python runs both pass, with identical JSON receipts `independent-model.json` and `independent-model-optimized.json`. The local-length and characteristic-zero bridge arguments are mathematical deductions above, not conclusions inferred from a finite search.
