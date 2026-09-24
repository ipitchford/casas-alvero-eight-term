from math import comb
import json
p=17
N=3

def add(*polys):
 o=[0]*N
 for a in polys:
  for i,c in enumerate(a[:N]):o[i]=(o[i]+c)%p
 return o

def sc(a,c):return [x*c%p for x in a]
def mul(a,b):
 o=[0]*N
 for i,x in enumerate(a):
  for j,y in enumerate(b[:N-i]):o[i+j]=(o[i+j]+x*y)%p
 return o

def power(a,n):
 o=[1]+[0]*(N-1)
 while n:
  if n&1:o=mul(o,a)
  a=mul(a,a);n//=2
 return o

def shift(a,n):return ([0]*n+a)[:N]
def const(c):return [c%p]+[0]*(N-1)
def C(n,k):return comb(n,k) if 0<=k<=n else 0
# c_k/17 in the cubic-plus-quadratic baseline with linear coefficient0.
A=[]
for k in range(17):
 row=[]
 for j in [0,4,10]:
  cj=C(20,j);dj=-cj*C(20-j,3);fj=-cj-dj
  value=cj*C(20-j,k)+dj*C(3,k)+fj*C(2,k)
  if k:assert value%17==0
  row.append(value//17 if k else 0)
 A.append(row)

def coeff(t,u):
 x=add(const(1),shift(t,1));y=add(const(1),shift(u,1))
 a=sc(power(x,4),-1)
 b=add(sc(power(y,10),-1),sc(mul(a,power(y,6)),-210))
 return [add(const(c0),sc(a,c1),sc(b,c2)) for c0,c1,c2 in A]

def eq(w,aa):
 o=const(0)
 for k in range(1,min(17,N+1)):
  o=add(o,shift(mul(aa[k],power(w,k-1)),k-1))
 return add(o,sc(power(w,16),1140),shift(sc(power(w,17),190),1),shift(sc(power(w,18),20),2),shift(power(w,19),3))

def h2(w,aa):
 o=const(0)
 for k in range(2,min(17,N+2)):
  o=add(o,shift(sc(mul(aa[k],power(w,k-2)),C(k,2)),k-2))
 # Terms k17,18 begin at pi15 or later. k19 and k20 contribute at pi and pi2.
 return add(o,shift(sc(power(w,17),20*171),1),shift(sc(power(w,18),190),2))

def pair(t0,u0):
 t=const(t0);u=const(u0)
 for k in range(1,N):
  aa=coeff(t,u)
  if t0:t[k]=-eq(t,aa)[k]*pow(16*pow(t0,15,p),-1,p)%p
  if u0:u[k]=-eq(u,aa)[k]*pow(16*pow(u0,15,p),-1,p)%p
 if t0:assert not any(eq(t,coeff(t,u)))
 if u0:assert not any(eq(u,coeff(t,u)))
 return t,u

def root(v0,aa):
 v=const(v0)
 for k in range(1,N):v[k]=-eq(v,aa)[k]*pow(16*pow(v0,15,p),-1,p)%p
 assert not any(eq(v,aa))
 return v

def order(a):return next((i for i,c in enumerate(a) if c),None)
records=[]
for t0 in range(17):
 for u0 in range(17):
  t,u=pair(t0,u0);aa=coeff(t,u)
  h20=aa[2]
  if not any(h20):records.append({'t0':t0,'u0':u0,'v0':0,'H2':h20})
  for v0 in range(1,17):
   v=root(v0,aa);hv=h2(v,aa)
   if not any(hv):records.append({'t0':t0,'u0':u0,'v0':v0,'H2':hv})
print(json.dumps({'precision':N,'survivor_count':len(records),'survivors':records},indent=2))
