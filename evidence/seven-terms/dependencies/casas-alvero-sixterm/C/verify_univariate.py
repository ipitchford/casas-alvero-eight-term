"""Read-only standard-library replay of C's two resultant certificates.

Reuses B's exact field/resultant helpers, whose source hash is recorded.
Resultants are checked at more distinct F_(13^3) points than their proved
Sylvester coefficient-degree bounds. This is interpolation, not a search.
"""
from pathlib import Path
from math import comb
from time import perf_counter
import hashlib
import importlib.util
import json

HERE=Path(__file__).resolve().parent
SHARED=HERE.parent/'B'/'verify_certificate.py'
spec=importlib.util.spec_from_file_location('b_replay_helpers',SHARED)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def require(condition,message):
    if not condition:raise ValueError(message)

def product(*polynomials):
    out=[1]
    for polynomial in polynomials:out=m.umul(out,polynomial)
    return out

def power(poly,n):return product(*([poly]*n))

def main():
    started=perf_counter()
    data=json.loads((HERE/'univariate-certificate.json').read_text())
    require(not any((r**3-r-1)%13==0 for r in range(13)),
            'The defining cubic is reducible')
    require((-comb(20,16))%13==4,'H16 normalization mismatch')
    b=[0,(-16*4)%13,0,0,0,(-comb(20,15))%13]
    N=[0]*20
    N[0],N[1],N[5],N[15],N[19]=5,b[1],b[5],8,7
    cn,remainder=m.udivide(N,[12,1])
    require(not remainder,'Nonexact removal of u-1')
    dn=m.uadd(m.umul([1,1],m.uadd([8],m.uscale(b,-1))),m.uscale(cn,-1))
    expected_generic=product(power([1,1],17),[11,1],[12,1],[11,4,1])
    expected_special=product([11,1],[10,1],[3,1])
    receipts=[]
    for name,q,bc,c,d,target in [
        ('generic',[1,1],b,cn,dn,expected_generic),
        ('special',[1],[6],[0,1],[2,12],expected_special),
    ]:
        qb=m.umul(q,bc)
        p=[[] for _ in range(20)]
        h3=[[] for _ in range(18)]
        h1=[[] for _ in range(20)]
        p[19],p[15],p[14],p[2],p[0]=q,m.uscale(q,4),qb,c,d
        h3[17]=m.uscale(q,comb(20,3))
        h3[13]=m.uscale(q,4*comb(16,3))
        h3[12]=m.uscale(qb,comb(15,3))
        h3[0]=c
        h1[19],h1[15],h1[14],h1[2],h1[0]=m.uscale(q,20),m.uscale(q,64),m.uscale(qb,15),m.uscale(c,3),d
        degrees=[max(len(a)-1 for a in array) for array in (p,h3,h1)]
        bounds=[17*degrees[0]+19*degrees[1],19*degrees[0]+19*degrees[2]]
        require(bounds==([648,684] if name=='generic' else [36,38]),'Unexpected degree bound')
        certificate=data['charts'][name]
        require(certificate['gcd']==target,'Claimed gcd factorization mismatch')
        R3,R1=certificate['R3'],certificate['R1']
        require(len(R3)-1<=bounds[0] and len(R1)-1<=bounds[1],'Saved resultant exceeds bound')
        points=[r for r in range(13**3) if name!='generic' or r!=12][:max(bounds)+1]
        require(len(set(points))==max(bounds)+1,'Not enough distinct field points')
        for t in points:
            pv,d3v,d1v=[[m.feval(coeff,t) for coeff in array] for array in (p,h3,h1)]
            require(len(m.clean(pv[:]))==20 and len(m.clean(d3v[:]))==18 and len(m.clean(d1v[:]))==20,
                    'Specialization dropped a degree')
            require(m.fresultant(pv,d3v)==m.feval(R3,t),f'R3 mismatch in {name} at {t}')
            require(m.fresultant(pv,d1v)==m.feval(R1,t),f'R1 mismatch in {name} at {t}')
        F,G=m.umul(c,R3),m.umul(d,R1)
        identity=m.uadd(m.umul(certificate['U'],F),m.umul(certificate['V'],G))
        require(identity==target,'Bezout multiplication failed')
        require(m.uadd(identity,F)!=target,'Mutation control failed')
        # Quotient information needed to classify c,d on the generic factors.
        if name=='generic':
            require(m.udivide(m.uadd(c,m.uscale(q,-3)),[11,1])[1]==[], 'u=2 does not give c=3')
            require(m.udivide(m.uadd(b,[7]),[11,1])[1]==[], 'u=2 does not give b=6')
            quadratic=[11,4,1]
            require(m.udivide(m.uadd(c,m.uscale(q,-2)),quadratic)[1]==[], 'Quadratic branch does not give c=2')
            require(m.udivide(d,quadratic)[1]==[], 'Quadratic branch does not give d=0')
            require(m.udivide(m.uadd(b,[7]),quadratic)[1]==[], 'Quadratic branch does not give b=6')
        receipts.append({'chart':name,'resultantDegrees':[len(R3)-1,len(R1)-1],
                         'degreeBounds':bounds,'distinctFieldPoints':len(points),
                         'BezoutIdentity':'PASS','mutationControl':'PASS'})
    # u=-1 cannot be a root because h(-1)=10 after normalization.
    require((1+4-8)%13==10,'Exceptional u=-1 chart check failed')
    print(json.dumps({'status':'PASS','charts':receipts,
                      'field':'F13[t]/(t3-t-1)',
                      'sharedImplementation':str(SHARED),
                      'sharedImplementationSha256':hashlib.sha256(SHARED.read_bytes()).hexdigest(),
                      'certificateSha256':hashlib.sha256((HERE/'univariate-certificate.json').read_bytes()).hexdigest(),
                      'elapsedSeconds':perf_counter()-started},indent=2))

if __name__=='__main__':main()
