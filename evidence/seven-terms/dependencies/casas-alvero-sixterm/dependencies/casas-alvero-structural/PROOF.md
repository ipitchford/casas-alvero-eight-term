# A uniform Frobenius obstruction for a moving Casas–Alvero family

23 September 2026. Research candidate; internal exact checks and adversarial audit. Historical novelty and publication significance are assessed separately.

## Statement and scope

In positive characteristic, the Casas–Alvero (CA) property here means sharing a root with every Hasse derivative of orders 1 through degree minus one. There is an explicitly specified nonzero integer \(\Delta\) such that, for every prime \(p>7\) not dividing \(\Delta\), the only CA polynomial over \(\overline{\mathbb F}_p\) of the form

\[
X^{p+7}+aX^{p+3}+cX^3+dX
\tag{1}
\]

is the monomial. In particular, only finitely many primes can admit a nontrivial member of this **moving-degree** family.

This gives coefficient restrictions in characteristic zero for infinitely many base degrees, as specified below. It does not prove the unrestricted conjecture in any new degree. The integer \(\Delta\) bounds the exceptional primes; its divisors are not claimed to be exactly the exceptional primes.

## 1. A fixed integral certificate

All polynomials in this section have integer coefficients and variable \(z\). Define

\[
P=35(17-z^3),\quad Q=z^2(51-35z),
\quad R=35(z^{18}-17^5),\quad S=17^3(51z^6-35\cdot17^2).
\]

Put \(A=34P\), \(B=35(Q-P)\), and

\[
E=A^4P^2+6A^2B^2PQ+B^4Q^2,\qquad
O=4AB(A^2P+B^2Q).
\]

The polynomial

\[
H(z)=\frac{(RE-34^4SQ^6)^2-PQR^2O^2}{17^8}
\tag{2}
\]

is integral and primitive, and has degree 72. These are exact coefficient identities, reproduced by the accompanying checker; no division by an unknown field element is involved. Define

\[
C(z)=z^{432}H(289/z^6),\qquad
\mathcal R=\operatorname{Res}_z(H,C).
\tag{3}
\]

The degrees of \(H,C\) remain 72 and 432 modulo 11, where an explicit extended-Euclidean certificate gives

\[
U(z)H(z)+V(z)C(z)=1\quad\text{in }\mathbb F_{11}[z].
\tag{4}
\]

Consequently \(\mathcal R\ne0\). Equation (4), checked by polynomial multiplication, suffices for this assertion; neither an irreducibility claim nor a factorization of the integer resultant is needed.

Take

\[
\Delta=17\cdot1229\cdot3114019\cdot\mathcal R.
\tag{5}
\]

The exact resultant is retained in the supplementary files (26,185 decimal digits). Its uncompleted factorization is not used in the proof.

## 2. Normalization and all coefficient cases

Fix a prime \(p>7\), \(p\ne17\), and suppose (1) is CA. At zero, every derivative condition except possibly orders \(p+3,3,1\) holds automatically. Lucas's theorem gives

\[
H_{p+3}=35X^4+a,\quad
H_3=35X^{p+4}+aX^p+c,\quad
H_1=7X^{p+6}+3aX^{p+2}+3cX^2+d.
\tag{6}
\]

If \(a=c=0\) but \(d\ne0\), a nonzero common root with \(H_1\) would force both \(w^{p+6}=-d\) and \(7w^{p+6}=-d\), which is impossible. The zero case is the monomial.

If \(a=0,c\ne0\), scale a common root with \(H_3\) to 1. Then \(c=-35,d=34\). A common root \(w\ne0\) with \(H_1\) satisfies

\[
w^{p+6}=17,\qquad w^2=51/35.
\]

The coprime exponents 2 and \(p+6\) show that \(w\in\mathbb F_p^*\): Bezout expresses \(w\) as a product of powers of these two prime-field values. Hence \(w^7=17\), giving

\[
0=51^7-17^2 35^7=-2^4\cdot17^2\cdot1229\cdot3114019\quad(\bmod p).
\tag{7}
\]

Thus this case is excluded when \(p\nmid\Delta\).

Now suppose \(a\ne0\). Scale a nonzero common root with \(H_{p+3}\) to 1, so \(a=-35\). There is a nonzero common root \(v\) with \(H_3\). This is automatic when \(c\ne0\); when \(c=0\), take \(v=1\), since both \(h(1)\) and \(H_3(1)\) vanish. Evaluating these equations gives

