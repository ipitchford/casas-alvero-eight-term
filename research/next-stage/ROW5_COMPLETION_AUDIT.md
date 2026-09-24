# Audit of the row-5 exact-support exclusion

Research argument audit, 24 September 2026. No paper or publication bundle was produced.

**Result: PASS for the stated exact support and normalized row-5 reduction.** The six cases in `ROW5_COMPLETION.md` exhaust the ten markings of the independently reconstructed first-divided sieve. Their contradictions remain valid over arbitrarily ramified extensions of the 17-adic valuation. The numerical identities and four integer Bézout certificates replay successfully. This is an internal mathematical audit with exact arithmetic checks, not an external referee report or a formal proof-assistant verification.

The mathematical conclusion audited here is that a characteristic-zero Casas–Alvero polynomial cannot have exact centered deficiency support

\[
S=\{2,3,4,10,12,19\}
\]

and the normalized reduction \(X^{17}(X-1)^2(X+2)\). The global exclusion of this support additionally uses the existing exhaustive nine-seed classification and the previously checked row-8 exclusion for the same support. Those are explicit inherited dependencies. This audit does not exclude arbitrary-support row 5, establish an eight-term lower bound, or solve degree 20.

## 1. Inputs and exact scope

Write

\[
f=X^{20}-190X^{18}+1140aX^{17}+4845AX^{16}
 +184756bX^{10}+125970cX^8+EX,
\]

where \(E=189-1140a-4845A-184756b-125970c\). The normalized coefficients and all roots are integral, \(f(1)=0\), and \(\nu(17)=1\). Exact support makes \(a,A,b,c,E\) nonzero. In particular the mean root zero is simple, and a common witness for \(G_{10}\) or \(G_{12}\) reducing to zero is a nonzero root.

The first-divided census, audited separately in `ROW5_FIRST_DIVIDED.md`, leaves ten markings. It forces the \(G_4\) witness into the simple residue class \(-2\), whose unique actual root is denoted by \(r\). Thus the witness is exactly \(r\). If the repeated \(H_1\) witness reduces to one, that residue class has total multiplicity two and already contains the actual root one. The repeated witness and every other root in that class must therefore be exactly one. This multiplicity argument, rather than residue equality alone, justifies the exact collisions in cases 1–4.

For the \(G_3\) witness \(r\), the identities are

\[
a=-r^3+3r,\qquad A=3r^4-6r^2.
\]

For the \(G_3\) witness one they are \(a=2\) and \(A=-r^4+6r^2-8r\). These follow directly from the normalized derivative equations.

## 2. Ramification-safe implicit identities

With the \(G_3\) witness \(r\), let \(F(r,b,c)=f(r)\). It has the form

\[
F_0(r)+17bB(r)+17cC(r),\qquad
\overline{F_0}=r(r-1)^2(r+2).
\]

The derivative at \(-2\) is 16 modulo 17. In particular every solution reducing to \(-2\) satisfies \(\nu(r+2)\geq1\): the value at \(-2\) is divisible by 17, whereas the linear Taylor coefficient is a unit. A positive displacement valuation below one would give a unique lowest Taylor term. This works over a ramified field as well as over \(\mathbf Q_{17}\).

There is also an all-orders explanation. Put \(U=17b,V=17c\). Formal implicit solution at the unique \(\mathbf Z_{17}\) root \(r_0\equiv-2\) gives

\[
\Phi(U,V)\in\mathbf Z_{17}[[U,V]],\qquad
R(b,c)=r_0+\sum_{i+j\geq1}17^{i+j}q_{ij}b^ic^j,
\quad q_{ij}\in\mathbf Z_{17}.
\]

This series converges for every integral \(b,c\) in every complete ramified extension and gives the unique root with this reduction. The statement that \(R+2\) is coefficientwise divisible by 17 refers to the expansion in \(b,c\); it need not hold in the expansion in \(U,V\). Substitution into any integral polynomial in \(r,U,V\) makes a coefficient of parameter degree \(d\) divisible by \(17^d\). Thus the higher-order bounds used in the producer note are proved, rather than inferred from finitely many numerical jets.

The finished checker supplies a stronger finite-polynomial alternative. After setting \(r=-2+17t\), it checks coefficientwise integer identities

\[
H+9F-153b=17^2K_H(t,b,c),
\]
\[
E+9F-17(10b+16c)=17^2K_E(t,b,c),
\]

