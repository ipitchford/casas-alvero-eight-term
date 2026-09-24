#!/usr/bin/env python3
"""Apply de Frutos 2013 Prop3.5.5 to all two-visible strata, with degeneration guards.
Primary text: https://uvadoc.uva.es/bitstream/10324/3602/1/tesis367-130927.pdf
Deficiency indices r<s; computation uses only exact integer arithmetic.
"""
from pathlib import Path
from math import comb,gcd
import json
ROOT=Path(__file__).resolve().parent

def old_pair_test(n,r,s,p):
    B=comb(n,r)%p;D=comb(n,s)%p;C=comb(n-r,s-r)%p;g=gcd(r,s)
    residue=(pow(B,s//g,p)*pow(C-1,(s-r)//g,p)*pow(D-C,r//g,p)-pow(B-1,r//g,p)*pow(D-1,s//g,p))%p
    # Independently transcribe the source in exponent indices i=n-s,j=n-r.
    rho=r//g;sigma=(s-r)//g;c_source=comb(s,r)%p
    source_residue=(pow(D,rho,p)*pow(B-c_source,rho,p)*pow(B-D*c_source,sigma,p)-(-1)**sigma*pow(D-1,rho+sigma,p)*pow(B-1,rho,p))%p
    if source_residue!=((-1)**sigma*residue)%p:raise ValueError('Source formula and deficiency-index formula disagree')
    # A coefficient may disappear upon reduction; B or D equal1 permits
    # a singleton degeneration, so the whole two-visible stratum is not excluded.
    applicable=(B not in (0,1) and D not in (0,1))
    return {'r':r,'s':s,'prime':p,'B':B,'D':D,'C':C,'gcd':g,'Nmodp':residue,'sourceResidue':source_residue,'nonzeroNonunitBinomialGuard':applicable,'excludes':applicable and residue!=0}

def main():
    raw=json.loads((ROOT/'enumeration.json').read_text());records=[]
    for record in raw['survivorRecords']:
        S=record['support'];tests=[]
        for p in raw['primes']:
            visible=record['visibleSupports'][str(p)]
            if len(visible)==2:tests.append(old_pair_test(20,*visible,p))
        records.append({'support':S,'tests':tests,'excludedByOldPairCriterion':any(t['excludes'] for t in tests)})
    result={'source':'de Frutos Marin2013 Proposition3.5.5 (printedp57/PDFp79), as audited by prior-art agent','newMaskFirstBaselineCount':len(records),'oldPairExcluded':[r['support'] for r in records if r['excludedByOldPairCriterion']],'survivors':[r['support'] for r in records if not r['excludedByOldPairCriterion']],'records':records}
    (ROOT/'two-visible-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
