# Eight-term Casas–Alvero bound — unrefereed candidate

**Version 0.1.0-candidate. Author: Anonymous. Current manuscript:** [PAPER.pdf](PAPER.pdf), with [Markdown](PAPER.md) and [standalone LaTeX](PAPER.tex). Prepared 24 September 2026.

The claimed theorem is that a nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least **eight nonzero monomials after centering at the root of its nineteenth derivative**, counting the leading term. Fourteen exact seven-term supports and nineteen compatible characteristic-seventeen seed cases are excluded, in addition to the complete earlier lower-term proof.

This is a public unrefereed candidate for scientific review. Internal proof audits and exact arithmetic checks are included; they are not external refereeing, formal proof-assistant certification, or priority clearance. This work does not prove the unrestricted degree-twenty or general conjecture.

## Read first

1. [REVIEW_GUIDE.md](REVIEW_GUIDE.md): argument structure, checkers, and limits.
2. [Final assembly audit](research/next-stage/coverage/EIGHT_TERM_AUDIT.md): all fourteen supports and nineteen cases.
3. [Current significance assessment](review/EIGHT_TERM_ASSESSMENT.md) and [literature comparison](review/FINAL_RESEARCH_LITERATURE.md).
4. [Final response to review](review/FINAL_REVIEW_RESPONSE.md).

## Reproduce

Use Python 3 (standard library) for the new checks. The inherited replay also requires a C++ compiler; its selected native checks compile in an isolated temporary directory. Run from an extracted bundle:

```sh
python3 -B replay.py --integrity-only
python3 -B replay_new.py --output ../eight-term-new-replay
python3 -B replay.py --output ../eight-term-inherited-replay
```

The new runner includes the complete 1,216-marking row-8 census and executes sixteen checkers in normal and optimized Python (thirty-two executions), compares their outputs, and writes outside the bundle. The inherited default replay runs twenty-six checks, plus one optional SymPy check when available; its receipt names every omission. Its optional larger m6 census is not required for the eight-term argument and is not part of this final default replay. Saved census evidence remains available and distinctly labelled.

For typesetting, `tectonic PAPER.tex` builds the standalone LaTeX source. The `build/build_eight_term.py` script records the original workspace assembly; it is not a standalone reconstruction command. The supplied Markdown can also be converted with Pandoc using the supplied layout and path-wrapping filter.

## Provenance and historical material

The current paper supersedes the earlier seven-term paper, whose frozen files are retained under `historical/`. Source proofs and arithmetic are under `research/next-stage/`; earlier evidence is under `evidence/` and `new-results/`. Current final reviews have `FINAL_` or `EIGHT_TERM_` names under `review/`.

To preserve the earlier audit trail, the bundle retains historical root files including `REPORT.*`, `FINAL_COVERAGE.json`, `FINAL_MANUSCRIPT_REVIEW.md`, `M6_*`, `CHECKS.md`, `PROOF_INDEX.md`, `PORTABILITY_CHANGES.md`, and `PACKAGING_TRANSFORMS.json`. Their old case counts and manuscript verdicts concern the earlier package. They must not be read as the status of this paper. The current audit and replay records are named in REVIEW_GUIDE.md.

Working notes can describe branches as open or audits as pending: those dated states are superseded by the final assembly audit. In particular, `research/next-stage/last-four/quadratic/B/probe_jets.py` and `probe-jets-output.txt` are an **invalid, superseded exploratory diagnostic** that omitted a second-derivative term. The corrected proof and `check_B.py` retain that term; the probe is never replayed as evidence. Other `probe*` files are exploratory, not authoritative proof checkers.

MANIFEST.json records SHA-256 integrity for all packaged files except itself. Integrity verifies bytes, not mathematical truth. Review the paper and argument audits separately from successful checker exits.

[AI_INDEX.md](AI_INDEX.md) is the machine-agent entry point. [ASSURANCE.md](ASSURANCE.md), [LICENSES.md](LICENSES.md) and [REVISION_RESPONSE.md](REVISION_RESPONSE.md) describe status, rights and the publication revision. Rebuild from bundled sources with `python3 build/build_publication.py`.

Exact-version DOI: [10.5281/zenodo.22943640](https://doi.org/10.5281/zenodo.22943640). [Public source](https://github.com/ipitchford/casas-alvero-eight-term).
