# Casas--Alvero research: review package

Start with [REPORT.pdf](REPORT.pdf), then [REVIEW_GUIDE.md](REVIEW_GUIDE.md).
The editable report is [REPORT.md](REPORT.md); [REPORT.tex](REPORT.tex) is
the complete typesetting source. Compile the latter with Tectonic or XeLaTeX.

Neither unrestricted degree 20 nor the full conjecture is proved.
This unpublished package contains partial results, proof audits, exact
certificates, unsuccessful approaches, and explicit remaining obligations.
No novelty, external-validation, or publication claim is made.

See [PROOF_INDEX.md](PROOF_INDEX.md) for all preserved proof notes and
[CHECKS.md](CHECKS.md) for the actual closeout replay scope and outcome.
Run `python3 replay.py` for the bounded default replay in a temporary copy.
The optional `--include-m6` also repeats the longer final native census.
`MANIFEST.json` checks file integrity only.


This is the portable revision of the 23 September review package. Mathematical
claims and raw execution receipts are unchanged. See [PORTABILITY_CHANGES.md](PORTABILITY_CHANGES.md)
for the revised commands, test scope, and preserved original files.
`CXX` or `--cxx` selects a C++17 compiler without invoking a shell. For a slower
host, `python3 replay.py --include-m6 --timeout-scale 4` gives a bounded longer
full replay; the default still checks the saved m6 census only.
