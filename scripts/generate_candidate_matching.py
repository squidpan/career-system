#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, re
from pathlib import Path
from typing import Any

USER_STRENGTH_TERMS = {
    "business analyst", "requirements", "uat", "jira", "acceptance criteria", "stakeholder",
    "application support", "production support", "incident", "runbook", "release", "deployment",
    "linux", "oracle", "aws", "api", "rest", "financial", "market data", "data validation",
    "operations", "workflow", "monitoring", "troubleshooting", "devops", "sdlc",
}

GAP_TERMS = {
    "workday": -10, "hris": -6, "gis": -8, "salesforce": -7, "unqork": -10,
    "deep ai": -5, "llm": -3, "prompt engineering": -3, "product marketing": -6,
    "customer success": -4, "payments": -3,
}

ROLE_BASE = {
    "support-appsupport": 92,
    "support-ops-lead": 88,
    "support-workday": 74,
    "ba": 89,
    "sba": 91,
    "bsa": 90,
    "ba-it": 91,
    "ba-ai": 87,
    "ba-pm": 86,
    "ba-requirements": 82,
    "ops": 80,
    "sre": 76,
}

INDUSTRY_BONUS = {
    "financial": 5, "bank": 5, "capital markets": 6, "fixed income": 6,
    "insurance": 4, "healthcare": 2, "utility": 2, "payments": 2,
}

COMPANY_STRATEGIC_BONUS = {
    "Citi": 3, "Barclays": 4, "FINBOURNE Technology": 4, "The Depository Trust & Clearing Corporation (DTCC)": 5,
    "New York Life": 4, "Dow Jones": 3, "Amtrak": 2, "Con Edison": 2, "Premera Blue Cross": 2,
}

BAD_TITLE_PREFIXES = ("**about", "**overview", "workforce classification", "**location designation", "**your success")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_get(d: dict[str, Any], *keys: str, default: Any = "") -> Any:
    cur: Any = d
    for k in keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return default
    return cur


def first_present(d: dict[str, Any], keys: list[str], default: str = "") -> str:
    for k in keys:
        v = d.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return default


