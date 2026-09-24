# Agent-readable research index

## Identity and exact scope

**An eight-term bound for degree-twenty Casas–Alvero polynomials**, Anonymous, version `0.1.0-candidate`. [Manuscript](PAPER.md), [PDF](PAPER.pdf), [claims](CLAIMS.json).

The candidate theorem excludes seven or fewer monomials in a nontrivial characteristic-zero degree-twenty Casas–Alvero polynomial after translation to the nineteenth-derivative root. The leading monomial counts. It does not prove the degree-twenty or general conjecture, sharpness, or a bound for arbitrary translates.

## Evidence and dependencies

The written proof includes normalization, fourteen exact supports, nineteen seed cases and all local transfer arguments, including arbitrary ramification. [Coverage audit](research/next-stage/coverage/EIGHT_TERM_AUDIT.md), [review guide](REVIEW_GUIDE.md), [row-8 census](new-results/check_row8_seven_term.py). Appendix A supplies the lower-term theorem. The structural dependency map appears in the introduction.

## Replay and environment

Use Python 3.10 or later for [the new runner](replay_new.py): sixteen standard-library checkers, each in normal and optimized modes, including all 1,216 row-8 markings. [The inherited runner](replay.py) additionally needs a C++ compiler; one historical cross-check needs optional SymPy. It reports every omission explicitly. [Environment](ENVIRONMENT.txt), [negative controls](test_publication.py), [reproduction commands](README.md).

## Trust boundaries

[ASSURANCE.md](ASSURANCE.md) separates producer replay, internal editorial review, external reported checks, formal verification and novelty. The theorem still depends on written mathematical implications, not only program exits. A supplied review reports no fatal error, but its latest linked audit ZIP was not accessible at intake. No journal peer review, independently authenticated specialist endorsement, or unconditional priority clearance is claimed. [Literature comparison](review/FINAL_RESEARCH_LITERATURE.md) and [revision response](REVISION_RESPONSE.md).

## Provenance, rights and versioning

[PROVENANCE.md](PROVENANCE.md) identifies the prior review archive and the publication changes. [LICENSES.md](LICENSES.md) applies CC0-1.0 to original prose/data and MIT to original code. Third-party review source files are not redistributed; cited works remain at their primary URLs. Historical records retain their earlier scope and are not current release receipts. [CITATION.cff](CITATION.cff) supplies the exact publication identity. Manifest checks establish bytes only.

Final internal editorial disposition: [EDITORIAL_DECISION.md](EDITORIAL_DECISION.md); individual reports are in review/publication-editorial/.
