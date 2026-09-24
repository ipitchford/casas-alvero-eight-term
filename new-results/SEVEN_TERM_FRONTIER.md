# Six global exclusions in the seven-term support frontier

24 September 2026. This note independently verifies a bounded new use of
the existing ramification-safe row-8 divided identity. The computation
contains 1,216 residue assignments in total. It is not the unrestricted
row-8 census.

## Statement

**Proposition.** The characteristic-17 row-8 branch cannot occur for any
of the seven exact centered deficiency supports in the table below.

| Exact deficiency support | Active middle indices \(J\) | Assignments \(4^{|J|}\) | After divided identity | Possible seed rows before this test |
|---|---|---:|---:|---|
| \(\{2,3,4,10,12,19\}\) | \(4,10,12\) | 64 | 0 | 5,8 |
| \(\{3,4,9,10,12,19\}\) | \(4,9,10,12\) | 256 | 0 | 8 |
| \(\{3,4,5,10,13,19\}\) | \(4,5,10,13\) | 256 | 0 | 8 |
| \(\{3,4,10,12,15,19\}\) | \(4,10,12,15\) | 256 | 0 | 8 |
| \(\{3,7,9,10,16,19\}\) | \(7,9,10,16\) | 256 | 0 | 8 |
| \(\{3,6,10,16,17,19\}\) | \(6,10,16\) | 64 | 0 | 1,8 |
| \(\{3,4,10,13,18,19\}\) | \(4,10,13\) | 64 | 0 | 8,9 |

No unit-root collision filter is used: every row is already empty after
the divided identity alone.

**Global corollary.** The following five exact centered seven-term
supports cannot occur for a characteristic-zero degree-20 CA polynomial:
\[
\begin{gathered}
\{3,4,9,10,12,19\},\qquad
\{3,4,5,10,13,19\},\\
\{3,4,10,12,15,19\},\qquad
\{3,7,9,10,16,19\},\\
\{3,4,10,13,18,19\}.
\end{gathered}
\]
The first four have no other possible seed. For the fifth, the previously
proved complete row-9 exclusion with \(J=\{4,10,13\}\) removes the
other possible seed. The first and sixth rows of the table remain
unresolved globally by this argument: rows 5 and 1, respectively,
are still possible.

## 1. Normalization and the inherited necessary identity

Use the centered monic notation
\[
f=\sum_{j=0}^{20} C_ja_jX^{20-j},\qquad
C_j=\binom{20}{j},\quad a_0=1,\quad a_1=a_{20}=0.
\]
Integral root normalization at 17 and the normalized derivative
recurrence make all roots and all \(a_j\) integral. Scaling, including
the later unit-witness normalization, preserves exact support.
Algebraic specialization retains an exact support by adjoining the
inverse of the product of its active coefficients. These details are
given explicitly in
[GLOBAL_SUPPORT_COROLLARY.md](GLOBAL_SUPPORT_COROLLARY.md).

In row 8,
\[
\bar f=X^{17}(X^3-1).
\]
The common witness for \(G_3\) is a unit; scale it exactly to one.
Then \(f(1)=G_3(1)=0\), so
\[
a_3=-1-3a_2.
\tag{1}
\]
The seed is unchanged by this additional scaling because the residue
of the scaling witness is a cube root of unity.

