#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SKILL_TERMS = {
    "business analysis": ["business analysis", "business analyst", "requirements", "user stories", "acceptance criteria"],
    "workflow analysis": ["workflow", "process", "process mapping"],
    "uat": ["uat", "user acceptance", "testing", "qa"],
    "application support": ["application support", "production support", "support", "operations"],
    "release coordination": ["release", "deployment", "cutover", "production readiness"],
    "stakeholder management": ["stakeholder", "cross-functional", "business users"],
    "documentation": ["documentation", "runbook", "confluence", "procedures"],
    "data validation": ["data validation", "data quality", "reconciliation", "mapping"],
    "incident coordination": ["incident", "troubleshooting", "escalation"],
}

TOOL_TERMS = {
    "jira": ["jira"],
    "confluence": ["confluence"],
    "servicenow": ["servicenow", "service now"],
    "linux": ["linux", "unix"],
    "oracle": ["oracle"],
    "aws": ["aws", "amazon web services"],
    "openshift": ["openshift", "open shift"],
    "rest api": ["rest", "api", "rest api"],
    "json": ["json"],
    "swagger/openapi": ["swagger", "openapi", "open api"],
    "excel": ["excel", "pivot", "power query"],
    "workday": ["workday"],
    "pega": ["pega"],
    "salesforce": ["salesforce"],
    "sql": ["sql"],
    "python": ["python"],
    "gis": ["gis", "arcgis", "geospatial"],
    "kubernetes": ["kubernetes", "k8s"],
    "terraform": ["terraform"],
}

DOMAIN_TERMS = {
    "financial services": ["financial services", "bank", "banking", "fixed-income", "fixed income", "market data", "trading"],
    "insurance": ["insurance", "premium", "claims", "underwriting", "policy"],
    "healthcare": ["healthcare", "health care", "patient", "clinical", "medical"],
    "financial data": ["reference data", "pricing data", "security master", "golden copy", "ratings"],
    "enterprise applications": ["enterprise application", "enterprise systems", "business systems"],
    "manufacturing": ["manufacturing", "aerospace", "automotive", "cad", "cam"],
    "government": ["government", "federal", "public sector"],
}

ROLE_TERMS = {
    "business analyst": ["business analyst", "ba", "bsa", "requirements analyst"],
    "senior business analyst": ["senior business analyst", "lead business analyst", "sba"],
    "application support": ["application support", "production support", "support analyst"],
    "sre": ["site reliability", "sre", "production engineer"],
    "project manager": ["project manager", "program manager", "pm"],
    "systems analyst": ["systems analyst", "business systems analyst"],
}

EFFORT_HINTS = {
    "workday": "medium",
    "pega": "medium",
    "gis": "medium",
    "python": "low-medium",
    "sql": "low",
    "kubernetes": "high",
    "terraform": "high",
    "salesforce": "medium",
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

def analysis_text(doc: dict, is_jd: bool = False) -> str:
    """
    Return the text used for matching.

    For normalized JDs, ignore capture/tracker noise such as Teal job-list tables.
    This prevents unrelated tracker entries from creating false gaps, e.g.,
    Workday leaking from VNS into ICF or Michael Baker.
    """
    text = doc["text"]

    if not is_jd:
        return text

    body = doc.get("body", text)

    # Remove common capture-only sections.
    body = re.split(r"\n## Capture Metadata\b", body, maxsplit=1)[0]
    body = re.split(r"\n## Clipped Content\b", body, maxsplit=1)[0]

    # Fallback: if section stripping removed too much, keep frontmatter + title lines.
    if len(body.strip()) < 50:
        body = doc.get("body", text)

    return "\n".join([
        "\n".join(f"{k}: {v}" for k, v in doc.get("frontmatter", {}).items()),
        body,
    ])

def slug_from_filename(path: Path) -> str:
    name = path.stem
    for prefix in ["jd-", "role-", "resume-", "gap-"]:
        if name.startswith(prefix):
            name = name[len(prefix):]
    for suffix in ["-v1", "-assembled-v1", "-teal-v1"]:
        if name.endswith(suffix):
            name = name[:-len(suffix)]
    return name

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower())

def phrase_in_text(text: str, phrase: str) -> bool:
    """
    Match terms safely.

    Short tokens like GIS, SQL, AWS require word-boundary matching.
    This prevents false positives such as matching "gis" inside "General Dynamics".
    """
    t = norm(text)
    p = phrase.lower().strip()

    if not p:
        return False

    if len(p) <= 4 and p.replace("#", "").replace("+", "").isalnum():
        return re.search(rf"(?<![a-z0-9]){re.escape(p)}(?![a-z0-9])", t, flags=re.I) is not None

    return p in t

def find_terms(text: str, term_map: dict[str, list[str]]) -> list[str]:
    found = []
    for label, patterns in term_map.items():
        if any(phrase_in_text(text, p) for p in patterns):
            found.append(label)
    return sorted(set(found))

