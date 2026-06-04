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
    for prefix in ["jd-", "role-", "resume-", "gap-", "jd-intelligence-", "resume-tailoring-"]:
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

def read_json_for_md(md_path: Path) -> dict:
    js = md_path.with_suffix(".json")
    if js.exists():
        return json.loads(js.read_text(encoding="utf-8"))
    doc = read_doc(md_path)
    return {"frontmatter": doc["frontmatter"]}

def md_list(items):
    if not items:
        return "- None identified\n"
    return "".join(f"- {x}\n" for x in items)

def dedupe(items):
    seen, out = set(), []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out

def collect_intel_terms(intel: dict):
    data = intel.get("intelligence", {}) or {}
    terms = []
    for key in ["tools", "platforms", "products", "domains", "methodologies"]:
        terms.extend(data.get(key, []) or [])
    return dedupe(terms)

def promote_from_terms(terms, gap, role_code):
    promote = []
    rc = (role_code or "").lower()

    mapping = {
        "market data": [
            "Market data application support and financial data validation",
            "FRBNY fixed-income pricing and streaming market data experience",
            "Production support across financial services systems",
        ],
        "market data platform": [
            "Ticker plant / feed-processing concepts through FRBNY market data modernization",
            "Runbooks and validation for market-data distribution workflows",
        ],
        "redline": [
            "Vendor-platform support mindset using AC Plus / Asset Control / OPS360 experience",
            "Customer-facing production issue triage and vendor/product support approach",
        ],
        "linux": [
            "Linux client/server application support exposure",
            "Operational troubleshooting, health checks, and environment validation",
        ],
        "python": [
            "Current Python learning path and ability to ramp quickly",
            "Scripting/automation mindset from Korn shell, Bash, and deployment runbooks",
        ],
        "workday": [
            "Enterprise application support experience applicable to Workday workflows",
            "Requirements, UAT, workflow analysis, and service-management transferability",
        ],
        "hris platform": [
            "Enterprise workflow support and business-user requirements gathering",
            "Application support and UAT practices transferable to HR systems",
        ],
        "gis": [
            "Requirements analysis and UAT for domain-specific platforms",
            "REST API and Oracle validation experience transferable to GIS systems",
        ],
        "geospatial": [
            "Data validation and stakeholder-driven UAT approach",
            "Requirements translation between business users and technical teams",
        ],
        "rest api": [
            "REST API validation against Oracle and legacy source outputs",
            "Data reconciliation and acceptance criteria for API migration",
        ],
        "oracle": [
            "Oracle data comparison and validation experience",
            "Source-to-target validation and reconciliation discipline",
        ],
        "application support platform": [
            "Application and production support experience",
            "Support for business applications after development and through daily operations",
        ],
        "production operations platform": [
            "Start-of-day checks, monitoring, handoff, and operational readiness",
            "Production validation, release support, and post-release health checks",
        ],
        "production operations": [
            "Production issue triage and business-impact prioritization",
            "Operational support, release validation, and post-implementation stability",
        ],
        "risk and controls": [
            "Risk/impact assessment during releases and production incidents",
            "Control-minded production support and escalation discipline",
        ],
        "incident management": [
            "Incident triage, escalation, and cross-team coordination",
            "Production troubleshooting and support communication",
        ],
        "problem management": [
            "Recurring issue follow-up, defect triage, and bug-fix prioritization",
            "Root-cause-oriented support documentation and process improvement",
        ],
        "release management": [
            "Release coordination, deployment validation, and runbooks",
            "Dev/QA/UAT/Production readiness and post-release health checks",
        ],
        "monitoring": [
            "Monitoring dashboards, operational checks, and stability validation",
            "Grafana/Prometheus exposure through FRBNY dashboard collaboration",
        ],
        "documentation": [
            "Runbooks, technical support documentation, and release procedures",
            "Clear operating procedures for support and implementation teams",
        ],
        "stakeholder communication": [
            "Business-user, DevOps, QA, infrastructure, and management coordination",
            "Clear translation between technical issues and business impact",
        ],
        "operational readiness": [
            "Release readiness, validation checklists, and post-release support readiness",
            "Stability, efficiency, and effectiveness improvement mindset",
        ],
        "requirements analysis": [
            "Epics, user stories, acceptance criteria, and implementation-ready requirements",
            "Business analysis and stakeholder requirements elicitation",
        ],
        "uat": [
            "UAT planning, business validation, and signoff support",
            "Acceptance criteria and test evidence discipline",
        ],
        "agile": [
            "Agile collaboration with Product Owners, Scrum Masters, QA, and DevOps",
            "Jira story decomposition and acceptance criteria practices",
        ],
    }

    for term in terms:
        promote.extend(mapping.get(term, []))

    missing = gap.get("missing", {}) or {}
    for tool in missing.get("tools", []) or []:
        promote.append(f"Bridge {tool} gap honestly through adjacent enterprise application support and fast ramp-up")
    if "sre" in rc:
        promote.append("SRE-adjacent production support, monitoring, resiliency, and Linux troubleshooting")
    if "support" in rc:
        promote.append("Application support, production operations, incident triage, and risk-aware escalation")
    if "ba" in rc or "bsa" in rc or "analyst" in rc:
        promote.append("Requirements, UAT, workflow analysis, stakeholder communication, and documentation")
    return dedupe(promote)

