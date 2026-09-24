"""Convert a complete native run into the common residue-certificate format."""
from hashlib import sha256
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def need(ok,why):
    if not ok:raise ValueError(why)


def main():
    config=json.loads((HERE/'CONFIG.json').read_text())
    receipt=json.loads((HERE/'combined-process.json').read_text())
    need(receipt['status']=='COMPLETE','producer is incomplete')
    raw=(HERE/'combined-producer.log').read_bytes()
    need(sha256(raw).hexdigest()==receipt['combinedOutputSHA256'],'producer output fingerprint')
    lines=iter(raw.decode().splitlines())
    need(next(lines)=='DOMAIN_PASS 17 10','domain check missing')
    permutation=config['frobeniusPermutation'];cases=[]
    for index,support in enumerate(config['supports']):
        active=[j for j in support if 4<=j<=16]
        row=next(lines).split()
        need(row[:4]==['CASE',str(index),'6',str(17**6)],'case completeness')
        need(list(map(int,row[5:]))==active,'support mismatch')
        survivors=[]
        for _ in range(int(row[4])):
            entry=next(lines).split();need(entry[0]=='SURVIVOR','survivor tag')
            mark=list(map(int,entry[1:]));need(len(mark)==6 and all(0<=i<17 for i in mark),'invalid marking')
            survivors.append(mark)
        need(survivors==sorted(survivors) and len({tuple(m) for m in survivors})==len(survivors),'duplicate or disordered marking')
        remaining={tuple(m) for m in survivors};orbits=[]
        while remaining:
            start=min(remaining);mark=start;orbit=[]
            while mark not in orbit:
                need(mark in remaining,'Frobenius closure')
                orbit.append(mark);mark=tuple(permutation[i] for i in mark)
            need(mark==start,'orbit cycle')
            remaining.difference_update(orbit)
            orbits.append({'representative':list(start),'size':len(orbit)})
        cases.append({'support':support,'active':active,'markingsChecked':17**6,
                      'survivors':survivors,'frobeniusOrbits':orbits})
    need(next(lines)=='ALL_PASS' and next(lines,None) is None,'producer completion marker')
    output={'scope':'Complete native enumeration of m=6 only; no exhaustive independent FLINT enumeration.',
            'activeSizes':[6],'presentationSHA256':config['presentationSHA256'],
            'fieldPolynomialAscending':config['fieldPolynomialAscending'],
            'nonzeroRoots':config['nonzeroRoots'],'frobeniusPermutation':permutation,
            'cases':cases,'totalMarkingsChecked':sum(c['markingsChecked'] for c in cases),
            'producerProcessReceiptSHA256':sha256((HERE/'combined-process.json').read_bytes()).hexdigest(),
            'producerExecution':'See combined-process.json and preserved per-run receipts.'}
    (HERE/'residue-batch.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'systems':len(cases),'markings':output['totalMarkingsChecked'],
                      'residueSurvivors':sum(len(c['survivors']) for c in cases),
                      'frobeniusOrbits':sum(len(c['frobeniusOrbits']) for c in cases)}))


if __name__=='__main__':main()
