# Exclusion of the second residue configuration

**Proposition.** A nontrivial centered characteristic-zero Casas–Alvero
polynomial of degree twenty with exact deficiency support
\[
S=\{2,4,10,17,18,19\}
\]
cannot have the characteristic-seventeen reduction
\[
h(X)=(X^{17}-1)X(X^2-3).
\]

Write \(H_kf=f^{(k)}/k!\) and
\[
f(X)=\sum_{j=0}^{20}\binom{20}{j}a_jX^{20-j},
\qquad
G_j(X)=\frac{H_{20-j}f(X)}{\binom{20}{j}}.
\]
We use the integral normalization in which the mean root is zero,
\(a_0=1\), \(a_1=a_{20}=0\), and the nonzero nonleading normalized
coefficients have precisely the indices in \(S\). Let \(O\) be the
valuation ring of a field containing the coefficients and roots, with
valuation normalized by \(\nu(17)=1\) and \(\nu(0)=+\infty\).
No unramifiedness assumption is imposed on this field. A bar denotes
reduction in its residue field.

## 1. Normalization and integral divided equations

The residue roots \(0\) and \(\pm\sqrt3\) of \(h\) are simple,
whereas the root \(1\) has multiplicity seventeen. The common root of
\(f\) and \(G_2\) reduces to \(1\). Scaling this actual root to
\(1\) gives
\[
a_2=-1,\qquad f(1)=0.
\]
Put \(a=a_4\), \(b=a_{10}\), \(T=H_3f(1)\), and let \(F\) be
the ordinary coefficient of \(X^2\). Then
\[
\begin{aligned}
f(X)={}&X^{20}-190X^{18}+4845aX^{16}+184756bX^{10}
       +DX^3+FX^2+EX,\\
D={}&153900-2713200a-22170720b+T,\\
E={}&189-4845a-184756b-D-F.
\end{aligned}
\tag{R2.1}
\]
All coefficients are integral, and \(\nu(T),\nu(F)>0\).

The selected common roots for \(H_1,H_2,H_3\) all lie in the residue
class of \(1\). For \(H_1\), every other residue class is simple.
For \(H_2\), the only common residue locations are \(0\) and \(1\),
but the zero class contains only the exact mean root, and
\(H_2f(0)=F\ne0\) by the exact-support assumption. For \(H_3\),
the only common residue location is \(1\).

Expand
\[
f(1+Y)=\sum_{k=0}^{20}c_kY^k.
\]
We have
\[
c_0=0,\quad c_3=T,\quad c_{17}=-2280,\quad c_{18}=0,
\quad c_{19}=20,\quad c_{20}=1,
\]
and \(c_4,\ldots,c_{16}\in17O\). Direct expansion gives
\[
\begin{aligned}
c_1&=-5353725a-42678636b+304589+2T+F,\\
c_2&=-7558200a-58198140b+432820+3T+F,\\
c_2-c_1&=T+17(7543-129675a-912912b).
\end{aligned}
\tag{R2.2}
\]

