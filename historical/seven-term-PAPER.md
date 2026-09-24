---
title: "A seven-term bound and local lifting obstructions for degree-twenty Casas–Alvero polynomials"
subtitle: "Scientific manuscript for review"
date: "24 September 2026"
lang: en-GB
---

# Abstract

We prove that a nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least seven nonzero terms after centering at the common root of its nineteenth derivative. The proof reduces small supports to five families and excludes the last family through a complete characteristic-thirteen residue classification and explicit lift obstructions. The specialization and lifting arguments include coefficient degeneration and ramified extensions. We exclude six further exact seven-term supports, reducing the audited seven-term frontier from fourteen possibilities to eight. We also give a multiplicity-preserving factorization of a local resultant norm into marked obstruction values. The latter identifies, but does not resolve, the remaining nonvanishing problem. Exact finite certificates, independent arithmetic checks, and reproducible code accompany the proofs. Neither the unrestricted degree-twenty case nor the general Casas–Alvero conjecture is proved.

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


# A seven-term bound for centered degree-20 Casas–Alvero polynomials

This section gives one proof path for the existing sparsity theorem. The finite identities needed in that proof are specified below, including their defining polynomials, coefficient-zero charts, verification bounds, and supplemental files. Earlier dossiers are not additional mathematical assumptions. The result concerns a restricted class of hypothetical counterexamples; it does not settle degree 20 or the Casas–Alvero conjecture.

## S.1. Statement, conventions, and specialization

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

**Theorem S.** Every nontrivial characteristic-zero degree-20 polynomial with the CA property has at least seven nonzero monomials in its centered form.

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

## S.2. Published restrictions and the complete finite support step

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

## S.3. The characteristic-13 lemma excluding D and the size-four survivor

**Lemma S.3.** Over any algebraically closed field of characteristic 13, the only CA polynomial
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

At 13 the invisible deficiency indices are 8 through 12. Lemma S.3 and S.1 therefore exclude the entire characteristic-zero closed support mask
\[
T_D=\{4,8,9,10,11,12,17,19\}.
\tag{S7}
\]
This removes D and the size-four survivor, proving already that a nontrivial centered polynomial needs at least six terms. Notice that this implication does not require every allowed coefficient to be nonzero.

## S.4. The characteristic-13 lemma excluding E

**Lemma S.4.** The only characteristic-13 CA polynomial
\[
h=X^{20}+aX^4+cX^3+dX
\]
is \(X^{20}\).

The case \(a=0\) is the first boundary argument of S.3. If \(a\ne0\), normalize an \(H_4\) common root to 1; then \(a=4,d=-5-c\). If \(c=0\), the first-derivative common-root equations imply \(w^3=9,w^{19}=8\), hence \(w=8\), inconsistent with \(8^3=5\).

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

## S.5. The larger characteristic-13 exclusion for B

**Lemma S.5.** The only characteristic-13 CA polynomial
\[
h=X^{20}+aX^{17}+bX^4+cX^3+dX
\tag{S8}
\]
is \(X^{20}\).

The chart \(a=0\) is Lemma S.4. If \(a\ne0\), normalize an \(H_{17}\) common root to 1, so \(a=4,d=-5-b-c\). The remaining active Hasse derivatives are
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

## S.6. Family A: a nonempty reduction that forces exact collisions

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
If \(a=b=0,c\ne0\), normalization gives \(c=5,d=7\). Then \(H_1h-7h/X=X+10\), so its common nonzero root would be 3, whereas \((h/X)(3)=12\). The remaining binomial \(X^{20}+dX\), \(d\ne0\), is excluded as in S.3.

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

Now take a characteristic-zero polynomial whose support is contained in A's exponent mask. Apply S.1 at 13; the \(X^{10}\) coefficient disappears, and the preceding classification shows that the \(X^{17}\) coefficient is a unit. Its \(H_{17}\) witness is therefore a unit and may be scaled to 1 while preserving integrality. The other two witnesses reduce to the simple root 1. They equal 1 exactly: the polynomial divided difference
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

## S.7. Family C: reduction, all six residue rows, and ramified precision

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

### S.7.1. Exact algebraic classification of the reduced seeds

Write the seed now as \(h=X^{20}+4X^{16}+bX^{15}+cX^3+dX\). Lemma S.3 excludes \(b=0\), so an \(H_{15}\) witness \(u\) is nonzero. At \(u=-1\) the equations give \(h(-1)=10\); treat \(u=1\) separately. For \(u\ne0,\pm1\),
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

### S.7.2. Two precision lemmas

Normalize \(\nu(13)=1\). Suppose integral polynomial equations have a zero \(x\) congruent to an integral base point \(b\), their Jacobian at \(b\) is invertible over \(O\), and their defects at \(b\) and any external parameter errors have valuation at least \(\lambda>0\). Then every coordinate of \(x-b\) has valuation at least \(\lambda\). Indeed, if their minimum \(\gamma\) were \(0<\gamma<\lambda\), the linear term would have minimum valuation \(\gamma\), preserved by an invertible integral matrix. Constant errors and all terms quadratic in the deviations have larger valuation. The equations cannot vanish. We call this the **unit-Jacobian bound**.

A second observation is needed at the triple residue root 4 of \(h_3\). Once the coefficients agree with an integer lift modulo \(13O\), \(F'(4),H_2F(4)\in13O\), while \(3H_3F(4)\) is a unit. If \(w\equiv4\) and \(F'(w)=0\), Taylor expansion forces \(\nu(w-4)\ge1/2\); otherwise its quadratic term has uniquely least valuation. If also \(F(w)=0\), Taylor expansion of \(F\) then shows \(\nu(F(4))>1\). Consequently \(\overline{F(4)/13}=0\). This does **not** claim \(w-4\in13O\).

### S.7.3. The exact \(u=1\) cases

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

### S.7.4. Row 2 without an assumed exact collision

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
has a uniquely smallest term \(H_2F(1)s\): the first term has valuation at least \(\min\{1,2r\}>r\), and the remaining terms have valuation at least \(2r\). Thus \(r\ge1\). It follows that \(B-B_0\in13^2O\) and \(v-2,D-3\in13O\). These conclusions also hold if \(s=0\). The \((2,4)\) first-jet calculation in S.7.3 is unchanged and again gives \(\gcd(h_3,g_4)=1\), excluding all of row 2.

