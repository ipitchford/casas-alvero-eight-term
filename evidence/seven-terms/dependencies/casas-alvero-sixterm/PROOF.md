# A unique remaining centered six-term support in degree 20

## Statement and conventions

A polynomial is Casas–Alvero (CA) if it shares a root with each derivative of orders 1 through one less than its degree. In positive characteristic we use Hasse derivatives
\(H_k(\sum c_jX^j)=\sum_{j\ge k}\binom jk c_jX^{j-k}\).
In characteristic zero these have the same roots as the ordinary derivatives.

Centering means translating the unique root of the nineteenth derivative to zero. For a CA polynomial this is also a root of the polynomial. After making the polynomial monic, write
\[
f=X^{20}+\sum_{m\in S}c_mX^{20-m},\qquad
S\subseteq\{2,\ldots,19\},\quad c_m\ne0.
\]
There are \(|S|+1\) nonzero terms. This is a coefficient count, not a count of distinct roots or derivative witnesses.

**Theorem (internally audited research result).** If such a nonmonomial CA polynomial has exactly six terms, then
\[
S=\{4,5,10,17,19\}.
\]
Equivalently it has the form displayed in the README. The preceding six-term lower bound remains in force. We do not prove a seven-term lower bound.

## Inherited finite support reduction

The preceding round applied Lucas visibility, singleton and two-visible coefficient criteria, published placement restrictions, and the Castryck–Laterveer–Ounaïes determinant criterion to all \(\binom{18}{5}=8568\) centered six-term supports. The old criteria leave five supports:
\[
\{3,4,10,18,19\},\quad \{3,10,16,17,19\},\quad
\{4,5,10,17,19\},\quad \{4,10,12,17,19\},\quad
\{8,10,16,17,19\}.
\]
Two previously proved characteristic-13 seed exclusions remove the last two. They concern, respectively,
\(X^{20}+aX^{16}+cX^3+dX\) and
\(X^{20}+bX^4+cX^3+dX\), with all coefficients allowed to vanish.
Their characteristic-zero deficiency masks are
\[
T_0=\{4,8,9,10,11,12,17,19\},\qquad
T_1=\{8,9,10,11,12,16,17,19\}.
\]

The frozen proofs, their prior-art attributions, and replay code are bundled at:

- [First seed and six-term lower bound](dependencies/casas-alvero-extension/PROOF.md).
- [Second seed](dependencies/casas-alvero-structural/sixterm/LAST_MASK_PROOF.md).
- [Complete support-sieve report](dependencies/casas-alvero-structural/sixterm/REPORT.md).

