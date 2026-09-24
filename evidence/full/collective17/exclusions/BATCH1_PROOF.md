# Seven complete canonical systems are excluded

23 September 2026. This is a completed first batch within the 240-system
row-9 cover. It excludes all seven systems with at most four active middle
indices, including every algebraic residue witness and every coefficient
degeneration. It does not exclude the other 233 systems or solve degree 20.

## Exact hypotheses and coverage

Use the exact row-9 normalization and integer polynomials f, g, G_j, T
from `../elimination/FINITE_FLAT_REDUCTION.md`. Write q=g/X, a monic
polynomial of degree 17. For a fixed active middle set J, set every
inactive u_j to zero. Every actual candidate with that support admits a
marking in which active derivative witnesses are nonzero. The simple mean
residue cluster contains only the exact root zero; consequently an active
coefficient cannot use a witness reducing to zero. This argument does
not say that an active coefficient must have nonzero residue.

Modulo 17, q is fixed, squarefree, and splits over F_(17^10). The native
replay proves irreducibility of the displayed degree-ten defining
polynomial by Rabin's criterion. It then checks seventeen distinct,
nonzero, simple roots of the monic degree-17 q. These are all its roots
over the algebraic closure, not merely a search over prime-field points.

At an active index j with witness rho_j the normalized derivative gives

    u_j = -rho_j^j + binom(j,3) rho_j^(j-3)
          - sum_{i in J, i<j} binom(j,i) u_i rho_j^(j-i).

Thus each of the 17^|J| marked assignments determines its residue
coefficients uniquely. For inactive indices zero is a common witness
automatically. The enumeration visits the complete Cartesian product in
lexicographic order and tests the exact first residue of T. No coefficient
is rejected because its residue is zero, and no distinctness condition is
placed on selected witnesses.

## Complete first-residue results

| Active middle indices J | Markings | T=0 residue markings | Frobenius orbits | Final result |
|---|---:|---:|---:|---|
| 4,10,13 | 4,913 | 1 | 1 | Excluded at precision 17^3 |
| 4,5,12,15 | 83,521 | 1 | 1 | Excluded at precision 17^2 |
| 4,7,10,15 | 83,521 | 0 | 0 | Excluded modulo 17 |
| 4,9,10,12 | 83,521 | 0 | 0 | Excluded modulo 17 |
| 4,9,10,14 | 83,521 | 17 | 4 | Excluded at precision 17^2 |
| 5,12,15,16 | 83,521 | 1 | 1 | Excluded at precision 17^2 |
| 10,11,15,16 | 83,521 | 0 | 0 | Excluded modulo 17 |

The sum is 506,039 markings. The four orbits for J={4,9,10,14} have
sizes 10, 1, 5, and 1. In particular the earlier single degree-five orbit
was not mistaken for the complete support calculation.

## The uniform square system and arbitrary ramification

For a surviving marking, use one variable x_r for each distinct residue
root selected. The normalized derivative equations determine every
active u_j recursively as an integer polynomial in these root variables.
Substitute those expressions into q, and impose

    q_u(x_r)=0 for each distinct selected root r.

This is a square system. All coefficients of q_u which depend on u are
divisible by 17, since the same holds for f and division by X(X-1)^2
uses integer polynomial identities. Therefore its reduced Jacobian is
diagonal, with entries q_bar'(r), all nonzero. The system has a unique
unramified lift of its residue point by Hensel's lemma.

Using one variable for repeated residue choices is valid: q_bar is
squarefree, so q has only one root in each residue class. Equivalently,
two such roots with the same reduction cannot differ, by their simple
root Taylor expansion. The root near residue one is treated uniformly
as a q-root in this square system. It is not fixed equal to one before
T=0 has been imposed. This avoids dropping a condition when lifting the
resultant presentation.

Here is the precise finite-precision implication, including ramified
extensions. Let x_tilde be the saved approximation, satisfying the
square system modulo 17^n, and suppose x is any exact integral solution
with the same reduction. Normalize the valuation by v(17)=1. If their
difference has minimum valuation gamma>0, the unit Jacobian preserves
that valuation in the linear Taylor term. The error at x_tilde has
valuation at least n, and nonlinear terms have valuation at least
2 gamma. Cancellation forces gamma >= min(n,2 gamma), hence gamma>=n.
The case x=x_tilde requires no argument. Therefore the exact value of
the integer polynomial T differs from its saved value by an element of
valuation at least n. A saved nonzero T of valuation less than n rules
out every exact solution, including solutions in ramified extensions.

The field polynomial defines an unramified degree-ten extension because
its residue is irreducible and separable. Its Frobenius automorphism
permutes the residue markings as recorded. The square equations and T
are defined over the 17-adic integers, so conjugation preserves their
solutions and the valuation of T. One representative certificate thus
excludes the full recorded Frobenius orbit. The replay explicitly checks
that these disjoint orbits cover all twenty residue survivors.

## Precision certificates and independent replay

For J={4,10,13}, T is zero modulo 17^2 but equals 3179=11*17^2
modulo 17^3. Every other surviving orbit has T of valuation exactly one.
`lift-batch.json` records all approximate roots, recursively derived
coefficients, simple Jacobian entries, and divided-H2 residues.

`enumerate_batch.py` uses FLINT field arithmetic. The separate native
`replay_residues.cpp` uses ten-coordinate integer arithmetic and fixed
linear multiplication matrices; it re-enumerates all 506,039 assignments
and returns exactly the same complete survivor lists. `check_batch.py`
binds the native input to the saved field/root/support data, rebuilds
the native executable from its source, and runs it with an external wall
guard. It independently checks irreducibility, the complete root domain,
the Frobenius permutation, and orbit coverage.

For precision replay, that checker imports neither producer. It solves
the low coefficients from f(1)=f'(1)=0, reconstructs q by ascending
coefficient division, and checks every claimed root equation. It computes
H2 f(1) directly at one extra digit and divides by 17, independently of
the producer's saved linear formula for T. The degree-five orbit agrees
with the earlier single-scenario certificate after the field embedding.
Normal and optimized runs give identical PASS receipts.

This is a reproducible computer-assisted exclusion with an explicit
coverage and valuation argument. It is not a formally verified proof.
The remaining systems in the cover require their own complete checks.
