# Casas–Alvero continuation: a broader support obstruction

23 September 2026. The agreed further research round is complete. This is an unpublished, internally audited mathematical result, with exact replay code. No external refereeing, formal proof-assistant verification, or historical-priority claim is implied.

## Outcome

The continuation produced a compact proof of a support obstruction for **every degree \(20\cdot13^e\), \(e\ge0\)**, together with the stronger degree-20 conclusion:

> Every nontrivial Casas–Alvero polynomial of degree 20 has at least **six nonzero terms after centering**, counting the leading term.

The broader theorem says that, at any root of a nontrivial Casas–Alvero polynomial of degree \(20q\), \(q=13^e\), the eleven derivatives of orders

\[
q\cdot\{2,4,5,6,7,13,14,15,17,18,19\}
\]

cannot all vanish. This is a necessary root-sharing restriction, not a solution of the conjecture in those degrees.

For degree 20, it excludes the entire family

\[
X^{20}+aX^{16}+X^8Q(X)+cX^3+dX,\qquad\deg Q\le4,
\]

apart from the trivial monomial. That particular family permits up to nine terms. **The theorem does not exclude every polynomial with nine or fewer terms.** The universal term-count conclusion is six.

Read [PROOF.md](PROOF.md) for the full argument.

## What made the extension work

The arithmetic at 13 forces a reduced polynomial into the form \(X^{20}+aX^{16}+cX^3+dX\). We exclude that entire finite-field family, including every zero-coefficient case. In its main case, two common-root witnesses have a ratio \(t\) satisfying \(t^{19}=4\). A short elimination gives a second polynomial of degree 18. The nineteenth cyclotomic factor is irreducible over \(\mathbb F_{13}\), and one value and one coefficient comparison prove that the two equations cannot share a root.

This replaces a 1,777-term membership certificate with a ten-term elimination polynomial and a sixteen-term remainder. The explicit certificate remains as an independent arithmetic cross-check of the normalized \(a\ne0\) case; the \(a=0\) cases have separate elementary proofs. Valuation normalization and the Hasse–Frobenius identity then transfer the base exclusion to every degree \(20\cdot13^e\). These transfer methods are established; the specific excluded family is the candidate contribution.

For the six-term corollary, elementary support restrictions leave 16 five-term possibilities. CLO's published determinant criterion leaves one; it lies inside the newly excluded family. Thus the argument covers all centered five-term polynomials, including witness collisions and coefficient degenerations handled by the lower-support bound.

## Correction to the earlier assessment

The earlier **five-term lower bound is already implicit in prior work**. Massri's placement restrictions, combined with CLO's determinant theorem, imply it. A still shorter valuation proof also follows from the standard coefficient-induction method. Our old certificate was correct, but it did not establish a new theorem. The initial novelty search missed an implication inside the proof of a multiplicity theorem.

The [correction](CORRECTION.md) supersedes the earlier novelty assessment. The old audit archive is preserved as a historical record. A second exploratory quantity—the proposed general good-prime integer—also coincided up to sign with Marashdeh's existing two-support integer; it is explicitly attributed and not claimed as new.

The extended search found no matching statement or checked implicit exclusion for the characteristic-13 family, the resulting infinite-degree restriction, or the six-term corollary. This remains **bounded uncertainty**, with thesis and unpublished-computation coverage gaps. [Novelty report](NOVELTY_REPORT.md).

## Assessment

This round achieved the intended advance beyond isolated modular calculations: a readable algebraic explanation, an entire forbidden support family, an infinite sequence of degree-specific restrictions, and a complete five-term exclusion in degree 20. It is more substantial than the previous certificate artifact.

It remains a partial constraint on a difficult conjecture. The current evidence supports a specialist-facing short note for review. It does not establish major publication significance, original priority, or tractability of a full proof. An extension to arbitrary degrees or unrestricted coefficient supports has not been obtained. No publication, submission, or author outreach occurred.

## Replay and evidence

From the extracted package, run:

```sh
python3 replay.py
```

Python 3.10 or later is sufficient; the main replay uses only the standard library and no network. It verifies all file hashes and compares normal and optimized runs against the saved receipts for:

- `check_mod13_explanation.py`: the compact remainder, factorization, Frobenius order, denominator and degenerate-case arithmetic;
- `check_support_and_lift.py`: binomial support rows, all 16 determinants using two exact methods, a published indexing fixture, and the first three Lucas/Frobenius examples;
- `supplement/verify_mod13.py`: an independent reconstruction of the normalized equations and the original 1,777-term unit identity, plus the finite-module certificate used in the first proof route.

The general valuation proof, the statement for all exponents \(e\), and the cited CLO theorem are mathematical arguments, not finite-test conclusions. Internal review records are in `reviews/`; source and exploratory-route records are in `prior-art/` and `supplement/`. Some earlier records preserve conditional wording from before the final proof. The integrated statement is [PROOF.md](PROOF.md).

The ZIP is accompanied by a SHA-256 sidecar and a fresh-extraction replay receipt. Successful replay establishes the stated arithmetic and file integrity, not theorem priority or external review.
