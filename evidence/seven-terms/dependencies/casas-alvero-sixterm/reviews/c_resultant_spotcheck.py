"""Independent direct Sylvester evaluations for C's two resultant charts.

Reuses only the reviewer's independent prime-field determinant helper.
The complete extension-field interpolation replay remains a separate check.
"""
import json
from pathlib import Path
from b_independent_spotcheck import resultant, evaluate


def main():
    data=json.loads((Path(__file__).parent.parent/'C'/'univariate-certificate.json').read_text())
    rows=[]
    for chart,points in (('generic',range(12)),('special',range(13))):
        for parameter in points:
            if chart=='generic':
                u=parameter
                q=u+1
                b=(5*pow(u,5,13)+u)%13
                numerator=(5+b-6*pow(u,19,13)-5*pow(u,15,13))%13
                cn=(25+1-6*19-5*15)%13 if u==1 else numerator*pow(u-1,-1,13)%13
                dn=(q*(8-b)-cn)%13
            else:
                q,b,cn,dn=1,6,parameter,(2-parameter)%13
            f,h3,h1=[0]*20,[0]*18,[0]*20
            for i,c in {19:q,15:4*q,14:q*b,2:cn,0:dn}.items():f[i]=c%13
            for i,c in {17:9*q,13:4*q,0:cn}.items():h3[i]=c%13
            for i,c in {19:7*q,15:12*q,14:2*q*b,2:3*cn,0:dn}.items():h1[i]=c%13
            actual=[resultant(f,h3),resultant(f,h1)]
            cert=data['charts'][chart]
            expected=[evaluate(cert['R3'],parameter),evaluate(cert['R1'],parameter)]
            if actual!=expected:raise RuntimeError((chart,parameter,actual,expected))
            rows.append({'chart':chart,'parameter':parameter,'resultants':actual})
    receipt={'status':'PASS','method':'Direct prime-field Sylvester determinant',
             'resultantEvaluations':2*len(rows),
             'scope':'Supplementary independent spot check; not substituted for the complete interpolation proof',
             'points':rows}
    Path(__file__).with_name('c-resultant-spotcheck.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='points'},indent=2))


if __name__=='__main__':main()
