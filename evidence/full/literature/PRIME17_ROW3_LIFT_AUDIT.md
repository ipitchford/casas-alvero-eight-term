# Independent audit: the third characteristic-17 seed cannot lift

23 September 2026. **PASS.** This is an exclusion of one entire
characteristic-zero residue branch, with arbitrary original coefficient
support and arbitrary ramification. It is stronger than checking that
the seed has the finite-characteristic CA property, but it does not
exclude the other eight seeds or settle degree 20.

## Exact primary-source input

[Castryck–Laterveer–Ounaïes, *Constraints on counterexamples to the
Casas–Alvero conjecture, and a verification in degree 12*, Theorem 2](https://arxiv.org/html/1208.5404),
states that for a characteristic-zero counterexample of degree \(p+1\),
the root of its \((d-1)\)-st derivative is a simple root of the
polynomial. Proposition 15 and the paragraph immediately following its
proof establish this property more generally when \(d=p^r+1\).
The primary statement and its proof context were freshly checked.

For degree 20 take \(p=19\). Therefore a hypothetical nontrivial CA
polynomial centered at its mean root zero satisfies \(f'(0)\ne0\).
This is an exact characteristic-zero property of \(f\); it imposes
no requirement to use a 19-adic normalization when later reducing at
17. Translation to the mean and nonzero scaling preserve simplicity.
No relation between residue fields at the two primes is being assumed.

## The residue calculation

The third normalized seed is

\[
h=X^{20}+14X^{18}+8X^{17}+16X^3+12X^2
\quad\text{in characteristic }17.
\]

Its zero root has multiplicity exactly two, since its constant and
linear coefficients vanish and its quadratic coefficient is 12.
The independent polynomial Euclidean computation in
`check_prime17_seed_gcds.py` gives

\[
\gcd(h,H_1h)=X.
\]

Here \(H_1h=h'=3X^{19}+14X^{17}+14X^2+7X\). The ordinary and
optimized replays agree. Because the gcd is computed as a polynomial
identity over \(\mathbb F_{17}\), the only common root is zero
over every algebraically closed extension, not only over the prime
field.

## Ramification-independent exclusion

Suppose an integral monic characteristic-zero CA polynomial \(f\),
centered at zero and with all roots integral, has reduction \(h\).
The CA condition for the first derivative supplies a repeated root
\(r\) of \(f\). Reduction of \(f(r)=f'(r)=0\) gives a common
root of \(h,h'\), so \(\bar r=0\).

The simple-mean theorem gives \(r\ne0\). Thus, over the splitting
valued field,

\[
X(X-r)^2\mid f(X).
\]

The quotient is monic and integral: it is the product of the remaining
linear factors, whose roots are all integral. Reducing the factorization
modulo the maximal ideal now yields

\[
X^3\mid h(X),
\]

contradicting the exact residue multiplicity two. This proof uses only
integrality and reduction. It assumes neither discrete valuations nor
integer-valued displacements, and requires no Hensel uniqueness theorem.

Equivalently, the zero residue cluster has total root multiplicity two.
It contains the exact mean root with multiplicity one, leaving capacity
one for all other roots in that cluster. A repeated root distinct from
the mean cannot fit. All other residue roots are simple as well, since
the only common root of \(h,h'\) is zero; therefore the parent's
alternative squarefreeness argument reaches the same contradiction.

The contradiction is independent of the higher coefficients that vanish
only upon reduction. It rules out every characteristic-zero lift in
this normalized residue branch, not merely a sparse family or a fixed
finite-precision approximation.
