#!/usr/bin/env python3
from __future__ import annotations

import json, re, sys
from pathlib import Path


def split_frontmatter(text: str):
    if not text.startswith('---'):
        return {}, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    fm = {}
    for line in parts[1].splitlines():
        if ':' in line and not line.lstrip().startswith('-'):
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, parts[2]


def read_doc(path: Path):
    text = path.read_text(encoding='utf-8')
    fm, body = split_frontmatter(text)
    return {'path': path, 'frontmatter': fm, 'body': body, 'text': text}


def slug_from_filename(path: Path) -> str:
    name = path.stem
    for prefix in ['jd-', 'role-', 'resume-', 'gap-', 'interview-prep-']:
        if name.startswith(prefix):
            name = name[len(prefix):]
    for suffix in ['-v1', '-teal-v1', '-assembled-v1']:
        if name.endswith(suffix):
            name = name[:-len(suffix)]
    return name


def find_by_slug(folder: Path, prefix: str, slug: str, ext: str = '.md') -> Path | None:
    direct = folder / f'{prefix}{slug}{ext}'
    if direct.exists():
        return direct
    slug_tokens = set(slug.split('-'))
    best, best_score = None, 0
    for p in folder.glob(f'*{ext}'):
        ptokens = set(slug_from_filename(p).split('-'))
        score = len(slug_tokens & ptokens)
        if score > best_score:
            best, best_score = p, score
    return best if best_score >= 2 else None


def md_list(items):
    return ''.join(f'- {x}\n' for x in items) if items else '- None identified\n'


def numbered(items):
    return ''.join(f'{i+1}. {x}\n' for i, x in enumerate(items)) if items else '1. None identified\n'


def read_gap_json(gap_md: Path) -> dict:
    js = gap_md.with_suffix('.json')
    if js.exists():
        return json.loads(js.read_text(encoding='utf-8'))
    doc = read_doc(gap_md)
    fm = doc['frontmatter']
    return {'company': fm.get('company',''), 'title': fm.get('title',''), 'role_code': fm.get('role_code',''), 'overall_match_score': int(fm.get('overall_match_score') or 0), 'recommendation': fm.get('recommendation',''), 'effort_level': fm.get('effort_level',''), 'matched': {}, 'missing': {}}


def question_set(role_code: str, gap: dict):
    role_code = (role_code or '').lower()
    missing = gap.get('missing', {})
    qs = []
    if any(x in role_code for x in ['support', 'ops', 'sre']):
        qs += [
            'Tell me about a production issue you helped investigate or resolve.',
            'How do you validate that an application is healthy after a deployment?',
            'How do you use runbooks during release or support activities?',
            'How do you coordinate with DevOps, infrastructure, database, QA, and business teams during an incident?',
            'How do you distinguish application issues from data, infrastructure, or environment issues?',
        ]
    if any(x in role_code for x in ['ba', 'bsa', 'analyst']):
        qs += [
            'How do you gather requirements from multiple stakeholders?',
            'How do you turn an Epic into user stories and acceptance criteria?',
            'How do you handle conflicting business requirements?',
            'How do you support UAT and ensure business signoff?',
            'Describe a time you documented a complex workflow or system process.',
        ]
    if 'sre' in role_code:
        qs += [
            'What Linux commands would you use first when troubleshooting performance or connectivity?',
            'How would you approach monitoring and alert triage?',
            'How do you think about resiliency, failover, and disaster recovery readiness?',
        ]
    for tool in missing.get('tools', []) or []:
        qs.append(f'What is your exposure to {tool}, and how would you ramp up quickly if this role requires it?')
        qs.append(f'How would you support a team using {tool} even if you are not the primary administrator?')
    for skill in missing.get('skills', []) or []:
        qs.append(f'This role emphasizes {skill}. What related experience can you map to that requirement?')
    for domain in missing.get('domains', []) or []:
        qs.append(f'What is your understanding of the {domain} domain, and how would you learn the business context?')
    if not qs:
        qs = ['Walk me through your most relevant experience for this role.', 'Why are you interested in this opportunity?', 'What would you want to learn in the first 30 days?', 'How do you build trust with business and technical teams?']
    out, seen = [], set()
    for q in qs:
        if q not in seen:
            seen.add(q); out.append(q)
    return out


def story_bank():
    return [
        ('FRBNY enterprise financial application modernization', 'application support, cloud modernization, REST API validation, release readiness', 'Use the AC Plus to OPS360/AWS modernization story. Emphasize requirements, validation, runbooks, release coordination, and cross-team execution.'),
        ('REST API validation against Oracle', 'data validation, API testing, production readiness', 'Explain how REST payloads were compared against Oracle/legacy sources to protect data quality during migration.'),
        ('Deployment runbooks and health checks', 'production support, release coordination, DevOps collaboration', 'Explain how runbooks, validation checklists, and post-release health checks reduced release risk.'),
        ('HP PPM insurance workflow analysis', 'business analysis, workflow, PMO, UAT', 'Explain requirements, workflow configuration/testing, representative UAT data, reporting, and stakeholder support.'),
        ('Financial data platform implementation', 'reference data, pricing data, data quality, financial systems', 'Explain ACPlus/Asset Control, golden copy, vendor feeds, normalization, and downstream data distribution.'),
    ]


