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

def resume_family_for(role_code: str) -> str:
    code = role_code.lower()
    if code.startswith("support"):
        return "application-support / production-support"
    if code == "sre":
        return "sre-adjacent production support"
    if code.startswith("ba") or code == "bsa":
        return "business analyst / business systems analyst"
    if code == "ops":
        return "operations / application-support hybrid"
    return "general BA / application-support"

def summary_direction(company: str, role: str, role_code: str) -> str:
    code = role_code.lower()
    if code.startswith("support"):
        return (
            "Position Paul as a senior BA/application support professional with strong production support, "
            "release validation, incident coordination, runbook, Linux, Oracle, and financial enterprise systems experience."
        )
    if code == "sre":
        return (
            "Position Paul as SRE-adjacent: production support, Linux, monitoring/readiness, incident coordination, "
            "runbooks, and financial market data stability; avoid overstating deep platform engineering."
        )
    if code.startswith("ba") or code == "bsa":
        return (
            "Position Paul as a senior BA/BSA with enterprise modernization, requirements, UAT, data validation, "
            "Jira/acceptance criteria, stakeholder management, and FRBNY financial systems experience."
        )
    if code == "ops":
        return (
            "Position Paul as an operations/application-support hybrid with process discipline, data validation, "
            "stakeholder coordination, production readiness, and enterprise systems support."
        )
    return (
        "Position Paul around BA, application support, requirements, UAT, production readiness, and enterprise systems."
    )

def themes_for(role_code: str, company: str, role: str) -> list[str]:
    code = role_code.lower()
    role_l = role.lower()
    themes: list[str] = []

    if code.startswith("support"):
        themes += [
            "Application and production support",
            "Incident coordination and escalation",
            "Release readiness and post-release validation",
            "Runbooks and operational documentation",
            "Linux / Oracle / AWS-connected enterprise systems",
        ]
    elif code == "sre":
        themes += [
            "Linux-based production support",
            "Operational readiness and incident response",
            "Monitoring and health checks",
            "Market data / financial data stability",
            "Runbook-driven support discipline",
        ]
    elif code.startswith("ba") or code == "bsa":
        themes += [
            "Requirements analysis and stakeholder communication",
            "Jira stories and acceptance criteria",
            "UAT planning and business validation",
            "Data validation and Oracle/API comparison",
            "Enterprise modernization and SDLC coordination",
        ]
    elif code == "ops":
        themes += [
            "Operations support and process execution",
            "Cross-functional coordination",
            "Data quality and reporting",
            "Workflow analysis",
            "Operational readiness",
        ]

    if "ai" in code or " ai " in f" {role_l} ":
        themes.append("AI-assisted business analysis and documentation workflow")
    if "workday" in code or "workday" in role_l:
        themes.append("Enterprise application workflow support / Workday transferability")
    if "gis" in code or "gis" in role_l:
        themes.append("Requirements and validation transferability for GIS/geospatial workflows")
    if any(x in company.lower() for x in ["citi", "barclays", "dtcc", "finbourne", "dow jones"]):
        themes.append("Financial services / regulated enterprise environment")

    return themes

def bullets_to_emphasize(role_code: str) -> list[str]:
    code = role_code.lower()
    if code.startswith("support"):
        return [
            "Supported enterprise financial applications delivering fixed-income pricing, reference data, and streaming market data across Linux, Oracle, OpenShift, and AWS-connected infrastructure.",
            "Coordinated production incident troubleshooting through log review, environment validation, data validation, escalation, and cross-team issue resolution.",
            "Maintained runbooks, deployment procedures, troubleshooting guides, validation checklists, and support documentation.",
            "Executed release readiness testing, deployment validation, post-release health checks, and operational verification.",
        ]
    if code == "sre":
        return [
            "Supported Linux-based enterprise financial applications requiring production readiness and operational validation.",
            "Coordinated incident troubleshooting, health checks, escalation, and release validation across technical teams.",
            "Supported market data / pricing systems where timeliness, data quality, and availability were business critical.",
        ]
    if code.startswith("ba") or code == "bsa":
        return [
            "Collaborated with Product Owners and Scrum Masters to decompose epics into Jira user stories, acceptance criteria, and implementation-ready requirements.",
            "Validated REST API pricing payloads against Oracle data sources during migration from legacy on-premise services to AWS-hosted microservices.",
            "Coordinated UAT planning, test data setup, defect tracking, workflow validation, and business signoff readiness.",
            "Produced requirements, validation checklists, implementation notes, operational documentation, and stakeholder-facing support materials.",
        ]
    if code == "ops":
        return [
            "Coordinated operational readiness, validation, issue follow-up, and cross-functional execution across enterprise systems teams.",
            "Supported reporting, workflow validation, data quality, and stakeholder communication for business and technology operations.",
            "Used Excel/Power Query-style analysis and structured documentation to support operational decisions.",
        ]
    return [
        "Emphasize FRBNY BA/application support experience.",
        "Emphasize enterprise systems, requirements, UAT, release readiness, and stakeholder communication.",
    ]

