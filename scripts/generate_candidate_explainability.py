#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

def slugify(text: str) -> str:
    text = text.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "unknown"

def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def to_list(x: Any) -> list[str]:
    if isinstance(x, list):
        return [str(v) for v in x if str(v).strip()]
    if x:
        return [str(x)]
    return []

def md_list(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items) if items else "- None"

def resume_focus(role_code: str, company: str, role: str) -> list[str]:
    code = role_code.lower()
    company_l = company.lower()
    role_l = role.lower()
    items: list[str] = []

    if code.startswith("support"):
        items += [
            "FRBNY application support and production support experience.",
            "Release validation, deployment readiness, runbooks, and post-release health checks.",
            "Incident coordination across DevOps, QA, database, infrastructure, operations, and business stakeholders.",
            "Linux, Oracle, AWS-connected services, ServiceNow, and monitoring/readiness language where truthful.",
        ]
    elif code == "sre":
        items += [
            "Linux-based production support and operational readiness.",
            "Incident troubleshooting, monitoring, runbooks, and release validation.",
            "Financial market data support and production stability.",
            "Frame as SRE-adjacent support, not deep infrastructure engineering unless directly true.",
        ]
    elif code.startswith("ba") or code == "bsa":
        items += [
            "BA/BSA requirements analysis, stakeholder communication, Jira stories, and acceptance criteria.",
            "UAT planning, data validation, defect tracking, and business signoff readiness.",
            "FRBNY modernization, REST API validation, Oracle data comparison, and enterprise system migration context.",
        ]
    elif code == "ops":
        items += [
            "Operations support, process discipline, issue coordination, and cross-functional execution.",
            "Data validation, workflow analysis, reporting, and operational readiness.",
            "Bridge BA/application support experience into business operations language.",
        ]
    else:
        items += ["Use BA/application support general positioning."]

    if any(x in company_l for x in ["citi", "barclays", "dtcc", "finbourne"]) or any(x in role_l for x in ["financial", "bank", "trading"]):
        items.append("Financial services, regulated environment, data quality, and operational risk awareness.")

    if "ai" in code or " ai " in f" {role_l} " or "artificial intelligence" in role_l:
        items.append("AI as business/process enablement: position Career System and ChatGPT workflow as practical AI-assisted analysis and documentation, not AI engineering.")

    if "workday" in code or "workday" in role_l:
        items.append("Enterprise application support and workflow analysis as a bridge to Workday; avoid claiming direct Workday administration.")

    if "gis" in code or "gis" in role_l:
        items.append("Requirements, data validation, and UAT transferability into GIS context; avoid overstating direct GIS hands-on experience.")

    return items

def story_focus(role_code: str, role: str) -> list[str]:
    code = role_code.lower()
    role_l = role.lower()
    items: list[str] = []

    if code.startswith("support"):
        items += [
            "FRBNY production support story: issue detection, log/data validation, escalation, communication, and closure.",
            "Release readiness story: runbook, deployment validation, post-release health checks, rollback/DR awareness.",
        ]
    elif code == "sre":
        items += [
            "Linux/application operations story: supporting production systems, checking health, and coordinating incidents.",
            "Market data stability story: timeliness, data quality, and escalation discipline.",
        ]
    elif code.startswith("ba") or code == "bsa":
        items += [
            "Modernization BA story: legacy/on-prem to AWS-connected services, requirements, testing, and business validation.",
            "REST API/Oracle validation story: comparing API payloads to source data and supporting migration confidence.",
            "Stakeholder story: translating business needs across DevOps, QA, operations, and management.",
        ]
    elif code == "ops":
        items += [
            "Operational readiness story: process discipline, handoffs, validation, and issue follow-through.",
            "Reporting/data story: Excel/Power Query, data quality, and operational decision support.",
        ]

    if "ai" in code or " ai " in f" {role_l} ":
        items.append("Career System story: using AI as a structured assistant to normalize JDs, compare roles, generate notes, and improve job-search operations.")

    return items or ["Use a concise enterprise application support / BA story grounded in FRBNY and prior consulting experience."]

