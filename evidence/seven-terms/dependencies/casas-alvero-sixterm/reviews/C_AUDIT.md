# Independent audit of C's residue classification and cluster constraints

23 September 2026. Internal mathematical and exact-arithmetic audit. No new exclusion was attempted; producer files were not edited.

**Verdict: the normalized characteristic-13 coefficient classification is proved, and the stated valuation restrictions and forced root equalities are valid necessary conditions for a full-support characteristic-zero lift. They do not exclude C.** With the separately established A and B exclusions, the useful frontier is the single exact deficiency support \(\{4,5,10,17,19\}\). A seven-term lower bound remains unproved.

The normalized residue seed is

\[
h=X^{20}+4X^{16}+bX^{15}+cX^3+dX,\qquad h(1)=0.
\]

Its complete CA coefficient list over \(\overline{\mathbf F}_{13}\) is

\[
(b,c,d)=(6,3,12),\ (6,2,0),\ (6,10,5).
\]

This is a classification of residue polynomials after the given normalization. It is not a classification of characteristic-zero polynomials or a claim that any residue point lifts.

## 1. Scope and exact dependency

I reviewed `C/UNIVARIATE_CLASSIFICATION.md`, `C/ROOT_CLUSTER_NOTE.md`, the replay and saved univariate certificate. I also read the actual earlier proof at

`work/casas-alvero-extension/explanation/MOD13_EXPLANATION.md`

and ran its `check_mod13_explanation.py`, which passed. Its complete characteristic-13 lemma excludes \(X^{20}+aX^{16}+cX^3+dX\) except the monomial, including coefficient-zero charts. This supplies the present \(b=0\) exclusion when \(a=4\).

In the frozen extension package, that argument is incorporated into `outputs/casas-alvero-extension/PROOF.md`, with checker `outputs/casas-alvero-extension/check_mod13_explanation.py`. The integrated package's dependency map should identify this flattening; the old work-tree relative filename is not the frozen file layout. This is a packaging issue, not a mathematical gap.

## 2. Exhaustiveness of the univariate split

The Hasse equations independently give

\[
H_{15}h=8X^5+12X+b,\quad H_3h=9X^{17}+4X^{13}+c,
\]
\[
H_1h=7X^{19}+12X^{15}+2bX^{14}+3cX^2+d.
\]

The \(X^{12}\) contribution from \(bX^{15}\) to \(H_3h\) vanishes because \(13\mid\binom{15}{3}\).

Since \(b=0\) is excluded by the dependency, an \(H_{15}\) common root \(u\) is nonzero. The normalization gives \(b+c+d=8\), so \(h(-1)=5-(b+c+d)=10\ne0\). Thus \(u=-1\) is impossible. The separate \(u=1\) chart is essential and correctly retained.

For \(u\ne0,1,-1\), substitution gives

\[
b=5u^5+u,\qquad c(u^2-1)=N:=5+b-6u^{19}-5u^{15}.
\]

Since \(N(1)=0\), \(C=N/(u-1)\) is a polynomial. With \(q=u+1\) and \(D=q(8-b)-C\), the actual coefficients are \(c=C/q,d=D/q\). Both denominator exclusions are justified on this chart.

The saved polynomials \(P,J_3,J_1\) equal \(qh/X,qH_3h,qH_1h\). If the order-3 witness is nonzero, its resultant vanishes; if that witness is zero, then \(C=0\). This proves \(CR_3=0\) in either case. The identical dichotomy proves \(DR_1=0\), including \(d=0\). No zero-witness branch is discarded.

The verified identity

\[
UCR_3+VDR_1=(u+1)^{17}(u-1)(u-2)(u^2+4u-2)
\]

therefore confines the generic chart to \(u=2\) or \(u^2+4u-2=0\). The checked remainders give coefficient points \((6,3,12)\) and \((6,2,0)\), respectively. The quadratic does not vanish at \(-1\), so its rational coefficient formulas are defined.

At \(u=1\), the equations give \(b=6,d=2-c\). The second verified identity has right side \((c-2)(c-3)(c-10)\), yielding precisely the stated three coefficient candidates. Direct Hasse gcds show that all three are actual residue CA polynomials. Thus the classification is exhaustive and includes coefficient degenerations; it does not rely on absence from a prime-field point search.

## 3. Certificate replay and independence

The generic polynomial coefficients have parameter-degree at most 18, while their \(X\)-degrees are 19,17,19. The Sylvester bounds are consequently 648 and 684. Exact agreement at 685 distinct points of \(\mathbf F_{13^3}\), with \(q=0\) omitted and all specialized leading coefficients checked nonzero, certifies the supplied resultant polynomials.

