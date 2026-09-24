"""Bounded higher-prime pilot; a partial basis is never an exclusion proof."""
from math import comb
from pathlib import Path
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
label = sys.argv[1]
supports = {'A':[3,4,10,18,19], 'C':[4,5,10,17,19]}
S = supports[label]
out = root/'prime31'/label
out.mkdir(parents=True, exist_ok=True)
variables = ['u','v','w','z']
witnesses = ['1']+variables
lines = ['ring r=31,(u,v,w,z),dp;', 'int degBound=40;']
for i,m in enumerate(S):
    witness = witnesses[i]
    rhs = '-('+witness+')^'+str(m)
    for j,k in enumerate(S[:i]):
        rhs += f'-{comb(m,k)}*a{j}*({witness})^{m-k}'
    lines.append(f'poly a{i}={rhs};')
equations=[]
for i,x in enumerate(witnesses):
    expr=f'({x})^20'+''.join(f'+{comb(20,m)}*a{j}*({x})^{20-m}' for j,m in enumerate(S))
    lines.append(f'poly E{i}={expr};')
    equations.append(f'E{i}')
lines += ['ideal I='+','.join(equations)+';', 'int started=timer;',
          'ideal G=std(I);', 'print("elapsed_seconds");', 'print(timer-started);',
          'print("basis_size");', 'print(size(G));',
          'if (size(G)==1 && G[1]==1) {print("UNIT");} else {print("INCONCLUSIVE_BOUNDED_BASIS");}',
          'quit;']
script=out/'normalized.sing'
script.write_text('\n'.join(lines)+'\n')
try:
    result=subprocess.run(['/opt/homebrew/bin/Singular','-q',str(script)],
                          capture_output=True,text=True,timeout=110)
    log=result.stdout+'\n'+result.stderr
    status='UNIT_NEEDS_CERTIFICATE_AND_TRANSFER' if '\nUNIT\n' in '\n'+log else 'INCONCLUSIVE'
    if result.returncode:
        status='TOOL_ERROR'
except subprocess.TimeoutExpired as error:
    log=(error.stdout or b'').decode()+'\nTIMEOUT_110_SECONDS\n'
    status='TIME_LIMIT_INCONCLUSIVE'
(out/'pilot.log').write_text(log)
record={'support':S,'prime':31,'chart':'highest displayed coefficient nonzero',
        'degree_bound':40,'timeout_seconds':110,'status':status,
        'limitation':'Neither a partial basis nor a modular unit alone proves the characteristic-zero family excluded.'}
(out/'receipt.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
