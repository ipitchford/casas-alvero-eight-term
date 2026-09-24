# Argument audit: the row-1 ramification obstruction

Research audit, 24 September 2026. No paper or bundle was produced.

**Argument conclusion: PASS**, with the exact arithmetic checks recorded below. The revised proof excludes the stated exact support \(\{3,6,10,16,17,19\}\). Its separate nonzero-\(a_3\) extension is also valid with the hypotheses stated in the producer note. Neither result proves an eight-term bound or the degree-20 conjecture. This is an internal proof audit and exact replay, not external refereeing or proof-assistant certification.

## 1. Algebraic and valuation setting

The passage from a complex counterexample to an algebraic counterexample is legitimate. All common-root equations are polynomial equations over \(\mathbf Q\); introduce an inverse variable for the product of the coefficients required to be nonzero. A complex solution implies that this ideal is proper. A maximal ideal over \(\overline{\mathbf Q}\) then gives an algebraic solution with the same exact support. Only this new algebraic point is placed in a fixed valued algebraic closure of \(\mathbf Q_{17}\). The proof does not assign a 17-adic valuation directly to arbitrary transcendental complex coefficients.

The established CA integral normalization retains a unit root, so reduction is nonmonomial. Exact coefficient zeros remain zero under scaling. The complete nine-seed classification leaves rows 1 and 8 for this support; the previously checked row-8 obstruction is an explicit dependency of the global conclusion. In row 1 every unit root reduces to one. The common Hasse-third root is a unit because its derivative has unit constant coefficient. Scaling this root to one preserves both the seed and the stipulated coefficient residues.

