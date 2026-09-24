# Two mixed middle-coefficient strata in the row-1 seed

Research proof, 24 September 2026. This note proves two local exclusions and explains their use with the existing global seed classification. Its finite arithmetic is checked by the adjacent standard-library program `check_mixed_strata.py`; its valuation and root-count arguments are separate proof obligations. No unramified-lift assumption is made.

## 1. Exact hypotheses and normalizations

Let K be a finite extension of Q_17 large enough to contain the coefficients and all roots under consideration; further finite extensions are allowed. Normalize the valuation by nu(17)=1. A bar denotes reduction in its residue field, which may be enlarged to an algebraic closure. Consider a centered monic characteristic-zero Casas–Alvero polynomial of degree twenty,

f(X)=X^20 + sum_{j in J} binom(20,j) a_j X^(20-j) + D X^3 + E X,

where J is either

J_A={10,12,13,16}, or J_B={9,10,15,16}.

All coefficients a_j are integral, all roots are integral, and the residue polynomial is the row-1 seed

h(X)=X^20-X^3=X^3(X-1)^17.

Normalize the selected common root for the third Hasse derivative to one. Thus f(1)=H_3 f(1)=0, and exactly

D=-1140-sum_{j in J} binom(20-j,3) binom(20,j) a_j,
E=-1-sum_{j in J} binom(20,j) a_j-D.                         (1)

The selected root can be scaled to one by a unit: its residue is necessarily one, since H_3 h=X^17-1. This unit scaling preserves the displayed residue pattern. Write

G_j(X)=sum_{i=0}^j binom(j,i) a_i X^(j-i),

with a_0=1, with the displayed a_i, and all other a_i for 1<=i<=16 equal to zero. The polynomials G_j are scalar multiples of H_(20-j) f in characteristic zero, so each shares a root with f.

The two patterns excluded here are

A: (bar a10,bar a12,bar a13,bar a16)=(16,14,1,0),
B: (bar a9,bar a10,bar a15,bar a16)=(16,9,9,0).              (2)

For the exact-support application, a16 is nonzero. The proof below also covers the a16=0 boundary: where a finite value for nu(a16) is used, that boundary can instead be assigned nu(a16)=infinity until the final equations force it nonzero.

**Local exclusion theorem.** No polynomial satisfying these hypotheses exists in either pattern A or pattern B.

## 2. The two small roots and the correct value of a16

Equation (1), reduced after division by 17, gives

bar(E/17)=6 in A, and bar(E/17)=7 in B.                    (3)

In particular E has valuation one. The three-root residue cluster at zero consists of the exact root zero and two nonzero roots q having

nu(q)=1/2.                                                (4)

Here is a direct Newton justification. In f(X)/X the constant coefficient is E of value one, the X^2 coefficient D is a unit, and every intervening or lower-degree middle coefficient is divisible by 17. Thus the small nonzero roots have initial equation -Y^2+bar(E/17)=0 after X=sqrt(17)Y. Its two roots are nonzero and distinct in characteristic seventeen. Both corresponding roots of f are simple. The root zero is also simple because E is nonzero. Consequently every repeated root of f lies in the seventeen-root cluster at one.

The selected G16 root cannot be in the unit cluster, because direct reduction gives

bar G16(1)=13 in A, and bar G16(1)=2 in B.

If a16 is nonzero, its selected root is not exactly zero, so it is one of the q in (4). For A, the lowest-power nonconstant term of G16(q) is binom(16,13)a13 q^3; its coefficient is a unit. For B it is 16 a15 q; again its coefficient is a unit. All other nonconstant terms have strictly larger valuation. Hence

A: nu(a16)=3/2;     B: nu(a16)=1/2.                       (5)

The estimate nu(a16)>=8, which would hold if every preceding active coefficient vanished, is inapplicable to these mixed-unit patterns. The lower powers just exhibited are essential.

## 3. Leading model of the seventeen-root cluster

