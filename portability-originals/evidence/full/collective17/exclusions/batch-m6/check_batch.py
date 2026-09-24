"""Verify two native execution receipts and independently replay all survivor precision certificates.

No imports from either producer. H2/17 is recomputed by direct Hasse
differentiation at one extra digit, not from the saved linear formula.
"""
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import subprocess
import time
import argparse
import shutil
import sys
import tempfile

HERE=Path(__file__).resolve().parent
Q=(-8,7,4,-6,1,0,6,0,-1,4,1)
D=10


def require(ok,why):
    if not ok: raise ValueError(why)


class Quotient:
    def __init__(self,modulus):
        self.m=modulus
        self.zero=(0,)*D
        self.one=(1,)+(0,)*(D-1)

    def n(self,a): return tuple(v%self.m for v in a)
    def constant(self,a): return (a%self.m,)+(0,)*(D-1)
    def plus(self,a,b): return self.n(x+y for x,y in zip(a,b))
    def times_integer(self,a,k): return self.n(k*x for x in a)
    def times(self,a,b):
        c=[sum(a[i]*b[k-i] for i in range(max(0,k-D+1),min(D,k+1))) for k in range(2*D-1)]
        for k in range(len(c)-1,D-1,-1):
            lead=c[k]
            for j in range(D+1): c[k-D+j]-=lead*Q[j]
        require(not any(c[D:]),'polynomial remainder failure')
        return self.n(c[:D])

    def power(self,a,n):
        r=self.one
        for bit in bin(n)[2:]:
            r=self.times(r,r)
            if bit=='1': r=self.times(r,a)
        return r

    def value(self,f,x,order=0):
        return self.sum(self.times_integer(self.times(c,self.power(x,k-order)),comb(k,order))
                        for k,c in enumerate(f) if k>=order)

    def sum(self,values):
        total=self.zero
        for v in values: total=self.plus(total,v)
        return total


