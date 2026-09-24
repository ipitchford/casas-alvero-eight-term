"""Independent prime-field Sylvester checks for Family B's saved resultants.

This supplements, rather than replaces, the complete extension-field
interpolation replay. It imports no producer arithmetic.
"""
import json
from pathlib import Path

P = 13


def evaluate(coefficients, x):
    return sum(c * pow(x, i, P) for i, c in enumerate(coefficients)) % P


def determinant(matrix):
    a = [[c % P for c in row] for row in matrix]
    answer = 1
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            answer = -answer % P
        value = a[i][i]
        answer = answer * value % P
        inverse = pow(value, -1, P)
        for j in range(i + 1, len(a)):
            factor = a[j][i] * inverse % P
            for k in range(i + 1, len(a)):
                a[j][k] = (a[j][k] - factor * a[i][k]) % P
            a[j][i] = 0
    return answer


def resultant(f, g):
    m, n = len(f) - 1, len(g) - 1
    fd, gd = f[::-1], g[::-1]
    matrix = [[0] * i + fd + [0] * (n - i - 1) for i in range(n)]
    matrix += [[0] * i + gd + [0] * (m - i - 1) for i in range(m)]
    return determinant(matrix)


def main():
    source = Path(__file__).parent.parent / 'B' / 'certificate.json'
    saved = json.loads(source.read_text())
    checked = []
    # At u=1 the rational coefficient is defined after cancelling u-1;
    # its numerator equals the derivative of the original numerator there.
    for u in range(12):
        q = (u + 1) % P
        b = (-9 * pow(u, 16, P) - 4 * pow(u, 13, P)) % P
        numerator = (5 + b - 5 * pow(u, 19, P)) % P
        if u == 1:
            cn = (-9 * 16 - 4 * 13 - 5 * 19) % P
        else:
            cn = numerator * pow(u - 1, -1, P) % P
        dn = (q * (-5 - b) - cn) % P
        f, g3, g1 = [0] * 20, [0] * 18, [0] * 20
        for i, coefficient in {19:q, 16:4*q, 3:q*b, 2:cn, 0:dn}.items():
            f[i] = coefficient % P
        for i, coefficient in {17:9*q, 14:3*q, 1:4*q*b, 0:cn}.items():
            g3[i] = coefficient % P
        for i, coefficient in {19:7*q, 16:3*q, 3:4*q*b, 2:3*cn, 0:dn}.items():
            g1[i] = coefficient % P
        computed = [resultant(f, g3), resultant(f, g1)]
        expected = [evaluate(saved['R3'], u), evaluate(saved['R1'], u)]
        if computed != expected:
            raise RuntimeError(f'Independent Sylvester mismatch at {u}: {computed} != {expected}')
        checked.append({'u':u, 'resultants':computed})
    print(json.dumps({'status':'PASS', 'method':'Direct prime-field Sylvester determinants, independent of producer arithmetic',
                      'points':checked, 'scope':'12 base-field spot checks; complete 685-point interpolation replay separately audited'}, indent=2))


if __name__ == '__main__':
    main()