Set F(Z)=f(1+Z)=sum c_k Z^k. Equation (1) implies c0=c3=0. More strongly, equation (1) and the integer divisibilities 17|binom(20,j) for 4<=j<=16 show that each c_k for 1<=k<=16 is an integer polynomial in the a_j whose coefficients are divisible by 17. For the constant terms this follows from X^20-1140X^3+1139X; for the variable terms it follows from their common binomial factor. Thus the following bounds are divisibility in 17O, not an inference from residue zero in a ramified field:

nu(c_k)>=1 for 1<=k<=16, c17 is a unit, and bar c17=1.

The first divided condition and the second coefficient are

nu(c1)>1,
bar(c2/17)=kappa, where kappa=5 in A and kappa=3 in B.     (6)

These follow directly from (1) and (2). In particular c2 has value exactly one. All c18,c19,c20 are integral.

Choose an exact repeated root w in the unit cluster. If w=1, then c1=0. Otherwise put z=w-1 and epsilon=nu(z)>0. Subtracting F(z)/z from F'(z), both zero, yields

0=sum_{k>=2}(k-1)c_k z^(k-1).

The only possible lowest-valued terms are c2 z, of value 1+epsilon, and 16c17 z^16, of value 16epsilon. Every other term has strictly greater value than the smaller of these two. Therefore epsilon=1/15. Substitution in F(z)/z then gives nu(c1)>=16/15. This also holds when w=1.

The same term comparison in F(z)/z shows that every nonzero root displacement in the unit cluster has value at least 1/15. Take pi with pi^15=17 and put

lambda=overline(c1/(17 pi)).

The integral polynomial F(pi Y)/pi^17 has reduced polynomial

g(Y)=Y^17+kappa Y^2+lambda Y.                             (7)

Exactly seventeen roots are represented in this leading cluster, counted with multiplicity. This follows either from the Newton polygon or by factoring out the three roots whose displacement from one is a unit. The leading coefficient of the resulting degree-seventeen factor is a unit and its reduction is (7). Thus the multiplicity of any root of g is exactly the number of roots of f, counted with multiplicity, in the corresponding next residue cluster. This statement includes arbitrary ramification and does not claim the roots already belong to K.

The repeated root w gives a common root eta of g and g'. Since g'=2 kappa Y+lambda, it is the unique repeated location of g. There are two possibilities:

- eta=0, lambda=0, and g=Y^2(Y^15+kappa), with a double root at zero and fifteen simple nonzero roots;
- eta is nonzero, lambda=-2 kappa eta, eta^15=kappa. After Y=eta T, its root locations satisfy

R(T)=T^17+T^2-2T=0.                                     (8)

## 4. First variations of the normalized derivative equations

For each of the first three active middle indices, its coefficient is a unit. Its selected common root therefore reduces to one. Denote its leading displacement by

Y_j=overline((w_j-1)/pi).

The all-witnesses-at-one normalized coefficient baselines are

A: (a10*,a12*,a13*)=(-1,65,-560),
B: (a9*,a10*,a15*)=(-1,9,-22023).

The exact recurrence G_j(w_j)=0, used in increasing j, proves nu(a_j-a_j*)>=1/15. Define A_j=overline((a_j-a_j*)/pi). Its first variation is

