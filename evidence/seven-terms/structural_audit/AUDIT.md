# Independent audit of the C valuation exclusions

23 September 2026. Internal mathematical and arithmetic review. Producer
files were read and replayed but not edited.

**Verdict: the exact `u=1` exclusion and the residue-row `(v,u,w)=(2,1,4)`
exclusion are valid under their stated hypotheses, including arbitrary
ramification. The final integrated coverage review in Section 6 also
passes.** I found no gap in the reviewed valuation arguments or assembly.
The independent arithmetic audit of the separate `u=v` exclusion belongs
to its assigned reviewer. This is not external peer review or a novelty
verdict.

The reviewed drafts are `../u_one/JET_PROOF.md` and `../cluster/PROOF.md`.
The underlying residue classification and forced cluster equalities were
already audited in `../../casas-alvero-sixterm/reviews/C_AUDIT.md`.

## 1. Exact scope and normalization

The polynomial is

\[
 f=X^{20}-4845X^{16}+BX^{15}+CX^{10}+DX^3+EX,
\]

with all roots integral at a valuation extending the 13-adic valuation,
normalized by \(\nu(13)=1\), and with \(f(1)=0\). In the full-support
application all five displayed lower coefficients are nonzero in
characteristic zero. The normalization sets an order-16 common root to 1,
so \(A=-\binom{20}{16}=-4845\) exactly. An order-15 witness \(u\) satisfies

\[
 B=15504(5u-u^5),\qquad E=4844-B-C-D.
\]

In particular \(u=1\) gives \(B_0=62016\). All these identities follow
directly from the Hasse derivatives; they do not follow merely from
reduction modulo 13.

The bound \(\nu(C)\ge1\) is legitimate. It follows from the previously
proved integrality of binomial-normalized CA coefficients, or directly
from any integral order-10 common root \(z\):

\[
C=-184756z^{10}-8008Az^6-3003Bz^5\in13\mathcal O.
\]

Each displayed integer is divisible by 13. Thus the proofs never replace
an arbitrary positive valuation by an unjustified integer lower bound.

## 2. The unit-Jacobian estimate

The following elementary lemma is sufficient; a global finiteness or
specialization theorem is unnecessary here.

Let two integral polynomial equations vanish at small unknowns \(x,y\)
and small parameters. Suppose the constant defects and parameter terms
have valuation at least \(a>0\), and the linear Jacobian in \((x,y)\)
is invertible over the valuation ring. Then

\[
\min\{\nu(x),\nu(y)\}\ge a.
\]

Indeed, if the minimum \(m\) were smaller than \(a\), the linear part
would have minimum valuation exactly \(m\): both the matrix and its
inverse are integral. The constant/parameter terms have greater
valuation, and nonlinear terms have valuation at least \(2m>m\).
The equations cannot then vanish. The proof also covers vanishing
differences by setting their valuation to infinity. It does not require
completeness, discreteness, unramifiedness, or a prime-field residue field.

For \((f(v),H_3f(v))\), after eliminating \(E\), the Jacobian in
\((v-r,D-d_0)\) is

\[
\begin{pmatrix}9&6\\4&1\end{pmatrix}
\quad\text{at }(r,d_0)=(2,3),\qquad
\begin{pmatrix}0&7\\4&1\end{pmatrix}
\quad\text{at }(11,10).
\]

Both determinants are 11 in characteristic 13. These are Jacobians of
the actual equations, including the dependence of \(E\) on \(D\).

## 3. The row with a potentially distinct order-15 root near 1

For the row \((\bar v,\bar u,\bar w)=(2,1,4)\), put
\(s=u-1\), \(\beta=B-B_0\), \(\delta=v-2\), and \(\eta=D-3\).
The exact identity is

\[
\beta=-15504s^2(10+10s+5s^2+s^3).
\]

The parenthesis and 15504 are units. Hence, for \(s\ne0\),
\(\nu(\beta)=2\nu(s)\). The preceding Jacobian estimate gives

\[
\min\{\nu(\delta),\nu(\eta)\}\ge
\min\{1,\nu(\beta),\nu(C)\}.
\]

The expansion at 1 is independently confirmed as

\[
f'(1)=13\cdot61198+14\beta+9C+2\eta,
\qquad H_2f(1)\equiv9.
\]