def bullets_to_rewrite(role_code: str, role: str) -> list[str]:
    code = role_code.lower()
    role_l = role.lower()
    items = []
    if code.startswith("support"):
        items += [
            "Rewrite summary to lead with application/production support before generic BA language.",
            "Add one bullet explicitly connecting runbooks, incident coordination, and release validation.",
            "Use production stability, operational readiness, and support documentation language."
        ]
    elif code.startswith("ba") or code == "bsa":
        items += [
            "Rewrite summary to lead with requirements, UAT, stakeholder management, and enterprise modernization.",
            "Add one bullet connecting Oracle/API validation to business acceptance and migration confidence.",
            "Use Jira, acceptance criteria, traceability, and business validation language."
        ]
    elif code == "sre":
        items += [
            "Rewrite summary to say SRE-adjacent production support, not pure SRE.",
            "Add one bullet connecting Linux, health checks, incident coordination, and market data stability.",
            "Avoid implying direct ownership of Kubernetes/OpenShift platform engineering."
        ]
    elif code == "ops":
        items += [
            "Rewrite summary to bridge BA/application support into operations execution.",
            "Add one bullet emphasizing process discipline, data validation, and cross-functional follow-through."
        ]

    if "ai" in code or " ai " in f" {role_l} ":
        items.append("Add a carefully worded AI-assisted workflow bullet: used AI tools to structure JD analysis, documentation, and decision support; do not claim production AI engineering.")

    if "workday" in code or "workday" in role_l:
        items.append("Add transferability language for Workday: enterprise application support, workflow analysis, UAT, and rapid platform ramp-up.")

    if "gis" in code or "gis" in role_l:
        items.append("Add transferability language for GIS: requirements gathering, data validation, user workflows, and UAT for domain-specific applications.")

    return items or ["Review role-specific keywords and adjust summary/top bullets manually."]

def keywords(role_code: str, company: str, role: str) -> list[str]:
    code = role_code.lower()
    role_l = role.lower()
    words = ["requirements", "UAT", "stakeholder communication", "documentation", "data validation"]

    if code.startswith("support"):
        words += ["application support", "production support", "incident management", "runbooks", "release validation", "ServiceNow", "Linux", "Oracle"]
    if code == "sre":
        words += ["Linux", "monitoring", "incident response", "operational readiness", "health checks", "market data"]
    if code.startswith("ba") or code == "bsa":
        words += ["business analysis", "Jira", "user stories", "acceptance criteria", "SDLC", "Agile", "REST API", "Oracle"]
    if code == "ops":
        words += ["operations", "process improvement", "workflow", "reporting", "cross-functional coordination"]
    if "ai" in code or " ai " in f" {role_l} ":
        words += ["AI enablement", "AI-assisted analysis", "workflow automation", "documentation"]
    if "workday" in code or "workday" in role_l:
        words += ["Workday", "HRIS", "enterprise applications", "workflow support"]
    if "gis" in code or "gis" in role_l:
        words += ["GIS", "geospatial", "requirements validation", "user workflows"]
    if any(x in company.lower() for x in ["citi", "barclays", "dtcc", "finbourne", "dow jones"]):
        words += ["financial services", "regulated environment", "risk", "controls"]

    seen = []
    for w in words:
        if w not in seen:
            seen.append(w)
    return seen

def claims_to_avoid(role_code: str, role: str) -> list[str]:
    code = role_code.lower()
    role_l = role.lower()
    avoid = [
        "Do not overstate hands-on Python experience; present as learning/ramp-up unless project evidence is included.",
        "Do not claim direct ownership of tools/platforms not actually used.",
    ]
    if "ai" in code or " ai " in f" {role_l} ":
        avoid.append("Do not claim AI engineering, model training, or production AI ownership; position AI as analysis/documentation/workflow enablement.")
    if "workday" in code or "workday" in role_l:
        avoid.append("Do not claim direct Workday administration if experience is transferable rather than hands-on.")
    if "gis" in code or "gis" in role_l:
        avoid.append("Do not claim direct GIS development/administration unless supported elsewhere.")
    if code == "sre":
        avoid.append("Do not position as a deep infrastructure/SRE engineer; use SRE-adjacent production support framing.")
    return avoid

def cover_angle(company: str, role: str, role_code: str) -> str:
    code = role_code.lower()
    if code.startswith("support"):
        return f"Open with production/application support fit: FRBNY financial systems, incident coordination, release readiness, and runbook-driven operational stability for {role} at {company}."
    if code == "sre":
        return f"Open with production support and market data stability, framing SRE fit as operational readiness, Linux support, monitoring awareness, and incident coordination for {company}."
    if code.startswith("ba") or code == "bsa":
        return f"Open with BA/BSA fit: requirements, UAT, data validation, enterprise modernization, and stakeholder communication relevant to {role} at {company}."
    if code == "ops":
        return f"Open with operations/support hybrid fit: workflow execution, data quality, operational readiness, and cross-functional coordination for {role} at {company}."
    return f"Open with BA/application support fit for {role} at {company}."