We first prove that \(T,F\in17O\). Suppose that
\[
\mu=\min\{\nu(T),\nu(F)\}<1.
\]
If \(\nu(c_1)=\mu\), every nonzero displacement \(z\) of a root
in the class of \(1\) has \(\nu(z)\ge\mu/16\): a smaller value
would make \(c_{17}z^{16}\) uniquely smallest in
\(f(1+z)/z\). At a repeated root, however, the constant term
\(c_1\) of \(f'(1+z)\) is then uniquely smallest. The terms from
\(c_2,c_3\) have larger value; the terms from degrees four through
sixteen have value at least one; the degree-seventeen term has an
additional factor of seventeen; and the degree-nineteen term has value
at least \(18\mu/16>\mu\). The same contradiction is immediate
if the repeated root is exactly \(1\).

Consequently \(\nu(c_1)>\mu\). Equation (R2.2) forces
\(\nu(T)=\nu(F)=\mu\) and cancellation of \(2T+F\). Let
\(1+z\) be the selected \(H_3\) common root. Its displacement is
nonzero, and its derivative equation forces
\[
\nu(z)=\frac{\mu}{17}.
\]
Indeed, only the constant term \(T\) and the degree-twenty
contribution \(1140z^{17}\) can have least value: all intervening
coefficients in the \(H_3\) equation are divisible by seventeen.
But in \(f(1+z)/z\), the term \(c_{17}z^{16}\) then has value
\(16\mu/17\), strictly smaller than every other term. This is
impossible, proving \(T,F\in17O\).

Every nonzero root displacement in the class of \(1\) now has value
at least \(1/16\). Applying the three derivative equations at their
selected roots gives
\[
\nu(c_1)>1,\qquad \nu(c_2)>1,\qquad \nu(T)>1.
\tag{R2.3}
\]
Here the degree-nineteen term of \(H_2\) must be retained:
\(\binom{19}{2}=171\) is a unit modulo seventeen, and its displacement
exponent is seventeen, so its value is at least \(17/16>1\).
A zero displacement makes the corresponding constant coefficient zero
and is included in these inequalities. Dividing (R2.2) by seventeen
therefore yields
\[
7543-129675\bar a-912912\bar b=0.
\tag{R2.4}
\]

## 2. Residue coverage and simple outside witnesses

Since \(a,b\ne0\), the selected \(G_4\) and \(G_{10}\) common
roots cannot be the exact mean. Their residues belong to
\(\{1,s,-s\}\), where \(s^2=3\). The equations
\[
G_4(X)=X^4-6X^2+a,
\qquad
G_{10}(X)=X^{10}-45X^8+210aX^6+b
\]
give the complete table

| \(\bar a\) | \(\bar b\) | Left side of (R2.4), modulo \(17\) |
|---:|---:|---:|
| \(5\) | \(14\) | \(2\) |
| \(5\) | \(8\) | \(6\) |
| \(9\) | \(7\) | \(5\) |
| \(9\) | \(6\) | \(0\) |

Thus
\[
(\bar a,\bar b)=(9,6),
\]
and both selected roots reduce to one of \(s,-s\).

Choose the exact comparison roots \(r_0=\pm\sqrt3\) in the
unramified quadratic extension. The coefficients of \(f\) differ
from those of the integer representative
\((X^{17}-1)X(X^2-3)\) by elements of \(17O\). Indeed,
\(T,F\in17O\), and the relevant middle binomial coefficients are
divisible by seventeen. Hence \(\nu(f(r_0))\ge1\), while
\(f'(r_0)\) is a unit. Every actual root \(r\) in the corresponding
simple residue class satisfies \(\nu(r-r_0)\ge1\): otherwise the
linear Taylor term would be uniquely smallest. This argument also
applies in a ramified ambient extension.

At the selected \(G_4\) root,
\[
a=9-(r^2-3)^2,
\]
so \(\nu(a-9)\ge2\). The \(G_{10}\) equation at its selected
root then gives \(\nu(b+47628)\ge1\). Equation (R2.2) consequently
improves to
\[
c_2-c_1-T\in17^2O.
\tag{R2.5}
\]
At these residues, \(\overline{c_4/17}=8\). In particular,
\(\nu(c_4)=1\), so the seventeen roots in the class of \(1\)
cannot all coincide exactly at \(1\).

## 3. The first nontrivial unit-cluster model

Let \(\delta\) be the least valuation of a nonzero displacement
from \(1\) among the roots in its residue class. By (R2.3),
\(\delta>1/16\). Descending through the three witness equations
gives
\[
\begin{aligned}
\nu(T)&\ge\min\{1+\delta,17\delta\}=1+\delta,\\
\nu(c_2)&\ge\min\{1+2\delta,17\delta\},\\
\nu(c_1)&\ge\min\{1+3\delta,18\delta\}.
\end{aligned}
\tag{R2.6}
\]
The term \(17\delta\) in the second bound comes from the
degree-nineteen contribution to \(H_2\). Combining (R2.5) and
(R2.6) improves the first bound to
\[
\nu(T)\ge\min\{1+2\delta,17\delta,2\}.
\]
If \(\delta<1/13\), a root attaining this value would make
\(c_{17}z^{16}\) uniquely smallest in \(f(1+z)/z\). Each
lower-degree contribution has value greater than \(16\delta\)
by these inequalities, as do the degree-nineteen and degree-twenty
contributions. Therefore \(\delta\ge1/13\), and
\[
\nu(c_1)\ge\frac{16}{13},\qquad
\nu(c_2)\ge\frac{15}{13},\qquad
\nu(T)\ge\frac{15}{13}.
\tag{R2.7}
\]

Choose \(\pi\) with \(\pi^{13}=17\). The reduction of
\(\pi^{-17}f(1+\pi Y)\) is
\[
L(Y)=-2Y^{17}+8Y^4+\lambda_2Y^2+\lambda_1Y.
\tag{R2.8}
\]
There is no cubic term because \(\nu(T)>14/13\). All seventeen
roots in the class are captured by this scaling, since their
displacements have value at least \(1/13\); the other three roots
contribute a unit local factor. The selected \(H_1,H_2,H_3\)
witnesses reduce to common roots of \(L\) with its corresponding
Hasse derivatives. Put \(\kappa=8\), so that
\(H_3L=4\kappa Y\).

We first show that \(\lambda_1=0\). Otherwise zero is a simple
root of \(L\). Its subcluster contains only one exact root, already
the root \(1\), and must contain the \(H_3\) witness. Thus that
witness is exactly \(1\) and \(T=0\). Equation (R2.5) then forces
\(\lambda_2=0\). Now \(H_2L=6\kappa Y^2\), so the \(H_2\)
witness also lies in this single-root subcluster and equals \(1\).
It follows that \(c_2=0\), and (R2.5) gives \(c_1\in17^2O\),
contrary to \(\lambda_1\ne0\).

Suppose next that \(\lambda_2\ne0\). The zero root of \(L\)
has multiplicity two. Let \(\eta\) be the scaled residue of a
repeated root of \(f\). If \(\eta=0\), that repeated root must
equal \(1\): a distinct repeated root together with \(1\) would
require at least three roots in this size-two subcluster. All roots
of the subcluster therefore equal \(1\). The \(H_3\) witness is
there too, so \(T=0\). But then (R2.5) contradicts
\(\nu(c_2)=15/13\), since \(\nu(c_1)>16/13\).

If \(\eta\ne0\), the equations \(L(\eta)=L'(\eta)=0\) imply
\[
\eta^2=-\frac{\lambda_2}{2\kappa},
\qquad
\eta^{13}=-\frac{\kappa}{2}.
\]
The \(H_2\) common witness has a nonzero scaled location \(v\),
and its equations give
\[
v^2=-\frac{\lambda_2}{6\kappa},
\qquad
v^{13}=-\frac{5\kappa}{2}.
\]
Consequently \(\rho=v/\eta\) satisfies
\[
\rho^2=\frac13,
\qquad \rho^{13}=5.
\]
In characteristic seventeen,
\[
\rho^{13}=\rho\left(\frac13\right)^6=8\rho,
\]
so \(\rho=7\). Its square is \(15\), whereas \(1/3=6\), a
contradiction over the full algebraic closure. Hence \(\lambda_2=0\).

We have proved
\[
L(Y)=Y^4(-2Y^{13}+\kappa).
\tag{R2.9}
\]
Its thirteen nonzero roots are simple, and \(H_1L,H_2L,H_3L\)
vanish only at zero. All three selected derivative witnesses therefore
belong to the size-four inner subcluster containing the exact root \(1\).

## 4. A good-characteristic cluster lemma

**Lemma 4 (separated-cluster collapse).** Let a separated cluster contain \(m\) roots of a
polynomial, counted with multiplicity. Suppose the cluster contains a
common root of \(f\) and \(H_kf\) for every \(1\le k<m\).
If every degree-\(m\) Hasse–Casas–Alvero polynomial over the
algebraic closure of the residue field is a power of a linear
polynomial, then all roots of the cluster coincide exactly.

**Proof.** If the cluster is not already collapsed, center at a root
and scale by a greatest distance between roots in the cluster. The
normalized cluster polynomial is integral and has degree \(m\),
with at least two distinct residue roots. Every outside root is
strictly farther away. After normalization, the outside factor thus
reduces to a nonzero constant, and its nonconstant coefficients have
positive valuation. The Hasse product rule transfers the selected
incidences to the residue cluster polynomial. It is a nontrivial
degree-\(m\) Hasse–Casas–Alvero polynomial, contradicting the
hypothesis. A greatest internal distance exists because the cluster
is finite. The argument permits arbitrary ramification. \(\square\)

For \(m=4\) in characteristic seventeen, the hypothesis has an
elementary proof. Center the \(H_3\) common root and make the
polynomial monic, obtaining
\[
q(X)=X^4+AX^2+BX.
\]
If \(A=0\) and \(B\ne0\), a common root of \(q\) and \(q'\)
cannot be zero, and the two nonzero-root equations contradict
\(3B\ne0\). If \(A\ne0\), an \(H_2\) common root is nonzero;
scaling it to one gives \(A=-6\) and then \(B=5\). However,
\[
\operatorname{disc}(X^4-6X^2+5X)=4725\not\equiv0\pmod{17},
\]
so this polynomial has no repeated root. It cannot satisfy the
\(H_1\) condition. Thus every quartic Hasse–Casas–Alvero
polynomial in characteristic seventeen is a fourth power of a
linear polynomial.

Apply Lemma 4 to the inner cluster in (R2.9). All four roots
coincide at \(1\), giving
\[
c_1=c_2=T=0.
\]
Equation (R2.2) now yields
\[
b=\frac{7543-129675a}{912912}.
\tag{R2.10}
\]
The denominator is a seventeen-adic unit. Since
\(\nu(a-9)\ge2\), we also have \(\nu(b-B)\ge2\), where
\[
B=\frac{7543-129675\cdot9}{912912}.
\tag{R2.11}
\]

## 5. The final simple-root lift obstruction

Evaluate the exact family determined by \(c_1=c_2=T=0\) at
\(a=9\), \(b=B\). Modulo \(X^2-3\), its relevant values
modulo \(17^2\) are
\[
\begin{aligned}
f(r_0)&\equiv170r_0,&
f'(r_0)&\equiv283r_0+130,\\
G_{10}(r_0)&\equiv204,&
G_{10}'(r_0)&\equiv92r_0.
\end{aligned}
\pmod{17^2}
\tag{R2.12}
\]
The actual parameters differ from \(9,B\) by elements of
\(17^2O\). Their effect on \(f\) belongs to \(17^3O[X]\),
and their effect on \(G_{10}\) belongs to \(17^2O[X]\).

The actual simple root selected by \(G_{10}\) has the form
\(r=r_0+17h\), with \(h\in O\). Reducing \(f(r)/17=0\)
gives
\[
0=10\bar r_0+11(\bar r_0+1)\bar h,
\qquad \bar r_0^2=3.
\]
The equation \(G_{10}(r)/17=0\) would therefore require
\[
0=12+7\bar r_0\bar h
 =\frac{12\bar r_0-4}{\bar r_0+1}.
\tag{R2.13}
\]
The denominator is nonzero. The numerator forces \(\bar r_0=6\),
whose square is \(2\), not \(3\), in characteristic seventeen.
This contradiction covers both signs of \(\sqrt3\), and hence all
four oriented choices of the \(G_4\) and \(G_{10}\) outside
witnesses. It proves the proposition. \(\square\)
