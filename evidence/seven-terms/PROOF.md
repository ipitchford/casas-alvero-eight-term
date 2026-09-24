# Excluding the last centered six-term family in degree 20

23 September 2026. Research proof with exact arithmetic certificates and internal audits. External review and historical novelty are separate questions.

## The result

**Theorem C.** Over a field of characteristic zero, there is no Casas–Alvero polynomial of the form
\[
f=X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\qquad ABCDE\ne0.
\]

**Corollary.** Every nontrivial degree-20 Casas–Alvero polynomial has at least **seven nonzero monomials after centering**, including the leading term.

Here a polynomial is Casas–Alvero (CA) if it shares a root with each of its derivatives of orders 1 through 19. Centering means translating the unique root of its nineteenth derivative to zero; that point is also a root of the polynomial. We then make the polynomial monic. The corollary is a bound on coefficients, not on distinct roots or recycled derivative witnesses. Neither statement resolves the unrestricted degree-20 case or the full conjecture.

The corollary uses the preceding six-term lower bound and exhaustive support reduction, which left precisely the exponent support in Theorem C after excluding two other families. These are bundled, unchanged, in [the preceding package](dependencies/casas-alvero-sixterm/PROOF.md). The present proof supplies the previously missing exclusion of C.

## 1. Valuation normalization and the finite residue classification

Pass to a field containing the roots and extend a 13-adic valuation. Write its valuation ring as \(O\), maximal ideal as \(\mathfrak m\), and residue field as \(\kappa\). All inequalities below allow ramification; integer or half-integer bounds denote multiples of \(\nu(13)\), normalized to 1. The same unique-minimum arguments work in an ordered value group. A zero difference has valuation infinity.

Since zero is a root, scale a nonzero root of least valuation to 1 and make the polynomial monic again. Every root and ordinary coefficient is integral, and a unit root remains. If \(z\) is an order-10 common root, then
\[
0=H_{10}f(z)=184756z^{10}+8008Az^6+3003Bz^5+C.
\]
The three displayed numerical coefficients are divisible by 13, so \(C\in13O\). The reduced polynomial is therefore
\[
h=X^{20}+aX^{16}+bX^{15}+dX^3+eX,
\]
and is nonmonomial because a nonzero residue root remains. Each Hasse common-root condition reduces. We use Hasse derivatives throughout; in characteristic zero they have the same roots as the ordinary derivatives.

The coefficient \(A\) is a unit. Indeed, a nonmonomial reduced CA seed with \(a=e=0\) is impossible: if \(b=0\), the two-term root and order-3 equations contradict each other; if \(b\ne0\), scaling an order-15 witness gives \(b=5,d=7\), and an order-3 witness would satisfy \(v^{17}=5,v^5=-1\), forcing \(v^2=8\) and then \(v=1\), a contradiction. Thus \(a=0\) would imply \(e\ne0\). But \(\overline{H_{16}f}=9X^4\), so its common root would reduce to the simple root zero of \(h\), forcing that exact root to be zero and hence \(A=0\). This contradicts exact support.

An order-16 common root is consequently a unit. Scale it to 1, preserving integrality. Then
\[
A=-4845,
\quad f(1)=0,
\quad E=-1-A-B-C-D.
\tag{1}
\]
Let \(u,v,w,z\) be common-root witnesses for Hasse orders 15, 3, 1, 10, respectively.

