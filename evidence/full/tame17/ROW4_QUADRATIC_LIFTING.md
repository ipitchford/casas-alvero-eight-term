# Row 4: a complete quadratic lifting reduction

23 September 2026. This is a finite local description of the whole row-4
branch, including arbitrary ramification. It does not exclude the branch.
The final repeated-root equation remains untested across the marked charts.

## Statement

Use the exact normalization already proved in `../LIFT_CONSEQUENCES_17.md`:

    a0=1, a1=a20=0, a2=-1, a3=a17=0, f(1)=0,
    f(X)=sum binom(20,j) a_j X^(20-j).

Its reduction is

    h=X20-3X18+11X2+8X.

Let K be the unramified extension of Q17 of degree four. Every hypothetical
characteristic-zero CA polynomial in this normalized branch, together with
all its roots, lies in an extension of K of degree at most two. Thus its
absolute local degree is at most eight and its ramification index is at
most two. This is a conclusion, not an assumption on the original point.

More precisely, finitely many signed marked residue charts cover all such
points. Each chart has a monic quadratic W(Z) over the integer ring A of K,
with W mod17=Z2. At each of its at most two distinct roots, all coefficients
and selected witness candidates are determined by convergent integral power
series. One further exact scalar equation decides whether the point is CA;
when it holds, all polynomial roots are given by the displayed functions.

There are 18 distinct residue roots. A crude covering bound is
2*19^13 signed charts: choose which of two double clusters supplies the
Hasse-first-derivative witness, then choose for each middle derivative one
of the 17 other residue classes or either sign in the remaining double
cluster. Duplicate charts and coincident roots cause no coverage problem.
This count is not an enumeration and is not a tractability guarantee.

## 1. Fixed residue data and visible equations

The exact factorization in F17[X] is

    h=X(X+7)(X+11)(X+16)(X2+3X+3)^2
      *(X4+3X3+4X2+2)
      *(X4+12X3+14X2+5X+14)
      *(X4+13X3+16X2+4X+11).

The quadratic and three quartics are irreducible. Consequently the entire
residue root set splits over E=F_(17^4). Write alpha,beta for the two roots
of X2+3X+3. They are the only multiple residue roots, each of multiplicity
two. Zero and one are simple. The Hasse-second-derivative common witness
has the unique residue six; the Hasse-first-derivative witness lies in
one of the two double clusters. Choose alpha to denote that cluster.
An actual repeated root exhausts its size two, so every actual root in
the alpha cluster coincides at one exact double root.

Put u_j=a_j for 4<=j<=16 and C_j=binom(20,j). Introduce s for the
Hasse-second-derivative witness. The equations G18(s)=0 and f(1)=0 give

    a18=-s18+153s16-sum_{j=4}^{16} binom(18,j) u_j s^(18-j),
    a19=(189-sum_{j=4}^{16} C_j u_j-190a18)/20.

The denominator is a 17-adic unit. Call the resulting polynomial F(u,s;X).
Its reduction, with s still variable, is

    X20-3X18-3s18 X2+(2+3s18)X.

Every partial derivative with respect to a u_j is coefficientwise divisible
by 17. At s=6 the last display equals h. In the equation F(u,s;s)=0 the
total s derivative is 9 modulo 17: its argument derivative is h'(6)=5
and its parameter derivative is 4. Thus this equation uniquely solves
s=S(u) locally, even over ramified ambient extensions.

## 2. Integral analytic functions on a marked coefficient chart

Fix all middle witness residues. The triangular equations

    G_j(w_j)=0,  4<=j<=16,

determine the coefficient residues ubar_j in E. Work over A=W(E), the
integer ring of K, on the formal residue chart

    B=A[[U4,...,U16]],  u_j=tilde(ubar_j)+U_j.

Here each U_j is to be evaluated at a positive-valuation element; it is
not assumed divisible by 17. The implicit function S exists over B and
has reduction identically six. Define F_u(X)=F(u,S(u);X). Its reduction
is identically h over E[[U]], not just at U=0. All coefficient derivatives
with respect to u vanish modulo 17.

Every simple residue root gamma has a unique root function P_gamma(u)
of F_u, with constant reduction gamma. In particular P_0=0, P_1=1 and
P_6=S. The critical equation G19(R)=F_u'(R)/20=0 uniquely defines
R_alpha(u) reducing to alpha, because

    H2 h mod (X2+3X+3)=3,
    (d/dR)G19(R) at alpha = 2*3/20 = 2 mod17.

Every one of these functions has all u derivatives zero modulo 17.
The equation F_u(R_alpha(u))=0 is deliberately omitted at this stage.

