#!/usr/bin/env python3
"""Check the frozen files and replay the three exact checkers, offline.

No computer algebra package is required. This checks finite algebraic evidence;
it does not formally verify the written proofs or establish historical novelty.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys


def main():
    base = Path(__file__).resolve().parent
    manifest = json.loads((base / 'MANIFEST.json').read_text())
    for name, expected in manifest['sha256'].items():
        actual = hashlib.sha256((base / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError('File hash mismatch: ' + name)
    checks = [
        ('check_audit.py', 'audit-check.json'),
        ('check_support_filter.py', 'support-filter.json'),
        ('verify_mod31.py', 'mod31-verification.json'),
    ]
    receipts = []
    for script, golden in checks:
        expected = json.loads((base / golden).read_text())
        for options in ([], ['-O']):
            run = subprocess.run(
                [sys.executable, *options, str(base / script)],
                cwd=base, check=True, text=True, capture_output=True,
                timeout=60,
            )
            actual = json.loads(run.stdout)
            if actual.get('status') != 'PASS' or actual != expected:
                raise ValueError('Receipt mismatch: ' + script)
            receipts.append({'script': script,
                             'mode': 'optimized' if options else 'normal',
                             'status': 'PASS'})
    print(json.dumps({
        'status': 'PASS', 'python': sys.version.split()[0],
        'manifest_files_checked': len(manifest['sha256']),
        'checks': receipts,
        'scope': 'File integrity and finite exact identities; written proof dependencies and novelty require separate assessment.'
    }, indent=2))


if __name__ == '__main__':
    main()