def normalize_slug(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return text or "unknown"


def collect_text(data: dict[str, Any]) -> str:
    parts: list[str] = []
    def walk(x: Any):
        if isinstance(x, dict):
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
        elif isinstance(x, str):
            parts.append(x)
    walk(data)
    return "\n".join(parts).lower()


def choose_role(data: dict[str, Any]) -> tuple[str, str, str, str]:
    company = first_present(data, ["company", "Company"], "Unknown")
    source_title = first_present(data, ["source_title", "normalized_title", "role", "title", "job_title"], "Unknown")
    normalized_title = first_present(data, ["normalized_title", "source_title", "role", "title", "job_title"], source_title)
    if normalized_title.lower().startswith(BAD_TITLE_PREFIXES):
        normalized_title = source_title
    role_code = first_present(data, ["role_code", "role_family"], "unknown")
    if role_code == "unknown":
        role_code = infer_role_code(source_title + " " + normalized_title)
    return company, normalized_title, role_code, source_title


def infer_role_code(text: str) -> str:
    t = text.lower()
    if "site reliability" in t or re.search(r"\bsre\b", t): return "sre"
    if "application support" in t or "technical support" in t or "it support" in t: return "support-appsupport"
    if "workday" in t: return "support-workday"
    if "business systems analyst" in t or "business system analyst" in t: return "bsa"
    if "business analyst" in t and "project manager" in t: return "ba-pm"
    if "business analyst" in t and (" ai" in t or "artificial intelligence" in t): return "ba-ai"
    if "technical business analyst" in t or "it business" in t: return "ba-it"
    if "business analyst" in t: return "ba"
    if "operations" in t or "operational" in t: return "ops"
    return "unknown"


def resume_family(role_code: str) -> str:
    if role_code.startswith("support"): return "support"
    if role_code.startswith("ba") or role_code.startswith("bsa") or role_code.startswith("sba"): return "ba"
    if role_code.startswith("ops"): return "ops"
    if role_code.startswith("sre"): return "sre"
    return "ba"


def score_candidate(data: dict[str, Any], role_code: str, company: str) -> tuple[int, list[str], list[str], str]:
    text = collect_text(data)
    score = ROLE_BASE.get(role_code, 68)
    strengths: list[str] = []
    gaps: list[str] = []

    for term in USER_STRENGTH_TERMS:
        if term in text:
            strengths.append(term)
            score += 1
    strengths = sorted(set(strengths))[:10]

    for term, penalty in GAP_TERMS.items():
        if term in text:
            gaps.append(term)
            score += penalty
    gaps = sorted(set(gaps))[:8]

    for term, bonus in INDUSTRY_BONUS.items():
        if term in text:
            score += bonus
    score += COMPANY_STRATEGIC_BONUS.get(company, 0)

    # Avoid universal 100s; keep practical spread.
    score = max(45, min(96, score))
    if score >= 88:
        rec = "apply_now"
    elif score >= 78:
        rec = "apply_selectively"
    elif score >= 68:
        rec = "possible_but_tailor_carefully"
    else:
        rec = "deprioritize"
    return score, strengths, gaps, rec


def render_match(run_id: str, src: Path, data: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    company, title, role_code, source_title = choose_role(data)
    fam = resume_family(role_code)
    score, strengths, gaps, recommendation = score_candidate(data, role_code, company)
    slug = normalize_slug(src.stem.replace("jd-intelligence-", ""))
    out_slug = f"candidate-match-{slug}"
    obj = {
        "type": "candidate_match", "status": "draft", "run_id": run_id, "source": "career-system",
        "company": company, "title": title, "source_title": source_title, "role_code": role_code,
        "resume_family": fam, "score": score, "recommendation": recommendation,
        "strengths": strengths, "gaps": gaps, "source_file": str(src),
    }
    md = f"""---
type: candidate_match
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
resume_family: {fam}
score: {score}
recommendation: {recommendation}
---

# Candidate Match — {company} — {title}

## Summary

- Score: **{score}**
- Recommendation: **{recommendation}**
- Resume family: **{fam}**
- Role code: **{role_code}**

## Strengths To Emphasize

{chr(10).join('- ' + s for s in strengths) if strengths else '- Review manually'}

## Gaps / Cautions

{chr(10).join('- ' + g for g in gaps) if gaps else '- No major deterministic gaps identified'}

## Resume Strategy

Use the **{fam}** resume path first. Tailor the professional summary and top 6 bullets toward the role code `{role_code}`.
"""
    return out_slug, {"json": obj, "md": md}


def write_report(run_id: str, output_dir: Path, candidates: list[dict[str, Any]]) -> None:
    candidates.sort(key=lambda c: (-c["score"], c["company"], c["title"]))
    report_json = {"type":"candidate_matching_report", "status":"draft", "run_id":run_id, "candidate_count":len(candidates), "candidates":candidates}
    (output_dir / f"candidate-matching-report-{run_id}.json").write_text(json.dumps(report_json, indent=2), encoding="utf-8")
    rows = []
    for i, c in enumerate(candidates, 1):
        rows.append(f"| {i} | {c['score']} | {c['recommendation']} | {c['company']} | {c['title']} | {c['resume_family']} | {c['role_code']} |")
    md = f"""---
type: candidate_matching_report
status: draft
run_id: {run_id}
source: career-system
candidate_count: {len(candidates)}
---

# Candidate Matching Report — {run_id}

## Summary

- Candidate count: **{len(candidates)}**
- Scoring model: deterministic v0.5.1.2
- Purpose: prioritize jobs for application and resume tailoring.

## Ranked Candidates

| Rank | Score | Recommendation | Company | Role | Resume Family | Role Code |
|---:|---:|---|---|---|---|---|
{chr(10).join(rows)}

## How To Use This

1. Start with `apply_now` roles.
2. Use `apply_selectively` for roles with strong benefits, location, or strategic value.
3. Treat `possible_but_tailor_carefully` as optional unless the role is especially attractive.
4. Deprioritize low-scoring roles unless they are quick applies or networking opportunities.
5. Review every recommendation manually before applying.
"""
    (output_dir / f"candidate-matching-report-{run_id}.md").write_text(md, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    candidates = []
    for src in sorted(input_dir.glob("jd-intelligence-*.json")):
        if src.name.startswith("jd-intelligence-report-"):
            continue
        data = read_json(src)
        slug, rendered = render_match(args.run_id, src, data)
        obj = rendered["json"]
        candidates.append(obj)
        (output_dir / f"{slug}.json").write_text(json.dumps(obj, indent=2), encoding="utf-8")
        (output_dir / f"{slug}.md").write_text(rendered["md"], encoding="utf-8")
        print(f"generated candidate match: {src.name} -> {slug}.md")

    write_report(args.run_id, output_dir, candidates)
    print(f"generated candidate matching report: candidate-matching-report-{args.run_id}.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