Hensel factorization separates the beta cluster from all other roots:

    F_u(X)=Q_beta(u;X) V(u;X),
    Q_beta mod17=(X-beta)^2,
    gcd((X-beta)^2, V mod17)=1.

Since 2 is a unit, write uniquely

    Q_beta(u;X)=(X-c(u))^2-d(u).

The reductions satisfy c(u)=beta and d(u)=0 identically over E[[U]].
In particular d belongs to 17B; this is a coefficientwise formal identity,
stronger than merely knowing d has positive valuation at a particular point.

## 3. One parameter covers both roots of the unresolved cluster

Introduce a parameter z of positive valuation. For each middle witness
choose the following expression:

- P_gamma(u) if its residue gamma is simple;
- R_alpha(u) if its residue is alpha;
- c(u)+epsilon_j*z, epsilon_j in {+1,-1}, if its residue is beta.

The signs are chosen independently for each witness. There is one shared z,
so this includes assignments using both roots of the beta cluster as well
as assignments using only one. We also retain z when no witness uses that
cluster, in order to describe all roots of the resulting polynomial.

Impose the thirteen middle equations G_j(w_j(u,z))=0. At z=0 their
Jacobian with respect to u is lower triangular with diagonal one modulo
17. Indeed the root functions have zero u derivatives modulo 17, G_j
depends directly only on coefficients through u_j, and its coefficient
of u_j is one. The equations at z=0 therefore have a unique lift u* in
A of the prescribed residue vector. The formal implicit function theorem
then gives a unique integral series vector

    u=u(z) in A[[z]]^13,  u(0)=u*.

The series converge whenever z has positive valuation. Their coefficients
are integral, and all substitutions into B are valid because u(z) has the
prescribed residue at such z. Modulo 17, u(z) need not be constant; the
argument does not impose this incorrect extra restriction.

The beta-root equation is now exactly

    P(z)=z^2-d(u(z))=0.

Because d is coefficientwise divisible by 17 before substitution,

    P(z) mod17=z^2 in E[[z]].

Weierstrass preparation over the complete DVR A therefore gives

    P(z)=V(z) W(z),
    W(z)=z^2+Bz+C,  B,C in 17A,

where V is a unit in A[[z]]. At every positive-valuation z, V(z) is a
unit, so P(z)=0 if and only if W(z)=0. All roots of W have positive
valuation (with zero allowed). Their fields over K have degree at most
two. Evaluating the integral power series in such a finite, hence complete,
extension keeps every coefficient and displayed witness candidate inside
that extension. The alpha candidate becomes a polynomial root only after
the remaining scalar equation is imposed.

## 4. Coverage of actual ramified points and the remaining equation

Take any actual CA point, with no assumption on ramification. Its H1
witness chooses alpha, and its middle witnesses determine a marked chart.
The separated beta cluster has two roots c+z,c-z; choose one labeling.
Then each selected witness in that cluster has one of the two prescribed
signs, including when z=0. Hensel factorization and simple-root uniqueness
identify the functions above with the actual coefficients and roots.

For completeness, uniqueness of the implicit u solution is also valid in
an arbitrary ramified extension: with z fixed, the Jacobian remains
integral and invertible modulo the maximal ideal. If two solutions with
the same residues differed, the linear term in their difference would
preserve its minimum valuation, whereas all nonlinear terms would have
strictly greater valuation. They cannot cancel. This applies to S and
the critical/simple root functions as well. Thus the actual point is
u(z), and z is a root of W. No ramified solution is discarded by choosing
the unramified coefficient ring for the series.

The remaining scalar equation is

    F_{u(z)}(R_alpha(u(z)))=0.

If it holds, the critical equation makes R_alpha an exact double root;
the residue multiplicity prevents higher multiplicity. The alpha cluster
has then collapsed, and the other roots are precisely the simple root
functions and c(u(z))+/-z. All lie in the same extension of K of degree
at most two.

Conversely, W(z)=0 and this extra scalar equation supply every missing
root incidence: the fixed normalization handles G1,G2,G3,G17, the
equations defining S handle G18, the middle equations handle G4 through
G16, and the critical equation plus the scalar equation handle G19.
This proves the stated complete finite local reduction. It does not
establish that the extra equation fails for all signed charts.

## Evidence and scope

`check_row4_quadratic_constants.py` independently checks the factorization,
irreducibility, Hasse gcds, splitting-field degree, parameter divisibility,
and Jacobian constants using standard-library finite-field arithmetic.
The implicit-function, factorization, convergence and Weierstrass arguments
are mathematical proofs above, not consequences of finite sampling.
The separate `ROW4_QUADRATIC_AUDIT.md` records independent internal review.
No external validation, novelty priority, or whole-row exclusion is claimed.
