# Full-scope Casas–Alvero method and status audit

23 September 2026. Focused primary-source refresh. No outreach or publication.

**Decision:** no independently established unrestricted degree-20 proof or
public complete degree-20 certificate was identified in this search. The
working research status remains unresolved, with several full-proof claims.
The strongest usable routes below cover all coefficient supports, but none
currently supplies the missing exclusion. A sparse seven-term lower bound
does not close either target.

## 1. Why the degree-24 statement is not a degree-20 proof

The authors' [Draisma–de Jong erratum, August
2011](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf)
explicitly retracts their degree-20 consequence: characteristic 5 is also
bad in base degree 4. The displayed resultant equations admit the entire
chart \(b=0\). This is direct correction evidence, not an inference from
later surveys.

[Gasull, *A Primer on Resultants and Their Applications*, published 28 May
2026](https://link.springer.com/article/10.1007/s44425-026-00047-6), section
3.4, calls 24 the smallest open degree and cites Draisma–de Jong's 2011
overview as reference 19. That section proves only degrees 4 and 5; it
supplies no later degree-20 argument or replacement reference. The natural
explanation is an inherited uncorrected status statement, but that causal
explanation is an inference. The conflict is unresolved bibliographically;
the sentence is not evidence of a new degree-20 proof.

Current claim records checked:

- [Ghosh 2501.09272](https://arxiv.org/abs/2501.09272) exposes v2 dated
  21 March 2026 and claims all degrees. The campaign's separate Proposition
  3.3 audit and repair investigation govern whether it can be used.
- [Lu 1707.04754](https://arxiv.org/abs/1707.04754) exposes v6 dated
  16 March 2021 and also claims a regular-sequence proof of all degrees.
  It was not certified in this task. “Only claimed full proof” is therefore
  inaccurate.
- [Battiston 1511.04932](https://arxiv.org/abs/1511.04932) is explicitly
  withdrawn for a crucial error.
- [Ghosh's earlier finiteness preprint](https://arxiv.org/abs/2402.18717)
  exposes v3, 14 January 2025. Its claimed dimension/finiteness results
  are not an emptiness theorem and must not be imported past the separate
  audit of its dependencies.

## 2. Unrestricted degree-20 constraints from CLO

[Castryck–Laterveer–Ounaïes, *Mathematics of Computation* 83 (2014),
3017–3037](https://arxiv.org/html/1208.5404), applies to arbitrary
characteristic-zero degree-20 counterexamples:

- Theorem 13: at least five distinct roots.
- Theorem 2: the mean root \(c\) is simple; at least two orders between
  2 and 18 vanish at \(c\); type is at most 16.
- Proposition 7: \(2\le t\le21-\gamma-m-\delta\), using hull vertices
  \(\gamma\), maximum root multiplicity \(m\), and its nonvertex indicator
  \(\delta\).
- Proposition 15 forbids one shared root for orders \(1,19\), for
  \(4,16\), or simultaneously \(5,10,15\).

For deficiency indices \(J=\{j_1<\cdots<j_s\}\subseteq\{2,\ldots,18\}\)
with \(H_{20-j_i}f(c)=0\), Theorem 2 requires \(19\mid\det\Delta_J\),
where the first column is \(-1\), diagonal entries are \(j_i\), lower
entries are \(j_i\binom{j_i-2}{j_h-2}\), and the final row after its
first entry is \(((-1)^{j_h})_h\).

Its projective scenario method covers full degree. When using affine
normalizations modulo a prime, the scenario collection must include
descendants, treated at the same prime (sections 5–6). Omitting collision
descendants invalidates that transfer. The supplied computation is degree
12, not degree 20.

## 3. What Massri adds, and what remains a computation claim

[Massri, arXiv:1806.09561v6](https://arxiv.org/html/1806.09561v6), dated
25 August 2023, is a preprint; its current record supplies no journal
reference. Relevant statements:

- Theorem 7.9: degree-20 root multiplicities are at most 10.
- Theorem 7.10: no three-recycled-root counterexample, so type is at least
  3 if this result is used. It reports checking \(3^{17}\) assignments;
  no public replay or case-list link was retrieved here.
- Remark 7.4 leaves 3125 binary mean-placement masks after its
  restrictions, not 3125 polynomials and not an exclusion of all cases.
- Lemma 5.5: in the normal form with repeated root 0 and mean root 1,
  the 19-adic residue is \(X^{19}(X-1)\). Thus 1 is a simple unit root
  and every other root lies in the maximal ideal. This translation differs
  from centering the mean at zero.
- Theorems 5.7 and 6.2 concern dimension/finiteness and algebraic
  coefficients, not absence of counterexamples.

For derivative-witness indices, the forbidden equalities are
\(y_1=y_{19}\), \(y_4=y_{16}\), and \(y_5=y_{10}=y_{15}\).
Type counts the minimum recycled roots minus one; it is neither the
monomial count nor the number of distinct roots.

## 4. The concrete obstruction to a bare 2-adic reduction

[Chellali's degree-\(5p^e\) result](https://arxiv.org/abs/1211.2059)
explicitly excludes \(p=2\), among eight other bad primes. This blocks
the naive propagation \(20=5\cdot2^2\). The alternative
\(20=4\cdot5\) is blocked by the erratum above.

Here is an independent direct calculation, not a new theorem claim. Over
an algebraically closed field of characteristic 2, an integral normalized
degree-20 CA reduction, with a retained root at 1 and only Lucas-visible
coefficients, has the form

\[
F=X^{20}+aX^{16}+bX^4,\qquad1+a+b=0.
\]

Its order-4 Hasse derivative is \(X^{16}+b\). If \(r\) is a common
root, \(r^{16}=b\), and substituting in \(F(r)\) gives \(ab=0\).
Thus

\[
(a,b)=(1,0)\quad\hbox{or}\quad(0,1).
\]

Both are genuine Hasse-CA seeds: their only nonzero nonconstant Hasse
derivatives have orders 4 and 16, and are witnessed at 0 or 1. They have
root clusters of sizes 16 and 4. Translation by 1 exchanges them.
Equivalently the degree-5 seed \(Y^5+Y^4\) has
\(H_1=Y^4,H_2=H_3=0,H_4=Y+1\), and substitution \(Y=X^4\)
gives the first degree-20 seed.

Therefore a 2-adic proof needs divided-derivative constraints or a
ramification-safe obstruction to lifting these seeds. Prime-field
point enumeration alone cannot help. The direct identities are checked
by `check_structural_facts.py`.

## 5. General criteria with the right scope

### A good prime for every degree

[Graf von Bothmer–Labs–Schicho–van de Woestijne, *Journal of Algebra*
316 (2007), 224–230](https://arxiv.org/pdf/math/0605090), Propositions
2.1–2.2 and 2.6, use a weighted projective CA scheme. Empty geometric
special fibre at one prime implies empty characteristic-zero fibre by
properness, and propagates from \(n\) to \(np^e\). Thus a valid
full-degree-20 certificate can consist of geometric projective emptiness
at a suitable prime. An empty affine chart or absence of rational
prime-field points is insufficient.

**Unproved step for all degrees:** establish, for every \(n\), at least
one good prime, or an equivalent uniform projective emptiness argument.
Proving only degree 20 does not provide this step.

### Uniform regular sequences / exact Macaulay rank

[Schaub–Spivakovsky, arXiv:2411.13967](https://arxiv.org/html/2411.13967),
sections 1–3, gives a full-scope formulation. For every
\(T=(j_1,\ldots,j_{n-1})\in\{1,\ldots,n\}^{n-1}\), set
\(G_{T,i}=\Phi_{j_i}(\sigma_i)\), where \(\sigma_i\) is elementary
symmetric and \(\Phi_j(x_j)=-x_j,\Phi_j(x_h)=x_h-x_j\) for \(h\ne j\);
\(\Phi_n\) is the identity. CA requires

\[
\sqrt{(G_{T,1},\ldots,G_{T,n-1})}=(x_1,\ldots,x_{n-1}).
\]

Equivalently every associated Macaulay matrix at degree
\(D=(n^2-3n+4)/2\) has full column rank. For \(n=20\), direct
arithmetic gives \(D=172\), with
\(\binom{190}{18}=7083408064081415263479975\) columns before reductions.
The paper's numerical upper bound on bad primes assumes characteristic-zero
CA already holds; using that assumption to manufacture a good prime would
be circular.

**Unproved step:** prove regularity/rank for every assignment in every
degree. The criterion does not itself reduce those assignments to a
tractable number.

### Nonredundancy is weaker than regularity

[Schaub–Spivakovsky, arXiv:2312.08742v7](https://arxiv.org/html/2312.08742),
Theorem 5, proves that each of the three highest derivative resultants
is outside the radical generated by the others. This does not imply
that successive resultants avoid every associated prime, which is the
regular-sequence condition needed for a full proof. Its added-in-press
endorsement of Ghosh cites the preprints; it is not an independent
replacement for the disputed argument. The same paper recalls that
omitting any one derivative condition permits real almost-counterexamples.
An argument must therefore use all conditions with their exact dependencies.

[Marashdeh, arXiv:2608.14726v1](https://arxiv.org/html/2608.14726v1),
sections 4 and 8, eliminates coefficients through triangular witness
recursions. For several nonzero recycled roots it leaves more equations
than unknowns. Such an equation count does not establish emptiness;
the general multi-root elimination remains the missing step. Its
single-root descent-count positivity does not settle those systems.

## 6. Practical priority for the full goal

The strongest bounded experiment with full degree-20 scope is a lift
analysis of the complete 2-adic seed classification above, retaining all
18 centered coefficient variables and all divided derivative conditions.
Its possible success is a hypothesis, not a promise. The 19-adic
mean-placement decomposition is an independently useful constraint on
the same unrestricted polynomial, but simultaneous local normalization
must not identify roots or coefficient residues across primes without
an exact argument.

For all degrees, a valid repair of the general regular-sequence argument
would have the required scope. Degree-by-degree sparsity improvements do
not. The explicit missing statement is the non-zero-divisor condition on
every remaining component, including embedded components; generator
counts only at minimal primes do not automatically supply it.

No current rigorous full certificate was retrieved. That is a search
result with the limits recorded in `QUERY_COVERAGE.md`, not an absolute
claim that no proof or private computation exists. The earlier ProofAtlas
source gap remains unresolved.

## 7. The characteristic-17 alternative: exact seed formulas

The same Lucas and coefficient-integrality argument gives, for degree
\(p+3\), \(p>3\), the centered residue family

\[
h=X^{p+3}+aX^{p+1}+bX^p+cX^3+dX^2+eX.
\]

This applies at \(p=17\) to unrestricted degree 20; it does not assume
that the original characteristic-zero polynomial was sparse. Set

\[
g=X^3+aX+b,\quad L=X^p+c,\quad
Q=dX^2+(e-ac)X-bc.
\]

Then \(h=Lg+Q\). Direct Lucas expansion gives exactly the following
possibly nonzero Hasse derivatives of positive order below the degree:

\[
\begin{aligned}
H_1h&=L(3X^2+a)+2dX+(e-ac),\\
H_2h&=3XL+d, & H_3h&=L,\\
H_ph&=g, & H_{p+1}h&=3X^2+a,
& H_{p+2}h&=3X.
\end{aligned}
\]

All orders from 4 to \(p-1\) are identically zero. Hence the unique root
\(u\) of \(L\) must obey \(Q(u)=0\), and a witness \(v\) for
\(H_ph\) must satisfy \(g(v)=Q(v)=0\). These equations reduce the
seed classification to the interaction of a cubic and a quadratic, plus
the remaining witness conditions. They do not prove the seed set finite
or classify its characteristic-zero lifts.

The direct \(p+3\) searches listed in `QUERY_COVERAGE.md` located no
primary-source classification of this exact family. The adjacent result
in [Kreidl's thesis](https://homepage.univie.ac.at/herwig.hauser/Publications/diplom_kreidl.pdf),
Satz 4.24, concerns degrees \(d_kp^k\) with one nonzero base-\(p\)
digit; it does not cover \(p+3\). Its following sparse examples concern
\(p-1\) and \((p-1)/2\), also different families. The formulas above
are elementary working identities, with no novelty claim.

Replay of `check_structural_facts.py` succeeded with ordinary Python and
with `python3 -O` on 23 September 2026. That small replay checks only the
characteristic-two seed identities, their Lucas indices, and the quoted
Macaulay matrix-size arithmetic; it does not verify the literature's
theorems or a lift exclusion.
