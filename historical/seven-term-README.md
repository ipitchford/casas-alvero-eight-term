# Casas–Alvero: final scientific manuscript for review

Start with [PAPER.pdf](PAPER.pdf), the 24 September 2026 manuscript, and
[review/REVIEW_RESPONSE.md](review/REVIEW_RESPONSE.md).
Editable source: [PAPER.md](PAPER.md); complete typesetting source: [PAPER.tex](PAPER.tex).

## Scientific status

The proved global lower bound is seven terms after centering. Six further
exact seven-term supports are excluded, reducing that frontier from fourteen
to eight. Neither an eight-term bound, unrestricted degree twenty, nor the
full conjecture is proved. Strong three-star significance remains unestablished;
[the assessment](review/FINAL_ASSESSMENT.md) explains why. No publication or
submission was performed. Administrative authorship, funding, contribution,
and interest declarations remain for the responsible author before submission.

## Reproduce the checks

Run from this directory with Python 3 and a C++ compiler; the optional symbolic
check uses SymPy. The default mathematical replay checks saved m6 certificates;
it does not regenerate the complete m6 census.

```sh
python3 replay.py --integrity-only
python3 replay.py --output ../casas-replay-results
python3 -B new-results/check_structural_argument.py
python3 -B new-results/check_row8_seven_term.py
python3 -B -O new-results/check_structural_argument.py
python3 -B -O new-results/check_row8_seven_term.py
```

See [PORTABILITY_CHANGES.md](PORTABILITY_CHANGES.md) for safe `CXX`/`--cxx`,
`--timeout-scale`, explicit deadline controls, and optional longer m6 replay.
The new row-8 check enumerates all 1,216 necessary residue assignments for
seven specified supports. It does not reprove the inherited seed classification.

The 27 default checks passed in the revised portable copy (51.024 seconds of
recorded child time). Seven portability smoke categories passed. The final
packaged new scripts passed normally and under `-O`, from `/tmp`; receipts
are in [verification/final-additions](verification/final-additions/RESULTS.json).
The supplied external independent arithmetic audit and its matching local
rerun are in `review/external-verification/`. No new full m6 census was run.

## Contents and preservation

- `new-results/`: current support corollaries, marked norm theorem, checkers and receipts.
- `evidence/`: preserved scientific evidence, with documented portability changes only.
- `review/`: response, source comparison, scope assessment and supplied external audit.
- `REPORT.pdf` and `REPORT.md`: the older 23 September consolidated report, retained as historical context.
- `portability-originals/`: exact former bytes and historical manifest resolution.
- `historical/`: portable-copy navigation documents before the final manuscript was added.
- `MANIFEST.json`: hashes of final archive files; integrity is not proof validation.

The main paper identifies the definitive proof path. Older frontier counts
inside frozen evidence are not silently rewritten; the six exact-support
updates are stated explicitly in the new paper and support note. Note-hash
changes caused only by packaged link repair are mapped in PACKAGING_TRANSFORMS.json.

## Rebuild the PDF

The standalone `PAPER.tex` builds using Tectonic or XeLaTeX. To regenerate it
from Markdown with Pandoc, then compile:

```sh
pandoc PAPER.md --from=markdown+tex_math_single_backslash --standalone --toc --number-sections --top-level-division=section -V geometry:margin=25mm -V fontsize=10pt -V colorlinks=true -V linkcolor=blue --include-in-header build/layout.tex --lua-filter build/wrap_paths.lua --to=latex -o PAPER.tex
tectonic PAPER.tex
```

`build/build_paper.py` records workspace assembly provenance and expects the
original research workspace; the commands above rebuild from this archive alone.
