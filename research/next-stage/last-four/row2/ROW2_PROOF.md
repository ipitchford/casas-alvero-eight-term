# Row2 exclusion for exact support {2,4,10,17,18,19}

Research proof proposed 24 September 2026, independent audit pending. All valuations have nu(17)=1; no unramified assumption on the candidate.

## 1. Normalization and integral divided equations

The seed is h=(X17-1)X(X²-3). Its roots0 and ±sqrt(3) are simple; the cluster at1 has multiplicity17. The normalized G2 witness lies in the1-cluster. Scale it exactly to1, giving a2=-1 and f(1)=0. Put a=a4,b=a10,T=H3f(1), and let F be the ordinary quadratic coefficient. Then

 f=X20-190X18+4845aX16+184756bX10+DX3+FX²+EX,
 D=153900-2713200a-22170720b+T,
 E=189-4845a-184756b-D-F.

All coefficients are integral. T,F have positive valuation. H1,H2,H3 common witnesses all lie in the1-cluster: H1 because the other roots are simple; H2 because its only seed common residues are0 and1 and F is exactly nonzero; H3 because its only common residue is1.

Write f(1+Y)=sum c_kY^k. We have c3=T,c18=0,c17=-2280,c19=20,c20=1, while c4,...,c16 belong to17O. Further

 c1=-5353725a-42678636b+304589+2T+F,
 c2=-7558200a-58198140b+432820+3T+F,
 c2-c1=T+17(7543-129675a-912912b).

Claim T,F lie in17O. If mu=min(nu(T),nu(F))<1 and c1 has value mu, every nonzero unit-root displacement has value at least mu/16. At a repeated root the term c1 of f' then has uniquely least value: terms from c2,c3 exceed mu; terms of orders4..16 have value>=1; order17 has an additional17; the order19 term has value>=18mu/16. This is impossible. Thus c1 has value>mu, requiring nu(T)=nu(F)=mu and cancellation of2T+F. A H3 witness1+z then has nu(z)=mu/17, because in its equation only T and the order20 contribution1140 z17 can be lowest; all intervening coefficients are divisible by17. But at this root, in f(1+z)/z, c17 z16 has value16mu/17, strictly less than every other term. Contradiction.

With T,F in17O, every nonzero unit displacement has value>=1/16. Evaluating H1,H2,H3 at their unit common roots now shows nu(c1),nu(c2),nu(T)>1. Retain the order19 H2 term: binom(19,2)=171 is a unit modulo17. Its displacement exponent is17, giving value>=17/16>1. Thus the divided relation

 7543-129675 abar-912912 bbar=0

holds in the residue field.

## 2. Residue coverage and simple outside witnesses

The active G4 and G10 witnesses cannot equal the unique residue-zero root0. Their possible residues are1,±s with s²=3. G4=X4-6X²+a implies abar5 at1 and abar9 at±s. G10=X10-45X8+210aX6+b gives the four possibilities

 (abar,bbar)=(5,14),(5,8),(9,7),(9,6).

The divided relation takes respective values2,6,5,0 modulo17. Hence both witnesses reduce to±s and (abar,bbar)=(9,6).

The actual roots in these two residue classes are unique. Over the unramified quadratic field choose exact roots r0=±sqrt(3). The polynomial coefficients differ from the seed's integer representative by17O (T,F are in17O and all middle binomial coefficients are divisible by17). Evaluating f(r0) gives value>=1, while f'(r0) is a unit. Every actual root in that class therefore differs from r0 by value>=1, even in a ramified ambient field. At its G4 witness,

 a=9-(r²-3)²,

so nu(a-9)>=2. At its G10 witness, this implies nu(b+47628)>=1. Consequently

 nu(c2-c1-T)>=2.

At the surviving residues c4/17=8. In particular c4 has value1, so the entire17-root unit cluster cannot coincide at1.

## 3. The first nontrivial unit-cluster model

Let delta be the least positive valuation of a nonzero unit-root displacement. The preceding strict coefficient bounds show delta>1/16. The witness equations give

 nu(T)>=min(1+delta,17delta)=1+delta,
 nu(c2)>=min(1+2delta,17delta),
 nu(c1)>=min(1+3delta,18delta).

Using c2-c1-T in17²O improves the first bound to

 nu(T)>=min(1+2delta,17delta,2).

If delta<1/13, a root attaining delta makes c17 z16 uniquely lowest in f(1+z)/z: all the displayed lower-degree terms have values greater than16delta, as do the terms of degree19 and20. Hence delta>=1/13. The resulting useful bounds are

 nu(c1)>=16/13, nu(c2)>=15/13, nu(T)>=15/13.