The special chart has parameter-degree bound one and resultant-degree bounds 36 and 38. Its 39 exact evaluations suffice. The field cubic \(t^3-t-1\) has no prime-field root and is irreducible. The field/resultant helpers are explicitly shared with B's previously audited standard-library checker. This is independence from the Singular producer, not a second independent implementation of those helpers.

Both normal and optimized C replay passed. Both Bezout identities and all stated coefficient remainders passed. I additionally used a separate prime-field Sylvester determinant implementation, importing no producer arithmetic, to verify 50 resultant evaluations across the two charts. These supplementary evaluations agree; they support the independent audit but do not replace the complete interpolation proof.

The old Gröbner output's quotient length 17 remains a CAS-reported scheme-theoretic diagnostic. The present classification proves the coefficient points and their geometric witness choices; it does not independently certify that nonreduced quotient length. No part of the argument below needs it.

## 4. All marked witness choices, including the quadratic branch

An independent standard-library Euclidean gcd calculation reconstructed every active Hasse gcd and checked the CA condition at all 19 orders. The results are:

| \((c,d)\) | \(\gcd(h,H_{16}h)\) | \(\gcd(h,H_{15}h)\) | \(\gcd(h,H_3h)\) | \(\gcd(h,H_1h)\) |
|---|---|---|---|---|
| \((2,0)\) | \(X-1\) | \((X-1)(X^2+4X-2)\) | \(X-10\) | \(X^2\) |
| \((3,12)\) | \(X-1\) | \((X-1)^2(X-2)\) | \(X-2\) | \((X-1)(X-4)^2\) |
| \((10,5)\) | \(X-1\) | \(X-1\) | \(X-11\) | \((X-3)(X-11)\) |

These are full polynomial gcds, so they control common roots over the algebraic closure, not only over \(\mathbf F_{13}\). The quadratic has discriminant 11, a nonsquare in \(\mathbf F_{13}\); its two distinct roots lie in the quadratic extension. Hence the complete marked assignments \((u,v,w)\), after fixing the \(H_{16}\) root to 1, are:

- \((c,d)=(2,0)\): \(u\in\{1,\rho_+,\rho_-\},v=10,w=0\), with \(\rho_\pm^2+4\rho_\pm-2=0\).
- \((c,d)=(3,12)\): \(u\in\{1,2\},v=2,w\in\{1,4\}\).
- \((c,d)=(10,5)\): \(u=1,v=11,w\in\{3,11\}\).

There are nine distinct geometric marked assignments before applying the characteristic-zero restriction. The last two lines supply the six assignments retained in the note. Counting only the prime-field choices would miss two assignments in the first line.

## 5. Why the characteristic-zero A coefficient is a unit

Use the note's notation

\[
f=X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\]

with all displayed coefficients nonzero in characteristic zero. Standard valuation normalization makes all roots and binomial-normalized coefficients integral and retains a root at 1. The invisible middle coefficient satisfies \(v(C)>0\).

A nonmonomial residue seed with \(a=d=0\) is impossible. If \(b=0,c\ne0\), an \(H_3\) witness scaled to 1 requires \(c=4\), whereas the root equation requires \(c=-1\). If \(b\ne0\), scaling an \(H_{15}\) witness gives \(b=5,c=7\); its \(H_3\) witness must satisfy \(v^{17}=5,v^5=-1\), hence \(v^2=8\) and then \(v=1\), a contradiction. The all-zero case is ruled out by the retained nonzero residue root.

Thus if \(a=0\), necessarily \(d\ne0\). Any characteristic-zero \(H_{16}\) witness then reduces to zero, since \(\overline{H_{16}f}=9X^4\). It is not exactly zero because \(A\ne0\). In \(f(r)/r\), the constant term \(E\) would be a unit and every other term would have positive valuation, impossible. Therefore \(A\) is a unit.

The \(H_{16}\) witness is consequently a unit, and a unit scaling makes it exactly 1, with \(A=-\binom{20}{16}=-4845\). The normalized residue is one of the three classified seeds. This argument depends on the exact full-support assumption \(A\ne0\); it is not a blanket assertion about arbitrary positive-characteristic seeds.

## 6. Why the d=0 residue point cannot lift with full support

