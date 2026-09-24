# Independent audit of Ghosh, Proposition 3.3

Audit date: 23 September 2026. Auditor: a separate Codex agent reconstructing the ideal directly from the primary source, without reading another agent's derivation. This is a mathematical derivation with optional computational cross-checks, not independent human refereeing.

Primary source: Soham Ghosh, *Proof of the Casas-Alvero conjecture*, [arXiv:2501.09272v2](https://arxiv.org/html/2501.09272v2), Section 2(iii)–(vi), Proposition 3.3, and its proof following equation (3.8). The public HTML identifies v2 as submitted 21 March 2026; its displayed internal manuscript date is 24 August 2026. The version and exact bytes should be retained separately by the root audit.

## Finding

Proposition 3.3 is false under its stated characteristic restriction. For n=3, the excluded product is 9, so both characteristics 5 and 7 are allowed. In either characteristic, the index choice j=(1,2,3) gives an ideal with three global minimal generators and two minimal generators at its unique minimal prime. The same holds for all 24 ordered triples of distinct indices from {1,2,3,4}, by a root-label symmetry proved below.

The failure is an embedded component at the origin. Localization at the generic point of the line removes that component and a generator. There is explicit t-torsion in the generator module, and also in the literal quotient used for the paper's disputed cancellation step.

This refutes the proposition as stated; it does not refute the characteristic-zero Casas-Alvero conjecture or prove the characteristic-zero restriction of Proposition 3.3 false.

## 1. Direct reconstruction of the generators

Write R=k[x,y,z]. The source defines the generators by applying its root-recentering automorphisms to elementary symmetric polynomials of degrees 3, 2, and 1. For j=(1,2,3), this gives exactly

\[
 F_1=-x(y-x)(z-x),\qquad
 F_2=xz-2xy-2yz+3y^2,\qquad
 F_3=x+y-3z.
\]

Set I=(F_1,F_2,F_3). No formula inferred from a claimed Gröbner basis is being used here: these are direct substitutions into xyz, xy+xz+yz, and x+y+z respectively.

Eliminating F_3 gives x=3z-y and

\[
 \overline F_1=(y-3z)(y-2z)(2y-3z),\qquad
 \overline F_2=5y^2-9yz+3z^2.
\]

## 2. Characteristic 5: a monomial ideal

Work over any field k of characteristic 5, including an algebraic closure if desired. Make the invertible linear change

\[
 \ell=x+y-3z,\qquad u=y-2z,\qquad t=z.
\]

Its inverse is x=ell+t-u, y=u+2t, z=t. In these coordinates,

\[
 F_3=\ell,
 \qquad F_2=(2t-2u)\ell+ut,
\]

and

\[
 F_1=-\ell^3-\ell^2u+\ell t^2+\ell tu-ut^2-u^2t+2u^3.
\]

Consequently,

\[
 \boxed{I=(\ell,ut,u^3).}
\]

Both containments are explicit: F_1 and F_2 belong to the displayed ideal, while ut=F_2-(2t-2u)ell and, modulo ell, 2u^3=F_1+(u+t)ut. Since 2 is a unit, u^3 also belongs to I.

### Global minimal number of generators

Let m=(ell,u,t). None of the three monomials ell, ut, u^3 belongs to mI. Their nonzero classes are linearly independent in I/mI because distinct monomials cannot cancel. They generate I/mI, so its dimension over k is 3. Nakayama's lemma gives mu(I_m)=3, hence mu_R(I)>=3. The displayed generators give the reverse inequality, and therefore

\[
 \mu_R(I)=3.
\]

This argument rules out arbitrary alternative generating sets, not only the possibility of dropping one of the three displayed generators.

### Unique minimal prime and its localization

Since u^3 lies in I and I is contained in (ell,u), its radical is

\[
 \mathfrak p=(\ell,u)=(x-z,y-2z).
\]

Thus p is the unique minimal prime. Its height is 2. Since t is not in p, it is a unit in R_p, and ut generates u there. It follows that

\[
 I_{\mathfrak p}=\mathfrak pR_{\mathfrak p}=(\ell,u)R_{\mathfrak p}.
\]

Krull's height theorem gives the lower bound 2 for its number of generators; the displayed pair gives the upper bound 2. Hence

\[
 \boxed{\mu_{R_{\mathfrak p}}(I_{\mathfrak p})=2<3=\mu_R(I).}
\]

### Embedded component and actual torsion

The primary decomposition is the elementary monomial identity

\[
 I=(\ell,u)\cap(\ell,t,u^3).
\]

The second ideal is m-primary and gives an embedded component at the origin. Multiplication by the minimal prime gives

\[
 \mathfrak pI=(\ell^2,\ell u,u^2t,u^4).
\]

The class of u^3 is nonzero in I/pI because u^3 is not in this monomial ideal, while t u^3 is in pI. Thus the generator module I/pI has nonzero t-torsion. Inverting t kills this class without annihilating the quotient ring: the image of 1 is still nonzero.

## 3. Literal torsion in the quotient used in Proposition 3.3

The preceding calculation can be matched exactly to the construction around equations (3.6)–(3.8), rather than merely used as an analogy.

Continue in characteristic 5. Normalize the line by the vector a=(3,1,3), choose r=2, and write the paper's parameter t as s to avoid confusing it with the preceding coordinate z. Thus a_r=1 and the full translated generators H_i are

\[
 H_i=F_i(3s+A,s+B,3s+C).
\]

The marked variable y_r is B. Define the invertible linear coordinates

\[
 L=A+B-3C,\qquad U=B-2C,\qquad B=B.
\]

The paper's ideal m^+ becomes (L,U,B). Translating the identity I=(ell,ut,u^3), observing that z=3s+C=3s+3B+2U, and then adjoining B gives

\[
 J^+=(H_1,H_2,H_3,B)
     =(L,B,Q,U^3),\qquad Q=3sU+2U^2.
\]

In the ring k[s,L,U,B]/m^+J^+, the class of U^3 is nonzero. Indeed, quotienting further by L and B gives

\[
 k[s,U]/(3sU^2+2U^3,U^4).
\]

The degree-three part of this last ideal is exactly the k-span of 3sU^2+2U^3, so it does not contain U^3. Nevertheless,

\[
 3sU^3=U^2Q-2U^4\in m^+J^+.
\]

Since 3 is invertible, s annihilates the nonzero class of U^3. This is an explicit zero divisor in the very quotient where the paper asserts that its parameter is a non-zero divisor. It is not merely a counterexample to a general rule about localization.

The quotient remains nonzero after inverting s: m^+J^+ is still contained in the proper ideal (L,U,B). Thus the paper's argument that inverting a zero divisor would make the quotient zero does not apply. A localization becomes the zero ring only when some element of the multiplicative set is zero in the original ring; nonzero torsion alone is insufficient.

## 4. Characteristic 7

Over any field of characteristic 7, use

\[
 \ell=x+y-3z,\quad u=y-3z,\quad t=z,
 \qquad x=\ell-u,\ y=u+3t.
\]

Modulo ell,

\[
 F_2=5u^2,\qquad
 F_1=2u^3+5u^2t+3ut^2.
\]

Because 5 and 3 are units,

\[
 \boxed{I=(\ell,u^2,ut^2).}
\]

Exactly the same graded Nakayama argument gives mu_R(I)=3. Its unique minimal prime is p=(ell,u)=(x,y-3z). In R_p the element t is invertible, so ut^2 generates u and I_p=pR_p. Therefore its local minimal generator number is 2.

The primary decomposition is

\[
 I=(\ell,u)\cap(\ell,u^2,t^2).
\]

Here pI=(ell^2,ell u,u^3,u^2t^2). The nonzero class u^2t in I/pI is annihilated by t; equivalently the nonzero class u^2 is annihilated by t^2.

## 5. Why all 24 distinct-entry triples follow

Introduce four root coordinates r_1=x,r_2=y,r_3=z,r_4=0. For each root index j and degree d in {3,2,1}, the paper's generator is the elementary symmetric polynomial e_d in the three differences r_k-r_j with k!=j.

For a permutation sigma in S_4, make the invertible linear substitution

\[
 x_i\longmapsto r_{\sigma(i)}-r_{\sigma(4)},\qquad i=1,2,3.
\]

The transformed differences are precisely r_{sigma(k)}-r_{sigma(j)}, so this substitution sends the generator indexed by j to the one indexed by sigma(j), with its derivative order unchanged. Consequently it sends I_3(j_1,j_2,j_3) isomorphically to I_3(sigma(j_1),sigma(j_2),sigma(j_3)).

The 24 permutations of four labels carry (1,2,3) bijectively to all 4*3*2 ordered distinct-entry triples. Ring isomorphisms preserve minimal primes, global minimal generator counts, and the corresponding localized counts. Thus all 24 examples follow from the single calculation in each characteristic. They are symmetry copies, not 24 algebraically unrelated mechanisms.

## 6. Characteristic-zero limitation and precise bad-prime calculation

For the same tuple over characteristic zero, the eliminated forms have no common projective root. In fact

\[
 \operatorname{Res}_Y((Y-3)(Y-2)(2Y-3),\,5Y^2-9Y+3)=315=3^2\cdot5\cdot7.
\]

There is no common root at infinity: at z=0 the two binary forms are 2y^3 and 5y^2, which never both vanish at a nonzero projective point in any characteristic. Therefore, among the characteristics permitted by Proposition 3.3 for n=3, precisely 5 and 7 yield the nonzero line for this distinct-index orbit. In characteristic zero the ideal is primary to the homogeneous maximal ideal and has height 3, so its local and global generator counts are both 3. This example cannot establish a characteristic-zero counterexample to the proposition.

## Computational corroboration

The companion script `counterexample-agent-check.py` reconstructs the generators from elementary symmetric polynomials and the source's substitutions. It verifies the two ideal equalities using SymPy over the finite fields; verifies both torsion witnesses; verifies the literal m^+J^+ torsion witness; and checks all 72 generator identities implementing the S_4 symmetry over the integers. Its output is saved separately. These checks corroborate the hand proof; the proof does not depend on a Gröbner-basis implementation.

## Audit scope

- Refuted: Proposition 3.3 under its published characteristic hypothesis, and the particular regularity assertion used in its proof.
- Established: explicit global/local discrepancy, unique minimal prime, embedded primary component, and the actual torsion responsible for loss of a generator.
- Not established: a false statement in characteristic zero, a counterexample to Casas-Alvero in characteristic zero, or a proof that every conceivable repair is impossible.
- The root audit should separately trace the dependency of the main theorem and assess whether a replacement lemma can be proved without circular reliance on the conjecture.
