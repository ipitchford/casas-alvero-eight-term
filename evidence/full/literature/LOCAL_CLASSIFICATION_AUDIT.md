# Independent audit of the unrestricted local reductions

23 September 2026. Read-only audit of the producer files. No exclusion of
characteristic-zero lifts is claimed.

**Conclusion:** the two-adic residue census and five-adic two-shape
classification are correct within the scope below. No mathematical error
was found. Their completeness over algebraically closed residue fields
comes from explicit algebraic arguments, not from finite-field searches.
Both leave genuine residue solutions, and neither proves degree 20.

Audited files:

- `../two_adic/enumerate_residue_patterns.py` and its two JSON receipts.
- `../five_adic/REDUCTION.md` and `check_reduction.py`.

## Common normalization

Write the centered, monic characteristic-zero polynomial as

\[
f=X^{20}+\sum_{j=2}^{19}\binom{20}{j}a_jX^{20-j},
\qquad a_0=1,quad a_1=a_{20}=0.
\]

After scaling a nonzero root of minimum valuation to one, all roots and
all selected derivative witnesses are integral. For each \(1\le j<20\),
the monic normalized derivative

\[
G_j=H_{20-j}f/\binom{20}{j}
=\sum_{i=0}^j\binom ji a_iX^{j-i}
\]

vanishes at its selected integral witness. Induction on \(j\) proves
that every \(a_j\) is integral, including coefficients whose ordinary
binomial factors vanish modulo the prime. Thus these divided derivatives
can be reduced and are stronger than the bare reduced Hasse equations.

For existence arguments one may first pass from a complex counterexample
to an algebraic point of its polynomial incidence equations, with a
nonzero coefficient enforced by an inverse variable. This does not
require a separate claim that every counterexample has algebraic
coefficients or that its parameter scheme is finite.

## Two-adic completeness over the algebraic closure

The retained root at one and Lucas visibility imply

\[
\bar f=X^{20}+aX^{16}+bX^4,\qquad a+b=1.
\]

If \(r\) witnesses \(H_4\bar f=X^{16}+b\), substitution in
\(\bar f(r)=0\) gives \(ab=0\). Thus the two shapes are exactly
\(X^{20}+X^{16}=X^{16}(X+1)^4\) and
\(X^{20}+X^4=X^4(X+1)^{16}\), over every algebraically closed
characteristic-two field. Every witness therefore reduces to zero or
one. This fact is established before any finite enumeration.

Let \(r_j\in\{0,1\}\) be the reduced witness of \(G_j\).
Then

\[
\bar a_j=0\ (r_j=0),\qquad
\bar a_j=\sum_{i<j}\binom ji\bar a_i\ (r_j=1).
\]

Starting from \(a_0=1,a_1=0\), this proves inductively that **all**
normalized coefficient residues lie in the prime field. There are no
missing extension-field coefficient points. It also proves the producer's
triangular recurrence.

For the \(16+4\) seed the forced witness residues are
\(r_4=1,r_{16}=0\); for the other seed they are reversed. The remaining
16 labels are free as residue labels. Consequently the producer scans
exactly \(2^{16}\) marked residue assignments per branch. The counts
are 873 and 1128 distinct normalized coefficient vectors, respectively.

An independently written coefficient-first scan in
`check_local_classifications.py` evaluates every \(G_j\) at zero and
one and multiplies the number of allowed choices. It reproduces **every
coefficient vector and its assignment multiplicity**, not just the two
totals. It also compares fresh producer output against both saved
receipts. Normal and optimized Python executions passed.

The resulting 2001 coefficient vectors are not 2001 characteristic-zero
polynomials. The 131072 marked residue assignments do not identify exact
roots within a cluster, their recycling pattern, their multiplicities,
or their ramified displacements. The census classifies geometric residue
points of these incidence conditions; it does not certify reducedness,
flatness, lifting, or an obstruction on the infinitesimal neighborhoods.

### Integral sharpening and approximate points

The elimination identity using \(f(1)=G_m(1)=0\), with \(m=4\) or
16 as appropriate, has an odd pivot on the other visible normalized
coefficient and even remaining coefficients. It correctly strengthens
that coefficient's positive valuation to membership in \(2\mathcal O\).
To apply it, choose the **unit witness of \(G_m\)** as the exact
normalizing root one. A retained arbitrary unit root alone does not imply
\(G_m(1)=0\). Such a witness exists because its residue is forced to
one, and this additional unit scaling preserves the earlier normalization
and residue shape. This requirement should accompany the identity.

The reported examples modulo 16 and modulo 4 satisfy the displayed
normalized incidence congruences. Their nonzero exact defects at one
correctly show that they are approximate points only. Existence at a
fixed precision does not imply a characteristic-zero lift, and absence
of unramified lifts would not exclude ramified lifts.

## Five-adic completeness over the algebraic closure

Lucas visibility gives \(\bar f=q^5\), where
\(q=X^4+AX^3+BX^2+CX\), after taking coefficient fifth roots in the
algebraically closed residue field. The identity
\(H_{5i}(q^5)=(H_iq)^5\) shows that \(q\) is Hasse-CA. It has
distinct roots zero and the retained unit root, so it is not a fourth
power of one linear polynomial.

Since \(H_3q=4X+A=-X+A\), its mean root is \(A\), which is a
root of \(q\). Translating that root to zero gives
\(Q=X^4+UX^2+VX\). If \(U=0,V\ne0\), a common root with
\(H_1Q=4X^3+V\) cannot be zero; \(Q(r)=0\) gives
\(r^3=-V\), making \(H_1Q(r)=2V\ne0\), a contradiction.
The case \(U=V=0\) contradicts the two distinct roots.

For \(U\ne0\), a common \(H_2Q=X^2+U\) root is nonzero and
may be scaled to one. This gives \(U=-1\), and \(Q(1)=0\) then
forces \(V=0\). Hence the quartic is a translate and scale of
\(X^2(X-1)(X+1)\). No prime-field-containment assumption entered
this derivation. The two cases, according as the original root zero is
the double center or a simple side root, are precisely

\[
q=X^4-X^2,
\qquad q=X(X-1)^2(X-2)=X^4+X^3+3X.
\]

Their fifth powers have the reported cluster multiplicities
\((10,5,5)\) and \((5,10,5)\). The producer arithmetic confirms
both factorizations, all 19 Hasse common-root conditions, and the
derivative formulas. This was replayed during the independent scan and
passed with ordinary and optimized Python. The translation of the
quartic is only a classification device, as the producer explicitly
states; it is not silently applied to the original centered polynomial.

The actual unresolved problem in both primes is a lift obstruction
covering every invisible normalized coefficient and every witness
displacement, including fractional positive valuations.
