# A short explanation of the degree-20 sparse exclusion

Research extension, 23 September 2026. Internal derivation; not published and not independently refereed. This file does not modify the frozen audit package.

## Main finding

The previous 1,800-term modular certificate is unnecessary. Two increasingly structural replacements are available:

1. In the last normalized four-term family, reduction modulo **3** gives the constant certificate **E1+E3=1**. The existing finite-module proof works at 3 unchanged.
2. More importantly, a general elementary valuation lemma proves the entire centered degree-20 five-term bound through four disjoint support constraints. It uses no determinant computation, no CAS, and no finite-module argument.

The second route is preferable as the mathematical explanation. Its method is a direct extension of the binomial-normalized coefficient induction used by Castryck–Laterveer–Ounaies (CLO) in [Section 3 and Proposition 15](https://arxiv.org/html/1208.5404). Historical priority of the stated support formulation has not been established; the method should not be advertised as new merely because we derived it here.

## 1. General visible-support lemma

Let f be a monic complex polynomial of degree n satisfying the Casas–Alvero common-root conditions, with f(0)=0 and f != x^n. Write

\[
 f(X)=X^n+\sum_{j\in S} b_jX^{n-j},\qquad
 S\subseteq\{1,\ldots,n-1\},\quad b_j\ne0.
\]

For a prime p, define

\[
 C_p(n)=\{j:1\le j<n,\ p\nmid\tbinom nj\}.
\]

**Lemma.** The following necessary conditions hold for every prime p:

1. S intersects C_p(n).
2. If S intersects C_p(n) in exactly one index m, then binom(n,m) is congruent to 1 modulo p.

This lemma concerns the support of the original characteristic-zero polynomial. It does not assert that every visible coefficient remains nonzero after reduction.

### Proof: integral binomial-normalized coefficients

Choose an extension of the p-adic valuation from Q to a field containing the coefficients and all roots of f. Such an extension exists by the standard valuation-extension theorem; it can be taken on an algebraically closed overfield. No rationality or algebraicity assumption on the complex coefficients is needed. A general ordered value group suffices.

Because f != x^n and f(0)=0, there is a nonzero root. Among the finitely many nonzero roots choose one with smallest valuation, and scale X by that root, adjusting the leading coefficient to keep the polynomial monic. Every root now has nonnegative valuation, and at least one root has valuation zero. This scaling preserves support, the zero root, and all common-root conditions.

Write the scaled polynomial as

\[
 f(X)=\sum_{j=0}^n\binom nj\alpha_jX^{n-j},
 \qquad\alpha_0=1,\quad\alpha_n=0.
\]

We claim v(alpha_j)>=0 for j=1,...,n-1. Indeed,

\[
 \frac{j!}{n!}f^{(n-j)}(X)
   =\sum_{k=0}^j\binom jk\alpha_kX^{j-k}.
\]

Choose a common root xi_j of f and this derivative. It is integral because it is a root of f. If alpha_0,...,alpha_(j-1) are integral, evaluation at xi_j expresses alpha_j as the negative of a sum of integral elements. This proves the claim by induction.

Consequently, if p divides binom(n,j), the actual coefficient b_j=binom(n,j)alpha_j has strictly positive valuation. This is the step that connects integer binomial divisibility with the support of a complex polynomial.

### Proof of the two support assertions

Reduce the scaled polynomial modulo the maximal ideal of the valuation ring. Its coefficients are integral and its leading coefficient is 1.

If S misses C_p(n), every nonleading coefficient reduces to zero. Hence the reduced polynomial is X^n. But a root of valuation zero reduces to a nonzero root, which is impossible for X^n. This proves assertion 1.

Suppose S intersects C_p(n) only at m. Then the reduction has the form

\[
 \overline f=X^n+cX^{n-m}.
\]

The existence of a root of valuation zero forces c != 0. The reduction of the Hasse derivative of order n-m is

\[
 \overline{H_{n-m}(f)}=\binom nm X^m+c.
\]

Every other coefficient disappears because its original coefficient has positive valuation and the Hasse derivative only multiplies it by an integer. A common root xi of f and H_(n-m)(f) is integral and must have valuation zero, since the derivative has nonzero constant term c in the residue field. Let eta != 0 be its reduction. Then

\[
 \eta^m+c=0,\qquad \binom nm\eta^m+c=0.
\]

Subtracting and using eta != 0 gives binom(n,m)=1 in the residue field, hence modulo p. This proves assertion 2. QED.

## 2. The degree-20 theorem without a CAS

Translate a degree-20 CA polynomial to the unique root of its nineteenth derivative and make it monic. Its constant coefficient and X^19 coefficient are zero, so its nonleading support satisfies

\[
 S\subseteq\{2,\ldots,19\}.
\]

The following four rows are immediate either from Lucas's theorem or direct binomial arithmetic:

| p | C_p(20) intersect {2,...,19} | Consequence |
|---:|---|---|
| 19 | {19} | 19 belongs to S. |
| 2 | {4,16} | S meets {4,16}. |
| 5 | {5,10,15} | S meets {5,10,15}. |
| 17 | {2,3,17,18,19} | S meets {2,3,17,18}. |

For the last row, 19 already belongs to S. If no other displayed index belonged to S, the singleton clause would require binom(20,19)=20 to be 1 modulo 17. But 20=3 modulo 17. Hence another index in that row is required.

The four required sets

\[
 \{19\},\quad\{4,16\},\quad\{5,10,15\},\quad
 \{2,3,17,18\}
\]

are pairwise disjoint. Therefore |S|>=4. Counting the leading monomial proves:

**Theorem.** The monic centered normal form of a nontrivial degree-20 Casas–Alvero polynomial has at least five nonzero monomials.

This proof also locates four separate groups in which nonzero coefficients must occur. There is no need for CLO's determinant restriction or for a search over the six four-term supports. The p=19 row reproves the simple-mean-root conclusion needed here rather than taking that special-degree theorem as an external dependency.

The Lucas calculations are especially transparent:

- 20=(10100)_2, so nonzero binomial residues have proper positive indices 4 or 16.
- 20=(40)_5, so the proper positive indices are 5, 10, 15.
- 20=(11)_19, so the proper positive indices are 1 and 19; centering removes 1.
- 20=(13)_17, so the proper positive indices are 1, 2, 3, 17, 18, 19; centering removes 1.

## 3. A particularly simple sufficient exclusion criterion

A direct corollary of the lemma is useful beyond degree 20.

**Corollary.** Suppose f(0)=0 and there exists a prime p such that p does not divide n-1 and p divides binom(n,j) for every nonleading support index j other than possibly n-1. Then f cannot be a nontrivial characteristic-zero CA polynomial.

If S misses C_p(n), use the first clause. Otherwise the only visible index is n-1, and the singleton clause would force binom(n,n-1)=n to be 1 modulo p, contradicting p not dividing n-1.

This corollary allows any number of nonzero terms; it is not limited to four-term polynomials. For the family X^20+aX^15+bX^4+cX, its support indices are 5,16,19. The primes 3 and 17 both satisfy this criterion because they divide binom(20,5) and binom(20,16), but not 19.

The criterion is a necessary-support filter, not a complete classification: when it does not apply, the family remains unresolved by this test. For n=20 it leaves all potential counterexamples with four or more nonleading support indices open.

## 4. Constant certificate at 3 for the existing normalized system

For compatibility with the previous proof, retain its normalized equations:

\[
 a=-15504,\quad b=-4845u^{16}+21162960u^{11},\quad
 c=-20v^{19}-15av^{14}-4bv^3,
\]

\[
 E_1=1+a+b+c,\quad
 E_2=u^{19}+au^{14}+bu^3+c,\quad
 E_3=v^{19}+av^{14}+bv^3+c.
\]

Modulo 3, a=b=0 and c=v^19. Thus

\[
 \overline E_1=1+v^{19},\qquad
 \overline E_3=2v^{19},\qquad
 \boxed{\overline E_1+\overline E_3=1.}
\]

The old finite-module bridge applies with A=Z_(3): E2-E1 is univariate in u with degree 19 and leading coefficient -4844=1 mod 3; E3-E1 is monic in v of degree 19. Hence their quotient is finite over A. The constant certificate and Nakayama imply that the characteristic-zero ideal is the unit ideal. This route is fully elementary too, but the visible-support proof is shorter and more general.

## 5. What happened to the modulus-31 calculation?

It was correct but concealed an elementary obstruction at a smaller prime. At 31, the binomial constants do not vanish, so the same normalized family yields a genuinely nontrivial elimination. I also found a smaller explanatory reformulation there: write P(X)=X^19-4X^14+B X^3+3-B; a nonzero common root with f' is a repeated root of P. Its resultant with 19X^16+14(-4)X^11+3B is degree 19 in B. Substituting B=-9u^16+4u^11 and reducing modulo the four-term polynomial -8u^19+9u^16-4u^11+3 gives a degree-18 polynomial coprime to it. That can replace the bivariate identity by a univariate resultant-and-Euclidean certificate.

There is no reason to prefer this more complicated route now that reduction at 3 supplies a constant certificate and the general valuation argument explains the underlying support obstruction. The exploration is recorded only to explain why the old calculation was valid yet unnecessarily large.

## 6. Novelty and assurance

- The lemma is proved here, not assumed from an unrefereed paper.
- Its ingredients are standard valuation extension, the classical binomial-normalized coefficient induction, and Lucas's theorem. CLO Section 3 contains the central induction and uses it for special support restrictions. A specialist may regard this lemma and the degree-20 consequence as routine corollaries of that method.
- A new short proof is not by itself evidence of a new theorem. This note does not settle historical priority or publication significance.
- No assertion is made that the five-term lower bound is sharp. A five-term CA counterexample may not exist at all.
- The lemma makes no claim that the whole CA conjecture follows from these support tests. It deliberately leaves all supports passing them unresolved.
- `check_explanation.py` uses only standard-library integer arithmetic to verify the four Lucas rows, the disjointness argument, and the modulus-3 constant certificate. The valuation argument remains a written mathematical proof, not a formally verified theorem.
