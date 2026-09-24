# Independent audit: row-4 quadratic lifting reduction

23 September 2026. **PASS for the theorem about actual Casas–Alvero points and the complete signed-chart reduction.** Row 4 is not excluded. The statement-level qualification described below was applied to the producer's text and its corrected statement was read back during this audit.

Reviewed `ROW4_QUADRATIC_LIFTING.md`, the inherited exact normalization in `../LIFT_CONSEQUENCES_17.md`, and `check_row4_quadratic_constants.py`. The audit checks the analytic and coverage argument independently of the finite arithmetic replay.

## Constants and normalization

The row has `a2=-1,a3=a17=0`, with exact roots 0 and 1, and residue

    h=X^20-3X^18+11X^2+8X.

The eliminations of `G18(s)=0` and `f(1)=0` give exactly the displayed formulas for a18 and a19. Both parameter-derivative families are divisible by 17 while s is independent. At s=6 the residue is h. Independently computing the total derivative of `F(u,s;s)` gives

    h'(6)=5,  a18_s=-6,  a19_s=6 (mod 17),
    5+190*(-6)*6^2+20*6*6 = 9 (mod 17).

Also `H2 h` has remainder 3 modulo `X^2+3X+3`, so the critical-root derivative is `2*3/20=2 (mod 17)`. These are the required units. The checker verifies the full factorization into four linear factors, a squared irreducible quadratic, and three distinct irreducible quartics. Thus h has 18 distinct roots and splitting field E=F_(17^4). Its gcds with H1 and H2 are respectively the quadratic and X-6.

The normalization concerns local coefficients and roots after the permitted affine changes. The resulting degree bound is local, not a bound on the global degree of a number field of coefficients.

## Formal coefficient charts are legitimate

For any chosen residue witnesses, the thirteen normalized equations determine the middle coefficient residues successively, because a_j has coefficient 1 in G_j. All residues lie in E. Choose lifts of this finite residue vector to A=W(E), and write u=tilde(ubar)+U in B=A[[U4,...,U16]]. Every actual U has positive valuation, possibly fractional; it need not belong to 17 times its ambient valuation ring.

The reduced equation defining S is independent of U and has the simple root 6. Hensel lifting over B gives a unique integral S whose reduction is identically 6 as a series in E[[U]]. Consequently F_u has reduction identically h. This coefficientwise statement is stronger than an assertion only at U=0, and is essential here.

The simple-root functions and the critical function R_alpha have constant reductions and therefore all their U derivatives are divisible by 17. Coprime Hensel factorization gives the unique monic degree-two factor for the beta cluster; its reduction is identically `(X-beta)^2`. Completing the square is legitimate because 2 is a unit. It gives c with constant reduction beta and **d in 17B coefficientwise**. There is no assumption that the beta cluster has already collapsed.

## Signed witnesses give full coverage

An actual H1 witness must reduce to alpha or beta. Call its class alpha. It is an exact repeated root, so it exhausts the size-two alpha residue cluster. Every selected witness reducing to alpha is therefore that same root, identified by the unique critical function R_alpha.

The other cluster can contain either two distinct roots or one double root. Its factor is exactly `(X-c)^2-d`; after choosing a labeling its two roots are c+z and c-z. A single common parameter z, together with independently chosen signs for all selected beta witnesses, covers both possibilities and every repeated selection. If z=0, duplicate signs are harmless. If no middle witness uses beta, adjoining an auxiliary z still covers the unused roots; omitting it gives unramified coefficients but would not by itself show that all roots are unramified.

Every other residue class is simple and has a unique root function. In particular the functions for 0, 1 and 6 are respectively the exact constants 0, 1 and S. No residue value such as 6 or beta is equated with an integer or a fixed characteristic-zero root without its defining equation.

The thirteen middle equations, after inserting these functions, have lower-triangular U Jacobian with diagonal 1 at the residue point. Dependence through each witness contributes zero modulo 17. Thus for a fixed signed residue chart there is a unique integral series u(z), with u(0) lifting ubar. Its reduction need not be constant as a series in z; the proof correctly does not require that.

## Convergence and arbitrary ramification

Integral power series in finitely many variables converge when every argument has positive valuation: terms of increasing total degree have valuations tending to infinity. Infinite coefficient sums arising from substitution also converge because each substituted U(z) lies in the ideal (17,z). This is the appropriate formal topology, even when the constant term of U(z) is nonzero and divisible by 17.

For any fixed actual z of positive valuation, there cannot be a different solution with the same coefficient residues in a ramified extension. If the minimum valuation of the difference of two solutions is r>0, an integral Jacobian with integral inverse preserves this minimum for its linear term. Every remaining Taylor term has valuation at least 2r. Cancellation is impossible. This argument also applies to the preliminary implicit functions. Integral divided Taylor coefficients suffice; no factorial invertibility or integer-valued valuation assumption is being used.

Thus the actual data are indeed evaluations of the selected integral series. This establishes coverage, rather than merely constructing unramified solutions alongside potentially missing ramified ones.

## Weierstrass preparation and the exact remaining condition

Substitution preserves coefficientwise divisibility of d, so

    P(z)=z^2-d(u(z)) is congruent to z^2 modulo 17 in E[[z]].

The standard Weierstrass preparation theorem over the complete DVR A gives a unit times a monic distinguished quadratic W. The exact version required here is stated in [Laurent Berger, *The Weierstrass preparation theorem and resultants of p-adic power series*, section 1](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf). Its coefficients below the leading term lie in 17A. The unit evaluates to a unit at every positive-valuation z, so no roots are introduced or lost there.

Each root z of W has degree at most two over K=Frac(A). The finite extension K(z) is complete; therefore evaluating the integral series leaves all coefficient values and displayed witness candidates in that same field. When the extra equation `F_u(R_alpha)=0` holds, the alpha cluster collapses exactly, and all actual polynomial roots are the simple-root functions, R_alpha, and c+/-z. The whole splitting field is then contained in K(z). Hence its degree over Q17 is at most eight and its ramification index is at most two.

**Candidate-point wording:** before `F_u(R_alpha)=0` is tested, R_alpha is only a critical point, and the polynomial's alpha cluster may still split. At an arbitrary root of W one may claim that coefficients and selected witness candidates are determined by the series; the claim that all polynomial roots have the displayed form is conditional on the extra equation. This qualification does not change the theorem for actual CA points.

The converse also has the required scope. The fixed normalization supplies G1,G2,G3,G17; S supplies both G18 and its root incidence; the middle equations and the beta-factor equation supply G4 through G16; and the critical equation plus the extra scalar equation supply G19 and its root incidence. No Hasse order is omitted.

There are finitely many charts: choose alpha in two ways, and then at most 19 marked choices per middle degree (the 17 non-beta classes plus two beta signs). Each chart has at most two distinct z values. The bound is only a covering count, with duplicates allowed. No enumeration of these charts, rejection of every candidate, or tractability assertion follows.

## Replay and review boundary

The finite checker was inspected and replayed with ordinary Python and `python3 -O`; both runs pass. Its explicit checks establish the arithmetic constants and finite-field factorization. Formal implicit functions, coprime factorization, series convergence, ramified uniqueness, Weierstrass preparation and complete witness coverage are the mathematical arguments audited above; they are not certified by finite sampling.

This is independent internal review of a complete local reduction for one whole branch. It is not an external validation, novelty determination, row-4 exclusion, unrestricted degree-20 proof, or proof in all degrees.
