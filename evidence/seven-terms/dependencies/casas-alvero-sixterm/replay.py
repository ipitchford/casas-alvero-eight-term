"""Portable exact replay of the two exclusions and remaining support frontier.

Inherited enumeration scripts produce JSON, so every check runs in a temporary
copy. This separates fresh computation from the frozen evidence being checked.
Only Python's standard library is required; no Singular producer is invoked.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CHECKS = [
    ('A/check_seed_certificates.py', 'zero'),
    ('A/check_seed_univariate.py',),
    ('A/check_collision_resultants.py',),
    ('A/check_mask_counterexamples.py',),
    ('B/verify_certificate.py',),
    ('C/verify_univariate.py',),
    ('reviews/c_independent_patterns.py',),
    ('reviews/c_resultant_spotcheck.py',),
    ('C/check_counterexamples.py',),
    ('reviews/check_A_formulas.py',),
    ('reviews/b_independent_spotcheck.py',),
    ('prior-art/replay_three_masks.py',),
    ('dependencies/casas-alvero-extension/check_mod13_explanation.py',),
    ('dependencies/casas-alvero-extension/check_support_and_lift.py',),
    ('dependencies/casas-alvero-extension/supplement/verify_mod13.py',),
    ('dependencies/casas-alvero-structural/sixterm/enumerate_sixterm.py',),
    ('dependencies/casas-alvero-structural/sixterm/apply_two_visible.py',),
    ('dependencies/casas-alvero-structural/sixterm/old_baseline_and_groups.py',),
    ('dependencies/casas-alvero-structural/sixterm/verify_last_mask.py',),
    ('dependencies/casas-alvero-structural/prior-art/check_known_criteria.py',),
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_manifest(root):
    path = root / 'MANIFEST.json'
    require(path.is_file(), 'Missing manifest: ' + str(root))
    data = json.loads(path.read_text())
    if data.get('format') == 'sha256-file-manifest-v1':
        data = data['sha256']
    for name, digest in data.items():
        require(hashlib.sha256((root / name).read_bytes()).hexdigest() == digest,
                'Manifest mismatch: ' + str(root / name))
    return len(data)


def main():
    count = verify_manifest(ROOT)
    for name in ('casas-alvero-extension', 'casas-alvero-structural'):
        verify_manifest(ROOT / 'dependencies' / name)
    records = []
    with tempfile.TemporaryDirectory(prefix='casas-sixterm-replay-') as temporary:
        scratch = Path(temporary) / 'package'
        shutil.copytree(ROOT, scratch)
        for optimized in (False, True):
            for relative, *arguments in CHECKS:
                command = [sys.executable, '-B'] + (['-O'] if optimized else [])
                proc = subprocess.run(command + [str(scratch / relative)] + arguments,
                                      cwd=scratch, capture_output=True, text=True,
                                      timeout=120)
                require(proc.returncode == 0,
                        relative + ': ' + proc.stderr[-4000:] + proc.stdout[-2000:])
                # The older criteria checker predates the JSON receipt format.
                if relative.endswith('prior-art/check_known_criteria.py'):
                    require(proc.stdout.startswith('PASS:'), 'Missing criteria PASS receipt')
                    receipt = proc.stdout.strip()
                else:
                    receipt = json.loads(proc.stdout)
                # Retain the checker receipt, including exact identity counts.
                records.append({'script': relative, 'arguments': arguments,
                                'optimized': optimized, 'status': 'PASS',
                                'receipt': receipt})

            baseline = json.loads((scratch / 'dependencies/casas-alvero-structural/'
                                   'sixterm/old-baseline-and-groups.json').read_text())
            five = next(b for b in baseline['baselines'] if b['totalTermCount'] == 6)
            expected = [[3, 4, 10, 18, 19], [3, 10, 16, 17, 19],
                        [4, 5, 10, 17, 19], [4, 10, 12, 17, 19],
                        [8, 10, 16, 17, 19]]
            require(five['counts']['all'] == 8568, 'Incomplete support enumeration')
            require(five['oldOnlySurvivors'] == expected, 'Inherited frontier changed')
            masks = [
                {4, 8, 9, 10, 11, 12, 17, 19},
                {8, 9, 10, 11, 12, 16, 17, 19},
                {3, 4, 10, 18, 19},
                {3, 8, 9, 10, 11, 12, 16, 17, 19},
            ]
            remaining = [s for s in five['oldOnlySurvivors']
                         if not any(set(s) <= mask for mask in masks)]
            require(remaining == [[4, 5, 10, 17, 19]], 'Combined frontier mismatch')

        certificate = scratch / 'B/certificate.json'
        altered = json.loads(certificate.read_text())
        altered['R3'][0] = (altered['R3'][0] + 1) % 13
        certificate.write_text(json.dumps(altered))
        negative = subprocess.run([sys.executable, '-B', '-O',
                                   str(scratch / 'B/verify_certificate.py')],
                                  cwd=scratch, capture_output=True, text=True,
                                  timeout=120)
        require(negative.returncode != 0 and 'resultant' in negative.stderr.lower(),
                'Altered-resultant negative control was not rejected as expected')

    require(verify_manifest(ROOT) == count, 'Frozen package changed during replay')
    print(json.dumps({'status': 'PASS', 'manifestFiles': count,
                      'checks': records, 'checkCount': len(records),
                      'remainingSixTermDeficiencySupport': remaining,
                      'negativeControl': 'Changed B resultant rejected under -O',
                      'scope': 'Exact arithmetic and frontier replay; written proof, '
                               'external review, and novelty are separate.'}, indent=2))


if __name__ == '__main__':
    main()
