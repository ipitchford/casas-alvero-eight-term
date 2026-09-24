"""Independent finite arithmetic for ROW2_PROOF; no imports from producer scripts.

This checks identities and the finite residue obstruction. The valuation and
cluster arguments are reviewed separately in ROW2_AUDIT.md.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json


def require(ok, explanation):
    if not ok:
        raise ValueError(explanation)


def hs(f,k,x=1):
    return sum(c*comb(i,k)*x**(i-k) for i,c in enumerate(f) if i>=k)


def family(a,b,t=0,F=0):
    f=[Fraction(0) for _ in range(21)]
    f[20],f[18],f[16],f[10]=1,-190,4845*a,184756*b
    f[3]=t-hs(f,3)
    f[2]=F
    f[1]=-hs(f,0)
    return f


def modq(f,modulus):
    # Exact remainder at a symbolic s satisfying s^2=3.
    result=[0,0]
    for i,c in enumerate(f):
        c=Fraction(c)
        result[i%2]=(result[i%2]+c.numerator*pow(c.denominator,-1,modulus)*pow(3,i//2,modulus))%modulus
    return result


def derivative(f):
    return [i*f[i] for i in range(1,len(f))]


def main():
    # Each target expression is affine in these four parameters: a basis check
    # proves the identity, not a sample of possible mathematical candidates.
    for a,b,t,F in [(0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
        f=family(a,b,t,F)
        c=[hs(f,k) for k in range(21)]
        require(f[3]==153900-2713200*a-22170720*b+t,'D identity')
        require(c[1]==-5353725*a-42678636*b+304589+2*t+F,'c1 identity')
        require(c[2]==-7558200*a-58198140*b+432820+3*t+F,'c2 identity')
        require(c[2]-c[1]-t==17*(7543-129675*a-912912*b),'divided difference')
        require(c[0]==0 and c[3]==t,'normalization and H3')
        require(all(c[k]%17==0 for k in range(4,17)),'middle shifted divisibility')
        require((c[17],c[18],c[19],c[20])==(-2280,0,20,1),'upper shifted coefficients')
    require(comb(19,2)%17==1 and comb(19,3)%17==0,'exceptional Hasse coefficients')
    cases=[]
    for u in (1,3):
        a=(-u*u+6*u)%17
        for v in (1,3):
            b=(-v**5+45*v**4-210*a*v**3)%17
            cases.append([a,b,(7543-129675*a-912912*b)%17])
    require(cases==[[5,14,2],[5,8,6],[9,7,5],[9,6,0]],'complete squared-root residue table')
    require(hs(family(9,6),4)/17%17==8,'unit quartic coefficient')
    require((-3**5+45*3**4-210*9*3**3)==-47628,'outside b constant')
    require((7543-129675*9-912912*(-47628))%17==0,'second divided precision')
    require(pow(pow(3,-1,17),6,17)==8,'rho13 reduction')
    rho=5*pow(8,-1,17)%17
    require(rho==7 and rho*rho%17==15 and pow(3,-1,17)==6,'lambda2 geometric obstruction')
    # Discriminant of x(x^3-6x+5): q(0)^2 times the cubic discriminant.
    discriminant=5**2*(-4*(-6)**3-27*5**2)
    require(discriminant==4725 and discriminant%17!=0,'quartic good characteristic')

    B=Fraction(7543-129675*9,912912)
    require(B.denominator%17!=0,'B denominator')
    f=family(9,B)
    # Solve H2 f(1)=0, then f(1)=0 again; H1=0 is a checked consequence.
    f[2]=-hs(f,2)
    f[1]=0
    f[1]=-hs(f,0)
    require(all(hs(f,k)==0 for k in range(4)),'exact quadruple-root family')
    g=[Fraction(0) for _ in range(11)]
    g[10],g[8],g[6],g[0]=1,-45,210*9,B
    values={'f':modq(f,289),'fprime':modq(derivative(f),289),
            'G10':modq(g,289),'G10prime':modq(derivative(g),289)}
    require(values=={'f':[0,170],'fprime':[130,283],'G10':[204,0],'G10prime':[0,92]},'mod289 simple-root data')
    require(283%17==130%17==11 and 92%17==7,'first-digit derivatives')
    # Cross-multiply the two first-digit equations using s^2=3.
    # 12 + 7s[-10s/(11(s+1))] = (12s-4)/(s+1).
    require((12*11-210)%17==(-4*11)%17,'final numerator identity')
    forced_s=4*pow(12,-1,17)%17
    require(forced_s==6 and forced_s**2%17==2,'no geometric outside-root solution')
    proof=Path(__file__).with_name('ROW2_PROOF.md')
    print(json.dumps({'status':'PASS','scope':'Independent finite coefficient/residue checks; valuation proof reviewed separately.',
                      'proofSHA256':sha256(proof.read_bytes()).hexdigest(),
                      'residueCases':cases,'mod289Values':values,
                      'quarticDiscriminant':discriminant,'finalImpossibleSquare':forced_s**2%17},indent=2))


if __name__=='__main__':main()