def generate_tailoring(e: dict[str, Any]) -> dict[str, Any]:
    company = str(e.get("company") or "Unknown")
    role = str(e.get("role") or "Unknown")
    role_code = str(e.get("role_code") or "unknown")
    rec = str(e.get("pursuit_recommendation") or "apply_selectively")
    score = int(e.get("combined_strategy_score") or 0)

    return {
        "company": company,
        "role": role,
        "role_code": role_code,
        "pursuit_recommendation": rec,
        "combined_strategy_score": score,
        "recommended_resume_family": resume_family_for(role_code),
        "summary_direction": summary_direction(company, role, role_code),
        "top_resume_themes": themes_for(role_code, company, role),
        "bullets_to_emphasize": bullets_to_emphasize(role_code),
        "bullets_to_rewrite_or_add": bullets_to_rewrite(role_code, role),
        "keywords_to_include": keywords(role_code, company, role),
        "claims_to_avoid": claims_to_avoid(role_code, role),
        "cover_letter_angle": cover_angle(company, role, role_code),
        "interview_story_focus": to_list(e.get("interview_story_focus")) or [],
        "next_action": f"Use this tailoring guidance to update the resume for {company} — {role}.",
    }

def render_one(run_id: str, t: dict[str, Any]) -> str:
    return f"""---
type: resume_tailoring
status: draft
run_id: {run_id}
source: career-system
company: {t['company']}
role: {t['role']}
role_code: {t['role_code']}
pursuit_recommendation: {t['pursuit_recommendation']}
combined_strategy_score: {t['combined_strategy_score']}
recommended_resume_family: {t['recommended_resume_family']}
---

# Resume Tailoring — {t['company']} — {t['role']}

## Recommended Resume Family

{t['recommended_resume_family']}

## Summary Direction

{t['summary_direction']}

## Top Resume Themes

{md_list(t['top_resume_themes'])}

## Bullets To Emphasize

{md_list(t['bullets_to_emphasize'])}

## Bullets To Rewrite / Add

{md_list(t['bullets_to_rewrite_or_add'])}

## Keywords To Include

{md_list(t['keywords_to_include'])}

## Claims To Avoid

{md_list(t['claims_to_avoid'])}

## Cover Letter Angle

{t['cover_letter_angle']}

## Interview Story Focus

{md_list(t['interview_story_focus'])}

## Next Action

{t['next_action']}
"""

def render_report(run_id: str, items: list[dict[str, Any]]) -> str:
    lines = [
        "---", "type: resume_tailoring_report", "status: draft", f"run_id: {run_id}",
        "source: career-system", f"candidate_count: {len(items)}", "---", "",
        f"# Resume Tailoring Report — {run_id}", "",
        "## Summary", "", f"- Candidate count: **{len(items)}**",
        "- Scoring model: deterministic v0.8.0",
        "- Purpose: convert candidate explainability into role-specific resume tailoring guidance.",
        "", "## Tailoring Index", "",
        "| Rank | Score | Recommendation | Company | Role | Resume Family | Role Code |",
        "|---:|---:|---|---|---|---|---|",
    ]
    for i, t in enumerate(items, 1):
        lines.append(f"| {i} | {t['combined_strategy_score']} | {t['pursuit_recommendation']} | {t['company']} | {t['role']} | {t['recommended_resume_family']} | {t['role_code']} |")
    lines += ["", "## How To Use This", "", "1. Start with top `pursue_first` roles.", "2. Use each file's Summary Direction and Bullets To Emphasize sections to tailor the resume.", "3. Use Claims To Avoid to prevent overstating experience.", "4. Use Cover Letter Angle and Interview Story Focus for application package prep."]
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
    for path in sorted(input_dir.glob("candidate-explainability-*.json")):
        if path.name.startswith("candidate-explainability-report-"):
            continue
        tailoring = generate_tailoring(load_json(path))
        items.append(tailoring)
        slug = slugify(f"{tailoring['company']}-{tailoring['role_code']}-2026")
        write_json(output_dir / f"resume-tailor-{slug}.json", tailoring)
        (output_dir / f"resume-tailor-{slug}.md").write_text(render_one(args.run_id, tailoring), encoding="utf-8")
        print(f"generated resume tailoring: {path.name} -> resume-tailor-{slug}.md")

    items.sort(key=lambda x: (x["combined_strategy_score"], x["pursuit_recommendation"]), reverse=True)

    report_base = f"resume-tailoring-report-{args.run_id}"
    write_json(output_dir / f"{report_base}.json", {"type": "resume_tailoring_report", "run_id": args.run_id, "candidate_count": len(items), "items": items})
    (output_dir / f"{report_base}.md").write_text(render_report(args.run_id, items), encoding="utf-8")
    print(f"generated resume tailoring report: {report_base}.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
