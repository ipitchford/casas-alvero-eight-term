"""Exploratory arithmetic in Z_17[pi]/(pi^N), pi^15=17; not an exclusion certificate."""
exec(open(__file__.replace('ramified_probe.py','probe_a4.py')).read().split("print('P4'")[0])
N=65

def norm(a):
 a=list(a[:N])+[0]*max(0,N-len(a))
 for i in range(N):
  carry,a[i]=divmod(a[i],17)
  if i+15<N:a[i+15]+=carry
 return a

def plus(a,b):return norm([a[i]+b[i] for i in range(N)])
def mul(a,b):
 c=[0]*N
 for i,v in enumerate(a):
  if v:
   for j,w in enumerate(b[:N-i]):c[i+j]+=v*w
 return norm(c)
def const(n):return norm([int(n)])
def ev(poly,at):
 out=const(0)
 for c in reversed(poly):out=plus(mul(out,at),const(c))
 return out
# S(Z)=R(1+pi Z)/(17^2 pi^2 Z^2).
coefs=[]
for k in range(2,R.degree()+1):
 c=int(R.nth(k));v=val(c);power=15*v+k-32
 if power<0:raise ValueError('Nonintegral scaling')
 coefs.append(norm([0]*power+[c//17**v]))
def seval(at):
 out=const(0)
 for c in reversed(coefs):out=plus(mul(out,at),c)
 return out
Z=const(5)
der=14*15*pow(5,14,17)%17
for i in range(1,N):
 defect=seval(Z)
 if any(defect[:i]):raise ValueError('Earlier digit changed')
 Z[i]=(-defect[i]*pow(der,-1,17))%17
Z=norm(Z)
if any(seval(Z)):raise ValueError('Hensel residual')
xring=plus(const(1),norm([0]+Z))
pQ0=list(reversed(s.Poly(Q0,x).all_coeffs()));pQ4=list(reversed(s.Poly(Q4,x).all_coeffs()))
q0=ev(pQ0,xring);q4=ev(pQ4,xring)
print('Q0 leading',next((i for i,v in enumerate(q0) if v),None),'Q4 leading',next((i for i,v in enumerate(q4) if v),None))
# Solve q0 + b q4 =0; q4 has initial pi^15.
q4unit=norm(q4[15:]);target=norm([-c for c in q0[15:]])
bdigits=const(0)
for i in range(N-15):
 residual=plus(mul(bdigits,q4unit),norm([-c for c in target]))
 bdigits[i]=(-residual[i]*pow(q4unit[0],-1,17))%17
print('b leading',[(i,v) for i,v in enumerate(bdigits) if v][:12])
print('b pi30digit',bdigits[30],'smallroot requirement 15')