### S.7.5. Rows 3 and 4: the collision \(u=v\)

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
Since \(F'(4),H_2F(4)\in13O\), Taylor expansion implies \(F(z)-F(4)\in13^2O\), contradicting \(F(z)=0\). This excludes row 3, completing the proof for C and hence Theorem S.

## S.8. Exact certificate dependencies and their scope

For the accompanying evidence tree, let \(E\) denote `evidence/seven-terms`.
Within \(E\), let \(P\) denote `dependencies/casas-alvero-sixterm`.
Within \(P\), let \(Q\) denote `dependencies/casas-alvero-structural`
and \(R\) denote `dependencies/casas-alvero-extension`.
These aliases locate coefficient data; they do not introduce additional proof assumptions.

| Mathematical item | Exact data / replay, relative to the indicated directory |
|---|---|
| Support sieve (S2)–(S4), five A–E supports | \(Q\): sixterm/old-baseline-and-groups.json; sixterm/old_baseline_and_groups.py; sixterm/enumerate_sixterm.py; sixterm/apply_two_visible.py |
| Lemma S.3 remainder (S6) | \(R\): check_mod13_explanation.py |
| Lemma S.4 resultant and displayed Bézout identity | \(Q\): sixterm/last-mask-probe.json; sixterm/verify_last_mask.py |
| Lemma S.5 identities (S9), (S10) and resultant arrays | \(P\): B/certificate.json; B/verify_certificate.py |
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

## S.9. The fourteen-support frontier before the additional exclusions

The frozen unrestricted support inventory contains the following fourteen seven-total-term supports. They are copied from *evidence/full/support_frontier/inventory.json*; no new enumeration is used here:
\[
\begin{array}{lll}
\{2,3,4,10,12,19\},&
\{3,4,9,10,12,19\},&
\{3,4,5,10,13,19\},\\
\{3,4,10,12,15,19\},&
\{3,7,9,10,16,19\},&
\{3,6,10,16,17,19\},\\
\{7,8,10,16,17,19\},&
\{10,12,13,16,17,19\},&
\{6,10,15,16,17,19\},\\
\{9,10,15,16,17,19\},&
\{2,4,10,12,18,19\},&
\{3,4,10,13,18,19\},\\
\{2,4,10,17,18,19\},&
\{4,10,16,17,18,19\}.&
\end{array}
\]
None is eliminated by Theorem S's completed A–E argument: adding an extra coefficient changes both the reduced seed and the exact collision equations. The characteristic-17 and cross-prime analyses elsewhere in the report give necessary restrictions or exclusions for specified residue branches. Those statements must retain their residue and normalization hypotheses; a local branch exclusion is not, by itself, an exclusion of an entire support in this list. The following sections supply the missing global coverage bridge for six of these supports, leaving eight. Neither the A–E argument nor those additional exclusions supplies an eight-term theorem. The remaining coefficient and witness branches, including ramified lifts, are unresolved.


# Global exclusion of the centered support {2,4,10,12,18,19}

24 September 2026. This corollary assembles the existing complete
characteristic-17 seed classification and the existing row-4 support
exclusion. It introduces no new census or lifting computation.

**Corollary.** No nontrivial characteristic-zero degree-20 Casas–Alvero
polynomial has exact centered deficiency support
\[
S=\{2,4,10,12,18,19\}.
\]
Equivalently, after centering the mean root at zero and making the
polynomial monic, there is no CA polynomial of the form
\[
X^{20}+c_2X^{18}+c_4X^{16}+c_{10}X^{10}
+c_{12}X^8+c_{18}X^2+c_{19}X,
\qquad \prod_{j\in S}c_j\ne0.
\]
The leading term is not counted in the deficiency set: this is one exact
seven-monomial support. The assertion is not conditional on already
belonging to row 4.

## Proof

Write
\[
f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\quad a_0=1,\quad a_1=a_{20}=0.
\]
The condition \(a_1=0\) is centering. The CA condition for the nineteenth
derivative makes its root zero a root of \(f\), giving \(a_{20}=0\).
Ordinary and binomial-normalized coefficients have the same exact zero
pattern in characteristic zero.

First reduce to algebraic coefficients. The coefficients and nineteen
chosen common-root witnesses satisfy polynomial equations over
\(\mathbb Q\). Add the equations \(a_j=0\) for every \(j\notin S\),
apart from \(a_0=1\), and
\[
v\prod_{j\in S}a_j=1.
\]
A solution over any characteristic-zero extension makes this ideal
proper; the weak Nullstellensatz supplies a point over
\(\overline{\mathbb Q}\). This retains exact support, not only containment.
It therefore suffices to exclude algebraic points.

Choose a valuation above 17, extend to a field containing all roots,
and divide the variable by a nonzero root of minimum valuation:
explicitly replace \(f(X)\) by \(f(\lambda X)/\lambda^{20}\).
All roots are now integral and one root is exactly one. This operation
sends \(a_j\) to \(a_j/\lambda^j\), so it preserves every exact zero
and nonzero coefficient. No translation is made after centering.

The normalized monic derivatives are
\[
G_j(X)=\frac{H_{20-j}f(X)}{\binom{20}{j}}
=\sum_{i=0}^j\binom ji a_iX^{j-i}.
\]
Every \(G_j\) has a common root \(w_j\) with \(f\); the witness \(w_j\)
is integral. Induction in \(j\), using the coefficient one on \(a_j\),
proves \(a_j\) integral. This step is necessary because ordinary
coefficient integrality alone would not justify Lucas visibility.

For \(4\le j\le16\), the integer \(\binom{20}{j}\) is divisible by
17. All other nonleading coefficients absent from \(S\) vanish exactly.
Thus the reduction has the visible form
\[
h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX
\quad\text{with }b=c=0.
\]
Reducing the ordinary Hasse common-root equations proves that \(h\)
is Hasse–CA. In particular the visible derivatives retain their
common-root identities; the Hasse orders 4 through 16 vanish identically
on the visible model. The reduction is not \(X^{20}\), because the
retained exact root one reduces to a nonzero root.

The complete algebraic-closure classification has nine nonmonomial rows
up to nonzero variable scaling. Only row 4 has both \(b=c=0\).
This remains true if \(a_2,a_{18}\), or \(a_{19}\) initially has positive
valuation; none of those coefficient residues was assumed nonzero.
Indeed, the coefficient-zero boundary charts are included in the
classification, and their only additional all-zero tuple is the already
excluded monomial.

Lift a classification scaling to a unit, extending the local field if
necessary. The resulting reduction is
\[
h=X^{20}-3X^{18}+11X^2+8X.
\]
Centering and exact support are still unchanged. At this stage
\(\bar a_2=-1\). Choose an actual common root \(z\) of \(f\) and
\(G_2=X^2+a_2\). Its reduction is \(1\) or \(-1\). In the row-4 seed,
\[
h(1)=0,\qquad h(-1)=1.
\]
Therefore \(z\) reduces to one and is a unit. Scaling by this actual
witness leaves the residue seed unchanged and gives
\[
a_2=-1,\qquad a_3=a_{17}=0
\]
exactly. The active middle indices are precisely \(J=\{4,10,12\}\).

This is the exact family excluded by the existing row-4 smallest-support
theorem. Its complete residue census retains all seventeen nonzero
witness residues, both critical-root orientations, and active
coefficients whose residues vanish. Its two residue survivors have
simple selected witness classes and a unit lifting Jacobian. The final
critical-value certificate is
\[
f(R)=17^2(9+4\alpha)\pmod{17^3},
\qquad \alpha^2+3\alpha+3=0,
\]
which is nonzero. The theorem's analytic division and uniqueness
arguments permit arbitrary ramified valued extensions. Thus the
normalization above falls within its proved scope and is impossible.
This excludes the algebraic specialization and hence the original
characteristic-zero point. \(\square\)

## Exact dependencies and verification boundary

1. [Complete seed classification](evidence/full/support_frontier/prime17/CLASSIFICATION.md):
   classification over the whole algebraic closure, with coefficient-zero
   charts and monomial retained separately. Its certificate checker and
   [independent mathematical audit](evidence/full/literature/PRIME17_CLASSIFICATION_AUDIT.md)
   validate completeness; checking only the nine displayed examples
   would not suffice.
2. [Normalization and integrality](evidence/full/LIFT_CONSEQUENCES_17.md):
   the recurrence proof is reproduced above. The general simple-mean
   argument is not an extra bridge needed to select row 4, whose mean
   residue root is already simple.
3. [Row-4 smallest-support exclusion](evidence/full/tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md):
   the local computational theorem for \(J=\{4,10,12\}\), together with
   its [separate audit](evidence/full/tame17/ROW4_SMALLEST_SUPPORT_AUDIT.md)
   and standard-library checker.

The corollary's normalization and support-preservation bridge received
a separate bounded algebraic audit. No existing evidence files were
modified and no large computation was rerun.

This does not exclude the whole row-4 branch, every seven-term support,
or degree 20. It does not assert the same conclusion merely from support
containment, and makes no claim about priority or an assessment grade.


# Six global exclusions in the seven-term support frontier

24 September 2026. This note independently verifies a bounded new use of
the existing ramification-safe row-8 divided identity. The computation
contains 1,216 residue assignments in total. It is not the unrestricted
row-8 census.

## Statement

**Proposition.** The characteristic-17 row-8 branch cannot occur for any
of the seven exact centered deficiency supports in the table below.

| Exact deficiency support | Active middle indices \(J\) | Assignments \(4^{|J|}\) | After divided identity | Possible seed rows before this test |
|---|---|---:|---:|---|
| \(\{2,3,4,10,12,19\}\) | \(4,10,12\) | 64 | 0 | 5,8 |
| \(\{3,4,9,10,12,19\}\) | \(4,9,10,12\) | 256 | 0 | 8 |
| \(\{3,4,5,10,13,19\}\) | \(4,5,10,13\) | 256 | 0 | 8 |
| \(\{3,4,10,12,15,19\}\) | \(4,10,12,15\) | 256 | 0 | 8 |
| \(\{3,7,9,10,16,19\}\) | \(7,9,10,16\) | 256 | 0 | 8 |
| \(\{3,6,10,16,17,19\}\) | \(6,10,16\) | 64 | 0 | 1,8 |
| \(\{3,4,10,13,18,19\}\) | \(4,10,13\) | 64 | 0 | 8,9 |

No unit-root collision filter is used: every row is already empty after
the divided identity alone.

**Global corollary.** The following five exact centered seven-term
supports cannot occur for a characteristic-zero degree-20 CA polynomial:
\[
\begin{gathered}
\{3,4,9,10,12,19\},\qquad
\{3,4,5,10,13,19\},\\
\{3,4,10,12,15,19\},\qquad
\{3,7,9,10,16,19\},\\
\{3,4,10,13,18,19\}.
\end{gathered}
\]
The first four have no other possible seed. For the fifth, the previously
proved complete row-9 exclusion with \(J=\{4,10,13\}\) removes the
other possible seed. The first and sixth rows of the table remain
unresolved globally by this argument: rows 5 and 1, respectively,
are still possible.

## 1. Normalization and the inherited necessary identity

Use the centered monic notation
\[
f=\sum_{j=0}^{20} C_ja_jX^{20-j},\qquad
C_j=\binom{20}{j},\quad a_0=1,\quad a_1=a_{20}=0.
\]
Integral root normalization at 17 and the normalized derivative
recurrence make all roots and all \(a_j\) integral. Scaling, including
the later unit-witness normalization, preserves exact support.
Algebraic specialization retains an exact support by adjoining the
inverse of the product of its active coefficients. These details are
given explicitly in
[GLOBAL_SUPPORT_COROLLARY.md](new-results/GLOBAL_SUPPORT_COROLLARY.md).

In row 8,
\[
\bar f=X^{17}(X^3-1).
\]
The common witness for \(G_3\) is a unit; scale it exactly to one.
Then \(f(1)=G_3(1)=0\), so
\[
a_3=-1-3a_2.
\tag{1}
\]
The seed is unchanged by this additional scaling because the residue
of the scaling witness is a cube root of unity.

The existing proof
[ROW8_BOUND_AND_DIVIDED_IDENTITY.md](evidence/full/wild17/ROW8_BOUND_AND_DIVIDED_IDENTITY.md)
gives
\[
\sum_{j=4}^{16}(C_j/17)\bar a_j=-1.
\tag{2}
\]
For completeness, its valuation bridge has no unramified-field
assumption. Let \(\delta>0\) be the least valuation of a nonzero
root in the seventeen-root zero cluster, normalized by \(\nu(17)=1\).
The cluster has such a root because the exact mean is simple;
for the seven supports here this also follows immediately from
the nonzero linear coefficient \(a_{19}\).
The witnesses for \(G_2,G_{17},G_{18},G_{19}\) reduce to zero.
Their exact equations imply
\[
\begin{aligned}
\nu(a_2)&\ge2\delta,\\
\nu(a_{17})&\ge\min(17\delta,1+\delta),\\
\nu(a_{18})&\ge\min(18\delta,1+2\delta),\\
\nu(a_{19})&\ge\min(19\delta,1+3\delta).
\end{aligned}
\]
At a root attaining \(\delta\), the \(X^{17}\) term has value
\(17\delta\); every other term has value at least
\(\min(20\delta,1+4\delta)\). Unique minimal valuation would prevent
cancellation if \(\delta<1/13\). Thus \(\delta\ge1/13\), and
\[
\nu(a_{17})\ge1+\delta,\quad
\nu(a_{18})\ge1+2\delta,\quad
\nu(a_{19})\ge1+3\delta.
\]
Substitution of (1) into \(f(1)=0\) gives the exact equation
\[
0=-17\cdot67-17\cdot190a_2
+\sum_{j=4}^{16}C_ja_j
+1140a_{17}+190a_{18}+20a_{19}.
\]
Divide by 17 and reduce. The displayed strict bounds remove the last
three terms, and \(\nu(a_2)>0\) removes the second. Since
\(67=-1\) modulo 17, equation (2) follows. Fractional valuations are
allowed throughout.

## 2. Canonical witnesses at inactive coefficients

Let \(S\) be an exact support from the table and
\(J=S\cap\{4,\ldots,16\}\). If \(j\notin J\), then \(a_j=0\)
exactly. Because \(G_j(0)=a_j\) and \(f(0)=0\), zero is an exact
common witness for this derivative. Choose it. These choices can be
made independently: the CA condition requires the existence of a
witness for each order and imposes no requirement that these
particular choices differ.

For an active coefficient \(j\in J\), every possible witness residue
must be retained:
\[
\rho_j\in\{0,1,\zeta,\zeta^2\},\qquad
\zeta^2+\zeta+1=0\text{ in }\mathbb F_{17^2}.
\]
In particular, an active coefficient or a nonzero exact witness may
have zero residue. Neither is discarded.

The residue equations start with
\(\bar a_0=1,\bar a_1=\bar a_2=0,\bar a_3=-1\), and determine
successively
\[
\bar a_j=-\sum_{i=0}^{j-1}
\binom ji\bar a_i\rho_j^{\,j-i},
\qquad 4\le j\le16.
\tag{3}
\]
At every inactive index the chosen \(\rho_j=0\) makes this coefficient
zero. Hence each of the \(4^{|J|}\) active label assignments determines
one complete residue coefficient vector. Every actual counterexample
with that support gives at least one of these assignments.

The finite field restriction is a conclusion of (3), not an assumption
about the ambient residue field or about the ramification of a lift.
The visible seed has no roots outside this four-element domain in
the algebraic closure. An empty necessary-condition census therefore
excludes row 8 for the exact support.

## 3. Independent finite check

[check_row8_seven_term.py](new-results/check_row8_seven_term.py) imports no producer
or existing checker. It represents the field as
\(\mathbb F_{17}[s]/(s^2-14)\), verifies that 14 is a nonsquare, and
uses the complete domain
\[
0,\quad1,\quad8+9s,\quad8+8s.
\]
The three nonzero entries are distinct cube roots of unity. This
presentation differs from the earlier producer's \(1,\zeta\) basis.

The checker traverses the Cartesian product independently for each
support, implements the full recurrence (3), evaluates (2), and
records a histogram of all attained sums. It verifies the expected
assignment count and finds no sum equal to \(-1\) in any of the seven
cases. Normal and optimized Python runs produce identical receipts:

- [normal receipt](new-results/row8-seven-term-normal.json);
- [optimized receipt](new-results/row8-seven-term-optimized.json).

The checker also binds the support list to the existing support
inventory, verifies that these are exactly its seven size-six
deficiency sets containing 3, and checks the seed routing in the
table. It does not rerun the much larger predecessor inventory.
The witness-canonicalization argument received a separate bounded
algebraic review.

## 4. From branch exclusions to global statements

The complete nine-seed classification applies after normalization
because a unit root is retained, excluding monomial reduction.
Exact coefficient zeros remain zero under reduction and scaling.
Here is the complete table, in ordinary visible coefficients
\(h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX\):

| Row | \(a\) | \(b\) | \(c\) | \(d\) | \(e\) |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 16 | 0 | 0 |
| 2 | 14 | 0 | 16 | 0 | 3 |
| 3 | 14 | 8 | 16 | 12 | 0 |
| 4 | 14 | 0 | 0 | 11 | 8 |
| 5 | 14 | 2 | 0 | 0 | 0 |
| 6 | 14 | 2 | 0 | 11 | 6 |
| 7 | 14 | 2 | 0 | 14 | 3 |
| 8 | 0 | 16 | 0 | 0 | 0 |
| 9 | 0 | 16 | 0 | 14 | 3 |

The table is an input from the independently checked
[algebraic-closure classification](evidence/full/support_frontier/prime17/CLASSIFICATION.md)
and its [audit](evidence/full/literature/PRIME17_CLASSIFICATION_AUDIT.md).
The new checker verifies routing against this table; it does not
reprove the classification merely by checking the nine examples.

For each of the seven supports, the table retains exactly the seed
rows whose nonzero visible coefficients do not occur at an absent
index. This argument never infers an exact coefficient zero from
a zero residue.

Four supports omit \(2,17,18\) and contain \(3,19\). The visible
polynomial can then have only its \(X^{17}\) and \(X\) coefficients
nonzero below the leading term. Row 8 is the only compatible
nonmonomial seed. Their row-8 exclusions are therefore global.

For \(\{3,4,10,13,18,19\}\), only rows 8 and 9 are compatible.
The row-9 canonical middle support is \(J=\{4,10,13\}\), which is
already completely excluded in
[BATCH1_PROOF.md](evidence/full/collective17/exclusions/BATCH1_PROOF.md).
That prior computation covers its entire algebraic residue domain
and arbitrary ramification. Combining it with the new row-8
exclusion proves the fifth global exclusion.

For \(\{2,3,4,10,12,19\}\), row 5 remains compatible. For
\(\{3,6,10,16,17,19\}\), row 1 remains compatible. The present
argument excludes neither remaining branch.

## 5. Exact coverage increment

The predecessor inventory contained fourteen possible exact
seven-term supports. The five global exclusions above and the
separate global row-4 corollary for \(\{2,4,10,12,18,19\}\) remove
six distinct entries. The remaining eight are
\[
\begin{gathered}
\{2,3,4,10,12,19\},\quad
\{3,6,10,16,17,19\},\\
\{7,8,10,16,17,19\},\quad
\{10,12,13,16,17,19\},\\
\{6,10,15,16,17,19\},\quad
\{9,10,15,16,17,19\},\\
\{2,4,10,17,18,19\},\quad
\{4,10,16,17,18,19\}.
\end{gathered}
\]
Explicitly, the six excluded exact supports are
\[
\begin{gathered}
\{2,4,10,12,18,19\},\quad
\{3,4,9,10,12,19\},\\
\{3,4,5,10,13,19\},\quad
\{3,4,10,12,15,19\},\\
\{3,7,9,10,16,19\},\quad
\{3,4,10,13,18,19\}.
\end{gathered}
\]
The eight remaining sets are necessary possibilities, not asserted
realizable supports.
The coverage statement depends on the predecessor inventory and its
underlying imported restrictions. It does not raise the seven-term
lower bound to eight terms, exclude the whole row-8 branch, or solve
degree 20. No priority or assessment-grade claim is made.


# Marked splitting of a local resultant algebra

## Input and notation

The input is the audited normalization and the explicit integer
polynomials in
[the explicit local presentation](evidence/full/collective17/elimination/FINITE_FLAT_REDUCTION.md).
In particular,
\[
f_u=(X-1)^2g_u,\qquad
g_u(1)=17T(u),
\]
where \(g_u\) is monic of degree eighteen and
\[
T=-8037+\sum_{j=4}^{16}
\binom{19-j}{2}\frac{\binom{20}{j}}{17}u_j.
\]
The normalized derivatives are
\[
G_j(X)=X^j-\binom j3 X^{j-3}
+\sum_{i=4}^j\binom ji u_iX^{j-i},
\qquad 4\leq j\leq16.
\]

For clarity, the integer presentation is
\[
\begin{aligned}
f_u={}&X^{20}-1140X^{17}
+\sum_{j=4}^{16}C_ju_jX^{20-j}
\\ &+\left(18221-\sum_{j=4}^{16}(19-j)C_ju_j\right)X^2
+\left(-17082+\sum_{j=4}^{16}(18-j)C_ju_j\right)X,
\end{aligned}
\qquad C_j=\binom{20}{j}.
\]
Direct substitution gives \(f_u(1)=f'_u(1)=0\), which defines
\(g_u=f_u/(X-1)^2\). The fixed reduction of \(g_u\) is
\[
D=\frac{X^{20}-X^{17}-3X^2+3X}{(X-1)^2}\quad\text{in }\mathbf F_{17}[X].
\]
Its squarefreeness and factor degrees are checked in the exact presentation accompanying the paper.

Set \(R_j=\operatorname{Res}_X(g_u,G_j)\). The complete row-9 incidence
problem is \(R_4=\cdots=R_{16}=T=0\) on integral parameters.
The resultant equations without \(T=0\) are only a square enlargement.

The fixed reduction \(D=\bar g_u\) is squarefree and has factor degrees
\(1,1,1,5,10\). The simple roots are \(0,1,-2\), five roots of \(Q_5\),
and ten roots of \(Q_{10}\), with \(Q_5,Q_{10}\) as in the input.
Consequently all eighteen residue roots lie in \(\mathbb F_{17^{10}}\).
Let \(K/\mathbb Q_{17}\) be the unramified extension of degree ten,
\(\mathcal O\) its integer ring, and \(\pi=17\).

The checked Frobenius identity is
\[
r^{17}=\frac{3r}{r^2+r+1}.
\]
For \(r\ne1\), putting \(y=7(r+1)/(r-1)\) gives
\[
y^{17}=y^2-5.
\]
These are residue-field identities. No exact characteristic-zero
quadratic Frobenius equation is assumed.

## A marked splitting lemma

**Proposition 1.** Let \(\mathcal O\) be a complete discrete valuation
ring with uniformizer \(\pi\), and put
\(S=\mathcal O\langle u_1,\ldots,u_m\rangle\), the restricted power-series
ring. For each \(j\) choose \(d_j\geq1\) elements
\(L_{j,1},\ldots,L_{j,d_j}\) such that
\[
\overline{L}_{j,r}
=u_j+A_{j,r}(u_1,\ldots,u_{j-1}).
\tag{1}
\]
Let \(F_j=\prod_{r=1}^{d_j}L_{j,r}\) and
\(B=S/(F_1,\ldots,F_m)\). Then:

1. \(B\) is finite free over \(\mathcal O\), of rank \(\prod_jd_j\).
2. For each marked tuple \(\mathbf r=(r_1,\ldots,r_m)\),
   \(S/(L_{1,r_1},\ldots,L_{m,r_m})\) is a rank-one unital
   \(\mathcal O\)-algebra and is therefore \(\mathcal O\). Its coordinates
   give a point \(u^{\mathbf r}\in\mathcal O^m\).
3. \(B\) has an \(S\)-module filtration with exactly these rank-one
   quotient modules, one for each marked tuple, including repetitions.
4. For every \(H\in S\),
\[
\det_{\mathcal O}(m_H\mid B)
=\prod_{\mathbf r}H(u^{\mathbf r}).
\tag{2}
\]

Distinct marked tuples need not give distinct coordinate points. The
proposition neither asserts that \(B\) is étale nor replaces \(B\) by
its radical.

**Proof.** Consider any system obtained by replacing any of the \(F_j\)
by a nonempty product of a subset of its factors. Its reduced equations,
ordered by increasing \(j\), are monic in successively fresh variables.
They therefore form a regular sequence, and successive monic division
gives a basis whose size is the product of the remaining factor counts.

The elementary lifting argument is as follows. If \(A\) is complete,
separated and \(\pi\)-torsion-free and \(\bar h\) is a nonzerodivisor
in \(A/\pi A\), then \(A/(h)\) is \(\pi\)-torsion-free: an equation
\(\pi x=hy\) first gives \(y=\pi z\), and cancellation gives \(x=hz\).
Also \(hx=0\) successively forces \(x\in\pi^nA\) for every \(n\), so
\(h\) is a nonzerodivisor. Apply this argument to the reduced regular
sequence. The resulting quotient is complete and torsion-free.

Lifting its finite monomial basis modulo \(\pi\), successive
approximation expresses every element as an \(\mathcal O\)-linear
combination of those same monomials. A relation among them has all
coefficients divisible by \(\pi\); torsion-freeness permits division,
and iteration makes the relation zero. Every full intermediate quotient
is thus finite free with the stated rank. In particular each fully
selected system has rank one. Its unit reduces to a basis of its
one-dimensional residue algebra, so the structural map
\(\mathcal O\to S/(L_{1,r_1},\ldots,L_{m,r_m})\) is an isomorphism.

It remains to justify a filtration rather than just a rank count.
Omit equation \(j\), and call the resulting complete quotient \(A\).
Write the current product in that equation as \(ab\), where \(a\)
is one of its factors. The element \(\bar a\) is a nonzerodivisor
in \(\bar A\). To see this, impose the lower-index equations first,
obtaining a possibly nonreduced ring \(C\). In \(C[u_j]\), the
element \(\bar a=u_j+A_{j,r}\) is monic and is a nonzerodivisor.
Adjoining each higher variable subject to its monic equation gives
a finite free extension and preserves this property. The preceding
lifting argument makes \(A\) torsion-free and \(a\) a nonzerodivisor.
Consequently the following sequence is exact:
\[
0\longrightarrow A/(b)
\xrightarrow{\;\cdot a\;}A/(ab)
\longrightarrow A/(a)\longrightarrow0.
\tag{3}
\]
Split each product recursively, then split the other equations.
This produces the asserted filtration. Repeated factors are allowed
in (3); they contribute repeated filtration factors.

Multiplication by \(H\) preserves the filtration. Each quotient is free
of rank one over \(\mathcal O\), and multiplication on it is the scalar
\(H(u^{\mathbf r})\). Choose an \(\mathcal O\)-basis adapted to the
filtration. The multiplication matrix is block triangular, so its
determinant is the product in (2). \(\square\)

## Consequences for the full row-9 algebra

In \(\mathcal O\langle u_4,\ldots,u_{16}\rangle[X]\), the polynomial
\(g_u\) has a unique analytic root function \(\rho_r(u)\) reducing to
each residue root \(r\) of \(D\). Indeed, a constant lift of \(r\)
has \(g_u\)-value divisible by \(17\), while the derivative reduces
to the nonzero constant \(D'(r)\). The complete-ring Hensel iteration
therefore constructs \(\rho_r\). Distinct root functions have unit
differences. Monicity and the degree give the exact factorization
\[
g_u(X)=\prod_{r\in Z(D)}(X-\rho_r(u)).
\]
Thus, without an omitted leading-coefficient factor,
\[
R_j(u)=\prod_{r\in Z(D)}G_j(\rho_r(u)).
\tag{4}
\]
The reduction of a factor is
\[
\overline{G_j(\rho_r(u))}
=u_j+r^j-\binom j3r^{j-3}
+\sum_{i=4}^{j-1}\binom ji u_i r^{j-i}.
\]
It has precisely form (1). Proposition 1 applies with thirteen
variables and eighteen factors per equation.

**Corollary 2.** After base change to \(\mathcal O\), the completed
row-9 resultant algebra has a filtration with \(18^{13}\) rank-one
factors. Its obstruction norm satisfies
\[
N=\prod_{\mathbf r\in Z(D)^{13}}\tau_{\mathbf r},
\qquad
\tau_{\mathbf r}=T(u^{\mathbf r})\in\mathcal O.
\tag{5}
\]
Every integral geometric solution of the square resultant system
has all its coordinates in \(K\). Every genuine row-9 CA polynomial,
if one exists, has all its roots in \(K\) after this normalization.

For the last assertion, an integral solution in any valued extension
chooses a vanishing factor of each product (4). The selected quotient
is \(\mathcal O\), so its parameters equal the corresponding
\(u^{\mathbf r}\). Then \(g_u\) splits into the displayed analytic
roots in \(\mathcal O\), and \(f_u=(X-1)^2g_u\) adds only the root one.
This treats arbitrary ramification; it does not assume it away.

The same result applies to every fixed active support \(J\), with
zero removed from the domain and \(g_u/X\) in place of \(g_u\).
Its rank is \(17^{|J|}\). Nominally active coefficients with zero
residue remain included.

This fixed unramified field conclusion was already implicit in the
marked Hensel proof of the existing batch exclusions. The additional
point here is the filtration of the potentially nonreduced resultant
algebra and the exact multiplicity-preserving norm identity (5).

Let \(\sigma\) be the Frobenius automorphism of \(K/\mathbb Q_{17}\).
Uniqueness of the marked lifts gives
\[
u^{\sigma\mathbf r}=\sigma(u^{\mathbf r}),\qquad
\tau_{\sigma\mathbf r}=\sigma(\tau_{\mathbf r}).
\tag{6}
\]
The residue-domain cycles have lengths \(1,5,10\); hence so do marked
tuple orbits. If an orbit has length \(d\), its representative value
belongs to the degree-\(d\) unramified subfield \(K_d\), and its
contribution to (5) is
\[
\operatorname{Norm}_{K_d/\mathbb Q_{17}}(\tau_{\mathbf r}).
\]
If every factor is nonzero, then
\[
v_{17}(N)=\sum_{\text{marked orbits }[\mathbf r]}
 d_{\mathbf r}\,v_{17}(\tau_{\mathbf r}).
\tag{7}
\]
All valuations in this sum are integers. This avoids any determinant
cancellation issue, but not the need to establish nonvanishing on
every relevant marked orbit.

## Why the quadratic Frobenius law alone does not close the branch

The coefficients of the equations lie in \(\mathbb Z_{17}\); the
coefficients of an individual solution need not. Equation (6) transports
a solution to its conjugate. It does not say that it fixes that
solution. The following compact example shows the issue within the
actual complete first-residue incidence equations.

Let \(r\) have irreducible polynomial
\[
Q_5(r)=r^5-3r^4-2r^2-5r-3=0
\quad\text{over }\mathbb F_{17}.
\]
Use the active set \(J=\{4,9,10,14\}\) and witnesses
\[
r_4=-2,\qquad r_9=r,\qquad r_{10}=1,\qquad r_{14}=-2.
\]
At inactive indices choose zero. The derivative recurrences give
\[
\begin{aligned}
u_4&=-7,\\
u_9&=-5r^4+5r^3+8r^2+7r-3,\\
u_{10}&=-r^4+r^3+5r^2-2r+4,\\
u_{14}&=-4r^4+4r^3+3r^2-8r-4,
\end{aligned}
\]
and all other middle \(u_j\) vanish. Every marked witness is a root
of \(h=X^{20}-X^{17}-3X^2+3X\), every marked normalized derivative
vanishes, and direct reduction gives \(\bar T=0\). Nevertheless,
\[
u_9^{17}-u_9
=7r^4+r^3-8r^2-7r+7\ne0.
\tag{8}
\]
The last inequality follows from irreducibility and the nonzero
degree-four remainder. The transformed \(y=7(r+1)/(r-1)\) also
satisfies \(y^{17}=y^2-5\), exactly as required.

Thus all first-residue constraints and the quadratic Frobenius law
are consistent with non-Frobenius-fixed coefficients. Taking traces
is legitimate, but cannot turn (6) into equality of the individual
coefficient values. This is the already known degree-five residue
fixture, here reconstructed symbolically; it is not a new surviving
characteristic-zero candidate.

The residue obstruction itself has a compact expression:
\[
\bar T=4+\sum_{j=4}^{16}
\frac{3(-1)^j}{j(j-3)}u_j.
\tag{9}
\]
For \(4\leq j\leq16\), cancelling the unique factor \(17\) in
\(\binom{20}{j}\) gives
\[
\frac{\binom{20}{j}}{17}
\equiv\frac{6(-1)^j}{j(j-1)(j-2)(j-3)}\pmod{17}.
\]
Multiplication by \(\binom{19-j}{2}\) proves (9).
The weights are symmetric under \(j\mapsto20-j\). Example (8) shows
that this smaller formula is not itself a nonvanishing invariant.

## Even the first three obstruction digits can vanish

There is a small exact example inside the true marked square system,
not only a residue-field construction. Use
\(J=\{4,5,8,10,11\}\), initially put every active witness equal to one,
and solve the normalized derivative equations recursively. This gives
\[
(u_4,u_5,u_8,u_{10},u_{11})
=(3,-6,181,-7144,50665).
\]
All those normalized derivative incidences at one hold exactly, and
\[
T=11294240224=17^3\cdot2298848,\qquad 17\nmid2298848.
\tag{10}
\]
For \(q_u=g_u/X\), the exact identity \(q_u(1)=17T\) makes the
single marked root equation vanish modulo \(17^4\).

The derivative equations express the \(u_j\) as integer polynomials
of the one common witness \(x\). The marked root equation
\(q_{u(x)}(x)=0\) has a unit derivative modulo \(17\): parameter
dependence disappears modulo \(17\), and \(\bar q'(1)\ne0\).
Its exact root therefore differs from one by an element of
\(17^4\mathbb Z_{17}\). All corresponding \(u_j\), and hence \(T\),
change by multiples of \(17^4\). Its exact square-system obstruction
has valuation precisely three.

Consequently no uniform claim that all marked obstruction values
are units, or have valuation at most one or two, can hold. This does
not disprove a larger uniform bound. No such bound was established
in this investigation.



# Scope and remaining problem

The complete global statement proved here is a lower bound on the number of terms of a centered hypothetical counterexample in degree twenty. The accompanying support exclusions strengthen its finite frontier. They do not amount to a proof in degree twenty: denser supports and several reduction branches remain.

The local resultant factorization isolates a precise obstruction. Each marked square subsystem has a unique lift in a fixed unramified extension, while the extra scalar equation need not hold. To exclude the entire branch one must show that this scalar is nonzero for every relevant marking. The product formula does not accomplish that, and the examples show that several low-precision shortcuts fail. A uniform nonvanishing argument would be a substantive next result; enlarging a finite census is not a substitute for it.

The computational claims are reproducibility claims with explicit scope. Default replay verifies the recorded certificates and bounded checks; it does not rerun the largest optional native census. The original full-census receipts and separate arithmetic checks are retained. Compiler and timeout controls permit fresh runs on other systems, and a failed or interrupted run is not recorded as mathematical completion.

# Data, code, and review provenance

The accompanying archive contains the editable manuscript, typesetting source, final PDF, proof notes, machine-readable certificates, source scripts, a file-integrity manifest, and a review response. Its README identifies the definitive proof and commands. The earlier consolidated report is retained as historical context; where its frontier counts differ, the explicitly scoped current support corollary governs only the newly excluded exact seven-term supports.

A supplied external review's independent arithmetic script was rerun unchanged with the pure-Python SymPy ground backend; all eight reported sections matched. Its checks support the particular identities tested and do not replace proof of coverage, novelty assessment, or external refereeing of this revision. The new additions have separate internal review and replay records. File hashes establish integrity, not mathematical validity. This manuscript has not been submitted or published as part of preparing this review package.


# Declarations for review

**Data availability.** The evidence and source code are included in the accompanying review archive; no permanent public repository or DOI is claimed.

**Ethics.** This is a mathematical investigation involving no human participants, animal experiments, or personal-data analysis.

**Author contributions (CRediT), funding, and competing interests.** Human authorship, CRediT assignments, funding information, and competing-interest declarations have not been supplied. These administrative declarations remain for the responsible author to complete before submission; absence of supplied information is not a declaration of no funding or no competing interests.

**AI use.** Codex assisted the mathematical investigation, code construction, literature comparison, drafting, and internal adversarial checks. Those internal checks are not human peer review or formal verification. The manuscript exposes the mathematical dependencies and executable evidence for independent assessment.


# References

**[CLO] Wouter Castryck, Robert Laterveer, Myriam Ounaïes, *Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12*.** [arXiv:1208.5404v1](https://arxiv.org/abs/1208.5404v1), 27 August 2012; [full text](https://arxiv.org/html/1208.5404). Relevant locations are Theorem 2 (degree \(p+1\), mean-root and determinant restrictions), Theorem 13 (distinct-root bound), Proposition 15 (prime-power derivative placement), and the scenario/descendant treatment in the computational sections. These are established predecessor methods, not campaign contributions. Their demonstrated full-degree computation is degree 12. In degree 20, derivative orders \(1,19\), orders \(4,16\), and the simultaneous triple \(5,10,15\) supply forbidden shared-root configurations. The appropriate hypotheses and normalization must be retained when translating these into coefficient conditions.

**[deFrutos] Rosa María de Frutos Marín, *Perspectivas aritméticas para la Conjetura de Casas-Alvero*.** Doctoral thesis, Universidad de Valladolid, repository year 2013; advisor Antonio Campillo López. [Primary PDF](https://uvadoc.uva.es/bitstream/handle/10324/3602/TESIS367-130927.pdf?isAllowed=y&sequence=1), [repository metadata](https://uvadoc.uva.es/handle/10324/3602?show=full), DOI [10.35376/10324/3602](https://doi.org/10.35376/10324/3602). The title-page date is 21 December 2012, the university catalog defense date is 11 June 2013, and repository availability is 27 September 2013; these describe distinct events. Sections 2.3 and 3.5, especially Proposition 3.5.5, contain the older sparse/two-visible-coefficient criterion used in the campaign's support sieve. The full thesis text and Proposition 3.5.5 were retrieved and compared on 24 September 2026; see review/NOVELTY.md.

**[Massri] Cesar Massri, *The Casas-Alvero conjecture for three recycled roots in degree 20*.** [arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6), [full text](https://arxiv.org/html/1806.09561v6). First submission 25 June 2018; v6, 25 August 2023. Some earlier versions are marked withdrawn; the current v6 title and scope should be cited, not an earlier full-proof claim. Relevant passages are Remark 7.4, the proof of Theorem 7.9, Theorem 7.10, and the finiteness/normalization results in Sections 5–6. The restrictions on shared derivative pairs \((5,10)\), \((10,15)\) imply more sparsity than a title-only comparison reveals. Together with CLO they defeat novelty of the campaign's initial five-term bound. The reported three-recycled-root computation is not a monomial-count theorem; no complete public replay of its reported \(3^{17}\) assignments was retrieved. The current arXiv metadata supplies no journal reference.

**[Marashdeh] Mohammad F. Marashdeh, *A descent-set obstruction for the Casas-Alvero conjecture*.** [arXiv:2608.14726v1](https://arxiv.org/abs/2608.14726v1), [full text](https://arxiv.org/html/2608.14726v1), 12 August 2026. The record exposes only v1. Relevant comparisons concern support stratification, triangular elimination of coefficients, descent-count determinants, and the two-element-support argument. These are not a degree-20 seven-total-term theorem. The campaign does not use a reported equation count as a proof that the remaining incidence system is empty. The preprint and its statements are distinct from external refereeing or a priority clearance.

**[Bothmer-et-al] Hans-Christian Graf von Bothmer, Oliver Labs, Josef Schicho, Christiaan van de Woestijne, *The Casas-Alvero conjecture for infinitely many degrees*.** [arXiv:math/0605090v2](https://arxiv.org/abs/math/0605090v2), 25 June 2007; first submission 3 May 2006. *Journal of Algebra* 316 (2007), 224–230, DOI [10.1016/j.jalgebra.2007.06.017](https://doi.org/10.1016/j.jalgebra.2007.06.017). The weighted projective formulation and good-prime transfer, including Propositions 2.1–2.2 and 2.6, explain why geometric special-fibre emptiness can prove a characteristic-zero result and propagate degree \(n\) to \(np^e\). Prime-field rational-point absence or an empty unsaturated affine chart does not meet those hypotheses.

**[Berger] Laurent Berger, *The Weierstrass preparation theorem and resultants of p-adic power series*.** [arXiv:1910.05319v2](https://arxiv.org/abs/1910.05319v2), 4 November 2019; first submission 11 October 2019. [Author-hosted PDF](https://perso.ens-lyon.fr/laurent.berger/articles/article33.pdf). Section 1, including Corollary 1.2, supplies a precise complete-ring preparation statement. In the campaign's row-4 local argument, a power series reducing coefficientwise to \(z^2\) over a complete unramified DVR is a unit times a monic distinguished quadratic. The campaign separately proves the hypotheses, convergence, and coverage of actual ramified points.

**[ProofAtlas]** [Casas–Alvero collaboration page](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/). Reported work, inspected 24 September 2026; exact-system equivalence unresolved.

**[Shih]** Shih, Cheng-Pang, *On the Casas-Alvero Conjecture*, 2022 master’s thesis. [NTHU catalog record](https://etd.lib.nycu.edu.tw/cgi-bin/gs32/hugsweb.cgi?o=dnthucdr&s=id%3D%22G021090215100%22.&searchmode=basic). Metadata inspected; full text unavailable.