def generate_one(gap_path: Path, jds_dir: Path, roles_dir: Path, resumes_dir: Path, output_dir: Path, run_id: str):
    gap = read_gap_json(gap_path)
    slug = slug_from_filename(gap_path)
    jd_path = find_by_slug(jds_dir, 'jd-', slug)
    role_path = find_by_slug(roles_dir, 'role-', slug)
    resume_path = find_by_slug(resumes_dir, 'resume-', slug)
    jd = read_doc(jd_path) if jd_path else {'frontmatter': {}}
    role = read_doc(role_path) if role_path else {'frontmatter': {}}
    company = gap.get('company') or jd['frontmatter'].get('company') or 'unknown-company'
    title = gap.get('title') or jd['frontmatter'].get('normalized_title') or slug
    role_code = gap.get('role_code') or jd['frontmatter'].get('role_code') or role['frontmatter'].get('role_code') or ''
    missing = gap.get('missing', {})
    matched = gap.get('matched', {})
    questions = question_set(role_code, gap)
    gap_strategy = []
    for x in missing.get('tools', []) or []:
        gap_strategy.append(f'If asked about {x}, be direct that you have not been the primary {x} administrator, then bridge to enterprise application support, requirements, UAT, workflow analysis, and fast ramp-up.')
    for x in missing.get('skills', []) or []:
        gap_strategy.append(f'For {x}, connect related experience from FRBNY, HP PPM, release coordination, or UAT.')
    for x in missing.get('domains', []) or []:
        gap_strategy.append(f'For {x}, show how you learn domain context through stakeholders, process documentation, data analysis, and UAT.')
    stories = ''.join(f"### {name}\n\n- Use for: {use_for}\n- Talking point: {prompt}\n\n" for name, use_for, prompt in story_bank())
    out_path = output_dir / f'interview-prep-{slug}.md'
    md = f'''---
type: interview_prep
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
gap_file: {gap_path}
jd_file: {jd_path or ''}
role_file: {role_path or ''}
resume_file: {resume_path or ''}
---

# Interview Prep — {company} — {title}

## Role Snapshot

- Company: **{company}**
- Role: **{title}**
- Role Code: **{role_code}**
- Gap Match Score: **{gap.get('overall_match_score','')}**
- Gap Recommendation: **{gap.get('recommendation','')}**
- Estimated Effort: **{gap.get('effort_level','')}**

## Positioning Statement

I am a Senior Business Analyst and Application Support professional with experience supporting enterprise financial applications, production readiness, release coordination, requirements, UAT, runbooks, REST API validation, Oracle data comparison, and cross-functional delivery across financial services and insurance environments.

## Strengths To Emphasize

### Matched Skills

{md_list(matched.get('skills', []) or [])}
### Matched Tools

{md_list(matched.get('tools', []) or [])}
### Matched Domains

{md_list(matched.get('domains', []) or [])}
## Gaps To Prepare For

### Missing Tools

{md_list(missing.get('tools', []) or [])}
### Missing Skills

{md_list(missing.get('skills', []) or [])}
### Missing Domains

{md_list(missing.get('domains', []) or [])}
## Likely Interview Questions

{numbered(questions)}
## Gap-Based Answer Strategy

{md_list(gap_strategy)}
## Story Bank

{stories}
## 30-Minute Study Guide

1. Re-read the JD and underline every tool, system, workflow, and stakeholder group.
2. Review the gap analysis and prepare a short answer for each missing tool or domain.
3. Practice the FRBNY modernization story in 90 seconds.
4. Practice the REST API validation against Oracle story in 60 seconds.
5. Practice the deployment runbook / health check story in 60 seconds.
6. Prepare one question for the hiring manager about first-90-day priorities.
7. Prepare one question about application support, production readiness, and team structure.

## Questions To Ask Them

1. What are the most important systems or workflows this role supports?
2. What are the most common production or business issues the team handles?
3. What would success look like in the first 90 days?
4. How does the team manage requirements, UAT, release readiness, and post-release support?
5. Which tools or platforms should I prioritize learning before joining?

## Notes

This v0.4.3 output is deterministic and based on JD, role, resume, and gap-analysis artifacts. It is intended as a first-pass interview prep note, not a final script.
'''
    out_path.write_text(md, encoding='utf-8')
    return out_path


def main(argv):
    if len(argv) < 3:
        print('Usage: generate_interview_prep.py <run_id> <gap_analysis_dir> [jds_dir] [roles_dir] [resumes_dir]', file=sys.stderr)
        return 2
    run_id = argv[1]
    gap_dir = Path(argv[2])
    jds_dir = Path(argv[3]) if len(argv) > 3 else Path('data/jds/normalized')
    roles_dir = Path(argv[4]) if len(argv) > 4 else Path('data/roles')
    resumes_dir = Path(argv[5]) if len(argv) > 5 else Path('data/resume-versions/teal-export')
    run_output = Path('ops/runs') / run_id / 'output'
    data_output = Path('data/interview-prep')
    run_output.mkdir(parents=True, exist_ok=True)
    data_output.mkdir(parents=True, exist_ok=True)
    generated = []
    for gap_path in sorted(gap_dir.glob('gap-*.md')):
        out = generate_one(gap_path, jds_dir, roles_dir, resumes_dir, run_output, run_id)
        generated.append(out.name)
        (data_output / out.name).write_text(out.read_text(encoding='utf-8'), encoding='utf-8')
        print(f'generated interview prep: {gap_path.name} -> {out.name}')
    report = {'run_id': run_id, 'count': len(generated), 'generated': generated}
    (run_output / f'interview-prep-report-{run_id}.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    (data_output / f'interview-prep-report-{run_id}.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('Done.')
    print(f'Run output: {run_output.resolve()}')
    print(f'Interview prep copied to: {data_output.resolve()}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
