# A second characteristic-13 seed: exponents 20, 4, 3, 1

## Statement and scope

**Lemma.** Over an algebraically closed field of characteristic 13, the only polynomial

\[
 h(X)=X^{20}+aX^4+cX^3+dX
\]

that shares a root with each of its Hasse derivatives is \(X^{20}\).

Only the common-root conditions at orders 4, 3, and 1 are needed. Every coefficient-zero case is included. This is a finite-characteristic statement; its characteristic-zero support consequence follows separately from the already proved valuation normalization and Lucas reduction.

## 1. Zero coefficients and normalization

If \(a=0,c\ne0\), choose a common root of \(h\) and \(H_3(h)\). It is nonzero, so scale it to 1. Since \(\binom{20}{3}=9\) in characteristic 13, the normalized coefficients are \(c=4,d=8\). A common root \(w\) with \(H_1(h)\) is nonzero and satisfies

\[
 w^{19}+4w^2+8=0,\qquad 7w^{19}+12w^2+8=0.
\]

These imply \(w^2=10\) and \(w^{19}=4\). Since \(10^9=-1\), the second equality gives \(w=9\), but \(9^2=3\ne10\), a contradiction. If \(a=c=0,d\ne0\), the two equations \(w^{19}=-d\) and \(7w^{19}=-d\) are inconsistent. The all-zero case is the permitted monomial.

Now suppose \(a\ne0\). A common root with \(H_4(h)=9X^{16}+a\) is nonzero. Normalize that root to 1. Then

\[
 a=4,\qquad 5+c+d=0.
\]

