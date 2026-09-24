# Full degree-20 reduction at 5

This is a structural reduction for the unrestricted problem, not an exclusion. It uses the known bad-prime phenomenon for degree4 in characteristic5 and must not be claimed as a new solution.

After translating the mean root to zero and normalizing integrally, the normalized-coefficient induction and Lucas's theorem give
\[
\bar f=X^{20}+aX^{15}+bX^{10}+cX^5=q(X)^5,
\quad q=X^4+AX^3+BX^2+CX.
\]
The residue field may be extended to an algebraic closure. Frobenius and the Hasse conditions imply that q is a characteristic-5 Hasse-CA quartic. A retained unit root rules out the monomial. The missing X19 coefficient of f does not imply that q is centered: the coefficient A must initially be retained.

Translate q's unique H3 root, namely A, to zero. This is an internal classification step, not a permitted arbitrary translation of the original characteristic-zero centered polynomial. The translated quartic has shape
\[
Q=X^4+UX^2+VX.
\]
If U=0,V!=0, a common root of Q and H1Q is nonzero. From Q it satisfies r^3=-V, while H1Q(r)=-r^3+V=2V!=0, impossible. If U=V=0, q is a fourth power; since its original root0 and retained nonzero root are distinct, this case is impossible too.

Thus U!=0. Normalize an H2 witness to1. Since H2Q=X²+U, this gives U=-1. The equation Q(1)=0 gives V=0. Conversely X4-X² is Hasse-CA in characteristic5. Therefore q has one double root at its own mean, and two simple roots equally spaced from it.

Because the original q has a root at0, there are two cases up to a scaling that preserves0:

1. The root0 is the double root: q=X4-X² and \(\bar f=X^{20}-X^{10}\). Residue clusters have sizes10,5,5 at0,1,-1.
2. The root0 is a simple root: choose the double root as1. Then q=X(X-1)²(X-2)=X4+X3+3X and \(\bar f=X^{20}+X^{15}+3X^5\). Residue clusters have sizes5,10,5 at0,1,2.

Both cases genuinely satisfy every Hasse common-root condition. Neither can be eliminated by residue emptiness. A proof in degree20 would need a lifting obstruction covering the normalized coefficients invisible modulo5, including ramified root displacements. The two cases cover arbitrary original supports; they do not presuppose sparsity or integral-valued root differences.

`check_reduction.py` verifies the derivative identities, binomial visibility, Frobenius factorizations, cluster multiplicities and all nineteen Hasse witness conditions. The completeness argument is the elementary quartic calculation above.