\[
c=35v^p(1-v^4),\qquad d=34v^{p+6},
\quad v^p(34v^6-35v^4+35)=34.
\tag{8}
\]

In particular \(d\ne0\), so a common root \(w\) with \(H_1\) is nonzero. The identity

\[
3(h/X)-H_1=-4X^{p+6}+2d
\]

gives, on putting \(t=w/v\),

\[
t^{p+6}=17,\qquad t^p=17/t^6.
\tag{9}
\]

Substitution into \(h(w)/w=0\) gives

\[
(51-35t^2)v^4=35t^2(t^p-1).
\tag{10}
\]

The coefficient on the left is nonzero. Otherwise (10) forces \(t^p=1\), whence \(t=1\) in characteristic \(p\), contradicting \(51-35=16\ne0\). Therefore, with \(z=t^2\),

\[
z^p=\psi(z):=289/z^6,\qquad
v^4=T(z):=\frac{35(17-z^3)}{z^2(51-35z)}=P/Q.
\tag{11}
\]

Both \(Q(z)\) and \(Q(z^p)\) are nonzero, because Frobenius takes the first nonzero value to the second.

## 3. Frobenius compatibility and finiteness

Let \(y=v^2\), so \(y^2=T\). Equation (8) becomes

\[
v^p\{34Ty+35(1-T)\}=34.
\]

Raise this equation to the fourth power and use \((v^4)^p=T(z)^p=T(\psi(z))\). The result is

\[
T(\psi(z))\{34Ty+35(1-T)\}^4=34^4.
\tag{12}
\]

For \(A_0=34T,B_0=35(1-T)\), reduction modulo \(y^2-T\) writes

\[
(A_0y+B_0)^4=E_0+O_0y,
\]

where \(E_0=A_0^4T^2+6A_0^2B_0^2T+B_0^4\) and \(O_0=4A_0B_0(A_0^2T+B_0^2)\). Squaring the linear equation in \(y\) from (12) gives the necessary condition

\[
\{T(\psi)E_0-34^4\}^2-T\{T(\psi)O_0\}^2=0.
\tag{13}
\]

Clearing denominators in (13) gives precisely (2). In fact its rational left side is

\[
\frac{H(z)}{z^{24}(35z-51)^{12}(3z^6-595)^2}.
\tag{14}
\]

The denominators are nonzero at a putative solution: the first two follow from (11), and \(3z^6-595\ne0\) is equivalent to \(51-35\psi(z)\ne0\). The numerical cancellation involved only \(17^8\), and \(p\ne17\). Consequently \(H(z)=0\).

Because \(H\) has coefficients in the prime field, \(H(z^p)=H(z)^p=0\). Equation (11) now implies \(C(z)=0\). A common root of \(H,C\) forces \(\mathcal R=0\) in characteristic \(p\). This contradicts \(p\nmid\Delta\), proving the assertion for all coefficient cases.

The mechanism is reusable: for a fixed polynomial \(H\) and rational map \(\psi\) over the integers, any point satisfying \(H(z)=0,z^p=\psi(z)\) must also lie in the zero set of the cleared composition \(H\circ\psi\). Coprimality in characteristic zero confines such points to finitely many characteristics, with denominator and content primes handled explicitly. This observation is used here as an elementary elimination argument; no claim of a new general principle is made.

## 4. A practical exact criterion

For a given prime \(p>7\) outside \(\{17,1229,3114019\}\), it suffices to check

\[
\gcd_{\mathbb F_p[z]}(H,C)=1.
\]

A potentially stronger sufficient exclusion test is

\[
\gcd_{\mathbb F_p[z]}(H,z^{p+6}-289)=1,
\]

which uses (11) directly. Compute the power modulo \(H\) by binary exponentiation; the arithmetic degree stays bounded independently of \(p\). A nonconstant gcd in either test is inconclusive, since the norm equation may introduce extraneous solutions. These are exact sufficient exclusion tests, not numerical searches or complete classifications.

## 5. Characteristic-zero consequence

For each good prime \(p>7\), put

\[
J_p=\{1,2,3,5,6,7,p,p+1,p+2,p+3,p+5\}.
\]

