# Prime-field-marked row 9 is covered by prior art

23 September 2026. **This is a corollary of an external theorem, not a new
exclusion or a locally replayed proof of that theorem.** No prime-field
residue enumeration or Hensel search was started.

César Massri's *The Casas-Alvero conjecture for three recycled roots in
degree 20*, arXiv:1806.09561v6 (25 August 2023), Theorem 7.10, printed
page 13, excludes the degree-20 Abel-Gontcharoff configurations

    G(x; 0,0,y2,...,y18,1), with each yi in {0,1,y}.

The stated proof reports a finite computation over the 3^17 markings;
that computation has not been independently replayed in this subtask.
The local argument below takes the theorem as an external dependency.
[Primary PDF, Theorem 7.10](https://arxiv.org/pdf/1806.09561v6#page=13).

## Corollary and precise scope

There is no genuine row-9 Casas-Alvero candidate admitting a choice of
all active middle derivative witnesses whose residues lie in F_17.
This concerns **witness residues**, not merely coefficient residues.
It does not exclude every marking of any entire support.

To prove the corollary, use the already audited row-9 normalization.
The only prime-field roots of its residue polynomial are 0, 1 and -2.
The mean-root residue cluster consists of the exact simple root zero.
The cluster at one consists of the exact triple root one. The residue
-2 is simple and therefore has a unique exact root, say r, above it.
These assertions use the genuine-candidate cluster-collapse results;
they are not inferred from residue equality alone.

An active middle coefficient is exactly nonzero, so its common witness
cannot be the exact zero root. Under the hypothesis, its witness must
therefore be either 1 or r. Every inactive middle derivative can use
zero. The remaining derivative orders already use zero or one in the
row-9 normalization. Hence all derivative common-root conditions can
be witnessed by the three exact roots {0,1,r}.

The change of variable F(x)=f(1-x) preserves monicity in degree 20 and
the CA property. The repeated root one becomes zero, the original mean
zero becomes one, and r becomes y=1-r. Thus F(0)=F'(0)=0 and its
nineteenth derivative vanishes at one. For each derivative order from
2 through 18 choose its transferred witness yi in {0,1,y}. The unique
monic polynomial satisfying these derivative interpolation conditions
is G(x;0,0,y2,...,y18,1). Massri's theorem excludes precisely this
configuration, proving the corollary.

The argument also covers a marking which happens to use only one of
{1,r}; the allowed witness set need not be used exhaustively. It places
no nonvanishing requirement on the residues of active coefficients.

## Consistency calculation and what remains

The 240 canonical support histogram gives

    sum over active sizes m of count(m)*2^m = 66,120.

`count-consistency.json` records this exact assignment-bound calculation
and the input fingerprint. This count is not a completed search, a
certificate for the cited theorem, or new mathematical evidence.

The corollary permits dropping the all-prime-field-witness part of each
remaining canonical system when the external theorem is accepted. It
does not remove those systems: markings containing a degree-five or
degree-ten residue root remain. In particular the earlier 28 complete
full-field system exclusions and their certificates remain separately
identified; their coverage file has not been changed here. There is no
novelty claim and no further computation running.
