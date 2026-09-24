# Family B outcome

**Internally checked exclusion obtained.** The closed characteristic-13 seed
\(X^{20}+aX^{17}+bX^4+cX^3+dX\) has no nonmonomial CA polynomial. All
coefficient-zero cases and coincident or zero witnesses are included. Together
with the preceding valuation/Lucas lemma, this excludes centered degree-20
deficiency support \(\{3,10,16,17,19\}\).

The previous \(a=0\) lemma is reused. For \(a\ne0\), normalize an
order-17 common root to 1. A separate 2,086-term unit certificate excludes
\(b=0\). For \(b\ne0\), an order-4 witness parametrizes \(c,d\)
rationally; two univariate resultants and the identity
\(ACR_3+BDR_1=(u+1)^{17}\) give a contradiction. The only forbidden
denominators are justified explicitly in [PROOF.md](PROOF.md).

| Bounded computation | Result |
|---|---|
| All 14,640 nonmonomial F11 coefficient tuples | 20 examples, all a=0 |
| All 28,560 nonmonomial F13 coefficient tuples | No examples; by itself only a finite search |
| Original normalized three-variable ideal | Basis [1], about 32 seconds |
| Tracked three-variable lift | 110-second timeout, terminated; no certificate |
| Rational-parametrization resultants | Degrees 359 and 395, about 0.05 seconds |
| Separate b=0 lift | 2,086 coefficient terms, about 0.09 seconds |
| Independent standard-library replay, normal and -O | PASS, under one second |

The replay reconstructs the Hasse equations, checks the b=0 unit identity,
independently certifies both resultants at 685 exact extension-field points
under proved degree bounds 648 and 684, and checks the univariate Bézout
identity by multiplication. It reads the saved certificate and does not
rewrite producer logs or runtime receipts. See `verification.json` and
`verification-optimized.json`. The raw b=0 producer's printed `I*L` diagnostic
is not used as proof; direct multiplication in the independent checker is.

Key files are `PROOF.md`, `certificate.json`, `verify_certificate.py`,
`resultants.sing`, and `b_zero.sing`. The earlier necessary-equation derivation
and all bounded-run receipts, including the timeout, are retained.

Certificate SHA-256:
`981ff911b8493e9a3cb37dea620dd63249e6bd2bff9c93f16aec2670e88179c7`.

The remaining six-term supports are \(\{3,4,10,18,19\}\) and
\(\{4,5,10,17,19\}\). This result does not prove the requested seven-term
lower bound or the Casas–Alvero conjecture. Historical novelty has not been
established. Nothing was published.
