# Complete degree-20 visible seed classification in characteristic 17

Status: exact computational classification, with proof and standalone replay in
this directory. The characteristic-zero lifting problem remains separate.

Let K be any algebraically closed field of characteristic 17. Consider

    h = X^20 + a X^18 + b X^17 + c X^3 + d X^2 + e X.

Require h and each Hasse derivative H_i h, 1 <= i <= 19, to have a common
root. Then, up to a nonzero scaling of X followed by monic normalization, h is
X^20 or one of the following nine polynomials. Entries are coefficients
(a,b,c,d,e) in F_17; all zero coefficients and all root collisions are allowed.

| Row | a | b | c | d | e | Chosen normalization |
|---|---:|---:|---:|---:|---:|---|
| 1 | 0 | 0 | 16 | 0 | 0 | H_3 common root 1 |
| 2 | 14 | 0 | 16 | 0 | 3 | H_3 common root 1 |
| 3 | 14 | 8 | 16 | 12 | 0 | H_3 common root 1 |
| 4 | 14 | 0 | 0 | 11 | 8 | H_18 common root 1 |
| 5 | 14 | 2 | 0 | 0 | 0 | H_18 common root 1 |
| 6 | 14 | 2 | 0 | 11 | 6 | H_18 common root 1 |
| 7 | 14 | 2 | 0 | 14 | 3 | H_18 common root 1 |
| 8 | 0 | 16 | 0 | 0 | 0 | H_17 common root 1 |
| 9 | 0 | 16 | 0 | 14 | 3 | H_17 common root 1 |

The coefficients are in F_17 as a conclusion, not an assumption on K. The
normalizations are successive charts, not a simultaneous choice of all
derivative witnesses. The table does not claim that the nine representatives
are pairwise inequivalent under every possible further normalization.

## Derivative identities and chart cover

Write U=X^17+c, V=X^3+aX+b, and Q=dX^2+(e-ac)X-bc. Then

    h=UV+Q,
    H_3 h=U,                    H_17 h=V,
    H_2 h=3XU+d,                H_18 h=3X^2+a,
    H_1 h=(3X^2+a)U+2dX+e-ac,  H_19 h=3X.

Every other Hasse derivative has zero constant coefficient and hence shares
the root 0 with h. These identities are checked directly from binomial
coefficients in the replay.

Suppose first c != 0. The unique root of H_3 is nonzero, so scaling it to 1
gives c=-1. The equation h(1)=0 gives e=-a-b-d, and

    Q=(X-1)(dX-b).

Let u be any common root of h and H_17=V. Then Q(u)=0. All possibilities
are covered by three polynomial charts:

1. b=0: a=s, d=t. There is no division or constraint on s,t.
2. b!=0 and u=1: a=-1-s, b=s, d=t.
3. b!=0 and u!=1: necessarily d!=0, u=b/d, and
   a=-s^2-t, b=st, d=t, with s=u.

For computational convenience charts 2 and 3 are extended to all s,t in K.
Every point of either extension still satisfies h(1)=0 and shares a root with
H_17. Thus overlaps, d=0, b=0, and all collisions introduce no missing cases
or spurious sufficiency claims.

In each chart, the three remaining conditions are exactly the vanishing of

    I=(Res_X(h,H_18 h), Res_X(h,H_2 h), Res_X(h,H_1 h)).

The polynomials in each resultant have fixed positive X-degrees and nonzero
constant leading coefficients. Therefore their vanishing is equivalent to a
common root over K, with no restriction on that root being zero.

## Exact chart certificates for c != 0

The exported certificates express each target below as a polynomial
combination of the three displayed resultants over F_17[s,t]. The replay
checks the identities coefficient by coefficient.

In chart 1 the ideal contains t^20 and

    s^20-3s^11t-2s^2t^2+3s^3-8s^2t-6st^2.

Consequently t=0 and s^3(s+3)^17=0, so (a,b,c,d,e) is row 1 or 2.

In chart 2 the ideal contains 1, so the chart is empty.

In chart 3 the ideal contains

    t^20(t+5),  t^20(s+5),  P(s,t),

where P is the explicit 40-degree target stored as T3 in the certificate.
Its specialization at t=0 is

    P(s,0)=s^40-3s^6=s^6(s^2-3)^17.