At \((a,b,c,d)=(4,6,2,0)\), the gcd \(\gcd(h,h')=X^2\) forces every characteristic-zero first-derivative witness \(w\) to reduce to zero. It cannot equal zero because \(E\ne0\). Subtracting \(f(w)/w\) from \(f'(w)\) gives

\[
19w^{19}+15Aw^{15}+14Bw^{14}+9Cw^9+2Dw^2=0.
\]

Here \(D\) is a unit and \(v(w)>0\). All terms other than \(2Dw^2\) have strictly larger valuation. A sum with a unique term of least valuation cannot vanish. The reasoning is valid in arbitrary ramified valued extensions and excludes all three marked assignments of this residue point, including its quadratic \(u\) choices.

## 7. Cluster multiplicities and the remaining necessary equalities

Since the monic polynomial splits into integral roots, reduction of its factorization shows that residue multiplicity equals the number of exact roots in that residue cluster, counted with multiplicity. A simple residue root therefore admits only one exact root. A repeated exact root consumes at least two positions in its cluster. This direct counting argument does not assume unramified lifting or a chosen Henselian model.

The independently computed multiplicities are: for \((c,d)=(3,12)\), roots 1 and 4 have multiplicities two and three, while 2 is simple; for \((10,5)\), root 1 is simple and 3 and 11 are double. They justify exactly the note's six-row table:

| \((\bar v,\bar u,\bar w)\) | Forced exact relations |
|---|---|
| \((2,1,1)\) | \(u=w=1\) |
| \((2,1,4)\) | None from cluster counts alone |
| \((2,2,1)\) | \(u=v,\ w=1\) |
| \((2,2,4)\) | \(u=v\) |
| \((11,1,3)\) | \(u=1\) |
| \((11,1,11)\) | \(u=1,\ v=w\) |

In the last two rows, the exact \(H_{15}\) condition at 1 gives \(B=62016\). All listed equalities are necessary; none alone proves existence or contradiction. The four grouped branch classes are a convenient coarsening of this table, not a certified decomposition into irreducible components.

Resolved wording point: the original \((2,1,4)\) discussion could suggest that this branch requires ramification. Distinct roots can share a residue already over an unramified field. The parent updated the note to call this the unresolved cluster branch and explicitly preserve arbitrary ramified extensions without claiming they are necessary. I read the corrected passage; it now states the warranted scope.

The divided middle-derivative observation also checks: normalized coefficients \(a_4=12,a_5=4\) yield \(G_{10}=X^{10}+11X^6+7X^5+a_{10}\), and \(a_{10}=7\) makes \(G_{10}(1)=0\). This supplies compatibility of one reduced equation, not an exact lift or a simultaneous solution to all higher valuation equations.

## 8. Reproduction and remaining obligations

- `python3 C/verify_univariate.py` and `python3 -O C/verify_univariate.py`: PASS.
- `reviews/c_independent_patterns.py`: independent full Hasse gcds, nine marked assignments, relevant multiplicities, PASS.
- `reviews/c_resultant_spotcheck.py`: 50 direct prime-field Sylvester determinant evaluations, PASS.
- Real work-tree \(b=0\) dependency checker: PASS.
- Certificate SHA-256: `c8a9258481d6c007041453acdc23bff2b643b767896e6a5f5d3bb7a8ee346273`.
- Shared B helper SHA-256: `76de89d46c42577b0d8f9129ef0f25a77cd4fed34c595bf48a0f0594a6b3bfc1`.
- Initially reviewed classification-note SHA-256: `1ae56e9cef4c50181b42e9dc18f9b666856076d7d1d63d5243ad13c3e182e69c`; subsequently read the clarification allowing all algebraically closed characteristic-13 fields.
- Initially reviewed cluster-note SHA-256: `97b707eabf2d4918383b2d4e68e3399b5173308f12e2c222a64d13781ceffb86`; subsequently read the corrected ramification wording described above. These hashes identify initial audited snapshots, not the subsequently edited note bytes.

The missing mathematical step is an exclusion or construction of the remaining characteristic-zero branch systems. Residue classification, unit constraints, forced equalities, or unsuccessful unramified lifting tests do not supply it. Historical novelty, external review, and formal proof verification are separate matters. The established outcome is A and B excluded with C alone remaining among the current exact six-term supports; the seven-term target is still open in this campaign.

## 9. Final integrated scope read

I read the completed `work/casas-alvero-sixterm/PROOF.md` and `README.md` after the wording corrections. They consistently state that A and B are excluded and C is the unique remaining exact centered six-term support. They retain all six C rows, expressly label their equalities as necessary conditions, and do not claim that the collision rows are solved or that only the row without a forced equality remains. They also preserve the unproved seven-term and unrestricted-degree boundaries. This final check concerns integration and scope; it does not substitute for the separately supplied A audit.
