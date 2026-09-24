"""Offline exact arithmetic replay; written valuation proofs remain separate.

The inherited package includes writers, as does one independent audit script.
Every computation therefore runs in a temporary copy, preserving frozen files.
The optional large integer-resultant replay is not needed by the compact proof.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CHECKS = ['cluster/check_jets.py', 'u_one/check_jets.py',
          'u_equals_v/check_jets.py', 'u_one/check_u_equals_v_audit.py',
          'structural_audit/check_independent_jets.py']


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def manifest_check():
    manifest = json.loads((ROOT / 'MANIFEST.json').read_text())
    for name, digest in manifest.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                'Manifest mismatch: ' + name)
    return len(manifest)


def run(root, filename, optimized=False, timeout=120):
    command = [sys.executable, '-B'] + (['-O'] if optimized else [])
    proc = subprocess.run(command + [str(root / filename)], cwd=root,
                          capture_output=True, text=True, timeout=timeout)
    require(proc.returncode == 0, filename + ': ' + proc.stderr[-4000:])
    receipt = json.loads(proc.stdout)
    require(receipt['status'] == 'PASS', filename + ': missing PASS')
    return receipt


def main():
    count = manifest_check()
    receipts = []
    with tempfile.TemporaryDirectory(prefix='casas-c-replay-') as temporary:
        scratch = Path(temporary) / 'package'
        shutil.copytree(ROOT, scratch)
        inherited = run(scratch, 'dependencies/casas-alvero-sixterm/replay.py')
        require(inherited['remainingSixTermDeficiencySupport'] == [[4,5,10,17,19]],
                'Inherited frontier differs')
        for optimized in (False, True):
            for filename in CHECKS:
                receipts.append({'script': filename, 'optimized': optimized,
                                 'receipt': run(scratch, filename, optimized)})

        # Reconstruct marked assignments from the earlier independently checked
        # full gcd polynomials. Linear factors cover these two surviving seeds.
        prior = json.loads((scratch / 'dependencies/casas-alvero-sixterm/reviews/'
                            'c-independent-patterns.json').read_text())
        derived = []
        for point in prior['coefficientPoints']:
            if point['coefficients'][3] == 0:
                continue  # Entire d=0 point was excluded in the written dependency.
            gcds = point['activeGcdsAscending']
            roots = {}
            for order in (3,15,1):
                polynomial = gcds[str(order)]
                roots[order] = [x for x in range(13)
                                if sum(c*pow(x,i,13) for i,c in enumerate(polynomial)) % 13 == 0]
            derived += [[v,u,w] for v in roots[3] for u in roots[15] for w in roots[1]]
        coverage = json.loads((scratch / 'case_coverage.json').read_text())
        covered = [row['residues'] for row in coverage['rows']]
        require(sorted(derived) == sorted(covered) and len(covered) == 6,
                'New branch list does not cover the inherited frontier')
        for row in coverage['rows']:
            require((scratch / row['proof']).is_file(), 'Missing branch proof')

        # A wrong coefficient in the independent full integer reconstruction
        # must be rejected by arithmetic, without relying on manifest rejection.
        audit = scratch / 'u_one/check_u_equals_v_audit.py'
        source = audit.read_text()
        needle = 'A = -comb(20, 16)'
        require(source.count(needle) == 1, 'Negative-control anchor changed')
        audit.write_text(source.replace(needle, needle + ' + 1'))
        negative = subprocess.run([sys.executable, '-B', '-O', str(audit)],
                                  cwd=scratch, capture_output=True, text=True)
        require(negative.returncode != 0 and 'ValueError' in negative.stderr,
                'Wrong-coefficient negative control was not rejected')

    require(manifest_check() == count, 'Replay changed frozen files')
    print(json.dumps({'status': 'PASS', 'manifestFiles': count,
                      'inheritedCheckCount': inherited['checkCount'],
                      'newCheckCount': len(receipts),
                      'totalCheckCount': inherited['checkCount'] + len(receipts),
                      'coveredResidueRows': covered,
                      'checks': receipts,
                      'negativeControl': 'Altered H16-normalization coefficient rejected under -O',
                      'conclusion': 'Arithmetic and case coverage support the written C exclusion and seven-term corollary.',
                      'scope': 'Exact arithmetic/internal proof; not external review, formal verification, or novelty certification.'}, indent=2))


if __name__ == '__main__':
    main()
