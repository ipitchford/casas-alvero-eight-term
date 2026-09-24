# Introduction

A polynomial over a field of characteristic zero is a Casas–Alvero polynomial if it has a common zero with each of its derivatives of orders one through one less than its degree. The Casas–Alvero conjecture asserts that every such polynomial is a power of a linear polynomial. This paper concerns coefficient supports in degree twenty. It does not prove the conjecture in that degree or in arbitrary degree.

Translate the zero of the nineteenth derivative to zero and make the polynomial monic. The resulting centered polynomial has the form
\[
f(X)=X^{20}+\sum_{j\in S}c_jX^{20-j},\qquad S\subseteq\{2,\ldots,19\},\quad c_j\ne0.
\]
The absence of the constant term follows from the Casas–Alvero condition for the nineteenth derivative. We count the leading monomial, so the total number of terms is \(|S|+1\). A bound on this number concerns the centered polynomial, not all of its translates.

Our principal result is that a nontrivial centered degree-twenty Casas–Alvero polynomial has at least seven terms. A support sieve leaves five exact six-term families. Four admit relatively short exclusions. The remaining family
\[
X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,\qquad ABCDE\ne0,
\]
is excluded by a complete characteristic-thirteen residue classification and explicit lift obstructions. The argument includes residue-zero nonzero coefficients and ramified ambient extensions; neither may be discarded in a reduction argument. The detailed proof below supplies the finite identities and the route from them to the characteristic-zero conclusion.

Earlier work supplies much of the framework. The prime-adic constraints and determinant restrictions of Castryck, Laterveer and Ounaïes [CLO], the sparse criteria of de Frutos Marín [deFrutos], and the shared-derivative restrictions in Massri [Massri] provide the predecessor context. The proof below identifies which restrictions it actually imports; Massri's additional support filter is redundant in the final small-support sieve. Their combination already implies the weaker five-term bound; we do not claim that bound as new. The singleton and two-visible-coefficient criteria are likewise older results. Marashdeh [Marashdeh] gives related support and triangular-elimination methods. Our new burden is the specific exclusions beyond those criteria, not a claim to have introduced valuation methods or Hensel lifting.

The final six-term family is not eliminated directly by the older singleton/two-visible-coefficient test at any prime: at primes \(2,3,5,17,19\), an allowed singleton degeneration has binomial coefficient congruent to one; at primes \(7,11,13\), at least four positions are visible; and at every prime greater than twenty, all five are visible. This explains why inspecting only the finite-field support is insufficient. The lift calculation uses derivative information lost by reduction.

We also record a further reduction of the seven-term support frontier, and a marked factorization theorem for the local resultant algebra of one characteristic-seventeen branch. The latter preserves multiplicities and identifies the remaining scalar obstruction, but does not prove that it is always nonzero. The previously certified exclusions of 79 of 240 canonical supports in that branch remain partial coverage. No surviving finite-field configuration is asserted to lift to a Casas–Alvero polynomial.

The evidence archive distinguishes the final proof path, executable finite checks, historical exploratory material, and external review records. The paper is a computer-assisted mathematical manuscript for review, not a proof-assistant-certified result. Literature comparison found no direct predecessor of the seven-term theorem in the inspected sources, but two specific overlap questions remain unresolved: the exact systems behind ProofAtlas's reported degree-twenty work and the unavailable full text of Shih, Cheng-Pang's 2022 thesis. These limits are documented rather than treated as novelty clearance.
