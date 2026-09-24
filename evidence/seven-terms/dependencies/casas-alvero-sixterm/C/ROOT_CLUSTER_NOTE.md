# Bounded root-cluster follow-up for family C

This note separates valuation arguments from a computer-algebra
classification. The full support remains unresolved.

Let a hypothetical characteristic-zero CA polynomial with exactly this
support be translated and scaled at 13 so all roots are integral and a
nonzero root is 1. Write

    f = X20 + A X16 + B X15 + C X10 + D X3 + E X.

Every displayed coefficient is nonzero in characteristic zero. The
normalized-coefficient integrality argument makes all coefficients
integral and gives v(C)>0. Lowercase letters denote residue coefficients,
so h=X20+aX16+bX15+cX3+dX.

## 1. The coefficient A is a unit

A nonmonomial seed with a=d=0 cannot be CA. If also b=0,c!=0,
normalizing the H3 witness to 1 gives c=4, whereas h(1)=0 would
require c=-1. If b!=0, normalize an H15 witness to 1, giving b=5,c=7.
An H3 common root v!=0 then satisfies v17=5 and v5=-1. Thus v2=8,
and v5=v(v2)^2=12v forces v=1, a contradiction.

If a=0 in any nonmonomial reduction, therefore d!=0. The reduction
of H16 is 9X4, so its characteristic-zero common root r reduces to
0. It cannot equal 0 because A!=0. But in f(r)/r the constant term
E is a unit and every other term has positive valuation, impossible.
This proves A is a unit. Normalize its H16 common root to 1 by a
unit scale: exactly A=-4845, and a=4, b+c+d=8 in the residue field.

## 2. A finite computational classification

Let u,v,w be H15,H3,H1 common-root witnesses. The derivative
equations give

    b=5u5+u, c=4v17+9v13, d=8-b-c.

The remaining equations h(u)=h(v)=h(w)=H1h(w)=0 form an ideal
in F13[u,v,w]. `seed_mod13.sing` computed its reduced Groebner
basis in 25.9 seconds, reporting dimension zero and quotient length 17.
The basis contains

    v3+3v2-4v+1 = (v-2)(v-10)(v-11).

Both this cubic and b-6 reduce to zero against the basis. Thus the
calculation identifies only the residue coefficient points

    (a,b,c,d) = (4,6,3,12), (4,6,2,0), (4,6,10,5).

The basis is saved in `seed-mod13-groebner.txt`. A separate request
for ideal-membership certificates via Singular's lift function exceeded
its 120-second cap. **This initial classification was only a CAS result,
not an independently replayed membership certificate.** The completed
Groebner output and two zero reductions are retained; the timeout is
recorded in `seed-classification-job.json`. No further three-variable
membership job was started.

The subsequently authorized univariate route in
`UNIVARIATE_CLASSIFICATION.md` now proves the same classification with
exact independently replayed resultant and Bezout identities; the earlier
membership timeout is no longer a blocker. These coefficient points have
several marked-root assignments, not merely three marked-root points.

## 3. The point (4,6,2,0) cannot lift

For h=X20+4X16+6X15+2X3, direct Euclidean computation gives
gcd(h,h')=X2. Any common root w of f,f' therefore reduces to zero.
It is nonzero because E!=0 in characteristic zero. Subtracting
f(w)/w from f'(w) gives

    19w19 + 15A w15 + 14B w14 + 9C w9 + 2D w2 = 0.

D is a unit and v(w)>0. The last term has strictly smaller
valuation than every other term, impossible. This works over
arbitrary ramified valued extensions; it is not an integer-lift
test modulo 169.

## 4. Six surviving marked points and four branch classes

For (a,b,c,d)=(4,6,10,5), the only common root with H16 or H15
is 1, and h'(1)=1. Both characteristic-zero witnesses therefore
equal the normalized root 1 exactly. A simple residue root has
only one root of the monic polynomial in its cluster, counted with
multiplicity. Consequently B=62016 exactly, from
15504+16A+B=0. The H3 witness reduces to 11, and the H1 witness
reduces to either 3 or 11, both double residue roots. If w reduces
to 11, its repeated exact root exhausts the two-root cluster and
forces v=w exactly. If w reduces to 3, this equality is not forced.

For (4,6,3,12), the root 1 has residue multiplicity two and 4 has
multiplicity three. The H15 witness u reduces to 1 or 2; the H3
witness v reduces to 2, which is simple. If u reduces to 2, then
u=v exactly. If u reduces to 1, multiplicity two alone does not
force u=1. The H1 witness w reduces to 1 or 4. If w reduces to 1,
the repeated exact root exhausts that cluster, forcing w=1 and
also u=1 whenever u reduces to 1.

Thus, after excluding the d=0 coefficient point, the six marked
residue assignments are

| v residue | u residue | w residue | Forced exact relation |
|---:|---:|---:|---|
| 2 | 1 | 1 | u=w=1 |
| 2 | 1 | 4 | None from cluster cardinality alone |
| 2 | 2 | 1 | u=v and w=1 |
| 2 | 2 | 4 | u=v |
| 11 | 1 | 3 | u=1 |
| 11 | 1 | 11 | u=1 and v=w |

Grouped by their high-derivative coincidence, these are three
exact-collision branch classes and one remaining class
(v,u,w)=(2,1,4) in which the H16 and H15 roots can be distinct
inside a double cluster while the H1 repeated root lies in a
triple cluster. This is the unresolved cluster branch. The residue
data neither assert that a characteristic-zero lift exists nor show
that one would have to be ramified: distinct roots with the same
residue can occur in unramified fields as well. Any exclusion must
also allow arbitrary ramified valued extensions.

None of the forced equalities alone contradicts the full CA system.
The missing bridge is either an exclusion of these exact-collision
systems and the remaining cluster class, or a stronger valuation
identity controlling their possible ramification. Merely testing
unramified lifts cannot handle the last case without an additional
argument.

## 5. The divided middle derivative does not immediately help

At (4,6,3,12), normalized coefficients a4,a5 reduce to 12,4, so
the monic divided derivative at deficiency 10 is

    G10(X)=X10+11X6+7X5+a10.

The invisible normalized coefficient a10 may be chosen so G10
vanishes at a selected nonzero seed root: at root 1, take a10=7.
This avoids relying on a middle-derivative witness at the simple
zero root, which could not lift when C and E are both nonzero.
All off-support divided
derivatives have zero constant term and are witnessed at zero.
Retaining these reduced equations alone does not eliminate the
bad seed. More information about lifts or the exact branch
equations is required.

The bounded follow-up gives valuation restrictions and an exact
certificate-backed classification, but does not establish the
seven-term bound.
