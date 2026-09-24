# Completion of the seven-term support cover

We now assemble the local exclusions into the global theorem. The labels \(S_i\) refer to the complete fourteen-support table. The residue classification is always applied after integral normalization with a retained unit root; the monomial special fibre is therefore unavailable.

## The first divided condition in row 1

For \(S_6,S_7,S_9\), the exact coefficients \(a_2,a_4,a_{18}\) vanish. Normalize the common \(H_3\) root to one. The argument at the start of Theorem 2, before imposing the middle residue conditions, shows that the two nonzero small roots have valuation at least \(1/2\), that neither is repeated, and that \(\nu(a_3)\ge3/2\). Thus the common \(H_1\) witness lies in the unit cluster. All first sixteen Taylor coefficients at one are in \(17\mathcal O\), and a nonzero unit-root displacement has valuation at least \(1/16\). The derivative equation therefore forces \(f'(1)/17\) to have zero residue. Explicitly,
\[
-133+\sum_{j=4}^{16}
 \left(19-j-2\binom{20-j}{3}\right)
 \frac{\binom{20}{j}}{17}\bar a_j=0.
\]
The \(a_3\) contribution disappears because \(\nu(a_3)>1\).

For each active middle index, its witness reduces to zero or one. At an inactive index we may choose the exact root zero, since \(G_j(0)=a_j=0\). The triangular recurrence reconstructs every coefficient residue. The complete small censuses are

| Support | Active middle indices | Binary markings | Survivors of the divided equation |
|---|---|---:|---|
| \(S_6\) | \(6,10,16\) | 8 | only \(\bar a_{16}=-1\), earlier residues zero |
| \(S_7\) | \(7,8,10,16\) | 16 | the same |
| \(S_9\) | \(6,10,15,16\) | 16 | the same |

Theorem 2 excludes all these survivors. The analogous sixteen-marking censuses for \(S_8,S_{10}\), proved in the mixed-stratum section, leave the unit-16 pattern and exactly one mixed pattern each. Theorem 2 removes the first; the mixed-stratum theorem removes the second. Every active coefficient with zero residue is retained in these enumerations.

## Other residue branches

The row-8 divided condition and the complete small census in Appendix B exclude that row for \(S_1,S_2,S_3,S_4,S_5,S_6,S_{12}\). The respective marking counts are \(64,256,256,256,256,64,64\), totalling 1,216. Each census is already empty after the necessary divided condition.

The row-5 theorem excludes the other branch of \(S_1\). Appendix B excludes row 4 for \(S_{11}\) and row 9 for \(S_{12}\). The quadratic-coefficient theorem excludes \(S_{14}\) and the row-1 branch of \(S_{13}\). The row-2 theorem excludes its other possible nontrivial branch. Its apparent row-4 alternative is impossible by the exact-root restriction \(a_{17}=0\), conflicting with this exact support.

For reference, the complete closing table is:

| Support | Exclusion of every compatible branch |
|---|---|
| \(S_1\) | row 5 theorem; row 8 divided census |
| \(S_2,S_3,S_4,S_5\) | row 8 divided census |
| \(S_6\) | row 1 Theorem 2 and eight-marking sieve; row 8 census |
| \(S_7,S_9\) | row 1 Theorem 2 and sixteen-marking sieves |
| \(S_8,S_{10}\) | row 1 unit-16 and mixed-stratum exclusions |
| \(S_{11}\) | complete row-4 critical-value certificate |
| \(S_{12}\) | row 8 census; complete row-9 certificate for \(J=\{4,10,13\}\) |
| \(S_{13}\) | row 1 and row 2 theorems; row 4 exact-zero contradiction |
| \(S_{14}\) | row 1 quadratic-coefficient theorem |

**Theorem 1 (restated).** A nontrivial characteristic-zero polynomial of degree twenty sharing a root with each of its nonconstant proper derivatives has at least eight nonzero monomials after translating the zero of its nineteenth derivative to zero.

**Proof.** Appendix A excludes fewer than seven terms. The complete necessary-condition enumeration leaves precisely \(S_1,\ldots,S_{14}\) for seven terms. Integral normalization sends any such candidate to one of the compatible nonmonomial seeds listed in the table. Each corresponding branch is excluded above, including all coefficient-zero residue charts and arbitrary ramified lifts. Thus seven terms are impossible. Algebraic specialization transfers the exclusion back to every characteristic-zero candidate with that exact support. \(\square\)

The proof does not identify a realizable eight-term support. It gives a lower bound, not a sharpness statement. The unrestricted degree-twenty problem includes denser supports and is not settled by this theorem.
