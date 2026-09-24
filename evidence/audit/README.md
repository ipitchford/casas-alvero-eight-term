# Casas–Alvero: proof audit and a sparse degree-20 result

23 September 2026. Unpublished research package. Exact certificates and internal mathematical audits; no external refereeing or formal proof-assistant verification.

## Result

**Every nontrivial characteristic-zero Casas–Alvero polynomial of degree 20 has at least five nonzero monomials in its monic centered normal form, counting the leading term.**

Here a Casas–Alvero polynomial shares a nonconstant factor with each derivative of orders 1 through 19. Centering means translating the unique root of the nineteenth derivative to zero. “Nontrivial” excludes a constant multiple of a twentieth power of a linear polynomial.

The [complete proof](SPARSE_DEGREE20_PROOF.md) combines published constraints of Castryck–Laterveer–Ounaïes with an exact exclusion of the remaining family

\[
x^{20}+ax^{15}+bx^4+cx,\qquad abc\ne0.
\]

Six possible supports reduce to one by an integer determinant condition. After a marked root is scaled to 1, the last family gives three explicit equations in two variables. A polynomial identity proves that they generate the unit ideal modulo 31. Two integral relations make the quotient finite over \(\mathbb Z_{(31)}\), so Nakayama's lemma transfers the contradiction to characteristic zero. A finite-field contradiction without that finiteness argument would not suffice.

The certificate contains 1,800 terms. Its verifier reconstructs the equations and multiplies out the identity. Singular produced it; a separate SymPy computation corroborated the unit ideal, and separate internal agents checked the mathematical bridge. The proof requires no result from Ghosh's or Marashdeh's unrefereed preprints.

This settles the centered case with at most four terms. **It does not settle degree 20 generally or the Casas–Alvero conjecture.** The bounded literature search found no matching theorem, but priority remains unestablished.

## Audit of the claimed full proof

The [counterexample derivation](COUNTEREXAMPLE_PROOF.md) reconstructs Ghosh's Proposition 3.3 directly from its definitions. For \(n=3\), the tuple \((1,2,3)\) gives, after invertible coordinate changes,

\[
I_5=(\ell,ut,u^3),\qquad I_7=(\ell,u^2,ut^2).
\]

In either characteristic the global minimum number of generators is 3, while localization at the unique minimal prime \((\ell,u)\) needs only 2. Characteristics 5 and 7 satisfy the proposition's stated restriction. Root permutation and recentering transport these examples to all 24 distinct-entry tuples; these are one symmetry orbit, not 24 separate mechanisms. The audit also exhibits a nonzero class annihilated by the actual parameter in the quotient used by the disputed cancellation step.

The [dependency audit](DEPENDENCY_AUDIT.md) traces the defect into the proof of Theorem A. It finds a second invalid supporting inference in characteristic zero: a unit polynomial over an Artinian local ring can have nonzero nilpotent higher coefficients. An explicit abstract determinantal model meets the relevant supporting hypotheses. This does **not** give a characteristic-zero counterexample to the Casas–Alvero conjecture, nor does it disprove the special Casas–Alvero conclusion of Lemma 4.5. It shows that its displayed argument needs an additional justification.

Repairing Proposition 3.3 alone would therefore not complete the preprint's argument as written. No repair proving Theorem A was found in this campaign. The same small counterexample orbit has resultant 315 after the linear equation is removed, so it supplies no characteristic-zero counterexample to Proposition 3.3.

The exact audited source is [Ghosh, arXiv:2501.09272v2](https://arxiv.org/html/2501.09272v2). Its version-history date is 21 March 2026; the downloaded manuscript displays 24 August 2026 internally. Hashes are in [SOURCE_IDENTITY.json](SOURCE_IDENTITY.json). The source manuscript is not redistributed in this package.

## Assessment and next decision

The audit-first approach was productive: the counterexample is explicit, the dependency analysis identifies a further repair obligation, and the bounded positive pilot produced a complete sparse exclusion. This supports preserving the result for specialist review. It does not yet justify committing to an all-degree proof campaign.

The sparse theorem is a **modest partial advance if novel**. Most of the support pruning comes from established work; the potential contribution is the last family's exclusion and its replayable characteristic-zero proof. The user’s original significance threshold remains relevant: this result should not be presented as comparable in importance to solving the conjecture. A more substantial next research target would need a structural argument covering a meaningful class of denser supports, with a bounded pilot before larger computation.

The [novelty report](NOVELTY_REPORT.md) separates this assessment from proof correctness. It also corrects two overstatements in the initial brief: Ghosh is not the only author whose preprint claims a full proof, and a bounded search cannot establish that no public objection exists. Degree 20 remains the first open degree in the checked specialist literature; a conflicting recent survey sentence supplies no new degree-20 proof.

## Replay

Unzip the package and run, using Python 3.10 or later:

```sh
cd casas-alvero-audit
python3 replay.py
```

The runner checks all manifest hashes and runs each of the following in normal and optimized Python, comparing the resulting JSON with frozen receipts:

| Checker | What it checks |
|---|---|
| `check_audit.py` | Finite-field ideal identities, local generator counts in monomial coordinates, symmetry, torsion, and characteristic-zero supporting identities |
| `check_support_filter.py` | The determinant filter by two exact arithmetic algorithms, including the published degree-12 indexing examples |
| `verify_mod31.py` | The explicit unit identity, generator reconstruction, leading coefficients needed for finiteness, and a corrupted-certificate rejection |

The three scripts use only the standard library. Their outputs are `audit-check.json`, `support-filter.json`, and `mod31-verification.json`. The optional `reviews/independent_mod31_audit.py` requires SymPy; its existing receipt records version 1.14.0. `regenerate_certificate.sing` is optional discovery/reproduction code for Singular, run in a fresh temporary directory; it is not needed to trust or replay the supplied identity. A fresh generation reproduced the exact certificate bytes. To repeat that step, run `Singular -q /path/to/regenerate_certificate.sing` from an empty directory, followed by `python3 /path/to/verify_mod31.py certificate.generated.txt`.

Mathematical dependencies still to read are the published CLO theorems, the coordinate and localization arguments, and the normalization/Nakayama proof. File integrity and a successful checker do not formally verify those arguments. The internal review records are preserved in `reviews/`, with their original narrower scopes and timing. Final conclusions are those stated in this README and the integrated proof, not conditional wording in earlier review snapshots.

The main certificate SHA-256 is:

`e63069da3f19151f84cd44ec9f5c46e55d6d806e743c0ccbd25827c6214020a0`.

The archive has an external checksum sidecar. Its extracted files were replayed independently of the working directory. No publication, submission, or author outreach was performed.