A_j=-bar(G_j*'(1))Y_j-sum_{i<j}binom(j,i)A_i.

For pattern A this gives

A10=7Y10,
A12=14Y10+Y12,
A13=9Y10+4Y12.

For pattern B it gives

A9=8Y9,
A10=5Y9,
A15=8Y9+8Y15.

All equalities in this section are over the residue field of characteristic seventeen. The absent coefficient Y13 in the first list and Y10 in the second are a consequence of the vanishing derivative residues; no assumption about these witnesses has been made.

Exactly, with h_j=((19-j)-2binom(20-j,3))binom(20,j),

c1=-2261+sum_{j in J} h_j a_j.                           (9)

Each h_j is divisible by 17. At the displayed baselines with a16=0, c1 is divisible by 17^2. Also nu(a16)>1/15 by (5), with the zero boundary harmless. Applying (9) to the preceding first variations proves

A: lambda=14Y10+2Y12,
B: lambda=12Y9+3Y15.                                    (10)

The finite integer identities for the derivative residues, h_j, and these linear forms are independently reconstructed by the checker.

## 5. A nonzero repeated leading location is impossible

Suppose eta is nonzero and divide the marked leading locations by eta. All resulting t_j satisfy (8). Since lambda/eta=-2kappa, equations (10) become

A: t12=12+10t10,
B: t15=15+13t9.

In characteristic seventeen the following elementary Euclidean calculations have nonzero constant last remainders:

A:
R(12+10T)-10R(T)=5T^2+2T+13=:Q_A(T),
R(T) mod Q_A(T)=2T+11,
Q_A(T) mod (2T+11)=13.

B:
R(15+13T)-13R(T)=3T^2+16T+6=:Q_B(T),
R(T) mod Q_B(T)=3T+4,
Q_B(T) mod (3T+4)=7.

Thus neither pair R(T)=R(alpha+beta T)=0 has a solution in any algebraically closed field of characteristic seventeen. This excludes eta nonzero in both cases. No finite-field rational-point search is being substituted for geometric emptiness: the Euclidean identities prove the assertion over the algebraic closure.

Consequently lambda=0 and the repeated leading location is zero.

## 6. The two simple-derivative witnesses are exactly one

When lambda=0, equations (10) give

A: Y12=10Y10;     B: Y15=13Y9.

Every nonzero root of g now has fifteenth power -kappa. If either paired root were nonzero, their ratio would have fifteenth power one. But 10^15=12 and 13^15=4 in F17. Therefore both marked leading locations are zero in either case.

The next cluster at leading location zero contains exactly two roots, counted with multiplicity. It contains the exact root one and the repeated root w. A repeated root already uses both available multiplicities, so w=1 exactly and this cluster consists of the double root one. Any common-root witness in this cluster is therefore exactly one. In particular:

A: w10=w12=1, giving a10=-1 and a12=65;
B: w9=w15=1, giving a9=-1 and a15=5004-3003a10.

We also have f'(1)=0 exactly. This is a root-count argument, not an assumption that congruent roots in a multiple residue cluster must coincide.

## 7. The remaining critical derivative witness is exactly one

In case A, substitute the preceding exact coefficients into (9). Let H_A=1961247925, the value of c1 at a13=-560 and a16=0. Then

0=H_A-4961280(a13+560)-24225 a16.                         (11)

Here nu(H_A)=2, while both displayed variable coefficients have value one. Since nu(a16)=3/2, equation (11) gives nu(a13+560)>=1. The polynomial G13 has the exact expansion at one

G13(1+Z)=(a13+560)-780 Z^2 + terms of degree at least 3,

with all higher coefficients integral and its linear coefficient exactly zero. The quadratic coefficient is a 17-adic unit. It follows that G13 cannot vanish at a unit-cluster root with displacement of value 1/15: the quadratic term would have the unique smallest value 2/15. Its common root must instead belong to the inner two-root cluster, hence is exactly one. Thus a13=-560.

For B, after eliminating a15 using its exact relation, equation (9) reads

0=H_B+L(a10-9)-24225 a16,
H_B=5132750687,
L=-42678636-3003(-248064).                               (12)

We have nu(H_B)=2 and nu(L)=1. Equation (12) and nu(a16)=1/2 give nu(a10-9)>=1/2. Here

G10(1+Z)=(a10-9)+45 Z^2 + terms of degree at least 3,

again with integral higher coefficients and zero exact linear coefficient. The quadratic term excludes every outer root of displacement value 1/15. Therefore the G10 witness is exactly one, a10=9, and a15=-22023.

If a16 was exactly zero at the outset, (11) or (12) gives the stronger bound at least one on the critical constant. The same reasoning still applies.

## 8. Final incompatible coefficient valuations

With all three unit witnesses now exactly one, equations (11) and (12) force respectively

A: a16=1961247925/24225=242879/3,
B: a16=5132750687/24225=15890869/75.

Both rational numbers have 17-adic valuation exactly one. This contradicts (5), namely 3/2 or 1/2. It also excludes a16=0. The local exclusion theorem follows.

For clarity, the exact arithmetic used at this last step is:

| Pattern | baseline c1 | nu(c1) | c1/17^2 mod17 | nu(h16) | forced nu(a16) |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 1961247925 | 2 | 10 | 1 | 1 |
| B | 5132750687 | 2 | 7 | 1 | 1 |

## 9. Exhaustive residue sieve and global scope

For either four-index J, every active G_j witness reduces to zero or one because h has precisely those roots. The triangular normalized recurrence reconstructs all coefficient residues from the sixteen binary markings. The necessary first divided condition is

0=bar(c1/17)=-133+sum_{j in J}(h_j/17)bar(a_j).

For completeness, the divided condition is necessary before either marking is selected. The same coefficientwise divisibility gives c_k in 17O for 1<=k<=16, so every nonzero displacement of a unit-cluster root has value at least 1/16. No nonzero root q in the zero cluster is repeated: f'(q)-f(q)/q has the unique lowest-valued term 2Dq^2, because every middle ordinary coefficient is divisible by 17 and has exponent at least four. The exact mean root zero is simple by the existing degree-19-plus-one theorem. A repeated root therefore lies in the unit cluster. At such a root w, all terms of f'(w)-f'(1) have value greater than one: orders 2 through 16 have their coefficient factor 17 and a positive displacement value; order 17 has the extra derivative factor 17; orders at least 18 have value at least 17/16. Hence nu(c1)>1, as claimed.

The complete sixteen-marking check leaves exactly two possibilities in each case:

- witnesses (0,0,0,1), coefficients (0,0,0,16);
- witnesses (1,1,1,0), coefficients as in (2).

The first is the previously excluded unit-16 stratum; the second is excluded by this note. These are exhaustive residue markings, not merely samples over the prime field: every possible residue root of h is already zero or one, so the recurrence covers every coefficient residue over an algebraic closure.

The existing complete degree-twenty characteristic-seventeen seed classification permits only row 1 for the exact centered deficiency supports

{10,12,13,16,17,19}, and {9,10,15,16,17,19}.

Combining that classification, the existing unit-16 exclusion, and the present theorem excludes both exact supports in characteristic zero. The source classification and its coverage audit are part of the already preserved degree-twenty evidence; this note neither redoes that classification nor treats its completeness as a consequence of the local argument.

The usual algebraic-specialization bridge suffices for complex candidates. Exact polynomial common-root equations and nonvanishing of the required coefficients define a finite-type variety over Q, with inverse variables encoding nonvanishing. A complex point would imply a point over Qbar by the Nullstellensatz. Its finitely many coefficients and marked roots lie in a number field and embed into Q17bar. The existing valuation normalization and unit H3 scaling then give the local hypotheses used above. Every valuation comparison and cluster argument permits finite ramification, with no use of coefficient congruence modulo 17O beyond what the displayed integer identities actually imply.

This is an exclusion of these two exact supports. It is not a proof of unrestricted degree twenty, the full Casas–Alvero conjecture, or an eight-term theorem without the separate exclusions of the other remaining supports.

## 10. Reproduction and assurance boundary

Run:

    python3 check_mixed_strata.py
    python3 -O check_mixed_strata.py

The adjacent verification.json and verification-optimized.json are identical. The checker reconstructs normalization (1), both sixteen-marking sieves, coefficient and derivative residues, all first-variation relations, the two geometric Euclidean exclusions, the critical quadratic expansions, and both forced rational a16 values. It uses only Python's standard library and explicit exceptions for failure, so optimized execution retains every acceptance condition. A changed quadratic constant is rejected as a negative control.

These computations certify the finite identities, not a mechanized proof of the root-count and valuation arguments. Independent review of that bridge is recorded separately.
