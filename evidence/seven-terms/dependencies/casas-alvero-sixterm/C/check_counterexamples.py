"""Independent direct Hasse-witness replay; all derivative orders are checked.

No result relies on absence from a bounded search. Explicit checks remain
active under optimized Python. No CAS is used.
"""
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
EXAMPLES=[
    {'p':2,'terms':{20:1,16:1},'nonzeroWitnesses':{16:1}},
    {'p':11,'terms':{20:1,16:6,15:10,1:5},
     'nonzeroWitnesses':{16:1,15:5,1:3}},
    {'p':13,'terms':{20:1,16:4,15:6,3:3,1:12},
     'nonzeroWitnesses':{16:1,15:1,3:2,1:1}},
    {'p':13,'terms':{20:1,16:4,15:6,3:2},
     'nonzeroWitnesses':{16:1,15:1,3:10}},
    {'p':13,'terms':{20:1,16:4,15:6,3:10,1:5},
     'nonzeroWitnesses':{16:1,15:1,3:11,1:3}},
    {'p':17,'terms':{20:1,3:-1},'nonzeroWitnesses':{3:1}},
    {'p':19,'terms':{20:1,1:-1},'nonzeroWitnesses':{1:1}},
]


def require(condition,message):
    if not condition:raise RuntimeError(message)


def hasse(coefficients,order):
    return [sum(value*comb(exponent,order)
                for exponent,value in coefficients.items()
                if exponent-order==output_exponent)
            for output_exponent in range(21-order)]


def horner(coefficients,x,p):
    result=0
    for value in reversed(coefficients):result=(result*x+value)%p
    return result


records=[]
for example in EXAMPLES:
    p=example['p']; coefficients=example['terms']
    values=[]
    for order in range(1,20):
        witness=example['nonzeroWitnesses'].get(order,0)
        fv=horner(hasse(coefficients,0),witness,p)
        dv=horner(hasse(coefficients,order),witness,p)
        require(fv==0 and dv==0, f'Failed witness at p={p}, order={order}')
        values.append({'order':order,'witness':witness,'f':fv,'Hasse':dv})
    require(len(coefficients)>1,'Example must be nonmonomial')
    records.append({'p':p,'terms':coefficients,'all19OrdersChecked':True,
                    'witnesses':values})

require(comb(20,10)==2**2*11*13*17*19,
        'Middle coefficient prime factorization is incorrect')
record={'status':'PASS','scope':'Exact positive-characteristic CA witnesses only',
        'middle_binomial':comb(20,10),
        'middle_binomial_prime_divisors':[2,11,13,17,19],
        'every_prime_killing_middle_term_has_seed_example':True,
        'examples':records}
(HERE/'counterexample-verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','examples':len(records),
                  'HasseOrdersPerExample':19,
                  'all_middle_term_primes_covered':True},indent=2))
