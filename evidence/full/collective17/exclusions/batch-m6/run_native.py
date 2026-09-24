"""One native execution with an external wall guard and an exclusive lock."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import fcntl
import json
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from native_options import add_native_options, compiler_argv


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--role',choices=['producer','continuation','replay'],required=True)
    parser.add_argument('--output', type=Path, required=True,
                        help='scratch output directory; existing role receipts are never overwritten')
    add_native_options(parser, native_default=None)
    args=parser.parse_args()
    wall=args.native_timeout if args.native_timeout is not None else {'producer':180,'continuation':60,'replay':240}[args.role]
    input_path=HERE/('continuation-input.txt' if args.role=='continuation' else 'native-input.txt')
    output_dir=args.output.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    compiler=compiler_argv(args.cxx)
    with (output_dir/'RUN.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        destination=output_dir/(args.role+'-process.json')
        if any((output_dir/(args.role+suffix)).exists() for suffix in ('-process.json','.log','-progress.log')):
            parser.error('refusing to overwrite an existing execution receipt or log')
        binary=output_dir/'replay_residues'
        subprocess.run(compiler+['-std=c++17','-O2',str(HERE/'replay_residues.cpp'),
                        '-o',str(binary)],capture_output=True,text=True,timeout=args.compile_timeout,check=True)
        receipt={'role':args.role,'startedUTC':datetime.now(timezone.utc).isoformat(),
                 'wallGuardSeconds':wall,'status':'RUNNING',
                 'compilerArgv':compiler,'compileWallLimitSeconds':args.compile_timeout,
                 'sourceSHA256':sha256((HERE/'replay_residues.cpp').read_bytes()).hexdigest(),
                 'binarySHA256':sha256(binary.read_bytes()).hexdigest(),
                 'inputSHA256':sha256(input_path.read_bytes()).hexdigest()}
        destination.write_text(json.dumps(receipt,indent=2)+'\n')
        start=time.monotonic()
        with (output_dir/(args.role+'.log')).open('w') as output, (output_dir/(args.role+'-progress.log')).open('w') as progress:
            try:
                result=subprocess.run([str(binary),str(input_path)],
                                      stdout=output,stderr=progress,timeout=wall)
                receipt['returncode']=result.returncode
                receipt['status']='COMPLETE' if result.returncode==0 else 'ERROR'
            except subprocess.TimeoutExpired:
                receipt['status']='TIMEOUT'
        receipt['elapsedSeconds']=time.monotonic()-start
        receipt['endedUTC']=datetime.now(timezone.utc).isoformat()
        receipt['outputSHA256']=sha256((output_dir/(args.role+'.log')).read_bytes()).hexdigest()
        destination.write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps(receipt),flush=True)
        if receipt['status']!='COMPLETE':
            raise SystemExit(124 if receipt['status']=='TIMEOUT' else 1)


if __name__=='__main__':main()