def make_polynomial(r,active,mark,roots):
    # Work with all normalized coefficients; inactive coefficients remain zero.
    a=[r.zero for _ in range(21)]
    a[0],a[3]=r.one,r.constant(-1)
    for j,ri in zip(active,mark):
        x=roots[ri]
        a[j]=r.times_integer(r.sum(r.times_integer(r.times(a[i],r.power(x,j-i)),comb(j,i))
                                   for i in range(j)),-1)
    f=[r.zero for _ in range(21)]
    for j in range(18): f[20-j]=r.times_integer(a[j],comb(20,j))
    v=r.sum(f); w=r.sum(r.times_integer(c,k) for k,c in enumerate(f))
    f[2]=r.plus(v,r.times_integer(w,-1))
    f[1]=r.plus(w,r.times_integer(v,-2))
    require(r.value(f,r.one)==r.value(f,r.one,1)==r.zero,'double root reconstruction')
    # Ascending coefficient recurrence for f=X*(X-1)^2*q.
    q=[]
    for k in range(18):
        value=f[k+1]
        if k>=1: value=r.plus(value,r.times_integer(q[k-1],2))
        if k>=2: value=r.plus(value,r.times_integer(q[k-2],-1))
        q.append(value)
    product=[r.zero for _ in range(21)]
    for k,c in enumerate(q):
        product[k+1]=r.plus(product[k+1],c)
        product[k+2]=r.plus(product[k+2],r.times_integer(c,-2))
        product[k+3]=r.plus(product[k+3],c)
    require(product==f and q[-1]==r.one,'exact quotient reconstruction')
    return a,f,q


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--directory',type=Path,default=HERE)
    parser.add_argument('--rerun-native',action='store_true',help='Repeat the full native enumeration in temporary files under its 240-second guard; the default checks the preserved completed-run receipts.')
    args=parser.parse_args();destination=args.directory.resolve()
    start=time.monotonic()
    raw=(destination/'residue-batch.json').read_bytes()
    residue=json.loads(raw)
    lifts=json.loads((destination/'lift-batch.json').read_text())
    require(lifts['residueCertificateSHA256']==sha256(raw).hexdigest(),'residue fingerprint')
    require(tuple(lifts['unramifiedPolynomialAscending'])==Q,'extension ring changed')
    presentation_raw=(HERE.parents[1]/'elimination/presentation.json').read_bytes()
    presentation=json.loads(presentation_raw)
    require(sha256(presentation_raw).hexdigest()==residue['presentationSHA256'],'presentation fingerprint')
    active_sizes=residue.get('activeSizes',[3,4])
    require(active_sizes==[6],'unauthorized batch range')
    supports=sorted((s for s in presentation['canonicalSupports'] if len(s)-3 in active_sizes),key=lambda s:(len(s),s))
    require([c['support'] for c in residue['cases']]==supports,'complete canonical batch')
    expected_input=[10,17,len(supports)]+list(Q)+[x for r in residue['nonzeroRoots'] for x in r]
    for case in residue['cases']:
        expected_input += [len(case['active'])]+case['active']
    require(list(map(int,(destination/'native-input.txt').read_text().split()))==expected_input,'native input binding')
    field=Quotient(17)
    z=(0,1)+(0,)*8
    frob=z
    for k in range(1,11):
        frob=field.power(frob,17)
        if k in (2,5):
            diff=field.plus(frob,field.times_integer(z,-1))
            require(field.times(diff,field.power(diff,17**10-2))==field.one,'proper-degree Rabin condition')
    require(frob==z,'final Rabin condition')
    roots=[tuple(v) for v in residue['nonzeroRoots']]
    require(len(roots)==len(set(roots))==17 and field.zero not in roots,'full nonzero domain')
    _,_,q0=make_polynomial(field,[],[],{})
    require(all(field.value(q0,r)==field.zero and field.value(q0,r,1)!=field.zero for r in roots),'domain completeness')
    frobenius=[roots.index(field.power(r,17)) for r in roots]
    require(frobenius==residue['frobeniusPermutation'],'Frobenius permutation')
    # These are two executions of the SAME native algorithm, not independent
    # exhaustive implementations. The arithmetic below independently checks
    # every survivor, orbit, and higher-precision certificate.
    combined=json.loads((HERE/'combined-process.json').read_text())
    require(combined['status']=='COMPLETE' and combined['caseCount']==51,'combined batch incomplete')
    combined_output=(HERE/'combined-producer.log').read_bytes()
    require(sha256(combined_output).hexdigest()==combined['combinedOutputSHA256'],'combined fingerprint')
    global_start=0
    for segment in combined['segments']:
        role=segment['role'];require(role in ('producer','continuation'),'unexpected segment')
        require(segment['globalStart']==global_start,'gap or overlap between segments')
        count=segment['caseCount'];subset=residue['cases'][global_start:global_start+count]
        receipt_raw=(HERE/(role+'-process.json')).read_bytes();receipt=json.loads(receipt_raw)
        require(sha256(receipt_raw).hexdigest()==segment['receiptSHA256'],'segment receipt fingerprint')
        require(receipt['status'] in (('COMPLETE','TIMEOUT') if role=='producer' else ('COMPLETE',)),'segment execution failed')
        require(receipt['sourceSHA256']==sha256((HERE/'replay_residues.cpp').read_bytes()).hexdigest(),'native source fingerprint')
        input_path=HERE/('continuation-input.txt' if role=='continuation' else 'native-input.txt')
        require(receipt['inputSHA256']==sha256(input_path.read_bytes()).hexdigest(),'segment input fingerprint')
        input_cases=residue['cases'] if role=='producer' else subset
        expected=[10,17,len(input_cases)]+list(Q)+[x for rr in residue['nonzeroRoots'] for x in rr]
        for c in input_cases:expected += [6]+c['active']
        require(list(map(int,input_path.read_text().split()))==expected,'segment input scope')
        output=(HERE/(role+'.log')).read_bytes()
        require(receipt['outputSHA256']==sha256(output).hexdigest(),'segment output fingerprint')
        segment_lines=iter(output.decode().splitlines());require(next(segment_lines)=='DOMAIN_PASS 17 10','segment domain check')
        for local,c in enumerate(subset):
            header=next(segment_lines).split()
            require(header==['CASE',str(local),'6',str(17**6),str(len(c['survivors']))]+list(map(str,c['active'])),'segment case mismatch')
            marks=[]
            for _ in c['survivors']:
                row=next(segment_lines).split();require(row[0]=='SURVIVOR','segment survivor marker');marks.append(list(map(int,row[1:])))
            require(marks==c['survivors'],'segment survivor mismatch')
        if receipt['status']=='COMPLETE':require(next(segment_lines)=='ALL_PASS' and next(segment_lines,None) is None,'segment completion')
        global_start+=count
    require(global_start==51,'incomplete segment coverage')
    replay=json.loads((HERE/'replay-process.json').read_text())
    require(replay['status']=='COMPLETE' and replay['returncode']==0,'full native replay incomplete')
    require(replay['sourceSHA256']==sha256((HERE/'replay_residues.cpp').read_bytes()).hexdigest(),'replay source fingerprint')
    require(replay['inputSHA256']==sha256((HERE/'native-input.txt').read_bytes()).hexdigest(),'replay input fingerprint')
    replay_output=(HERE/'replay.log').read_bytes()
    require(replay['outputSHA256']==sha256(replay_output).hexdigest(),'replay output fingerprint')
    require(combined_output==replay_output,'split producer and full replay disagree')
    native_outputs=[combined_output,replay_output]
    lines=iter(native_outputs[0].decode().splitlines())
    require(next(lines)=='DOMAIN_PASS 17 10','native domain checks')
    for index,case in enumerate(residue['cases']):
        row=next(lines).split()
        expected=['CASE',str(index),str(len(case['active'])),str(17**len(case['active'])),
                  str(len(case['survivors']))]+list(map(str,case['active']))
        require(row==expected,'native case count or support mismatch')
        actual=[]
        for _ in case['survivors']:
            row=next(lines).split(); require(row[0]=='SURVIVOR','native survivor tag')
            actual.append(list(map(int,row[1:])))
        require(actual==case['survivors'],'native full enumeration mismatch')
    require(next(lines)=='ALL_PASS' and next(lines,None) is None,'native completion')
    total_orbits=0; counts={}; summaries=[]; residual_orbits=[]
    require(len(lifts['cases'])==len(residue['cases'])==len(supports),'batch coverage')
    for case,cert in zip(residue['cases'],lifts['cases']):
        active=case['active']
        require(cert['active']==active and cert['support']==case['support'],'lift support mismatch')
        covered=set()
        for record in cert['orbits']:
            mark=tuple(record['representative']); orbit=[]; v=mark
            while v not in orbit:
                orbit.append(v);v=tuple(frobenius[i] for i in v)
            require(v==mark and len(orbit)==record['orbitSize'],'orbit size')
            require(not covered.intersection(orbit),'orbit overlap')
            covered.update(orbit)
            distinct=sorted(set(mark))
            require(distinct==record['distinctRootIndices'],'distinct-root model')
            initial={i:roots[i] for i in distinct}
            aa,ff,qq=make_polynomial(field,active,mark,initial)
            for j in active:
                require(aa[j]==tuple(record['residueParameters'][str(j)]),'residue coefficient mismatch')
            for i in distinct:
                diagonal=field.value(qq,roots[i],1)
                require(diagonal==tuple(record['jacobianDiagonalMod17'][str(i)]) and diagonal!=field.zero,'Jacobian diagonal')
            prior=initial; previous_precision=1
            for step in record['steps']:
                precision=step['precision']; require(precision==previous_precision+1,'precision gap')
                modulus=17**precision; r=Quotient(modulus)
                rr={int(i):tuple(v) for i,v in step['rootCoordinates'].items()}
                require(sorted(rr)==distinct,'missing root coordinate')
                for i in distinct:
                    require(tuple(v%17**previous_precision for v in rr[i])==prior[i],'inconsistent lift')
                a,f,q=make_polynomial(r,active,mark,rr)
                for j in active:
                    require(a[j]==tuple(step['parameters'][str(j)]),'lift coefficient mismatch')
                    gj=r.sum(r.times_integer(r.times(a[i],r.power(rr[mark[active.index(j)]],j-i)),comb(j,i)) for i in range(j+1))
                    require(gj==r.zero,'normalized derivative mismatch')
                require(all(r.value(q,x)==r.zero for x in rr.values()),'root equations at claimed precision')
                # One extra digit makes direct division of H2 by 17 exact at this precision.
                high=Quotient(17*modulus)
                _,fhigh,_=make_polynomial(high,active,mark,rr)
                h2=high.value(fhigh,high.one,2)
                require(all(v%17==0 for v in h2),'H2 not divisible by 17')
                actual_t=tuple(v//17 for v in h2)
                require(actual_t==tuple(step['T']),'direct divided H2 mismatch')
                prior=rr;previous_precision=precision
            final=record['steps'][-1]; td=tuple(final['T'])
            if not any(td):
                require(final['precision']==6 and record['status']=='UNRESOLVED_THROUGH_PRECISION_6','invalid residual status')
                residual_orbits.append({'active':active,'representative':list(mark),'orbitSize':len(orbit)})
                total_orbits+=1
                continue
            require(record['status']=='EXCLUDED','missing obstruction')
            valuation=0
            while all(v%17**(valuation+1)==0 for v in td):valuation+=1
            digit=tuple(v//17**valuation%17 for v in td)
            require(valuation==record['valuationOfT'] and digit==tuple(record['firstNonzeroTDigit']),'valuation mismatch')
            require(valuation<final['precision'],'insufficient precision')
            counts[final['precision']]=counts.get(final['precision'],0)+len(orbit)
            total_orbits+=1
            # Regression: the earlier degree-five marked orbit has the same
            # first nonzero divided-H2 digit under the field embedding.
            if active==[4,9,10,14] and len(orbit)==5:
                eta=roots[mark[1]]
                expected=field.sum(field.times_integer(field.power(eta,k),c)
                                   for k,c in enumerate([13,11,13,8,3]))
                require(digit==expected and valuation==1,'earlier five-orbit regression')
        require(covered=={tuple(v) for v in case['survivors']},'incomplete residual orbit coverage')
        expected_status='RESIDUAL_ORBITS' if any(r['status']!='EXCLUDED' for r in cert['orbits']) else 'EXCLUDED'
        require(cert['status']==expected_status,'case status')
        summaries.append({'active':active,'markings':case['markingsChecked'],
                          'firstResidueSurvivors':len(covered),'liftedOrbits':len(cert['orbits']),
                          'status':cert['status']})
    total_markings=sum(17**(len(s)-3) for s in supports)
    require(sum(c['markingsChecked'] for c in residue['cases'])==total_markings,'total marking count')
    result={'status':'PASS_PARTIAL' if residual_orbits else 'PASS','scope':'m=6 native coverage run twice; no independent exhaustive FLINT replay. All survivors and precision certificates independently verified.',
            'residualOrbits':residual_orbits,
            'activeSizes':active_sizes,'totalMarkings':total_markings,'residueSurvivors':sum(len(c['survivors']) for c in residue['cases']),
            'liftedFrobeniusOrbits':total_orbits,'markingsExcludedByPrecision':counts,
            'cases':summaries,'residueSHA256':sha256(raw).hexdigest(),
            'nativeSourceSHA256':sha256((HERE/'replay_residues.cpp').read_bytes()).hexdigest(),
            'liftCertificateSHA256':sha256((destination/'lift-batch.json').read_bytes()).hexdigest()}
    if args.rerun_native:
        with tempfile.TemporaryDirectory(prefix='casas-row9-m6-review-') as temporary:
            scratch=Path(temporary)
            for name in ('run_native.py','replay_residues.cpp','native-input.txt'):
                shutil.copy2(HERE/name,scratch/name)
            completed=subprocess.run([sys.executable,str(scratch/'run_native.py'),'--role','replay'],
                                     capture_output=True,text=True,timeout=280,check=True)
            fresh=json.loads((scratch/'replay-process.json').read_text())
            require(fresh['status']=='COMPLETE' and fresh['returncode']==0,'fresh native replay incomplete')
            require((scratch/'replay.log').read_bytes()==combined_output,'fresh native replay differs')
            result['freshNativeReplay']={'status':'PASS','elapsedSeconds':fresh['elapsedSeconds'],
                                        'outputSHA256':fresh['outputSHA256'],
                                        'scope':'Repeat of the same validated native algorithm; not an independent exhaustive implementation.'}
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