def score_category(required: list[str], present: list[str]):
    req = sorted(set(required))
    pres = sorted(set(present))
    if not req:
        return 100, [], []
    matched = [x for x in req if x in pres]
    missing = [x for x in req if x not in pres]
    return round((len(matched) / len(req)) * 100), matched, missing

def score_role_alignment(required: list[str], present: list[str], role_code: str):
    """
    Avoid penalizing unrelated role families.

    Example:
    Application-support roles should not show SRE as a gap unless SRE is the role family.
    """
    req = sorted(set(required))
    if not req:
        return 100, [], []

    role_code_l = (role_code or "").lower()
    filtered = []

    for r in req:
        if r == "sre" and "sre" not in role_code_l:
            continue
        if r == "systems analyst" and not any(x in role_code_l for x in ["bsa", "ba", "analyst", "systems"]):
            continue
        filtered.append(r)

    if not filtered:
        filtered = req

    return score_category(filtered, present)

def recommendation(score: int) -> str:
    if score >= 85:
        return "strong_apply"
    if score >= 70:
        return "apply"
    if score >= 55:
        return "stretch_apply"
    return "strategic_only"

def effort_level(missing_tools: list[str], missing_domains: list[str]) -> str:
    high = {"kubernetes", "terraform", "workday", "pega", "salesforce", "gis"}
    if any(x in high for x in missing_tools) and len(missing_tools) >= 3:
        return "high"
    if any(x in high for x in missing_tools) or len(missing_domains) >= 2:
        return "medium"
    if missing_tools or missing_domains:
        return "low-medium"
    return "low"

def refine_jd_domains(jd_text: str, domains: list[str]) -> list[str]:
    """
    Keep JD domain signals conservative.
    The JD itself must clearly express the domain.
    """
    t = norm(jd_text)
    refined = set(domains)

    if "healthcare" in refined and not any(x in t for x in ["healthcare", "health care", "clinical", "patient", "medical", "health system"]):
        refined.remove("healthcare")

    if "insurance" in refined and not any(x in t for x in ["insurance", "premium", "claims", "underwriting", "policy"]):
        refined.remove("insurance")

    if "government" in refined and not any(x in t for x in ["government", "federal", "public sector", "state agency", "municipal"]):
        refined.remove("government")

    return sorted(refined)

def load_resume(master_id: str, resume_master_dir: Path):
    if "sre" in master_id.lower():
        p = resume_master_dir / "master-sre-resume.md"
    else:
        p = resume_master_dir / "master-ba-resume.md"
    if not p.exists():
        raise FileNotFoundError(f"Missing resume master: {p}")
    return read_doc(p)

def find_role_for_jd(jd_path: Path, roles_dir: Path):
    jd_slug = slug_from_filename(jd_path)
    direct = roles_dir / f"role-{jd_slug}.md"
    if direct.exists():
        return direct
    jd_tokens = set(jd_slug.split("-"))
    best, best_score = None, 0
    for role in roles_dir.glob("*.md"):
        rtokens = set(slug_from_filename(role).split("-"))
        score = len(jd_tokens & rtokens)
        if score > best_score:
            best, best_score = role, score
    return best if best_score >= 2 else None

def md_list(items: list[str]) -> str:
    if not items:
        return "- None identified\n"
    return "".join(f"- {x}\n" for x in items)

