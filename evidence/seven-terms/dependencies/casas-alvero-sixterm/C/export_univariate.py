"""Export C's two univariate necessary-condition certificates.

Uses B's existing standard-library univariate implementation explicitly.
"""
from pathlib import Path
import importlib.util
import json
import hashlib

HERE=Path(__file__).resolve().parent
source=HERE.parent/'B'/'export_certificate.py'
spec=importlib.util.spec_from_file_location('b_export_helpers',source)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
lines=(HERE/'seed-univariate.log').read_text().splitlines()
def get(tag):
    return m.parse(lines[lines.index(tag)+1].replace('*','').replace('^',''))
b=[0,1,0,0,0,5]
N=[0]*20
N[0],N[1],N[5],N[15],N[19]=5,1,5,8,7
cn,rem=m.divide(N,[12,1])
if rem:raise ValueError('Nonexact cancellation')
dn=m.add(m.mul([1,1],m.add([8],m.scale(b,-1))),m.scale(cn,-1))
charts={}
for label,c,d in [('GENERIC',cn,dn),('SPECIAL',[0,1],[2,12])]:
    R3,R1=get(label+'_R3'),get(label+'_R1')
    gcd,U,V=m.bezout(m.mul(c,R3),m.mul(d,R1))
    if m.add(m.mul(U,m.mul(c,R3)),m.mul(V,m.mul(d,R1)))!=gcd:
        raise ValueError('Bezout identity failed')
    if gcd!=get(label+'_GCD'):raise ValueError('Gcd disagrees with Singular')
    charts[label.lower()]={'R3':R3,'R1':R1,'gcd':gcd,'U':U,'V':V}
data={'field':13,'coefficientOrder':'ascending powers','charts':charts,
      'sharedImplementation':str(source),
      'sharedImplementationSha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(HERE/'univariate-certificate.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
print(json.dumps({k:{'R3degree':len(v['R3'])-1,'R1degree':len(v['R1'])-1,'gcdDegree':len(v['gcd'])-1,
                    'BezoutDegrees':[len(v['U'])-1,len(v['V'])-1]} for k,v in charts.items()},indent=2))
