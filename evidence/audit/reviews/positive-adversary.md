# Adversarial scope and lifting audit: degree-20 four-term exclusion

Date: 23 September 2026.

Disposition: **PASS on the proposed proof architecture and semantic bridge**, subject to retaining the exact certificate and its checker. No fatal mathematical gap was found in the supplied argument. This is an internal reasoning audit, not independent human review or a formal proof. Novelty was not established by this audit.

## Precisely supported statement

Let f be a complex polynomial of degree 20 satisfying the Casas-Alvero common-root conditions and not a twentieth power of a linear polynomial. Translate the unique root of f^(19) to zero and scale its leading coefficient to one. Then the resulting polynomial has at least five nonzero monomials, counting its leading monomial.

Equivalently, there is no nontrivial degree-20 Casas-Alvero polynomial whose centered normal form has at most four nonzero terms.

The word **centered** and the convention **including the leading term** are essential. Sparsity is generally not invariant under arbitrary translation. This is a restricted degree-20 result, not the complete degree-20 conjecture and not the full Casas-Alvero conjecture.

## Checks against primary source

I directly read Theorem 2 and Proposition 15 in Castryck–Laterveer–Ounaies, *Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree 12*, [arXiv:1208.5404](https://arxiv.org/html/1208.5404). The source defines its CA-polynomials to exclude powers of linear polynomials; the proposed theorem preserves this hypothesis.

Write centered monic f as

    f(x)=x^20 + sum_{m in S} a_m x^(20-m),   S subset {2,...,19}.

The missing x^19 term follows from centering. The missing constant term follows from the Casas-Alvero condition for f^(19), whose unique root is zero. Therefore this normal form loses no nontrivial CA candidate before imposing sparsity.

Theorem 2 at p=19 forces f'(0) != 0, so 19 belongs to S. Proposition 15 at p=2, k=2, n=5=2^2+1 forces S to meet {4,16}. At p=5, k=1, n=4, it forces S to meet {5,10,15}. These three index sets are disjoint. Thus any such S has at least three elements. This independently handles every normal form with fewer than four total terms; no supplementary sparsity theorem is needed for that part.

If |S|=3, it must consist of 19, one element of {4,16}, and one element of {5,10,15}. The six options exhaust the sparse case.

## Independent determinant calculation

I reconstructed the matrix in CLO Theorem 2 directly from its displayed formula and evaluated its determinant using modular Gaussian elimination, rather than invoking the existing audit's Schur-complement implementation. For a support S, its zero-index set is

    J={2,...,18} minus S.

This indexing is correct because f^(20-j)(0) is (20-j)! times the coefficient indexed by j. No coefficient of f is being reduced modulo 19; only the integer determinant prescribed by the characteristic-zero theorem is reduced.

The determinant residues are:

| Support S | det Delta mod 19 |
|---|---:|
| {4,5,19} | 15 |
| {4,10,19} | 7 |
| {4,15,19} | 10 |
| {5,16,19} | 0 |
| {10,16,19} | 12 |
| {15,16,19} | 13 |

Thus the sole remaining support is {5,16,19}, corresponding to

    f(x)=x^20+a*x^15+b*x^4+c*x,   abc != 0.

## Normalization and equation semantics

For this family, all derivative orders except 15, 4, and 1 already share the zero root with f. The active Hasse derivatives are

    H15(f)(x)=15504*x^5+a,
    H4(f)(x)=4845*x^16+1365*a*x^11+b,
    H1(f)(x)=20*x^19+15*a*x^14+4*b*x^3+c.

Each corresponding common root is nonzero because its derivative's constant term is respectively a, b, or c. Choose one root r of f and H15(f). Scaling x by r and the polynomial by r^(-20) makes this root 1 and forces a=-15504. The other chosen roots become u and v, which remain nonzero. There is no reason to assume 1,u,v distinct, and the proposed equations make no such assumption.

Eliminating the derivative conditions gives exactly

    a=-15504,
    b=-4845*u^16+21162960*u^11,
    c=-20*v^19-15*a*v^14-4*b*v^3.

Because all three witnesses are nonzero, dividing f(w)=0 by w is valid for w=1,u,v. This yields

    E1=1+a+b+c,
    E2=u^19+a*u^14+b*u^3+c,
    E3=v^19+a*v^14+b*v^3+c.

Every hypothetical sparse counterexample therefore gives a common zero of E1,E2,E3 over C. For exclusion, the reverse direction and a bijection of unmarked polynomials are unnecessary. Proving that the unsaturated ideal is the unit ideal is stronger than proving that it has no solutions with u*v*a*b*c != 0. Consequently no saturation is needed in the final argument.

## The characteristic-zero lifting argument is valid

Let A=Z_(31), the localization of the integers at their prime ideal (31), and let

    B=A[u,v]/(E1,E2,E3).

Subtraction eliminates c. The polynomial Fu=E2-E1 lies in Z[u], has degree 19, and has leading coefficient

    1-4845=-4844 = 23 mod 31.

This coefficient is a unit of A, so Fu can be made monic over A. Thus the image of u is integral over A.

The polynomial Fv=E3-E1 lies in Z[u,v] and is monic of degree 19 in v. Thus the image of v is integral over A[u]. More concretely, reducing powers of v using Fv and then powers of u using Fu shows that B is generated as an A-module by

    {u^i*v^j : 0<=i<19, 0<=j<19}.

There are at most 361 such generators. No assumption that B is a domain, nonzero, torsion-free, flat, or reduced is required.

The supplied exact certificate establishes

    C1*E1+C2*E2+C3*E3=1 in F31[u,v].

Hence B/31B=0. Since A is local, (31) is its maximal ideal, and B is a finite A-module, Nakayama's lemma gives B=0. Tensoring with Q implies

    (E1,E2,E3)=Q[u,v].

The integer equations therefore have no common zero in C. Combined with the necessary normalization map above, this eliminates the remaining support.

This argument supplies the missing justification that an arbitrary modular unit-ideal computation alone would not provide. For example Z[x]/(31*x-1) has zero mod-31 fiber but a nonempty characteristic-zero fiber; it is not finite over Z_(31). The explicit monic relations rule out precisely that escape here.

## Certificate handling

I read and executed `sparse-pilot/verify_mod31.py`. It independently builds the Hasse equations as integer polynomial dictionaries, compares their reductions to the certificate's exported generators, and checks the complete polynomial identity over F31. It additionally checks the exact two integrality hypotheses used above and has a certificate-corruption negative control.

The run returned PASS for certificate SHA-256

    e63069da3f19151f84cd44ec9f5c46e55d6d806e743c0ccbd25827c6214020a0

with certificate coefficient-polynomial term counts 515, 629, and 656; maximum total degree 39; and the u-leading residue 23. I did not rerun the Singular search producing the certificate, since the explicit identity is sufficient and the assignment was to pressure-test the proof bridge.

## Boundaries to preserve

1. The result depends on established characteristic-zero CLO restrictions plus the new final-family exclusion; the old support restrictions should not be presented as newly proved.
2. Prime 31 has been used only to certify emptiness of one normalized support family. This does not assert that 31 is a good prime for all degree-20 CA polynomials.
3. The modular certificate applies to all algebraic-closure points, because it is a unit-ideal identity, not an enumeration of F31-rational points.
4. The proof does not assume rational or algebraic coefficients of a hypothetical complex polynomial. Its normalized witnesses must satisfy an integer unit ideal, which is impossible over any characteristic-zero extension field.
5. No distinctness of the chosen roots is assumed. Cases u=1, v=1, and u=v are covered.
6. The conclusion gives a lower bound on the number of nonzero terms after centering. It does not prove the existence of a counterexample with five or more terms, nor identify the remaining cases as likely to exist.
7. Correctness and novelty are separate. The final-family calculation may be a useful result, but the title and claims should remain provisional until prior work on sparse CA polynomials and four-term normal forms has been searched directly.
