#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

def split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, parts[2]

def read_doc(path: Path):
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    return {"path": path, "frontmatter": fm, "body": body, "text": text}

def slug_from_filename(path: Path) -> str:
    name = path.stem
    for prefix in ["jd-", "role-", "resume-", "gap-", "interview-prep-", "jd-intelligence-"]:
        if name.startswith(prefix):
            name = name[len(prefix):]
    for suffix in ["-v1", "-teal-v1", "-assembled-v1"]:
        if name.endswith(suffix):
            name = name[:-len(suffix)]
    return name

def find_by_slug(folder: Path, prefix: str, slug: str, ext: str = ".md") -> Path | None:
    direct = folder / f"{prefix}{slug}{ext}"
    if direct.exists():
        return direct
    slug_tokens = set(slug.split("-"))
    best, best_score = None, 0
    for p in folder.glob(f"*{ext}"):
        ptokens = set(slug_from_filename(p).split("-"))
        score = len(slug_tokens & ptokens)
        if score > best_score:
            best, best_score = p, score
    return best if best_score >= 2 else None

def read_gap_json(gap_md: Path) -> dict:
    js = gap_md.with_suffix(".json")
    if js.exists():
        return json.loads(js.read_text(encoding="utf-8"))
    doc = read_doc(gap_md)
    fm = doc["frontmatter"]
    return {
        "company": fm.get("company", ""),
        "title": fm.get("title", ""),
        "role_code": fm.get("role_code", ""),
        "overall_match_score": int(fm.get("overall_match_score") or 0),
        "recommendation": fm.get("recommendation", ""),
        "effort_level": fm.get("effort_level", ""),
        "matched": {},
        "missing": {},
    }

def read_intelligence(intel_dir: Path, slug: str) -> tuple[dict, str]:
    p = find_by_slug(intel_dir, "jd-intelligence-", slug, ".json")
    if p and p.exists():
        return json.loads(p.read_text(encoding="utf-8")), str(p)
    return {"intelligence": {}, "jd_aware_questions": [], "story_mapping": []}, ""

def md_list(items):
    if not items:
        return "- None identified\n"
    return "".join(f"- {x}\n" for x in items)

def numbered(items):
    if not items:
        return "1. None identified\n"
    return "".join(f"{i+1}. {x}\n" for i, x in enumerate(items))

def dedupe(items):
    seen, out = set(), []
    for x in items:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out

def baseline_questions(role_code: str, gap: dict):
    rc = (role_code or "").lower()
    missing = gap.get("missing", {}) or {}
    q = []
    if "support" in rc or "ops" in rc or "sre" in rc:
        q += [
            "Tell me about a production issue you helped investigate or resolve.",
            "How do you validate that an application is healthy after a deployment?",
            "How do you use runbooks during release or support activities?",
            "How do you coordinate with DevOps, infrastructure, database, QA, and business teams during an incident?",
            "How do you distinguish application issues from data, infrastructure, or environment issues?",
        ]
    if "ba" in rc or "bsa" in rc or "analyst" in rc:
        q += [
            "How do you gather requirements from multiple stakeholders?",
            "How do you turn an Epic into user stories and acceptance criteria?",
            "How do you handle conflicting business requirements?",
            "How do you support UAT and ensure business signoff?",
            "Describe a time you documented a complex workflow or system process.",
        ]
    if "sre" in rc:
        q += [
            "What Linux commands would you use first when troubleshooting performance or connectivity?",
            "How would you approach monitoring and alert triage?",
            "How do you think about resiliency, failover, and disaster recovery readiness?",
        ]
    for tool in missing.get("tools", []) or []:
        q.append(f"What is your exposure to {tool}, and how would you ramp up quickly if this role requires it?")
        q.append(f"How would you support a team using {tool} even if you are not the primary administrator?")
    return dedupe(q)

