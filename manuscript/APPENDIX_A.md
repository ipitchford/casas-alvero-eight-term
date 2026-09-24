# Appendix A. Excluding six or fewer terms

This appendix proves the intermediate seven-term bound used in the main theorem. The finite identities needed in that proof are specified below, including their defining polynomials, coefficient-zero charts, verification bounds, and supplemental files. Earlier dossiers are not additional mathematical assumptions. The result concerns a restricted class of hypothetical counterexamples; it does not settle degree 20 or the Casas–Alvero conjecture.

## A.1. Statement, conventions, and specialization

For a polynomial \(f=\sum c_iX^i\), write
\[
H_kf=\sum_{i\ge k}\binom{i}{k}c_iX^{i-k}.
\]
In characteristic zero, \(f^{(k)}=k!H_kf\), so the ordinary and Hasse common-root conditions agree. Say that \(f\) has the CA property if \(f\) and \(H_kf\) have a common root for every \(1\le k<\deg f\). Roots are taken in an algebraic closure. The polynomial is nontrivial if it is not a scalar multiple of a power of a linear polynomial.

Let \(\alpha\) be the unique root of \(H_{19}f\). The CA property implies \(f(\alpha)=0\). Translate \(\alpha\) to zero and make the polynomial monic. Its centered form is
\[
F(X)=X^{20}+\sum_{j\in S}c_jX^{20-j},
\qquad S\subseteq\{2,\ldots,19\},\quad c_j\ne0.
\tag{S1}
\]
The indices \(j\) are **deficiencies**, not exponents or derivative orders. There are exactly \(1+|S|\) nonzero monomials. Changing scale \(X\mapsto rX\), \(r\ne0\), does not change \(S\).

**Proposition A.** Every nontrivial characteristic-zero degree-20 polynomial with the CA property has at least seven nonzero monomials in its centered form.

