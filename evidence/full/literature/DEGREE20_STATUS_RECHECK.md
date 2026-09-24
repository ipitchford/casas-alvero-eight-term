# Degree-20 status recheck: Gasull's degree-24 statement

Checked 23 September 2026. Bounded primary-source audit; no outreach.

**Finding:** the 2026 article supplies no new degree-20 theorem. Its status sentence is unsupported by its cited source after that source's explicit correction. It should not be used to stop the degree-20 investigation or to claim that degree 20 is settled.

## The citation chain

Armengol Gasull, *A Primer on Resultants and Their Applications*, published 28 May 2026, DOI [10.1007/s44425-026-00047-6](https://link.springer.com/article/10.1007/s44425-026-00047-6), §3.4, calls 24 the lowest open degree. The associated reference [19] is Draisma–de Jong (2011). Gasull's own Proposition 7 proves only degrees 4 and 5; the surrounding discussion references computations up to degree 7, not a new proof for degree 20.

Jan Draisma and Johan P. de Jong, *On the Casas–Alvero conjecture*, EMS Newsletter 80 (June 2011), 29–33, [original issue PDF](https://ems.press/content/serial-issue-files/13698), Theorem 7 on printed p. 32, claimed the result for degrees n=n' p^e with n' in {1,2,3,4}, p>n', excluding p=7 when n'=4. The paragraph immediately following it explicitly counted 20 as settled. That was the erroneous n'=4, p=5 specialization.

The same authors' [August 2011 erratum](https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf) adds p=5 to the exclusions and explicitly retracts the degree-20 consequence. The reason is that the quartic resultant pair

    -b^2(4a^3+27b^2),   a(25a^3+216b^2)

vanishes in characteristic 5 for b=0 and arbitrary a. Thus the required characteristic-5 quartic exclusion fails. This defeats that reduction argument for degree 20; it is not a characteristic-zero counterexample.

**Interpretation:** inheritance of the uncorrected 2011 status is a plausible explanation of Gasull's sentence, but authorial provenance is an inference. The decisive verified fact is that neither Gasull's proof nor the corrected cited theorem settles degree 20.

## Ghosh revision check

The current primary [arXiv record 2501.09272](https://arxiv.org/abs/2501.09272), read on the audit date, exposes v1 (16 January 2025) and v2 (21 March 2026, 01:41:44 UTC), with “Major revisions.” It still claims an all-degree characteristic-zero proof via Koszul homology. The record shows no v3, withdrawal notice, or journal reference. This is a metadata check, not a fresh proof audit; it supplies no replacement for the campaign's existing Proposition 3.3 audit.

## Search and assurance boundary

In addition to reading those four primary pages, the scoped queries were:

- `"10.1007/s44425-026-00047-6" correction Casas Alvero degree 20`
- `"2501.09272" erratum correction v3`

No replacement degree-20 proof or relevant newer Ghosh revision was located in this bounded check. This is not a universal assertion that no public comment, correction, or other proof exists. The current investigation remains justified by the checked source chain; its own unrestricted degree-20 and all-degree targets remain unproved.
