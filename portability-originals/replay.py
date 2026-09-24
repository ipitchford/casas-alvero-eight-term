#!/usr/bin/env python3
"""Bounded review replay. Runs writers in a temporary evidence copy."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest():
    doc = json.loads((ROOT / 'MANIFEST.json').read_text())
    for name, expected in doc['sha256'].items():
        if digest(ROOT / name) != expected:
            raise ValueError('File-integrity mismatch: ' + name)
    return len(doc['sha256'])


def execute(command, cwd, timeout, log):
    started = time.monotonic()
    with log.open('w') as output:
        process = subprocess.Popen(command, cwd=cwd, stdout=output,
                                   stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = process.wait(timeout=timeout)
            state = 'PASS' if code == 0 else 'FAIL'
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            code = process.wait()
            state = 'TIMEOUT'
    return {'status': state, 'exitCode': code,
            'elapsedSeconds': round(time.monotonic()-started, 3),
            'wallLimitSeconds': timeout, 'log': log.name,
            'logSHA256': digest(log)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path.cwd()/'replay-results')
    parser.add_argument('--include-m6', action='store_true',
                        help='also repeat the final, longer m=6 native census if complete')
    parser.add_argument('--integrity-only', action='store_true')
    args = parser.parse_args()
    count = verify_manifest()
    if args.integrity_only:
        print(json.dumps({'status': 'PASS', 'integrityFiles': count,
                          'scope': 'File integrity only; no mathematical replay'}))
        return
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    checks = [
        ('audit', 'audit/replay.py', 120),
        ('seven-terms', 'seven-terms/replay.py', 180),
        ('p17-classification', 'full/support_frontier/prime17/check_classification.py', 120),
        ('seed-gcds', 'full/literature/check_prime17_seed_gcds.py', 30),
        ('p5-classification', 'full/five_adic/check_reduction.py', 30),
        ('p2-integral-cut', 'full/two_adic/check_first_saturation.py', 60),
        ('p2-occupancy', 'full/two_adic/check_cluster_occupancy.py', 60),
        ('row4-quadratic', 'full/tame17/check_row4_quadratic_constants.py', 30),
        ('row4-exclusion', 'full/tame17/check_row4_smallest_support.py', 120),
        ('row6-etale', 'full/tame17/check_row6_etale_constants.py', 30),
        ('row7-etale', 'full/tame17/check_row7_etale_constants.py', 30),
        ('row9-etale', 'full/tame17/check_row9_etale_constants.py', 30),
        ('row9-batch1', 'full/collective17/exclusions/check_batch.py', 120),
        ('row9-batch2', 'full/collective17/exclusions/check_batch.py', 120),
        ('row9-algebra', 'full/collective17/elimination/check_presentation.py', 30),
        ('cross-prime', 'full/cross_prime/check_cross_prime.py', 60),
        ('row8-radius', 'full/wild17/check_row8_bound.py', 30),
        ('row8-collective', 'full/wild17/blowup/check_collective.py', 60),
        ('quartic-models', 'full/wild17/blowup/m4/check_independent_model.py', 60),
        ('quartic-lift', 'full/wild17/blowup/m4/check_lift_consequences.py', 30),
        ('p19-first-jet', 'full/global/verify_p19_first_jet.py', 30),
        ('digit-blocks', 'full/cluster_tree/verify_digit_blocks.py', 30),
        ('analytic-models', 'full/global_analytic/verify_integral_countermodels.py', 30),
        ('height-models', 'full/global_height/verify_height_models.py', 30),
        ('matrix-models', 'full/global_matrix/verify_compressions.py', 30),
    ]
    if importlib.util.find_spec('sympy'):
        checks.append(('independent-integral-cut', 'full/check_integral_syzygy.py', 60))
    results = []
    with tempfile.TemporaryDirectory(prefix='casas-review-replay-') as temporary:
        evidence = Path(temporary)/'evidence'
        shutil.copytree(ROOT/'evidence', evidence)
        for name, relative, limit in checks:
            command = [sys.executable, '-B', str(evidence/relative)]
            if name == 'row9-batch2':
                command += ['--directory', str(evidence/'full/collective17/exclusions/batch-m5')]
            receipt = execute(command, evidence, limit, output/(name+'.log'))
            receipt.update({'check': name, 'script': relative})
            results.append(receipt)
            print(json.dumps(receipt), flush=True)
        configuration = ROOT/'M6_REPLAY.json'
        if configuration.exists() or args.include_m6:
            if not configuration.exists():
                raise ValueError('No completed m6 replay configured in this package')
            specification = json.loads(configuration.read_text())
            command = [sys.executable, '-B', str(evidence/specification['script'])]
            command += specification.get('defaultArguments', [])
            if args.include_m6:
                command += specification.get('freshCensusArguments', [])
            receipt = execute(command, evidence, 300, output/'row9-batch3.log')
            receipt.update({'check': 'row9-batch3', 'script': specification['script']})
            results.append(receipt)
            print(json.dumps(receipt), flush=True)
    verify_manifest()
    status = 'PASS' if all(x['status']=='PASS' for x in results) else 'FAIL'
    report = {'status': status, 'scope': 'Listed finite arithmetic and coverage replays only',
              'integrityFiles': count, 'checks': results,
              'sympyIndependentSyzygyIncluded': bool(importlib.util.find_spec('sympy')),
              'm6SavedCertificateChecked': configuration.exists(),
              'm6FreshCensusIncluded': args.include_m6,
              'notProved': ['unrestricted degree20', 'all-degree Casas-Alvero',
                            'novelty', 'external validation']}
    (output/'REPLAY.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': status, 'checks': len(results),
                      'receipt': str(output/'REPLAY.json')}))
    if status != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