Choose pi13=17. After scaling, the degree17 initial polynomial of the complete unit cluster is

 L(Y)=-2Y17+8Y4+lambda2 Y²+lambda1 Y.

The missing cubic term follows from the strict inequality nu(T)>14/13. All17 roots are captured because delta>=1/13; the other three roots contribute a unit local factor. Define kappa=8. The selected H1,H2,H3 roots reduce to common roots of L with its corresponding Hasse derivatives, since differentiation and this integral scaling give the leading derivatives. In particular H3L=4kappa Y.

First lambda1=0. Otherwise the zero root of L is simple. The H3 witness must belong to this single-root subcluster, which already contains the exact root1; hence that witness is exactly1 and T=0. The relation c2-c1-T in17²O then forces lambda2=0. Now H2L=6kappa Y², so its witness also belongs to the same single-root subcluster and is exactly1. Thus c2=0, which forces c1 in17²O, contradicting lambda1 nonzero.

Suppose lambda2 nonzero. The zero root of L has multiplicity2. Let eta be the scaled location of a repeated root of f. If eta=0, the size-two subcluster containing the exact root1 and that repeated root collapses to1. The H3 witness is in the same subcluster, so T=0. Again c2-c1-T in17²O contradicts the nonzero lambda2 (nu(c2)=15/13 while nu(c1)>16/13).

If eta nonzero, L(eta)=L'(eta)=0 implies

 eta²=-lambda2/(2kappa), eta13=-kappa/2.

The H2 common witness has a nonzero scaled location v and satisfies

 v²=-lambda2/(6kappa), v13=-5kappa/2.

Thus rho=v/eta satisfies rho²=1/3 and rho13=5. But rho13=rho*(1/3)^6=8rho in characteristic17, so rho=7. Its square is15, different from1/3=6. This contradiction is over the full algebraic closure. Therefore lambda2=0.

We obtain L=Y4(-2Y13+kappa). Its13 nonzero roots are simple; its derivatives H1,H2,H3 vanish only at0. All three selected derivative witnesses are therefore in the size-four inner subcluster containing the exact root1.

## 4. A good-characteristic cluster lemma

A separated cluster of m roots, in which f and each H_kf for1<=k<m have a common witness, collapses to a single exact root if the degree-m Casas-Alvero conjecture holds over the residue field. To prove this, if the cluster is not collapsed, center at one of its roots and scale by a greatest distance between two roots of the cluster. The normalized cluster polynomial has degree m and at least two distinct residue roots. All roots outside the cluster are strictly farther away, so their factor reduces to a nonzero constant after normalization; their differentiated contributions have strictly positive valuation. The selected derivative witnesses give common roots of the residue cluster polynomial with every Hasse derivative below m. This is a nontrivial degree-m CA polynomial, a contradiction. The maximum distance exists because the cluster is finite; the argument permits arbitrary ramification.

For m=4 in characteristic17, the needed statement has a short proof. Center the H3 witness at0, giving q=X4+A X²+B X. If A=0 and B nonzero, q and q' cannot share a root, since their nonzero-root equations differ by3B. If A nonzero, its H2 common witness is nonzero; scale it to1. Then A=-6 and q(1)=0 gives B=5. The discriminant of X4-6X²+5X is4725, nonzero modulo17, so q has no repeated root. Thus every quartic CA polynomial in characteristic17 is a fourth power of a linear polynomial.

Apply the lemma to the inner cluster. All four roots coincide at1, yielding the exact equalities c1=c2=T=0. Therefore

 b=(7543-129675a)/912912.

The denominator is a17-adic unit. Since nu(a-9)>=2, b differs from B=(7543-129675*9)/912912 by value>=2.

## 5. The final simple-root lift obstruction

Evaluate the resulting exact family at a=9,b=B. Modulo X²-3 its relevant values, reduced modulo17², are

 f(r0)=170 r0,
 f'(r0)=283 r0+130,
 G10(r0)=204,
 G10'(r0)=92 r0.

The actual a,b differ by17²O; their effect on f is at least17³O and on G10 at least17²O. The actual simple root selected by G10 has the form r=r0+17h. Reduction of f(r)/17 gives

 0=10 r0+11(r0+1) h,

where now r0 denotes its residue with r0²=3. Reduction of G10(r)/17 would require

 0=12+7r0 h=(12r0-4)/(r0+1).

The denominator is nonzero. The numerator would give r0=6, whose square is2, not3. This contradiction handles both signs and all four choices of the G4/G10 outside witnesses. It excludes row2 for the entire exact support. The global support exclusion still requires its remaining row1 branch to be excluded independently.
