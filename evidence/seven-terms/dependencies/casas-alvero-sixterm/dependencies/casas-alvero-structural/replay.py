"""Portable arithmetic replay; no third-party modules required.

The optional full resultant computation uses SymPy and is deliberately not a
dependency of the finiteness certificate. Mathematical arguments live in PROOF.md.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    'dynamics/check_fixed_dynamics.py',
    'uniform/check_boundaries.py',
    'uniform/check_proof_formula.py',
    'uniform/check_fixed_controls.py',
    'uniform/fast_necessary_filter.py',
    'uniform/finish_linear_candidates.py',
    'uniform/check_primes_below_10000.py',
    'sixterm/enumerate_sixterm.py',
    'sixterm/apply_two_visible.py',
    'sixterm/old_baseline_and_groups.py',
    'sixterm/verify_last_mask.py',
    'prior-art/check_known_criteria.py',
]

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

manifest_file = ROOT / 'MANIFEST.json'
manifest = json.loads(manifest_file.read_text()) if manifest_file.exists() else {}
for filename, digest in manifest.items():
    require(hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == digest,
            'Manifest mismatch: ' + filename)

results = []
for optimized in (False, True):
    for filename in SCRIPTS:
        command = [sys.executable, '-B'] + (['-O'] if optimized else [])
        proc = subprocess.run(command + [str(ROOT / filename)],
                              cwd=ROOT, capture_output=True, text=True)
        require(proc.returncode == 0, filename + ': ' + proc.stderr[-3000:])
        results.append({'script': filename, 'optimized': optimized, 'status': 'PASS'})

# A deliberate coefficient mutation must be caught by reconstruction, even -O.
with tempfile.TemporaryDirectory(prefix='casas-frobenius-negative-') as temporary:
    test_root = Path(temporary)
    (test_root / 'dynamics').mkdir()
    shutil.copy2(ROOT / 'dynamics/check_fixed_dynamics.py', test_root / 'dynamics')
    changed = json.loads((ROOT / 'fixed-polynomial.json').read_text())
    changed['H_coefficients_high_first'][5] += 1
    (test_root / 'fixed-polynomial.json').write_text(json.dumps(changed))
    negative = subprocess.run([sys.executable, '-B', '-O',
                               str(test_root / 'dynamics/check_fixed_dynamics.py')],
                              capture_output=True, text=True)
    require(negative.returncode != 0 and 'Reconstructed H disagrees' in negative.stderr,
            'Changed-coefficient negative control failed to reject')

for filename, digest in manifest.items():
    require(hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == digest,
            'Replay changed a frozen artifact: ' + filename)

print(json.dumps({'status': 'PASS', 'manifest_files': len(manifest),
                  'checks': results, 'negative_control': 'changed H coefficient rejected',
                  'scope': 'Exact arithmetic replay, not formal proof or historical novelty.'},
                 indent=2))
