# A certified support bound in degree 20

23 September 2026. Unpublished, internally audited research note. Historical priority is not established. This is a partial result about the Casas–Alvero conjecture, not a proof of the conjecture in degree 20.

## Statement

Let \(f\in\mathbb C[X]\) have degree 20 and share a nonconstant factor with each of its derivatives of orders 1 through 19. Let \(c\) be the unique root of \(f^{(19)}\), and let \(L\) be the leading coefficient of \(f\). Define the monic centered polynomial \(g(X)=L^{-1}f(X+c)\).

**Theorem (candidate, certificate-backed).** Either \(g=X^{20}\), or \(g\) has at least five nonzero monomials. Equivalently, a nontrivial degree-20 Casas–Alvero polynomial cannot have at most four nonzero monomials in its monic centered normal form.

The count includes the leading monomial. Centering is essential: the statement is about this specific normal form, not every translate of the polynomial. The same conclusion holds over any characteristic-zero field: the finitely generated field of coefficients embeds into the complex numbers, preserving the relevant common-factor conditions. The claim leaves all centered polynomials with five or more nonzero monomials unresolved.

## 1. Published prerequisites and support reduction

Because \(c\) is a common root of \(f\) and \(f^{(19)}\), the centered polynomial has zero constant term and zero coefficient of \(X^{19}\). Write

\[
g(X)=X^{20}+\sum_{m\in S}a_m X^{20-m},
\qquad S\subseteq\{2,\ldots,19\},\quad a_m\ne0.
\]