The existing proof
[ROW8_BOUND_AND_DIVIDED_IDENTITY.md](../evidence/full/wild17/ROW8_BOUND_AND_DIVIDED_IDENTITY.md)
gives
\[
\sum_{j=4}^{16}(C_j/17)\bar a_j=-1.
\tag{2}
\]
For completeness, its valuation bridge has no unramified-field
assumption. Let \(\delta>0\) be the least valuation of a nonzero
root in the seventeen-root zero cluster, normalized by \(\nu(17)=1\).
The cluster has such a root because the exact mean is simple;
for the seven supports here this also follows immediately from
the nonzero linear coefficient \(a_{19}\).
The witnesses for \(G_2,G_{17},G_{18},G_{19}\) reduce to zero.
Their exact equations imply
\[
\begin{aligned}
\nu(a_2)&\ge2\delta,\\
\nu(a_{17})&\ge\min(17\delta,1+\delta),\\
\nu(a_{18})&\ge\min(18\delta,1+2\delta),\\
\nu(a_{19})&\ge\min(19\delta,1+3\delta).
\end{aligned}
\]
At a root attaining \(\delta\), the \(X^{17}\) term has value
\(17\delta\); every other term has value at least
\(\min(20\delta,1+4\delta)\). Unique minimal valuation would prevent
cancellation if \(\delta<1/13\). Thus \(\delta\ge1/13\), and
\[
\nu(a_{17})\ge1+\delta,\quad
\nu(a_{18})\ge1+2\delta,\quad
\nu(a_{19})\ge1+3\delta.
\]
Substitution of (1) into \(f(1)=0\) gives the exact equation
\[
0=-17\cdot67-17\cdot190a_2
+\sum_{j=4}^{16}C_ja_j
+1140a_{17}+190a_{18}+20a_{19}.
\]
Divide by 17 and reduce. The displayed strict bounds remove the last
three terms, and \(\nu(a_2)>0\) removes the second. Since
\(67=-1\) modulo 17, equation (2) follows. Fractional valuations are
allowed throughout.

## 2. Canonical witnesses at inactive coefficients

Let \(S\) be an exact support from the table and
\(J=S\cap\{4,\ldots,16\}\). If \(j\notin J\), then \(a_j=0\)
exactly. Because \(G_j(0)=a_j\) and \(f(0)=0\), zero is an exact
common witness for this derivative. Choose it. These choices can be
made independently: the CA condition requires the existence of a
witness for each order and imposes no requirement that these
particular choices differ.

For an active coefficient \(j\in J\), every possible witness residue
must be retained:
\[
\rho_j\in\{0,1,\zeta,\zeta^2\},\qquad
\zeta^2+\zeta+1=0\text{ in }\mathbb F_{17^2}.
\]
In particular, an active coefficient or a nonzero exact witness may
have zero residue. Neither is discarded.

The residue equations start with
\(\bar a_0=1,\bar a_1=\bar a_2=0,\bar a_3=-1\), and determine
successively
\[
\bar a_j=-\sum_{i=0}^{j-1}
\binom ji\bar a_i\rho_j^{\,j-i},
\qquad 4\le j\le16.
\tag{3}
\]
At every inactive index the chosen \(\rho_j=0\) makes this coefficient
zero. Hence each of the \(4^{|J|}\) active label assignments determines
one complete residue coefficient vector. Every actual counterexample
with that support gives at least one of these assignments.

The finite field restriction is a conclusion of (3), not an assumption
about the ambient residue field or about the ramification of a lift.
The visible seed has no roots outside this four-element domain in
the algebraic closure. An empty necessary-condition census therefore
excludes row 8 for the exact support.

## 3. Independent finite check

[check_row8_seven_term.py](check_row8_seven_term.py) imports no producer
or existing checker. It represents the field as
\(\mathbb F_{17}[s]/(s^2-14)\), verifies that 14 is a nonsquare, and
uses the complete domain
\[
0,\quad1,\quad8+9s,\quad8+8s.
\]
The three nonzero entries are distinct cube roots of unity. This
presentation differs from the earlier producer's \(1,\zeta\) basis.

The checker traverses the Cartesian product independently for each
support, implements the full recurrence (3), evaluates (2), and
records a histogram of all attained sums. It verifies the expected
assignment count and finds no sum equal to \(-1\) in any of the seven
cases. Normal and optimized Python runs produce identical receipts:

- [normal receipt](row8-seven-term-normal.json);
- [optimized receipt](row8-seven-term-optimized.json).

