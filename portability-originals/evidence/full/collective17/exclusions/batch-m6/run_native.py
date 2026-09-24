"""One native execution with an external wall guard and an exclusive lock."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import fcntl
import json
import subprocess
import time

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--role',choices=['producer','continuation','replay'],required=True)
    args=parser.parse_args()
    wall={'producer':180,'continuation':60,'replay':240}[args.role]
    input_path=HERE/('continuation-input.txt' if args.role=='continuation' else 'native-input.txt')
    with (HERE/'RUN.lock').open('w') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        subprocess.run(['/usr/bin/clang++','-std=c++17','-O2',str(HERE/'replay_residues.cpp'),
                        '-o',str(HERE/'replay_residues')],capture_output=True,text=True,timeout=30,check=True)
        receipt={'role':args.role,'startedUTC':datetime.now(timezone.utc).isoformat(),
                 'wallGuardSeconds':wall,'status':'RUNNING',
                 'sourceSHA256':sha256((HERE/'replay_residues.cpp').read_bytes()).hexdigest(),
                 'binarySHA256':sha256((HERE/'replay_residues').read_bytes()).hexdigest(),
                 'inputSHA256':sha256(input_path.read_bytes()).hexdigest()}
        destination=HERE/(args.role+'-process.json')
        destination.write_text(json.dumps(receipt,indent=2)+'\n')
        start=time.monotonic()
        with (HERE/(args.role+'.log')).open('w') as output, (HERE/(args.role+'-progress.log')).open('w') as progress:
            try:
                result=subprocess.run([str(HERE/'replay_residues'),str(input_path)],
                                      stdout=output,stderr=progress,timeout=wall)
                receipt['returncode']=result.returncode
                receipt['status']='COMPLETE' if result.returncode==0 else 'ERROR'
            except subprocess.TimeoutExpired:
                receipt['status']='TIMEOUT'
        receipt['elapsedSeconds']=time.monotonic()-start
        receipt['endedUTC']=datetime.now(timezone.utc).isoformat()
        receipt['outputSHA256']=sha256((HERE/(args.role+'.log')).read_bytes()).hexdigest()
        destination.write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps(receipt),flush=True)


if __name__=='__main__':main()
