# Direct second-jet obstruction in the unit-16 residue stratum

Research proposal, 24 September 2026; independent audit pending. This strengthens and simplifies the previously audited row-1 unit-16 and nonzero-a3 theorems.

## Statement and normalization

Let f be a nontrivial, centered monic, characteristic-zero CA polynomial of degree20, integrally normalized at17 with reduction X20-X3. Write f=sum binom(20,j) a_j X^(20-j). Assume a2=a18=0 exactly, a4,...,a15 have residue zero, and a16 has residue -1. The reduction implies a3 has residue zero. Claim: no such f exists. No restriction on the number of nonzero coefficients a4,...,a15 is imposed, and a3 may vanish or be nonzero.

Use the established simplicity-of-the-mean lemma (characteristic19) to obtain E, the ordinary linear coefficient, nonzero. Normalize a common Hasse-third root to1. Put t=a3, u=a16 and Cj=binom(20,j). Then

 f=X20+1140tX17+sum[j=4..15] Cj a_j X^(20-j)+4845uX4+DX3+EX,
 D=-1140-775200t-sum[j=4..15] binom(20-j,3) Cj a_j-19380u,
 E=-1-1140t-sum[j=4..15] Cj a_j-4845u-D.

All roots are integral, D is a unit, and the residue-zero cluster consists of0 and two nonzero roots. Each nonzero small root has value delta=nu(E)/2, since only E and Dq² can be lowest in f(q)/q. None is repeated, by the unique lowest term2Dq² in f'(q)-f(q)/q.

If t=0, E is in17O, so delta>=1/2. If t nonzero, G3=X³+t has a nonzero small common root, giving nu(t)=3delta. The formula for E gives2delta>=min(1,3delta), hence delta>=1/2. Thus nu(t)>=3/2 (infinity if zero). The specified residues now give E/17=11 in the residue field, so delta=1/2. For nonzero t its value is exactly3/2.

Induction in G_j=sum[i<=j] binom(j,i)a_i X^(j-i), at its small selected roots, gives nu(a_j)>=j/2 for4<=j<=15. A zero coefficient may use the exact root0. All ordinary contributions of these middle coefficients have valuation at least3.

## Collision

A G16 common root x reduces to1. Its equation gives

 u=-x16-560t x13+e, nu(e)>=2.

For f(1+Y)=sum c_kY^k, the exact coefficients are

 c1=17(-133-1425u)-1532160t+e1,
 c2=17(-190-1710u)-2170560t+e2,
 c3=0,
 c4=4845(1+u)+2713200t+e4,

where all e_k have value>=3. For5<=k<=16, c_k is in17O, while c17=1140(1+t), c18=190,c19=20,c20=1. In particular c2 has value1 and divided residue7.

If t=0 and 0<epsilon=nu(x-1)<1, the two possible lowest terms in f(x)/(x-1) have values1+epsilon and16epsilon, with coefficients10 and1 after scaling. Thus epsilon=1/15. If epsilon>=1, including x=1, c1 has value>=2 and c2 has value1. There are fifteen simple outer roots of displacement value1/15, from the nonzero roots of Y15+7, and an inner cluster of multiplicity2 containing1 and x. A repeated root must lie in this inner cluster. Consequently it must equal x=1.

If t nonzero, the same low-order balance applies for0<epsilon<1/2 and forces epsilon=1/15. For finite epsilon>1/2, c1 has value3/2 and is uniquely lowest in the divided-root equation, impossible. For epsilon=1/2, the divided-root equation forces c1 to have value3/2; the Newton polygon gives fifteen simple outer roots plus the simple root1 and one simple inner root of displacement value1/2, leaving no repeated root. The same simple-root description holds at x=1 because then c1 has value3/2. Thus the only case left is epsilon=1/15.

In that case put pi15=17, xi=bar((x-1)/pi). The initial polynomial is

 L(Y)=Y17+7Y²+3xi Y, with xi15=7.

All seventeen unit-cluster roots are captured: a displacement of smaller positive value would make the degree17 term uniquely lowest in the divided-root equation. L has just one multiple root, xi, of multiplicity2. That cluster already contains x and must contain the repeated root of f. Root counting forces that repeated root to be exactly x. Thus f(x)=f'(x)=0.

## The incompatible second jet

After substituting the G16 equation, the exact repeated-root equation gives

 Q0(x)+t Q1(x)+error=0, nu(error)>=3,
 Q0=-14516X19+38760X18-2280X²,
 Q1=-8121360X16+21705600X15-1550400X².

These are f'(x)-f(x)/x after discarding a4,...,a15; the discarded terms and the error in u carry a binomial multiplier divisible by17. Q1 is integral.

Write Q0(1+z)=sum q_k z^k. The exact facts needed are:

- nu(q0)=nu(q1)=2;
- nu(q2)=1 and q2/17=1 mod17;
- nu(qk)>=1 for3<=k<=16;
- q17=2 mod17, while q18,q19 are integral.

At nu(z)=1/15 the only least terms are q2z² and q17z17. Dividing by pi17 gives residue

 xi²+2xi17 = xi²(1+2*7)=15xi², nonzero.

Therefore nu(Q0(x))=17/15. The tQ1 term has value at least3/2 when t nonzero (and is zero otherwise); the error has value at least3. They cannot cancel Q0(x). If t=0 and x=1, instead Q0(1)=21964=17²*76 has value2, again below the error bound3. This closes the last collision case.

The theorem is therefore proved conditional on independent verification of the finite coefficient identities and the full collision argument. It does not eliminate any of the four mixed-residue supports currently remaining. It removes the previously retained a3=0,a4-nonzero boundary from the uniform unit-16 theorem. The older Bezout and ramification-field arguments remain valid alternative proofs on their narrower hypotheses, but are unnecessary for this stronger statement.
