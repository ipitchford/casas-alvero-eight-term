# The last six-term family is excluded

23 September 2026. Unpublished mathematical research result; exact arithmetic and internal mathematical review are supplied.

The focused attack on C produced a complete exclusion of
\[
X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\qquad ABCDE\ne0.
\]
Together with the preceding exhaustive support reduction and A/B exclusions, this proves the following internally audited result:

> Every nontrivial degree-20 Casas–Alvero polynomial has at least **seven nonzero terms after centering**, including the leading term.

**The full conjecture and unrestricted degree 20 remain unsolved by this work.** The bound concerns monomials, not distinct roots or recycled derivative witnesses.

Read [PROOF.md](PROOF.md) for the complete argument and six-case coverage. The main development is a valuation argument that recovers information lost when the middle coefficient disappears modulo 13. The remaining root equations force its normalized residue. In five cases this immediately conflicts with the middle derivative's possible roots; one case needs a second precision argument. Every step allows ramified extensions.

The detailed branch proofs are [exact u=1](u_one/JET_PROOF.md), [the unresolved cluster](cluster/PROOF.md), and [u=v](u_equals_v/JET_PROOF.md). Separate internal audits are [structural and integrated coverage](structural_audit/AUDIT.md) and [the two-stage u=v argument](u_one/U_EQUALS_V_AUDIT.md).

Run `python3 replay.py` after extracting the archive. The standard-library replay checks all three branch calculations normally and under `-O`, both independent reconstructions, the inherited classification/support certificates, and coverage of all six residue rows. It works in temporary copies to preserve frozen evidence. The earlier package is bundled unchanged under `dependencies/`.

That historical package still describes C as unresolved. The present proof supersedes that status; its earlier exclusions and certificates remain the dependencies used here.

An alternative, larger integer-resultant proof for u=v is retained in `u_equals_v/`; its optional `verify_certificate.py` took about 132 seconds and verified 1,544 integer Sylvester determinants in the producer's completed replay. The compact main proof does not depend on it. The exploratory `root_collision/` resultant output is a discovery record, also unused by the main proof.

The [prior-art update](structural_audit/PRIOR_ART_ADDENDUM.md) found no exact match but leaves a material unavailable-source overlap unresolved. Historical priority and publication significance are not established. Internal audits and exact replay do not constitute external refereeing or formal proof-assistant verification. Nothing was published or sent externally.
