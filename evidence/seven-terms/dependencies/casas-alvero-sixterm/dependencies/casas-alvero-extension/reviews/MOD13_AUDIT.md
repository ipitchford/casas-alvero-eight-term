# Independent audit of the final five-term support, modulo 13

Date: 23 September 2026. **PASS.** The ordinary, unsaturated equations for support (4,10,17,19) have no characteristic-zero solution. Together with the exhaustively checked support restrictions, this proves the conditional statement: every nontrivial centered degree-20 CA polynomial has at least six nonzero terms, including the leading term. Historical novelty is not asserted here.

## Exact integer model

Normalize the witness for Hasse derivative order 16 to 1 and call the other witnesses u,v,w. The polynomial is

    f=x^20+a x^16+b x^10+c x^3+d x.

The derivative equations give, over Z[u,v,w],

    a=-4845,
    b=-184756u^10-8008a u^6,
    c=-1140v^17-560a v^13-120b v^7,
    d=-20w^19-16a w^15-10b w^9-3c w^2.

Set P(X)=X^19+aX^15+bX^9+cX^2+d and I=(P(1),P(u),P(v),P(w)). These are ordinary polynomial equations. Every exact-support CA polynomial gives a point on this model; the model may contain more points, which makes proving its unit ideal sufficient. No deleted-divisor assumption is introduced.

## Reduction modulo 13

Both coefficients of b vanish modulo 13. The remaining reduced coefficients are

    a=4,
    c=4v^17-4v^13,
    d=6w^19+w^15+(v^17-v^13)w^2.

Thus the three members E_1=P(1), E_v=P(v), E_w=P(w) of the full four-generator ideal become polynomials in v,w alone:

    E_1=v^17w^2+4v^17-v^13w^2-4v^13+6w^19+w^15+5,
    E_v=5v^19+v^17w^2-v^13w^2+6w^19+w^15,
    E_w=5v^17w^2-5v^13w^2+7w^19+5w^15.

The producer's certificate is a polynomial identity

    C_1 E_1+C_2 E_v+C_3 E_w=1 in F_13[v,w].

The independent standard-library checker `replay_mod13.py` reconstructs these inputs from the integer binomial formulas, parses the exported multipliers, and verifies the identity by exact modular multiplication. It passes with input term counts (7,5,4) and multiplier term counts (481,649,647), totalling 1777 multiplier terms. The certificate SHA-256 is

    23552e44cc926d21e48b0e57e2022d309b91c34df265292a8dc753f61cd000d9.

Separately, SymPy 1.14.0 with variable order (w,v), grevlex, and modulus 13 returns basis [1], agreeing with the producer's Singular computation. Receipts are `mod13-certificate-replay.json` and `independent-mod13.json`. The plain membership identity is the decisive computational evidence; no CAS kernel is needed to replay it.

## Explicit characteristic-zero bridge

Let A=Z_(13) and M=A[u,v,w]/I. In A[u,v], define

    F_u=P(u)-P(1), F_v=P(v)-P(1).

Their degree-19 homogeneous parts reduce modulo 13 to

    H_u=u^19+4u^2v^17,
    H_v=5v^19.

They are coprime in F_13[u,v]: every irreducible factor of H_v is v, but v does not divide H_u. Therefore the degree-37 Macaulay map

    F_13[u,v]_18^2 -> F_13[u,v]_37,
    (q_1,q_2) -> q_1H_u+q_2H_v

is an isomorphism. The map is injective because a syzygy of degree-18 multipliers of two coprime degree-19 forms must be zero; both sides have dimension 38. Its integer coefficient matrix has determinant a unit in A, so its inverse exists over A. This step does not require 13>20. The good-prime closed formula in SPECIALIZATION_LEMMA.md was stated only for primes greater than 20; it is not being applied here.

Every u,v monomial of degree 37 consequently reduces modulo (F_u,F_v) to degree at most 36. Induction proves that A[u,v]/(F_u,F_v) is a finite A-module.

Finally,

    F_w=P(w)-P(1)

is monic of degree 19 in w over A[u,v]: a,b,c are independent of w, and the eliminated d cancels. Hence the quotient by (F_u,F_v,F_w), and its further quotient M, are finite A-modules. One explicit generating bound is 19*binom(38,2)=13357 monomials. No freeness assumption is needed.

The modular identity for 1 belongs to I modulo 13, even though it uses only three generators. Thus M/13M=0. Nakayama's lemma over the local ring A gives M=0. Tensor with Q to obtain Q[u,v,w]/I_Q=0. This rules out all characteristic-zero solutions of the model, including any with coincident witnesses or vanishing coefficients. In particular it rules out the desired exact support.

This proves the bridge without assuming arbitrary complex witnesses can be reduced modulo 13, without a saturation argument, and without treating a single modular failure as sufficient on its own.

## Audit of the global sparse scope

The published/elementary restrictions used are:

- 19 is in the support, because the centered mean root is simple for degree 20=19+1 (CLO Theorem 2).
- The support meets {4,16} (CLO Proposition 15, p=2).
- The support meets {5,10,15} (CLO Proposition 15, p=5).
- The support meets {10,15} and {5,10}, from the degree-20 common-root exclusions for derivative pairs (5,10) and (10,15) appearing in Massri's argument. Their direct 5-adic proofs were independently checked in this audit round.
- The nonlinear support meets {2,9,10,11,18}, from the elementary valuation lemma with p=3, proved in SPECIALIZATION_LEMMA.md.
- CLO's determinant, built from the **zero** indices j in {2,...,18}, vanishes modulo 19.

An independent enumeration of all binom(17,3)=680 supports with four nonleading terms including 19, applying those set intersections and evaluating the determinant by a triangular solve modulo 19, leaves exactly (4,10,17,19). The certificate above excludes it.

The earlier at-most-four-term exclusion is already supplied by prior-art consequences, including the same filters. Thus the new computational ingredient concerns the last five-term support; it must not be presented as a solution of all degree 20, nor should prior-art exclusions be represented as new achievements.

The resulting minimum of six terms is specifically **after centering** and includes the leading term. Translating an arbitrary polynomial can change the number of terms. No assertion about uncentered sparsity, arbitrary degrees, historical priority, or external refereeing follows.
