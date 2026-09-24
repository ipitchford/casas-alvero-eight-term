#!/usr/bin/env python3
"""Build a separate, scoped review artifact without modifying frozen evidence."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEST = ROOT / 'outputs/casas-alvero-final-review'

def clean_copy(source, target):
    shutil.copytree(source, target, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))

def manifest():
    entries = {str(p.relative_to(DEST)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted(DEST.rglob('*')) if p.is_file() and p != DEST/'MANIFEST.json'}
    (DEST/'MANIFEST.json').write_text(json.dumps({'scope': 'File integrity only; not proof or novelty validation',
                                                'sha256': entries}, indent=2)+'\n')

def main():
    required = [HERE/'manuscript/SPARSE_THEOREM.md', HERE/'research/GLOBAL_SUPPORT_COROLLARY.md']
    for p in required:
        if not p.exists():
            raise FileNotFoundError(p)
    DEST.mkdir(parents=True, exist_ok=True)
    clean_copy(HERE/'portable', DEST)
    clean_copy(HERE/'research', DEST/'new-results')
    clean_copy(HERE/'review', DEST/'review')
    clean_copy(HERE/'manuscript', DEST/'manuscript-parts')
    external = ROOT/'work/external-review-verification-2026-09-24'
    clean_copy(external, DEST/'review/external-verification')
    (DEST/'build').mkdir(exist_ok=True)
    for name in ('layout.tex', 'wrap_paths.lua'):
        shutil.copy2(ROOT/'work/casas-alvero-review'/name, DEST/'build'/name)
    shutil.copy2(Path(__file__), DEST/'build/build_paper.py')
    intro = (HERE/'manuscript/INTRODUCTION.md').read_text()
    sparse = (HERE/'manuscript/SPARSE_THEOREM.md').read_text()
    sparse = sparse.replace('# Appendix S. ', '# ').replace('This appendix gives', 'This section gives')
    sections = [intro, sparse]
    for name in ('GLOBAL_SUPPORT_COROLLARY.md', 'SEVEN_TERM_FRONTIER.md'):
        path = HERE/'research'/name
        if path.exists():
            sections.append(path.read_text())
    structural = (HERE/'research/STRUCTURAL_ARGUMENT.md').read_text()
    # Keep the mathematical statement and proof; separate route diagnostics stay in the supplement.
    structural = structural[:structural.index('## 6. Verification and unresolved implication')]
    structural = structural.replace('# Marked splitting and the limits of the row-9 Frobenius relation',
                                    '# Marked splitting of a local resultant algebra')
    start = structural.index('## 1. Input and notation')
    structural = '# Marked splitting of a local resultant algebra\n\n' + structural[start:]
    structural = re.sub(r'^## [1-5]\. ', '## ', structural, flags=re.M)
    explicit = r"""
