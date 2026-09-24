"""Run one local Singular source with a strict process-group deadline."""
from pathlib import Path
from time import perf_counter
import json
import os
import signal
import subprocess
import sys

base=Path(__file__).resolve().parent
name=sys.argv[1]
cap=float(sys.argv[2]) if len(sys.argv)>2 else 115
if Path(name).name!=name or not name.endswith('.sing'):raise ValueError(name)
start=perf_counter()
with (base/(name+'.log')).open('w') as log:
    proc=subprocess.Popen(['/opt/homebrew/bin/Singular','-q',str(base/name)],stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    try:status=proc.wait(timeout=cap)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid,signal.SIGTERM)
        try:proc.wait(timeout=2)
        except subprocess.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
        status='TIMEOUT'
result={'source':name,'limitSeconds':cap,'elapsedSeconds':perf_counter()-start,'status':status}
(base/(name+'.receipt.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