If t=0, this yields a=0 or -3, b=d=0, giving rows 1 and 2. If t!=0,
the first two identities force t=s=-5. The coefficient tuple is row 3.
All three retained tuples satisfy the original conditions, as independently
checked by univariate gcds; no converse radical-ideal assertion is needed.

## The chart c=0, a != 0

Choose a common root of H_18 and h. Since a!=0 it is nonzero. Scaling it
to 1 gives a=-3 and h(1)=0 gives e=2-b-d. Put b=s,d=t. The remaining
conditions are the vanishing of

    I=(Res_X(h,H_17 h), Res_X(h,H_2 h), Res_X(h,H_1 h)).

The exact membership certificate proves

    [s(s-2)]^19 in I,
    [st+6s-2t+5]^19 in I,
    [t(t-11)(t-14)]^18 in I.

Thus s=0 or 2. If s=0, the second polynomial forces t=11. If s=2,
the third forces t=0,11,14. These are exactly rows 4--7; all four
satisfy every active derivative condition by direct gcd verification.

## Remaining coefficient-zero charts

If c=a=0 and b!=0, scale a common H_17 root to 1. This gives b=-1 and
e=-d. If d=0, row 8 results. If d!=0, a common H_2 root r is nonzero
and d=-3r^18. Substitution in h(r)/r=0 gives

    -r^16(r-1)^2(2r+1)=0.

Hence r=1 or 8, giving d=14 or 12. For d=12, the gcd of h and H_1 is
1. For d=14 all conditions hold, giving row 9. The direct gcd checks are
over F_17[X], so their conclusions also hold over its algebraic closure.

If c=a=b=0 and d!=0, scaling an H_2 common root to 1 gives d=-3,e=2.
Any common H_1 root r is nonzero. Subtracting 3h(r)/r from H_1 h(r)
gives 3r-4=0, so r=7; but h(7)/7=1 in F_17, a contradiction.

If c=a=b=d=0 and e!=0, a common H_1 root r is nonzero and
H_1 h(r)-3h(r)/r=-2e != 0, again impossible. The all-zero tuple is the
monomial X^20 and is retained separately. This completes all coefficient
charts.

## Scope and replay

This is a classification of Hasse-CA seeds in the specified visible model
over the whole algebraic closure of F_17. It is not a proof that any seed
lifts to characteristic zero, or that it cannot lift. In a separate
characteristic-zero application, integrality of the binomial-normalized
coefficients and a retained unit root justify passing to a nonmonomial
visible seed; that transfer is not supplied merely by a finite-field table.

The `certificate_*.sing.log` files contain coefficient arrays for resultants,
targets, and lift multipliers. `check_classification.py` verifies the
resultants independently by exact finite-field interpolation bounds and
Euclidean resultants, the membership identities by sparse polynomial
multiplication, the target specializations, every listed gcd, and all
remaining boundary exclusions. It does not invoke Singular or trust a
Groebner-basis or radical output. Singular is only the certificate producer.

For clarity, the interpolation field is F_17[alpha]/(alpha^2-3), where 3
is a nonsquare modulo 17. The integer encoding i+17j represents i+j alpha
for 0 <= i,j < 17; it is not integer reduction modulo 17. Thus the grid
values encoded 0,...,B are distinct whenever B<289. For a resultant of
X-degrees m,n and coefficient degrees at most A,B in one parameter, its
degree in that parameter is at most nA+mB. The checker derives these bounds
from the source chart polynomials and checks that the candidate resultants
also satisfy them. The bounds used, in (s,t), are:

| Chart | First resultant | H_2 resultant | H_1 resultant |
|---|---|---|---|
| b=0 | (22,2) | (18,38) | (39,39) |
| u=1 | (22,2) | (18,38) | (39,39) |
| other u | (44,22) | (36,38) | (78,39) |
| c=0,a=-3 | (23,3) | (18,38) | (39,39) |

Each polynomial identity is checked on a full rectangular grid with one
more point in each coordinate than its displayed bound. These 12,895 exact
evaluations prove equality of bivariate polynomials: fix one coordinate
and use the univariate root bound, then repeat in the other coordinate.
The verification uses no randomness and makes no restriction to F_17-valued
parameters. After verification the membership identities hold as polynomial
identities over every extension field, so the deductions above cover all
algebraic-extension coefficient and witness values.
