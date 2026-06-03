#!/usr/bin/env python3
from pathlib import Path
FILES=[Path('data/resume-masters/master-ba-resume-v2.md'),Path('data/resume-masters/master-sre-resume-v2.md')]
REQ=['## Target Positioning','## Professional Summary','## Core Competencies','## Professional Experience','## Education','## Skills','## Languages']
def validate(p):
    t=p.read_text(encoding='utf-8'); e=[]
    for r in REQ:
        if r not in t: e.append(f'{p}: missing {r}')
    if 'Learning REST APIs' in t: e.append(f'{p}: contains Learning REST APIs')
    if '## Publications' in t: e.append(f'{p}: contains Publications')
    return e
def main():
    errs=[]
    for p in FILES:
        if not p.exists(): errs.append(f'missing file: {p}')
        else: errs.extend(validate(p))
    if errs:
        print('Narrative master validation FAILED')
        [print('- '+x) for x in errs]
        return 1
    print('Narrative master validation PASSED')
    return 0
if __name__=='__main__': raise SystemExit(main())
