# Outcome of the u=v branch attack

**Both assigned collision branches are excluded:**
\((\bar v,\bar u,\bar w)=(2,2,1)\) and \((2,2,4)\).
The result uses the previously audited normalization and residue classification.
It does not by itself exclude the other C branches or establish the seven-term
bound.

The primary proof, `JET_PROOF.md`, is small. A unit Jacobian first strengthens
the congruences on the shared witness and cubic coefficient. First jets and the
divided order-10 derivative exclude the branch with \(\bar w=4\). In the
\(\bar w=1\) branch, a second unit-Jacobian step supplies the additional
precision needed to force an order-10 witness within \(13\mathcal O\) of 4;
the root equation then contradicts the checked nonzero residue
\(f(4)/13=6\). The proof allows arbitrary ramification and ordered value
groups. `check_jets.py` and its normal and optimized receipts verify every
integer jet, determinant, linear solution, root multiplicity, and polynomial
gcd used in that argument.

An independent larger proof is retained in `RESULTANT_PROOF.md`. Rational
parametrization yields integer resultants of degrees 422 and 661, whose only
common factor after including the zero-coefficient factor is \(L^{10}\),
where \(L\) is a forbidden denominator. The read-only checker independently
certifies the resultants with 1,544 exact integer determinants, verifies exact
division by \(L^{10}\), and proves quotient coprimality using a
degree-preserving reduction modulo 101. It passed in 131.6 seconds. The bounded
Singular producer completed in under one second.

The exceptional values \(u=0,1\) are excluded by the target residue
\(\bar u=2\). The potential denominator \(L=0\) is separately excluded
by \(\gcd(L,N)=1\); also \(L(2)\equiv4\pmod{13}\). No denominator,
coefficient-zero case, or witness division is omitted silently.

Files:

- `JET_PROOF.md`, `check_jets.py`, `jet-verification*.json`: primary proof and
  small exact replay.
- `RESULTANT_PROOF.md`, `certificate.json`, `verify_certificate.py`,
  `verification.json`: independent characteristic-zero resultant route.
- `collision.sing`, its log and bounded runtime receipt: original producer.

No external publication or outreach occurred. The written proof is undergoing
independent internal audit; novelty and external validation are separate claims.
