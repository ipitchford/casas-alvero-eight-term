"""Export small exact determinant circuits, never expand their resultants."""
from collections import Counter
from hashlib import sha256
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'support_frontier' / 'inventory.json'
VARIABLES = list(range(4, 17))


def main():
    # Every coefficient is [constant, coefficient of u4, ..., coefficient of u16].
    f = [[0] * 14 for _ in range(21)]
    f[20][0], f[17][0], f[2][0], f[1][0] = 1, -1140, 18221, -17082
    for column, j in enumerate(VARIABLES, 1):
        c = comb(20, j)
        f[20-j][column] = c
        f[2][column] = -(19-j)*c
        f[1][column] = (18-j)*c
    # Division by (X-1)^2, calculated from highest degree downward.
    remainder = [v.copy() for v in f]
    g = [[0] * 14 for _ in range(19)]
    for degree in range(20, 1, -1):
        q = remainder[degree].copy()
        g[degree-2] = q
        for column in range(14):
            remainder[degree][column] -= q[column]
            remainder[degree-1][column] += 2*q[column]
            remainder[degree-2][column] -= q[column]
    if any(any(v) for v in remainder):
        raise ValueError('inexact double-root division')
    derivatives = {}
    for j in VARIABLES:
        q = [[0]*14 for _ in range(j+1)]
        q[j][0], q[j-3][0] = 1, -comb(j, 3)
        for i in VARIABLES:
            if i <= j:
                q[j-i][i-3] = comb(j, i)
        derivatives[str(j)] = q
    obstruction = [-8037] + [comb(19-j, 2)*(comb(20, j)//17) for j in VARIABLES]
    source_bytes = SOURCE.read_bytes()
    inventory = json.loads(source_bytes)
    supports = sorted(s for s in inventory['finalSurvivors']
                      if {3, 18, 19} <= set(s) and not {2, 17} & set(s))
    counts = Counter(len(s)-3 for s in supports)
    doc = {
        'scope': 'Exact compact presentation only; no row exclusion or norm evaluation.',
        'coefficientEncoding': {'polynomialOrder': 'ascending powers of X',
                                'affineOrder': ['constant'] + ['u'+str(j) for j in VARIABLES]},
        'f': f, 'g_f_divided_by_X_minus_1_squared': g,
        'g_divided_by_X': g[1:], 'G': derivatives, 'T': obstruction,
        'normCircuit': {
            'companionConvention': 'For q=X^d+sum(q[k]*X^k,k<d), C[k+1,k]=1 and C[k,d-1]=-q[k]; all other entries zero.',
            'fullRelations': 'R_j=det(G_j(C_g)), j=4,...,16; impose T=0 separately.',
            'fullCompanionDimension': 18,
            'canonicalRelations': 'For active J, set inactive u_i=0, and use det(G_j(C_(g/X))) for j in J; impose T=0 separately.',
            'canonicalCompanionDimension': 17,
            'resultantFactor': 'R_j=u_j*Res_X(g/X,G_j) exactly.',
        },
        'completedAlgebra': {'base': 'Z_17', 'fullRank': 18**13,
                             'canonicalRankByActiveSize': {str(m): 17**m for m in sorted(counts)},
                             'canonicalTotalRank': sum(n*17**m for m,n in counts.items())},
        'canonicalSupports': supports,
        'canonicalSupportHistogram': dict(sorted(counts.items())),
        'inventoryDependency': {'relativePath': str(SOURCE.relative_to(HERE.parents[1])),
                                'sha256': sha256(source_bytes).hexdigest()},
        'frobeniusCoordinate': {'definition': 'y=7*(r+1)/(r-1)',
                                'inverse': 'r=(y+7)/(y-7)',
                                'equation': 'y^17-y^2+5=0',
                                'exception': 'r=1 corresponds to infinity'},
    }
    destination = HERE/'presentation.json'
    destination.write_text(json.dumps(doc, indent=2)+'\n')
    print(json.dumps({'file': str(destination), 'bytes': destination.stat().st_size,
                      'canonicalSupports': len(supports), 'fullRank': 18**13,
                      'canonicalTotalRank': doc['completedAlgebra']['canonicalTotalRank']}))


if __name__ == '__main__':
    main()
