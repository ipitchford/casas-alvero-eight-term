# Dependency and characteristic-zero repairability audit

Audit date: 23 September 2026. This is a bounded internal mathematical audit, not a complete review or a resolution of Casas–Alvero. The finite-field counterexamples are being independently checked by another agent; this report does not claim to have reproduced them.

## Source pinning and dependency map

Primary sources read: [Ghosh, arXiv:2501.09272v2](https://arxiv.org/html/2501.09272v2), especially Proposition 3.3, Corollary 3.9, Proposition 4.3, Lemma 4.5 and Sections 4.2.2–4.2.3; [the prequel, arXiv:2402.18717v3](https://arxiv.org/html/2402.18717v3), for the stated finiteness/height input. The prequel's proof has not been independently audited here.

The dependency is:

```
prequel: height(I_m) >= m-1
Theorem 3.6: global mu(I_m) = m (characteristic zero)
              + Proposition 3.3: local/global equality
                      ↓
Corollary 3.9: mu((I_m)_p) = m at every minimal prime
                      ↓
Lemma 4.5, contradiction after (4.24)
                      ↓
Proposition 4.3: injectivity on filtered H_0
                      ↓
Section 4.2.2: vanishing of H_1 in the lower-degree complex
                      ↓
CA in degree n+1 => CA in degree n
                      ↓
known unbounded good degrees => Theorem A
```

The characteristic exclusion in Proposition 3.3 is that the field characteristic does not divide the product of the binomial coefficients binom(n,i-1), i=1,...,n. Its genuinely difficult case is a height n-1 minimal prime with global generator number n. The height n case follows immediately from the height bound. Corollary 3.9 combines the proposition with the separate global-generator result.

## Correct saturation statement for the cancellation step

The following is an original elementary reformulation of what cancellation requires; it is not a theorem established for the paper's ideals.

Let B=k[t,y_1,...,y_s], m=(y_1,...,y_s), H_i in B, J=(H_i), and N=mJ. Let H_i^0 denote H_i specialized at t=0. Assume the classes of H_i^0 in J_0/mJ_0 are linearly independent over k. If

    (N:t)=N,

then the classes of H_i in (J/mJ) tensor_{k[t]} k(t) are linearly independent over k(t).

Proof: clear denominators in a proposed relation, giving sum c_i(t)H_i in N. Specializing at t=0 gives c_i(0)=0 for every i. Write c_i=t d_i. The displayed saturation condition gives sum d_i H_i in N. Repeat. A nonzero finite tuple of polynomials cannot remain divisible by arbitrarily high powers of t. This proves independence. Equivalently, multiplication by t must be injective on B/N, or N must equal N:t^infinity.

The nonvanishing of B/N after inverting t says only that the localization did not kill the whole module. It does not establish this saturation. For example k[t,y]/(ty) has nonzero localization k[t,t^-1] and nonzero t-torsion, represented by y.

Care is needed about the polynomial model: J must be generated over k[t,y], not ambiguously treated as an ideal already over k(t)[y]. Also, proving saturation for mJ does not prove saturation for m(J+(y_r)), nor does independence modulo mJ automatically imply independence after adjoining y_r. These must be checked in whatever repaired proof is offered. The finite-field torsion witness reported by the counterexample agent addresses the literal plus-ideal too, but is not proved again here.

## What local generator equality does and does not say

CA in degree m+1 immediately implies the characteristic-zero local assertion for I_m: the only minimal prime is the irrelevant maximal ideal, its height is m, and the m displayed generators are minimal by the height theorem.

The converse is not a general commutative-algebra fact. An ideal of height m-1 can need m generators even at its minimal primes. For example (u^2,uv,v^2) in k[u,v,w] has height two and needs three generators both globally and at its unique minimal prime (u,v). Thus the proposed equality does not itself exclude a nontrivial projective solution. It says such a solution would have to be locally an almost complete intersection, rather than a complete intersection.

A characteristic-zero proof of the requested equality would therefore be useful but would not be a short stand-alone proof of CA. It would feed a descent argument that also needs the next repair. No equivalence between this local assertion alone and CA has been proved in this audit.

## A second invalid inference, already over characteristic zero

At Lemma 4.5, equations (4.22)–(4.23), the proof works modulo a determinantal ideal in a zero-dimensional local ring A. It attempts to infer that the coefficient f of x in a unit polynomial f x+g vanishes in A. This inference is false: positive-degree coefficients of a polynomial unit must be nilpotent, not necessarily zero.

An exact characteristic-zero witness is

    A = Q[e]/(e^2),       (1-e x)(1+e x) = 1,

with e nonzero in A. For the coefficient induction in the proof, c_1=-e belongs to the maximal ideal but c_0=1 does not. The equation c_0 e+c_1=0 is precisely why the next induction step fails. The conclusion c_m in the maximal ideal may be valid; its repetition for c_{m-1} is not.

This is a counterexample to the supporting inference, not a counterexample to Lemma 4.5 for the special CA polynomials. It prevents us from saying that a repair of Proposition 3.3 alone repairs the full proof. The issue is nilpotent structure, not positive characteristic.

### Pressure test retaining surrounding algebraic properties

Here is a stronger abstract model over Q showing why the surrounding regular-sequence and generator hypotheses do not automatically fix the problem. This construction is not a CA configuration and has a different degree pattern.

Set R=Q[u,v,w], S=R[z], and

    f=(uv,u^2,v^2),             g=(w^3,u^3,v^3),
    F=(uvz+w^3, u^2(z+u), v^2(z+v)).

Let D be the ideal of 2x2 minors of the matrix with rows f,g. Direct expansion gives

    D=(u^2(u^2v-w^3), v^2(uv^2-w^3), u^2v^2(v-u)).

At p=(u,v), w and the two factors u^2v-w^3, uv^2-w^3 are units. Consequently

    D_p=(u^2,v^2),
    A=R_p/D_p=Q(w)[u,v]_(u,v)/(u^2,v^2).

This is an Artinian local complete-intersection ring. The element uv is nonzero and square-zero in A. Moreover

    (w^-3-uv w^-6 z)(w^3+uvz)=1 in A[z].

Thus F_1 is a polynomial unit although its z coefficient is nonzero. All f_i lie in p, while mu((f)_p)=3: u^2,uv,v^2 are independent in the degree-two part of the maximal ideal filtration. Also D_p needs only two generators. In particular, equality (f)_p=D_p is false, exactly as the invalid polynomial-unit inference would overlook.

The F_i themselves form a regular sequence in S. To check height three, split the equations F_2=F_3=0 into the four choices

    u=v=0;
    u=0, z=-v;
    v=0, z=-u;
    z=-u=-v.

In the first three cases F_1 forces w=0, leaving a line. In the fourth it forces w^3=u^3, again giving dimension-one components. Hence S/(F) has dimension one, the ideal has height three, and the three generators form a regular sequence in the polynomial Cohen–Macaulay ring. Adjoining the linear equation z yields the ideal (z,w^3,u^3,v^3), of height four.

There is no common irreducible factor of the three displayed minors: any such factor would divide u, v or v-u, and direct substitution excludes each. Thus D has height two (the determinantal upper bound supplies the reverse inequality), and the expected-height determinantal Cohen–Macaulay property is available as well.

Finally D is contained in (F), while F_1 becomes a unit modulo D_p. Therefore (F)S_p=S_p, so the contraction (F) cap R localized at p is R_p, whereas D_p is proper. This explicitly defeats the proposed contraction equality in this abstract model despite the surrounding algebraic properties. The special CA form must supply an additional argument that the paper has not supplied at the cited step.

## Possible correct replacements and decision

1. **Cancellation:** prove the precise colon-ideal identity for the appropriate polynomial model, and separately justify the added-variable conormal step. Merely restricting the statement to characteristic zero supplies no such proof.
2. **Lemma 4.5:** a sufficient extra hypothesis would be that the relevant Artinian local determinantal quotient is reduced. Then it is a field and polynomial units have zero positive-degree coefficients. Cohen–Macaulayness and being a complete intersection do not imply reducedness; the example above already has both locally. A special argument controlling these nilpotents is required instead if reducedness is unavailable.
3. **A narrower descent target:** directly prove the contraction identity (F_1,...,F_{n-1}) cap R_{n-1}=I_2([f;g]) for the special CA family, with all necessary hypotheses. That would bypass both local-generator and polynomial-unit inferences. This is a substantial elimination/saturation theorem, not a routine repair.

Small characteristic-zero cases where CA is already known do not exercise the disputed nontrivial branch: there are no height m-1 minimal primes of I_m in those cases. Passing small checks is therefore weak evidence about the missing argument in an unresolved degree.

Recommendation: **GO for the bounded audit note and exact replay; NO-GO for an open-ended full-conjecture campaign justified solely by this proposed proof.** Continue toward a positive result only if an independently proved characteristic-zero statement controls the relevant torsion or determinantal nilpotents. The audit has located an additional concrete proof defect, but has not produced a positive characteristic-zero advance toward CA or a counterexample to CA.