def gap_strategy(gap: dict):
    missing = gap.get("missing", {}) or {}
    rows = []
    for tool in missing.get("tools", []) or []:
        rows.append(f"If asked about {tool}, be direct that you have not been the primary {tool} administrator, then bridge to enterprise application support, requirements, UAT, workflow analysis, and fast ramp-up.")
    for skill in missing.get("skills", []) or []:
        rows.append(f"For {skill}, connect related experience from FRBNY, HP PPM, release coordination, or UAT.")
    for domain in missing.get("domains", []) or []:
        rows.append(f"For {domain}, show how you learn domain context through stakeholders, process documentation, data analysis, and UAT.")
    return rows

def intel_summary(intel: dict):
    data = intel.get("intelligence", {}) or {}
    return f"""### JD-Specific Tools

{md_list(data.get("tools", []) or [])}
### JD-Specific Platforms

{md_list(data.get("platforms", []) or [])}
### JD-Specific Products

{md_list(data.get("products", []) or [])}
### JD-Specific Domains

{md_list(data.get("domains", []) or [])}
### JD-Specific Methodologies

{md_list(data.get("methodologies", []) or [])}
"""

def story_bank():
    return """### FRBNY enterprise financial application modernization

- Use for: application support, cloud modernization, REST API validation, release readiness
- Talking point: Use the AC Plus to OPS360/AWS modernization story. Emphasize requirements, validation, runbooks, release coordination, and cross-team execution.

### REST API validation against Oracle

- Use for: data validation, API testing, production readiness
- Talking point: Explain how REST payloads were compared against Oracle/legacy sources to protect data quality during migration.

### Deployment runbooks and health checks

- Use for: production support, release coordination, DevOps collaboration
- Talking point: Explain how runbooks, validation checklists, and post-release health checks reduced release risk.

### HP PPM insurance workflow analysis

- Use for: business analysis, workflow, PMO, UAT
- Talking point: Explain requirements, workflow configuration/testing, representative UAT data, reporting, and stakeholder support.

### Financial data platform implementation

- Use for: reference data, pricing data, data quality, financial systems
- Talking point: Explain ACPlus/Asset Control, golden copy, vendor feeds, normalization, and downstream data distribution.
"""

