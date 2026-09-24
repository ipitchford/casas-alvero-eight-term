# An arithmetic support obstruction for Casas–Alvero polynomials

23 September 2026. Unpublished research note with exact arithmetic checks and internal adversarial review. Historical novelty remains a separate question.

## Results

A characteristic-zero polynomial is called Casas–Alvero here if it shares a nonconstant factor with each ordinary derivative of orders 1 through one less than its degree. A polynomial is nontrivial if it is not a constant multiple of a power of a linear polynomial. In positive characteristic, the corresponding condition always means **Hasse derivatives**.

Put

\[
J=\{1,2,3,5,6,7,13,14,15,16,18\},\qquad
K=20-J=\{2,4,5,6,7,13,14,15,17,18,19\}.
\]

**Theorem 1 (an infinite sequence of degrees).** Let \(e\ge0\), \(q=13^e\), and \(N=20q\). If a characteristic-zero polynomial \(f\) of degree \(N\) is a nontrivial Casas–Alvero polynomial, then, at every root \(\alpha\) of \(f\), at least one of the derivatives

\[
\{f^{(qk)}:k\in K\}
\]

is nonzero. Equivalently, in the monic translate

\[
L^{-1}f(X+\alpha)=X^N+\sum_{j=1}^{N-1}b_jX^{N-j},
\]

at least one coefficient \(b_{qj}\), \(j\in J\), is nonzero. Here \(L\) is the leading coefficient of \(f\).

For degree 20, the theorem excludes every support contained in

\[
T=\{4,8,9,10,11,12,17,19\}.
\]

Thus it excludes the whole family

\[
X^{20}+aX^{16}+X^8 Q(X)+cX^3+dX,\qquad\deg Q\le4,
\]

with arbitrary coefficients, apart from the trivial monomial. This includes polynomials with as many as nine nonzero terms.

**Corollary 2 (degree-20 sparsity).** A nontrivial characteristic-zero Casas–Alvero polynomial of degree 20 has at least **six nonzero monomials in its monic centered normal form**, counting the leading monomial. Centering translates the unique root of the nineteenth derivative to zero.

These are necessary conditions. They do not solve the conjecture in any unrestricted degree. No assertion is made that either bound is sharp.

## 1. Valuation reduction and a support lemma

