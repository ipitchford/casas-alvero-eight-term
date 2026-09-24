#!/usr/bin/env python3
"""Independent finite arithmetic for ROW2_PROOF.md; standard library only.

The producer proof is not imported. Acceptance checks use explicit exceptions,
so python -O leaves them active. Valuation/cluster arguments require the
separate mathematical audit and are not inferred from these finite checks.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json

P=17

def require(c,message):
    if not c:
        raise ValueError(message)

def trim(a):
    a=list(a)
    while a and a[-1]==0:
        a.pop()
    return a

def add(a,b,scale=1):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=scale*x
    return trim(out)

def scaled(a,c):return trim([c*x for x in a])

def poly(terms):
    out=[0]*(max(terms,default=-1)+1)
    for k,v in terms.items():out[k]=v
    return trim(out)

def hasse(a,j):return trim([comb(k,j)*a[k] for k in range(j,len(a))])

def shift(a):return [sum(comb(i,k)*a[i] for i in range(k,len(a))) for k in range(len(a))]

def val(n):
    n=Fraction(n)
    if not n:return None
    def one(m):
        k=0
        while m%P==0:m//=P;k+=1
        return k
    return one(n.numerator)-one(n.denominator)

def mod(q,m=P):
    q=Fraction(q)
    return q.numerator*pow(q.denominator,-1,m)%m

# Quadratic algebra, exact in Q[s]/(s^2-3), and optionally reduced modulo m.
def qadd(a,b,m=None):
    v=(a[0]+b[0],a[1]+b[1])
    return tuple(mod(x,m) for x in v) if m else v

def qmul(a,b,m=None):
    v=(a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    return tuple(mod(x,m) for x in v) if m else v

def qscale(a,c,m=None):return qmul(a,(c,0),m)

def qeval(a,r=(0,1),m=None):
    v=(0,0)
    for c in reversed(a):v=qadd(qmul(v,r,m),(c,0),m)
    return v

def qinv(a):
    n=(a[0]*a[0]-3*a[1]*a[1])%P
    require(n!=0,'quadratic field inverse nonzero norm')
    return (a[0]*pow(n,-1,P)%P,-a[1]*pow(n,-1,P)%P)

def divmod_p(a,b):
    a=trim([x%P for x in a]);b=trim([x%P for x in b])
    require(bool(b),'polynomial denominator')
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*pow(b[-1],-1,P)%P;q[k]=c
        a=trim([x%P for x in add(a,[0]*k+[c*x for x in b],-1)])
    return trim(q),a

# Build f from its coefficients and solve H3 f(1)=T and f(1)=0,
# rather than starting from any printed c1/c2 identities.
def fbuild(a,b,T=0,F=0):
    f=poly({20:1,18:-190,16:comb(20,4)*a,10:comb(20,10)*b})
    D=T-sum(hasse(f,3));f=add(f,poly({3:D,2:F}))
    E=-sum(f);f=add(f,poly({1:E}))
    require(sum(f)==0,'f(1)=0')
    require(sum(hasse(f,3))==T,'H3 f(1)=T')
    return f

zero=fbuild(0,0)
dirs={'constant':zero}
for key,args in [('a',(1,0,0,0)),('b',(0,1,0,0)),('T',(0,0,1,0)),('F',(0,0,0,1))]:
    dirs[key]=add(fbuild(*args),zero,-1)
cs={key:shift(v)+[0]*21 for key,v in dirs.items()}
expected={
    1:{'constant':304589,'a':-5353725,'b':-42678636,'T':2,'F':1},
    2:{'constant':432820,'a':-7558200,'b':-58198140,'T':3,'F':1},
    3:{'constant':0,'a':0,'b':0,'T':1,'F':0},
    17:{'constant':-2280,'a':0,'b':0,'T':0,'F':0},
    18:{'constant':0,'a':0,'b':0,'T':0,'F':0},
    19:{'constant':20,'a':0,'b':0,'T':0,'F':0},
    20:{'constant':1,'a':0,'b':0,'T':0,'F':0},
}
for k,expected_k in expected.items():
    require({key:cs[key][k] for key in dirs}==expected_k,'shifted coefficient c'+str(k))
for key in dirs:
    require(all(cs[key][k]%17==0 for k in range(4,17)),
            'coefficientwise middle divisibility')
diff={key:cs[key][2]-cs[key][1]-(1 if key=='T' else 0) for key in dirs}
require(diff=={'constant':17*7543,'a':-17*129675,'b':-17*912912,'T':0,'F':0},
        'c2-c1-T exact identity')
require(comb(19,2)%17==1,'order19 H2 contribution remains a unit')

# Complete visible-root coverage over F17bar.  s^2=3 is irreducible;
# the seed factors as (X-1)^17 * X * (X^2-3), so these are all locations.
require(3 not in {i*i%17 for i in range(17)},'s gives a quadratic field')
roots={'0':(0,0),'1':(1,0),'s':(0,1),'-s':(0,16)}
h=poly({20:1,18:-3,3:-1,1:3})
# Frobenius expansion (X-1)^17=X^17-1 in characteristic17.
require(all(comb(17,k)%17==0 for k in range(1,17)),'Frobenius factorization')
require(all(qeval(h,r,17)==(0,0) for r in roots.values()),'seed roots')
common_hasse={}
values_hasse={}
for j in (1,2,3):
    vals={name:qeval(hasse(h,j),r,17) for name,r in roots.items()}
    values_hasse[str(j)]={k:list(v) for k,v in vals.items()}
    common_hasse[str(j)]=[name for name,v in vals.items() if v==(0,0)]
require(common_hasse=={'1':['1'],'2':['0','1'],'3':['1']},'H1/H2/H3 common locations')
g2=poly({2:1,0:-1})
require([name for name,r in roots.items() if qeval(g2,r,17)==(0,0)]==['1'],
        'G2 unit witness coverage')
require(qeval(hasse(h,1),roots['0'],17)!=(0,0) and
        all(qeval(hasse(h,1),roots[name],17)!=(0,0) for name in ('s','-s')),
        'outside seed roots are simple')

census=[]
for w4,w10 in product(('1','s','-s'),repeat=2):
    r=roots[w4];s=roots[w10]
    a=qscale(qeval(poly({4:1,2:-6}),r,17),-1,17)
    require(a[1]==0,'G4 coefficient is in F17')
    av=a[0]
    b=qscale(qeval(poly({10:1,8:-45,6:210*av}),s,17),-1,17)
    require(b[1]==0,'G10 coefficient is in F17')
    bv=b[0]
    divided=(7543-129675*av-912912*bv)%17
    require(qeval(poly({4:1,2:-6,0:av}),r,17)==(0,0),'G4 incidence')
    require(qeval(poly({10:1,8:-45,6:210*av,0:bv}),s,17)==(0,0),'G10 incidence')
    census.append({'w4':w4,'w10':w10,'a':av,'b':bv,'divided':divided})
pairs=sorted({(x['a'],x['b'],x['divided']) for x in census})
require(pairs==[(5,8,6),(5,14,2),(9,6,0),(9,7,5)],'complete pair/divided list')
survivors=[x for x in census if x['divided']==0]
require(len(survivors)==4 and all(x['a']==9 and x['b']==6 and x['w4']!='1' and x['w10']!='1' for x in survivors),
        'all four independent sign choices survive initial sieve')

# Exact simple-root anchoring identities.  The actual signs need not agree.
require(poly({4:-1,2:6})==add([9],poly({4:1,2:-6,0:9}),-1),
        'a=9-(r^2-3)^2')
G10base=poly({10:1,8:-45,6:210*9})
require(qeval(G10base)==(47628,0),'outside G10 baseline')
base_diff=17*(7543-129675*9-912912*(-47628))
require(val(base_diff)==2 and mod(Fraction(base_diff,17**2))==8,
        'base c2-c1-T has value exactly two')
surviving=fbuild(9,6)
c4=shift(surviving)[4]
require(val(c4)==1 and c4//17%17==8,'c4 divided residue')
# Integer representative congruence: T,F in17O, all a,b integral.
require(all(x%17==0 for x in add(zero,h,-1)),'constant polynomial differs from seed in17Z')
require(all(x%17==0 for key in ('a','b') for x in dirs[key]),'middle ordinary directions in17Z')

# The lambda2-nonzero ratio equations have no geometric solution.
R2=poly({2:1,0:-6});R13=poly({13:1,0:-5})
q1,r1=divmod_p(R13,R2);q2,r2=divmod_p(R2,r1)
require(r1==[12,8] and r2==[9],'ratio Euclidean certificate')
require(pow(6,6,17)==8 and 5*pow(8,-1,17)%17==7 and 7*7%17!=6,
        'hand ratio contradiction')
# Direct Hasse derivatives of the leading model, with symbolic coefficient directions.
Ldir={'kappa':poly({4:1}),'lambda2':poly({2:1}),'lambda1':poly({1:1}),'wild':poly({17:-2})}
require(all(x%17==0 for j in (1,2,3) for x in hasse(Ldir['wild'],j)),
        'wild term disappears from first three Hasse derivatives')
require(hasse(Ldir['kappa'],3)==[0,4] and hasse(Ldir['kappa'],2)==[0,0,6],
        'low Hasse leading terms')

# Quartic discriminant, computed by a fraction-free determinant of the Sylvester matrix.
def bareiss(matrix):
    a=[row[:] for row in matrix];n=len(a);previous=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            require(pivot is not None,'nonzero determinant pivot')
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                require(numerator%previous==0,'Bareiss exact division')
                a[i][j]=numerator//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]
quartic=poly({4:1,2:-6,1:5});der=hasse(quartic,1)
n=len(quartic)-1;m=len(der)-1;matrix=[]
for i in range(m):matrix.append([0]*i+list(reversed(quartic))+[0]*(m-1-i))
for i in range(n):matrix.append([0]*i+list(reversed(der))+[0]*(n-1-i))
disc=bareiss(matrix)
require(disc==4725 and disc%17==16,'quartic discriminant')

# Final exact rational family after c1=c2=T=0 and a=9.
B=Fraction(7543-129675*9,912912)
require(B==Fraction(-1387,1092) and val(Fraction(1,912912))==0,'B and unit denominator')
F=-(cs['constant'][1]+cs['a'][1]*9+cs['b'][1]*B)
f=fbuild(9,B,0,F)
cf=shift(f)
require(cf[1]==cf[2]==cf[3]==0,'triple derivative vanishing in final exact family')
require(F==-6329185,'final F')
G=poly({10:1,8:-45,6:210*9,0:B})
final_values={
    'f':qeval(f,m=289),'fprime':qeval(hasse(f,1),m=289),
    'G10':qeval(G,m=289),'G10prime':qeval(hasse(G,1),m=289)}
require(final_values=={'f':(0,170),'fprime':(130,283),'G10':(204,0),'G10prime':(0,92)},
        'final mod289 quadratic-ring values')
# Check both signs and verify the rational expression, without searching only F17-points.
final_residuals={}
for name in ('s','-s'):
    r=roots[name]
    f1=qscale(r,10,17);fp=qscale(qadd(r,(1,0),17),11,17)
    hvalue=qscale(qmul(f1,qinv(fp),17),-1,17)
    residual=qadd((12,0),qmul(qscale(r,7,17),hvalue,17),17)
    target=qmul(qadd(qscale(r,12,17),(-4,0),17),qinv(qadd(r,(1,0),17)),17)
    require(residual==target and residual!=(0,0),'final nonzero residual at '+name)
    final_residuals[name]={'h':list(hvalue),'residual':list(residual)}
require((4*pow(12,-1,17))%17==6 and 6*6%17==2,'algebraic numerator contradiction')

# Mutation control: the printed f-value coefficient 170 cannot be replaced by171.
require(final_values['f']!=(0,171),'negative control must reject altered target')
result={
    'status':'PASS','checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'coefficient_formulas':{str(k):v for k,v in expected.items()},
    'c4_formula':{key:cs[key][4] for key in dirs},'difference_formula':diff,
    'hasse_values_at_seed_roots':values_hasse,'common_hasse_locations':common_hasse,
    'outside_witness_census':census,'survivors':survivors,
    'base_difference':base_diff,'base_difference_valuation':val(base_diff),
    'base_difference_over_17_squared_residue':8,'c4_over_17_residue':8,
    'rho_euclidean':{'first_remainder':r1,'last_remainder':r2,'first_quotient':q1,'second_quotient':q2},
    'quartic_discriminant':disc,'B':str(B),'F':str(F),
    'final_mod_289_values':{key:list(value) for key,value in final_values.items()},
    'final_two_sign_residuals':final_residuals,'negative_control':'altered f-value coefficient rejected',
    'scope':'Finite exact arithmetic only; arbitrary-ramification and cluster-cover arguments are audited separately.'}
print(json.dumps(result,indent=2,sort_keys=True))