def explain(strategy: dict[str, Any]) -> dict[str, Any]:
    company = str(strategy.get("company") or "Unknown")
    role = str(strategy.get("role") or "Unknown")
    role_code = str(strategy.get("role_code") or "unknown")
    rec = str(strategy.get("pursuit_recommendation") or "apply_selectively")
    technical = int(strategy.get("technical_match_score") or 0)
    personal = int(strategy.get("personal_strategy_score") or 0)
    combined = int(strategy.get("combined_strategy_score") or 0)

    reasons = to_list(strategy.get("reasons"))
    risks = to_list(strategy.get("risk_flags"))
    if not reasons:
        reasons = ["General match based on candidate matching and strategy scores."]
    if not risks:
        risks = ["No major deterministic risk flags detected; review manually before applying."]

    explanation = (
        f"{company} — {role} is marked `{rec}` because it combines a technical match score of {technical} "
        f"with a personal strategy score of {personal}, producing a combined score of {combined}. "
        f"The role code `{role_code}` maps to Paul's current positioning around BA/BSA, application support, "
        f"production readiness, regulated enterprise environments, and practical AI-assisted workflow interest where relevant."
    )

    if rec == "pursue_first":
        priority = "Top priority: tailor resume and apply promptly."
    elif rec == "apply_this_week":
        priority = "Strong priority: apply this week after normal tailoring."
    elif rec == "apply_selectively":
        priority = "Selective: apply if benefits, commute, and role details remain attractive."
    elif rec == "network_or_research_first":
        priority = "Research/network first before investing in full tailoring."
    else:
        priority = "Lower priority unless quick apply or strong personal interest."

    return {
        "company": company,
        "role": role,
        "role_code": role_code,
        "resume_family": strategy.get("resume_family", ""),
        "technical_match_score": technical,
        "personal_strategy_score": personal,
        "combined_strategy_score": combined,
        "pursuit_recommendation": rec,
        "explanation": explanation,
        "why_attractive": reasons,
        "risk_flags": risks,
        "resume_focus": resume_focus(role_code, company, role),
        "interview_story_focus": story_focus(role_code, role),
        "application_priority": priority,
        "next_action": str(strategy.get("next_action") or priority),
    }

def render_one(run_id: str, e: dict[str, Any]) -> str:
    return f"""---
type: candidate_explainability
status: draft
run_id: {run_id}
source: career-system
company: {e['company']}
role: {e['role']}
role_code: {e['role_code']}
technical_match_score: {e['technical_match_score']}
personal_strategy_score: {e['personal_strategy_score']}
combined_strategy_score: {e['combined_strategy_score']}
pursuit_recommendation: {e['pursuit_recommendation']}
---

# Candidate Explainability — {e['company']} — {e['role']}

## Recommendation

**{e['pursuit_recommendation']}**

## Explanation

{e['explanation']}

## Why This Role Is Attractive

{md_list(e['why_attractive'])}

## Resume Focus

{md_list(e['resume_focus'])}

## Interview / Story Focus

{md_list(e['interview_story_focus'])}

## Risks / Watch Items

{md_list(e['risk_flags'])}

## Application Priority

{e['application_priority']}

## Next Action

{e['next_action']}
"""

def render_report(run_id: str, items: list[dict[str, Any]]) -> str:
    lines = [
        "---", "type: candidate_explainability_report", "status: draft", f"run_id: {run_id}",
        "source: career-system", f"candidate_count: {len(items)}", "---", "",
        f"# Explainable Candidate Strategy Report — {run_id}", "",
        "## Summary", "", f"- Candidate count: **{len(items)}**",
        "- Scoring model: deterministic v0.7.0",
        "- Purpose: explain why each candidate strategy recommendation exists and how to act on it.",
        "", "## Ranked Explainability", "",
        "| Rank | Combined | Recommendation | Company | Role | Role Code | Short Reason |",
        "|---:|---:|---|---|---|---|---|",
    ]
    for i, e in enumerate(items, 1):
        short = "; ".join(e["why_attractive"][:2]).replace("|", "/")
        lines.append(f"| {i} | {e['combined_strategy_score']} | {e['pursuit_recommendation']} | {e['company']} | {e['role']} | {e['role_code']} | {short} |")
    lines += ["", "## How To Use This", "", "1. Start with `pursue_first` roles.", "2. Use each role's Resume Focus section to tailor the resume.", "3. Use each role's Interview / Story Focus section for recruiter calls and interviews.", "4. Review Risks / Watch Items before spending time on a full application."]
    return "\n".join(lines) + "\n"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    items = []
    for path in sorted(input_dir.glob("candidate-strategy-*.json")):
        if path.name.startswith("candidate-strategy-report-"):
            continue
        e = explain(load_json(path))
        items.append(e)
        slug = slugify(f"{e['company']}-{e['role_code']}-2026")
        write_json(output_dir / f"candidate-explainability-{slug}.json", e)
        (output_dir / f"candidate-explainability-{slug}.md").write_text(render_one(args.run_id, e), encoding="utf-8")
        print(f"generated candidate explainability: {path.name} -> candidate-explainability-{slug}.md")

    items.sort(key=lambda x: (x["combined_strategy_score"], x["technical_match_score"], x["personal_strategy_score"]), reverse=True)

    report_base = f"candidate-explainability-report-{args.run_id}"
    write_json(output_dir / f"{report_base}.json", {"type": "candidate_explainability_report", "run_id": args.run_id, "candidate_count": len(items), "items": items})
    (output_dir / f"{report_base}.md").write_text(render_report(args.run_id, items), encoding="utf-8")
    print(f"generated candidate explainability report: {report_base}.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
