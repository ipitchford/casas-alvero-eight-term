# Support A: routing and two local restrictions

24 September 2026. Research only. Exact centered normalized deficiency
support S={2,4,10,17,18,19}. These arguments are not a complete exclusion.
Write G_j=sum_{i=0}^j binom(j,i)a_i X^(j-i), and normalize nu(17)=1.
All roots and normalized coefficients are integral after the standard
root normalization. Exact support and arbitrary ramification are retained.

## 1. Correct routing: rows 1 and 2, after an exact-root argument

The complete nine-seed table first retains rows 1,2,4 because a3=0
exactly. Row 3 has nonzero a3 residue and is excluded immediately.
In row 4, a17 has residue zero and G17 reduces to X^17: all intermediate
binomial coefficients binom(17,i) are divisible by 17. Its common witness
must reduce to zero. But the row-4 seed has linear coefficient 8, so zero
is a simple residue root and its unique lift is the exact mean root zero.
That witness forces a17=G17(0)=0 exactly, contrary to support. Thus only
rows 1 and 2 remain. Nonzero exact a17 alone would not exclude its zero
residue; the simple-root argument is essential.

G3=X(X^2+3a2) has the canonical exact witness zero because a3=0. It does
not force a nonzero witness or an additional root at sqrt(-3a2).

## 2. Row 1: exclude a G18 witness reducing to zero

The seed is X^20-X^3. Normalize its unit G17 witness to exactly one;
its residue is one, so this preserves the seed and integrality. Put
t=a2, A=a4, b=a10, D=1140a17, K=190a18, E=20a19. Then

    f=X20+190tX18+4845AX16+184756bX10+DX3+KX2+EX,
    D=-1140-155040t-2713200A-22170720b,
    E=1139+154850t+2708355A+21985964b-K.

Here f(1)=H3 f(1)=0, where H3 is the third Hasse derivative. Also
nu(t)>0, D is a unit, and zero is simple exactly because E is nonzero.

Suppose the G18/Hasse-second witness q reduces to zero. It is nonzero
because a18 is nonzero. Set eta=nu(q)>0. Its derivative equation gives

    K=-3Dq + error of valuation >eta.

All higher terms have strictly larger valuation, including the terms
with the integral parameters t,A,b. The root equation then gives

    E=2Dq^2 + error of valuation >2eta.

After scaling X=qY, the degree-two initial polynomial of f(X)/X is a
unit times (Y-1)(Y-2). Thus the two nonzero roots in the zero residue
class both have valuation eta and are simple. The G2 witness is one of
these roots, so nu(t)=2eta. Every repeated root of f must now lie in
the residue class of one.

Write f(1+Z)=sum c_k Z^k. Exactly c0=c3=0, and

    c1=-2261-306850t-5353725A-42678636b+K,
    c2=-3230-436050t-7558200A-58198140b+K.

All c4,...,c16 belong to 17O; c17 is a unit, and c18,c19,c20 are
integral. If eta<1, then nu(c1)=nu(c2)=eta. Every nonzero root
displacement in the one-class has valuation eta/16, by unique-minimum
comparison in f(1+Z)/Z. At such a root the constant c1 is uniquely lowest
in f'(1+Z): the order-17 contribution gains a factor 17, and the other
contributions have larger valuation. Exact root one is simple as well.
This contradicts the existence of a repeated root. Therefore eta>=1.

It follows that nu(t)>=2 and nu(E)=2eta>=2. All c1,...,c16 are now in
17O. Every nonzero root displacement in the one-class has valuation at
least 1/16. Evaluation at a repeated root gives nu(c1)>1. Dividing the
two exact displayed identities by 17 and reducing in the residue field
therefore gives

    K/17 = 14-bbar,
    K/17 = 16+8Abar,
    hence bbar+8Abar=15.

The G4 and G10 witness residues belong to {0,1}. Their triangular
recurrences give exactly

    (Abar,bbar)=(0,0),(0,16),(16,0),(16,5).

The corresponding values bbar+8Abar are 0,16,9,14, never 15. This
excludes the entire row-1 subbranch with a G18 witness reducing to zero.
The remaining row-1 G18 witness must reduce to one; no equality with the
fixed exact root one is asserted in that 17-fold residue class.

## 3. Row 2: a ramification-safe four-marking sieve

The ordinary seed factors as

    h=X20-3X18-X3+3X = X(X-1)^17(X^2-3).

Its G2 witness reduces to one (minus one is not a root); scale it
exactly to one. Thus a2=-1 and f(1)=0. Write A=a4,b=a10. The other three
simple residue classes are zero and the two roots alpha,beta of X^2-3.
Every H1 repeated witness reduces to one. The G17 witness reduces to
one because G17bar=X^17-1. The G18 witness also reduces to one: its
reduction is X(X^17-1), but the zero class contains only the exact mean,
which cannot witness the nonzero exact coefficient a18.

Put f(1+Z)=sum c_k Z^k. Then c0=0, c4,...,c16 belong to 17O,
c17 is a unit, c18=0 exactly, and c19,c20 are units. The selected
common roots of f with its first three derivatives all reduce to one.
If all seventeen roots in that class equal one, c1=c2=c3=0. Otherwise
let delta be the least valuation of a nonzero displacement. The third,
second, and first derivative equations, in that order, imply

    nu(c3)>=min(1+delta,17delta),
    nu(c2)>=min(1+2delta,17delta),
    nu(c1)>=min(1+3delta,18delta).

These inequalities also hold when a selected displacement is exactly
zero. At a root attaining delta, the c17 Z17 term has valuation
17delta, while every other term has valuation at least
min(1+4delta,19delta). Thus delta>=1/13. In particular all of
c1,c2,c3 have valuation strictly greater than one.

Eliminating the low-degree coefficients D,K,E yields the exact identity

    c1-c2+c3 = -128231+2204475A+15519504b.

After division by 17, this gives the necessary residue equation

    5+16Abar+12bbar=0.

Active G4 and G10 witnesses cannot lie at the simple mean root. Their
residues lie in {1,alpha,beta}, and their squared values are 1 or 3.
The exact derivative recurrences therefore give this complete table:

| Abar | bbar | 5+16Abar+12bbar |
|---:|---:|---:|
| 5 | 14 | 15 |
| 5 | 8 | 11 |
| 9 | 7 | 12 |
| 9 | 6 | 0 |

Only (Abar,bbar)=(9,6) remains. Both selected middle witnesses then
reduce to alpha or beta. These residue classes are simple, so equal
residues imply equal exact roots. There remain four oriented markings
for the G4/G10 witnesses. Opposite residues do not justify treating the
exact witnesses as negatives of each other.

## Remaining obstruction and arithmetic scope

The later A_ROW1_EXCLUSION.md completes the remaining row-1 argument
and records its separate proof/jet obligations. The row-2 branch with
four oriented simple-root markings remains unresolved by these files.
No old claim of automatic simplicity of the zero cluster has been used;
it was proved only in the row-1 subbranch treated above. Every valuation
comparison allows arbitrary positive fractional valuations.

check_arithmetic.py checks the integer identities and complete tiny
residue tables using only Python integer arithmetic. It does not certify
the valuation arguments or the inherited nine-seed classification.
