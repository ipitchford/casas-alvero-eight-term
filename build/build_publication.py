#!/usr/bin/env python3
"""Rebuild the publication manuscript from its bundled section sources."""
from pathlib import Path
import re,subprocess
R=Path(__file__).resolve().parents[1]
order=['INTRODUCTION','FOUNDATIONS','DIRECT','MIXED','QUADRATIC','ROW2','ROW5','ASSEMBLY','CONCLUSION','APPENDIX_A','INHERITED','REFERENCES']
old=(R/'PAPER.md').read_text();front=old[:old.index('# Introduction')]
front=re.sub(r'(?m)^author:.*\n','',front).replace('subtitle: "Wild root clusters and exact lifting obstructions"','subtitle: "Wild root clusters and exact lifting obstructions — unrefereed preprint"\nauthor: "Anonymous"')
if 'author:' not in front: front=front.replace('lang: en-GB','author: "Anonymous"\nlang: en-GB')
sections=[]
for name in order:
 body=(R/'manuscript'/f'{name}.md').read_text()
 if name in ('MIXED','QUADRATIC','ROW5'):body=re.sub(r'^(#{2,}) ',lambda m:m.group(1)[1:]+' ',body,flags=re.M)
 if name=='ROW5':body=body.replace('the preceding residue argument','the residue argument in Appendix B')
 if name=='ROW2':body=re.sub(r'^## [1-5]\. ','## ',body,flags=re.M)
 if name=='APPENDIX_A':body=re.sub(r'^(#{2,}) (A\.[0-9.]+) (.*)$',r'\1 \2 \3 {.unnumbered}',body,flags=re.M)
 sections.append(body.replace('(../next-stage/','(research/next-stage/'))
(R/'PAPER.md').write_text(front+'\n\n'.join(sections).replace('∎',r'\(\blacksquare\)')+'\n')
subprocess.run(['pandoc',str(R/'PAPER.md'),'--from=markdown+tex_math_single_backslash','--standalone','--toc','--number-sections','-V','geometry:margin=25mm','-V','fontsize=10pt','-V','papersize=a4','-V','colorlinks=true','-V','linkcolor=blue','--include-in-header',str(R/'build/layout.tex'),'--lua-filter',str(R/'build/wrap_paths.lua'),'--to=latex','-o',str(R/'PAPER.tex')],check=True)
subprocess.run(['tectonic','--keep-logs','PAPER.tex'],cwd=R,check=True)