def demote_from_terms(terms, role_code):
    rc = (role_code or "").lower()
    demote = [
        "Older CAD/CAM implementation details unless directly relevant",
        "Long historical employer detail that does not support the target JD",
    ]
    if "workday" not in terms and "hris platform" not in terms:
        demote.append("HRIS/Workday-specific language unless the JD requires it")
    if "gis" not in terms and "geospatial" not in terms:
        demote.append("GIS/geospatial language unless the JD requires it")
    if "market data" not in terms and "market data platform" not in terms:
        demote.append("Deep market-data terminology unless the JD is financial-data or trading focused")
    if "insurance" not in terms:
        demote.append("Detailed insurance workflow language unless domain fit is important")
    if "sre" not in rc:
        demote.append("Heavy SRE/Linux/networking detail unless the role is support/SRE-oriented")
    return dedupe(demote)

def story_recommendations(terms, story_mapping):
    stories = []
    for row in story_mapping or []:
        stories.append(row)
    defaults = [
        "FRBNY modernization: market data application migration, AWS/OPS360 distribution, REST API validation, Oracle comparison",
        "Deployment runbooks: release coordination, environment readiness, post-release health checks",
        "Application support: production troubleshooting, escalation, and stakeholder communication",
        "HP PPM / insurance systems: workflow analysis, UAT, reporting, and business process support",
    ]
    if any(t in terms for t in ["market data", "market data platform", "redline"]):
        stories.insert(0, "Use FRBNY market data modernization as the primary story")
    if any(t in terms for t in ["rest api", "oracle", "data validation"]):
        stories.insert(0, "Use REST API validation against Oracle as a technical validation story")
    if any(t in terms for t in ["production operations", "incident management", "release management"]):
        stories.insert(0, "Use deployment runbooks and production readiness as the operations story")
    return dedupe(stories + defaults)

def confidence_score(gap, intel_terms):
    score = int(gap.get("overall_match_score") or 0)
    if len(intel_terms) >= 8:
        score += 5
    elif len(intel_terms) <= 2:
        score -= 5
    return max(0, min(100, score))

