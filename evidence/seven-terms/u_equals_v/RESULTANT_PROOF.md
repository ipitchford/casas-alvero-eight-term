# Independent characteristic-zero resultant route for u=v

The compact primary argument is `JET_PROOF.md`. This second argument uses
integer polynomial identities and provides a separate exclusion of the assigned
collision branches. Its large certificate is not needed by the jet proof.

Suppose
\[
f=X^{20}+AX^{16}+BX^{15}+CX^{10}+DX^3+EX,
\quad A=-4845,\quad f(1)=0,
\]
and a common root \(u\) of \(f,H_{15}f,H_3f\) satisfies \(u\ne0,1\).
The targeted residue assignments have \(u\equiv2\pmod{\mathfrak m}\),
so both exclusions hold. Direct Hasse differentiation gives
\[
B=-15504u^5+77520u,
\]
\[
D=D_0-120Cu^7,\quad D_0=7053180u^{17}-32558400u^{13},
\]
\[
E=E_0+119Cu^9,\quad E_0=-7037677u^{19}+32485725u^{15}.
\]
Here \(H_3f(u)=0\) gives \(D\), and \(f(u)/u=0\) gives \(E\);
the division is justified by \(u\ne0\). The equation \(f(1)=0\) is
\[
L_0(u)C=N_0(u),
\]
where
\[
L_0=1-120u^7+119u^9,
\]
\[
N_0=4844-77520u+15504u^5+32558400u^{13}
      -32485725u^{15}-7053180u^{17}+7037677u^{19}.
\]
Both are divisible by \(u-1\). Put \(L=L_0/(u-1)\),
\(N=N_0/(u-1)\), of degrees 8 and 18. The independently checked
degree-preserving modular gcd proves \(\gcd_{\mathbb Q[u]}(L,N)=1\).
Thus \(L=0\) is impossible at a solution of \(LC=N\), and
\[
C=N/L,\quad D=D_*/L,\quad E=E_*/L,
\]
where
\[
D_*=D_0L-120Nu^7,\qquad E_*=E_0L+119Nu^9.
\]
In the actual target residue class, the stronger direct check \(L(2)=4\)
modulo 13 already makes \(L\) a unit.

Define the denominator-cleared polynomials
\[
Q=L(X^{19}+AX^{15}+BX^{14})+NX^9+D_*X^2+E_*,
\]
\[
J_{10}=L(184756X^{10}+8008AX^6+3003BX^5)+N,
\]
\[
J_1=L(20X^{19}+16AX^{15}+15BX^{14})+10NX^9+3D_*X^2+E_*.
\]
These are \(Lf/X,LH_{10}f,LH_1f\). Set
\(R_{10}=\operatorname{Res}_X(Q,J_{10})\),
\(R_1=\operatorname{Res}_X(Q,J_1)\).

The order-10 common-root condition implies \(NR_{10}=0\): if \(C=0\),
then \(N=0\); otherwise the witness is nonzero and the resultant vanishes.
The order-1 condition always implies \(R_1=0\). Indeed a nonzero witness
is a root of \(Q\), while a zero witness forces \(E_*=0\), making zero
a root of both \(Q\) and \(J_1\). These arguments retain coefficient-zero
cases rather than assuming them away.

The exact integer resultants have degrees 422 and 661. Direct exact division
in \(\mathbb Z[u]\) gives
\[
S_{10}=NR_{10}/L^{10},\qquad S_1=R_1/L^{10},
\]
of degrees 360 and 581. Both degrees survive modulo 101, and the reduced
polynomials are coprime. Gauss's lemma therefore gives
\(\gcd_{\mathbb Q[u]}(S_{10},S_1)=1\). Since \(L\ne0\), a
hypothetical solution would give \(S_{10}=S_1=0\), a contradiction.

This proves the exclusion for \(u\ne0,1\). The value \(u=0\) was
excluded before dividing by it, and \(u=1\) was excluded before canceling
\(u-1\); neither is silently discarded. Both are absent from the assigned
residue class. No conclusion about the otherwise exceptional \(u=1\)
collision is needed here.

## Independent replay

`verify_certificate.py` reconstructs the rational parametrization directly from
integer binomial coefficients and verifies
\(f(1)=f(u)=H_{15}f(u)=H_3f(u)=0\) as polynomial identities after clearing
denominators. It imports no CAS or producer arithmetic.

The maximum parameter degrees of the coefficients of \(Q,J_{10},J_1\)
are 25, 18, and 25. Their Sylvester determinants consequently have degree
bounds \(10\cdot25+19\cdot18=592\) and
\(19\cdot25+19\cdot25=950\). The checker evaluates the defining integer
Sylvester determinants at 593 and 951 distinct integer parameters, using
exact Bareiss division, and compares them to the supplied arrays. These
counts exceed the bounds and therefore certify both entire integer
polynomials. This also handles any specialization at which a leading
coefficient vanishes, because the full Sylvester matrix is retained.

It then verifies exact division by \(L^{10}\), preservation of all relevant
degrees modulo 101, both modular coprimality statements, and a coefficient
mutation control. Replay passed in about 132 seconds. The preserved
certificate SHA-256 is
`5a361c539843a71648b1c792367a3e4c7d2c12f56b71248ec79959398821183e`.

The modular gcd is used only to certify rational coprimality of already
certified integer polynomials with preserved degrees. There is no inference
from emptiness of an arbitrary modular affine variety to characteristic zero.
