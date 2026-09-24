#!/usr/bin/env python3
"""Replay the sixteen new arithmetic/assembly checks, in both Python modes.

This checks exact calculations and finite coverage. It does not replace the
written valuation proofs, establish novelty, or certify the full conjecture.
All execution takes place in an isolated copy; logs must be outside the bundle.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CHECKS = [
    '../../new-results/check_row8_seven_term.py',
    'check_row1_certificate.py',
    'check_row1_binary_census.py',
    'check_row5_first_divided.py',
    'row5-unit/check_row5_unit.py',
    'row5-jets/check_row5_jets.py',
    'row1-ramification/check_row1_elimination.py',
    'last-four/boundary/check_direct_jet.py',
    'last-four/middle/check_direct_jet_independent.py',
    'last-four/middle/check_mixed_strata.py',
    'last-four/quadratic/A/check_arithmetic.py',
    'last-four/quadratic/B/check_B.py',
    'last-four/row2/check_row2.py',
    'last-four/row2/check_row2_independent.py',
    'coverage/check_seven_term_inventory.py',
    'coverage/check_eight_term_assembly.py',
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise SystemExit('Choose an output directory outside the evidence bundle.')
    output.mkdir(parents=True, exist_ok=True)
    records = []
    with tempfile.TemporaryDirectory(prefix='casas-eight-term-') as tmp:
        copy = Path(tmp)/'bundle'
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        for index, relative in enumerate(CHECKS, 1):
            path = copy/'research/next-stage'/relative
            outputs = []
            record = {'checker': relative, 'sourceSHA256': hashlib.sha256(path.read_bytes()).hexdigest(), 'modes': []}
            for optimized in (False, True):
                mode = 'optimized' if optimized else 'normal'
                cmd = [sys.executable, '-B'] + (['-O'] if optimized else []) + [str(path)]
                result = subprocess.run(cmd, cwd=copy, capture_output=True, text=True, timeout=180)
                log = f'{index:02d}-{mode}.txt'
                (output/log).write_text(result.stdout + result.stderr)
                # Exit status is primary; require a positively asserted checker verdict.
                try:
                    payload = json.loads(result.stdout)
                    positive = payload.get('status') == 'PASS'
                except (json.JSONDecodeError, AttributeError):
                    positive = relative.endswith('/A/check_arithmetic.py') and result.stdout.strip().startswith('PASS')
                passed = result.returncode == 0 and positive
                record['modes'].append({'mode': mode, 'exitCode': result.returncode, 'status': 'PASS' if passed else 'FAIL', 'log': log})
                outputs.append(result.stdout)
            record['identicalModeOutput'] = outputs[0] == outputs[1]
            record['status'] = 'PASS' if record['identicalModeOutput'] and all(r['status'] == 'PASS' for r in record['modes']) else 'FAIL'
            records.append(record)
            print(f"{index:02d}/{len(CHECKS)} {record['status']} {relative}", flush=True)
    passed = all(r['status'] == 'PASS' for r in records)
    summary = {'status': 'PASS' if passed else 'FAIL', 'checkers': len(records), 'executions': 2*len(records), 'records': records,
               'scope': 'Exact arithmetic and assembly replay only. Mathematical arguments and external novelty require separate review.'}
    (output/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
