#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

def split_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end].strip(), text[end + 4:].lstrip()
    return "", text

def parse_simple_yaml(frontmatter: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key = None
    for raw in frontmatter.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            if current_key not in data or data[current_key] == "":
                data[current_key] = []
            elif not isinstance(data[current_key], list):
                data[current_key] = [data[current_key]]
            data[current_key].append(line[4:].strip().strip('"'))
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
            current_key = key.strip()
    return data

def render_frontmatter(data: dict[str, Any]) -> str:
    order = [
        "id", "slug", "type", "title", "categories", "tags", "status", "version", "created", "last",
        "company", "company_slug", "source_system", "source_file", "source_url", "source_role_id",
        "origin", "run_id", "source_title", "normalized_title", "location", "tracker_source",
        "tracker_status", "tracker_scope", "active_in_tracker",
        "role_family", "role_level", "role_qualifiers", "role_code", "role_code_confidence",
        "recommended_resume_family", "recommended_resume_master_id", "recommended_resume_file",
        "classification_status", "classification_source",
        "added_at", "applied_at", "posted_at", "updated_at", "archived_at",
        "min_salary", "max_salary", "salary_currency", "salary_pay_period",
        "existing_role_id", "existing_jd_ids", "match_status", "match_notes"
    ]
    lines = ["---"]
    for key in order:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value if value is not None else ''}")
    for key, value in data.items():
        if key in order:
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value if value is not None else ''}")
    lines.append("---")
    return "\n".join(lines) + "\n"

def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

def contains(text: str, phrase: str) -> bool:
    return phrase.lower() in text.lower()

def classify(text: str) -> tuple[str, str, list[str], str, str]:
    t = f" {text.lower()} "
    if contains(t, "support operations systems lead"):
        return "support", "lead", ["ops"], "support-ops-lead", "high"
    if contains(t, "application and production support") or contains(t, "production support"):
        return "support", "", ["appsupport"], "support-appsupport", "high"
    if contains(t, "site reliability engineer"):
        return "sre", "", [], "sre", "high"
    if contains(t, "lead business systems analyst"):
        return "bsa", "lead", [], "bsa", "high"
    if contains(t, "business system analyst") or contains(t, "business systems analyst") or contains(t, "systems analyst"):
        level = "senior" if contains(t, "senior") or contains(t, "sr ") else ""
        return "bsa", level, [], "bsa", "medium"
    if contains(t, "business analyst") and (contains(t, "artificial intelligence") or contains(t, " ai") or contains(t, "ai ")):
        level = "senior" if contains(t, "senior") or contains(t, "sr ") else ""
        return "ba", level, ["ai"], "sba-ai" if level == "senior" else "ba-ai", "high"
    if contains(t, "business analyst"):
        level = "senior" if contains(t, "senior") or contains(t, "sr ") else ""
        quals = []
        if contains(t, "project manager") or contains(t, "program manager"):
            quals.append("pm")
        code = "sba" if level == "senior" else "ba"
        if "pm" in quals:
            code = "sba-pm" if level == "senior" else "ba-pm"
        return "ba", level, quals, code, "high"
    if contains(t, "infrastructure operations") or contains(t, "operations specialist") or contains(t, "operations analyst") or contains(t, "business operations"):
        level = "senior" if contains(t, "senior") or contains(t, "sr ") else ""
        return "ops", level, [], "ops", "medium"
    if contains(t, "support specialist") or contains(t, "operations & support"):
        return "support", "", ["appsupport"], "support-appsupport", "medium"
    return "", "", [], "unknown", "low"

def get_resume_mapping(role_code: str, repo_root: Path) -> dict[str, str]:
    ref_dir = repo_root / "data" / "reference"
    role_code_registry = load_json(ref_dir / "role-code-registry.json")
    resume_family_registry = load_json(ref_dir / "resume-family-registry.json")
    role_entry = role_code_registry.get(role_code, {})
    family = role_entry.get("recommended_resume_family", "")
    master_id = role_entry.get("recommended_resume_master_id", "")
    master_file = resume_family_registry.get(family, {}).get("master_resume_file", "") if family else ""
    return {"family": family, "master_id": master_id, "master_file": master_file}

def classify_file(path: Path, output_dir: Path, run_id: str, repo_root: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(text)
    fm = parse_simple_yaml(fm_text)
    evidence = "\n".join([fm.get("source_title", ""), fm.get("normalized_title", ""), fm.get("company", ""), fm.get("title", "")])
    family, level, qualifiers, code, confidence = classify(evidence)
    mapping = get_resume_mapping(code, repo_root)
    status = "classified" if code != "unknown" else "needs_review"
    fm.update({
        "run_id": run_id,
        "role_family": family,
        "role_level": level,
        "role_qualifiers": qualifiers,
        "role_code": code,
        "role_code_confidence": confidence,
        "recommended_resume_family": mapping["family"],
        "recommended_resume_master_id": mapping["master_id"],
        "recommended_resume_file": mapping["master_file"],
        "classification_status": status,
        "classification_source": "tracker_title_rules_v0.3.7",
    })
    out = output_dir / path.name
    out.write_text(render_frontmatter(fm) + "\n" + body, encoding="utf-8")
    return {"file": path.name, "role_code": code, "classification_status": status, "resume_master": mapping["master_id"]}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--report-dir", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    report_dir = Path(args.report_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for p in sorted(input_dir.glob("*.md")):
        r = classify_file(p, output_dir, args.run_id, repo_root)
        results.append(r)
        print(f"classified tracker role: {r['file']} -> {r['role_code']} [{r['classification_status']}]")
    classified = sum(1 for r in results if r["classification_status"] == "classified")
    needs_review = sum(1 for r in results if r["classification_status"] == "needs_review")
    report_md = report_dir / f"tracker-role-classification-report-{args.run_id}.md"
    lines = [
        "---",
        f"id: tracker-role-classification-report-{args.run_id}",
        "type: tracker_report",
        f"title: Tracker Role Classification Report {args.run_id}",
        "categories:",
        "  - [[Careers]]",
        "  - [[Tracker]]",
        "tags:",
        "  - career",
        "  - tracker",
        "  - classification",
        "---",
        "",
        f"# Tracker Role Classification Report - {args.run_id}",
        "",
        f"- Total tracker roles: {len(results)}",
        f"- Classified: {classified}",
        f"- Needs review: {needs_review}",
        "",
        "## Results",
        "",
        "| File | Role Code | Status | Resume Master |",
        "|---|---|---|---|",
    ]
    for r in results:
        lines.append(f"| {r['file']} | {r['role_code']} | {r['classification_status']} | {r['resume_master']} |")
    report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    report_json = report_dir / f"tracker-role-classification-report-{args.run_id}.json"
    report_json.write_text(json.dumps({"run_id": args.run_id, "total": len(results), "classified": classified, "needs_review": needs_review, "results": results}, indent=2), encoding="utf-8")
    print()
    print(f"total={len(results)}")
    print(f"classified={classified}")
    print(f"needs_review={needs_review}")
    print(f"report={report_md}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
