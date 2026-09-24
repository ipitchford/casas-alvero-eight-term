# Prior-art audit: sparse degree 20 and a moving degree family

23 September 2026. Bounded primary-source audit, with an independent arithmetic replay. This is not an external review or a certification of historical novelty. Previous research outputs were left untouched.

The thesis access gap is resolved: indexed full text of the primary PDF was retrieved. It establishes earlier priority for two ingredients that this project had initially rediscovered. Neither the degree-20 characteristic-13 seed nor the new moving-degree obstruction was located in the material inspected. The latter remains a plausible new result, with the qualified scope below.

## Primary-source findings

Rosa María de Frutos Marín, *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, Universidad de Valladolid doctoral thesis (2013), is available as a [primary PDF](https://uvadoc.uva.es/bitstream/10324/3602/1/tesis367-130927.pdf). The relevant source locations are:

| Location | Printed pages | Relevance |
|---|---:|---|
| Theorem 2.3.3, Eq. (2.11), Corollary 2.3.4 | 27–29 | Two-support discriminant; trinomials |
| Theorem 3.3.5, Corollary 3.3.6 | 49–50 | Reduction of visible support |
| Theorem 3.5.1, Propositions 3.5.3 and 3.5.5 | 55–57 | Singleton and two-support modular criteria |
| Corollary 3.6.9; Theorem 4.2.1 | 65–66; 72 | Conjectural transfer; proved prime-power condensation |
| Definition 5.6.1; Observation 5.6.9; Theorem 5.6.11 | 113; 117–118 | Fixed-degree discriminants and resultants |

The [2015 conference abstract](https://www.singacom.uva.es/JTN2015/contribuciones/ordinarias/frutos.pdf), *Un problema sobre números combinatorios*, also gives modular four-monomial criteria based on reducing to at most two visible coefficients. These statements cover coefficient degenerations.

Martin Kreidl's [2007 thesis](https://homepage.univie.ac.at/herwig.hauser/Publications/diplom_kreidl.pdf), *Methoden der kommutativen Algebra in Charakteristik Null und positiver Charakteristik*, Satz 4.25, p.33, constructs other sparse families with degree depending on the characteristic. It does not state the family studied here.

## Exact formula identification

The following is our algebraic comparison, implemented independently in `check_known_criteria.py`.

Use deficiency indices \(r<s\), so the monomials have exponents \(n-r,n-s\). Put

\[
B={n\choose r},\quad D={n\choose s},\quad C={n-r\choose s-r},\quad
g=\gcd(r,s),\quad u=(s-r)/g,\quad v=r/g.
\]

The integer previously produced by the project's boundary calculation is

\[
N=B^{u+v}(C-1)^u(D-C)^v-(B-1)^v(D-1)^{u+v}.
\]

In the thesis notation, substitute

\[
i=n-s,\quad j=n-r,\quad a=D,\quad b=B,\quad c={s\choose r}=BC/D,
\quad\rho=v,\quad\sigma=u.
\]

Then \(b-c=B(D-C)/D\) and \(b-ac=-B(C-1)\). These two identities give

\[
\Delta_{(2.11)}=(-1)^{uv+u}N,
\qquad \Delta_{(5.23)}=(-1)^uN.
\]

The sign difference between the two source expressions has no effect on nonvanishing. This is an exact identification, not merely a similarity of methods. The replay checks 3,654 integer instances for degrees 4 through 30. The symbolic substitutions above prove the identity in general. Attribution of this criterion only to the 2026 Marashdeh preprint would be incomplete.

For clarity in applying the source, its binomial-presented polynomials and net derivatives must not be identified indiscriminately with ordinary coefficients and Hasse derivatives in positive characteristic. In the characteristic-13 seed, the three active binomial coefficients are units, so rescaling the active equations is valid. Derivatives at inactive exponents have the common root zero.

## Independent implications for the project's support lists

Let \(S\) be the set of allowed deficiencies, and \(V_p=\{m\in S:p\nmid{20\choose m}\}\). The replay uses the source criteria as follows: empty \(V_p\) excludes the family; singleton \(\{m\}\) excludes it if \({20\choose m}\not\equiv1\); a pair \(\{r,s\}\) excludes it when both binomials differ from 1 and \(N\not\equiv0\pmod p\).

All relevant primes were checked. For supports of size at least three, primes greater than 20 cannot shrink the visible support to two, since they divide no degree-20 binomial coefficient. Thus the finite list is \(2,3,5,7,11,13,17,19\).

| Deficiency support | Outcome from these older criteria |
|---|---|
| \(\{4,10,17,19\}\) | Not excluded |
| \(\{4,8,9,10,11,12,17,19\}\) | Not excluded |
| \(\{2,4,5,10,19\}\) | Excluded at 17 |
| \(\{2,4,10,12,19\}\) | Excluded at 17 |
| \(\{2,4,10,16,19\}\) | Excluded at 17 |
| \(\{2,10,14,16,19\}\) | Excluded at 17 |
| \(\{3,4,10,18,19\}\) | Not excluded |
| \(\{3,10,16,17,19\}\) | Not excluded |
| \(\{4,5,10,17,19\}\) | Not excluded |
| \(\{8,10,16,17,19\}\) | Not excluded |

For the four exclusions, \(V_{17}=\{2,19\}\) and \(N\equiv2\pmod {17}\). The complete residue table is `known-criteria-results.json`.

These results change the attribution and the baseline for the next six-total-term search. They do not supply the missing characteristic-13 exclusion behind the frozen centered degree-20 lower bound of six total terms. The three active coefficients of \(X^{20}+aX^{16}+cX^3+dX\) remain visible at 13: their binomial residues are \(9,9,7\). No direct implication from the inspected old criteria was found for that full three-coefficient chart.

Late bounded addition: the parent reports a second characteristic-13 seed, \(X^{20}+aX^4+cX^3+dX\), intended to exclude the last listed support \(\{8,10,16,17,19\}\). Its independent proof audit is separate from this report. A short exact-family/support search found no matching source; all three active binomial coefficients again remain units at 13, so the older at-most-two-visible-support criterion does not itself exclude this full chart. This is a possible additional finite support calculation, not a new general theory or a claim that all six-term candidates are excluded.

## The moving degree family

The candidate is a uniform finite-characteristic obstruction for

\[
h=X^{p+7}+aX^{p+3}+cX^3+dX,\qquad p>7.
\]

Its potential new content is the construction of a fixed degree-72 polynomial \(H\) and the rational map

\[
\psi(z)=289/z^6,\qquad
T(z)=\frac{35(17-z^3)}{z^2(51-35z)},
\]

such that every appropriate nontrivial solution forces \(H(z)=0\) and \(z^p=\psi(z)\), followed by the certified coprimality of \(H\) with the cleared composition \(H\circ\psi\). Exact searches for these formula aliases and the prescribed moving support returned no matching primary-source result in this bounded search.

The distinction from a fixed-degree discriminant is substantive. An integer depending on \((n,I)\) can vary as \(n=p+7\) varies with the characteristic. Its existence alone does not give one fixed nonzero integer bounding all exceptional primes for this moving family. The thesis's proved condensation concerns degrees \(hp^r\); its transfer statements involving arbitrary shifts are conjectural equivalents, not a theorem giving the present obstruction.

The Frobenius step itself is elementary: if an integral \(H\) vanishes at \(z\), then \(H(z^p)=H(z)^p=0\). A rational Frobenius relation gives a second fixed polynomial equation, and a nonzero resultant confines the characteristic to its prime divisors, together with denominator/content exceptions. This general reasoning should not be advertised as a new elimination principle. The support-specific uniform construction and exact nonvanishing certificate are the research candidates.

The boundary charts with at most two active coefficients belong to the older criterion's scope. In particular, characteristic 17 singleton examples are old-criterion cases. Other agents' explicit boundary computations are useful independent specializations, not evidence that the general two-support mechanism is new.

The present 26,185-digit nonzero resultant gives a finite obstruction, not an exact classification of exceptional primes. Its factorization is incomplete; even a fully factored resultant can contain primes introduced by elimination. A nonconstant modular gcd is inconclusive. A paper should state the finite obstruction and the sufficient bounded-degree exclusion test separately from any claim classifying all actual solutions.

This family is also strictly narrower than all degree \(p+7\) polynomials. For every \(p>7\), \(X^{p+7}-X^7\) already has the positive-characteristic CA property: the only derivative with a nonzero constant term is Hasse order 7, whose value vanishes at 1, while all other orders share zero. Hence no uniform assertion excluding all degree \(p+7\) CA polynomials is possible. This example is our direct scope check.

## Assessment

Proceed with the structural candidate as a bounded research result, subject to the independent proof audits. Its moving-degree uniformity is stronger than a single characteristic-13 calculation and was not absorbed by the inspected older results. Its significance remains moderate: it excludes one prescribed sparse family and yields coefficient restrictions, without settling any new unrestricted characteristic-zero degree. The fixed arithmetic test is more useful to a reader than the enormous integer alone.

Do not present the singleton lemma, two-support integer, fixed-degree discriminant technique, or prime-power transfer as new. Do not claim an exhaustive novelty search. Full text of the de Frutos thesis was available to this audit, but only the relevant sections and targeted searches were reviewed; unrelated thesis chapters and all later literature were not exhaustively checked. See `QUERY-COVERAGE.md` and `SOURCE-ACCESS.md` for retrieval and search boundaries.
