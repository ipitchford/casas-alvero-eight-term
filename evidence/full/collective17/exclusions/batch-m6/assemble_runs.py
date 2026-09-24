"""Recover complete native cases and assemble the one permitted continuation."""
from hashlib import sha256
from math import comb
from pathlib import Path
import argparse
import importlib.util
import json

HERE=Path(__file__).resolve().parent


def need(ok,why):
    if not ok:raise ValueError(why)


def parse(role,supports,truncated=False):
    receipt=json.loads((HERE/(role+'-process.json')).read_text())
    need(receipt['status'] in (('COMPLETE','TIMEOUT') if truncated else ('COMPLETE',)),'invalid run status')
    raw=(HERE/(role+'.log')).read_bytes()
    need(receipt['outputSHA256']==sha256(raw).hexdigest(),'run fingerprint')
    need(receipt['sourceSHA256']==sha256((HERE/'replay_residues.cpp').read_bytes()).hexdigest(),'source fingerprint')
    lines=raw.decode().splitlines();need(lines and lines[0]=='DOMAIN_PASS 17 10','missing domain verification')
    cursor=1;cases=[]
    for index,support in enumerate(supports):
        if cursor==len(lines):break
        row=lines[cursor].split()
        if row==['ALL_PASS']:break
        active=[j for j in support if 4<=j<=16]
        need(row[:4]==['CASE',str(index),'6',str(17**6)],'invalid complete-case header')
        need(list(map(int,row[5:]))==active,'wrong case support')
        count=int(row[4])
        if cursor+1+count>len(lines):
            need(truncated,'incomplete survivor block');break
        survivors=[]
        for entry in lines[cursor+1:cursor+1+count]:
            tokens=entry.split();need(tokens[0]=='SURVIVOR','invalid survivor marker')
            mark=list(map(int,tokens[1:]));need(len(mark)==6 and all(0<=i<17 for i in mark),'invalid marking')
            survivors.append(mark)
        need(survivors==sorted(survivors) and len({tuple(m) for m in survivors})==count,'duplicate marking')
        cases.append({'support':support,'active':active,'survivors':survivors})
        cursor+=1+count
    if receipt['status']=='COMPLETE':
        need(len(cases)==len(supports) and lines[cursor:]==['ALL_PASS'],'false completion')
    checkpoints=(HERE/(role+'-progress.log')).read_text().splitlines()
    need(len(checkpoints)<=len(cases),'missing flushed record')
    for i,line in enumerate(checkpoints):
        tokens=line.split()
        need(tokens[:2]==['CASE_COMPLETE',str(i)],'checkpoint sequence')
        need(tokens[2]=='markings='+str(17**6),'checkpoint count')
        need(tokens[3]=='survivors='+str(len(cases[i]['survivors'])),'checkpoint survivors')
    return cases,receipt


def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','combine']);args=parser.parse_args()
    config=json.loads((HERE/'CONFIG.json').read_text());supports=config['supports']
    first,receipt=parse('producer',supports,True)
    # Independent scalar-polynomial replay of every recovered residue point.
    spec=importlib.util.spec_from_file_location('m6_survivor_checker',HERE/'check_batch.py')
    checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
    field=checker.Quotient(17);roots=[tuple(r) for r in config['nonzeroRoots']]
    for case in first:
        for mark in case['survivors']:
            a,_,q=checker.make_polynomial(field,case['active'],mark,{i:roots[i] for i in set(mark)})
            t=field.constant(-8037)
            for j in case['active']:
                t=field.plus(t,field.times_integer(a[j],comb(19-j,2)*(comb(20,j)//17)))
            need(t==field.zero,'recovered point fails residue obstruction')
            need(all(field.value(q,roots[i])==field.zero for i in set(mark)),'recovered witness outside domain')
    if args.mode=='prepare':
        remaining=supports[len(first):]
        need(remaining,'continuation not needed')
        data=[10,17,len(remaining)]+config['fieldPolynomialAscending']+[x for row in config['nonzeroRoots'] for x in row]
        for support in remaining:data += [6]+[j for j in support if 4<=j<=16]
        (HERE/'continuation-input.txt').write_text(' '.join(map(str,data))+'\n')
        result={'status':'COMPLETE_PREFIX_RECOVERED','casesRecovered':len(first),'markingsRecovered':len(first)*17**6,
                'survivorsIndependentlyChecked':sum(len(c['survivors']) for c in first),
                'remainingCases':len(remaining),'remainingSupports':remaining,
                'producerReceiptSHA256':sha256((HERE/'producer-process.json').read_bytes()).hexdigest()}
        (HERE/'prefix-recovery.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result));return
    segments=[{'role':'producer','globalStart':0,'caseCount':len(first)}]
    if len(first)<len(supports):
        rest,second=parse('continuation',supports[len(first):])
        segments.append({'role':'continuation','globalStart':len(first),'caseCount':len(rest)})
        cases=first+rest
    else:cases=first
    need(len(cases)==51,'incomplete combined batch')
    lines=['DOMAIN_PASS 17 10']
    for i,case in enumerate(cases):
        lines.append(' '.join(map(str,['CASE',i,6,17**6,len(case['survivors'])]+case['active'])))
        lines += ['SURVIVOR '+' '.join(map(str,m)) for m in case['survivors']]
    lines.append('ALL_PASS');output='\n'.join(lines)+'\n'
    (HERE/'combined-producer.log').write_text(output)
    for segment in segments:
        role=segment['role'];segment['receiptSHA256']=sha256((HERE/(role+'-process.json')).read_bytes()).hexdigest()
    result={'status':'COMPLETE','caseCount':51,'markings':51*17**6,'segments':segments,
            'combinedOutputSHA256':sha256(output.encode()).hexdigest(),
            'scope':'Producer split after original 180-second timeout; continuation contains only remaining cases.'}
    (HERE/'combined-process.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
