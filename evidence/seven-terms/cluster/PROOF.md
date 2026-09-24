# Excluding the family-C residue row (v,u,w)=(2,1,4)

Internal proof candidate, 23 September 2026. Arithmetic is independently
replayable; the valuation argument is stated explicitly for adversarial
review. No publication or full-conjecture claim.

## Proposition

Let K be a characteristic-zero valued field extending the 13-adic
valuation, normalized by nu(13)=1, with valuation ring O. Arbitrary
ramification is allowed. Suppose

\[
f=X^{20}-4845X^{16}+B X^{15}+C X^{10}+D X^3+E X
\]

has integral coefficients and roots, with f(1)=0 and residues
(B,D,E)=(6,3,12). There do not exist
common-root witnesses u,v,w,z for Hasse derivative orders 15,3,1,10,
respectively, with residues u=1,v=2,w=4. The witness z is unrestricted.

The conclusion also covers u=1 exactly. It does not assume integer
valuations of any root difference or unramified lifting.

We first derive the coefficient bound needed below. The integral H10
common root z gives

\[
C=-184756z^{10}-8008A z^6-3003B z^5\in13O,
\]

because all three displayed integers are divisible by 13 and A,B,z
are integral. Hence nu(C)>=1 is a consequence of the hypotheses,
not an assumption that a positive valuation is an integer.

## 1. Exact normalizations and a unit Jacobian

Write A=-4845 and B0=62016. The H15 equation at u gives

\[
B=77520u-15504u^5.
\]

With s=u-1 and beta=B-B0, this becomes

\[
\beta=-15504s^2(10+10s+5s^2+s^3).                     \tag{1}
\]

The parenthesized factor and 15504 are units at 13. If s!=0 and
r=nu(s)>0, then nu(beta)=2r. If s=0, beta=0.

Eliminate E by f(1)=0, so E=-1-A-B-C-D. Put delta=v-2,
eta=D-3. The two equations f(v)=0 and H3f(v)=0, expanded about
v=2,D=3,B=B0,C=0, have Jacobian in (delta,eta) reducing to

\[
J=\begin{pmatrix}9&6\\4&1\end{pmatrix},\qquad
\det J=11\ne0\quad(\bmod13).                         \tag{2}
\]

Both constant defects at that base point are divisible by 13.
All expansion coefficients are integral.

Consequently

\[
\min\{\nu(\delta),\nu(\eta)\}
\ \ge\ \min\{1,\nu(\beta),\nu(C)\}.                \tag{3}
\]

Here is a direct valuation justification, without assuming a Hensel
lifting theorem over a particular field. Let m be the minimum on the
left. If m were strictly smaller than the right side, the linear
Jacobian part would have minimum valuation exactly m because J is
invertible over O. The constant terms, beta and C terms would have
larger valuation; every remaining term involving delta or eta would
have larger valuation as well, since delta and eta have positive
valuation and the omitted terms are at least quadratic or multiplied
by beta or C. Such a linear leading part cannot sum to zero. This
proves (3), including when some differences vanish exactly.

## 2. The high-derivative root is within 13O of 1

If s=0, (1) already gives beta=0. Suppose s!=0. A direct exact
calculation gives

\[
f'(1)=13\cdot61198+14\beta+9C+2\eta,
\qquad H_2f(1)\equiv9\pmod{\mathfrak m}.             \tag{4}
\]

If 0<r<1, equations (1) and (3) and nu(C)>=1 imply

