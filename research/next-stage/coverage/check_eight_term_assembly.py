#!/usr/bin/env python3
"""Read-only indexing/receipt check for the written eight-term assembly audit.

This checks routing and recorded coverage, not the underlying mathematical
exclusions. It does not import any producer arithmetic or rerun a census.
"""
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
# The extracted review bundle has research/next-stage/coverage here; the
# workspace has work/casas-alvero-upgrade/next-stage/coverage. Locate inputs
# only within that layout. In particular, a bundle never falls back to the
# original workspace when a packaged input is missing.
BUNDLE = (
    HERE.parents[2]
    if HERE.parents[1].name == "research"
    and (HERE.parents[2] / "evidence").is_dir()
    else None
)
ROOT = HERE.parents[3] if BUNDLE is None else BUNDLE
UPGRADE_LOGICAL = "work/casas-alvero-upgrade/"
BUNDLE_PREFIXES = (
    (UPGRADE_LOGICAL + "next-stage/", "research/next-stage/"),
    (UPGRADE_LOGICAL + "research/", "new-results/"),
    ("work/casas-alvero-full/", "evidence/full/"),
    ("outputs/casas-alvero-review/evidence/seven-terms/", "evidence/seven-terms/"),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def source_path(logical_name):
    """Resolve a stable original source name within the current package."""
    if BUNDLE is None:
        return ROOT / logical_name
    for original, packaged in BUNDLE_PREFIXES:
        if logical_name.startswith(original):
            return BUNDLE / packaged / logical_name[len(original):]
    raise RuntimeError(f"No bundle mapping for proof input: {logical_name}")


SUPPORTS = [
    (2, 3, 4, 10, 12, 19),
    (3, 4, 9, 10, 12, 19),
    (3, 4, 5, 10, 13, 19),
    (3, 4, 10, 12, 15, 19),
    (3, 7, 9, 10, 16, 19),
    (3, 6, 10, 16, 17, 19),
    (7, 8, 10, 16, 17, 19),
    (10, 12, 13, 16, 17, 19),
    (6, 10, 15, 16, 17, 19),
    (9, 10, 15, 16, 17, 19),
    (2, 4, 10, 12, 18, 19),
    (3, 4, 10, 13, 18, 19),
    (2, 4, 10, 17, 18, 19),
    (4, 10, 16, 17, 18, 19),
]
SEEDS = [
    (0, 0, 16, 0, 0),
    (14, 0, 16, 0, 3),
    (14, 8, 16, 12, 0),
    (14, 0, 0, 11, 8),
    (14, 2, 0, 0, 0),
    (14, 2, 0, 11, 6),
    (14, 2, 0, 14, 3),
    (0, 16, 0, 0, 0),
    (0, 16, 0, 14, 3),
]
VISIBLE = (2, 3, 17, 18, 19)

# The proof keys identify implications checked in EIGHT_TERM_AUDIT.md.
COVER = {
    1: {5: "row5-completion", 8: "row8-divided-identity"},
    2: {8: "row8-divided-identity"},
    3: {8: "row8-divided-identity"},
    4: {8: "row8-divided-identity"},
    5: {8: "row8-divided-identity"},
    6: {1: "row1-nonzero-a3", 8: "row8-divided-identity"},
    7: {1: "row1-unit16"},
    8: {1: "row1-unit16-or-mixed"},
    9: {1: "row1-unit16"},
    10: {1: "row1-unit16-or-mixed"},
    11: {4: "row4-complete-J4-10-12"},
    12: {8: "row8-divided-identity", 9: "row9-complete-J4-10-13"},
    13: {1: "quadratic-A-row1", 2: "quadratic-A-row2", 4: "row4-exact-a17-zero"},
    14: {1: "quadratic-B-row1"},
}

INPUTS = [
    "next-stage/coverage/inventory-normal.json",
    "next-stage/coverage/inventory-optimized.json",
    "next-stage/coverage/INVENTORY_AUDIT.md",
    "research/SEVEN_TERM_FRONTIER.md",
    "research/GLOBAL_SUPPORT_COROLLARY.md",
    "next-stage/ROW1_UNIT16.md",
    "next-stage/ROW1_AUDIT.md",
    "next-stage/ROW1_RAMIFICATION.md",
    "next-stage/ROW1_RAMIFICATION_AUDIT.md",
    "next-stage/ROW5_COMPLETION.md",
    "next-stage/ROW5_COMPLETION_AUDIT.md",
    "next-stage/last-four/middle/MIXED_STRATA.md",
    "next-stage/last-four/middle/MIXED_AUDIT.md",
    "next-stage/last-four/quadratic/A/A_ROW1_EXCLUSION.md",
    "next-stage/last-four/quadratic/A/A_ROW1_SECOND_AUDIT.md",
    "next-stage/last-four/quadratic/B/B_EXCLUSION.md",
    "next-stage/last-four/quadratic/B/B_AUDIT.md",
    "next-stage/last-four/row2/ROW2_PROOF.md",
    "next-stage/last-four/row2/ROW2_AUDIT.md",
]
OTHER_INPUTS = [
    "work/casas-alvero-full/support_frontier/prime17/CLASSIFICATION.md",
    "work/casas-alvero-full/literature/PRIME17_CLASSIFICATION_AUDIT.md",
    "work/casas-alvero-full/LIFT_CONSEQUENCES_17.md",
    "work/casas-alvero-full/tame17/ROW4_SMALLEST_SUPPORT_EXCLUSION.md",
    "work/casas-alvero-full/tame17/ROW4_SMALLEST_SUPPORT_AUDIT.md",
    "work/casas-alvero-full/collective17/exclusions/BATCH1_PROOF.md",
    "work/casas-alvero-full/collective17/exclusions/residue-batch.json",
    "work/casas-alvero-full/collective17/exclusions/lift-batch.json",
    "work/casas-alvero-full/collective17/exclusions/verification-normal.json",
    "outputs/casas-alvero-review/evidence/seven-terms/PROOF.md",
    "outputs/casas-alvero-review/evidence/seven-terms/structural_audit/AUDIT.md",
    "outputs/casas-alvero-review/evidence/seven-terms/COMPLETION_AUDIT.md",
    "outputs/casas-alvero-review/evidence/seven-terms/dependencies/casas-alvero-sixterm/PROOF.md",
    "outputs/casas-alvero-review/evidence/seven-terms/dependencies/casas-alvero-sixterm/dependencies/casas-alvero-extension/PROOF.md",
    "outputs/casas-alvero-review/evidence/seven-terms/dependencies/casas-alvero-sixterm/dependencies/casas-alvero-structural/sixterm/REPORT.md",
]


def main():
    normal = json.loads((HERE / "inventory-normal.json").read_text())
    optimized = json.loads((HERE / "inventory-optimized.json").read_text())
    require(normal == optimized, "Inventory receipts disagree")
    require(normal["status"] == "PASS", "Inventory did not pass")
    require(normal["counts"] == {
        "linearTermSupports": 6188, "afterSingleton": 586,
        "afterTwoVisible": 348, "afterCLO": 14,
    }, "Unexpected inventory counts")
    require(set(map(tuple, normal["survivors"])) == set(SUPPORTS), "Support-list mismatch")
    require(len(set(SUPPORTS)) == len(SUPPORTS) == 14, "Duplicate/missing support")

    rows = []
    for label, support in enumerate(SUPPORTS, 1):
        require(len(support) == 6 and 19 in support, "Incorrect exact term count")
        compatible = [
            row for row, seed in enumerate(SEEDS, 1)
            if all(c == 0 or j in support for j, c in zip(VISIBLE, seed))
        ]
        require(set(compatible) == set(COVER[label]), f"Uncovered/extraneous case S{label}")
        rows.append({"label": f"S{label}", "support": support,
                     "compatibleSeedRows": compatible, "proofs": COVER[label]})
    require(sum(len(row["compatibleSeedRows"]) for row in rows) == 19, "Wrong pair count")

    batch = source_path("work/casas-alvero-full/collective17/exclusions/")
    residue = json.loads((batch / "residue-batch.json").read_text())
    lift = json.loads((batch / "lift-batch.json").read_text())
    verification = json.loads((batch / "verification-normal.json").read_text())
    target = [4, 10, 13]
    rc = [c for c in residue["cases"] if c["active"] == target]
    lc = [c for c in lift["cases"] if c["active"] == target]
    vc = [c for c in verification["cases"] if c["active"] == target]
    require(len(rc) == len(lc) == len(vc) == 1, "Missing/duplicated row9 record")
    rc, lc, vc = rc[0], lc[0], vc[0]
    require(rc["support"] == lc["support"] == list(SUPPORTS[11]), "Wrong row9 exact support")
    require(rc["markingsChecked"] == 17**3 == vc["markings"], "Incomplete recorded row9 domain")
    require(len(rc["survivors"]) == len(lc["orbits"]) == 1, "Unexpected row9 survivors")
    require(lc["status"] == vc["status"] == "EXCLUDED", "Missing recorded exclusion")
    orbit = lc["orbits"][0]
    require(orbit["orbitSize"] == 1 and orbit["valuationOfT"] == 2, "Incorrect row9 orbit")
    require(orbit["steps"][-1]["precision"] == 3, "Wrong row9 precision")
    require(orbit["steps"][-1]["T"] == [11 * 17**2] + [0] * 9, "Wrong row9 obstruction")

    logical_names = [UPGRADE_LOGICAL + p for p in INPUTS] + OTHER_INPUTS
    hashes = {}
    for logical_name in logical_names:
        path = source_path(logical_name)
        require(path.is_file(), f"Missing proof input: {path}")
        hashes[logical_name] = hashlib.sha256(path.read_bytes()).hexdigest()
    print(json.dumps({
        "status": "PASS", "exactSupports": 14, "compatibleSeedPairs": 19,
        "uncoveredSeedPairs": [], "rows": rows,
        "row9RecordedMarkings": 17**3, "row9RecordedObstruction": "11*17^2 mod 17^3",
        "inputSHA256": hashes,
        "scope": "Assembly/routing and saved-receipt consistency only; mathematical implications are reviewed in EIGHT_TERM_AUDIT.md. No census or finite identity was re-proved by this script.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
