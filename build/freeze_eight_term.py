#!/usr/bin/env python3
"""Freeze the reviewed eight-term manuscript and its evidence, without rebuilding science."""
from pathlib import Path
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
import zipfile
import sympy

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
BUNDLE = ROOT/'outputs/casas-alvero-eight-term-review'
ARCHIVE = BUNDLE.with_suffix('.zip')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for name in ('FINAL_SCOPE_REVIEW.md', 'FINAL_PROOF_TRANSCRIPTION.md', 'FINAL_REVIEW_RESPONSE.md'):
        shutil.copy2(BASE/'review'/name, BUNDLE/'review'/name)
    shutil.copy2(BASE/'final-manuscript/INTEGRATION_REVIEW.md', BUNDLE/'manuscript/INTEGRATION_REVIEW.md')
    for source, target in (('casas-eight-term-new-replay', 'eight-term-new'), ('casas-eight-term-inherited-replay', 'eight-term-inherited')):
        shutil.copytree(ROOT/'outputs'/source, BUNDLE/'verification'/target, dirs_exist_ok=True)
    new = json.loads((BUNDLE/'verification/eight-term-new/summary.json').read_text())
    inherited = json.loads((BUNDLE/'verification/eight-term-inherited/REPLAY.json').read_text())
    if new['status'] != 'PASS' or inherited['status'] != 'PASS':
        raise RuntimeError('Cannot freeze failed arithmetic replays')
    missing = []
    for name in ('PAPER.md', 'README.md', 'REVIEW_GUIDE.md'):
        for link in re.findall(r'\]\(([^)]+)\)', (BUNDLE/name).read_text()):
            if '://' not in link and not link.startswith('#') and not (BUNDLE/link.split('#')[0]).exists():
                missing.append((name, link))
    if missing:
        raise RuntimeError(f'Unresolved current evidence links: {missing}')
    log = (BUNDLE/'PAPER.log').read_text()
    if any(x in log for x in ('Overfull', 'Missing character:', 'undefined references')):
        raise RuntimeError('Unresolved typesetting problem')
    qa = {
        'status': 'PASS', 'date': '2026-09-24',
        'manuscriptSHA256': sha(BUNDLE/'PAPER.md'), 'pdfSHA256': sha(BUNDLE/'PAPER.pdf'),
        'pages': 40, 'visuallyInspectedPages': [1, 5, 15, 23, 37, 40],
        'allPageTextBoundingBoxesWithinPage': True,
        'texWarnings': ['One underfull hbox, badness 1158; no overfull boxes, missing glyphs or undefined references'],
        'currentDocumentLocalLinks': 'all resolve',
        'newCheckers': new['checkers'], 'newExecutions': new['executions'],
        'inheritedDefaultChecks': len(inherited['checks']),
        'optionalM6FullCensusRerun': False,
        'python': sys.version, 'sympy': sympy.__version__, 'platform': platform.platform(),
        'scope': 'Manuscript presentation, exact replay and package QA; not external peer review, priority clearance, formal verification, or a full-conjecture solution.'
    }
    (BUNDLE/'verification/FINAL_PACKAGE_QA.json').write_text(json.dumps(qa, indent=2)+'\n')
    files = [p for p in sorted(BUNDLE.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc']
    manifest = {'scope': 'File integrity only; not mathematical or novelty validation',
                'sha256': {str(p.relative_to(BUNDLE)): sha(p) for p in files if p != BUNDLE/'MANIFEST.json'}}
    (BUNDLE/'MANIFEST.json').write_text(json.dumps(manifest, indent=2)+'\n')
    subprocess.run([sys.executable, '-B', str(BUNDLE/'replay.py'), '--integrity-only'], check=True, cwd=ROOT)
    with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            z.write(p, str(Path(BUNDLE.name)/p.relative_to(BUNDLE)))
    with zipfile.ZipFile(ARCHIVE) as z:
        if z.testzip() is not None:
            raise RuntimeError('ZIP CRC failure')
        for name, expected in manifest['sha256'].items():
            actual = hashlib.sha256(z.read(BUNDLE.name+'/'+name)).hexdigest()
            if actual != expected:
                raise RuntimeError('Archived manifest mismatch: '+name)
    receipt = {'status': 'PASS', 'archive': ARCHIVE.name, 'archiveBytes': ARCHIVE.stat().st_size,
               'archiveSHA256': sha(ARCHIVE), 'manifestFilesVerifiedInArchive': len(manifest['sha256']),
               'manuscriptSHA256': qa['manuscriptSHA256'], 'pdfSHA256': qa['pdfSHA256'],
               'scope': 'Archive CRC and every manifest hash verified against archived bytes.'}
    ARCHIVE.with_suffix('.zip.sha256').write_text(f"{receipt['archiveSHA256']}  {ARCHIVE.name}\n")
    ARCHIVE.with_suffix('.verification.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
