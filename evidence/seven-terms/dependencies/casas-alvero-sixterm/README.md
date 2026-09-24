# Two exclusions and one remaining six-term family

23 September 2026. Unpublished research result, with internal mathematical audits and exact arithmetic certificates.

The bounded investigation excluded two of the three remaining centered six-term degree-20 Casas–Alvero supports. Combined with the preceding support sieve, it gives the following necessary condition:

> If a nontrivial degree-20 Casas–Alvero polynomial has exactly six nonzero terms after centering and making it monic, then it has the form
> \[
> X^{20}+aX^{16}+bX^{15}+cX^{10}+dX^3+eX,
> \qquad abcde\ne0.
> \]

**This last family is unresolved. The seven-term lower bound and the full conjecture have not been proved.**

The most useful development is the proof for family A. Its reduction modulo 13 has a nontrivial CA polynomial, so an empty-reduction argument cannot work. Nevertheless, several derivative witnesses must reduce to the same simple root. This forces those witnesses to be exactly equal in characteristic zero, reducing the family to one parameter; two coprime resultants then exclude it.

Family B has a complete characteristic-13 exclusion, including every coefficient degeneration. Its valuation transfer also excludes a larger closed coefficient mask. For family C, exact certificates classify three normalized residue coefficient points. One cannot lift, leaving six possible marked-root assignments in two coefficient patterns. Their necessary root coincidences are recorded, but none of the remaining branch classes is claimed excluded.

Read [PROOF.md](PROOF.md) for the combined theorem and dependency map, [A's proof](A/A_EXCLUSION_PROOF.md) and [B's proof](B/PROOF.md) for the exclusions, and [C's remaining branches](C/ROOT_CLUSTER_NOTE.md) for the obstruction to completion. [DECISION.md](DECISION.md) assesses what this changes about tractability and significance.

From the extracted archive, run `python3 replay.py`. The replay uses the standard library, checks the saved certificates normally and with `-O`, recomputes the finite support frontier, and runs inherited dependencies in a temporary copy so frozen evidence is not rewritten. Singular is needed only to reproduce the discovery calculations, not the main replay.

The checks certify arithmetic identities. The accompanying proofs and reviews supply their mathematical interpretation; no formal proof-assistant verification or external refereeing is claimed. The prior-art search found no exact overlap, but an inaccessible support-level research package remains an unresolved lead. Novelty and publication significance are therefore unconfirmed. Nothing was published or sent externally.
