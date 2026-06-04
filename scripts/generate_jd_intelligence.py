#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

INTELLIGENCE_TERMS = {
    "tools": {
        "linux": ["linux", "unix"],
        "python": ["python"],
        "sql": ["sql"],
        "oracle": ["oracle"],
        "aws": ["aws", "amazon web services"],
        "openshift": ["openshift", "open shift"],
        "kubernetes": ["kubernetes", "k8s"],
        "docker": ["docker"],
        "grafana": ["grafana"],
        "prometheus": ["prometheus"],
        "servicenow": ["servicenow", "service now"],
        "jira": ["jira"],
        "confluence": ["confluence"],
        "workday": ["workday"],
        "pega": ["pega"],
        "salesforce": ["salesforce"],
        "gis": ["gis", "arcgis", "geospatial"],
        "excel": ["excel", "power query", "pivot"],
        "rest api": ["rest api", "rest", "api"],
        "json": ["json"],
        "swagger/openapi": ["swagger", "openapi", "open api"],
    },
    "platforms": {
        "enterprise applications": ["enterprise applications", "enterprise systems", "business systems"],
        "market data platform": ["market data", "ticker plant", "feed", "feeds"],
        "financial data platform": ["reference data", "pricing data", "security master", "golden copy"],
        "cloud platform": ["cloud", "aws", "microservices"],
        "hris platform": ["hris", "workday", "human resources"],
        "gis platform": ["gis", "arcgis", "geospatial"],
        "service management platform": ["servicenow", "incident", "ticket"],
    },
    "products": {
        "redline": ["redline"],
        "inrush": ["inrush"],
        "b-pipe": ["b-pipe", "bpipe", "b pipe"],
        "bloomberg": ["bloomberg"],
        "workday": ["workday"],
        "hp ppm": ["hp ppm", "project and portfolio management"],
        "asset control/acplus": ["asset control", "acplus", "ac plus"],
        "ops360": ["ops360", "ops 360"],
        "pega": ["pega"],
        "salesforce": ["salesforce"],
    },
    "domains": {
        "financial services": ["financial services", "banking", "bank", "trading", "fixed income", "fixed-income"],
        "market data": ["market data", "ticker plant", "feed handler", "feed", "feeds", "latency"],
        "insurance": ["insurance", "premium", "policy", "claims", "underwriting"],
        "healthcare": ["healthcare", "health care", "patient", "clinical", "medical"],
        "government": ["government", "federal", "public sector", "municipal", "state agency"],
        "geospatial": ["gis", "arcgis", "geospatial", "mapping", "map"],
        "enterprise application support": ["application support", "production support", "enterprise applications"],
    },
    "methodologies": {
        "agile": ["agile", "scrum", "sprint"],
        "requirements analysis": ["requirements", "user stories", "acceptance criteria"],
        "uat": ["uat", "user acceptance testing"],
        "incident management": ["incident", "troubleshooting", "root cause"],
        "release management": ["release", "deployment", "cutover"],
        "monitoring": ["monitoring", "alert", "grafana", "prometheus"],
        "data validation": ["data validation", "data quality", "reconciliation"],
    },
}

QUESTION_RULES = {
    "market data": [
        "How would you troubleshoot delayed or missing market data?",
        "How would you validate feed integrity after a deployment?",
        "What signals would tell you a market data issue is source-side versus application-side?",
    ],
    "redline": [
        "What do you understand about Redline or low-latency market data platforms?",
        "How would you approach supporting a vendor platform you are still learning?",
    ],
    "inrush": [
        "How would you investigate an issue in a ticker plant or feed-processing component?",
    ],
    "grafana": [
        "What Grafana dashboards or metrics would you review first during an incident?",
    ],
    "prometheus": [
        "How would Prometheus metrics help you confirm application health?",
    ],
    "workday": [
        "How would you support Workday workflows or integrations without being the primary Workday administrator?",
        "How would you gather requirements for an enterprise HRIS workflow?",
    ],
    "gis": [
        "How would you gather requirements for a GIS or geospatial application?",
        "How would you validate map-based or geospatial outputs with business users?",
    ],
    "pega": [
        "How would you approach requirements and testing for a Pega-based workflow application?",
    ],
    "servicenow": [
        "How do you use ServiceNow or ticket data to manage operational work and stakeholder communication?",
    ],
    "rest api": [
        "How would you validate REST API output against a source system?",
    ],
    "oracle": [
        "How would you compare application output against Oracle data?",
    ],
}

STORY_MAPPING = {
    "market data": "FRBNY market data modernization and streaming financial data support",
    "financial services": "FRBNY fixed-income pricing and financial application support",
    "rest api": "REST API validation against Oracle/legacy data sources",
    "oracle": "REST API validation against Oracle/legacy data sources",
    "release management": "Deployment runbooks, release validation, and health checks",
    "incident management": "Production support, log review, validation, and cross-team escalation",
    "workday": "Bridge from enterprise application support, workflow analysis, UAT, and rapid platform ramp-up",
    "gis": "Bridge from requirements analysis, data validation, and stakeholder-driven UAT",
    "pega": "Bridge from HP PPM workflow analysis, insurance systems, and enterprise application modernization",
}

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
    for prefix in ["jd-", "role-", "gap-", "interview-prep-", "jd-intelligence-"]:
        if name.startswith(prefix):
            name = name[len(prefix):]
    for suffix in ["-v1"]:
        if name.endswith(suffix):
            name = name[:-len(suffix)]
    return name

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower())

