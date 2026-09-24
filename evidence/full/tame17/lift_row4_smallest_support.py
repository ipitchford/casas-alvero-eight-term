"""Lift the unique unramified coefficient scenario for row4 support 4,10,12.

The two orientations of the H1 root are conjugate over Q17.  This producer
checks the critical value at one root of Z^2+3Z+3; conjugation handles both.
"""
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def need(ok, why):
    if not ok:
        raise ArithmeticError(why)


def data(t, s, modulus):
    a4 = (-pow(t, 4, modulus)+6*pow(t, 2, modulus)) % modulus
    a10 = (44-210*a4) % modulus
    a12 = (-pow(s, 12, modulus)+66*pow(s, 10, modulus)
           -495*a4*pow(s, 8, modulus)-66*a10*pow(s, 2, modulus)) % modulus
    u = {4: a4, 10: a10, 12: a12}
    a18 = -pow(s, 18, modulus)+153*pow(s, 16, modulus)
    a18 -= sum(comb(18, j)*v*pow(s, 18-j, modulus) for j, v in u.items())
    a18 %= modulus
    f = [0]*21
    f[20], f[18], f[2], f[1] = 1, -190, 190*a18, 189-190*a18
    for j, v in u.items():
        f[20-j] = comb(20, j)*v
        f[1] -= comb(20, j)*v
    return [v % modulus for v in f], u


def evaluate(f, x, modulus, derivative=0):
    out = 0
    for i in range(len(f)-1, derivative-1, -1):
        out = (out*x+comb(i, derivative)*f[i]) % modulus
    return out


def add(a, b, m):
    return ((a[0]+b[0]) % m, (a[1]+b[1]) % m)


def mul(a, b, m):
    return ((a[0]*b[0]-3*a[1]*b[1]) % m,
            (a[0]*b[1]+a[1]*b[0]-3*a[1]*b[1]) % m)


def pair_evaluate(f, x, modulus, derivative=0):
    out = (0, 0)
    for i in range(len(f)-1, derivative-1, -1):
        out = add(mul(out, x, modulus), (comb(i, derivative)*f[i], 0), modulus)
    return out


def main():
    t, s = 10, 6
    stages = []
    for k in (1, 2):
        pk, modulus = 17**k, 17**(k+1)
        f, _ = data(t, s, modulus)
        ft, fs = evaluate(f, t, modulus), evaluate(f, s, modulus)
        need(ft % pk == fs % pk == 0, 'root lift is not at previous precision')
        ds = -(fs//pk)*pow(9, -1, 17) % 17
        dt = -((ft//pk)+12*ds)*pow(2, -1, 17) % 17
        t, s = t+pk*dt, s+pk*ds
        f, u = data(t, s, modulus)
        need(evaluate(f, t, modulus) == evaluate(f, s, modulus) == 0,
             'root Newton correction failed')
        need(evaluate(f, 1, modulus) == evaluate(f, s, modulus, 2) == 0,
             'fixed visible equations failed')
        stages.append({'precision': k+1, 't': t, 's': s, 'u': u})
    modulus = 17**3
    f, u = data(t, s, modulus)
    r = (0, 1)
    for k in (1, 2):
        pk = 17**k
        submodulus = pk*17
        residual = pair_evaluate(f, r, submodulus, 1)
        need(all(c % pk == 0 for c in residual), 'critical lift precision')
        # Ordinary f'' is 6 at either residual quadratic root.
        delta = tuple(-(c//pk)*pow(6, -1, 17) % 17 for c in residual)
        r = add(r, tuple(pk*c for c in delta), submodulus)
        need(pair_evaluate(f, r, submodulus, 1) == (0, 0), 'critical correction failed')
    critical = pair_evaluate(f, r, modulus)
    need(all(c % (17**2) == 0 for c in critical), 'first divided obstruction did not vanish')
    nonzero = any(c for c in critical)
    result = {'status': 'EXCLUDED' if nonzero else 'UNRESOLVED_AT_THIS_PRECISION',
              'scope': 'Row4 canonical middle support {4,10,12} only.',
              'modulus': modulus, 'unramified_quadratic': [3, 3, 1],
              'lift_stages': stages, 'ordinary_coefficients': f,
              'critical_root': r, 'critical_value': critical,
              'critical_value_divided_by_17_squared': [c//(17**2) for c in critical],
              'critical_derivative': pair_evaluate(f, r, modulus, 1)}
    (HERE/'row4-smallest-support-lift.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
