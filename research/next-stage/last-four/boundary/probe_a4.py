from math import comb
import sympy as s
X,x,z,b,u=s.symbols('X x z b u')
f=X**20+comb(20,4)*b*X**16+comb(20,16)*u*X**4
D=-1140-comb(16,3)*comb(20,4)*b-4*comb(20,16)*u
E=-1-comb(20,4)*b-comb(20,16)*u-D
f+=D*X**3+E*X
U=-x**16-comb(16,4)*b*x**12
P=s.Poly(s.expand((f/X).subs({X:x,u:U})),b)
Q=s.Poly(s.expand((s.diff(f,X)-f/X).subs({X:x,u:U})),b)
P0,P4=P.nth(0),P.nth(1);Q0,Q4=Q.nth(0),Q.nth(1)
R=s.Poly(s.expand((P0*Q4-Q0*P4).subs(x,1+z)),z)
def val(n):
 n=abs(int(n));v=0
 if not n:return None
 while n%17==0:v+=1;n//=17
 return v
print('P4',P4,'Q4',Q4)
print('R',[(k,val(R.nth(k)),int(R.nth(k))//17**val(R.nth(k))%17) for k in range(R.degree()+1) if R.nth(k)])
print('Q4at1',Q4.subs(x,1),val(Q4.subs(x,1)))
print('R factor',s.factor(R.as_expr()))
print('Q0at1',Q0.subs(x,1),'Q4at1',Q4.subs(x,1))
