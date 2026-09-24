#!/usr/bin/env python3
"""Assemble the completed eight-term review paper in a new output directory."""
from pathlib import Path
import json, shutil, re, subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DEST=ROOT/'outputs/casas-alvero-eight-term-review'
OLD=ROOT/'outputs/casas-alvero-final-review'

def copy(src,dst):
 shutil.copytree(src,dst,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.DS_Store'))

def main():
 if not (DEST/'historical/seven-term-PAPER.pdf').exists():
  copy(OLD,DEST)
  (DEST/'historical').mkdir(exist_ok=True)
  for name in ('PAPER.pdf','PAPER.md','PAPER.tex','MANIFEST.json','README.md','REVIEW_GUIDE.md'):
   shutil.copy2(OLD/name,DEST/'historical'/('seven-term-'+name))
 copy(HERE/'next-stage',DEST/'research/next-stage')
 copy(HERE/'review',DEST/'review')
 copy(HERE/'final-manuscript',DEST/'manuscript')
 order=['INTRODUCTION','FOUNDATIONS','DIRECT','MIXED','QUADRATIC','ROW2','ROW5','ASSEMBLY','CONCLUSION','APPENDIX_A','INHERITED']
 sections=[]
 for name in order:
  body=(HERE/'final-manuscript'/f'{name}.md').read_text()
  if name in ('MIXED','QUADRATIC','ROW5'):
   body=re.sub(r'^(#{2,}) ',lambda m:m.group(1)[1:]+' ',body,flags=re.M)
  if name=='ROW5':body=body.replace('the preceding residue argument','the residue argument in Appendix B')
  if name=='ROW2':body=re.sub(r'^## [1-5]\. ','## ',body,flags=re.M)
  if name=='APPENDIX_A':
   body=re.sub(r'^(#{2,}) (A\.[0-9.]+) (.*)$',r'\1 \2 \3 {.unnumbered}',body,flags=re.M)
  sections.append(body.replace('(../next-stage/','(research/next-stage/'))
 oldpaper=(OLD/'PAPER.md').read_text()
 refs=oldpaper[oldpaper.index('# References'):]
 # Reference entries remain sourced from the already verified prior bibliography.
 sections.append(refs.replace('degree-20 seven-total-term theorem','degree-20 eight-term lower bound'))
 front='''---
title: "An eight-term bound for degree-twenty Casas–Alvero polynomials"
subtitle: "Wild root clusters and exact lifting obstructions"
date: "24 September 2026"
lang: en-GB
---

# Abstract {.unnumbered}

We prove that a nontrivial characteristic-zero Casas–Alvero polynomial of degree twenty has at least eight nonzero monomials after centering at the common root of its nineteenth derivative. Published arithmetic restrictions reduce the seven-term case to fourteen exact coefficient supports. A complete characteristic-seventeen seed classification and ramification-safe lifting arguments exclude every compatible branch. The new local arguments include a uniform second-jet obstruction, forced collisions in a seventeen-root cluster, a quadratic residue obstruction with controlled precision, and a separated-cluster reduction to the quartic Casas–Alvero theorem in characteristic seventeen. The proof retains coefficient degeneration and arbitrary ramified extensions. Exact certificates and independent arithmetic reconstructions accompany the finite calculations, while the earlier exclusion of six or fewer terms is included in full. This is a completed sparsity theorem; it does not prove the unrestricted degree-twenty case or the general conjecture.

**Keywords:** Casas–Alvero conjecture; sparse polynomials; Hasse derivatives; nonarchimedean root clusters; exact computation.

'''
 body='\n\n'.join(sections).replace('∎',r'\(\blacksquare\)')
 (DEST/'PAPER.md').write_text(front+body+'\n')
 (DEST/'build/layout.tex').write_text(r'''\usepackage{microtype}
\usepackage{xurl}
\usepackage{etoolbox}
\emergencystretch=3em
\setlength{\parskip}{0.35em}
\AtBeginEnvironment{longtable}{\small}
\AtBeginEnvironment{verbatim}{\small}
\AtBeginDocument{\hypersetup{pdfsubject={Eight-term sparsity theorem in degree twenty; manuscript for review}}}
''')
 shutil.copy2(__file__,DEST/'build/build_eight_term.py')
 subprocess.run(['pandoc',str(DEST/'PAPER.md'),'--from=markdown+tex_math_single_backslash','--standalone','--toc','--number-sections','--top-level-division=section','-V','geometry:margin=25mm','-V','fontsize=10pt','-V','papersize=a4','-V','colorlinks=true','-V','linkcolor=blue','--include-in-header',str(DEST/'build/layout.tex'),'--lua-filter',str(DEST/'build/wrap_paths.lua'),'--to=latex','-o',str(DEST/'PAPER.tex')],check=True)
 print(json.dumps({'output':str(DEST),'manuscriptWords':len(body.split())}))

if __name__=='__main__':main()
