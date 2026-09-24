# Completed sparsity research — 24 September 2026

All fourteen exact seven-term supports and nineteen compatible characteristic-seventeen seed cases have now been excluded. Together with the complete lower-term proof, this establishes the claimed bound of at least eight centered nonzero monomials for a nontrivial degree-twenty characteristic-zero Casas–Alvero polynomial.

The argument and internal review are indexed in `coverage/EIGHT_TERM_AUDIT.md`. The final paper is assembled separately as `outputs/casas-alvero-eight-term-review/PAPER.md`; its ZIP is a review submission, not an external publication or independent referee acceptance.

The full degree-twenty conjecture and the general conjecture remain unresolved by this work. A strong three-star assessment is not established. See `review/EIGHT_TERM_ASSESSMENT.md` in the bundle for the current significance assessment.

The dated working notes below are preserved as research history. Their remaining-case counts and pending-audit statements are superseded by the final assembly audit and the separately named argument audits. In particular, `last-four/quadratic/B/probe_jets.py` and its output contain an earlier incomplete second-jet diagnostic; the final proof and `check_B.py` retain the missing degree-nineteen term. The probe is not proof evidence.

---

## Historical checkpoint (superseded)

# Research status — 24 September 2026

The user has instructed that research must finish before another paper is produced. The frozen paper and evidence ZIP have not been updated. This directory records research, exact checks, and internal audits only.

## Confirmed progress beyond the frozen paper

The eight exact seven-term deficiency supports remaining in the frozen paper have been reduced to four. A support lists the six non-leading nonzero normalized coefficients of a centered monic degree-twenty polynomial.

New global exclusions:

- {7,8,10,16,17,19}: uniform row-1 unit-16 obstruction; ROW1_UNIT16.md and ROW1_AUDIT.md.
- {6,10,15,16,17,19}: same uniform theorem and separate exhaustive sixteen-marking census.
- {2,3,4,10,12,19}: complete row-5 case cover in ROW5_COMPLETION.md, independently checked in ROW5_COMPLETION_AUDIT.md, plus the previously established row-8 exclusion.
- {3,6,10,16,17,19}: ramification mismatch in ROW1_RAMIFICATION.md, checked in ROW1_RAMIFICATION_AUDIT.md, plus the previous row-8 exclusion.

These global corollaries inherit the existing complete characteristic-seventeen seed classification. Their new exact-arithmetic certificates and ramification-safe arguments have passed internal audits. Internal audit is not external refereeing or formal proof-assistant certification.

## Remaining exact supports

1. {10,12,13,16,17,19}.
2. {9,10,15,16,17,19}.
3. {2,4,10,17,18,19}.
4. {4,10,16,17,18,19}.

For supports 1 and 2 the first row-1 divided census leaves two markings each. The unit-16 marking is already excluded. The other middle coefficient residues are respectively (a10,a12,a13,a16)=(16,14,1,0) and (a9,a10,a15,a16)=(16,9,9,0) in F17. This finite filtering does not exclude those strata.

No eight-term lower bound, full degree-twenty result, full Casas–Alvero proof, or strong three-star significance assessment is established. No new final paper, ZIP, or publication action is authorized by completion of an isolated support.


## Uniform ramification theorem

The final argument audit also passes a stronger, support-independent local statement: in the row-1 normalized residue seed X20-X3, no candidate exists with a2=a18=0 exactly, a3 nonzero of positive valuation, all a4,...,a15 of residue zero, and a16 of residue -1. There may be arbitrarily many nonzero intermediate coefficients within those indices. The polynomial degree remains twenty. The proof forces nu(a3)=3/2, then approximates a3 beyond that precision by an element of a local field whose value group is (1/15)Z, an impossibility.

This theorem includes a4 nonzero. It does not settle the separate a3=0,a4 nonzero boundary. The earlier uniform theorem handles a3=a4=0. Both restrictions and the quantitative error bounds are checked in the research audits.

The producer notes were frozen before their audits, so their provisional headings are historical. ROW5_COMPLETION_AUDIT.md and ROW1_RAMIFICATION_AUDIT.md record the final passing status and exact reviewed fingerprints. The final row1 elimination checker, including its exhaustive eight-choice census, passes normal and optimized replay; root replays match the saved receipts. The argument audit and computational replay remain separate evidence obligations.