Let \(q=p^e\), \(e\ge0\), and \(n=(p+7)q\). At every root \(\alpha\) of a nontrivial characteristic-zero CA polynomial, its monic translate has a nonzero coefficient at some deficiency \(qj\), \(j\in J_p\). Equivalently, at least one ordinary derivative of order \(q(p+7-j)\), \(j\in J_p\), is nonzero at \(\alpha\).

Here is the transfer argument with its quantifiers. Extend a p-adic valuation to a field containing all coefficients and roots. After translating the chosen root to zero, scale a nonzero root of minimum valuation to 1. All roots are integral. In the binomial-normalized expansion \(f=\sum_{j=0}^n\binom nj a_jX^{n-j}\), all \(a_j\) are integral: evaluating the monic normalized derivative of order \(n-j\) at a common integral root expresses \(a_j\) using preceding integral coefficients. Thus coefficients whose binomial factors are divisible by p disappear on reduction. The root 1 survives.

Lucas's theorem says the only nonleading nonconstant visible deficiencies for degree n are q times \(\{1,\ldots,7,p,\ldots,p+6\}\). If all coefficients at qJ_p vanish, reduction is

\[
h(X^q),\qquad h=X^{p+7}+aX^{p+3}+cX^3+dX.
\]

The identity \(H_{qk}(h(X^q))=(H_kh)(X^q)\) and the reduced common-root witnesses imply that h is CA. Its root 1 makes it nonmonomial, contradicting the characteristic-p theorem. This proves the consequence for any chosen root and all e.

For e=0, the excluded ambient family is

\[
X^{p+7}+aX^{p+3}+X^8Q_0(X)+cX^3+dX,
\qquad\deg Q_0\le p-9.
\]

This permits as many as p−4 terms. It excludes that specified family; it does not exclude every polynomial with that many terms. Valuation reduction and Hasse–Frobenius lifting are established methods, including [Graf von Bothmer et al. (2007)](https://arxiv.org/abs/math/0605090) and [Castryck–Laterveer–Ounaïes (2014)](https://arxiv.org/abs/1208.5404).

## 6. What fails, and what remains open

Uniform exclusion at every p is false. Direct Hasse witnesses give \(X^{26}+3X^{22}+14X^3+X\) in characteristic 19 and \(X^{30}+11X^{26}+11X\) in characteristic 23. The separate boundary analysis completely classifies all zero-coefficient cases: at p=17, precisely d=0 and ac=0; away from 17, the c=0 nontrivial boundary occurs at p=23 or 87169343, and the a=0 boundary at p=1229 or 3114019. Those boundary calculations are applications of older two-support techniques and are not claimed as new general results.

The three-coefficient exceptional primes have not been fully classified. An exact bounded computation, independent of the large integer resultant, does classify existence for every prime 7<p<10000: nontrivial members exist exactly at p=17,19,23,1229. The direct H/Frobenius gcd test leaves 19,23,79,257 on the a≠0 chart; reconstructing the v equation gives unit gcds at 79 and 257. The coefficient-boundary proof handles the other charts. The scripts and exact Bezout checks are in `uniform/`; this bounded conclusion is computer-assisted and does not settle primes outside the stated range.

Nor has the unrestricted degree-20 problem been solved. The companion enumeration leaves four possible six-term centered supports after the checked old criteria and the first characteristic-13 obstruction. The separately audited exclusion of \(X^{20}+aX^4+cX^3+dX\) removes one more. Three deficiency supports remain:

\[
\{3,4,10,18,19\},\qquad\{3,10,16,17,19\},\qquad\{4,5,10,17,19\}.
\]

See `sixterm/` for the complete second-seed proof and replay, and `dynamics/LAST_MASK_AUDIT.md` for the separate audit. Survival means only that the applied necessary tests did not exclude these supports; no realization is asserted. A seven-term lower bound has not been proved. The present main result is a uniform arithmetic support obstruction, with exact finite-field certificates and unresolved historical priority.

The support restriction is essential even qualitatively: for every p>7, \(X^{p+7}-X^7\) is a nontrivial characteristic-p CA polynomial. Its only derivative with nonzero value at zero is order 7, whose Hasse derivative \(X^p-1\) shares the root 1. Thus the finite-exception conclusion cannot hold for the unrestricted degree-p+7 problem in characteristic p.