def generate_one(gap_path: Path, jds_dir: Path, roles_dir: Path, resumes_dir: Path, intel_dir: Path, output_dir: Path, run_id: str):
    gap = read_gap_json(gap_path)
    slug = slug_from_filename(gap_path)
    jd_path = find_by_slug(jds_dir, "jd-", slug)
    role_path = find_by_slug(roles_dir, "role-", slug)
    resume_path = find_by_slug(resumes_dir, "resume-", slug)
    intel, intel_file = read_intelligence(intel_dir, slug)
    jd = read_doc(jd_path) if jd_path else {"frontmatter": {}}
    role = read_doc(role_path) if role_path else {"frontmatter": {}}
    company = gap.get("company") or jd["frontmatter"].get("company") or "unknown-company"
    title = gap.get("title") or jd["frontmatter"].get("normalized_title") or slug
    role_code = gap.get("role_code") or jd["frontmatter"].get("role_code") or role["frontmatter"].get("role_code") or ""
    matched = gap.get("matched", {}) or {}
    missing = gap.get("missing", {}) or {}
    jd_questions = intel.get("jd_aware_questions", []) or []
    all_questions = dedupe(jd_questions + baseline_questions(role_code, gap))
    story_mapping = intel.get("story_mapping", []) or []
    out_path = output_dir / f"interview-prep-{slug}.md"
    md = f"""---
type: interview_prep
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
gap_file: {gap_path}
jd_file: {jd_path or ""}
role_file: {role_path or ""}
resume_file: {resume_path or ""}
jd_intelligence_file: {intel_file}
---

# Interview Prep — {company} — {title}

## Role Snapshot

- Company: **{company}**
- Role: **{title}**
- Role Code: **{role_code}**
- Gap Match Score: **{gap.get("overall_match_score", "")}**
- Gap Recommendation: **{gap.get("recommendation", "")}**
- Estimated Effort: **{gap.get("effort_level", "")}**

## Positioning Statement

I am a Senior Business Analyst and Application Support professional with experience supporting enterprise financial applications, production readiness, release coordination, requirements, UAT, runbooks, REST API validation, Oracle data comparison, and cross-functional delivery across financial services and insurance environments.

## JD Intelligence Summary

{intel_summary(intel)}
## Strengths To Emphasize

### Matched Skills

{md_list(matched.get("skills", []) or [])}
### Matched Tools

{md_list(matched.get("tools", []) or [])}
### Matched Domains

{md_list(matched.get("domains", []) or [])}
## Gaps To Prepare For

### Missing Tools

{md_list(missing.get("tools", []) or [])}
### Missing Skills

{md_list(missing.get("skills", []) or [])}
### Missing Domains

{md_list(missing.get("domains", []) or [])}
## JD-Aware Interview Questions

{numbered(jd_questions)}
## Full Interview Question Set

{numbered(all_questions)}
## Gap-Based Answer Strategy

{md_list(gap_strategy(gap))}
## JD-to-Resume Story Mapping

{md_list(story_mapping)}
## Story Bank

{story_bank()}

## 30-Minute Study Guide

1. Re-read the JD intelligence summary and focus on extracted tools, products, domains, and methodologies.
2. Review the gap analysis and prepare a short answer for each missing tool or domain.
3. Practice the FRBNY modernization story in 90 seconds.
4. Practice the REST API validation against Oracle story in 60 seconds.
5. Practice the deployment runbook / health check story in 60 seconds.
6. Practice one JD-specific answer from the JD-Aware Interview Questions section.
7. Prepare one question for the hiring manager about first-90-day priorities.

## Questions To Ask Them

1. What are the most important systems or workflows this role supports?
2. What are the most common production or business issues the team handles?
3. What would success look like in the first 90 days?
4. Which tools, platforms, or products should I prioritize learning before joining?
5. How does the team manage requirements, UAT, release readiness, and post-release support?

## Notes

This v0.4.5 output integrates v0.4.3 interview prep with v0.4.4 JD intelligence. It is still deterministic, but now company-specific and JD-aware.
"""
    out_path.write_text(md, encoding="utf-8")
    return out_path

def main(argv):
    if len(argv) < 3:
        print("Usage: generate_interview_prep.py <run_id> <gap_analysis_dir> [jds_dir] [roles_dir] [resumes_dir] [jd_intelligence_dir]", file=sys.stderr)
        return 2
    run_id = argv[1]
    gap_dir = Path(argv[2])
    jds_dir = Path(argv[3]) if len(argv) > 3 else Path("data/jds/normalized")
    roles_dir = Path(argv[4]) if len(argv) > 4 else Path("data/roles")
    resumes_dir = Path(argv[5]) if len(argv) > 5 else Path("data/resume-versions/teal-export")
    intel_dir = Path(argv[6]) if len(argv) > 6 else Path("data/jd-intelligence")
    run_output = Path("ops/runs") / run_id / "output"
    data_output = Path("data/interview-prep")
    run_output.mkdir(parents=True, exist_ok=True)
    data_output.mkdir(parents=True, exist_ok=True)
    generated = []
    for gap_path in sorted(gap_dir.glob("gap-*.md")):
        out = generate_one(gap_path, jds_dir, roles_dir, resumes_dir, intel_dir, run_output, run_id)
        generated.append(out.name)
        (data_output/out.name).write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"generated interview prep: {gap_path.name} -> {out.name}")
    report = {"run_id": run_id, "count": len(generated), "generated": generated}
    for folder in [run_output, data_output]:
        (folder/f"interview-prep-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("Done.")
    print(f"Run output: {run_output.resolve()}")
    print(f"Interview prep copied to: {data_output.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
