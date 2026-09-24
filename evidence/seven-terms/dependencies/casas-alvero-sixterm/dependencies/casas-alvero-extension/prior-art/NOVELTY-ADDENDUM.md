# Six-term candidate and exact formula overlap

23 September 2026, later extension-stage check. Read together with REPORT.md. The parent reports a modulus-13 certificate for the final five-term family; its complete independent verification is handled elsewhere. This note examines prior-art implications, not that certificate's integrity.

## What is already contained in prior methods

The visible-support lemma in `../explanation/EXPLANATION.md` is a direct combination of the binomial-normalized coefficient induction in [CLO, Proposition 15 proof](https://arxiv.org/html/1208.5404) and the elementary one-support characteristic-p calculation. For a reduced polynomial \(x^n+c x^{n-m}\) with \(c\ne0\), a nonzero common root with its Hasse derivative of order \(n-m\) forces \(\binom nm=1\) in the residue field.

That one-support binomial obstruction is explicit in [Marashdeh, Corollary 4.7 and the subsequent discussion](https://arxiv.org/html/2608.14726v1), and the corresponding pure-power resultant coefficient is [Schaub–Spivakovsky, Theorem 6, attributed there to de Frutos Marín](https://arxiv.org/html/2307.05997v2). The particular characteristic-zero support formulation may be convenient, but these sources leave no basis for claiming a new general mechanism merely from repackaging it. Its application with primes 3 or 17 excludes \(\{5,15,16,19\}\) just as it excludes the old four-term family.

## The boundary integer is exactly an existing integer

Use the pilot's notation

\[
B=\binom nr,\quad D=\binom ns,\quad C=\binom{n-r}{s-r},
\quad g=\gcd(r,s),\quad u=(s-r)/g,\quad v=r/g.
\]

The proposed boundary obstruction is

\[
N=B^{s/g}(C-1)^{(s-r)/g}(D-C)^{r/g}
 -(B-1)^{r/g}(D-1)^{s/g}.
\]

Set \(C_1=B,C_2=D,E=C,m_1=r,m_2=s,d=n\) in [Marashdeh, Theorem E / Theorem 6.1](https://arxiv.org/html/2608.14726v1). His integer is

\[
\begin{aligned}
\mathcal N
&=(D-1)^u[(B-1)(D-1)]^v
 -[B(C-1)]^u[B(D-C)]^v\\
&=(B-1)^v(D-1)^{u+v}
 -B^{u+v}(C-1)^u(D-C)^v\\
&=-N.
\end{aligned}
\]

This is an exact symbolic identity, not merely a numerical resemblance. Theorem 5.9 there gives its nonvanishing; Theorem 6.1 uses its prime divisors subject to denominator conditions. Consequently the formula, its nonvanishing, and the corresponding two-support bad-prime arithmetic are prior art. Identifying this integer as the boundary condition of a larger support calculation could be a useful application, but is not a new integer obstruction. The quoted paper is a preprint; one can independently reprove the needed finite case without depending on its general inequality theorem, while still acknowledging priority.

## The final family is not covered by the checked prior exclusions

For \(S_A=\{4,10,17,19\}\), the centered active derivative orders are \(\{16,10,3,1\}\). The chosen matching scenario is

\[
(0,1,2,1,1,1,1,1,1,3,1,1,1,1,1,4,1,1,1).
\]

It can require five recycled roots, so the statement of Massri's three-recycled-root theorem does not apply. The equal-placement tests from Remark 7.4 and the determinant obstruction both pass. Its Goncharoff binary mask has \(v_{19}G(1)=2\), so the valuation-one exclusion also does not apply. The source's list of 3125 masks is a list of remaining possibilities; it is not a certificate that those possibilities were all eliminated.

Marashdeh's all-characteristic two-support theorem does not directly exclude this four-element characteristic-zero support, nor the three-element support \(\{4,17,19\}\) that can remain after reduction modulo 11 or 13. His reported support computations cover small degrees, not an enumerated degree-20 exclusion. The paper's general triangular reduction would generate such a calculation, but a general algorithm is not a record that every generated instance has previously been solved.

The prime-13 reduction is useful precisely because

\[
\binom{20}{4}\equiv9,\quad\binom{20}{10}\equiv0,
\quad\binom{20}{17}\equiv9,\quad\binom{20}{19}\equiv7\pmod{13}.
\]

Neither a singleton obstruction nor the two-support formula alone settles the possible three-element residue support. The parent's modulus-13 unit certificate addresses that remaining content.

## Optional direct valuation transfer, including the smaller residue chart

There is an alternative to proving finiteness of the normalized characteristic-zero algebra, if the certificate is stated as an exclusion of all necessary residue cases. Normalize valuation as in REPORT.md; reduction of the last family has the form

\[
h=x^{20}+A x^{16}+C x^3+D x
\]

and retains a nonzero root. A nontrivial CA reduction also satisfies all Hasse common-root conditions, even if coefficients vanish.

If \(A=0\), its proper residue cases can be checked without a general sparse theorem:

- A singleton nonleading support at 17 or 19 is impossible because the corresponding binomial residues 9 and 7 are not 1. Empty support is impossible because a nonzero residue root remains.
- If \(C,D\ne0\), choose a common root with \(H_3(h)\); it is nonzero. Scale it to one. Then \(C=-\binom{20}{3}=4\) and \(D=-1-C=8\). At a common root \(v\ne0\) with \(H_1(h)\), subtracting seven times \(h(v)/v=0\) from \(H_1(h)(v)=0\) gives \(v^2=10\). Consequently \(v^{19}=-v\), and \(h(v)/v=0\) forces \(v=9\). But \(9^2=3\ne10\) in characteristic 13. This is a contradiction over the algebraic closure, not just at rational finite-field points.

If \(A\ne0\), normalize a common root with \(H_{16}(h)\) to one. It is nonzero, and \(A=4\). The three equations in `../root-mod13/test.sing` then apply, with the following degeneration checks required when using equations divided by a root:

- If \(C\ne0\), an \(H_3\) witness is nonzero. If \(C=0\), then \(D=8\) from \(h(1)=0\), and \(H_3(h)(1)=9+4=0\); choose the nonzero witness 1.
- If \(D\ne0\), an \(H_1\) witness is nonzero. If \(D=0\), the divided polynomial \(h(x)/x\) also vanishes at zero, so a zero witness satisfies that equation too.

Thus, after a successful independent check of the parent certificate, the standard valuation argument can transfer its contradiction directly. This is a proof simplification, not a new specialization principle. The parent may retain the already checked finite-module bridge instead.

## Updated novelty assessment

The five-term lower bound is a prior-argument consequence, and the proposed general boundary integer is exactly prior art. A certified exclusion of \(S_A\), combined with the existing reductions, would give the stronger bound of **at least six centered nonzero terms** in degree 20. This bounded search found no explicit theorem or checked implicit argument already giving that conclusion.

That is the defensible candidate contribution: a specific further sparse-degree-20 exclusion, with a reproducible arithmetic proof. It is not a full degree-20 result, a general sparse classification, or a novel modular method. Its significance is limited by the amount of known reduction and the size of the last calculation; journal-level importance is not established by the fact that the ambient conjecture is famous.

Additional searches used the exact two remaining support strings, their polynomial exponent patterns, `pentanomial`, `five-term`, `six-term`, the bad-prime integer aliases, and sources cited for the singleton obstruction. De Frutos Marín's repository PDF was located by search but its full text could not be retrieved by the web tool, so that thesis is an explicit remaining coverage gap. No author contact or publishing action occurred.
