# Portability revision — 24 September 2026

This copy addresses compiler selection and bounded replay portability. It does
not change mathematical assertions, strengthen the seven-term theorem, or
claim a higher research rating. The original `outputs/casas-alvero-review`
package and every historical raw receipt remain unchanged.

## Commands and limits

Run `python3 replay.py --output /path/to/new/results` on Linux or macOS for
the default checks. A C++17 compiler is selected by `--cxx`, then `CXX`, then
`c++` on PATH. Commands are parsed with `shlex.split` and passed as argument
arrays without a shell; wrapper arguments and quoted paths are supported.

For a slower machine, use:

```sh
CXX=g++ python3 replay.py --include-m6 --timeout-scale 4 --output /path/to/new/full-results
```

All limits remain finite. The historical defaults are 30 seconds for
compilation, 90 seconds for each early native batch, 240 seconds for fresh
m6 enumeration, 120 seconds for each early outer checker, and 300 seconds
for the outer m6 checker. The scale applies to default limits. Explicit
`--compile-timeout`, `--native-timeout` and `--check-timeout` override their
respective scaled defaults. Invalid, zero, infinite and NaN limits are rejected.
When the outer limit is not explicitly set, overridden native/compiler
limits receive extra outer headroom. An explicit outer limit remains a hard
complete-check budget. Increasing it alone does not increase an inner limit.

The m6 checker has no competing worker deadline: the worker owns the compiler
and native deadlines, while the package runner guards the whole checker process
group. On every checker exit, the package runner cleans that private group.
Direct native runs require a scratch `--output` directory and refuse to replace
existing role receipts or logs. Native timeout/error states return failure.

The default m6 check verifies saved execution records and independently
checks survivor/lift arithmetic; it does not launch the 51-system census.
`--include-m6` repeats the same native implementation. It is not an independent
exhaustive FLINT replay. A timeout remains incomplete, never UNSAT or PASS.

## Files and integrity

Modified runtime scripts: `replay.py`,
`evidence/full/collective17/exclusions/check_batch.py`,
`evidence/full/collective17/exclusions/batch-m6/check_batch.py`, and
`evidence/full/collective17/exclusions/batch-m6/run_native.py`.
The new shared helper is `evidence/full/collective17/exclusions/native_options.py`.
The runtime changes are limited to compiler/guard options, receipt protection,
and execution metadata; the native C++ sources, residue enumeration formulas,
Hensel arithmetic and saved mathematical certificates are unchanged.

`README.md`, `REVIEW_GUIDE.md` and `CHECKS.md` document this revision.
`test_portability.py` gives the bounded smoke tests;
`refresh_portability_manifest.py` refreshes current manifests from child to
parent. `MANIFEST.json` and the two current exclusions/m6 manifests are refreshed.
Their exact former bytes and the former edited files are preserved under
`portability-originals/`; its PRESERVATION.md explains historical manifest resolution.
Historical process receipts, coverage counts, inputs and raw outputs are not
rewritten. No manifest hashes itself or its current parent.

## Verification

Portability smoke and the default 27-check receipt are stored in
`verification/portability/`. The final test outcomes are recorded below after
the run. No full m6 enumeration is a dependency of this revision.

## Recorded result

**PASS: all 27 default checks**, with 51.024 seconds of recorded child
time, including the optional SymPy check. See
[REPLAY.json](verification/portability/replay/REPLAY.json). The m6 entry checked
saved records and survivor/lift arithmetic; no full m6 census was launched.

**PASS: 7 portability smoke categories**, including safe compiler argv,
option propagation, real outer/native deadlines, no-overwrite behavior, and
a real compile/domain check over only one previously checked small system
(4,913 markings). Mocked dispatch tests establish argument flow, not mathematical
validity. See [SMOKE.json](verification/portability/SMOKE.json).

After the 27-check run, the outer timeout handler received one small robustness
fix: an already-exited process group no longer raises `ProcessLookupError`.
The final smoke suite tests this race deterministically. No mathematical
checker or native source changed after the successful default replay.

An independent internal code reviewer passed the revised controls, independently
reran the smoke tests, tested descendant cleanup after failure/timeout, and
compared all 621 original files. That review did not repeat the full m6 census
or independently rerun the 27-check campaign. It is not external mathematical
refereeing. The original package's 620-entry manifest still verifies.
