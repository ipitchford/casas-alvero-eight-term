"""Export exact integer resultant arrays without rerunning the producer."""
from pathlib import Path
import hashlib
import json
import re

base=Path(__file__).resolve().parent
source=base/'collision.sing.log'
lines=source.read_text().splitlines()


def parse(expression):
    coefficients={}
    for term in re.findall(r'[+-]?[^+-]+',expression):
        if 'u' in term:
            coefficient,exponent=term.split('u')
            coefficient=1 if coefficient in ('','+') else -1 if coefficient=='-' else int(coefficient)
            exponent=int(exponent or '1')
        else:coefficient,exponent=int(term),0
        if exponent in coefficients:raise ValueError('Repeated exponent')
        coefficients[exponent]=coefficient
    return [coefficients.get(i,0) for i in range(max(coefficients)+1)]


data={'coefficientOrder':'ascending powers of u',
      'R10':parse(lines[lines.index('R10')+1]),
      'R1':parse(lines[lines.index('R1')+1]),
      'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(base/'certificate.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
print(json.dumps({'resultantDegrees':[len(data['R10'])-1,len(data['R1'])-1],
                  'certificateSha256':hashlib.sha256((base/'certificate.json').read_bytes()).hexdigest()}))
