"""Independent arithmetic replay of de Frutos Marin's support tests.

Primary source: 2013 thesis, Proposition 3.5.5 and (2.11).
This checks formula aliasing and the reported degree-20 support applications.
It does not certify arbitrary Casas-Alvero polynomials or historical novelty.
"""

import json
from math import comb, gcd
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def boundary_integer(n, r, s):
    B, D, C = comb(n, r), comb(n, s), comb(n - r, s - r)
    g = gcd(r, s)
    u, v = (s - r) // g, r // g
    return B ** (u + v) * (C - 1) ** u * (D - C) ** v - (B - 1) ** v * (D - 1) ** (u + v)


def thesis_determinant(n, r, s):
    i, j = n - s, n - r
    a, b, c = comb(n, i), comb(n, j), comb(n - i, n - j)
    g = gcd(n - j, j - i)
    rho, sigma = (n - j) // g, (j - i) // g
    bracket = a ** rho * (b - c) ** rho * (b - a * c) ** sigma - (-1) ** sigma * (a - 1) ** (rho + sigma) * (b - 1) ** rho
    return (-1) ** (rho * sigma) * bracket


def inspect_support(support):
    rows = []
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        visible = [m for m in support if comb(20, m) % p]
        residues = [comb(20, m) % p for m in visible]
        exclude = not visible
        N_mod_p = None
        if len(visible) == 1:
            exclude = residues[0] != 1
        elif len(visible) == 2:
            N_mod_p = boundary_integer(20, *visible) % p
            exclude = 1 not in residues and N_mod_p != 0
        rows.append(dict(p=p, visible=visible, binomial_residues=residues,
                         N_mod_p=N_mod_p, excluded=exclude))
    return dict(support=support, checks=rows,
                exclusion_primes=[r['p'] for r in rows if r['excluded']])


def main():
    aliases_checked = 0
    for n in range(4, 31):
        for r in range(2, n - 1):
            for s in range(r + 1, n):
                g = gcd(r, s)
                u, v = (s - r) // g, r // g
                require(
                    thesis_determinant(n, r, s) == (-1) ** (u * v + u) * boundary_integer(n, r, s),
                    f'Formula alias failed at n={n}, r={r}, s={s}',
                )
                aliases_checked += 1
    supports = [
        [4, 10, 17, 19], [4, 8, 9, 10, 11, 12, 17, 19],
        [2, 4, 5, 10, 19], [2, 4, 10, 12, 19],
        [2, 4, 10, 16, 19], [2, 10, 14, 16, 19],
        [3, 4, 10, 18, 19], [3, 10, 16, 17, 19],
        [4, 5, 10, 17, 19], [8, 10, 16, 17, 19],
    ]
    rows = [inspect_support(s) for s in supports]
    require(all(not r['exclusion_primes'] for r in rows[:2]),
            'Unexpected old-criterion exclusion of a frozen support')
    require(all(r['exclusion_primes'] == [17] for r in rows[2:6]),
            'Four claimed p=17 support exclusions did not replay')
    require(all(not r['exclusion_primes'] for r in rows[6:]),
            'Unexpected old-criterion exclusion of a remaining six-term support')
    result = dict(status='PASS', formula_alias_checks=aliases_checked,
                  scope='Arithmetic checks only; all relevant primes for reducing a >=3-element degree-20 support to <=2 are <=19.',
                  support_results=rows)
    Path(__file__).with_name('known-criteria-results.json').write_text(json.dumps(result, indent=2) + '\n')
    print('PASS:', aliases_checked, 'formula aliases; 10 support checks; four additional old-criterion exclusions')


if __name__ == '__main__':
    main()