We use the standard binomial-normalized coefficient induction appearing in [Castryck–Laterveer–Ounaïes (CLO), Section 3](https://arxiv.org/html/1208.5404). The argument is included to specify the reduction precisely. Modular exclusion and prime-power degree lifting are established Casas–Alvero methods; see [Graf von Bothmer–Labs–Schicho–van de Woestijne, Propositions 2.2 and 2.6](https://arxiv.org/html/math/0605090v2). The contribution under assessment here is the particular characteristic-13 support exclusion and its consequences, not those general methods.

Let \(F\) be monic, nontrivial, of degree \(n\), satisfying the Casas–Alvero conditions, with \(F(0)=0\). Extend the \(p\)-adic valuation to a field containing its coefficients and roots. Choose a nonzero root of minimum valuation and scale it to 1. All roots are now integral in the valuation ring, and 1 is a root. Write

\[
F(X)=\sum_{j=0}^{n}\binom nj a_jX^{n-j},\qquad
a_0=1,\quad a_n=0.
\]

All \(a_j\) are integral. Indeed,

\[
\frac{j!}{n!}F^{(n-j)}(X)
=\sum_{i=0}^{j}\binom ji a_iX^{j-i}.
\]

Evaluation at a common root of \(F\) and that derivative expresses \(a_j\) as an integral polynomial in the preceding coefficients and an integral root. Induction proves the claim. Consequently every coefficient whose binomial factor is divisible by \(p\) vanishes on reduction. Hasse derivatives commute with reduction, and reductions of the original common roots remain common-root witnesses. The reduced polynomial retains the root 1, so it cannot be \(X^n\).

This argument works for arbitrary characteristic-zero coefficients. One can use a valuation extension with an ordered value group; discreteness or an algebraicity assumption on the coefficients is unnecessary. Equivalently, the finitely generated coefficient field can first be embedded into the complex numbers. All assertions concern finitely many coefficients and common-factor conditions.

For the original nonleading support \(S\), let

\[
C_p(n)=\{j:1\le j<n,\ p\nmid\binom nj\}.
\]

**Support lemma.** The intersection \(S\cap C_p(n)\) is nonempty. If it consists of one index \(m\), then \(\binom nm\equiv1\pmod p\).

The empty-intersection case would reduce to \(X^n\), contrary to the retained root 1. In the singleton case the reduction is

\[
\overline F=X^n+cX^{n-m},\qquad c\ne0.
\]

The Hasse derivative of order \(n-m\) is \(\binom nmX^m+c\). Its common root with \(\overline F\) is nonzero, because the constant term is nonzero. The two root equations give \(X^m=-c\) and \(\binom nmX^m=-c\), proving the congruence. Notice that the lemma concerns the characteristic-zero support; it does not claim that every visible coefficient survives reduction.

## 2. The characteristic-13 obstruction

**Lemma 3.** Over an algebraically closed field of characteristic 13, the only polynomial

\[
h(X)=X^{20}+aX^{16}+cX^3+dX
\]

with the Casas–Alvero Hasse-derivative property is \(X^{20}\).

We prove the lemma explicitly, including zero coefficients.

### The case \(a=0\)

If \(c\ne0\), a common root of \(h\) and \(H_3(h)\) is nonzero. Scale it to 1. Since \(\binom{20}{3}=9\) in the residue field, this gives \(c=4\), and \(h(1)=0\) gives \(d=8\). A common root \(w\) of \(h\) and \(H_1(h)\) is nonzero and satisfies

\[
w^{19}+4w^2+8=0,\qquad 7w^{19}+12w^2+8=0.
\]

Thus \(w^2=10\) and \(w^{19}=4\). But \(w^{19}=w(10)^9=-w\), so \(w=9\), inconsistent with \(w^2=10\), since \(9^2=3\) in characteristic 13.

If \(c=0\) and \(d\ne0\), a common root of \(X^{20}+dX\) and its first derivative must be nonzero. Their equations imply \(w^{19}=-d\) and \(7w^{19}=-d\), which is impossible. The remaining case is \(h=X^{20}\).

### The case \(a\ne0\): choosing witnesses without deleting a boundary

A common root of \(h\) and \(H_{16}(h)\) is nonzero. Scale it to 1. Since \(\binom{20}{16}=9\), we now have \(a=4\).

Choose a nonzero common root \(v\) of \(h\) and \(H_3(h)\). If \(c\ne0\), every such witness is nonzero. If \(c=0\), use \(v=1\): then \(h(1)=0\) and \(H_3(h)(1)=9+4=0\). Thus this choice is valid even when a coefficient vanishes.

The Hasse derivative equation and the root equation give

\[
c=4v^{17}-4v^{13},\qquad d=-5v^{19},
\]

while \(h(1)=0\) gives

\[
F(v):=5v^{19}-4v^{17}+4v^{13}-5=0.
\]

In particular \(v\ne0\) and \(d\ne0\). Therefore any common root \(w\) of \(h\) and its first derivative is also nonzero. Put

\[
P(X)=h(X)/X=X^{19}+4X^{15}+cX^2+d.
\]

From \(P(w)=h'(w)=0\),

\[
0=3P(w)-h'(w)=9w^{19}+2d
=9w^{19}+3v^{19}.
\]

It follows that \(w^{19}=4v^{19}\). Set \(t=w/v\), so

\[
M(t)=t^{19}-4=0.
\]

Substitute this relation and the expressions for \(c,d\) into \(P(w)=0\), and divide by \(v^{15}\). The result is

\[
(4t^2-1)v^4+4(t^{15}-t^2)=0.
\]

Let \(D=4t^2-1\), \(B=4(t^2-t^{15})\), and \(T=v^4\). The two roots of \(D\) are 6 and 7; their nineteenth powers are 7 and 6, respectively, so neither is a root of \(M\). Consequently \(D\ne0\) and \(T=B/D\).

### A small univariate calculation

Using \(v^4=T\), the equation \(F(v)=0\) becomes

\[
5T^4v^3+4T^3(1-T)v=5.
\]

Square this equation and substitute \(v^4=T\). Collecting terms gives

\[
T^6(-T^3+3T^2-6T+3)v^2=T^9-T^8-1.
\]

Squaring once more gives the necessary condition

\[
R(T)=(T^9-T^8-1)^2-T^{13}(-T^3+3T^2-6T+3)^2=0.
\]

These steps make no division by the cubic factor; any extraneous solutions introduced by squaring cause no problem for an exclusion. Compute the remainder of \(D^{19}R(B/D)\) modulo \(M\). It is

\[
\begin{aligned}
H(t)={}&5t^{18}-6t^{17}-3t^{16}+3t^{15}-2t^{14}-6t^{13}
+t^{11}+3t^{10}\\
&-t^8+t^7-t^6+3t^5+6t^4+5t^3-4t^2+6.
\end{aligned}
\]

This is a finite polynomial identity, independently reproduced by `check_mod13_explanation.py`. A hypothetical ratio would satisfy both \(M(t)=0\) and \(H(t)=0\).

But

\[
M(t)=(t-4)Q(t),\qquad Q(t)=\sum_{j=0}^{18}4^jt^{18-j}.
\]

The polynomial \(Q\) is irreducible over \(\mathbb F_{13}\). Its roots are 4 times the primitive nineteenth roots of unity, and \(\operatorname{ord}_{19}(13)=18\). To check the order, Fermat gives a divisor of 18; the congruences \(13^6=11\) and \(13^9=-1\pmod{19}\) rule out every proper divisor.

Now \(H(4)=8\), so \(t-4\) is not a common factor. If \(H\) had a root in common with the irreducible degree-18 polynomial \(Q\), their equal degree and leading coefficients would imply \(H=5Q\). Their \(t^{16}\) coefficients disagree: that of \(H\) is \(-3=10\), while that of \(5Q\) is \(5\cdot4^2=2\). This contradiction proves Lemma 3.

Only three common-root conditions were needed in this lemma: orders 16, 3, and 1. The proof works over the algebraic closure, not just at rational points of the finite field.

## 3. Proof of Theorem 1

Translate the chosen root \(\alpha\) to zero and make the polynomial monic. Suppose every coefficient with deficiency index \(qj\), \(j\in J\), is zero. Apply the valuation normalization from Section 1 at the prime 13.

Lucas's theorem gives

\[
\binom{20q}{r}\not\equiv0\pmod{13}
\quad\Longleftrightarrow\quad
r=qj\text{ with }j\in\{0,1,\ldots,7,13,14,\ldots,20\}.
\]

Indeed, \(20=(17)_{13}\), and multiplication by \(q\) adds \(e\) zero digits. After removing the assumed zero coefficients, the zero constant term, and the leading coefficient, only indices \(q\cdot4,q\cdot17,q\cdot19\) can survive. Thus

\[
\overline F(X)=h(X^q),\qquad h(Y)=Y^{20}+aY^{16}+cY^3+dY.
\]

Also \(h(1)=\overline F(1)=0\), so \(h\ne Y^{20}\).

For \(1\le k\le19\), the Hasse derivative identity in characteristic 13 is

\[
H_{qk}\bigl(h(X^q)\bigr)=\bigl(H_kh\bigr)(X^q).
\]

For example, it follows by comparing coefficients in \((X+Z)^q=X^q+Z^q\), or directly from Lucas's theorem. A common-root witness for \(F\) and \(H_{qk}(F)\) is integral by normalization. Reducing it and taking its \(q\)th power supplies a common root of \(h\) and \(H_k(h)\). Hence \(h\) has the Casas–Alvero Hasse-derivative property, contradicting Lemma 3. This proves the coefficient assertion of Theorem 1. The derivative assertion follows because characteristic-zero factorials are nonzero.

The argument treats arbitrary \(e\) symbolically. Checks at \(e=0,1,2\) in the companion code illustrate the indexing but do not substitute for this proof.

## 4. Proof of the six-term corollary

For a centered monic degree-20 polynomial write

\[
g(X)=X^{20}+\sum_{m\in S}b_mX^{20-m},\qquad
S\subseteq\{2,\ldots,19\}.
\]

The support lemma gives the following necessary conditions:

| Prime | Required intersection |
|---:|---|
| 19 | \(19\in S\) |
| 2 | \(S\cap\{4,16\}\ne\varnothing\) |
| 5 | \(S\cap\{5,10,15\}\ne\varnothing\) |
| 17 | \(S\cap\{2,3,17,18\}\ne\varnothing\) |
| 3 | \(S\cap\{2,9,10,11,18\}\ne\varnothing\) |

For primes 17 and 3, the only additional visible index is 19, and a singleton there would require \(20\equiv1\), which fails for both primes. The first four required sets are disjoint, so \(|S|\ge4\). This recovers the earlier five-term lower bound by an elementary argument; that bound is not being claimed as new.

If \(|S|=4\), it consists of 19 and one index from each of the three other disjoint sets. The prime-3 condition reduces the resulting 24 choices to 16.

We now use [CLO, Theorem 2](https://arxiv.org/html/1208.5404), at prime 19. For the missing coefficient indices \(Z=\{2,\ldots,18\}\setminus S\), form the matrix with rows

\[
\left[-1,\ \left(j\binom{j-2}{k-2}\mathbf1_{k\le j}\right)_{k\in Z}\right]
\quad(j\in Z),
\]

and final row \([-1,((-1)^k)_{k\in Z}]\). Its determinant must be divisible by 19. The indices are the missing coefficients, not the active derivative orders. The sixteen determinant residues are:

| \(S\setminus\{19\}\) | Residue | \(S\setminus\{19\}\) | Residue |
|---|---:|---|---:|
| \(\{2,4,5\}\) | 5 | \(\{2,5,16\}\) | 13 |
| \(\{4,5,18\}\) | 17 | \(\{5,16,18\}\) | 12 |
| \(\{2,4,10\}\) | 1 | \(\{2,10,16\}\) | 18 |
| \(\{3,4,10\}\) | 1 | \(\{3,10,16\}\) | 14 |
| \(\{4,10,17\}\) | 0 | \(\{10,16,17\}\) | 11 |
| \(\{4,10,18\}\) | 7 | \(\{10,16,18\}\) | 2 |
| \(\{2,4,15\}\) | 17 | \(\{2,15,16\}\) | 9 |
| \(\{4,15,18\}\) | 3 | \(\{15,16,18\}\) | 2 |

The only remaining support is \(\{4,10,17,19\}\). It is contained in \(T\), so Theorem 1 excludes it. Therefore \(|S|\ge5\); counting the leading monomial proves Corollary 2.

The determinant values are checked by independent integer Bareiss and modular Gaussian elimination, with CLO's printed degree-12 examples as an indexing control. The independent 680-support enumeration reaches the same final family.

## 5. Dependencies and scope

Theorem 1 uses valuation extension, the reproduced coefficient induction, Lucas's theorem, elementary finite-field irreducibility, and the explicit degree-18 remainder. Corollary 2 additionally uses CLO's published determinant theorem. Neither result requires the claimed full proof of Ghosh, nor the unrefereed inequality theorem of Marashdeh.

The support induction, modular specialization, and triangular coefficient elimination are established methods. The good-prime integer discovered during the exploratory finite-module route coincides, up to sign, with Marashdeh's existing two-support obstruction and is not a new invariant. Massri's placement restrictions already imply the earlier five-term lower bound. The accompanying novelty report distinguishes these overlaps from the precise characteristic-13 exclusion and its consequences.

An independently checked 1,777-term unit-ideal certificate is retained as a second route for the normalized \(a\ne0\) case of the finite-field exclusion; the \(a=0\) cases use the separate elementary arguments above. The main proof uses the compact remainder instead. Arithmetic replay supports the finite identities; it is not a formal verification of the written argument or an external referee's judgment.
