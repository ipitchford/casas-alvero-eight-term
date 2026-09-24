"""Compute a divided row-4 obstruction and exhaust its smallest support.

Producer only. The mathematical divided-identity proof is separate.
"""
from math import comb
from itertools import product
from pathlib import Path
import json
import flint

BASE = Path(__file__).resolve().parent
PRIME = 17
ACTIVE = (4, 10, 12)


def need(ok, why):
    if not ok:
        raise ArithmeticError(why)


def pair_add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def pair_scale(a, c):
    return (a[0]*c, a[1]*c)


def pair_mul(a, b):
    # alpha^2=-3alpha-3 over Z, not only in the residue field.
    return (a[0]*b[0]-3*a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]-3*a[1]*b[1])


def pair_power(k):
    a = (1, 0)
    for _ in range(k):
        a = pair_mul(a, (0, 1))
    return a


def family_directions():
    """Ordinary coefficient vectors for F(u,6;X)."""
    s = 6
    a18 = -s**18 + 153*s**16
    f = [0]*21
    f[20], f[18], f[2], f[1] = 1, -190, 190*a18, 189-190*a18
    out = [f]
    for j in range(4, 17):
        b = comb(18, j)*s**(18-j)
        f = [0]*21
        f[20-j] = comb(20, j)
        f[2] = -190*b
        f[1] = 190*b-comb(20, j)
        out.append(f)
    return out


def divided_coefficients():
    out = []
    for f in family_directions():
        v = (0, 0)
        for k, c in enumerate(f):
            v = pair_add(v, pair_scale(pair_power(k), c))
        phi = sum(c*6**k for k, c in enumerate(f))
        need(phi % 17 == 0 and all(t % 17 == 0 for t in v),
             'division not integral')
        # S=6+17 sigma, sigma=-[F(u,6;6)/17]/9 mod17.
        sigma = -(phi//17)*pow(9, -1, 17) % 17
        # Partial_s F mod17 = X-X^2 = 3+4alpha at the quadratic root.
        out.append([(v[0]//17+3*sigma) % 17,
                    (v[1]//17+4*sigma) % 17])
    return out


def main():
    modulus = [2, 0, 4, 3, 1]
    K = flint.fq_default_ctx(modulus=flint.fmpz_mod_poly_ctx(17)(modulus), var='t')
    polys = flint.fq_default_poly_ctx(K)
    X = polys.gen()
    h = X**20-3*X**18+11*X**2+8*X
    _, factors = h.factor()

    def vec(x):
        v = [int(a) for a in x.to_list()]
        return v+[0]*(4-len(v))

    need(all(f.degree() == 1 for f, _ in factors), 'incomplete root field')
    roots = sorted([-f[0]/f[1] for f, _ in factors], key=vec)
    need(len(roots) == 18, 'distinct residue root count')
    nonzero = [r for r in roots if not r.is_zero()]
    doubles = [r for r in roots if (r*r+3*r+3).is_zero()]
    need(len(nonzero) == 17 and len(doubles) == 2, 'marked root domain')
    pair_coeffs = divided_coefficients()
    powers = [[r**k for k in range(17)] for r in nonzero]
    records = []
    counts = {'base_oriented_markings': 0, 'after_critical_division': 0,
              'signed_markings_after_division': 0,
              'signed_markings_after_quadratic_first_jet': 0}
    for alpha in doubles:
        beta = -3-alpha
        weights = [K(a)+K(b)*alpha for a, b in pair_coeffs]
        other = [K(a)+K(b)*beta for a, b in pair_coeffs]
        for choices in product(range(17), repeat=len(ACTIVE)):
            counts['base_oriented_markings'] += 1
            u = {}
            for j, index in zip(ACTIVE, choices):
                rp = powers[index]
                u[j] = -rp[j]+comb(j, 2)*rp[j-2]
                for i in ACTIVE:
                    if i < j:
                        u[j] -= comb(j, i)*u[i]*rp[j-i]
            ell = weights[0]+sum((weights[j-3]*u[j] for j in ACTIVE), K(0))
            if not ell.is_zero():
                continue
            counts['after_critical_division'] += 1
            ell_beta = other[0]+sum((other[j-3]*u[j] for j in ACTIVE), K(0))
            positions = [j for j, index in zip(ACTIVE, choices) if nonzero[index] == beta]
            survivors = []
            for signs in product((-1, 1), repeat=len(positions)):
                eps = dict(zip(positions, signs))
                counts['signed_markings_after_division'] += 1
                tangent = {}
                for j, index in zip(ACTIVE, choices):
                    rp = powers[index]
                    gjprev = rp[j-1]-comb(j-1, 2)*rp[j-3]
                    for i in ACTIVE:
                        if i < j:
                            gjprev += comb(j-1, i)*u[i]*rp[j-1-i]
                    tangent[j] = -j*eps.get(j, 0)*gjprev
                    for i in ACTIVE:
                        if i < j:
                            tangent[j] -= comb(j, i)*tangent[i]*rp[j-i]
                jet = sum((weights[j-3]*tangent[j] for j in ACTIVE), K(0))
                # If ell_beta!=0 then v(z)=1/2. An extra obstruction with
                # constant divisible by17 and unit z coefficient cannot vanish.
                if not ell_beta.is_zero() and not jet.is_zero():
                    continue
                counts['signed_markings_after_quadratic_first_jet'] += 1
                survivors.append({'signs': list(signs), 'linear_jet': vec(jet)})
            records.append({'alpha': vec(alpha), 'witnesses': [vec(nonzero[i]) for i in choices],
                            'u': {str(j): vec(u[j]) for j in ACTIVE},
                            'other_critical_value': vec(ell_beta),
                            'beta_witness_degrees': positions, 'remaining_signs': survivors})
    need(counts['base_oriented_markings'] == 2*17**len(ACTIVE), 'incomplete enumeration')
    output = {'status': 'COMPLETE_FINITE_ENUMERATION',
              'scope': 'One canonical row4 support; full degree20 and row4 remain unproved.',
              'support': [2, *ACTIVE, 18, 19], 'field_modulus': modulus,
              'nonzero_root_domain': list(map(vec, nonzero)),
              'ell_affine_pair_coefficients': pair_coeffs, 'counts': counts,
              'first_division_survivors': records}
    destination = BASE/'row4-first-obstruction.json'
    destination.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'file': str(destination), 'counts': counts}))


if __name__ == '__main__':
    main()