For the exact support, the linear coefficient \(E\ne0\); zero is simple. The ordinary cubic coefficient \(D\) is a unit, and there is no quadratic term. For any nonzero small root \(q\), the terms \(E\) and \(Dq^2\) in \(f(q)/q\) are the only possible lowest terms. Thus the two nonzero small roots both have valuation \(\delta=\nu(E)/2\). In \(f'(q)-f(q)/q\), the term \(2Dq^2\) is uniquely lowest. These roots cannot be repeated. This also proves that every repeated root lies in the unit cluster.

Since \(G_3=X^3+t\) and \(t\ne0\), its common root is nonzero and small. Hence \(\nu(t)=3\delta\). All other summands in the formula for \(E\) have valuation at least one. The inequality \(2\delta\geq\min(1,3\delta)\) therefore rules out \(\delta<1/2\), and gives \(\nu(t)\geq3/2\). None of these arguments assumes integral root valuations.

## 2. The residue sieve and coefficient bounds

After this preliminary bound, all coefficients \(c_1,\ldots,c_{16}\) of \(f(1+Y)\) lie in \(17\mathcal O\), and \(c_{17}\) is a unit. A nonzero displacement of a unit root cannot have valuation below \(1/16\): the \(c_{17}Y^{16}\) term would be uniquely lowest in \(f(1+Y)/Y\). At a repeated root, all nonconstant terms of the ordinary derivative then have valuation greater than one. For the \(c_{17}\) term this uses the factor 17 in differentiation; for the subsequent terms it uses \(17/16>1\). Consequently \(c_1/17\) has zero residue.

The eight binary markings for \(G_6,G_{10},G_{16}\) are exhaustive because the seed has only the root residues zero and one. The recurrence is triangular and fixes all residue coefficients. Independently reconstructing the divided linear constraint gives:

| Witness residues | \((\bar v,\bar b,\bar u)\) | Divided constraint |
|---|---|---:|
| 000 | (0,0,0) | 3 |
| 001 | (0,0,16) | 0 |
| 010 | (0,16,0) | 2 |
| 011 | (0,16,0) | 2 |
| 100 | (16,0,0) | 5 |
| 101 | (16,0,0) | 5 |
| 110 | (16,5,0) | 10 |
| 111 | (16,5,12) | 12 |

Thus only \((0,0,-1)\) survives. The zero residues force the \(G_6,G_{10}\) witnesses to be small, since their reduced normalized derivatives are respectively \(X^6,X^{10}\). The unit \(G_{16}\) witness reduces to one.

The residue \(\overline{E/17}=11\) gives \(\delta=1/2\), \(\nu(t)=3/2\). The triangular equations at small roots give \(\nu(v)\geq3\), \(\nu(b)\geq5\). Thus their ordinary polynomial contributions have valuation at least four. An independent binomial expansion reproduced all four displayed low Taylor coefficients, \(c_{17}=1140(1+t)\), and the crucial combined linear residue \(1425\cdot16+1520\equiv10\pmod {17}\).

## 3. All possible displacements and collisions

Let \(x\) be the common \(G_{16}\) root and put \(z=x-1\). Its derivative equation gives

\[
u=-x^{16}-560tx^{13}+e,\qquad \nu(e)\geq3.
\]

If \(0<\epsilon=\nu(z)<1/2\), the uniquely relevant two candidate orders in \(f(x)/z\) are \(1+\epsilon\) and \(16\epsilon\). The first has nonzero combined residue 10; the \(t\) contribution has higher value \(3/2\), and every other term is higher than their minimum. Thus \(\epsilon=1/15\).

If finite \(\epsilon>1/2\), then \(\nu(u+1)>1/2\). The unit multiple of \(t\) in \(c_1\) gives \(\nu(c_1)=3/2\), strictly below every other term of the divided-root equation. This is impossible.

The boundary \(\epsilon=1/2\) is also covered. Here \(\nu(c_1)\geq3/2\), while \(\nu(c_2z)=3/2\) and every remaining term is larger. The exact root equation therefore forces \(\nu(c_1)=3/2\), even if its two leading contributions initially appeared capable of cancellation. If \(z=0\), the same value of \(c_1\) follows directly from the \(t\) term.

In these last two cases the unit-cluster Newton polygon has fifteen outer roots of displacement value \(1/15\), one inner root of value \(1/2\), and the exact root one. The outer residual polynomial is \(Y^{15}+7\), with fifteen distinct nonzero roots. The inner segment has length one. The exact root one is simple because \(c_1\ne0\). All seventeen roots in the unit cluster are simple, contradicting the required repeated root.

It remains that \(\epsilon=1/15\). Choose \(\pi^{15}=17\) and let \(\xi=\overline{z/\pi}\). The scaled initial polynomial is

\[
Y^{17}+7Y^2+3\xi Y,\qquad \xi^{15}=7.
\]

The revised proof includes the necessary full-cluster bound: no other unit root can have displacement valuation below \(1/15\), since then \(c_{17}Y^{16}\) is uniquely lowest in the divided polynomial. Therefore all seventeen roots are represented in this initial polynomial, counted with multiplicity. Its derivative is \(14Y+3\xi\), so the only repeated residual root is \(\xi\); it has multiplicity exactly two because the quadratic Hasse derivative is 7. All other residual roots lift to simple roots. The selected actual root \(x\) lies in the double class. A different repeated root there would use at least three roots counted with multiplicity. Consequently the repeated root is exactly \(x\), proving \(f(x)=f'(x)=G_{16}(x)=0\).

## 4. The local-field contradiction

The checked eliminant coefficient bounds imply

\[
S(Z)=\frac{R(1+\pi Z)}{17\pi^2 Z^2}\in\mathcal O_{K_0}[Z],
\quad K_0=\mathbf Q_{17}(\pi),\quad \bar S=7-Z^{15}.
\]

The displayed quotient is a polynomial because the exact translated eliminant is divisible by \(z^2\). The reduction has simple roots. No claim about simplicity of every possibly nonintegral root of \(S\) is needed.

Inside the same fixed valued algebraic closure, set

\[
L=K_0\,\mathbf Q_{17}^{\mathrm{unr},4}.
\]

The Eisenstein polynomial \(T^{15}-17\) makes \(K_0\) totally ramified of degree 15. The compositum is unramified of degree four over \(K_0\), has residue field \(\mathbf F_{17^4}\), and has value group exactly \((1/15)\mathbf Z\). Every possible actual \(\xi\) is present in this residue field: all solutions of \(\xi^{15}=7\) are 5 times fifteenth roots of unity, and \(5^{15}=7\), \(15\mid17^4-1\). Thus no extra restriction on the residue of the candidate was introduced.

Let \(Z_0\in L\) be the unique Hensel lift of the actual residue \(\xi\), and \(x_0=1+\pi Z_0\). The error estimate \(\nu(R(x))\geq4\) gives

\[
\nu(S((x-1)/\pi))\geq4-1-2/15=43/15.
\]

The polynomial divided difference between \(Z=(x-1)/\pi\) and \(Z_0\) is a unit because it reduces to \(\bar S'(\xi)\ne0\). Hence

\[
\nu(x-x_0)\geq44/15.
\]

This remains true after adjoining the arbitrarily ramified candidate field; no containment of that field in \(L\) was assumed. Since \(Q_1\) has unit value throughout the residue class of one, the integral rational function \(-Q_0/Q_1\) satisfies the valuation inequality

\[
\nu\bigl(g(x)-g(x_0)\bigr)\geq\nu(x-x_0).
\]

The approximate \(Q\)-equation therefore gives \(\nu(t-t_0)\geq44/15>3/2\), where \(t_0=g(x_0)\in L\). This forces \(\nu(t_0)=\nu(t)=3/2\), which is absent from \((1/15)\mathbf Z\). The contradiction is valid.

## 5. Separate uniform nonzero-\(a_3\) extension

The extension also passes. Its hypotheses are essential: in the normalized row-1 seed, \(a_2=a_{18}=0\) exactly; \(a_3=t\ne0\) has positive valuation; \(a_4,\ldots,a_{15}\) have zero residues; and \(\bar a_{16}=-1\). There is no bound on how many of \(a_4,\ldots,a_{15}\) are nonzero.

If \(E=0\), the cubic term is a unit and zero is an exact triple root, exhausting the small cluster. But \(G_3=X^3+t\) needs a nonzero common root reducing to zero. This excludes that boundary case immediately. Otherwise the same small-cluster argument gives \(\delta=1/2\) and \(\nu(t)=3/2\).

For \(4\leq j\leq15\), reduction of \(G_j\) is \(X^j\); hence any selected witness is small (or exactly zero when permitted). Triangular induction gives \(\nu(a_j)\geq j/2\), interpreting zero coefficients as valuation infinity. The binomial coefficients \(\binom{20}{j}\) all have valuation one for these indices. Thus all discarded ordinary contributions have valuation at least three, and their contribution to \(G_{16}\) has valuation at least two. Eliminating \(a_{16}\) introduces another factor \(\binom{20}{16}\), again of valuation one, so both approximate \(P,Q\) errors have valuation at least three.

All cluster comparisons above are strict below this error threshold, so the repeated-root collision remains valid. The same eliminant now gives

\[
\nu(S(Z))\geq28/15,\qquad \nu(x-x_0)\geq29/15>3/2.
\]

The same value-group contradiction excludes the entire stated nonzero-\(a_3\) stratum. The residue conditions are hypotheses for this uniform result; the eight-marking sieve only establishes them in the exact-support application. The proof does not extend the \(a_3=0\) result to \(a_4\ne0\). The producer note correctly retains that boundary as unproved by this argument.

## 6. Exact-check record

The eight markings and the low Taylor coefficients were independently recomputed using standard-library binomial arithmetic during this audit. The separate elimination checker reconstructs the ordinary polynomial, differentiates it, composes at the marked root, and checks the full integer coefficient arrays of \(P_0,P_1,Q_0,Q_1,R\). It also checks every translated coefficient valuation and the normalized initial polynomial. These finite checks establish the coefficient claims; the preceding arguments supply the ramification and coverage reasoning that finite arithmetic alone does not prove.

The finished checker includes the eight-marking census and the residue-field checks. It was inspected and replayed normally and under `python3 -O` from `/private/tmp`. Both runs returned PASS, with identical parsed outputs agreeing exactly with both saved receipts. A supplied-checker replay is not a new independent implementation; the separate binomial calculation and valuation/field arguments above are the independent audit work.

| Reviewed input | SHA-256 |
|---|---|
| `ROW1_RAMIFICATION.md` | `81d077a984e6aa33b0e5c3f375538884db055c160fcb009ca312741c130bba8b` |
| `row1-ramification/check_row1_elimination.py` | `43128c3b951f5fce880309be875b650f2cf849ab8de740d2f08e6ab234d2d478` |
| `row1-ramification/row1-elimination-certificate.json` | `68f783490d20f46b0defb1e221e0c16a32e6904e248aeba86dcf11954001e2d4` |
| `row1-ramification/verification.json` | `4b264a920c9645f1c2462b9b4d0b3297a1d383f96843bf0a4e500b9480e664c1` |

The revised source includes the requested specialization, full-cluster, and simple-reduction clarifications. No blocking gap remains in the exact-support proof or in the separately stated uniform nonzero-\(a_3\) extension. The existing row-8 exclusion and complete seed classification remain dependencies of the global exact-support conclusion; their full proofs were not replayed in this bounded audit.