If \(0<r=\nu(s)<1\), then \(\nu(f'(1))\ge\min(1,2r)>r\).
In

\[
0=(f(1+s)-f(1))/s=f'(1)+H_2f(1)s+H_3f(1)s^2+\cdots,
\]

the second term has valuation exactly \(r\), and every other term has
larger valuation. This is impossible. Consequently \(\nu(s)\ge1\),
or \(s=0\); in either event \(\beta\in13^2\mathcal O\) and
\(v-2,D-3\in13\mathcal O\). This argument allows fractional
valuations and does not assume that distinct roots in one cluster
require ramification.

Now write \(C=13S,v=2+13R,D=3+13T\). All three new variables are
proved integral. The first two reduced equations are

\[
12+9R+8S+6T=0,\qquad6+4R+7S+T=0.
\]

For \(\tau=w-4\), the constant and linear coefficients in the Taylor
expansion of \(f'(4+\tau)\) have valuation at least 1, while its
quadratic coefficient is 2 modulo 13. If \(0<\nu(\tau)<1/2\), that
quadratic term is uniquely of least valuation. Therefore
\(\nu(\tau)\ge1/2\), also allowing \(\tau=0\). The Taylor expansion
of \(f(4+\tau)=0\) then gives \(\nu(f(4))\ge3/2>1\): the first
two Taylor coefficients lie in \(13\mathcal O\), and later powers
have order at least \(3\nu(\tau)\). Thus the third equation

\[
1+5S+8T=0
\]

is warranted even for ramified extensions. It forces
\((R,S,T)=(5,12,7)\).

## 4. The exact u=1 rows

When \(u=1\), \(\beta=0\) exactly and the Jacobian lemma immediately
proves \(v-r,D-d_0\in13\mathcal O\). Put
\(C=13S,v=r+13R,D=d_0+13T\). The first jets for the second residue
polynomial, \((r,d_0)=(11,10)\), are

\[
2+12S+7T=0,\qquad3+4R+6S+T=0.
\]

If \(\bar w=3\), its simple root in \(\overline{f'}\) and the
integral-order coefficient defects force \(\nu(w-3)\ge1\). Since 3
is a double root of \(\bar f\), \(f(w)/13\) gives \(9+11T=0\).
If \(\bar w=11\), the repeated exact root \(w\) consumes both
positions in that residue cluster, so \(v=w\). The additional
first-derivative equation gives \(7+R+S+11T=0\).

For the two \(\bar v=2\) cases, \(\bar w=4\) uses the preceding
half-valuation argument. If \(\bar w=1\), the double residue cluster
contains the exact root 1 and the repeated exact root \(w\), so
\(w=1\). Its derivative equation is \(7+9S+2T=0\).

Thus all four linear systems and their consequences are:

| \((\bar v,\bar w)\) | Additional equation | \((R,S,T)\) | Constant in reduced \(G_{10}\) | gcd with \(\bar f\) |
|---|---|---|---:|---|
| \((2,1)\) | \(7+9S+2T=0\) | \((1,0,3)\) | 0 | \(X\) |
| \((2,4)\) | \(1+5S+8T=0\) | \((5,12,7)\) | 4 | 1 |
| \((11,3)\) | \(9+11T=0\) | \((8,1,11)\) | 9 | 1 |
| \((11,11)\) | \(7+R+S+11T=0\) | \((0,5,6)\) | 6 | 1 |

Here

\[
G_{10}=H_{10}f/184756,
\qquad\overline{G_{10}}=X^{10}+11X^6+7X^5+9S.
\]

The denominator has valuation exactly 1, and the numerator coefficients
have valuation at least 1. The displayed monic polynomial is therefore
integral. In the possibly distinct-\(u\) row, \(B-B_0\in13^2\mathcal O\)
gives the same reduction; no exact equality \(B=B_0\) was assumed there.

Each gcd 1 rules out a common root in every residue extension. In the
gcd \(X\) case, an order-10 common root must reduce to 0. Since
\(\bar f'(0)=12\), any such root \(z\ne0\) would make \(f(z)/z\)
a unit, a contradiction. Thus \(z=0\) and \(C=H_{10}f(0)=0\),
contrary to the exact-support hypothesis. This last step is why that
case is an exact-support exclusion rather than a statement excluding
every coefficient degeneration.

## 5. Independent arithmetic and boundaries

I wrote `check_independent_jets.py` from the integer polynomial and
binomial Hasse formula without importing any producer arithmetic or
certificate. It reconstructs the normalizations, the \(B\) expansion,
Jacobians, Taylor constants, all four linear systems, and the normalized
middle derivative. A separately written extended Euclidean algorithm
returns and directly verifies the four Bezout identities. The output
is `independent-jets.json`. Normal and optimized Python runs both pass;
all checks use explicit exceptions and remain active with `-O`.

I also read and ran both producer `check_jets.py` scripts in normal and
optimized modes. Both pass, and their arithmetic agrees with the
independent reconstruction. The valuation inequalities were reviewed
mathematically; finite arithmetic replay is not a substitute for them.

The original `u=w=1` one-parameter resultant formulas also check:

\[
f=X^{20}-4845X^{16}+62016X^{15}+2tX^{10}
  +(-397784-9t)X^3+(340612+7t)X.
\]

They follow from \(f(1)=f'(1)=0\). For exact C the order-3 and order-10
witnesses are nonzero, so the two resultants with \(f/X\) must vanish.
The logged coprime characteristic-zero resultants are a separate
computational route; I have not independently certified those large
integer resultants here. The compact jet proof already independently
settles that row, so no conclusion in this audit depends on that log.

At the initial branch-review stage, this established the two stated
branch exclusions. Final C closure required the separately assigned `u=v` branch and the
exhaustiveness of the prior residue classification. A seven-total-term
bound additionally requires the earlier global support enumeration and
A/B exclusions. Unrestricted degree 20 and the full Casas–Alvero
conjecture are outside these conclusions. Prior-art coverage and the
unresolved ProofAtlas overlap lead are not settled by this audit.

## 6. Final integrated coverage review — PASS

I subsequently read `../PROOF.md` and the completed
`../u_equals_v/JET_PROOF.md`, and compared the former with the frozen
six-term frontier proof `../../casas-alvero-sixterm/PROOF.md` and its C
classification. This is an assembly and mathematical-implication review;
the independent arithmetic audit of the `u=v` producer belongs to its
separate reviewer.

The integrated argument covers every required normalization and branch:

1. Integral roots give integral ordinary coefficients. The exact order-10
   equation gives the stronger bound \(C\in13O\) directly. The unit-root
   normalization prevents monomial reduction.
2. The \(A\)-unit argument accounts for the \(a=e=0\) reduced
   degenerations. Its order-16 witness is a unit, so the later normalization
   to 1 preserves integrality and support.
3. The complete coefficient classification is invoked over an algebraically
   closed residue extension. The middle coefficient point is excluded by a
   least-valuation argument that covers all three of its marked assignments,
   including both quadratic extension-field witnesses.
4. The remaining six rows map to proofs without a missing equality case:
   rows 1, 5, and 6 to the exact `u=1` proof; row 2 to the general cluster
   precision proof, whether or not \(u=1\); and rows 3 and 4 to `u=v`.
5. The `u=v`, \(\bar w=1\) proof applies the precision lemma twice. The
   second application is justified because the substituted exact equations,
   divided by 13, are integer-coefficient polynomials whose reductions are
   the displayed affine linear system with invertible matrix. Thus the
   upgrade from \(\bar k=3\) to \(k-3\in13O\) is valid. It implies
   \(G(4)\in13O\), then \(z-4\in13O\), and finally the contradiction
   between \(f(4)\in13^2O\) and \(\overline{f(4)/13}=6\). There is no
   hidden integer-valuation assumption in this step.
6. The theorem is an exclusion of exact C support. The frozen preceding
   theorem says any exact centered six-term counterexample must have C
   support, while the earlier lower bound already excludes fewer than six
   terms. Together these statements give at least seven centered nonzero
   monomials, including the leading term, for any nontrivial degree-20 CA
   polynomial. They do not prove unrestricted degree 20 or the full
   conjecture.

No mathematical correction was requested in this final assembly review.
I recommended renaming the residue field \(k\) to \(\kappa\), because
the coefficient parameter \(C/13\) is also named \(k\); this is a
notation clarification, not a proof gap. Exact replay, internal audit,
historical novelty, external review, and publication significance remain
separate claims.

Final readback: the integrated proof now uses \(\kappa\) for the residue
field in its definition and in equation (9). The notation point is
resolved. No proof or coverage correction remains from this review.
Historical-priority uncertainty, in particular the unretrieved ProofAtlas
source material, remains explicitly open.
