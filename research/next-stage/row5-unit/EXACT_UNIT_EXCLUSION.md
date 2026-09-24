# Row 5: four exact unit-witness systems are impossible

This is a bounded research result. It addresses the subcases specified below and does not address a middle witness in the residue-zero cluster.

## Conditional branch statement

Work in characteristic zero. Write
\[
f=X^{20}-190X^{18}+1140a_3X^{17}+4845a_4X^{16}
 +184756a_{10}X^{10}+125970a_{12}X^8+EX,
\]
\[
E=189-1140a_3-4845a_4-184756a_{10}-125970a_{12}.
\]
Thus \(f(1)=0\), and the normalized degree-two derivative \(G_2=X^2-1\) vanishes at 1. Put
\[
G_j=\sum_{i=0}^j\binom ji a_iX^{j-i},
\qquad a_0=1,\quad a_1=0,\quad a_2=-1,
\]
where coefficients outside the displayed support are zero.

Suppose there is a root \(r\) of \(f\) such that:

1. \(f'(1)=0\);
2. \(G_4(r)=0\);
3. \(G_{10}(1)=0\);
4. either \(G_3(1)=0\) or \(G_3(r)=0\);
5. either \(G_{12}(1)=0\) or \(G_{12}(r)=0\).

**Proposition.** These conditions are inconsistent, in all four choices in items 4 and 5. No nonzero-coefficient assumption is needed in this proposition.

In the intended characteristic-17 row-5 application,
\[
\bar f=X^{17}(X-1)^2(X+2),\qquad \bar r=-2.
\]
An \(H_1\) witness in the residue-1 cluster must equal 1 exactly: that cluster contains the root 1 and an exact repeated root and has total multiplicity two. It is therefore exhausted by the repeated root. Every other common-root witness in that cluster also equals 1. The residue-\(-2\) cluster is simple, so every common-root witness there is the same exact root \(r\). The reduction of \(G_3\) is \((X-1)^2(X+2)\), explaining its two exact choices. Consequently the proposition applies whenever the \(H_1\) and \(G_{10}\) witnesses are in the residue-1 cluster, the \(G_4\) witness is in the residue-\(-2\) cluster, and the \(G_{12}\) witness is a unit. These cluster implications allow arbitrary ramification; they do not use unramified digit expansions.

The assertion that all relevant preliminary markings have their \(G_4\) witness near \(-2\) belongs to the separate residue enumeration. It is a hypothesis of this bounded application, not a conclusion of the present certificates.

## Exact elimination

Let \(s\) denote the chosen \(G_3\) witness and \(t\) the chosen \(G_{12}\) witness, with \(s,t\in\{1,r\}\). The derivative equations successively force
\[
a_3=-s^3+3s,\qquad
a_4=-r^4+6r^2-4a_3r,
\]
\[
a_{10}=44-120a_3-210a_4,
\]
\[
a_{12}=-t^{12}+66t^{10}-220a_3t^9-495a_4t^8-66a_{10}t^2.
\tag{1}
\]
In particular \(s=1\) gives \(a_3=2\). All coefficients in (1) are integer polynomials in \(r\). There has been no division by \(a_{10}\), any other coefficient, or a witness difference.

For each choice \((s,t)\), define integer polynomials
\[
\begin{aligned}
P_{s,t}(r)={}&r^{20}-190r^{18}+1140a_3r^{17}
 +4845a_4r^{16}\\
&+184756a_{10}r^{10}+125970a_{12}r^8+Er,
\end{aligned}
\]
\[
Q_{s,t}(r)=-3211+18240a_3+72675a_4
              +1662804a_{10}+881790a_{12}.
\tag{2}
\]
These are exactly \(f(r)\) and \(f'(1)\). A putative solution must make both vanish.

The certificate file **row5-unit-certificates.json** contains their full integer coefficient arrays, the arrays for \(a_3,a_4,a_{10},a_{12},E\), and integer polynomials \(A_{s,t},B_{s,t}\) and nonzero integers \(D_{s,t}\) satisfying
\[
A_{s,t}P_{s,t}+B_{s,t}Q_{s,t}=D_{s,t}.
\tag{3}
\]
Every array is in ascending degree. The certificate properties are:

| \((s,t)\) | \(\deg P\) | \(\deg Q\) | \(\deg A\) | \(\deg B\) | \(\nu_{17}(D)\) |
|---|---:|---:|---:|---:|---:|
| \((1,1)\) | 20 | 4 | 3 | 19 | 1 |
| \((1,r)\) | 20 | 12 | 11 | 19 | 2 |
| \((r,1)\) | 20 | 4 | 3 | 19 | 2 |
| \((r,r)\) | 20 | 12 | 11 | 19 | 2 |

Evaluating (3) at a common zero would give \(0=D_{s,t}\) in characteristic zero. This proves the proposition. In fact, the contradiction is global in \(r\); the congruence \(r\equiv-2\pmod{\mathfrak m}\) is needed only to identify the exact witness choices in the intended branch.

## Exact replay and its scope

The producer used polynomial Euclidean division over Python's exact Fraction type, followed by denominator clearing. The read-only **check_row5_unit.py** uses a separate route. It constructs \(a_3,a_4,a_{10},a_{12}\) directly from the general binomial formula for \(G_j\); forms \(f\) and its derivative as polynomials in \(X\) with integer-polynomial coefficients in \(r\); and evaluates them to reconstruct (2). It then checks (3) by integer convolution alone. It performs no polynomial gcd, rational division, or external CAS calls, and it imports no producer code.

The checker verifies coverage of exactly the four witness pairs, checks the exact normalizations and every imposed \(G_j\) equation, compares every coefficient with the saved arrays, and rejects a multiplier mutation separately in every case. All checks use explicit exceptions, so remain active under optimized Python.

Normal and optimized runs pass with identical JSON receipts:

    python3 -B check_row5_unit.py
    python3 -B -O check_row5_unit.py

The receipts are **verification.json** and **verification-optimized.json**. The certificate SHA-256 is

    c9cac222f898ebf56de2b94e8a0a40a4dfc9fafed937affe85de4f358b8a7102

Only the stated unit-witness subcases are excluded. No conclusion here covers a residue-zero \(G_{10}\) or \(G_{12}\) witness, a residue-zero \(H_1\) witness, the entire row-5 branch, or the entire seven-term support.