For clarity, the integer presentation is
\[
\begin{aligned}
f_u={}&X^{20}-1140X^{17}
+\sum_{j=4}^{16}C_ju_jX^{20-j}
\\ &+\left(18221-\sum_{j=4}^{16}(19-j)C_ju_j\right)X^2
+\left(-17082+\sum_{j=4}^{16}(18-j)C_ju_j\right)X,
\end{aligned}
\qquad C_j=\binom{20}{j}.
\]
Direct substitution gives \(f_u(1)=f'_u(1)=0\), which defines
\(g_u=f_u/(X-1)^2\). The fixed reduction of \(g_u\) is
\[
D=\frac{X^{20}-X^{17}-3X^2+3X}{(X-1)^2}\quad\text{in }\mathbf F_{17}[X].
\]
Its squarefreeness and factor degrees are checked in the exact presentation accompanying the paper.
"""
    structural = structural.replace('Set \\(R_j=', explicit+'\nSet \\(R_j=', 1)

    structural = structural.replace('../../casas-alvero-full/', 'evidence/full/')
    structural = structural.replace('[FINITE_FLAT_REDUCTION.md](evidence/full/collective17/elimination/FINITE_FLAT_REDUCTION.md)',
                                    '[the explicit local presentation](evidence/full/collective17/elimination/FINITE_FLAT_REDUCTION.md)')
    sections += [structural, (HERE/'manuscript/CONCLUSION.md').read_text()]
    refs = (ROOT/'work/casas-alvero-review/REFERENCES.md').read_text()
    selected = []
    for key in ('CLO','deFrutos','Massri','Marashdeh','Bothmer-et-al','Berger'):
        match = re.search(r'\*\*\['+re.escape(key)+r'\].*?(?=\n\n\*\*\[|\n\n##)', refs, re.S)
        if not match:
            raise ValueError('Missing reference '+key)
        text = match.group(0)
        if key == 'deFrutos':
            text = text[:text.index(' Indexed primary PDF')] + ' The full thesis text and Proposition 3.5.5 were retrieved and compared on 24 September 2026; see review/NOVELTY.md.'
            text = text.replace('https://uvadoc.uva.es/bitstream/10324/3602/1/tesis367-130927.pdf',
                                'https://uvadoc.uva.es/bitstream/handle/10324/3602/TESIS367-130927.pdf?isAllowed=y&sequence=1')
        selected.append(text)
    sections.append('# References\n\n'+'\n\n'.join(selected))
    metadata = '''---
title: "A seven-term bound and local lifting obstructions for degree-twenty Casas–Alvero polynomials"
subtitle: "Scientific manuscript for review"
date: "24 September 2026"
lang: en-GB
---

# Abstract

We prove that a nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least seven nonzero terms after centering at the common root of its nineteenth derivative. The proof reduces small supports to five families and excludes the last family through a complete characteristic-thirteen residue classification and explicit lift obstructions. The specialization and lifting arguments include coefficient degeneration and ramified extensions. We exclude six further exact seven-term supports, reducing the audited seven-term frontier from fourteen possibilities to eight. We also give a multiplicity-preserving factorization of a local resultant norm into marked obstruction values. The latter identifies, but does not resolve, the remaining nonvanishing problem. Exact finite certificates, independent arithmetic checks, and reproducible code accompany the proofs. Neither the unrestricted degree-twenty case nor the general Casas–Alvero conjecture is proved.

'''
    body = '\n\n'.join(sections).replace('∎', r'\(\blacksquare\)')
    body = body.replace('../../casas-alvero-full/', 'evidence/full/')
    for p in sorted((DEST/'new-results').iterdir()):
        body = body.replace(']('+p.name+')', ']('+str(p.relative_to(DEST))+')')
    for p in (DEST/'new-results').glob('*.md'):
        p.write_text(p.read_text().replace('../../casas-alvero-full/', '../evidence/full/'))
    body += '\n\n**[ProofAtlas]** [Casas–Alvero collaboration page](https://www.proofatlas.ai/collaboration/casas-alvero-conjecture/). Reported work, inspected 24 September 2026; exact-system equivalence unresolved.\n\n**[Shih]** Shih, Cheng-Pang, *On the Casas-Alvero Conjecture*, 2022 master’s thesis. [NTHU catalog record](https://etd.lib.nycu.edu.tw/cgi-bin/gs32/hugsweb.cgi?o=dnthucdr&s=id%3D%22G021090215100%22.&searchmode=basic). Metadata inspected; full text unavailable.\n'
    (DEST/'PAPER.md').write_text(metadata+body+'\n')
    subprocess.run(['pandoc',str(DEST/'PAPER.md'),'--from=markdown+tex_math_single_backslash',
                    '--standalone','--toc','--number-sections','--top-level-division=section',
                    '-V','geometry:margin=25mm','-V','fontsize=10pt','-V','colorlinks=true',
                    '-V','linkcolor=blue','--include-in-header',str(DEST/'build/layout.tex'),
                    '--lua-filter',str(DEST/'build/wrap_paths.lua'),
                    '--to=latex','-o',str(DEST/'PAPER.tex')],check=True,timeout=30)
    manifest()
    print(json.dumps({'output':str(DEST),'words':len(body.split())}))

if __name__ == '__main__':
    main()
