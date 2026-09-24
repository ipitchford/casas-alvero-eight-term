#!/usr/bin/env python3
"""Bounded semantic mutation controls and publication-runner contract checks."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,shutil
R=Path(__file__).resolve().parent

def require(ok,msg):
 if not ok:raise RuntimeError(msg)

results=[]
with tempfile.TemporaryDirectory(prefix='casas-negative-') as d:
 d=Path(d)
 cases=[
  ('row8-domain',R/'new-results/check_row8_seven_term.py','(8, 9), (8, 8)','(8, 9), (8, 9)'),
  ('quadratic-discriminant',R/'research/next-stage/last-four/quadratic/A/check_arithmetic.py','require(3 not in','require(4 not in'),
  ('row2-final-sign',R/'research/next-stage/last-four/quadratic/A/check_arithmetic.py','(9+14+8*4+16*16)%17==5','(9+14+8*4+16*16)%17==6'),
 ]
 for name,path,old,new in cases:
  text=path.read_text();require(text.count(old)==1,'Mutation selector is not unique: '+name)
  target=d/(name+'.py');target.write_text(text.replace(old,new))
  for mode in ([],['-O']):
   r=subprocess.run([sys.executable,'-B']+mode+[str(target)],capture_output=True,text=True)
   require(r.returncode!=0 and ('ValueError' in r.stderr or 'RuntimeError' in r.stderr),'Mutation accepted: '+name)
   results.append({'mutation':name,'optimized':bool(mode),'status':'REJECTED','stderrSHA256':hashlib.sha256(r.stderr.encode()).hexdigest()})
 # The census must reject an incomplete support inventory independently of its arithmetic.
 inventory=json.loads((R/'evidence/full/support_frontier/inventory.json').read_text())
 inventory['finalSurvivors']=[s for s in inventory['finalSurvivors'] if s!=[2,3,4,10,12,19]]
 target=d/'inventory.json';target.write_text(json.dumps(inventory))
 for mode in ([],['-O']):
  r=subprocess.run([sys.executable,'-B']+mode+[str(R/'new-results/check_row8_seven_term.py'),'--inventory',str(target)],capture_output=True,text=True)
  require(r.returncode!=0 and 'inventory differs' in r.stderr,'Incomplete inventory accepted')
  results.append({'mutation':'missing-support','optimized':bool(mode),'status':'REJECTED'})
source=(R/'replay_new.py').read_text()
require("'../../new-results/check_row8_seven_term.py'" in source,'Primary replay omits row8 dependency')
require("for optimized in (False, True)" in source,'Both modes not advertised')
require("'omitted': omitted" in (R/'replay.py').read_text(),'Missing explicit omission reporting')
print(json.dumps({'status':'PASS','controls':results,'scope':'Eight bounded mutation executions and runner contract checks; not full proof verification.'},indent=2))