where \(H=f'(1)\), \(K_H,K_E\in\mathbf Z[t,b,c]\), and

\[
K_H(3,0,0)\equiv5,\qquad K_E(3,0,0)\equiv14\pmod {17}.
\]

When \(b,c\) have positive valuation, \(F/17=0\) gives \(\bar t=3\). Hence \(F=H=0\) gives directly

\[
b=-\frac{17}{9}K_H,\qquad
\overline{b/17}=7.
\]

This already proves \(\nu(b)=1\). If \(0<\gamma=\nu(c)<1\), the identity for \(E\) gives \(\nu(E)=1+\gamma\). If \(\gamma\geq1\), it gives

\[
\overline{E/17^2}=16+16\overline{c/17}.
\]

For the exact \(G_{10}\) witness one, substitute

\[
b_*(r)=44-120a(r)-210A(r).
\]

The corresponding exact identities are

\[
H_*+9F_*=17^2K_{H*}(t,c),\qquad
E_*+9F_*-272c=17^2K_{E*}(t,c),
\]

with \(K_{H*}(3,0)\equiv11\), \(K_{E*}(3,0)\equiv15\). Thus \(F_*=0\), \(\nu(c)>0\) imply \(\nu(H_*)=2\) exactly. This proves case 3 without any concern about evaluating a truncated expansion at a fractionally valued parameter.

The finite checker also verifies the baseline roots \(4095\) and \(49\) modulo \(17^3\), all stated constant and linear jets, and the three unit Jacobians. The independent analytic audit agrees with the coefficientwise identities.

## 3. The six contradictions

**Case 1: repeated witness one; both middle witnesses at units.** All required collisions are exact by the preceding multiplicity argument. The four integer identities \(U(r)P(r)+V(r)Q(r)=D\ne0\) cover the two choices each for the \(G_3\) and \(G_{12}\) witnesses. The checker reconstructs the original binomial-coefficient family and then checks every coefficient of these identities. No division by a middle coefficient or deletion of a boundary component is involved. One of the four choices is not needed by the first sieve; checking it does not weaken coverage.

**Case 2: repeated witness one; \(G_{10}\) witness small and \(G_{12}\) witness a unit.** The two divided equations in \((t,b)\) are coefficientwise integral. Their three residue Jacobians have determinants \(16,8,8\), and their residue solutions are \((0,0),(0,0),(8,0)\). A solution of integral equations with unit Jacobian, reducing to an integer approximate solution whose defects lie in \(17\mathcal O\), differs from that approximation by valuation at least one. Indeed if the least coordinate displacement valuation were \(\eta<1\), the invertible linear part would have valuation \(\eta\), the error would have valuation at least one, and the nonlinear part would have valuation at least \(2\eta\). They cannot cancel. Therefore \(b\in17\mathcal O\), without an assumption of unramified coordinates.

The independently checked values \(\overline{E/17}=8,8,15\) give \(\nu(E)=1\). In \(f/X\) the Newton segment from the constant term to its unit \(X^{16}\) coefficient has slope \(-1/16\); all other terms are strictly above it. All sixteen nonzero small roots therefore have valuation \(1/16\). The \(G_{10}\) equation at such a root has unique lowest nonconstant term \(210Aq^6\), so \(\nu(b)=3/8\), a contradiction.

**Case 3: repeated witness one; \(G_{10}\) witness one and \(G_{12}\) witness small.** The exact polynomial identity above gives \(\nu(f'(1))=2\), contradicting the required equality \(f'(1)=0\).

**Case 4: repeated witness one; both middle witnesses small.** The identities imply \(\nu(b)=1\). If \(0<\gamma=\nu(c)<1\), then \(\nu(E)=1+\gamma\). The same Newton segment makes every nonzero small root have valuation \((1+\gamma)/16<1/8\). Its \(G_{10}\) equation would force \(\nu(b)=6(1+\gamma)/16<3/4\), impossible. Thus \(\gamma\geq1\).

The \(G_{10}\) equation now forces its small witness to have valuation \(1/6\). In \(f(q)/q\), the unit \(q^{16}\) term has value \(8/3\); all other nonconstant terms have greater value. Thus \(\nu(E)=8/3\). If \(\gamma>1\), the divided identity instead gives \(\nu(E)=2\), so \(\gamma=1\).

At a small \(G_{12}\) witness with valuation \(\eta\), the only possible lowest nonconstant values are \(8\eta\) and \(1+2\eta\). Matching the constant value one forces \(\eta=1/8\). In \(f(z)/z\) the unit \(z^{16}\) term then has value two, while \(E\) has value \(8/3\) and every other term has larger value than two. This is impossible.

**Case 5: repeated witness small; \(G_{10}\) witness small.** Let \(\delta\) be the least valuation of a nonzero small root. Such a minimum exists: the residue-zero cluster has multiplicity 17 and contains the simple root zero. The derivative equations give

\[
\nu(b)\geq6\delta,\quad \nu(c)\geq8\delta,\quad
\nu(E)\geq\min(17\delta,1+15\delta).
\]

At a root attaining \(\delta\), the unit \(X^{17}\) term has value \(17\delta\); every other term of \(f\) has value at least \(\min(18\delta,1+16\delta)\). Thus \(\delta\geq1\). In particular \(\nu(b)\geq6\), \(\nu(c)\geq8\), and \(\nu(E)\geq16\). The unit implicit derivative and the factors 17 on both parameters show that \(r\) changes from its \(b=c=0\) value by valuation at least seven. The resulting change in \(E\) has valuation above two. But the baseline has \(\overline{E/17^2}=14\ne0\), a contradiction.

**Case 6: repeated witness small; \(G_{10}\) witness reducing to one.** This case does not identify that witness \(x\) with one. The first divided equations give \(\nu(f'(1))>1\), and \(H_2f(1)\) is a unit. If \(0<\nu(x-1)\leq1\), the exact divided-root equation has unique lowest term \(H_2f(1)(x-1)\). Hence either \(x=1\), or \(\nu(x-1)>1\). In both cases

\[
b=b_*(r)+\epsilon,\qquad \nu(\epsilon)>1
\]

(with \(\epsilon=0\) permitted). The first jet \(\overline{b_*(r)/17}=12\) gives \(\nu(b)=1\). The remaining derivative equations imply

\[
\nu(c)\geq\min(8\delta,1+2\delta),\qquad
\nu(E)\geq\min(17\delta,1+15\delta,2+9\delta).
\]

The minimum-root equation forces \(\delta\geq2/7\): below that value its unit \(X^{17}\) term is uniquely smallest. Thus \(\nu(c)\geq11/7\), \(\nu(E)\geq32/7\). Compare with the simple implicit base equation having \(b=b_*(r),c=0\). Its defects caused by \(\epsilon,c\) have valuation greater than two because both enter multiplied by 17. The displacement in \(r\), and then in \(E\), also has valuation greater than two. The baseline \(\overline{E/17^2}=15\ne0\) therefore persists, contradicting the preceding bound.

None of these minimum-term or implicit-root arguments assumes integer-valued root valuations.

## 4. Coverage and reproducible checks

The ten markings distribute among the six cases as follows:

| Case | Number of first-sieve markings |
|---|---:|
| 1 | 3 |
| 2 | 3 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1 |

This is a cover of witness markings, not a count of distinct polynomials. A polynomial admitting several witness selections causes harmless overlap.

The two finished checkers were read and replayed on 24 September 2026, each normally and under `python3 -O`, with working directory `/private/tmp`. All four runs returned PASS. Their parsed outputs agreed exactly with each other and with the saved normal and optimized receipts. Replaying a supplied checker is not a second independent implementation; the independent components here are the first-sieve reconstruction, proof audit, and separate all-orders argument review.

Fingerprints of the reviewed inputs:

| Input | SHA-256 |
|---|---|
| `ROW5_COMPLETION.md` | `03b35ff5e51d9d5c27716d2a5c896ed5e19c8f9cba11ebe52f58594c4567a38d` |
| `ROW5_FIRST_DIVIDED.md` | `4f429fce666152f1d836fdedad40077925af2a0f4201d818147da22afbe646fc` |
| `row5-jets/check_row5_jets.py` | `f71e0c67bb3ca81cbee9ed7ad70da70c9eed126fbb9b75677696c9c66a6664c9` |
| `row5-jets/verification.json` | `8dd7b861b6ed9fb5705f284a10076d3032bb6c76b5cc8624c369fe0e036cdcbb` |
| `row5-unit/EXACT_UNIT_EXCLUSION.md` | `7eae40f86f564092f06bb647a537fe7a051afccae383a1ecf35acf2d54282b4a` |
| `row5-unit/check_row5_unit.py` | `519bf5fb81f4b64890911139457703be52a7f4fd476c28ca207c412a688cd131` |
| `row5-unit/row5-unit-certificates.json` | `c9cac222f898ebf56de2b94e8a0a40a4dfc9fafed937affe85de4f358b8a7102` |

No blocking correction was found. The only clarity refinement is to specify that coefficientwise divisibility of \(R+2\) concerns the original parameter expansion in \(b,c\), or to use the finite integer-polynomial identities displayed above. The global exact-support corollary is justified once combined with the named pre-existing seed classification and row-8 certificate; no stronger support or degree conclusion follows from this audit.

### Final checker addendum, 24 September 2026

The jet checker subsequently added direct checks of \(\overline{H_2f(1)}=3\) and \(\overline{G_{10}'(1)}=1\) at the surviving near-unit residue configuration. Both formulas were inspected and agree with the normalized family. The updated checker was replayed normally and under `-O` from `/private/tmp`; both returned PASS, with parsed output exactly equal to both updated stored receipts. Its final reviewed SHA-256 is `1da001ee2d90d4582dd7702e3c9b713ba318c105cc9994c6e122b212fe4d5db6`; the final normal receipt SHA-256 is `ef380c5bd4bbf41e9a003c85993a6911e0aa42f2e0dc9ff3f0e9ab4d5a3f8901`. The earlier fingerprints above identify the original reviewed state. The producer proof and mathematical conclusion are unchanged.
