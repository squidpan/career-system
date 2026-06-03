#!/usr/bin/env python3
from pathlib import Path
import re
FILES=[Path('data/resume-masters/master-ba-resume.md'),Path('data/resume-masters/master-sre-resume.md')]
def section(text,heading):
    marker=f'### {heading}'
    start=text.find(marker)
    if start==-1:return ''
    rest=text[start:]
    m=re.search(r'\n### ', rest[len(marker):])
    if not m:return rest
    return rest[:len(marker)+m.start()]
def bullets(s):return sum(1 for line in s.splitlines() if line.startswith('- '))
def validate(path):
    text=path.read_text(encoding='utf-8'); errors=[]
    if 'Learning REST APIs' in text: errors.append(f'{path}: contains Learning REST APIs')
    if '## Publications' in text: errors.append(f'{path}: contains Publications section')
    if 'resume_structure: narrative_v2_compressed' not in text: errors.append(f'{path}: missing resume_structure narrative_v2_compressed')
    core_start=text.find('## Core Competencies')
    core_end=text.find('## Professional Experience')
    if core_start!=-1 and core_end!=-1:
        core=text[core_start:core_end]
        if '- ' in core: errors.append(f'{path}: Core Competencies should be compact line, not bullets')
    if path.name.startswith('master-ba'):
        g=section(text,'Financial Services & Enterprise Financial Applications')
        if bullets(g)>8: errors.append(f'{path}: BA Gresham section has {bullets(g)} bullets; expected <= 8')
    else:
        g=section(text,'Financial Services Production Support & Application Modernization')
        if bullets(g)>9: errors.append(f'{path}: SRE Gresham section has {bullets(g)} bullets; expected <= 9')
    return errors
def main():
    errors=[]
    for p in FILES:
        if not p.exists(): errors.append(f'missing file: {p}')
        else: errors.extend(validate(p))
    if errors:
        print('Resume compression v2 validation FAILED')
        for e in errors: print(f'- {e}')
        return 1
    print('Resume compression v2 validation PASSED')
    return 0
if __name__=='__main__': raise SystemExit(main())