We first record the specialization argument used throughout. Extend the \(p\)-adic valuation to a field containing the coefficients and all roots. Choose a nonzero root \(\rho\) of minimum valuation, and replace \(F(X)\) by \(\rho^{-20}F(\rho X)\). All roots are integral and a root equals 1. In binomial normalization write
\[
F(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\qquad a_0=1,\quad a_1=a_{20}=0.
\]
The monic normalized derivative of degree \(j\) is
\[
G_j(X)=\frac{H_{20-j}F(X)}{\binom{20}{j}}
      =\sum_{i=0}^{j}\binom ji a_iX^{j-i}.
\]
At an integral common root \(\beta_j\), its equation expresses \(a_j\) as an integral polynomial in \(a_0,\ldots,a_{j-1},\beta_j\). Induction proves \(a_j\) integral. Therefore reduction deletes every ordinary coefficient whose binomial multiplier is divisible by \(p\). It preserves common-root witnesses for the Hasse derivatives and retains a nonzero root. In particular, the reduction is not \(X^{20}\).

No assertion about an arbitrary affine special fiber is used here: integrality and the retained unit root are established before reduction. The argument permits ramification, coefficient degeneration, and coincident witnesses. A valuation extension of the coefficient field is sufficient; the elementary minimum-valuation arguments below also work in an ordered value group. Alternatively, for this finite algebraic existence question one may first specialize an assumed exact-support solution to an algebraic characteristic-zero solution, encoding the nonzero coefficients by inverse variables, and then work over a finite extension of \(\mathbf Q_p\).

## A.2. Published restrictions and the complete finite support step

The proof uses two published arithmetic restrictions. The first is reproduced here as an elementary support test. The second is the determinant theorem of Castryck, Laterveer, and Ounaïes.

For a prime \(p\), put
\[
V_p=\{j\in\{2,\ldots,19\}:p\nmid\binom{20}{j}\}.
\]
The normalization above shows that \(S\cap V_p\ne\varnothing\). If \(S\cap V_p=\{r\}\), the reduction is \(X^{20}+aX^{20-r}\), with \(a\ne0\). A common root with \(H_{20-r}\) is nonzero, and the root and derivative equations imply
\[
\binom{20}{r}\equiv1\pmod p.
\tag{S2}
\]
This test includes coefficient loss: the remaining visible coefficient cannot also disappear because a unit root was retained.

For completeness, the two-visible test is stated with the necessary degeneration guards. It is the deficiency-index form of de Frutos Marín's two-support criterion [deFrutos]: *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, Theorem 3.5.1 and Proposition 3.5.5, printed pp. 55–57 ([thesis and repository record](https://uvadoc.uva.es/handle/10324/3602?show=full), DOI 10.35376/10324/3602). If \(S\cap V_p=\{r,s\}\), \(r<s\), define in \(\mathbf F_p\)
\[
B=\binom{20}{r},\quad D=\binom{20}{s},\quad
C=\binom{20-r}{s-r},\quad g=\gcd(r,s),
\]
\[
N=B^{s/g}(C-1)^{(s-r)/g}(D-C)^{r/g}
 -(B-1)^{r/g}(D-1)^{s/g}.
\tag{S3}
\]
If \(B,D\notin\{0,1\}\), a necessary condition is \(N=0\). The guard excludes singleton degenerations; it must not be omitted.

Here is a direct derivation. Both reduced coefficients must be nonzero by (S2). Normalize the common root for order \(20-r\) to 1. The two coefficients then become \(-B\) and \(B-1\). For a nonzero common root \(v\) for order \(20-s\), subtraction of the root and derivative equations gives
\[
(D-C)v^s=(C-1)(B-1),\qquad
B(D-C)v^{s-r}=(D-1)(B-1).
\]
The second equality rules out \(D=C\), and the first then rules out \(C=1\). Taking powers after division gives (S3). Thus this finite support test can be checked without relying on an unquoted source formula.

The other imported restriction is [Castryck–Laterveer–Ounaïes, Theorem 2](https://arxiv.org/html/1208.5404) [CLO]. For degree \(p+1=20\), the centered root is simple, and, with
\[
Z=\{j:2\le j\le18,\ j\notin S\},
\]
the following determinant is zero modulo 19:
\[
\Delta(Z)=
\det\begin{pmatrix}
\bigl[-1,\ (j\binom{j-2}{k-2}\mathbf1_{k\le j})_{k\in Z}\bigr]_{j\in Z}\\
-1,\ ((-1)^k)_{k\in Z}
\end{pmatrix}.
\tag{S4}
\]
The rows and columns indexed by \(Z\) are in increasing order. The indices in this formula are the **missing deficiency indices**. In particular, simplicity gives \(19\in S\). This is the only determinant theorem imported here.

The elementary tests already give four disjoint required sets:
\[
\{19\},\qquad\{4,16\},\qquad
\{5,10,15\},\qquad\{2,3,17,18\}.
\tag{S5}
\]
They come from primes \(19,2,5,17\), respectively; at 17 a singleton at 19 is forbidden by \(20\not\equiv1\). Hence \(|S|\ge4\), without importing an earlier sparsity result.

Apply (S2) and (S3) at \(p=2,3,5,7,11,13,17,19\), then (S4), to all subsets of \(\{2,\ldots,19\}\) of size 4 or 5. This is the entire finite support calculation:

| Number of nonleading terms | All subsets | After visible/singleton tests | After guarded two-visible test | After determinant |
|---:|---:|---:|---:|---:|
| 4 | 3060 | 8 | 4 | 1 |
| 5 | 8568 | 100 | 54 | 5 |

The size-four survivor is \(\{4,10,17,19\}\). The five size-five survivors, named here once and for all, are:

| Family | Deficiency support \(S\) | Ordinary exponent support |
|---|---|---|
| A | \(\{3,4,10,18,19\}\) | \(\{20,17,16,10,2,1\}\) |
| B | \(\{3,10,16,17,19\}\) | \(\{20,17,10,4,3,1\}\) |
| C | \(\{4,5,10,17,19\}\) | \(\{20,16,15,10,3,1\}\) |
| D | \(\{4,10,12,17,19\}\) | \(\{20,16,10,8,3,1\}\) |
| E | \(\{8,10,16,17,19\}\) | \(\{20,12,10,4,3,1\}\) |

All operations in this sieve are explicit small integer or finite-field operations in (S2)–(S4). Supplemental code verifies the determinants both by integer Bareiss elimination and modular Gaussian elimination; the degree-12 example printed after CLO Theorem 2 is an indexing control. No search for polynomial coefficients enters this step.

The archived implementation additionally applies the restrictions \(S\cap\{5,10\}\ne\varnothing\) and \(S\cap\{10,15\}\ne\varnothing\), available from the degree-20 characteristic-5 calculation in the proof of [Massri, Theorem 7.9](https://arxiv.org/html/1806.09561v6) [Massri]. They remove no support after the preceding two-visible tests: the counts remain 4 and 54. They can therefore be omitted from this proof dependency. Neither Massri's three-recycled-root theorem nor any claimed full proof of the conjecture is needed.

## A.3. The characteristic-13 lemma excluding D and the size-four survivor

**Lemma A.3.** Over any algebraically closed field of characteristic 13, the only CA polynomial
\[
h=X^{20}+aX^{16}+cX^3+dX
\]
is \(X^{20}\). Coefficients are allowed to vanish.

If \(a=0,c\ne0\), normalize an \(H_3\) common root to 1. Then \(c=4,d=8\). A common \(H_1\) root \(w\ne0\) satisfies
\[
w^{19}+4w^2+8=7w^{19}+12w^2+8=0,
\]
so \(w^2=10,w^{19}=4\). Since \(10^9=-1\), this forces \(w=9\), inconsistent with \(9^2=3\). If \(a=c=0,d\ne0\), the root and first-derivative equations give \(-d=w^{19}\) and \(-d=7w^{19}\), also impossible.

If \(a\ne0\), normalize an \(H_{16}\) common root to 1, giving \(a=4\). Choose a nonzero \(H_3\) common root \(v\). This is forced when \(c\ne0\); when \(c=0\), \(v=1\) is available because \(H_3h(1)=9+4=0\). The equations yield
\[
c=4v^{17}-4v^{13},\qquad d=-5v^{19},
\qquad F(v)=5v^{19}-4v^{17}+4v^{13}-5=0.
\]
Thus \(v,d\ne0\). For an \(H_1\) common root \(w\ne0\), subtracting \(h'(w)\) from \(3h(w)/w\) gives \(w^{19}=4v^{19}\). With \(t=w/v\), \(T=v^4\),
\[
M(t)=t^{19}-4=0,\qquad
(4t^2-1)T=4(t^2-t^{15}).
\]
The zeros 6 and 7 of \(D(t)=4t^2-1\) have nineteenth powers 7 and 6, so \(D\ne0\). Put \(B(t)=4(t^2-t^{15})\), so \(T=B/D\). Substituting \(v^4=T\) in \(F(v)=0\) gives
\[
5T^4v^3+4T^3(1-T)v=5.
\]
Squaring, using \(v^4=T\), and squaring once more yields the necessary equation
\[
R(T)=(T^9-T^8-1)^2-T^{13}(-T^3+3T^2-6T+3)^2=0.
\]
No factor in this expression has been divided out. The remainder of \(D^{19}R(B/D)\) modulo \(M\) is
\[
\begin{aligned}
H={}&5t^{18}-6t^{17}-3t^{16}+3t^{15}-2t^{14}-6t^{13}
+t^{11}+3t^{10}\\
&-t^8+t^7-t^6+3t^5+6t^4+5t^3-4t^2+6.
\end{aligned}
\tag{S6}
\]
But \(M=(t-4)Q\), where \(Q=\sum_{j=0}^{18}4^jt^{18-j}\) is irreducible: its roots are 4 times the primitive nineteenth roots of unity, and \(\operatorname{ord}_{19}(13)=18\). The latter order follows from \(13^6=11\) and \(13^9=-1\pmod{19}\). Now \(H(4)=8\), and \(H\ne5Q\), since their \(t^{16}\) coefficients are 10 and 2. Thus \(M,H\) are coprime, a contradiction.

At 13 the invisible deficiency indices are 8 through 12. Lemma A.3 and A.1 therefore exclude the entire characteristic-zero closed support mask
\[
T_D=\{4,8,9,10,11,12,17,19\}.
\tag{S7}
\]
This removes D and the size-four survivor, proving already that a nontrivial centered polynomial needs at least six terms. Notice that this implication does not require every allowed coefficient to be nonzero.

## A.4. The characteristic-13 lemma excluding E

**Lemma A.4.** The only characteristic-13 CA polynomial
\[
h=X^{20}+aX^4+cX^3+dX
\]
is \(X^{20}\).

The case \(a=0\) is the first boundary argument of A.3. If \(a\ne0\), normalize an \(H_4\) common root to 1; then \(a=4,d=-5-c\). If \(c=0\), the first-derivative common-root equations imply \(w^3=9,w^{19}=8\), hence \(w=8\), inconsistent with \(8^3=5\).

Choose an \(H_3\) witness \(v\ne0\), and put \(T=v^{16}\). The equations give
\[
c=v(4T-3),\qquad d=-v^3(5T+1),\qquad
Q(v,T)=(5T+1)v^3+(3-4T)v-5=0.
\]
If \(d=0\), then \(T=5,c=8,v=2\), inconsistent with \(2^{16}=3\). Thus a first-derivative witness \(w\) is nonzero. Set \(t=w/v\). Subtracting seven times \(h(w)/w\) from \(h'(w)\) and then using the root equation gives
\[
D(t)T=B(t),\quad D=10t^2+4,\quad B=-t^3+t^2-6,
\]
\[
U(t)=B(t)(t^{19}+4t^2-5)+D(t)(4t^3-3t^2-1)=0.
\]
At the two zeros 6 and 7 of \(D\), the values of \(B\) are 9 and 12, so \(D\ne0\). Explicitly,
\[
U=-t^{22}+t^{21}-6t^{19}-3t^5-5t^3+t^2.
\]
Define
\[
R(T)=\operatorname{Res}_v(v^{16}-T,Q(v,T)),\qquad
H(t)=D^{19}R(B/D)\bmod U.
\]
Here and below arrays list coefficients in ascending degree in \(\mathbf F_{13}\). The complete small certificate is

    R  = [1,11,0,11,9,1,5,9,0,10,8,4,11,10,4,0,12,4,8,12]
    H  = [6,0,10,0,3,4,1,9,2,9,7,12,9,1,8,4,4,3,11,2,10,5]
    CU = [2,4,0,1,6,9,7,10,2,10,8,8,0,5,2,7,0,7,2,1,4]
    CH = [11,0,3,1,8,7,9,1,9,8,2,0,2,7,7,6,4,9,0,10,3,6].

Direct multiplication gives \(C_UU+C_HH=1\). A putative solution has \(U=H=0\), contradiction. The resultant is independently checked as the determinant of the full \(19\times19\) Sylvester matrix, rather than by the producer's reduced \(5\times5\) determinant.

Valuation reduction now excludes the closed characteristic-zero deficiency mask
\[
T_E=\{8,9,10,11,12,16,17,19\},
\]
and hence family E.

## A.5. The larger characteristic-13 exclusion for B

**Lemma A.5.** The only characteristic-13 CA polynomial
\[
h=X^{20}+aX^{17}+bX^4+cX^3+dX
\tag{S8}
\]
is \(X^{20}\).

The chart \(a=0\) is Lemma A.4. If \(a\ne0\), normalize an \(H_{17}\) common root to 1, so \(a=4,d=-5-b-c\). The remaining active Hasse derivatives are
\[
H_4h=9X^{16}+4X^{13}+b,\quad
H_3h=9X^{17}+3X^{14}+4bX+c,
\]
\[
H_1h=7X^{19}+3X^{16}+4bX^3+3cX^2+d.
\]
For the whole chart \(b=0\), choose arbitrary witnesses \(v,w\) for orders 3 and 1 and substitute \(c=-9v^{17}-3v^{14},d=-5-c\). In \(\mathbf F_{13}[v,w]\), define
\[
F_3=v(5v^{19}+v^{16}+d),\quad
F_0=w(w^{19}+4w^{16}+cw^2+d),\quad
F_1=7w^{19}+3w^{16}+3cw^2+d.
\]
The supplemental sparse polynomials \(L_3,L_0,L_1\), with respectively 680, 694, and 712 terms, satisfy
\[
L_3F_3+L_0F_0+L_1F_1=1.
\tag{S9}
\]
This is ordinary ideal membership, with no saturation and no assumption \(c,d,v,w\ne0\).

For \(b\ne0\), an \(H_4\) witness \(u\) is nonzero and
\[
b=4u^{13}(u^3-1),\qquad c(u^2-1)=5+b-5u^{19}.
\]
The case \(u=1\) would give \(b=0\); at \(u=-1\) the second equation is inconsistent. Thus put
\[
q=u+1,\quad C=\frac{5+b-5u^{19}}{u-1},\quad D=q(-5-b)-C.
\]
The quotient defining \(C\) is a polynomial, of degree 18. The actual coefficients are \(c=C/q,d=D/q\), and \(q\ne0\). Define
\[
P=q(X^{19}+4X^{16}+bX^3)+CX^2+D,
\]
\[
J_3=q(9X^{17}+3X^{14}+4bX)+C,\quad
J_1=q(7X^{19}+3X^{16}+4bX^3)+3CX^2+D,
\]
and \(R_i=\operatorname{Res}_X(P,J_i)\), \(i=3,1\).
A zero common root for order 3 forces \(C=0\); a nonzero one forces \(R_3=0\). Therefore the necessary equation is \(CR_3=0\), and similarly \(DR_1=0\). The supplemental univariate multipliers satisfy
\[
A(u)C(u)R_3(u)+B(u)D(u)R_1(u)=(u+1)^{17}.
\tag{S10}
\]
Its left side vanishes at a solution and its right side does not. This proves the lemma.

The saved resultant degrees are 359 and 395. The coefficient degrees of \(P,J_3,J_1\) in \(u\) are at most 18, so the Sylvester bounds are 648 and 684. Independent exact evaluation at 685 distinct elements of \(\mathbf F_{13^3}\), excluding \(u=-1\) to preserve leading degrees, certifies the entire two resultant polynomials. Multiplication then checks (S9) and (S10) coefficient by coefficient. This is an identity check over an extension field with a proved degree bound, not a search for the absence of rational points.

The resulting characteristic-zero closed mask is
\[
T_B=\{3,8,9,10,11,12,16,17,19\}.
\]
It contains family B.

## A.6. Family A: a nonempty reduction that forces exact collisions

Family A needs a different argument because its reduced coefficient family does contain a nontrivial CA polynomial.

Consider
\[
h=X^{20}+aX^{17}+bX^{16}+cX^2+dX
\]
in characteristic 13. Its active derivatives are
\[
H_{17}=9X^3+a,\quad H_{16}=9X^4+4aX+b,
\]
\[
H_2=8X^{18}+6aX^{15}+3bX^{14}+c,\quad
H_1=7X^{19}+4aX^{16}+3bX^{15}+2cX+d.
\]
The following complete algebraic classification includes every degeneration.

If \(a=0,b\ne0\), normalize an \(H_{16}\) witness to 1: \(b=4,d=-5-c\). With an \(H_2\) witness \(v\), substitute \(c=-8v^{18}-12v^{14}\). The supplied identity expresses 1 in the ordinary ideal
\[
\bigl(h(v),h(w),7w^{19}+12w^{15}+2cw+d\bigr)
\subset\mathbf F_{13}[v,w].
\tag{S11}
\]
If \(a=b=0,c\ne0\), normalization gives \(c=5,d=7\). Then \(H_1h-7h/X=X+10\), so its common nonzero root would be 3, whereas \((h/X)(3)=12\). The remaining binomial \(X^{20}+dX\), \(d\ne0\), is excluded as in A.3.

Thus \(a\ne0\). Normalize an \(H_{17}\) witness to 1, giving \(a=4,d=-5-b-c\), and put \(P=h/X\). The conditions for orders 2 and 1 imply
\[
c\,\operatorname{Res}_X(P,H_2h)=0,\qquad
d\,\operatorname{Res}_X(P,H_1h)=0.
\tag{S12}
\]
Multiplication by \(c,d\) retains zero-coefficient charts. There are three univariate cases:

| Case | Parameter and coefficient substitution | Gcd of the two polynomials in (S12) |
|---|---|---|
| \(b=0\) | \(c,\ d=-5-c\) | \(1\) |
| \(H_{16}\)-witness \(u=1\) | \(b=1,\ d=-6-c\) | \(c-4\) |
| \(b\ne0,\ u\ne1\) | \(b=4u^4-3u,\ c=(5+b-5u^{19}-u^{16})/(u-1),\ d=-5-b-c\) | \(1\) |

The last numerator is divisible by \(u-1\); it is a degree-18 polynomial after division. The witnesses there also satisfy \(u\ne0\), since \(b\ne0\). The supplied resultants are exact Sylvester determinants; the checked parameter-degree bounds for the multiplied resultants are \(38,39\) in the first two cases and \(684,702\) in the last. Evaluation at more than each bound over \(\mathbf F_{13^3}\), followed by exact polynomial gcd, proves the table.

Consequently the unique normalized nonmonomial seed is
\[
h_A=X^{20}+4X^{17}+X^{16}+4X^2+3X.
\]
Exact gcds are
\[
\gcd(h_A,H_{17}h_A)=\gcd(h_A,H_{16}h_A)
=\gcd(h_A,H_2h_A)=X-1,
\]
and \(h_A'(1)=11\ne0\).

Now take a characteristic-zero polynomial whose support is contained in A's exponent mask. Apply A.1 at 13; the \(X^{10}\) coefficient disappears, and the preceding classification shows that the \(X^{17}\) coefficient is a unit. Its \(H_{17}\) witness is therefore a unit and may be scaled to 1 while preserving integrality. The other two witnesses reduce to the simple root 1. They equal 1 exactly: the polynomial divided difference
\[
\frac{F(r)-F(1)}{r-1}
\]
is integral and reduces to \(h_A'(1)\), so is a unit; its product with \(r-1\) is zero. This proves exact equality without a completeness or unramified-lifting assumption.

Writing \(t\) for the ordinary \(X^{10}\) coefficient, the exact equations at 1 give
\[
F=X^{20}-1140X^{17}+14535X^{16}+tX^{10}
  +(-1589350-45t)X^2+(1575954+44t)X.
\tag{S13}
\]
Let \(Q=F/X\), and define the exact integer polynomials
\[
R_{10}(t)=\operatorname{Res}_X(Q,H_{10}F),\qquad
R_1(t)=\operatorname{Res}_X(Q,H_1F).
\]
Their degrees are 19 and 28; reduction modulo 101 preserves both degrees and gives gcd 1. Hence they are coprime over \(\mathbf Q\). For \(t\ne0\), an \(H_{10}\) witness is nonzero, forcing \(R_{10}(t)=0\). The \(H_1\) condition always forces \(R_1(t)=0\): if its witness is zero, the linear coefficient vanishes and zero is then also a root of \(Q\). This contradicts coprimality. For \(t=0\), the separately checked value \(R_1(0)\ne0\) supplies the contradiction.

The integer resultants are certified at 30 and 39 distinct integer parameter values by exact Sylvester determinants: the a priori parameter-degree bounds are 29 and 38. This certifies the resultant identities before the degree-preserving modular gcd check. Family A is thus excluded as a closed support, including the \(t=0\) boundary.

## A.7. Family C: reduction, all six residue rows, and ramified precision

It remains to exclude exact support C:
\[
F=X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\qquad ABCDE\ne0.
\tag{S14}
\]
Normalize integrally at 13. An \(H_{10}\) witness gives
\[
184756z^{10}+8008Az^6+3003Bz^5+C=0.
\]
The first three numerical coefficients are divisible by 13; hence \(C\in13O\). The reduced shape is \(h=X^{20}+aX^{16}+bX^{15}+dX^3+eX\).

We must justify normalizing an \(H_{16}\) witness. If \(a=e=0\) in a nonmonomial seed, \(b=0\) gives an immediate root/\(H_3\) contradiction. For \(b\ne0\), normalize an \(H_{15}\) witness to 1; then \(b=5,d=7\), and an \(H_3\) witness would satisfy \(v^{17}=5,v^5=-1\). These imply \(v^2=8,v=1\), a contradiction. Thus \(a=0\) would require \(e\ne0\). But \(\overline{H_{16}F}=9X^4\) would force its witness into the simple residue root zero. Divided-difference uniqueness would make that exact witness zero, contrary to \(A\ne0\). Therefore \(A\) is a unit. Normalize its witness to 1:
\[
A=-4845,\qquad F(1)=0,\qquad E=-1-A-B-C-D.
\tag{S15}
\]

### A.7.1. Exact algebraic classification of the reduced seeds

Write the seed now as \(h=X^{20}+4X^{16}+bX^{15}+cX^3+dX\). Lemma A.3 excludes \(b=0\), so an \(H_{15}\) witness \(u\) is nonzero. At \(u=-1\) the equations give \(h(-1)=10\); treat \(u=1\) separately. For \(u\ne0,\pm1\),
\[
b=5u^5+u,\quad N=5+b-6u^{19}-5u^{15},\quad
C_n=N/(u-1),\quad q=u+1,\quad D_n=q(8-b)-C_n,
\]
\[
c=C_n/q,\qquad d=D_n/q.
\]
Again \(C_n\) is a polynomial of degree 18. Set
\[
P=q(X^{19}+4X^{15}+bX^{14})+C_nX^2+D_n,
\]
\[
J_3=q(9X^{17}+4X^{13})+C_n,\quad
J_1=q(7X^{19}+12X^{15}+2bX^{14})+3C_nX^2+D_n,
\]
and \(R_i=\operatorname{Res}_X(P,J_i)\). The necessary conditions are \(C_nR_3=D_nR_1=0\), including coefficient loss. The exact supplemental identity is
\[
UR_3C_n+VR_1D_n=(u+1)^{17}(u-1)(u-2)(u^2+4u-2).
\tag{S16}
\]
It leaves \(u=2\), giving \((b,c,d)=(6,3,12)\), or \(u^2+4u-2=0\), giving \((6,2,0)\).

For \(u=1\), \(b=6,d=2-c\). Use \(P=X^{19}+4X^{15}+6X^{14}+cX^2+2-c\) and the corresponding unscaled derivatives
\[
J_3=9X^{17}+4X^{13}+c,\quad
J_1=7X^{19}+12X^{15}+12X^{14}+3cX^2+2-c.
\]
A second identity has left side \(UcR_3+V(2-c)R_1\) and right side
\[
(c-2)(c-3)(c-10).
\tag{S17}
\]
Thus the complete list is \((6,3,12),(6,2,0),(6,10,5)\). The generic resultants have degree bounds 648 and 684 and are certified at 685 extension-field points; the special bounds are 36 and 38 and require 39 points. These identities prove completeness over every algebraically closed characteristic-13 field; there is no restriction to base-field coefficients or witnesses.

For the seed \((6,2,0)\), \(\gcd(h,h')=X^2\). In characteristic zero, an \(H_1\) witness \(w\ne0\) must therefore have positive valuation; it cannot be zero because \(E\ne0\). Yet
\[
F'(w)-F(w)/w
=19w^{19}+15Aw^{15}+14Bw^{14}+9Cw^9+2Dw^2=0
\]
has its last term of uniquely least valuation, as \(D\) is a unit. This excludes that entire coefficient point, including its extension-field marked witnesses.

Put
\[
h_3=X^{20}+4X^{16}+6X^{15}+3X^3+12X,\qquad
h_{10}=X^{20}+4X^{16}+6X^{15}+10X^3+5X.
\]
The exact monic gcds that determine the marked roots are
\[
\begin{array}{c|ccc}
 &H_{15}&H_3&H_1\\ \hline
h_3&(X-1)^2(X-2)&X-2&(X-1)(X-4)^2\\
h_{10}&X-1&X-11&(X-3)(X-11).
\end{array}
\]
The relevant multiplicities in \(h_3\) are 1 at 0 and 2, 2 at 1, and 3 at 4; in \(h_{10}\) they are 1 at 0 and 1, and 2 at 3 and 11. These are checked by division and evaluation of Hasse derivatives.

Let \(u,v,w,z\) denote the common-root witnesses for Hasse orders \(15,3,1,10\). The gcds give precisely the six rows below:

| Row | Seed | \(\bar v\) | \(\bar u\) | \(\bar w\) | Exact consequences |
|---:|---|---:|---:|---:|---|
| 1 | \(h_3\) | 2 | 1 | 1 | \(u=w=1\) |
| 2 | \(h_3\) | 2 | 1 | 4 | none initially |
| 3 | \(h_3\) | 2 | 2 | 1 | \(u=v,\ w=1\) |
| 4 | \(h_3\) | 2 | 2 | 4 | \(u=v\) |
| 5 | \(h_{10}\) | 11 | 1 | 3 | \(u=1\) |
| 6 | \(h_{10}\) | 11 | 1 | 11 | \(u=1,\ v=w\) |

The exact consequences use only cluster multiplicity. A simple residue root has a unique exact root above it. A double residue cluster containing an exact repeated root is exhausted by that repeated root; if it also contains the already fixed root 1, the repeated root equals 1. Root counting here is valid because the monic polynomial factors into integral linear factors, whose reductions record the cluster multiplicities.

### A.7.2. Two precision lemmas

Normalize \(\nu(13)=1\). Suppose integral polynomial equations have a zero \(x\) congruent to an integral base point \(b\), their Jacobian at \(b\) is invertible over \(O\), and their defects at \(b\) and any external parameter errors have valuation at least \(\lambda>0\). Then every coordinate of \(x-b\) has valuation at least \(\lambda\). Indeed, if their minimum \(\gamma\) were \(0<\gamma<\lambda\), the linear term would have minimum valuation \(\gamma\), preserved by an invertible integral matrix. Constant errors and all terms quadratic in the deviations have larger valuation. The equations cannot vanish. We call this the **unit-Jacobian bound**.

A second observation is needed at the triple residue root 4 of \(h_3\). Once the coefficients agree with an integer lift modulo \(13O\), \(F'(4),H_2F(4)\in13O\), while \(3H_3F(4)\) is a unit. If \(w\equiv4\) and \(F'(w)=0\), Taylor expansion forces \(\nu(w-4)\ge1/2\); otherwise its quadratic term has uniquely least valuation. If also \(F(w)=0\), Taylor expansion of \(F\) then shows \(\nu(F(4))>1\). Consequently \(\overline{F(4)/13}=0\). This does **not** claim \(w-4\in13O\).

### A.7.3. The exact \(u=1\) cases

The order-15 equation gives \(B=B_0=62016\). At \((v,D)=(2,3)\) and \((11,10)\), the Jacobians of \((F(v),H_3F(v))\) in \((v,D)\) are respectively
\[
\begin{pmatrix}9&6\\4&1\end{pmatrix},\qquad
\begin{pmatrix}0&7\\4&1\end{pmatrix}
\pmod{13},
\]
both of determinant 11. Since \(C\in13O\), the bound proves
\[
v=v_0+13t,\qquad D=d_0+13l,\qquad C=13k,\qquad t,l,k\in O.
\]
Dividing the exact equations by 13 gives, for \((v_0,d_0)=(2,3)\),
\[
9t+6l+8k+12=0,\qquad 4t+l+7k+6=0;
\tag{S18}
\]
for \((11,10)\), it gives
\[
7l+12k+2=0,\qquad 4t+l+6k+3=0.
\tag{S19}
\]
All equations in the following table are residue equations.

| \((\bar v,\bar w)\) | Additional equation and reason | \((\bar t,\bar l,\bar k)\) |
|---|---|---|
| \((2,1)\) | \(2l+9k+7=0\), from \(F'(1)=0\) | \((1,3,0)\) |
| \((2,4)\) | \(8l+5k+1=0\), by the triple-cluster bound | \((5,7,12)\) |
| \((11,3)\) | \(11l+9=0\), from \(F(w)=0\) | \((8,11,1)\) |
| \((11,11)\) | \(t+11l+k+7=0\), from \(F'(v)=0\) | \((0,6,5)\) |

For the third row, \(h_{10}'\) has a simple root at 3, so first apply the one-variable bound to obtain \(w-3\in13O\); its displacement contributes zero to \(F(w)/13\) because 3 is a double root of \(h_{10}\). In the fourth row, \(v=w\) is an exact collision.

The integral monic middle derivative \(H_{10}F/184756\) reduces to
\[
g_\lambda=X^{10}+11X^6+7X^5+\lambda,\qquad \lambda=9\bar k.
\]
Exact Euclidean gcds are
\[
\gcd(h_3,g_0)=X,\quad\gcd(h_3,g_4)=1,\quad
\gcd(h_{10},g_9)=\gcd(h_{10},g_6)=1.
\tag{S20}
\]
The last three cases are impossible. In the first, the middle witness reduces to the simple root zero and hence is exactly zero; this would give \(C=H_{10}F(0)=0\), contrary to exact support. This excludes rows 1, 5, 6 and the \(u=1\) part of row 2.

### A.7.4. Row 2 without an assumed exact collision

Here the order-15 equation gives \(B(u)=77520u-15504u^5\). For \(s=u-1\),
\[
B(u)-B_0=-15504s^2(10+10s+5s^2+s^3).
\tag{S21}
\]
If \(r=\nu(s)>0\), this has valuation \(2r\). The same two-variable bound now gives
\[
\min\{\nu(v-2),\nu(D-3)\}\ge\min\{1,2r\}.
\]
Moreover
\[
F'(1)=13\cdot61198+14(B-B_0)+9C+2(D-3),
\qquad H_2F(1)\equiv9.
\]
If \(r<1\), the exact divided-difference equation
\[
0=\frac{F(u)-F(1)}{u-1}
 =F'(1)+H_2F(1)s+H_3F(1)s^2+\cdots
\]
has a uniquely smallest term \(H_2F(1)s\): the first term has valuation at least \(\min\{1,2r\}>r\), and the remaining terms have valuation at least \(2r\). Thus \(r\ge1\). It follows that \(B-B_0\in13^2O\) and \(v-2,D-3\in13O\). These conclusions also hold if \(s=0\). The \((2,4)\) first-jet calculation in A.7.3 is unchanged and again gives \(\gcd(h_3,g_4)=1\), excluding all of row 2.

### A.7.5. Rows 3 and 4: the collision \(u=v\)

Substitute \(B(u)=77520u-15504u^5\) in \(F(u)=H_3F(u)=0\). The Jacobian in \((u,D)\) at \((2,3)\), including differentiation of \(B(u)\), is
\[
\begin{pmatrix}10&6\\4&1\end{pmatrix}\pmod{13},
\qquad\det=12.
\]
Hence \(u=2+13r,D=3+13l,C=13k\), with integral \(r,l,k\). The first two divided equations reduce to
\[
10r+6l+8k+7=0,\qquad4r+l+7k+6=0.
\tag{S22}
\]
In row 4, the triple-cluster bound supplies \(10r+8l+5k+3=0\). Together they give \((\bar r,\bar l,\bar k)=(5,7,12)\), so (S20) excludes the row.

In row 3, \(w=1\), and \(F'(1)=0\) gives \(11r+2l+9k+4=0\). The solution is \((12,3,3)\). Here
\[
\gcd(h_3,g_1)=X-4,\qquad g_1'(4)=3,
\]
so the middle witness \(z\) reduces to 4, but a further precision argument is essential. After substitution, the three exact expressions \(F(u),H_3F(u),F'(1)\) are coefficientwise divisible by 13 in \(\mathbf Z[r,l,k]\). Their divided polynomials reduce to the three affine equations above, whose coefficient matrix has determinant 3. Apply the bound again at \((12,3,3)\), obtaining
\[
r-12,\ l-3,\ k-3\in13O.
\tag{S23}
\]
It follows that the monic middle derivative evaluated at 4 lies in \(13O\); its derivative there is a unit. The one-variable bound gives \(z-4\in13O\). But the exact expansion is
\[
\overline{F(4)/13}
=10\bar r+8\bar l+5\bar k+3=6.
\]
Since \(F'(4),H_2F(4)\in13O\), Taylor expansion implies \(F(z)-F(4)\in13^2O\), contradicting \(F(z)=0\). This excludes row 3, completing the proof for C and hence Proposition A.

## A.8. Exact certificate dependencies and their scope

For the accompanying evidence tree, let \(E\) denote `evidence/seven-terms`.
Within \(E\), let \(P\) denote `dependencies/casas-alvero-sixterm`.
Within \(P\), let \(Q\) denote `dependencies/casas-alvero-structural`
and \(R\) denote `dependencies/casas-alvero-extension`.
These aliases locate coefficient data; they do not introduce additional proof assumptions.

| Mathematical item | Exact data / replay, relative to the indicated directory |
|---|---|
| Support sieve (S2)–(S4), five A–E supports | \(Q\): sixterm/old-baseline-and-groups.json; sixterm/old_baseline_and_groups.py; sixterm/enumerate_sixterm.py; sixterm/apply_two_visible.py |
| Lemma A.3 remainder (S6) | \(R\): check_mod13_explanation.py |
| Lemma A.4 resultant and displayed Bézout identity | \(Q\): sixterm/last-mask-probe.json; sixterm/verify_last_mask.py |
| Lemma A.5 identities (S9), (S10) and resultant arrays | \(P\): B/certificate.json; B/verify_certificate.py |
| A boundary ideal identity (S11) | \(P\): A/seed13-a-zero-certificate.txt; A/check_seed_certificates.py zero |
| A univariate classification (S12) | \(P\): A/seed13-univariate.txt; A/check_seed_univariate.py |
| A characteristic-zero resultants of (S13) | \(P\): A/collision-resultants.log; A/check_collision_resultants.py |
| C classification identities (S16), (S17) | \(P\): C/univariate-certificate.json; C/verify_univariate.py |
| C exact jets and gcds (S18)–(S23) | \(E\): u_one/check_jets.py; cluster/check_jets.py; u_equals_v/check_jets.py |
| Separate C arithmetic reconstructions | \(E\): u_one/check_u_equals_v_audit.py; structural_audit/check_independent_jets.py |
| Complete package and six-row coverage replay | \(E\): replay.py; case_coverage.json; MANIFEST.json |

The B certificate has SHA-256
981ff911b8493e9a3cb37dea620dd63249e6bd2bff9c93f16aec2670e88179c7.
The package manifest fixes the other certificate bytes. The B and C resultant replays share a finite-field arithmetic implementation; their independence is from the Singular producer, not from each other. The C jet computations have additional separately written reconstructions.

The theorem depends on the written normalization, denominator, degeneration, root-cluster, and precision arguments, as well as the finite identities. A PASS receipt alone does not establish those arguments. Conversely, the elementary implications do not excuse an unchecked resultant identity. The optional large characteristic-zero resultant proof of C, exploratory Gröbner outputs, and older modular finite-module certificates are not dependencies of this proof.

This is a proof dependency consolidation of an existing result. It makes no assertion of historical novelty, publication significance, external refereeing, proof-assistant verification, or a solution in unrestricted degree 20.