If \(c=0\), then \(d=8\). For a nonzero common root \(w\) with the first derivative, put \(P(X)=h(X)/X\). The equations \(P(w)=h'(w)=0\) imply

\[
 w^3=9,\qquad w^{19}=8.
\]

Because \(9^6=1\), they give \(w=8\), contrary to \(8^3=5\ne9\). Thus \(c\ne0\).

Choose a common root \(v\ne0\) with \(H_3(h)=9X^{17}+3X+c\). The derivative and root equations give

\[
 T=v^{16},\qquad c=v(4T-3),\qquad d=-v^3(5T+1).
\]

If \(d=0\), then \(T=5\), while \(h(1)=0\) gives \(c=8\). Hence \(8=v(4\cdot5-3)=4v\), so \(v=2\). But \(2^{16}=3\ne5\). Therefore

\[
 v\ne0,\quad d\ne0,\quad A(T):=5T+1\ne0.
\]

The normalization equation \(h(1)=0\) becomes

\[
 Q(v,T):=(5T+1)v^3+(3-4T)v-5=0,
 \qquad v^{16}-T=0.
\]

## 2. Eliminate the repeated-root witness

Choose a common root \(w\) of \(h\) and \(H_1(h)\). Since \(d\ne0\), this root is nonzero. From

\[
 P(w)=w^{19}+4w^3+cw^2+d=0,
\]

and

\[
 h'(w)=7w^{19}+3w^3+3cw^2+d=0,
\]

subtracting \(7P(w)\) gives

\[
 w^3+9cw^2+7d=0.
\]

Set \(t=w/v\). Substitution of the formulas for \(c,d\) gives

\[
 D(t)T=B(t),\qquad
 D(t)=10t^2+4,\quad B(t)=-t^3+t^2-6.
\]

The root equation \(P(w)=0\), divided by \(v^3\), gives

\[
 T(t^{19}+4t^2-5)+4t^3-3t^2-1=0.
\]

The two roots of \(D\) are 6 and 7; the corresponding values of \(B\) are 9 and 12. Therefore \(D(t)\ne0\), so \(T=B(t)/D(t)\). The ratio must satisfy

\[
 U(t)=B(t)(t^{19}+4t^2-5)+D(t)(4t^3-3t^2-1)=0.
\]

Explicitly,

\[
 U(t)=-t^{22}+t^{21}-6t^{19}-3t^5-5t^3+t^2.
\]

## 3. A small resultant and a univariate certificate

The two equations for \(v\) imply

\[
 R(T):=\operatorname{Res}_v\bigl(v^{16}-T,\ (5T+1)v^3+(3-4T)v-5\bigr)=0.
\]

All following coefficient arrays are in ascending powers, with entries represented in \(\{0,\ldots,12\}\). The exact degree-19 resultant is

```
R = [1,11,0,11,9,1,5,9,0,10,8,4,11,10,4,0,12,4,8,12].
```

Let \(H(t)\) be the remainder of \(D(t)^{19}R(B(t)/D(t))\) on division by \(U(t)\). Then

```
H = [6,0,10,0,3,4,1,9,2,9,7,12,9,1,8,4,4,3,11,2,10,5].
```

The following two coefficient arrays define polynomials \(C_U,C_H\) satisfying the exact identity

\[
 \boxed{C_U(t)U(t)+C_H(t)H(t)=1\quad\text{in }\mathbb F_{13}[t].}
\]

```
CU = [2,4,0,1,6,9,7,10,2,10,8,8,0,5,2,7,0,7,2,1,4],
CH = [11,0,3,1,8,7,9,1,9,8,2,0,2,7,7,6,4,9,0,10,3,6].
```

Their degrees are 20 and 21. The arrays have 43 coefficient slots, of which 37 are nonzero. A hypothetical pair of witnesses would give \(U(t)=H(t)=0\), contradicting the identity. This proves the lemma.

## 4. How the finite calculation is checked

The producer first reduces \(A^{16}v^{16}\) modulo the cubic. If \((q_0,q_1,q_2)\) represents \(A^kv^k\), multiplication by \(Av\) gives the recurrence

\[
(q_0,q_1,q_2)\longmapsto
(5q_2,\ A q_0-(3-4T)q_2,\ A q_1).
\]

After 16 steps, subtract \(TA^{16}\) from the constant coordinate and take the resultant of this quadratic remainder and the cubic by a \(5\times5\) Sylvester determinant. The raw determinant is \(A^{34}R(T)\). Since \(A\ne0\) in the relevant case, stripping that factor is legitimate.

The independent checker does **not** use that reduction. It forms the full \(19\times19\) Sylvester matrix for \(v^{16}-T\) and \(Q(v,T)\), computes its determinant by exact polynomial Bareiss elimination, and obtains the displayed \(R\) directly. It then independently reconstructs \(U,H\), multiplies the displayed Bezout identity, and rejects a deliberately altered coefficient. It checks the scalar identities for all zero-coefficient cases and both denominator roots. Ordinary and optimized Python runs pass.

The producer's original elapsed-time receipt is frozen. Replay uses `verify_last_mask.py` and does not rewrite that receipt.

## 5. Characteristic-zero consequence and remaining frontier

For a characteristic-zero degree-20 CA polynomial translated to any chosen root, assume its nonleading deficiency support is contained in

\[
 T_{\mathrm{new}}=\{8,9,10,11,12,16,17,19\}.
\]

Valuation normalization at 13 makes every root integral and retains a root at 1. Lucas reduction removes indices 8 through 12, leaving precisely the family in the lemma, including all coefficient degenerations. The reduced polynomial cannot be the monomial because it still has the root 1. This contradiction excludes the entire support mask \(T_{\mathrm{new}}\).

In the separately checked six-total-term enumeration, this removes the support

\[
 \{8,10,16,17,19\}.
\]

It leaves exactly three necessary support candidates:

\[
 \{3,4,10,18,19\},\qquad
 \{3,10,16,17,19\},\qquad
 \{4,5,10,17,19\}.
\]

No claim is made that these candidates are realizable, that the full six-term class is excluded, or that this finite-characteristic lemma is historically new. The proof and exact arithmetic have internal checks, not external referee or proof-assistant assurance.