def generate_one(gap_path: Path, intel_dir: Path, roles_dir: Path, resumes_dir: Path, output_dir: Path, run_id: str):
    slug = slug_from_filename(gap_path)
    gap = read_json_for_md(gap_path)
    intel_path = find_by_slug(intel_dir, "jd-intelligence-", slug, ".json")
    intel = json.loads(intel_path.read_text(encoding="utf-8")) if intel_path else {}
    role_path = find_by_slug(roles_dir, "role-", slug)
    resume_path = find_by_slug(resumes_dir, "resume-", slug)

    company = gap.get("company") or intel.get("company") or "unknown-company"
    title = gap.get("title") or intel.get("title") or slug
    role_code = gap.get("role_code") or intel.get("role_code") or ""

    terms = collect_intel_terms(intel)
    promote = promote_from_terms(terms, gap, role_code)
    demote = demote_from_terms(terms, role_code)
    story_map = story_recommendations(terms, intel.get("story_mapping", []) or [])
    confidence = confidence_score(gap, terms)

    output_dir.mkdir(parents=True, exist_ok=True)
    md_path = output_dir / f"resume-tailoring-{slug}.md"
    json_path = output_dir / f"resume-tailoring-{slug}.json"

    data = {
        "run_id": run_id,
        "company": company,
        "title": title,
        "role_code": role_code,
        "gap_file": str(gap_path),
        "jd_intelligence_file": str(intel_path or ""),
        "role_file": str(role_path or ""),
        "resume_file": str(resume_path or ""),
        "confidence_score": confidence,
        "promote": promote,
        "demote": demote,
        "story_recommendations": story_map,
        "jd_terms": terms,
    }

    md = f"""---
type: resume_tailoring
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
confidence_score: {confidence}
gap_file: {gap_path}
jd_intelligence_file: {intel_path or ""}
role_file: {role_path or ""}
resume_file: {resume_path or ""}
---

# Resume Tailoring — {company} — {title}

## Summary

- Company: **{company}**
- Role: **{title}**
- Role Code: **{role_code}**
- Tailoring Confidence: **{confidence}**

## JD Signals Used

{md_list(terms)}
## Promote These Themes

{md_list(promote)}
## De-Emphasize These Themes

{md_list(demote)}
## Resume Story Recommendations

{md_list(story_map)}
## Suggested Resume Strategy

### Opening Summary

Emphasize the strongest overlap between the JD and your background. Lead with enterprise application support, business analysis, production readiness, release coordination, UAT, data validation, and domain-specific experience when relevant.

### Most Recent Role

Prioritize FRBNY/Gresham bullets that match the JD intelligence signals. Use the strongest 8-10 bullets rather than trying to cover every responsibility.

### Older Experience

Compress older experience into sector or platform narratives unless the JD specifically asks for that domain.

## Notes

This v0.4.6 output is a deterministic tailoring recommendation report. It does not rewrite the resume directly yet. It prepares the logic that a future resume generator can consume.
"""
    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return md_path, json_path

def main(argv):
    if len(argv) < 3:
        print("Usage: generate_resume_tailoring.py <run_id> <gap_analysis_dir> [jd_intelligence_dir] [roles_dir] [resumes_dir]", file=sys.stderr)
        return 2
    run_id = argv[1]
    gap_dir = Path(argv[2])
    intel_dir = Path(argv[3]) if len(argv) > 3 else Path("data/jd-intelligence")
    roles_dir = Path(argv[4]) if len(argv) > 4 else Path("data/roles")
    resumes_dir = Path(argv[5]) if len(argv) > 5 else Path("data/resume-versions/teal-export")

    run_out = Path("ops/runs") / run_id / "output"
    data_out = Path("data/resume-tailoring")
    run_out.mkdir(parents=True, exist_ok=True)
    data_out.mkdir(parents=True, exist_ok=True)

    generated = []
    for gap_path in sorted(gap_dir.glob("gap-*.md")):
        md_path, json_path = generate_one(gap_path, intel_dir, roles_dir, resumes_dir, run_out, run_id)
        generated.append(md_path.name)
        for src in [md_path, json_path]:
            (data_out / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"generated resume tailoring: {gap_path.name} -> {md_path.name}")

    report = {"run_id": run_id, "count": len(generated), "generated": generated}
    for folder in [run_out, data_out]:
        (folder / f"resume-tailoring-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print("Done.")
    print(f"Run output: {run_out.resolve()}")
    print(f"Resume tailoring copied to: {data_out.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