The two-visible criterion is attributed to de Frutos Marín, Proposition 3.5.5 of her [2013 thesis](https://uvadoc.uva.es/bitstream/10324/3602/1/tesis367-130927.pdf). The determinant criterion is due to [Castryck, Laterveer and Ounaïes](https://arxiv.org/abs/1208.5404). The seed exclusions, rather than those established general techniques, are the candidate contributions of the preceding work.

## The two additional exclusions

Call the first three supports A, B, C, in their order above.

**A.** [The full proof](A/A_EXCLUSION_PROOF.md) excludes every characteristic-zero CA polynomial supported inside \(\{20,17,16,10,2,1\}\), except \(X^{20}\). Its characteristic-13 seed has exactly one normalized nonmonomial coefficient point:
\[
h_0=X^{20}+4X^{17}+X^{16}+4X^2+3X.
\]
The common roots for Hasse orders 17, 16, and 2 are all 1, and \(h_0'(1)=11\ne0\). Following valuation normalization, the corresponding characteristic-zero witnesses must coincide at 1. The resulting family is
\[
f=X^{20}-1140X^{17}+14535X^{16}+tX^{10}
 +(-1589350-45t)X^2+(1575954+44t)X.
\]
The order-10 and order-1 common-root resultants are coprime over \(\mathbb Q\); the \(t=0\) degeneration is separately excluded by the nonzero order-1 resultant. Seed classification, resultant identities, and all zero-coefficient charts have exact replay. [Independent internal audit](reviews/A_AUDIT.md).

**B.** [The full proof](B/PROOF.md) shows that the only characteristic-13 CA polynomial
\[
X^{20}+aX^{17}+bX^4+cX^3+dX
\]
is \(X^{20}\). A sparse polynomial unit certificate covers one exceptional chart. In the main chart, exact resultant identities imply
\[
U(u)C(u)R_3(u)+V(u)D(u)R_1(u)=(u+1)^{17},
\]
where the common-root conditions force the left side to vanish and the normalization guarantees \(u\ne-1\). The factors \(C,D\) retain the zero-coefficient cases. Valuation reduction excludes the larger characteristic-zero deficiency mask
\[
T_B=\{3,8,9,10,11,12,16,17,19\},
\]
which contains B. [Independent internal audit](reviews/B_AUDIT.md).

Removing A and B from the three-support frontier leaves exactly C. This proves the stated theorem.

## Why the reduction and collision steps are valid

For a nonmonomial characteristic-zero CA polynomial with zero as a root, extend the 13-adic valuation to a field containing its coefficients and roots. Scale a nonzero root of least valuation to 1. Every root is then integral and a unit root remains. Write
\(f=\sum_j\binom{20}{j}a_jX^{20-j}\).
Evaluation of the monic normalized derivative at an integral common root gives
\[
a_j=-\sum_{i<j}\binom ji a_i\beta^{j-i}.
\]
Induction proves all \(a_j\) integral. Hence a coefficient disappears in reduction whenever its binomial multiplier is divisible by 13; the common-root witnesses reduce as well. The retained unit root prevents a monomial reduction. This handles coefficient loss and does not assume that an arbitrary empty affine special fibre proves characteristic-zero emptiness.

For A, the highest active reduced coefficient is nonzero, so its marked derivative witness is a unit and can be rescaled to 1. If another root \(r\) reduces to that same simple root, write \(f=(X-1)g\). Synthetic division keeps \(g\) integral, while \(g(r)\) reduces to \(h_0'(1)\ne0\). Thus \(f(r)=0\) implies \(r=1\). This applies over ramified or nondiscrete valued extensions; completeness is unnecessary. The seed identities hold over any characteristic-13 field extension, including transcendental residue extensions.

## The remaining family C

For exact C support, normalize all roots integrally at 13 and then its Hasse-order-16 witness to 1. The proof in [ROOT_CLUSTER_NOTE.md](C/ROOT_CLUSTER_NOTE.md) justifies that this is a unit scaling. The reduced seed is
\[
h=X^{20}+4X^{16}+bX^{15}+cX^3+dX.
\]
[Replayed univariate identities](C/UNIVARIATE_CLASSIFICATION.md) prove that the complete coefficient possibilities are
\[
(b,c,d)=(6,3,12),\quad(6,2,0),\quad(6,10,5).
\]
This is a classification over every algebraically closed characteristic-13 field, not a search restricted to base-field coefficients. The middle point admits extension-field marked witnesses and must not be discarded merely because of that. A separate valuation argument excludes its characteristic-zero exact-support lifts: the lowest term in \(f'(w)-f(w)/w\) has uniquely least valuation at the forced nonzero root \(w\) reducing to zero.

For the other two coefficient points, let \(u,v,w\) witness Hasse orders 15, 3, and 1. The six possible residue assignments and forced exact equalities are:

| \(\bar v\) | \(\bar u\) | \(\bar w\) | Forced equality |
|---:|---:|---:|---|
| 2 | 1 | 1 | \(u=w=1\) |
| 2 | 1 | 4 | None from these cluster counts |
| 2 | 2 | 1 | \(u=v,\ w=1\) |
| 2 | 2 | 4 | \(u=v\) |
| 11 | 1 | 3 | \(u=1\) |
| 11 | 1 | 11 | \(u=1,\ v=w\) |

These are necessary conditions. Neither the rows with exact collisions nor the row without one have been eliminated in characteristic zero. In particular, the table does not establish that only one branch is unresolved. The order-10 condition and possible ramified root splitting remain part of the unsolved system.

## Certificate interpretation

Finite-field resultant polynomials are verified at more distinct extension-field points than their proved degree bounds. Polynomial identity then follows exactly; this is not probabilistic testing. The characteristic-zero resultants for A are verified by integer Sylvester determinants and a degree-preserving coprimality check modulo 101. Separate scripts reconstruct Hasse formulas and selected determinant values. B and C explicitly share part of their replay arithmetic and are not represented as fully independent implementations of each other.

The main replay also reconstructs the inherited finite support frontier and applies exactly the four proved masks above. Earlier source packages are included unchanged, with their own manifests. Historical notes may name working-directory paths; this document's links identify the bundled proof dependencies.

This proves a restricted necessary condition, subject to the usual review of an unpublished computer-assisted argument. It does not prove the full conjecture, unrestricted degree 20, a seven-term bound, historical novelty, or publication readiness.
