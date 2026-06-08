#!/usr/bin/env python3
"""Generate candidate/job matching reports from JD intelligence files.

v0.5.1 is intentionally deterministic and conservative. It is a ranking aid,
not a hiring guarantee and not a replacement for manual review.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "unknown"


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive CLI behavior
        return {"_load_error": str(exc), "_source_file": str(path)}


def flatten_text(value: Any) -> str:
    parts: list[str] = []
    if isinstance(value, dict):
        for k, v in value.items():
            parts.append(str(k))
            parts.append(flatten_text(v))
    elif isinstance(value, list):
        for item in value:
            parts.append(flatten_text(item))
    elif value is not None:
        parts.append(str(value))
    return "\n".join(p for p in parts if p)


def first_nonempty(data: dict[str, Any], keys: list[str], default: str = "") -> str:
    for key in keys:
        val = data.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    # Try common nested metadata containers.
    for container in ("metadata", "frontmatter", "jd", "source"):
        obj = data.get(container)
        if isinstance(obj, dict):
            for key in keys:
                val = obj.get(key)
                if isinstance(val, str) and val.strip():
                    return val.strip()
    return default


def infer_from_filename(path: Path) -> tuple[str, str, str]:
    name = path.stem
    name = name.removeprefix("jd-intelligence-")
    name = re.sub(r"-2026$", "", name)
    parts = name.split("-")
    role_markers = {"ba", "bsa", "sba", "ops", "sre", "support", "appsupport", "pm", "ai", "it", "workday", "requirements"}
    split_at = len(parts)
    for i, part in enumerate(parts):
        if part in role_markers:
            split_at = i
            break
    company = " ".join(parts[:split_at]).title() if split_at else "Unknown"
    role_code = "-".join(parts[split_at:]) if split_at < len(parts) else "unknown"
    title = role_code.replace("-", " ").title()
    return company, title, role_code


def score_terms(text: str, term_scores: dict[str, int]) -> tuple[int, list[str]]:
    score = 0
    hits: list[str] = []
    lowered = text.lower()
    for term, points in term_scores.items():
        pattern = r"\b" + re.escape(term.lower()) + r"\b"
        if re.search(pattern, lowered):
            score += points
            hits.append(term)
    return score, hits


def recommendation(score: int) -> str:
    if score >= 85:
        return "apply_now"
    if score >= 70:
        return "apply_selectively"
    if score >= 55:
        return "possible_but_tailor_carefully"
    return "deprioritize"


def resume_family(role_code: str, text: str) -> str:
    rc = role_code.lower()
    if rc.startswith("support"):
        return "support"
    if rc.startswith("ops"):
        return "ops"
    if rc.startswith("sre"):
        return "sre"
    if rc.startswith("ba") or rc.startswith("bsa") or rc.startswith("sba"):
        return "ba"
    lowered = text.lower()
    if "application support" in lowered or "production support" in lowered or "technical support" in lowered:
        return "support"
    if "business analyst" in lowered or "business systems analyst" in lowered:
        return "ba"
    if "operations" in lowered:
        return "ops"
    return "ba"


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None identified."
    return "\n".join(f"- {item}" for item in items)


def analyze(path: Path, run_id: str) -> dict[str, Any]:
    data = load_json(path)
    raw_text = flatten_text(data)
    company_f, title_f, role_code_f = infer_from_filename(path)

    company = first_nonempty(data, ["company", "employer"], company_f)
    title = first_nonempty(data, ["title", "source_title", "normalized_title", "role_title"], title_f)
    role_code = first_nonempty(data, ["role_code"], role_code_f)

    text = "\n".join([company, title, role_code, raw_text])

    positive_terms = {
        "business analyst": 10,
        "business systems analyst": 10,
        "requirements": 8,
        "stakeholder": 6,
        "uat": 8,
        "acceptance criteria": 7,
        "jira": 6,
        "confluence": 4,
        "application support": 12,
        "production support": 14,
        "technical support": 8,
        "incident": 9,
        "troubleshooting": 8,
        "runbook": 8,
        "release": 8,
        "deployment": 8,
        "monitoring": 6,
        "linux": 10,
        "oracle": 8,
        "sql": 7,
        "api": 8,
        "rest": 8,
        "data": 5,
        "financial": 8,
        "banking": 7,
        "insurance": 6,
        "healthcare": 5,
        "market data": 12,
        "reference data": 10,
        "operations": 6,
        "workflow": 6,
        "service management": 5,
        "servicenow": 5,
        "ai": 3,
    }

    gap_terms = {
        "workday": -8,
        "hris": -7,
        "salesforce": -6,
        "kubernetes": -8,
        "terraform": -8,
        "java developer": -12,
        "software engineer": -8,
        "machine learning": -10,
        "data scientist": -12,
        "marketing": -8,
        "content strategy": -6,
        "people manager": -8,
        "manage a team": -8,
        "on-call": -3,
    }

    score = 50
    pos_score, pos_hits = score_terms(text, positive_terms)
    gap_score, gap_hits = score_terms(text, gap_terms)
    score += pos_score + gap_score

    # Role family adjustment based on Paul's current targets.
    family = resume_family(role_code, text)
    if family in {"ba", "support"}:
        score += 12
    elif family == "ops":
        score += 6
    elif family == "sre":
        score += 4

    # Cap score to keep deterministic output readable.
    score = max(0, min(100, score))

    strengths: list[str] = []
    if family == "ba":
        strengths.append("BA/BSA alignment with requirements, stakeholder communication, UAT, and workflow experience.")
    if family == "support":
        strengths.append("Application/production support alignment with FRBNY release coordination, validation, and troubleshooting experience.")
    if family == "ops":
        strengths.append("Operations alignment with process, workflow, data, and cross-functional coordination experience.")
    if family == "sre":
        strengths.append("SRE-adjacent alignment with Linux, monitoring, incident response, release validation, and market-data operations.")
    if pos_hits:
        strengths.append("Matched keywords: " + ", ".join(sorted(set(pos_hits))[:18]) + ".")

    gaps: list[str] = []
    if gap_hits:
        gaps.append("Potential gap keywords: " + ", ".join(sorted(set(gap_hits))) + ".")
    if "ai" in text.lower():
        gaps.append("AI should be positioned as AI-assisted BA/knowledge workflow experience, not AI engineering, unless the JD is non-technical/user-facing.")
    if family == "ops":
        gaps.append("Ops roles may require stronger evidence of direct operational ownership; tailor around workflow, data validation, and cross-functional execution.")
    if not gaps:
        gaps.append("No major deterministic gap identified; review JD manually before applying.")

    tailoring_focus: list[str] = []
    if family == "ba":
        tailoring_focus = ["requirements analysis", "UAT", "stakeholder communication", "Jira/user stories", "data/API validation"]
    elif family == "support":
        tailoring_focus = ["production support", "incident troubleshooting", "runbooks", "release validation", "Linux/API/data support"]
    elif family == "ops":
        tailoring_focus = ["operations coordination", "workflow execution", "data quality", "process improvement", "cross-functional support"]
    elif family == "sre":
        tailoring_focus = ["Linux operations", "monitoring", "incident response", "release readiness", "financial market data"]

    rec = recommendation(score)
    next_action_map = {
        "apply_now": "Prioritize this role. Tailor resume immediately and prepare a short cover/recruiter note.",
        "apply_selectively": "Apply if the location, compensation, and benefits are acceptable; tailor resume before submitting.",
        "possible_but_tailor_carefully": "Review gaps carefully before applying; use only if role is attractive or strategically useful.",
        "deprioritize": "Deprioritize unless there is a strong personal/company reason to apply.",
    }

    slug = slugify(f"{company}-{role_code}-2026")
    return {
        "run_id": run_id,
        "source_file": str(path),
        "slug": slug,
        "company": company,
        "title": title,
        "role_code": role_code,
        "resume_family": family,
        "match_score": score,
        "recommendation": rec,
        "strengths": strengths,
        "gaps": gaps,
        "tailoring_focus": tailoring_focus,
        "next_action": next_action_map[rec],
    }


def render_match(item: dict[str, Any]) -> str:
    return f"""---