The preceding exact residue classification, valid over every algebraically closed field of characteristic 13, gives three possible coefficient tuples
\[
(a,b,d,e)=(4,6,3,12),\ (4,6,2,0),\ (4,6,10,5).
\]
Its [proof and resultant certificates](dependencies/casas-alvero-sixterm/C/UNIVARIATE_CLASSIFICATION.md), including zero-coefficient charts and extension-field witnesses, are bundled. At the middle point \(\gcd(h,h')=X^2\), so a first-derivative witness \(w\ne0\) reduces to zero. Subtracting \(f(w)/w\) from \(f'(w)\) gives
\[
19w^{19}+15Aw^{15}+14Bw^{14}+9Cw^9+2Dw^2=0.
\]
The last term has uniquely least valuation because \(D\) is a unit. This excludes that point, including its two extension-field order-15 witnesses.

The complete surviving list is as follows. The equalities follow by counting roots, with multiplicity, in each residue cluster: a simple residue root has a unique exact root above it, and a repeated exact root exhausts a cluster of size two.

| Row | \(\bar v\) | \(\bar u\) | \(\bar w\) | Forced exact equality |
|---:|---:|---:|---:|---|
| 1 | 2 | 1 | 1 | \(u=w=1\) |
| 2 | 2 | 1 | 4 | None at this stage |
| 3 | 2 | 2 | 1 | \(u=v,\ w=1\) |
| 4 | 2 | 2 | 4 | \(u=v\) |
| 5 | 11 | 1 | 3 | \(u=1\) |
| 6 | 11 | 1 | 11 | \(u=1,\ v=w\) |

The first four rows have residue polynomial
\(h_3=X^{20}+4X^{16}+6X^{15}+3X^3+12X\);
the last two have
\(h_{10}=X^{20}+4X^{16}+6X^{15}+10X^3+5X\).
The rest of the proof excludes all six rows.

## 2. Two elementary valuation observations

**Unit Jacobian bound.** Let \(F_1,\ldots,F_n\) be integral polynomial equations in deviations \(x_1,\ldots,x_n\in\mathfrak m\). Suppose the constant defects have valuation at least \(\lambda>0\), the Jacobian matrix at zero is invertible over \(O\), and any additional parameter perturbations have valuation at least \(\lambda\). Then each \(\nu(x_i)\ge\lambda\).

For otherwise put \(\gamma=\min_i\nu(x_i)<\lambda\). Multiplication by an invertible integral matrix preserves the minimum coordinate valuation. The linear part has minimum valuation \(\gamma\), whereas the constant and parameter terms have larger valuation, and all remaining terms have valuation greater than \(\gamma\) because they are quadratic in positive-valuation deviations or contain an additional perturbation. The equations cannot vanish. This is a valuation comparison, not an assumption of unramified lifting.

**Triple-cluster bound.** Suppose the coefficients of \(f\) differ by elements of \(13O\) from an integer polynomial whose reduction has a triple root at 4, with \(f'''(4)/2\) a unit. If \(w\equiv4\pmod{\mathfrak m}\) and \(f'(w)=0\), Taylor expansion shows
\[
\nu(w-4)\ge\tfrac12.
\]
Otherwise the quadratic term of \(f'(4+(w-4))\) would have uniquely least valuation: its constant and linear coefficients lie in \(13O\). If also \(f(w)=0\), expansion of \(f\) then gives \(\nu(f(4))>1\). Thus reduction of \(f(4)/13\) is zero, even if \(w-4\notin13O\). This distinction is crucial.

## 3. Rows with u=1 exactly

The order-15 equation at 1 gives \(B=B_0=62016\). At residue pairs \((v,D)=(2,3)\) and \((11,10)\), the Jacobians of \((f(v),H_3f(v))\) in \((v,D)\) reduce respectively to
\[
\begin{pmatrix}9&6\\4&1\end{pmatrix},\qquad
\begin{pmatrix}0&7\\4&1\end{pmatrix}.
\]
Both determinants are 11. Since \(C\in13O\), the unit Jacobian bound proves
\[
v=v_0+13t,\qquad D=d_0+13l,\qquad C=13k,
\quad t,l,k\in O.
\tag{2}
\]
These divisibilities are stronger than, and are derived from, the initial residue information.

Dividing the exact equations by 13 and reducing gives, for \((v_0,d_0)=(2,3)\),
\[
9t+6l+8k+12=0,\qquad4t+l+7k+6=0;
\tag{3}
\]
for \((v_0,d_0)=(11,10)\), it gives
\[
7l+12k+2=0,\qquad4t+l+6k+3=0.
\tag{4}
\]
The extra root condition supplies a third equation as follows:

| Pattern \((\bar v,\bar w)\) | Third equation | Solution \((\bar t,\bar l,\bar k)\) |
|---|---|---|
| \((2,1)\) | \(2l+9k+7=0\), from \(f'(1)=0\) | \((1,3,0)\) |
| \((2,4)\) | \(8l+5k+1=0\), from the triple-cluster bound | \((5,7,12)\) |
| \((11,3)\) | \(11l+9=0\), from \(f(w)=0\) | \((8,11,1)\) |
| \((11,11)\) | \(t+11l+k+7=0\), from \(f'(v)=0\) | \((0,6,5)\) |

For \((11,3)\), the reduction of \(f'\) has a simple root at 3, so the unit Jacobian bound first gives \(w-3\in13O\); the displacement then disappears from \(f(w)/13\), because 3 is a double root of \(h_{10}\). For \((11,11)\), the exact equality \(v=w\) justifies \(f'(v)=0\). These facts supply the precision needed for the table.

The monic divided middle derivative is integral and reduces to
\[
g_\lambda=X^{10}+11X^6+7X^5+\lambda,
\qquad \lambda=9\bar k,
\tag{5}
\]
since \(184756=13\cdot14212\) and \(14212\equiv3\pmod{13}\).
Exact Euclidean identities give
\[
\gcd(h_3,g_0)=X,\quad \gcd(h_3,g_4)=1,\quad
\gcd(h_{10},g_9)=\gcd(h_{10},g_6)=1.
\tag{6}
\]
The latter three cases contradict the existence of an integral middle-derivative witness. In the first, that witness must reduce to zero. Zero is a simple residue root, so its exact lift as a root of \(f\) is zero itself, forcing \(H_{10}f(0)=C=0\), also impossible. This excludes rows 1, 5, 6, and the exact \(u=1\) portion of row 2. The complete branch proof and arithmetic are in [u_one/JET_PROOF.md](u_one/JET_PROOF.md).

## 4. The unresolved-cluster row also has enough precision

In row 2, the order-15 equation gives
\[
B=77520u-15504u^5.
\]
Writing \(s=u-1\) gives the exact identity
\[
B-B_0=-15504s^2(10+10s+5s^2+s^3).
\tag{7}
\]
If \(s\ne0\) and \(r=\nu(s)>0\), the right side has valuation \(2r\). The unit Jacobian used at \((v,D)=(2,3)\) now gives
\[
\min\{\nu(v-2),\nu(D-3)\}\ge\min\{1,2r\}.
\tag{8}
\]
Also
\[
f'(1)=13\cdot61198+14(B-B_0)+9C+2(D-3),
\qquad H_2f(1)\equiv9\pmod{\mathfrak m}.
\]
If \(r<1\), the equation
\[
0=\frac{f(u)-f(1)}{u-1}
 =f'(1)+H_2f(1)s+H_3f(1)s^2+\cdots
\]
has a unique term of least valuation, namely \(H_2f(1)s\): the first term has valuation at least \(\min\{1,2r\}>r\), and later terms at least \(2r\). Hence \(r\ge1\).

Thus \(B-B_0\in13^2O\), and \(v-2,D-3\in13O\). The same conclusions hold if \(s=0\). Every first-jet equation for the \((2,4)\) case in Section 3 is consequently unchanged, including the triple-cluster estimate. It forces \(\bar k=12\) and \(\gcd(h_3,g_4)=1\), excluding all of row 2. [Complete proof](cluster/PROOF.md).

## 5. The two rows with u=v

Now \(\bar u=\bar v=2\) and \(u=v\) exactly. Substitute
\[
B(u)=77520u-15504u^5
\]
in the two exact equations \(f(u)=H_3f(u)=0\). Their Jacobian in \((u,D)\), at \((2,3)\), is
\[
\begin{pmatrix}10&6\\4&1\end{pmatrix}\pmod{13},
\qquad\det=12.
\]
This includes differentiation of \(B(u)\). The unit Jacobian bound proves
\[
u=2+13r,\quad D=3+13l,\quad C=13k,
\qquad r,l,k\in O.
\]
The first two divided equations are
\[
10r+6l+8k+7=0,\qquad4r+l+7k+6=0
\quad\text{in }\kappa.
\tag{9}
\]

For row 4, the triple-cluster argument at \(w\equiv4\) gives
\[
10r+8l+5k+3=0.
\]
Its solution with (9) is \((\bar r,\bar l,\bar k)=(5,7,12)\). Equation (6) again supplies a contradiction.

For row 3, \(w=1\) exactly, so \(f'(1)=0\) supplies
\[
11r+2l+9k+4=0.
\]
The solution is \((\bar r,\bar l,\bar k)=(12,3,3)\). This time
\[
\gcd(h_3,g_1)=X-4,
\qquad g_1'(4)=3,
\tag{10}
\]
so the middle witness reduces to 4. A further precision step is necessary.

After the substitutions, each exact polynomial \(f(u),H_3f(u),f'(1)\) is divisible by 13 in \(\mathbb Z[r,l,k]\). The reductions of these divided equations are the three affine linear equations just displayed, whose coefficient matrix is invertible. Apply the unit Jacobian bound a second time, now around \((r,l,k)=(12,3,3)\). It proves
\[
r-12,\ l-3,\ k-3\in13O.
\tag{11}
\]
In particular the divided middle derivative at the integer point 4 belongs to \(13O\), and its derivative there is a unit by (10). The one-variable bound therefore gives \(z-4\in13O\). But direct expansion gives
\[
\overline{f(4)/13}
 =10\bar r+8\bar l+5\bar k+3=6\ne0.
\tag{12}
\]
Since \(f'(4),H_2f(4)\in13O\) and \(z-4\in13O\), Taylor expansion shows \(f(z)-f(4)\in13^2O\). Equation (12) contradicts \(f(z)=0\).

Thus rows 3 and 4 are excluded as well. The [complete collision-branch proof](u_equals_v/JET_PROOF.md) includes the exact jet checker. A separately reconstructed characteristic-zero resultant calculation supplies an alternative exclusion of these two rows; the short proof above does not depend on that larger computation.

## 6. Coverage and verification boundary

The residue classification and the root-cluster table are exhaustive, and Sections 3–5 exclude every row. This proves Theorem C. The preceding finite support sieve and A/B exclusions then prove the seven-term corollary.

All displayed constants, Jacobians, linear-system solutions, root multiplicities, and polynomial gcds are derived from exact integer Hasse formulas in the supplied standard-library checkers. Independent internal reconstructions audit both arithmetic and the valuation implications. The first- and second-precision bounds are mathematical arguments, not conclusions from unramified modular searches. No existence of a characteristic-zero lift is presumed from a residue point.

The proof is an unpublished computer-assisted research result. Exact replay, internal review, formal verification, external refereeing, historical priority, and publication significance remain distinct. This result supplies a necessary sparsity condition only; it does not prove the full Casas–Alvero conjecture.
