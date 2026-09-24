# Independent audit: completed-local finiteness at prime 19

23 September 2026. **PASS for the formulation below.** This is a conceptual audit, with no new enumeration or lift computation. It gives finiteness, not emptiness, an explicit local length, or a computed ramification bound.

The cleanest whole-degree-20 statement uses prime 19. It does not depend on the characteristic-17 seed classification or the row-8 radius bound.

## 1. The normalized incidence algebra

Let

    f(X)=sum_{i=0}^{20} binom(20,i) a_i X^(20-i),
    G_j(X)=sum_{i=0}^j binom(j,i) a_i X^(j-i),
    a0=1, a1=a20=0, w19=1.

Over Z19, let B be the finite-type algebra in a2,...,a19 and w2,...,w18 with relations

    G_j(w_j)=f(w_j)=0,  2<=j<=19.

Here G1 is automatically witnessed at zero. The equation f(1)=0 is included, so a geometric characteristic-zero point cannot be the centered trivial polynomial X^20. A nontrivial degree-20 CA polynomial can be centered and normalized into this chart because its mean is simple and its H1 witness is therefore nonzero. The elementary prime-19 argument already recorded in `../../LIFT_CONSEQUENCES_17.md` proves that simple-mean fact.

## 2. Exactly 2^17 reduced special-fibre points

In characteristic 19,

    fbar=X^20+abar19 X,
    G19bar=X^19+abar19.

Since w19=1, abar19=-1 and fbar=X(X-1)^19. Every marked witness residue is consequently 0 or 1. Given any word (wbar2,...,wbar18) in {0,1}^17, the equations G_j(w_j)=0 determine abar2,...,abar18 successively, with coefficient 1 on each new unknown. These residues lie in F19. The degree-19 equation fixes abar19 independently, and every fbar(wbar_j)=0 then holds. Thus all 2^17 words occur as reduced geometric special-fibre points, all rational over F19.

This is a description of the underlying geometric points, not a claim that the special fibre is reduced. Because B/19B is finite type over a field and has finitely many geometric points, it is a zero-dimensional Noetherian algebra, hence Artinian and finite-dimensional over F19. Nilpotents have finite length and must be retained.

## 3. Why every relevant generic point is integral

This is the indispensable no-escape step. Finite special fibre alone does not imply finite generic fibre for an affine scheme.

Take an algebraic Q19-point of B, so its coefficients and witnesses lie in some finite extension after adjoining its roots. Pick a nonzero root rho of minimum valuation and put g(X)=rho^(-20) f(rho X). All roots of g are integral, and g has the retained unit root 1. Its normalized coefficients b_i=a_i/rho^i are integral by induction in the monic common-root equations G_j: all selected witnesses are roots, hence integral after this scaling.

Reduction gives gbar=X^20+bbar19 X. Since gbar(1)=0, bbar19=-1. The original chosen H1 witness 1 becomes rho^(-1); the reduced degree-19 common-root equation is X^19-1. That witness must be a unit. Therefore nu(rho)=0, and the original f, all its roots, all its normalized coefficients, and all marked witnesses were already integral in the w19=1 normalization.

This proof allows arbitrary finite ramification. No coordinate is assumed integral merely from its being an algebraic number, and no reduction is performed before the integrality induction.

## 4. The completed local algebras are finite, nilpotents included

For each of the 2^17 special-fibre maximal ideals m, form

    R_m = completion of B_m with respect to m B_m.

This is a complete Noetherian local Z19-algebra. Its quotient by 19 is the completion of the Artinian local ring B_m/19B_m, so is Artinian and finite-dimensional over F19. In particular the radical of 19R_m is the maximal ideal n_m. There exists N with n_m^N contained in 19R_m. Hence

    n_m^(Nk) contained in 19^k R_m contained in n_m^k.

The maximal-ideal and 19-adic topologies are equivalent; R_m is therefore separated and complete for the latter topology too.

Lift a finite F19-basis of R_m/19R_m to elements r1,...,rD. For any r in R_m, express it modulo 19 as a linear combination of those lifts, subtract, divide the remainder by 19 in the sense of choosing an element whose multiple is that remainder, and repeat. The successive scalar coefficients converge in Z19, and the remainder lies in 19^k R_m after k steps. Completeness gives r=sum c_i r_i with c_i in Z19. Thus R_m is finite as a Z19-module.

No cancellation of a factor 19 is needed. The proof does not require R_m to be reduced, a domain, flat, or 19-torsion-free. Its generic fibre can be zero, nonreduced, or a nonzero finite algebra.

## 5. Coverage by these completions

An integral algebraic generic point gives a local map B_m -> O_L for its residue point m, where L is a finite complete extension of Q19. Every source maximal-ideal element maps into the maximal ideal of O_L. The local map is continuous for these adic topologies and extends uniquely to R_m -> O_L. Inverting 19 gives a point of the finite Q19-algebra R_m[1/19]. This covers every algebraic geometric generic point, not only points over an unramified field.

If an ambient complete rank-one valued extension is used instead, the same extension argument works: choose finitely many generators of m, whose images have a strictly positive minimum valuation. Images of m^k then tend to zero. Rank greater than one is unnecessary for this proof; the finite-extension formulation already covers all algebraic geometric points needed for the scheme argument.

There are finitely many m, and each finite generic algebra has finitely many geometric points. By the proved coverage, B[1/19] has finitely many geometric points. As it is finite type over Q19, it is zero-dimensional and is itself a finite Q19-algebra. This global generic-fibre conclusion uses the no-escape proof in section 3; it is not inferred from section 2 alone.

The equations are defined over Z. If desired, faithful flat base change from Q to Q19 therefore also proves that the same normalized incidence scheme over Q is finite. This is an algebraic consequence, not a test showing that any of its points is absent. Nontriviality and mean/scale normalization must be retained when comparing it with an unnormalized CA family.

## Scope

The finite collection of completed local algebras covers all normalized degree-20 points, hence also every row-8 coefficient stratum, including the degenerate leading strata. This coverage does not compute any of the algebras or show that a particular local generic fibre is empty.

For the alternative prime-17 construction, a genuinely finite geometric special fibre would give the same completed-local finiteness conclusion by section 4. The complete seed classification and triangular normalized-witness equations can establish that finite special fibre after a unit-witness normalization. The prime-19 argument above is simpler and avoids those extra dependencies.

No explicit module length, list of characteristic-zero points, degree bound, ramification bound, whole-row exclusion, full degree-20 proof, or novelty claim has been established by this audit.
