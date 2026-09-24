# Independent audit of Family A's characteristic-zero lifting route

**Verdict: PASS for the stated closed support.** I found no fatal mathematical
gap in `A/A_EXCLUSION_PROOF.md`. This is an internal adversarial audit and exact
replay, not formal verification, an external referee report, or a novelty
assessment. Family C remains unresolved; no seven-term bound follows yet.

## Scope checked

The audited claim is that a monic characteristic-zero CA polynomial with zero
as a root and support contained in \(\{20,17,16,10,2,1\}\) must be
\(X^{20}\). Every displayed coefficient is allowed to vanish. I checked the
seed classification, the normalization and lifting implications, the forced
coefficient formulas, and the final characteristic-zero resultant contradiction.

### Complete residual charts

The \(a=0,b\ne0\) chart is covered by the replayed ordinary-ideal unit
certificate, without dividing out zero witnesses. The \(a=b=0,c\ne0\)
normalization gives \(c=5,d=7\); independently, I verified
\(H_1-7(h/X)=X+10\) and \((h/X)(3)=12\), which exclude it. The remaining
nonmonomial binomial chart is excluded because \(20\not\equiv1\pmod{13}\).

For \(a\ne0\), the three resultant branches are exhaustive: \(b=0\);
\(b\ne0\) with an order-16 witness equal to 1; and \(b\ne0\) with that
witness different from 0 and 1. The coefficient factors multiplying the
resultants retain \(c=0\) and \(d=0\). The generic quotient is a polynomial,
and the division by \(u-1\) is used only where \(u\ne1\).

I checked the interpolation degree bounds: 38 and 39 for the affine branches,
and \(18(19+18)+18=684\), \(18(19+19)+18=702\) for the generic branch.
The extra 18 comes from the coefficient factor. The finite-field points are
distinct, the cubic defining the field is irreducible, and the counts exceed
the bounds. The independent Sylvester replay passes all branches.

### Valuation normalization and root collision

The binomial-normalized coefficient induction is valid over an arbitrary
extension of the 13-adic valuation; no discreteness is needed. Initial scaling
by a root of minimum valuation makes all roots integral and preserves a unit
root, so the reduction is nonmonomial. The complete \(a=0\) classification
then forces the ordinary \(X^{17}\) coefficient to be a unit. Since 1140
is a 13-adic unit, any order-17 common root is a unit. Scaling that root to 1
therefore preserves integrality of every root.

I independently derived all Hasse derivatives of the residual polynomial and
computed
\[
\gcd(h_0,H_{17}h_0)=\gcd(h_0,H_{16}h_0)=\gcd(h_0,H_2h_0)=X-1,
\qquad h_0'(1)=11.
\]
Thus every order-16 and order-2 witness reduces to 1. The exact collision
argument is sound: write \(f=(X-1)g\). Synthetic division gives integral
coefficients for \(g\), and an integral root \(r\equiv1\) satisfies
\(g(r)\equiv g(1)=f'(1)\equiv11\). Hence \(g(r)\) is a unit and
\(f(r)=0\) forces \(r=1\). This does not require completeness, an
unramified field, or an invocation of Hensel's lemma.

### Exact coefficients and characteristic-zero conclusion

Direct independent use of the binomial formula gives
\[
A=-1140,\quad B=14535,\quad
C=-1589350-45e,\quad D=1575954+44e.
\]
The order-10 binomial coefficients are exactly 184756, 19448, and 8008.
The two resultant identities were replayed at 30 and 39 integer parameters
using exact Bareiss determinants. Their affine Sylvester degree bounds are
29 and 38, so these evaluations certify the whole integer polynomials.
Both leading coefficients survive modulo 101, and the modular gcd is 1.
Gauss's lemma therefore rules out a common nonconstant rational factor.

For \(e\ne0\), an order-10 common root cannot be zero, so the order-10
resultant vanishes. The order-1 condition always forces its resultant to
vanish, including when \(D=0\): then zero is itself a common root of
\(f/X\) and \(H_1f\). For \(e=0\), the separate checked inequality
\(R_1(0)\ne0\) supplies the contradiction. Consequently the proof covers
the closed support, not only the exact six-term stratum.

## One wording clarification requested

Section 1 should state the seed classification over **any algebraically closed
field of characteristic 13**, rather than only an algebraic closure of the
prime field. A valuation residue field for arbitrary characteristic-zero
coefficients can be transcendental over the prime field. The displayed
polynomial identities already prove the universal statement, so this is a
quantifier clarification and requires no additional computation. This request
was sent to the author during the audit.

## Replay evidence

- `A_seed_zero_replay.json`: the 1,935-term ordinary-ideal unit certificate.
- `A_seed_univariate_replay.json`: all three classification branches.
- `A_collision_replay.json`: 69 exact integer determinants, preserved modular
  degrees, gcd 1 modulo 101, and the nonzero order-1 resultant at zero.
- `check_A_formulas.py`, `A_formula_replay.json`: independently reconstructed
  Hasse gcds, the simple-root value, coefficient formulas, and lower chart.

All reported replays passed. The former nonempty-modular-mask obstruction
remains true; this lifting proof uses the residual point's simple-root
structure and does not reinterpret that obstruction as modular emptiness.