def phrase_in_text(text: str, phrase: str) -> bool:
    t = norm(text)
    p = phrase.lower().strip()
    if not p:
        return False
    if len(p) <= 4 and p.replace("#", "").replace("+", "").isalnum():
        return re.search(rf"(?<![a-z0-9]){re.escape(p)}(?![a-z0-9])", t, flags=re.I) is not None
    return p in t

def analysis_text(doc: dict) -> str:
    """
    Return JD text for intelligence extraction.

    Keep the actual JD body, but remove tracker/navigation table rows
    such as Teal's "| Jobs |" table. Do NOT truncate at
    "## Capture Metadata" or "## Clipped Content" because the real
    job description often appears after those headings.
    """
    body = doc.get("body", doc.get("text", ""))

    filtered_lines = []
    for line in body.splitlines():
        stripped = line.strip()

        # Remove Teal tracker/navigation markdown tables.
        if stripped.startswith("|"):
            continue

        # Remove obvious webclipper navigation noise.
        if stripped.startswith("**Guidance**"):
            continue

        filtered_lines.append(line)

    return "\n".join([
        "\n".join(f"{k}: {v}" for k, v in doc.get("frontmatter", {}).items()),
        "\n".join(filtered_lines),
    ])

def extract_terms(text: str):
    result = {}
    for category, terms in INTELLIGENCE_TERMS.items():
        found = []
        for label, patterns in terms.items():
            if any(phrase_in_text(text, pattern) for pattern in patterns):
                found.append(label)
        result[category] = sorted(set(found))
    return result

def derive_questions(intel: dict):
    keys = []
    for category in ["tools", "products", "domains", "methodologies"]:
        keys.extend(intel.get(category, []))
    questions = []
    for key in keys:
        questions.extend(QUESTION_RULES.get(key, []))
    # baseline if sparse
    if not questions:
        questions = [
            "What are the most important systems or workflows this role supports?",
            "What would you do in the first 30 days to understand the platform?",
            "How would you validate requirements and confirm business readiness?",
        ]
    seen, out = set(), []
    for q in questions:
        if q not in seen:
            seen.add(q)
            out.append(q)
    return out

def derive_story_map(intel: dict):
    keys = []
    for category in ["tools", "products", "domains", "methodologies"]:
        keys.extend(intel.get(category, []))
    stories = []
    for key in keys:
        story = STORY_MAPPING.get(key)
        if story:
            stories.append(f"{key}: {story}")
    return sorted(set(stories)) or ["Use FRBNY modernization, REST API validation, runbooks, UAT, and enterprise application support stories."]

def md_list(items):
    if not items:
        return "- None identified\n"
    return "".join(f"- {x}\n" for x in items)

def generate_one(jd_path: Path, output_dir: Path, run_id: str):
    doc = read_doc(jd_path)
    text = analysis_text(doc)
    intel = extract_terms(text)
    questions = derive_questions(intel)
    story_map = derive_story_map(intel)

    fm = doc["frontmatter"]
    company = fm.get("company") or fm.get("company_name") or "unknown-company"
    title = fm.get("normalized_title") or fm.get("title") or jd_path.stem
    role_code = fm.get("role_code", "")
    slug = slug_from_filename(jd_path)

    data = {
        "run_id": run_id,
        "company": company,
        "title": title,
        "role_code": role_code,
        "source_file": str(jd_path),
        "intelligence": intel,
        "jd_aware_questions": questions,
        "story_mapping": story_map,
    }

    json_path = output_dir / f"jd-intelligence-{slug}.json"
    md_path = output_dir / f"jd-intelligence-{slug}.md"

    md = f"""---
type: jd_intelligence
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
source_file: {jd_path}
---

# JD Intelligence — {company} — {title}

## Extracted Tools

{md_list(intel.get("tools", []))}
## Extracted Platforms

{md_list(intel.get("platforms", []))}
## Extracted Products

{md_list(intel.get("products", []))}
## Extracted Domains

{md_list(intel.get("domains", []))}
## Extracted Methodologies

{md_list(intel.get("methodologies", []))}
## JD-Aware Interview Questions

{md_list(questions)}
## Resume Story Mapping

{md_list(story_map)}
## Notes

This v0.4.4 intelligence layer is deterministic. It extracts JD-specific signals for downstream use by interview prep, skills generation, resume tailoring, and application packages.
"""
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(md, encoding="utf-8")
    return md_path, json_path

def main(argv):
    if len(argv) < 3:
        print("Usage: generate_jd_intelligence.py <run_id> <normalized_jds_dir>", file=sys.stderr)
        return 2

    run_id = argv[1]
    jds_dir = Path(argv[2])
    run_output = Path("ops/runs") / run_id / "output"
    data_output = Path("data/jd-intelligence")
    run_output.mkdir(parents=True, exist_ok=True)
    data_output.mkdir(parents=True, exist_ok=True)

    generated = []
    for jd_path in sorted(jds_dir.glob("*.md")):
        md_path, json_path = generate_one(jd_path, run_output, run_id)
        generated.append(md_path.name)
        for src in [md_path, json_path]:
            (data_output / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"generated jd intelligence: {jd_path.name} -> {md_path.name}")

    report = {"run_id": run_id, "count": len(generated), "generated": generated}
    for folder in [run_output, data_output]:
        (folder / f"jd-intelligence-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print("Done.")
    print(f"Run output: {run_output.resolve()}")
    print(f"JD intelligence copied to: {data_output.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
