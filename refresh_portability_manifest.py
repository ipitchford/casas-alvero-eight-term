#!/usr/bin/env python3
"""Refresh only the current portable manifests, from children to parent; no hash cycles."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def record(path):
    data=path.read_bytes()
    return {'bytes':len(data),'sha256':sha256(data).hexdigest()}


def main():
    base=ROOT/'evidence/full/collective17/exclusions'
    for relative in ('batch-m6/MANIFEST.json','MANIFEST.json'):
        path=base/relative
        doc=json.loads(path.read_text())
        for name in doc['files']:
            doc['files'][name]=record(path.parent/name)
        if relative=='MANIFEST.json':
            doc['files']['native_options.py']=record(base/'native_options.py')
            doc['historicalSnapshots']['MANIFEST.before-m6.json']='Earlier 28-system manifest: resolve REPORT.md and COVERAGE.json against batch-m6/*.before-m6.*; resolve the revised check_batch.py against package-root portability-originals/evidence/full/collective17/exclusions/check_batch.py. Other historical inputs are unchanged.'
        else:
            doc['files']['../native_options.py']=record(base/'native_options.py')
        doc['portabilityRevision']='Current script hashes updated; original scripts/manifests preserved under package-root portability-originals. Raw mathematical certificates and execution receipts unchanged.'
        path.write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n')
    files={}
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts or path.name in ('RUN.lock','replay_residues') or path==ROOT/'MANIFEST.json':
            continue
        files[str(path.relative_to(ROOT))]=record(path)['sha256']
    doc={'scope':'Current portable package file integrity, not proof validation',
         'historicalSnapshots':'portability-originals preserves the prior manifests and edited files; see its PRESERVATION.md for historical path resolution.',
         'hashBoundary':'Nested current manifests omit parent manifests; this root manifest omits itself and volatile compiled/cache/lock files.',
         'sha256':files}
    (ROOT/'MANIFEST.json').write_text(json.dumps(doc,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','currentRootEntries':len(files)}))


if __name__=='__main__':main()