We use two published results of Castryck–Laterveer–Ounaïes (CLO), *Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12*, Mathematics of Computation 83 (2014), 3017–3037; [primary manuscript](https://arxiv.org/html/1208.5404).

1. **Theorem 2, with prime 19.** A nontrivial degree-\(p+1\) counterexample has a simple mean root. Therefore \(a_{19}=g'(0)\ne0\), so \(19\in S\).
2. **Proposition 15, with \(20=4\cdot5\).** The polynomial and its derivatives of orders 5, 10 and 15 cannot all vanish at the same root. At zero these derivative values are nonzero constant multiples of the coefficients indexed by 15, 10 and 5. Hence \(S\cap\{5,10,15\}\ne\varnothing\).
3. **The stronger clause of Proposition 15, with \(20=5\cdot2^2\) and \(5=2^2+1\).** The derivatives of orders 4 and 16 cannot both vanish at the common root zero. Hence \(S\cap\{4,16\}\ne\varnothing\).

The three required sets are disjoint. Thus \(|S|\ge3\). To exclude exactly three nonleading terms, only the following six supports remain:

\[
\{4,5,19\},\ \{4,10,19\},\ \{4,15,19\},\
\{5,16,19\},\ \{10,16,19\},\ \{15,16,19\}.
\]

CLO Theorem 2 also supplies a determinant divisibility condition. For \(S=\{a,b,19\}\), let \(J=\{2,\ldots,18\}\setminus\{a,b\}\), in increasing order. These are precisely the indices \(j\) with \(g^{(20-j)}(0)=0\). Form a matrix with one row for every \(j\in J\),

\[
\left[-1,\quad
\left(j\binom{j-2}{k-2}\,\mathbf1_{k\le j}\right)_{k\in J}\right],
\]

and final row \(\left[-1,\left((-1)^k\right)_{k\in J}\right]\).
Its determinant must be divisible by 19. Exact integer determinants and an independently implemented finite-field elimination give:

| Support \(S\) | Determinant modulo 19 |
|---|---:|
| \(\{4,5,19\}\) | 15 |
| \(\{4,10,19\}\) | 7 |
| \(\{4,15,19\}\) | 10 |
| \(\{5,16,19\}\) | 0 |
| \(\{10,16,19\}\) | 12 |
| \(\{15,16,19\}\) | 13 |

Only \(\{5,16,19\}\) remains. `check_support_filter.py` checks these numbers, all 136 supports containing 19, and the five degree-12 examples printed in the source as an indexing control. This pruning is an application of CLO, not a new theorem attributed to this campaign.

## 2. The remaining family and marked-root normalization

Suppose

\[
g(X)=X^{20}+aX^{15}+bX^4+cX,
\qquad abc\ne0.
\]

Use Hasse derivatives, equivalent to ordinary derivatives in characteristic zero up to nonzero factorials. The active derivative orders are 15, 4 and 1. All other derivative conditions hold at zero.

Choose a common root \(r\) of \(g\) and its 15th Hasse derivative. Since that derivative takes value \(a\ne0\) at zero, \(r\ne0\). Replacing \(g(X)\) by \(r^{-20}g(rX)\) preserves the conditions and makes this marked root equal to 1. Then

\[
a=-\binom{20}{15}=-15504.
\]

Choose common roots \(u,v\) for the fourth and first derivatives respectively. They are nonzero because their values at zero are \(b,c\ne0\). They need not be distinct from one another or from 1; no collision cases are deleted. The derivative equations yield

\[
\begin{aligned}
b(u)&=-\binom{20}{4}u^{16}-\binom{15}{4}a u^{11}
      =-4845u^{16}+21162960u^{11},\\
c(u,v)&=-20v^{19}-15a v^{14}-4b(u)v^3.
\end{aligned}
\]

The root equations \(g(1)=g(u)=g(v)=0\), divided by the corresponding nonzero marked roots, are

\[
\begin{aligned}
E_1&=1+a+b+c,\\
E_2&=u^{19}+a u^{14}+b u^3+c,\\
E_3&=v^{19}+a v^{14}+b v^3+c.
\end{aligned}
\]

Thus a hypothetical polynomial gives a solution of \(E_1=E_2=E_3=0\). For the exclusion it suffices to prove that this **unsaturated** system has no solution. We allow even \(u=0\), \(v=0\), or zero coefficients when testing it, so no nonzero constraint can be lost in specialization.

## 3. Finite-module specialization lemma

**Lemma.** Let \(A=\mathbb Z_{(p)}\), and let \(I\subseteq A[u,v]\). Suppose \(I\) contains a polynomial in \(u\) alone whose leading coefficient is a unit of \(A\), and a polynomial monic in \(v\) with coefficients in \(A[u]\). If the reduction of \(I\) modulo \(p\) is the unit ideal, then \(A[u,v]/I=0\), and consequently \(I\mathbb Q[u,v]=\mathbb Q[u,v]\).

**Proof.** Divide the first polynomial by its unit leading coefficient. If its degree is \(r\), powers of \(u\) reduce to exponents below \(r\). The monic second polynomial, of degree \(s\) in \(v\), reduces powers of \(v\) to exponents below \(s\), after which coefficients can be reduced using the first relation. Hence \(M=A[u,v]/I\) is a finite \(A\)-module, generated by the \(rs\) monomials \(u^i v^j\), \(0\le i<r,0\le j<s\).

The unit-ideal hypothesis modulo \(p\) means \(M/pM=0\). Nakayama's lemma for the local ring \(A\), with maximal ideal \(pA\), gives \(M=0\). Tensoring with \(\mathbb Q\) proves the last conclusion. \(\square\)

Finiteness is indispensable. A unit ideal after reducing an arbitrary affine system modulo \(p\) does not by itself exclude characteristic-zero solutions. For example \(pu-1=0\) has a rational solution but no reduction modulo \(p\); its leading coefficient is not a unit of \(A\). The present argument uses the precise monic relations below, not that invalid general implication.

## 4. Applying the lemma at 31

Let \(I=(E_1,E_2,E_3)\subseteq A[u,v]\) with \(A=\mathbb Z_{(31)}\). The polynomial

\[
E_2-E_1=u^{19}+a u^{14}+b(u)u^3-1-a-b(u)
\]

has degree 19 in \(u\) and leading coefficient

\[
1-4845=-4844\equiv23\pmod{31},
\]

which is a unit in \(A\). Also

\[
E_3-E_1=v^{19}+a v^{14}+b(u)v^3-1-a-b(u)
\]

is monic of degree 19 in \(v\). The quotient is therefore generated over \(A\) by at most \(19^2=361\) monomials.

The accompanying certificate gives three explicit polynomials \(C_1,C_2,C_3\in\mathbb F_{31}[u,v]\) with

\[
\boxed{C_1\overline E_1+C_2\overline E_2+C_3\overline E_3=1.}
\]

The certificate contains 515, 629 and 656 terms respectively, with maximum total degree 39. Its SHA-256 is

`e63069da3f19151f84cd44ec9f5c46e55d6d806e743c0ccbd25827c6214020a0`.

`verify_mod31.py` uses only Python's standard library. It reconstructs the integer equations from the Hasse-derivative definition, checks the three exported generators, multiplies out this identity modulo 31, and verifies both integral leading-coefficient conditions. It also rejects a deliberately altered certificate. It does not rely on a claimed Gröbner basis output. Singular generated the certificate; a separate SymPy computation with reversed variable order corroborated that the ideal is the unit ideal.

The lemma now excludes every characteristic-zero solution of the unsaturated system, and therefore excludes the remaining support. This completes the theorem. \(\square\)

## 5. Reproduction and claim boundary

Run with Python 3.10 or later:

```sh
python3 check_support_filter.py
python3 verify_mod31.py
```

Normal and optimized Python produced identical receipts. The final replay requires no CAS, numerical root approximation, network service or unrefereed result of Ghosh or Marashdeh. The published CLO prerequisites and the normalization/specialization proof remain mathematical dependencies to inspect; the scripts do not formally verify those arguments.

This gives a checked partial exclusion in degree 20, subject to ordinary mathematical review. It does not settle degree 20, higher degrees, historical priority, or publication significance. The bounded search did not locate this exact support bound, but that is not proof of novelty. Separate internal agents checked the support reduction, normalization, finite-module argument, and finite-field unit ideal. They are not independent human referees.
