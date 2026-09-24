# Characteristic-17 full-model classification

The complete visible model for centered degree 20,

    X^20+aX^18+bX^17+cX^3+dX^2+eX,

has exactly the nine normalized nonmonomial representatives listed in
`CLASSIFICATION.md`, over the whole algebraic closure of F_17. All nine
have coefficients in F_17. The proof includes every zero-coefficient chart;
it is not a prime-field point search.

The classification has passed an independent proof/checker audit in
`../../literature/PRIME17_CLASSIFICATION_AUDIT.md`. Normal and Python `-O`
replays both pass. Each checks nine polynomial membership identities, twelve
resultants, and all nineteen derivative gcd conditions for every listed
seed. The resultant verification uses 12,895 deterministic grid evaluations
in F_(17^2), with rigorous bidegree bounds. There are 36,689 monomials across
the four coefficient-array certificates. Replay takes approximately one
second and requires only Python's standard library.

## Complete retained seed list

The coefficient tuples (a,b,c,d,e), in F_17, are:

1. (0,0,16,0,0)
2. (14,0,16,0,3)
3. (14,8,16,12,0)
4. (14,0,0,11,8)
5. (14,2,0,0,0)
6. (14,2,0,11,6)
7. (14,2,0,14,3)
8. (0,16,0,0,0)
9. (0,16,0,14,3)

Rows 1--3 normalize the H_3 common root to 1; rows 4--7 normalize the
H_18 common root to 1; rows 8--9 normalize an H_17 common root to 1.
The monomial X^20 is retained separately and is excluded from an application
only after a justified unit-root normalization.

The complete marked gcd polynomials are in `verification-normal.json`.
Some have roots outside F_17: row 2 has the roots of X^2-3 among the
H_17 witnesses, and row 4 has the roots of X^2+3X+3 among the H_1
witnesses. These algebraic-extension possibilities were retained throughout.

## Consequences available for a characteristic-zero lift

The classification itself is not a characteristic-zero exclusion. Given an
integral characteristic-zero model with this reduction, uniqueness of an
exact root in a simple residual root class does yield the following useful
constraints. Coefficient names below refer to the ordinary coefficients of
X^18, X^17, X^3, X^2, X, respectively; the unlisted coefficients of the
full degree-20 polynomial may still be nonzero and divisible by 17.

- Row 3: the H_3 and H_18 witnesses coincide exactly (residue 1), and the
  H_17 and H_2 witnesses coincide exactly (residue 12).
- Row 4: b=c=0 exactly, because H_17 and H_3 have their only common
  residual root with h at the simple root 0.
- Rows 6 and 7: c=0 exactly. H_17 and H_18 have the same exact witness,
  at residue 1; in row 7 the H_2 witness coincides with them as well.
- Row 9: a=c=0 exactly. Its H_1 and H_2 witnesses are both in the
  residual cluster at 1 of size three; they are not equated merely by
  reduction, since that cluster is multiple.

These statements use simple residual-root rigidity and make no unramified
assumption. Further cluster and lifting exclusions are being developed by
the parent task separately; they are not incorporated as claims of this
classification package.

## Reproducibility and scope

Run:

    python3 check_classification.py
    python3 -O check_classification.py

The checker does not invoke Singular, overwrite producer receipts, or rely
on Python assertions. It rejects malformed or incomplete coefficient arrays.
The four `certificate_*.sing` files and their logs are the exact certificate
producer/replay inputs. Initial chart and radical computations are retained
as diagnostics, but the replay trusts no Groebner or radical output.

The unrestricted degree-20 support inventory still has 2,482 supports after
the earlier established filters and sparse exclusions. This nine-seed
classification replaces a coefficient continuum by finitely many complete
residue models; proving that all their characteristic-zero lifts are
impossible remains open in this subtask. It supplies no all-degrees theorem
and makes no historical-priority or publication claim.
