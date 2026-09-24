# Independent adversarial audit: sparse degree-20 theorem

Date: 23 September 2026. Result: **PASS for mathematical correctness, within the stated sparse scope and with the cited published inputs.** Novelty is not established by this audit. This is not a proof of the full degree-20 Casas–Alvero conjecture.

## Exact conclusion

Let f be a nontrivial Casas–Alvero polynomial of degree 20 over C. Translate its center of mass to zero and divide by the leading coefficient. Then the resulting monic polynomial has at least five nonzero terms, including its leading term.

Equivalently, the monic centered CA condition for a polynomial with at most four nonzero terms forces f=x^20. The restriction concerns term count **after centering**, not in an arbitrary coordinate system. The theorem does not bound the number of distinct roots by five; that is a different, previously known statement.

## Published inputs and index audit

The inputs are [Castryck–Laterveer–Ounaies, Theorem 2 and Proposition 15](https://arxiv.org/html/1208.5404v1). Theorem 2 supplies f'(0) != 0 and a determinant congruence modulo 19. Proposition 15 prohibits a common root of specified derivatives. These are applied over C, not reduced modulo 31.

Write the support indices as m when the monomial is x^(20-m). Centering removes x^19, and the CA condition at derivative order 19 makes the constant term zero. The nonleading support S is therefore a subset of {2,...,19}.

The following independent substitutions into the published statements are correct:

- Theorem 2, with p=19: f'(0) != 0, so 19 belongs to S.
- Proposition 15, p=2, k=2, n=5=2^2+1: f, f^(4), f^(16) cannot all vanish at zero. Hence S meets {4,16}.
- Proposition 15, p=5, k=1, n=4: f, f^(5), f^(10), f^(15) cannot all vanish at zero. Hence S meets {5,10,15}.

These three sets are pairwise disjoint. Thus |S|<=2 is impossible for a nontrivial CA polynomial. If |S|=3, there are exactly six possibilities. For each, the determinant uses the **zero coefficient indices** J={2,...,18} minus S, not S itself. Independent modular triangular elimination gives:

| S | determinant modulo 19 |
|---|---:|
| (4,5,19) | 15 |
| (4,10,19) | 7 |
| (4,15,19) | 10 |
| (5,16,19) | 0 |
| (10,16,19) | 12 |
| (15,16,19) | 13 |

Only (5,16,19) remains. Normalizing coefficients by binomial factors does not change this zero pattern in characteristic zero. The determinant is the integer matrix from the theorem, reduced modulo 19; coefficients of f are not being reduced for this step.

## Derivative normalization and completeness

The survivor is f=x^20+a x^15+b x^4+c x with a,b,c nonzero. The only derivative orders not already sharing zero with f are 15,4,1. Their Hasse derivative constants are a,b,c respectively, so their common roots r_1,r_2,r_3 are all nonzero. They need not be distinct.

Rescale x by r_1 and divide f by r_1^20. Write u=r_2/r_1 and v=r_3/r_1. The three derivative equations force

    a=-15504,
    b=-4845 u^16+21162960 u^11,
    c=-20 v^19-15a v^14-4b v^3.

The checked binomial constants are binom(20,5)=15504, binom(20,4)=4845, binom(15,4)=1365, and 15504*1365=21162960. These derivative equations are triangular with coefficient one on each newly eliminated coefficient.

Since each witness is nonzero, the remaining root equations are precisely

    E1=1+a+b+c,
    E2=u^19+a u^14+b u^3+c,
    E3=v^19+a v^14+b v^3+c.

No division by u-1, v-1, u-v, b, or c is used. Only the known nonzero first witness is used for scaling, and each known nonzero witness is used to replace f(r)=0 by f(r)/r=0. Proving the **whole** ideal (E1,E2,E3) is the unit ideal is stronger than excluding the desired open subset: it requires no saturation and loses no degenerate solutions.

## Independent modular computation

The producer used Singular. This audit reconstructed a,b,c and E_i directly from binomial coefficients and used **SymPy**, with reversed variable order (v,u), modulus 31, and grevlex. The computed basis was [1]. The executable checker is `sparse-pilot/independent_mod31_audit.py`, and its receipt is `sparse-pilot/independent-mod31-audit.json`.

This second CAS result is corroboration, not a formal proof certificate. The public proof package should retain and independently replay a finite-field ideal-membership identity for 1, so the conclusion does not depend on trusting either Gröbner-basis engine.

## Why the reduction lifts to characteristic zero

Let A=Z_(31), I=(E1,E2,E3) in A[u,v], and M=A[u,v]/I. A unit ideal modulo 31 alone would not suffice: for example 31u-1 has a characteristic-zero root but becomes a unit modulo 31. Here the missing finiteness hypothesis can be proved explicitly.

Subtract E1 from E2. The resulting polynomial depends only on u:

    P(u)=-4844u^19+4845u^16+21147456u^14-21162960u^11+15503.

Its leading coefficient is -4844, which equals 23 modulo 31 and is a unit in A. Dividing by this unit produces a monic degree-19 relation for u in M.

Subtract E1 from E3. The resulting relation is

    Q(u,v)=v^19+a(v^14-1)+b(u)(v^3-1)-1.

This is monic of degree 19 in v over A[u]. Consequently M is generated as an A-module by the 361 monomials u^i v^j with 0<=i,j<19. For example, first reduce v powers using Q and then reduce resulting u coefficients using P. These reductions show finite generation even if the generators satisfy further relations; freeness is not required.

The modular unit-ideal identity gives M/31M=0. Since A is local and M is finitely generated, Nakayama's lemma yields M=0. Tensoring with Q gives Q[u,v]/I_Q=0. Therefore the normalized equations have no solution over any characteristic-zero field extension. In particular the last support is impossible over C.

This reasoning uses the exact integer ideal and the local ring at 31. It is not an unjustified inference from one unsuccessful finite-field root search, and it does not assume that arbitrary characteristic-zero witnesses can be reduced modulo 31.

## Adversarial checks and residual boundaries

- The normalization is valid for every polynomial in the remaining exact support, including repeated witness choices. No distinctness assumption is needed.
- The support count is exhaustive for up to three nonleading terms because the three required sets are disjoint.
- The characteristic-zero published constraints and the prime-31 certificate have separate roles; no theorem about arbitrary characteristic-31 CA polynomials is asserted.
- The finite-module lift is valid because both required leading coefficients are units at 31. This condition must remain in any shortened write-up.
- Sparse polynomials with more than three nonleading terms remain untreated. Centering can increase term count, so the result must not be stated as an unrestricted four-term theorem in arbitrary coordinates.
- Correctness depends on the published CLO results. Their statements and use were checked directly; this audit is not a new proof of those results.
- Historical priority and publication significance require a separate literature assessment. The computation proves a restricted exclusion, not the full conjecture and not full degree 20.

The new sparse result clears the earlier audit campaign's proposed mathematical continuation gate: it is an independently checked positive characteristic-zero statement with exact scope. That supports packaging the result for review, while leaving novelty and publication decisions open.
