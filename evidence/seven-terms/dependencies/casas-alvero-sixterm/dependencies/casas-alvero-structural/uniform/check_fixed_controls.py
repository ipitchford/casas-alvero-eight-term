#!/usr/bin/env python3
"""Independent standard-library positive controls for the root's fixed H,C."""
from pathlib import Path
import hashlib
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def evaluate(coefficients, x, p):
    result = 0
    for coefficient in coefficients:
        result = (result*x+coefficient) % p
    return result


def decimal_mod(text, p):
    text = text.strip()
    sign = -1 if text.startswith('-') else 1
    text = text.lstrip('+-')
    require(text.isdigit(), 'Resultant is not a decimal integer')
    result = 0
    for character in text:
        result = (10*result+int(character)) % p
    return sign*result % p


root = Path(__file__).resolve().parent.parent
path = root/'fixed-polynomial.json'
coefficients = json.loads(path.read_text())['H_coefficients_high_first']
degree = len(coefficients)-1
require(degree == 72, 'Unexpected fixed polynomial degree')
resultant_text = (root/'resultant-integer.txt').read_text()
records = []
for p, v, w in [(19, 2, 13), (23, 1, 5),
                 (87169343, 1, 35**2*pow(9*17, -1, 87169343) % 87169343)]:
    z = (w*pow(v, -1, p))**2 % p
    psi = 289*pow(pow(z, 6, p), -1, p) % p
    Hvalue = evaluate(coefficients, z, p)
    Cvalue = pow(z, 6*degree, p)*evaluate(coefficients, psi, p) % p
    require(psi == z and Hvalue == 0 and Cvalue == 0, 'Positive control failed')
    require(decimal_mod(resultant_text, p) == 0, 'Resultant misses a known example prime')
    records.append({'prime': p, 'z': z, 'psi': psi, 'H': Hvalue, 'C': Cvalue,
                    'resultantModuloPrime': 0})
print(json.dumps({'status': 'PASS', 'fixedPolynomialSha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                  'controls': records,
                  'scope': 'Positive controls only; not an independent resultant reconstruction.'}, indent=2))