def generate_one(jd_path: Path, roles_dir: Path, resume_master_dir: Path, output_dir: Path, run_id: str):
    jd = read_doc(jd_path)
    role_path = find_role_for_jd(jd_path, roles_dir)
    role = read_doc(role_path) if role_path else None

    master_id = "resume-master-ba-v1"
    if role:
        master_id = role["frontmatter"].get("recommended_resume_master_id") or role["frontmatter"].get("resume_master_id") or master_id
    resume = load_resume(master_id, resume_master_dir)

    jd_match_text = analysis_text(jd, is_jd=True)

    # Remove markdown table rows from JD matching text.
    # Teal tracker captures may include a "| Jobs |" navigation table
    # containing unrelated roles, which can create false gaps.
    jd_match_text = "\n".join(
        line for line in jd_match_text.splitlines()
        if not line.strip().startswith("|")
    )

    resume_match_text = analysis_text(resume, is_jd=False)

    jd_skills = find_terms(jd_match_text, SKILL_TERMS)
    jd_tools = find_terms(jd_match_text, TOOL_TERMS)
    jd_domains = refine_jd_domains(jd_match_text, find_terms(jd_match_text, DOMAIN_TERMS))
    jd_roles = find_terms(jd_match_text, ROLE_TERMS)

    resume_skills = find_terms(resume_match_text, SKILL_TERMS)
    resume_tools = find_terms(resume_match_text, TOOL_TERMS)
    resume_domains = find_terms(resume_match_text, DOMAIN_TERMS)
    resume_roles = find_terms(resume_match_text, ROLE_TERMS)

    company = jd["frontmatter"].get("company") or jd["frontmatter"].get("company_name") or "unknown-company"
    title = jd["frontmatter"].get("normalized_title") or jd["frontmatter"].get("title") or jd_path.stem
    role_code = jd["frontmatter"].get("role_code") or (role["frontmatter"].get("role_code") if role else "")

    skill_score, matched_skills, missing_skills = score_category(jd_skills, resume_skills)
    tool_score, matched_tools, missing_tools = score_category(jd_tools, resume_tools)
    domain_score, matched_domains, missing_domains = score_category(jd_domains, resume_domains)
    role_score, matched_roles, missing_roles = score_role_alignment(jd_roles, resume_roles, role_code)

    overall = round(skill_score * 0.4 + tool_score * 0.2 + domain_score * 0.2 + role_score * 0.2)
    effort = effort_level(missing_tools, missing_domains)
    learning = {x: EFFORT_HINTS.get(x, "low-medium") for x in missing_tools}
    for x in missing_domains:
        learning.setdefault(x, "low-medium")

    out_slug = slug_from_filename(jd_path)
    md_path = output_dir / f"gap-{out_slug}.md"
    json_path = output_dir / f"gap-{out_slug}.json"

    data = {
        "run_id": run_id,
        "company": company,
        "title": title,
        "role_code": role_code,
        "overall_match_score": overall,
        "recommendation": recommendation(overall),
        "effort_level": effort,
        "jd_file": str(jd_path),
        "role_file": str(role_path) if role_path else "",
        "resume_master_file": str(resume["path"]),
        "scores": {
            "skills": skill_score,
            "tools": tool_score,
            "domain": domain_score,
            "role_alignment": role_score,
        },
        "matched": {
            "skills": matched_skills,
            "tools": matched_tools,
            "domains": matched_domains,
            "roles": matched_roles,
        },
        "missing": {
            "skills": missing_skills,
            "tools": missing_tools,
            "domains": missing_domains,
            "roles": missing_roles,
        },
        "estimated_learning_effort": learning,
    }

    md = f"""---
type: gap_analysis
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
overall_match_score: {overall}
recommendation: {recommendation(overall)}
effort_level: {effort}
jd_file: {jd_path}
role_file: {role_path or ""}
resume_master_file: {resume["path"]}
---

# Gap Analysis — {company} — {title}

## Summary

- Overall Match Score: **{overall}**
- Recommendation: **{recommendation(overall)}**
- Effort Level: **{effort}**

## Category Scores

| Category | Score |
|---|---:|
| Skills | {skill_score} |
| Tools | {tool_score} |
| Domain | {domain_score} |
| Role Alignment | {role_score} |

## Strengths

### Matched Skills

{md_list(matched_skills)}
### Matched Tools

{md_list(matched_tools)}
### Matched Domains

{md_list(matched_domains)}
### Matched Role Signals

{md_list(matched_roles)}
## Gaps

### Missing Skills

{md_list(missing_skills)}
### Missing Tools

{md_list(missing_tools)}
### Missing Domains

{md_list(missing_domains)}
### Missing Role Signals

{md_list(missing_roles)}
## Estimated Learning Effort

{md_list([f"{k}: {v}" for k, v in learning.items()])}
## Resume Strategy

### Emphasize

{md_list((matched_skills + matched_tools + matched_domains)[:10])}
### De-emphasize

- Older engineering details unless directly relevant.
- Long tool lists that do not match the JD.
- Unrelated domain history.

## Notes

This v0.4.2 engine uses deterministic keyword matching. It is intentionally explainable and conservative.
"""
    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return {"md": str(md_path), "json": str(json_path), "score": overall, "recommendation": recommendation(overall)}

def main(argv):
    if len(argv) < 3:
        print("Usage: generate_gap_analysis.py <run_id> <normalized_jds_dir> [roles_dir] [resume_master_dir]", file=sys.stderr)
        return 2
    run_id = argv[1]
    jds_dir = Path(argv[2])
    roles_dir = Path(argv[3]) if len(argv) > 3 else Path("data/roles")
    resume_master_dir = Path(argv[4]) if len(argv) > 4 else Path("data/resume-masters")

    run_output = Path("ops/runs") / run_id / "output"
    data_output = Path("data/gap-analysis")
    run_output.mkdir(parents=True, exist_ok=True)
    data_output.mkdir(parents=True, exist_ok=True)

    results = []
    for jd_path in sorted(jds_dir.glob("*.md")):
        result = generate_one(jd_path, roles_dir, resume_master_dir, run_output, run_id)
        results.append(result)
        for key in ["md", "json"]:
            src = Path(result[key])
            dst = data_output / src.name
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"generated gap analysis: {jd_path.name} -> {Path(result['md']).name}")

    report = {"run_id": run_id, "count": len(results), "results": results}
    (run_output / f"gap-analysis-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (data_output / f"gap-analysis-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("Done.")
    print(f"Run output: {run_output.resolve()}")
    print(f"Gap analyses copied to: {data_output.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
