# Family B: normalized characteristic-13 equations

The closed seed is
\[
h(X)=X^{20}+aX^{17}+bX^4+cX^3+dX.
\]
All coefficients may vanish; Hasse derivatives are used. The earlier lemma in
`work/casas-alvero-structural/sixterm/LAST_MASK_PROOF.md` handles the complete
chart \(a=0\), where only the monomial can have the CA property.

Suppose \(a\ne0\). Since
\(H_{17}h=\binom{20}{17}X^3+a=9X^3+a\) in characteristic 13,
a common root \(r\) of \(h,H_{17}h\) is nonzero. Replace \(h\) by
\(r^{-20}h(rX)\). Then this common root is 1, \(a=-9=4\), and
\[
h(1)=0\quad\Longrightarrow\quad d=-5-b-c.
\]
This scaling preserves every common-root condition. No coefficient other than
\(a\) is assumed nonzero.

Choose common roots \(u,v,w\) of \(h\) with Hasse derivatives 4, 3, and 1,
respectively. They may be zero or coincide. Directly from the binomial formula,
\[
H_4h=9X^{16}+4X^{13}+b,
\qquad H_3h=9X^{17}+3X^{14}+4bX+c,
\]
\[
H_1h=7X^{19}+3X^{16}+4bX^3+3cX^2+d.
\]
Thus set, in \(\mathbf F_{13}[u,v,w]\),
\[
b=-9u^{16}-4u^{13},\qquad
c=-9v^{17}-3v^{14}-4bv,\qquad d=-5-b-c.
\]
The necessary equations are precisely
\[
\begin{aligned}
E_4&=h(u)=u(5u^{19}+cu^2+d),\\
E_3&=h(v)=v(5v^{19}+v^{16}+10bv^3+d),\\
E_1&=h(w)=w(w^{19}+4w^{16}+bw^3+cw^2+d),\\
D_1&=H_1h(w)=7w^{19}+3w^{16}+4bw^3+3cw^2+d.
\end{aligned}
\]
The displayed factors \(u,v,w\) are retained. In particular \(b=0\),
\(c=0\), or \(d=0\) may be witnessed by zero, without imposing the
extra root condition \(h(X)/X=0\). There is no saturation, division by a
witness, distinctness condition, or affine-to-characteristic-zero inference.

The exact computation `normalized.sing` returns the Gröbner basis \([1]\)
for \(I=(E_4,E_3,E_1,D_1)\) in characteristic 13, in approximately 32 seconds.
The raw result and bounded runtime receipt are preserved. Certificate extraction
and independent arithmetic replay are separate verification steps. Both are
now complete through the alternative univariate route in `PROOF.md`; see
`REPORT.md` for the retained timeout and successful certificate details.

If the unit-ideal result is independently certified, no normalized \(a\ne0\)
CA polynomial exists even over \(\overline{\mathbf F}_{13}\). Combining with
the complete \(a=0\) lemma then excludes the entire closed seed, apart from the
monomial. The established valuation normalization and Lucas reduction would
then exclude characteristic-zero support \(\{3,10,16,17,19\}\). This last
transfer requires the valuation argument, including the retained unit root;
it does not follow merely by reducing arbitrary affine equations modulo 13.

## Characteristic-11 obstruction

The closed family in characteristic 11 contains the explicit nonmonomial CA
polynomial \(X^{20}+2X^4+X^3+5X\). Orders 3 and 4 share the root 7 with it;
order 1 shares the root 8; every other derivative shares zero. The exhaustive
`search_fp.py` script checks all 19 derivative gcds for each reported example.
It finds 20 examples in \(\mathbf F_{11}\), all with \(a=0\), and none
among the 28,560 nonmonomial coefficient tuples in \(\mathbf F_{13}\).
The latter finite search alone does not exclude algebraic-extension coefficients.
