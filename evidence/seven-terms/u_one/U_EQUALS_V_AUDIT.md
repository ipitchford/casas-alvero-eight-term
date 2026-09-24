# Independent audit of the two u=v exclusions

23 September 2026. Internal mathematical and exact-arithmetic audit. Producer files were not edited.

**Verdict: PASS.** I read `../u_equals_v/JET_PROOF.md` in full and independently reconstructed its divided equations as integer polynomials. Both branch exclusions are valid under the previously audited normalization and residue classification. In particular, the second precision step in the wbar=1 branch is justified in arbitrary ramified valued extensions; it does not infer divisibility by13 merely from equality of residues.

This audit concerns the compact jet proof. I did not use or independently audit the separate large-resultant proof. Nor does this file on its own audit the other C branches or establish historical novelty.

## 1. Exact setup and first precision improvement

The simple residue root2 forces u=v by counting integral roots in its residue cluster. The H15 equation gives exactly

    B(u)=-15504u^5+77520u,
    E=-1-A-B-C-D,    A=-4845.

The C coefficient lies in13O because its binomial-normalized coefficient is integral. This is actual divisibility by13, not just a positive valuation statement.

After composing B(u), the Jacobian of the two exact equations f(u),H3f(u) with respect to u,D, at u=2,D=3,C=0, is

    [[10,6],[4,1]] modulo13,

with determinant12. The composition matters: the u-derivative of f includes B'(u)*(u^15-u). The producer includes this term correctly. Both constants lie in13Z. The minimum-valuation lemma therefore forces u-2,D-3 into13O even when the value group is not discrete. Hence the variables r,l,k defined by u=2+13r,D=3+13l,C=13k are integral.

This also gives f-h0 in13O[X], where h0=X20+4X16+6X15+3X3+12X. That stronger congruence is subsequently used correctly.

## 2. Independent full-polynomial reconstruction

The audit checker `check_u_equals_v_audit.py` imports no producer arithmetic, jet table, or certificate. It constructs B,E,f,H3,H1 as sparse integer polynomials, substitutes u=2+13r,D=3+13l,C=13k, and verifies coefficient by coefficient that division by13 is exact for

    f(u), H3f(u), H1f(1), f(4).

It then confirms that every nonlinear coefficient of each divided polynomial is a multiple of13. Their reduced affine rows, with variables r,l,k, are

    7 +10r+6l+8k,
    6 +4r+l+7k,
    4 +11r+2l+9k,
    3 +10r+8l+5k.

This verifies the complete polynomial reduction, rather than just evaluating a few chosen inputs or checking formal derivatives.

## 3. The wbar=4 branch

The residue root4 is triple for h0. Because f-h0 lies in13O[X], the constant and linear terms in the Taylor expansion of f'(4+delta) have valuations at least1. Its quadratic coefficient is3*H3h0(4)=2, a unit. Thus a common first-derivative root w satisfies2*val(w-4)>=1, unless w=4 exactly.

The Taylor expansion of f(4+delta) then has all nonconstant terms of valuation greater than1. This conclusion holds in an arbitrary ordered value group: from2t>=1 and t>0, one obtains3t>=1+t>1. No half-integer discretization is assumed.

The first, second, and fourth affine equations have determinant5 and unique solution(r,l,k)=(5,7,12) in every residue-field extension. The normalized middle derivative has reduction X10+11X6+7X5+4, whose gcd with h0 is1. This excludes the branch.

## 4. The wbar=1 branch and the essential second precision step

The residue root1 is double. Since f already has an exact root at1 and w is a repeated root, cluster counting forces w=1. Thus the first three divided equations vanish exactly.

Their reduced linear matrix has determinant3 and unique solution(r,l,k)=(12,3,3). This initially supplies only equality of residues. The proof correctly makes a second argument before treating these differences as divisible by13.

The three divided equations are integral polynomials. Their values at the integer point(12,3,3) are in13Z, and their Jacobian there is a unit matrix modulo13. Therefore the same minimum-valuation lemma gives

    r-12, l-3, k-3 in13O.

The full-polynomial reconstruction gives an additional direct way to see this step: each divided equation equals an affine map with a unit linear matrix plus13 times an integral polynomial. The affine map at(12,3,3) is divisible by13. Evaluating at the integral triple(r,l,k) and inverting that matrix yields the asserted divisibility. Thus this step does not rely on Hensel uniqueness, unramified coefficients, or a formal power-series convergence claim.

## 5. Precision of the order-10 common root and the final contradiction

Let G=H10f/184756. Its denominator after cancellation of13 is14212, a13-adic unit. The audit independently checks the exact coefficient identity

    H10f(4)/13 = k-3 modulo13Z[r,l,k].

Since k-3 is now known to lie in13O, G(4) lies in13O. The reduced G is

    G1=X10+11X6+7X5+1,

with gcd(h0,G1)=X-4 and G1'(4)=3. Every order-10 common root z therefore reduces to4, and the one-variable precision lemma forces z-4 into13O. This stronger conclusion would not have followed merely from the first residue solution; the second precision step supplies the missing coefficient control.

Since f'(4) lies in13O and z-4 lies in13O, Taylor expansion gives

    f(z)-f(4) in13^2 O.

But f(z)=0, whereas the independently reconstructed fourth divided polynomial evaluates to

    f(4)/13 = 3+10*12+8*3+5*3 = 6 modulo the maximal ideal.

This contradicts f(4) in13^2 O. The argument is valid for any ordered value group used in the prior normalization.

## 6. Reproduction and assurance limits

The independent checker and its normal/optimized receipts are:

- `check_u_equals_v_audit.py`
- `u-equals-v-audit-verification.json`
- `u-equals-v-audit-verification-optimized.json`

Both runs pass. The checks independently verify the exact integer divisions, all four affine reductions, both Jacobian determinants, both candidate triples, all nonlinear divided coefficients being in13Z, the middle-derivative root gcds and derivative, and the final nonzero residue6.

The finite identities support the written valuation argument; they are not a formal proof-assistant certification. The prior residue-classification and normalization hypotheses remain explicit dependencies. Subject to those already audited dependencies, no gap was found in either assigned u=v exclusion.
