# Independent audit of the uniform obstruction, Sections 2–3

23 September 2026. Internal mathematical audit, not external refereeing or a novelty assessment.

**Result: no proof gap found in the normalization, coefficient cases, or Frobenius implication in Sections 2–3 of `../PROOF.md`.** The reconstruction of equations (2) and (14) also passes an independent standard-library integer-coefficient check. This audit does not certify the characteristic-zero transfer or the resultant computation; those have separate checks.

## Normalization and coefficient coverage

For p>7 and p!=17, Lucas gives exactly the three displayed Hasse polynomials in equation (6). Every other derivative order has zero constant coefficient and shares the root zero. Thus the three active equations cover the full CA property for this sparse family.

The a=c=0,d!=0 case fails because the H1 and h/X equations would force 6d=0. If a=0,c!=0, the H3 common root is nonzero and can be scaled to 1. The conclusions c=-35,d=34 follow directly. The H1 root w is nonzero and has w^(p+6)=17 and w^2=51/35. Since p+6 is odd, Bezout for the exponents puts w in F_p. The obstruction integer in equation (7) is correct. This case includes every possible degeneration with a=0.

If a!=0, the H_(p+3) root is nonzero, so scaling it to 1 gives a=-35 and h(1)=0. For c!=0 the H3 common root is nonzero. For c=0, v=1 is a valid common root because H3(1)=35-35=0. In either case H3(v)=0 gives c=35v^p(1-v^4), and h(v)/v=0 then gives d=34v^(p+6). Since 34 is invertible and v!=0, d!=0. The last equation in (8) is precisely c+d=34, obtained from h(1)=0.

The identity 3h/X-H1=-4X^(p+6)+2d is correct. Applied at w, it gives w^(p+6)=17v^(p+6), hence equation (9). Dividing h(w)/w by v^(p+2), then using t=w/v and equation (9), gives the undivided equation (10). This division uses only v!=0.

The exclusion of D=51-35t^2=0 is rigorous in the algebraic closure: equation (10) forces t^p=1, and the only root of X^p-1 is 1. Then D=16, a contradiction. This avoids a spurious exceptional prime 137 produced by eliminating only some of the equations. It justifies the rational T=P/Q, and Frobenius ensures Q(z^p)=Q(z)^p!=0.

## Frobenius and the fixed integer numerator

With y=v^2 and T=v^4, equation (8) becomes exactly v^p(34Ty+35(1-T))=34. Its fourth power has the stated coefficient T(z)^p=T(z^p)=T(psi(z)). This uses only that T has prime-field coefficients and its denominators are nonzero.

Reduction of (A0*y+B0)^4 modulo y^2-T gives

    E0=A0^4*T^2+6*A0^2*B0^2*T+B0^4,
    O0=4*A0*B0*(A0^2*T+B0^2).

The displayed norm equation is necessary even when O0 vanishes; no division by O0 occurs. Squaring can add solutions, but cannot discard genuine ones. Only necessity is used subsequently.

Writing T=P/Q, direct substitution gives T(psi)=R/S with the definitions in Section 1. Furthermore E0=E/Q^6 and O0=O/Q^5. Hence the rational numerator before cancellation is

    (R*E-34^4*S*Q^6)^2 - P*Q*R^2*O^2,

and its denominator is S^2*Q^12. The checker `check_proof_formula.py` constructs these integer polynomials independently, confirms that their numerator content is exactly 17^8, confirms degree 72 and primitivity after division, and matches every saved coefficient of H.

Since S=17^4*(3z^6-595), its denominator check gives exactly

    S^2*Q^12 = 17^8*z^24*(35z-51)^12*(3z^6-595)^2.

This proves equation (14) by an exact polynomial identity. Since p!=17, the numerical cancellation is legitimate. The final denominator factor is nonzero because

    51-35*psi(z) = 17*(3z^6-595)/z^6.

Thus H(z)=0 follows. Frobenius then gives H(z^p)=0, and z^p=289/z^6 with z!=0 gives C(z)=0. A common root forces the specialized resultant to vanish, including when a leading coefficient drops. No converse implication from H=C=0 is claimed or needed.

## Reproducibility and limits

Normal and optimized Python checks pass in `check-proof-formula.json` and `check-proof-formula-optimized.json`. The H source hash is recorded in both receipts. The calculation uses plain integer lists, no CAS and no assertions disabled by optimization.

This audit verifies the mathematical implication on which the practical necessary tests depend. The separate bounded scan and exact v-lift in this directory establish the small-prime existence classification described in `STRUCTURAL_BOUNDARIES.md`, Section 10. They do not establish a full list of exceptional primes.
