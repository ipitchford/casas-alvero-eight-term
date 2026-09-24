# Independent audit of the quartic next-lift exclusion

23 September 2026. **PASS for sections 4 and 5 of `LIFT_CONSEQUENCES.md`, conditional on the already established sections 1–3.** No new numerical experiment was needed. This audit does not certify the separate inventory counts or any implementation computing the coefficients lambda_j.

The result excludes the following configuration throughout J=L=16: a17=a18=0 and every selected zero-residue middle witness is the exact mean. It does not exclude the whole J=L=16 stratum, J=16 with L<16, or unrestricted degree 20.

## 1. The first variation has the stated precision

Use delta=1/13 and the exact coefficient alternatives from section 3. Every unit root differs from its matching exact cube root of unity by valuation at least 2delta. To see this without an assumption on ramification, subtract the base polynomial X^17(X^3-1): its coefficient perturbations have value at least 2delta, and at the chosen unit residue the other root factors are units. Thus the same bound holds for the root difference.

The constants A_j obtained by triangular recursion at the exact cube roots lie in the unramified quadratic integer ring. For a zero-residue witness, the only possible term of order delta in its normalized equation is j*abar_(j-1)*w_j; every term involving a higher power of w_j has higher value. This proves the displayed formula

    d_j=-j*abar_(j-1)*x_j.

For a unit witness, its root perturbation and the perturbations of a2,a3 begin at order 2delta. At order delta only the previous coefficient variations contribute. This gives precisely

    d_j=-sum_(i=4)^(j-1) binom(j,i)*d_i*rho_j^(j-i).

Induction simultaneously proves nu(a_j-A_j)>=delta, so the divisions defining d_j are legitimate. The formulas permit an exact-zero witness and also a zero leading variation.

In G17, after division by 17*pi, the index-16 term is the only surviving nonconstant term. Its binomial coefficient is exactly 17. All lower indices have at least one additional factor of pi, and the leading degree-17 term has strictly larger valuation. Therefore

    bar(a17/(17*pi))=-abar16*x17.

In the divided f(1) identity, the unramified constant part has value at least one, the a2 and a18/17 terms have value at least 2delta, and a19/17 has value 3delta. Since 1140 is congruent to 1 modulo 17, the order-delta coefficient is exactly equation (F), including its sign and its coefficient on x17.

Under the affine change from the original first model to its canonical form, write x_j=kappa*(z_j-gamma) and x17=-kappa*gamma. Substitution into (F) and cancellation of the nonzero kappa gives (F'). This explicitly preserves the distinction between the translated H3 root and the original mean. The equation is only necessary; no first-variation emptiness conclusion follows.

## 2. The unit-root approximation in section 5 is modulo 17O

Assume a17=a18=0 and that every zero-residue middle witness is exactly zero. Set T=a2. The initial exact relations are a3=-1-3T and f(1)=0. Put

    Q_T(X)=X^3+3TX-1-3T=(X-1)(X^2+X+1+3T).

Every coefficient of f-X^17 Q_T belongs to 17O. Explicitly the discrepancies in degrees 18 and 17 are

    (190-3)T=17*11*T,
    (1140-1)a3=17*67*a3.

The middle ordinary coefficients are divisible by 17, a17 and a18 vanish, and the remaining coefficient 20a19 has value 16/13>1. This proves the required ideal membership; merely knowing positive valuation would not suffice.

Let A be the unramified quadratic integer ring containing the cube roots of unity. The three roots phi_rho(T) of Q_T are in A[[T]], with their indicated distinct residues. Their series converge for T=0 or any T of positive valuation, including fractional value 2/13.

For an actual unit root w of f, Q_T(w) belongs to 17O because w^17 is a unit. Factor Q_T(w) as the product of w-phi_rho(T) over its three series roots. Exactly one factor has positive valuation; the other two are units. Therefore the matching difference belongs to 17O. This factorization proves the precision directly over any ramified ambient extension and requires no integer-valued valuation assumption.

If a middle witness is zero, its coefficient a_j is exactly zero. Otherwise apply the triangular normalized equation to its unit witness. Inductively replacing earlier coefficients and the witness by congruent values modulo 17O preserves that congruence, since every normalized equation has integral coefficients and is monic in a_j. This constructs the claimed A_j(T) in A[[T]], with

    a_j-A_j(T) in 17O.

The coefficient ring is unramified; the parameter T itself is not assumed unramified.

## 3. The valuation contradiction is valid

The exact divided f(1) equation, with a17=a18=0, is

    -67-190T+sum_(j=4)^16 (binom(20,j)/17)*a_j+20a19/17=0.

Replacing a_j by A_j(T) introduces an error in 17O. Hence

    F(T)+20a19/17 is in 17O.

The original residue cut says F(0) reduces to zero. Because F(0) belongs to A, its valuation is at least one. All coefficients of F lie in A, so each is either a unit or has valuation at least one; this discreteness is used only for the fixed series coefficients.

The second summand has value 3/13<1. Consequently F(T) must have that same value. If T=0 its value is at least one. If nu(T)=2/13 and the linear coefficient is a unit, the linear term is uniquely smallest and the value is 2/13. If the linear coefficient is not a unit, the constant term has value at least one, the linear term has value at least 1+2/13, and all remaining terms have value at least 4/13. Their convergent sum therefore has value at least 4/13. None of these cases allows 3/13.

This proves the exclusion. The case of no zero-residue middle labels is included because its witness assumption is vacuous.

## Remaining scope

The canonical leading configuration with u=0, v nonzero, gamma=0 and every marked zero-middle root equal to gamma was a universal survivor of (F'). Section 3 makes gamma a simple leading root, so such equality of leading roots forces the actual witnesses to be the exact mean. Section 5 therefore excludes that configuration, rather than merely one chosen numerical representative.

Other zero-cluster witness placements and other quartic leading models remain. The argument supplies no whole-J16, whole-row8, degree-20, or all-degree Casas–Alvero proof.
