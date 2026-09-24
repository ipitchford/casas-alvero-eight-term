"""Exact scalar and polynomial replay of the compact u=v jet exclusion."""
from math import comb
import json

P=13
A=-comb(20,16)


def B(u):return -comb(20,15)*u**5-comb(16,15)*A*u


def Bprime(u):return -5*comb(20,15)*u**4-comb(16,15)*A


def E(u,D,C):return -1-A-B(u)-C-D


def f(x,u,D,C):return x**20+A*x**16+B(u)*x**15+C*x**10+D*x**3+E(u,D,C)*x


def H3(u,D,C):return comb(20,3)*u**17+comb(16,3)*A*u**13+comb(15,3)*B(u)*u**12+comb(10,3)*C*u**7+D


def H1at1(u,D,C):return 20+16*A+15*B(u)+10*C+3*D+E(u,D,C)


def scalar_hasse(x,k,u=2,D=3,C=0):
    return sum(comb(n,k)*c*x**(n-k) for n,c in [(20,1),(16,A),(15,B(u)),(10,C),(3,D),(1,E(u,D,C))] if n>=k)


def divide13(a):
    q,r=divmod(a,13)
    if r:raise ValueError('Constant is not divisible by13')
    return q%13


def determinant(matrix):
    a,b,c=matrix
    return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))%13


def solve(matrix,constants):
    a=[[x%P for x in row]+[-c%P] for row,c in zip(matrix,constants,strict=True)]
    for i in range(3):
        j=next(j for j in range(i,3) if a[j][i])
        a[i],a[j]=a[j],a[i]
        q=pow(a[i][i],-1,P)
        a[i]=[q*x%P for x in a[i]]
        for j in range(3):
            if i!=j:
                q=a[j][i]
                a[j]=[(x-q*y)%P for x,y in zip(a[j],a[i],strict=True)]
    return [a[i][3] for i in range(3)]


def trim(a):
    while a and not a[-1]:a.pop()
    return a


def gcd(a,b):
    while b:
        r=a[:]
        while len(r)>=len(b):
            k,c=len(r)-len(b),r[-1]*pow(b[-1],-1,P)%P
            for j,d in enumerate(b):r[k+j]=(r[k+j]-c*d)%P
            trim(r)
        a,b=b,r
    return [c*pow(a[-1],-1,P)%P for c in a]


def hasse(a,k):return trim([comb(i,k)*a[i]%P for i in range(k,len(a))])


def value(a,x):return sum(c*pow(x,i,P) for i,c in enumerate(a))%P


# Every entry below is derived from the integer defining equations, not copied
# from a precomputed jet matrix. Column order is r,l,k.
Fu=scalar_hasse(2,1)+Bprime(2)*(2**15-2)
Frow=[Fu,2**3-2,2**10-2]
H3u=17*comb(20,3)*2**16+13*comb(16,3)*A*2**12+comb(15,3)*(Bprime(2)*2**12+12*B(2)*2**11)
H3row=[H3u,1,comb(10,3)*2**7]
H1row=[14*Bprime(2),2,9]
F4row=[Bprime(2)*(4**15-4),4**3-4,4**10-4]
rows=[[x%P for x in row] for row in [Frow,H3row,H1row,F4row]]
constants=[divide13(f(2,2,3,0)),divide13(H3(2,3,0)),divide13(H1at1(2,3,0)),divide13(f(4,2,3,0))]
if rows!=[[10,6,8],[4,1,7],[11,2,9],[10,8,5]] or constants!=[7,6,4,3]:
    raise ValueError('Jet calculation differs')
initial_det=(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])%P
if initial_det!=12:raise ValueError('Initial Jacobian is singular')
h=[0]*21
for i,c in [(20,1),(16,4),(15,6),(3,3),(1,12)]:h[i]=c
if [value(hasse(h,j),4) for j in range(4)]!=[0,0,0,5]:
    raise ValueError('Root4 does not have multiplicity3')
if [value(hasse(h,j),1) for j in range(3)]!=[0,0,9] or value(hasse(h,1),2)!=9:
    raise ValueError('Root1/root2 cluster multiplicities differ')
normalized=[comb(20,10)//13,comb(16,10)*A//13,comb(15,10)*B(2)//13]
if any(n%13 for n in [comb(20,10),comb(16,10),comb(15,10)]):
    raise ValueError('H10 division not integral')
if normalized[0]%P!=3:raise ValueError('Divided H10 leading coefficient not unit3')
record=[]
for name,third in [('wbar1',2),('wbar4',3)]:
    matrix=[rows[0],rows[1],rows[third]]
    const=[constants[0],constants[1],constants[third]]
    solution=solve(matrix,const)
    r,l,k=solution
    g=[0]*11
    g[10]=1
    g[6]=normalized[1]*pow(normalized[0]%P,-1,P)%P
    g[5]=normalized[2]*pow(normalized[0]%P,-1,P)%P
    g[0]=k*pow(normalized[0]%P,-1,P)%P
    common=gcd(h,g)
    f4jet=(constants[3]+sum(rows[3][i]*solution[i] for i in range(3)))%P
    if name=='wbar1':
        if solution!=[12,3,3] or common!=[9,1] or value(hasse(g,1),4)!=3 or f4jet!=6:
            raise ValueError('wbar1 conclusion differs')
    else:
        if solution!=[5,7,12] or common!=[1]:raise ValueError('wbar4 conclusion differs')
    record.append({'branch':name,'jetMatrix':matrix,'constantVector':const,
                   'matrixDeterminantMod13':determinant(matrix),'solution_r_l_k':solution,
                   'normalizedH10LowFirst':g,'residualCommonRootGcd':common,
                   'GprimeAt4':value(hasse(g,1),4),'f4_div13_jet':f4jet})
print(json.dumps({'status':'PASS','B2':B(2),'Bprime2_mod13':Bprime(2)%P,
                  'initialJacobianMod13':[[10,6],[4,1]],'initialJacobianDeterminantMod13':initial_det,
                  'rows_F_H3_H1at1_f4':rows,'constantJets':constants,
                  'H10_div13_coefficient_residues':[x%P for x in normalized],
                  'root4_Hasse_values_orders0to3':[value(hasse(h,j),4) for j in range(4)],
                  'root1_Hasse_values_orders0to2':[value(hasse(h,j),1) for j in range(3)],
                  'root2_derivative':value(hasse(h,1),2),
                  'branches':record},indent=2))
