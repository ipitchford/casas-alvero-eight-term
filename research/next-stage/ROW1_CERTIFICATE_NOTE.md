# Independent row-1 finite identities

The checks here concern two exact algebraic ingredients. They do not, on their own, exclude a characteristic-zero branch or establish an eight-term theorem.

## 1. Integer Bézout certificate with a sharp constant valuation

Define
\[
P=-4844X^{19}+19380X^{18}-14535X^{16}-1140X^2+1139,
\]
\[
Q=-14516X^{19}+38760X^{18}-2280X^2.
\]
The file **row1-certificate.json** contains ascending integer coefficient arrays for degree-18 polynomials \(A,B\) satisfying
\[
AP+BQ=D,\qquad
D=2347990055314667642830371373680474152955750087350688785027939089482846402772.
\]
The exact constant has
\[
\nu_{17}(D)=3,\qquad D/17^3\equiv13\pmod{17}.
\]
The certificate is primitive: the gcd of \(D\) and every multiplier coefficient is 1. It was produced independently by a polynomial extended Euclidean algorithm over Python's exact Fraction type, followed by denominator clearing. That calculation took ten Euclidean steps. No rational gcd or resultant output from the other producer was imported.

The read-only checker **check_row1_certificate.py** reconstructs \(P,Q\) from the displayed formulas and verifies the integer identity by coefficient convolution. It uses no polynomial division, external algebra package, or producer code. It computes the 17-adic valuation by repeated integer division, checks primitivity, and rejects both a one-coefficient change in \(A\) and a change of \(D\). All failures raise explicit exceptions; checks remain active under optimized Python.

The certificate SHA-256 is

    e43bd1bf6710a1ae682e1603d82137ed26e43b2d83e47a25a38b5aa8868d928e

For any integral input \(x\) in any extension of the 17-adic valuation, the identity implies
\[
\min\{\nu(P(x)),\nu(Q(x))\}\le3
\]
when \(\nu(17)=1\). Indeed \(A(x),B(x)\) are integral; if both displayed values had valuation greater than 3, their linear combination could not equal \(D\). This implication permits arbitrary ramification. The certificate does not justify imposing the two polynomial values, or any particular lower bound on them, without the separate characteristic-zero proof.

## 2. Complete binary residue checks for two four-index sets

The two exact-support families considered have full deficiency sets
\[
S_1=\{7,8,10,16,17,19\},\qquad
S_2=\{6,10,15,16,17,19\}.
\]
Their middle active indices are respectively
\[
J_1=\{7,8,10,16\},\qquad J_2=\{6,10,15,16\}.
\]
On the normalized characteristic-17 row-1 seed
\(h=X^{20}-X^3=X^3(X-1)^{17}\), every common-root residue belongs to \(\{0,1\}\). Put \(a_0=1,a_1=a_2=a_3=0\). For \(4\le j\le16\), use a marked root \(w_j\in\{0,1\}\) at active indices and set \(w_j=0\) otherwise. The normalized derivative equation determines
\[
a_j=-\sum_{i<j}\binom ji a_iw_j^{j-i}\pmod{17}.
\]
Inactive coefficients are therefore zero. Every one of the \(2^4=16\) assignments is enumerated for each \(J\), and the checker independently reevaluates all reconstructed \(G_j(w_j)\).

The given first divided constraint is
\[
W=-133+\sum_{j=4}^{16}
\left((19-j)-2\binom{20-j}{3}\right)
\frac{\binom{20}{j}}{17}\,a_j
=0\pmod{17}.
\]
The integer quotients are checked before reduction. In each of the two enumerations, exactly one marking satisfies this equation:
\[
w_j=0\quad(j\in J\setminus\{16\}),\qquad w_{16}=1,
\]
\[
a_j=0\quad(j\in J\setminus\{16\}),\qquad a_{16}=-1.
\]
The full 32-assignment records are in **row1_binary_census-verification.json**; **check_row1_binary_census.py** reconstructs them with standard-library integer arithmetic. This is an exhaustive binary residue calculation, not a test restricted to a convenient subset of witnesses. It does not assert that the one surviving marking lifts.

For these two exact supports, the closed visible mask at 17 permits only ordinary \(X^3\) and \(X\) lower terms: indices 2, 3, and 18 are absent exactly. Comparing with the exhaustive nine-seed classification, the only nonmonomial row with those three ordinary coefficients zero is row 1. Thus, once the established integral normalization and retained-unit-root argument are applied, this row is the globally required reduction for these two supports. The binary calculation is still only the first necessary lifting constraint within that row.

## Replay receipts

Both scripts pass normally and under Python optimization, with identical JSON output:

    python3 -B check_row1_certificate.py
    python3 -B -O check_row1_certificate.py
    python3 -B check_row1_binary_census.py
    python3 -B -O check_row1_binary_census.py

Frozen receipts are **row1_certificate-verification.json**,
**row1_certificate-optimized-verification.json**,
**row1_binary_census-verification.json**, and
**row1_binary_census-optimized-verification.json**.
These certify the displayed identities and bounded marking coverage. The separate valuation argument is responsible for any subsequent branch exclusion.
