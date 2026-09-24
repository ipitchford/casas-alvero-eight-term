#!/usr/bin/env python3
"""Short option/guard tests; no m6 census (the native smoke is one existing three-coefficient system)."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import argparse
import contextlib
import importlib.util
import io
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'evidence/full/collective17/exclusions'
sys.path.insert(0,str(BASE))
from native_options import compiler_argv, positive_seconds


def require(value, explanation):
    if not value:
        raise ValueError(explanation)


def load(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    tests=[]
    for invalid in ('nan','inf','-inf','0','-1'):
        try:
            positive_seconds(invalid)
        except argparse.ArgumentTypeError:
            pass
        else:
            raise ValueError('unsafe timeout accepted: '+invalid)
    require(compiler_argv('"/compiler with spaces" --literal ";touch"')==
            ['/compiler with spaces','--literal',';touch'],'compiler argv parsing')
    with patch.dict(os.environ,{'CXX':'c++ -DMOCK=1'}):
        require(compiler_argv()==['c++','-DMOCK=1'],'CXX inheritance')
    tests.append('finite positive guards; quoted compiler argv and CXX inheritance')

    root=load('portable_runner',ROOT/'replay.py')
    with tempfile.TemporaryDirectory(prefix='casas-portability-options-') as tmp:
        calls=[]
        def fake_execute(command,cwd,timeout,log):
            calls.append((command,timeout))
            return {'status':'PASS','scope':'MOCK: argument propagation only'}
        for full in (False,True):
            calls.clear()
            argv=['replay.py','--output',str(Path(tmp)/str(full)),
                  '--cxx','custom-cxx -DTEST=1','--timeout-scale','2',
                  '--native-timeout','5','--compile-timeout','3','--check-timeout','9']
            if full: argv+=['--include-m6']
            with patch.object(sys,'argv',argv),patch.object(root,'verify_manifest',return_value=0),\
                 patch.object(root,'execute',side_effect=fake_execute),contextlib.redirect_stdout(io.StringIO()):
                root.main()
            for command,wall in calls:
                require(wall==9,'outer override not propagated')
                if command[2].endswith('/exclusions/check_batch.py') or (full and command[2].endswith('/batch-m6/check_batch.py')):
                    require(command[command.index('--native-timeout')+1]=='5.0','native override')
                    require(command[command.index('--compile-timeout')+1]=='3.0','compile override')
                    require(command[command.index('--cxx')+1]=='custom-cxx -DTEST=1','CXX CLI override')
                if command[2].endswith('/batch-m6/check_batch.py'):
                    require(('--rerun-native' in command)==full,'default unexpectedly reruns m6')
                    if not full: require('--cxx' not in command,'saved m6 needs no compiler')
        args=SimpleNamespace(check_timeout=None,compile_timeout=60,native_timeout=None,timeout_scale=2)
        require(root.configured_native(args,240)==480 and root.configured_outer(args,300,480)==600,'scaled defaults')
        args.native_timeout=1000
        require(root.configured_outer(args,300,1000)>=1180,'automatic outer headroom')
    tests.append('top runner propagation, scaled defaults, explicit headroom and saved-only m6 default (mocked checks)')
    with tempfile.TemporaryDirectory(prefix='casas-portability-outer-') as tmp:
        receipt=root.execute([sys.executable,'-c','import time; time.sleep(2)'],
                             Path(tmp),0.03,Path(tmp)/'timeout.log')
        require(receipt['status']=='TIMEOUT' and receipt['exitCode']!=0,'outer deadline did not stop checker')
    tests.append('real outer process-group timeout on a short sleeping checker')
    with tempfile.TemporaryDirectory(prefix='casas-portability-race-') as tmp:
        class FinishedAtDeadline:
            pid=12345
            waits=0
            def wait(self,timeout=None):
                self.waits+=1
                if self.waits==1:
                    raise subprocess.TimeoutExpired('mock checker',timeout)
                return 0
        with patch.object(root.subprocess,'Popen',return_value=FinishedAtDeadline()),\
             patch.object(root.os,'killpg',side_effect=ProcessLookupError):
            receipt=root.execute(['mock'],Path(tmp),0.03,Path(tmp)/'race.log')
        require(receipt['status']=='TIMEOUT','deadline/exit race lost its timeout receipt')
    tests.append('benign process-exit/deadline race emits a TIMEOUT receipt (mocked process)')

    m6=load('portable_m6',BASE/'batch-m6/check_batch.py')
    args=SimpleNamespace(cxx='mock-cxx',compile_timeout=7,native_timeout=11,native_wrapper_timeout=None)
    def fake_worker(command,**kwargs):
        require('timeout' not in kwargs,'competing worker timeout could orphan native child')
        require(command[command.index('--compile-timeout')+1]=='7','worker compile timeout')
        require(command[command.index('--native-timeout')+1]=='11','worker native timeout')
        require(command[command.index('--cxx')+1]=='mock-cxx','worker CXX')
        scratch=Path(command[command.index('--output')+1])
        (scratch/'replay.log').write_bytes(b'fixture\n')
        (scratch/'replay-process.json').write_text(json.dumps({'status':'COMPLETE','returncode':0,
            'elapsedSeconds':0,'outputSHA256':'mock','compilerArgv':['mock-cxx']}))
    with patch.object(m6.subprocess,'run',side_effect=fake_worker):
        require(m6.run_fresh_native(args,b'fixture\n')['status']=='PASS','worker dispatch')
    tests.append('m6 checker-to-worker compiler and guard propagation (mocked worker)')

    with tempfile.TemporaryDirectory(prefix='casas-portability-native-') as tmp:
        tmp=Path(tmp); worker=tmp/'batch-m6';worker.mkdir()
        shutil.copy2(BASE/'native_options.py',tmp/'native_options.py')
        for name in ('run_native.py','replay_residues.cpp'):
            shutil.copy2(BASE/'batch-m6'/name,worker/name)
        words=(BASE/'batch-m6/native-input.txt').read_text().split()
        words[2]='1'  # One already-checked three-coefficient system: only 17^3 markings.
        (worker/'native-input.txt').write_text(' '.join(words[:3+11+170]+['3','4','10','13'])+'\n')
        smoke=tmp/'small-smoke-output'
        command=[sys.executable,'-B',str(worker/'run_native.py'),'--role','replay',
                 '--output',str(smoke),'--native-timeout','5','--compile-timeout','30']
        done=subprocess.run(command,capture_output=True,text=True,timeout=40,check=True)
        receipt=json.loads(done.stdout)
        require(receipt['status']=='COMPLETE' and receipt['wallGuardSeconds']==5,'native smoke status')
        lines=(smoke/'replay.log').read_text().splitlines()
        require(lines[0]=='DOMAIN_PASS 17 10' and lines[1].startswith('CASE 0 3 4913 ') and lines[-1]=='ALL_PASS','small-smoke scope')
        tests.append('real C++17 compilation, full field validation and 4913 markings of one existing small system')

        fake=tmp/'compiler with spaces.py'
        fake.write_text('import pathlib,sys\n'
                       'p=pathlib.Path(sys.argv[sys.argv.index("-o")+1])\n'
                       'p.write_text("#!"+sys.executable+"\\nimport time\\ntime.sleep(2)\\n")\n'
                       'p.chmod(0o755)\n')
        timeout_dir=tmp/'timeout-output'
        timeout_command=[sys.executable,'-B',str(worker/'run_native.py'),'--role','replay',
                         '--output',str(timeout_dir),'--native-timeout','0.03',
                         '--cxx',shlex.join([sys.executable,str(fake)])]
        timed=subprocess.run(timeout_command,capture_output=True,text=True,timeout=10)
        require(timed.returncode==124,'timeout was reported as success')
        timed_receipt=json.loads((timeout_dir/'replay-process.json').read_text())
        require(timed_receipt['status']=='TIMEOUT' and timed_receipt['wallGuardSeconds']==0.03,'timeout receipt')
        before=(timeout_dir/'replay-process.json').read_bytes()
        refused=subprocess.run(timeout_command,capture_output=True,text=True,timeout=10)
        require(refused.returncode!=0 and before==(timeout_dir/'replay-process.json').read_bytes(),'receipt overwrite')
        tests.append('quoted compiler path, short timeout exit/receipt and refusal to overwrite historical execution files')
    print(json.dumps({'status':'PASS','scope':'Portability only; no full m6 enumeration or proof extension.',
                      'checks':tests},indent=2))


if __name__=='__main__':main()
