# Independent audit of the seven-total-term inventory

24 September 2026. **PASS as an exhaustive necessary-support reduction to the fourteen listed exact supports.** Excluding those fourteen is a separate mathematical dependency.

Reviewed checker SHA-256: cea4f40ec5b6ced2b11b335a7e21cfb3516db792503eddb90de7687fd24c45c5.

## Mathematical scope and indexing

Centering a nontrivial degree-20 CA polynomial makes \(a_1=a_{20}=0\). The mean is a simple root by [Castryck–Laterveer–Ounaïes, Theorem 2](https://arxiv.org/html/1208.5404), checked against the primary text on 24 September 2026. Thus \(a_{19}\ne0\). A polynomial with exactly seven nonzero monomials has exactly six active deficiency indices, one of which is 19. Choosing the other five from \(2,\ldots,18\) gives precisely \(\binom{17}{5}=6188\) possibilities. No exact seven-term support is omitted.

For each of the eight primes used, binomial-normalized integrality and a retained unit root justify the visible-index test. If no support index is visible, the reduction is a monomial, contradicting that unit root. If only one is visible, it cannot disappear too; its common-root equation requires its binomial multiplier to be 1. These are necessary tests, so using only the listed primes cannot cause a false exclusion.

For two visible indices \(r<s\), the check correctly requires both binomial multipliers \(B,D\) to differ from 0 and 1 before applying the two-visible obstruction. Those guards exclude loss to either singleton. With both reduced coefficients nonzero, normalize the first relevant common root to 1. The reduced polynomial becomes \(X^{20}-BX^{20-r}+(B-1)X^{20-s}\). At a nonzero second witness \(v\), the two equations give
\[
(D-C)v^s=(C-1)(B-1),\qquad
B(D-C)v^{s-r}=(D-1)(B-1),
\]
where \(C=\binom{20-r}{s-r}\). They force \(D-C\ne0\) and \(C-1\ne0\). Raising to the powers determined by \(\gcd(r,s)\) yields exactly the implemented integer expression. This directly verifies the necessary formula without relying solely on its prior attribution to de Frutos Marín. It remains valid in characteristics dividing either exponent because it uses powers, not division by an exponent.

For the final determinant, the missing set is precisely
\(J=\{2,\ldots,18\}\setminus S\). At the centered mean, \(a_j=0\) is equivalent in characteristic zero to the vanishing of the derivative of order \(20-j\). The matrix therefore uses missing deficiencies, exactly as in the primary Theorem 2. Its lower triangular entries \(j\binom{j-2}{k-2}\), first column \(-1\), and final row \((-1,(-1)^k)\) agree with that theorem. No complement or derivative-order reversal occurs.

## Independent verification

The producer checker passes under normal and optimized Python. Both outputs are identical and match the saved receipt.

A separate calculation re-enumerated all supports using full integer powers for the two-visible expression and exact integer Bareiss determinants, rather than the producer's modular Gaussian elimination. Every Bareiss division was checked for exactness. It reproduced the counts
\[
6188\longrightarrow586\longrightarrow348\longrightarrow14
\]
and exactly the same fourteen supports. This is an independent arithmetic and enumeration cross-check; it does not reprove the published determinant theorem.

The Massri conditions are not used to filter any support. The optional diagnostic merely checks that all 348 supports already satisfy them. Consequently no assumption about Massri's three-recycled-root theorem or any interpretation of its type condition enters this inventory.

## Implication and limitation

The inventory is complete for exactly seven total centered monomials. The earlier theorem excluding fewer than seven is a separate dependency; this script does not replace that proof. A theorem excluding all fourteen surviving exact supports, combined with that earlier theorem, gives the eight-total-term lower bound. Neither this necessary-condition sieve nor a count of fourteen establishes realizability of any survivor or settles unrestricted degree 20.