type: candidate_match
status: draft
run_id: {item['run_id']}
source: career-system
company: {item['company']}
title: {item['title']}
role_code: {item['role_code']}
match_score: {item['match_score']}
recommendation: {item['recommendation']}
resume_family: {item['resume_family']}
---

# Candidate Match — {item['company']} — {item['title']}

## Summary

- Company: **{item['company']}**
- Role: **{item['title']}**
- Role Code: **{item['role_code']}**
- Match Score: **{item['match_score']}**
- Recommendation: **{item['recommendation']}**
- Resume Family: **{item['resume_family']}**

## Strengths

{bullet_list(item['strengths'])}

## Gaps / Risks

{bullet_list(item['gaps'])}

## Tailoring Focus

{bullet_list(item['tailoring_focus'])}

## Suggested Next Action

{item['next_action']}
"""


def render_report(items: list[dict[str, Any]], run_id: str) -> str:
    lines = [
        "---",
        "type: candidate_matching_report",
        "status: draft",
        f"run_id: {run_id}",
        "source: career-system",
        f"candidate_count: {len(items)}",
        "---",
        "",
        f"# Candidate Matching Report — {run_id}",
        "",
        "## Summary",
        "",
        f"- Candidate count: **{len(items)}**",
        "- Scoring model: deterministic v0.5.1",
        "- Purpose: prioritize jobs for application and resume tailoring.",
        "",
        "## Ranked Candidates",
        "",
        "| Rank | Score | Recommendation | Company | Role | Resume Family | Role Code |",
        "|---:|---:|---|---|---|---|---|",
    ]
    for idx, item in enumerate(items, 1):
        lines.append(
            f"| {idx} | {item['match_score']} | {item['recommendation']} | {item['company']} | {item['title']} | {item['resume_family']} | {item['role_code']} |"
        )
    lines.extend([
        "",
        "## How To Use This",
        "",
        "1. Start with `apply_now` roles.",
        "2. Use `apply_selectively` for roles with strong benefits, location, or strategic value.",
        "3. Treat `possible_but_tailor_carefully` as optional unless the role is especially attractive.",
        "4. Deprioritize low-scoring roles unless they are quick applies or networking opportunities.",
        "5. Review every recommendation manually before applying.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("jd-intelligence-*.json"))
    items = [analyze(path, args.run_id) for path in files]
    items.sort(key=lambda x: (-int(x["match_score"]), x["company"], x["title"]))

    for item in items:
        base = f"candidate-match-{item['slug']}"
        (output_dir / f"{base}.json").write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (output_dir / f"{base}.md").write_text(render_match(item), encoding="utf-8")
        print(f"generated candidate match: {Path(item['source_file']).name} -> {base}.md")

    report_base = f"candidate-matching-report-{args.run_id}"
    report = {
        "run_id": args.run_id,
        "candidate_count": len(items),
        "ranked_candidates": items,
    }
    (output_dir / f"{report_base}.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output_dir / f"{report_base}.md").write_text(render_report(items, args.run_id), encoding="utf-8")
    print(f"generated candidate matching report: {report_base}.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