The checker also binds the support list to the existing support
inventory, verifies that these are exactly its seven size-six
deficiency sets containing 3, and checks the seed routing in the
table. It does not rerun the much larger predecessor inventory.
The witness-canonicalization argument received a separate bounded
algebraic review.

## 4. From branch exclusions to global statements

The complete nine-seed classification applies after normalization
because a unit root is retained, excluding monomial reduction.
Exact coefficient zeros remain zero under reduction and scaling.
Here is the complete table, in ordinary visible coefficients
\(h=X^{20}+aX^{18}+bX^{17}+cX^3+dX^2+eX\):

| Row | \(a\) | \(b\) | \(c\) | \(d\) | \(e\) |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 16 | 0 | 0 |
| 2 | 14 | 0 | 16 | 0 | 3 |
| 3 | 14 | 8 | 16 | 12 | 0 |
| 4 | 14 | 0 | 0 | 11 | 8 |
| 5 | 14 | 2 | 0 | 0 | 0 |
| 6 | 14 | 2 | 0 | 11 | 6 |
| 7 | 14 | 2 | 0 | 14 | 3 |
| 8 | 0 | 16 | 0 | 0 | 0 |
| 9 | 0 | 16 | 0 | 14 | 3 |

The table is an input from the independently checked
[algebraic-closure classification](../evidence/full/support_frontier/prime17/CLASSIFICATION.md)
and its [audit](../evidence/full/literature/PRIME17_CLASSIFICATION_AUDIT.md).
The new checker verifies routing against this table; it does not
reprove the classification merely by checking the nine examples.

For each of the seven supports, the table retains exactly the seed
rows whose nonzero visible coefficients do not occur at an absent
index. This argument never infers an exact coefficient zero from
a zero residue.

Four supports omit \(2,17,18\) and contain \(3,19\). The visible
polynomial can then have only its \(X^{17}\) and \(X\) coefficients
nonzero below the leading term. Row 8 is the only compatible
nonmonomial seed. Their row-8 exclusions are therefore global.

For \(\{3,4,10,13,18,19\}\), only rows 8 and 9 are compatible.
The row-9 canonical middle support is \(J=\{4,10,13\}\), which is
already completely excluded in
[BATCH1_PROOF.md](../evidence/full/collective17/exclusions/BATCH1_PROOF.md).
That prior computation covers its entire algebraic residue domain
and arbitrary ramification. Combining it with the new row-8
exclusion proves the fifth global exclusion.

For \(\{2,3,4,10,12,19\}\), row 5 remains compatible. For
\(\{3,6,10,16,17,19\}\), row 1 remains compatible. The present
argument excludes neither remaining branch.

## 5. Exact coverage increment

The predecessor inventory contained fourteen possible exact
seven-term supports. The five global exclusions above and the
separate global row-4 corollary for \(\{2,4,10,12,18,19\}\) remove
six distinct entries. The remaining eight are
\[
\begin{gathered}
\{2,3,4,10,12,19\},\quad
\{3,6,10,16,17,19\},\\
\{7,8,10,16,17,19\},\quad
\{10,12,13,16,17,19\},\\
\{6,10,15,16,17,19\},\quad
\{9,10,15,16,17,19\},\\
\{2,4,10,17,18,19\},\quad
\{4,10,16,17,18,19\}.
\end{gathered}
\]
Explicitly, the six excluded exact supports are
\[
\begin{gathered}
\{2,4,10,12,18,19\},\quad
\{3,4,9,10,12,19\},\\
\{3,4,5,10,13,19\},\quad
\{3,4,10,12,15,19\},\\
\{3,7,9,10,16,19\},\quad
\{3,4,10,13,18,19\}.
\end{gathered}
\]
The eight remaining sets are necessary possibilities, not asserted
realizable supports.
The coverage statement depends on the predecessor inventory and its
underlying imported restrictions. It does not raise the seven-term
lower bound to eight terms, exclude the whole row-8 branch, or solve
degree 20. No priority or assessment-grade claim is made.
