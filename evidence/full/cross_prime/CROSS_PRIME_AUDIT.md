# Bounded independent audit of the cross-prime restrictions

23 September 2026. **PASS for §§1–4**, with the total-scaling convention
below. This review does not recount the finite residue patterns in §5
and does not claim any complete characteristic-17 branch is excluded.

## Scaling and exact inputs

The transported identities follow from \(b_j=a_j/r^j\) and
\(t=1/r\). The initial minimum-valuation root can have nonzero
valuation, so \(\nu(t)\ge0\), not necessarily zero. After the
additional active-witness **unit** scaling, use \(r\) for the total
scaling factor. With that convention \(t=1/r\) and
\(a_j=r^jb_j\) remain exact. Without this relabeling, the later
formula for an original root would omit a unit, although its valuation
would be unchanged. The producer has now explicitly made the substitutions
\(r\mapsto rs\), \(b_j\mapsto b_j/s^j\), \(t\mapsto t/s\)
and absorbed the unit \(s\) into \(r\); I checked this wording. The
notation issue is resolved.

The exact simple distinguished roots in rows 4,6,7 and the exact triple
root in row 9 are justified by the previously audited characteristic-17
arguments. Their multiplicities are invariant under the new scaling.
The mean root zero is exactly simple. No residue equality is being
used as a substitute for those exact facts.

The type-B congruence modulo \(2\mathcal O\) is stronger than a
maximal-ideal reduction, and is justified by the active-witness
normalization and the exact odd-pivot coefficient elimination in the
two-adic note. I checked this dependency. I also independently recalculated
the root-bound minima: the ratios of the ordinary coefficient lower
bounds to \(k-e\) have minimum \(1/14\) for \(k=16\), and
\(1/2\) for \(k=4\), in both cases at exponent \(e=2\).
Translation by the exact unit root preserves binomial-normalized
integrality and switches the two ordinary congruences, so the quoted
opposite-cluster bounds follow as well. These arguments allow ramification.

## Row 9, type B, nonunit distinguished root

The type-B zero cluster has total multiplicity four. If the distinguished
triple root \(t\) is nonunit, that cluster consists exactly of simple
zero and triple \(t\). The factorization \(F=X(X-t)^3V\) is therefore
valid with \(V\) integral monic and \(V_0\) a unit. Its cubic
coefficient is

\[
-3tV_0+3t^2V_1-t^3V_2.
\]

It vanishes because the exact coefficient \(b_{17}\) is zero.
Dividing by nonzero \(t\) leaves the unit \(-3V_0\) and two terms
of positive valuation, a contradiction. This genuinely excludes the
whole stated scale/type subcase. The generalization with multiplicity
\(m\) and residue characteristic not dividing \(m\) is the same
coefficient argument and is valid under its stated isolation hypothesis.

## Rows 4,6,7 with a repeated root in the zero cluster

With \(\lambda=\nu(t)>0\), any first-derivative witness \(u\)
in that cluster is distinct from the two simple roots zero and \(t\).
Multiplicity capacity gives exactly
\(F=X(X-t)(X-u)^2V\). Put \(\mu=\nu(u)\ge1/2\).
The displayed coefficient expansion and identity (2) are exact.

Initially \(V_0\) is a unit and \(\nu(V_1)>0\). The denominator
\(V_0-2uV_1+u^2V_2\) is a unit. Thus

\[
\lambda\ge\mu+\min(1,\mu+\nu(V_1))>1.
\]

The strict last inequality holds even when \(\mu=1/2\); it uses
\(\nu(V_1)>0\). It also holds when \(V_1=0\). This makes every
nonleading coefficient of the quartic factor divisible by 2: their
lower bounds are respectively greater than 1, at least 1, and greater
than 2. Therefore \(U\equiv X^4\pmod{2\mathcal O[X]}\).
Combining with the type-B congruence and shifting coefficients by four
places gives \(V\equiv X^{16}-1\pmod{2\mathcal O[X]}\).
This cancellation is valid even if \(\mathcal O/2\mathcal O\)
has zero divisors. In particular \(\nu(V_1)\ge1\).

The two terms inside \(-2V_0+uV_1\) now have valuations 1 and at
least \(\mu+1>1\), so the exact relation is
\(\lambda=\mu+1\). The reduction of the degree-18 normalized
derivative is \(X^{18}+X^2+\bar b_{18}\): Lucas leaves indices
0,2,16,18, the \(b_2\) term vanishes, and \(\bar b_{16}=1\).
Evaluation at either possible root residue forces \(\bar b_{18}=0\).

In the quadratic coefficient formula, \(u^2V_0\) has valuation
\(2\mu\), strictly below the other terms. Since \(\nu(190)=1\),
one obtains \(\nu(b_{18})=2\mu-1>0\), proving
\(\mu>1/2\) and \(\lambda>3/2\). The linear coefficient uses
\(\nu(20)=2\), giving \(\nu(b_{19})=3\mu-1\). The remaining
displayed valuations of \(b_2,b_3\) follow directly from their exact
weighted identities. Every minimum used here is strict where equality
of a valuation is asserted.

The Hasse-order-two witness cannot also occupy this zero cluster:
orders 1 and 3 already have witnesses there, so the audited size-four
collapse lemma in characteristic two would collapse the cluster to
the simple mean. This is impossible. The conditional unit-cluster
conclusion and its consequence when \(0<\lambda\le3/2\) are valid.

The degree-four normalized witness is one of \(0,t,u\). Substitution
in \(G_4=X^4-6t^2X^2+4b_3X+b_4\) gives exactly the three
listed possibilities. At \(u\), the leading term has valuation
\(4\mu\); the other terms have valuations \(4\mu+3\) and,
where present, \(4\mu+6\), so no cancellation was overlooked.

Finally, transporting back with the total factor \(r\) gives
\(\nu(ru)=\mu-\lambda=-1\), the possibilities
\(\nu(a_4)\in\{\infty,0,-4\}\), and

\[
\nu(a_{18})=-16\lambda-3,\qquad
\nu(a_{19})=-16\lambda-4.
\]

The claimed ratio valuation \(-1\) and exact middle values
\(a_4=5\) or \(-3\) are correct. These remain conditional
necessary restrictions; they neither construct a lift nor eliminate
the other scale/type cases.
