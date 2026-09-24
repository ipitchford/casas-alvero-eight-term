"""Run one named Singular file, with a bounded process-tree lifetime."""
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
from time import perf_counter

base = Path(__file__).resolve().parent
name = sys.argv[1]
limit = float(sys.argv[2]) if len(sys.argv) > 2 else 60
if Path(name).name != name or not name.endswith('.sing'):
    raise ValueError('expected one local .sing filename')
start = perf_counter()
with (base / (name + '.log')).open('w') as log:
    p = subprocess.Popen(['/opt/homebrew/bin/Singular', '-q', str(base/name)],
                         stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    try:
        status = p.wait(timeout=limit)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGTERM)
        try:
            p.wait(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)
            p.wait()
        status = 'TIMEOUT'
receipt = {'input': name, 'limitSeconds': limit,
           'elapsedSeconds': perf_counter()-start, 'status': status}
(base / (name+'.receipt.json')).write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt))
