# Casas–Alvero: uniform sparse-family obstruction

Research round completed 23 September 2026. Internal research candidate; not published or externally refereed.

For all but finitely many primes p>7, the only Hasse–Casas–Alvero polynomial of the form

\[
X^{p+7}+aX^{p+3}+cX^3+dX
\]

over the algebraic closure of F_p is the monomial. The exceptional primes lie among the divisors of an explicitly defined nonzero integer. The proof yields specified coefficient restrictions at every root of characteristic-zero CA polynomials of degrees (p+7)p^e.

Read [PROOF.md](PROOF.md) for the complete uniform theorem and [DECISION.md](DECISION.md) for the significance and continuation judgment. The result concerns the stated support, not all degree-p+7 polynomials. Neither the entire exceptional set nor the original conjecture is solved.

## Evidence

- [dynamics/DYNAMICS_AUDIT.md](dynamics/DYNAMICS_AUDIT.md): separate algebraic audit of normalization, denominators, all coefficient cases, and characteristic-zero transfer.
- [dynamics/bezout-mod11.json](dynamics/bezout-mod11.json): explicit certificate that the defining resultant is nonzero.
- [uniform/STRUCTURAL_BOUNDARIES.md](uniform/STRUCTURAL_BOUNDARIES.md): complete zero-coefficient classification, direct positive examples, and bounded-range refinement.
- [prior-art/REPORT.md](prior-art/REPORT.md): retrieved 2013 thesis, corrected attribution, exact overlap tests, and stated search limits. No external novelty certification.
- [sixterm](sixterm): exact degree-20 support enumeration and the separately audited additional characteristic-13 calculation.

## Replay

Run `python3 -B replay.py` from this folder. It needs Python's standard library only. It reconstructs the degree-72 polynomial from the integral norm, verifies the modulo-11 Bezout identity, checks coefficient boundaries and finite-field witnesses, repeats the support enumeration, and checks prior-art formula identities. All scripts run normally and with optimization enabled. A changed-coefficient negative control must fail. The frozen file manifest is checked before and after replay.

The 26,185-digit resultant is supplementary. `resultant_bound.py` recomputes it using SymPy 1.14; it is not needed to check the finiteness proof, and its complete factorization is not available. The main replay includes the independent direct gcd test of all 1,225 primes in 7<p<10000, without using that large integer.

Exact arithmetic checks support the accompanying proof; they are not formal proof certification, external peer review, or proof of historical priority. No publication or author outreach occurred in this round. Earlier research packages were left unchanged.