\[
\nu(f'(1))\ge\min\{1,2r\}>r.
\]

But f(u)=f(1)=0, divided by the nonzero s, gives

\[
0=f'(1)+H_2f(1)s+H_3f(1)s^2+\cdots.                 \tag{5}
\]

The second term has valuation r and is uniquely of smallest valuation:
the first has valuation greater than r and every later term at least
2r. This contradiction proves nu(s)>=1. Combining with the s=0 case,

\[
\nu(\beta)\ge2,
\qquad \nu(v-2)\ge1,
\qquad \nu(D-3)\ge1.                                \tag{6}
\]

The latter two inequalities follow again from (3). They were derived,
not assumed from the residue values.

## 3. The triple cluster forces a third linear residue equation

Write

\[
C=13k,\quad v=2+13t,\quad D=3+13l,
\qquad k,t,l\in O.
\]

By (6), B=B0 modulo 13^2 O. Dividing f(v)=H3f(v)=0 by 13
after exact Taylor expansion gives the following equations in the
residue field (bars are suppressed):

\[
9t+6l+8k+12=0,\qquad4t+l+7k+6=0.                   \tag{7}
\]

Let tau=w-4. The residue polynomial is

\[
h=X^{20}+4X^{16}+6X^{15}+3X^3+12X.
\]

Since all coefficient perturbations from the integer base polynomial
are now in 13O, both f'(4) and f''(4) belong to 13O. Furthermore

\[
\frac{f'''(4)}2=3H_3f(4)\equiv2\pmod{\mathfrak m}.
\]

In the Taylor expansion of f'(4+tau)=0, if
0<nu(tau)<1/2, the quadratic term would be uniquely of smallest
valuation. Thus nu(tau)>=1/2; if tau=0 the same bound holds with
infinite valuation. Expanding f(4+tau)=0 now shows

\[
\nu(f(4))\ge3/2>1.                                  \tag{8}
\]

Indeed the linear term has valuation at least 1+nu(tau), the
quadratic term at least 1+2nu(tau), and every later term at least
3nu(tau). All are at least 3/2. The divisions by 2 or 6 in
these expressions are units at 13; alternatively these are integral
Hasse-Taylor expansions.

Dividing f(4) by 13 and reducing using (8) therefore yields

\[
8l+5k+1=0.                                           \tag{9}
\]

The coefficient matrix of (7),(9) in (t,l,k) is

\[
\begin{pmatrix}9&6&8\\4&1&7\\0&8&5\end{pmatrix},
\]

whose determinant is 2 modulo 13. Its unique solution is

\[
(t,l,k)=(5,7,12).                                    \tag{10}
\]

All statements (6)–(10) apply over arbitrary residue extensions and
arbitrary ramified value groups; no lift modulo 169 was presumed.

## 4. The divided middle derivative supplies the contradiction

The Hasse derivative of order 10 is

\[
H_{10}f=184756X^{10}+8008A X^6+3003B X^5+C.
\]

Since 184756=13*14212, with 14212 congruent to 3 modulo 13,
division by 184756 gives a monic polynomial with integral
coefficients. Using (10), its reduction is

\[
g=X^{10}+11X^6+7X^5+4.                               \tag{11}
\]

The integral common root z of f and H10f would therefore reduce
to a common root of h and g. But the explicit polynomials

\[
U=X^9-2X^8+6X^7+3X^5+5X^4-X^3+5X^2-3X+2,
\]
\[
\begin{aligned}
V={}&-X^{19}+2X^{18}-6X^{17}+4X^{15}-5X^{14}+2X^{13}
       +X^{12}-X^{11}\\
   &+4X^9+5X^8-3X^7+4X^6+6X^5+2X^4+3X^3-4X^2-6X-3
\end{aligned}
\]

satisfy

\[
Uh+Vg=1\qquad\text{in }\mathbb F_{13}[X].             \tag{12}
\]

Thus there is no common root in any residue extension. This is the
required contradiction.

## Arithmetic replay and scope

`check_jets.py` reconstructs the integer normalizations, B expansion,
Jacobians, first-order constants and coefficients, middle-derivative
reduction, and verifies (12) by direct multiplication using only the
Python standard library. Its explicit checks remain active with -O.
The valuation inequalities are the written proof; the checker does
not replace their independent review.

This proposition excludes the specified last cluster row of family C.
Combining it with other branch exclusions requires their separate
proofs and the previously certified completeness of the residue
classification. It does not alone prove a global CA result.
