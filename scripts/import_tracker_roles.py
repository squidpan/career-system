#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

def slugify(text: str) -> str:
    text = (text or "").lower().strip()
    text = re.sub(r"&", " and ", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "unknown"

def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

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
        "id", "slug", "type", "title",
        "categories", "tags",
        "status", "version", "created", "last",
        "company", "company_slug",
        "source_system", "source_file", "source_url", "source_role_id",
        "origin", "run_id",
        "source_title", "normalized_title", "location", "tracker_source",
        "tracker_status", "tracker_scope", "active_in_tracker",
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
    lines.append("---")
    return "\n".join(lines) + "\n"

def registry_company_slug(company: str, repo_root: Path) -> str:
    registry = load_json(repo_root / "data" / "reference" / "company-registry.json")
    company_norm = (company or "").strip().lower()
    for code, item in registry.items():
        names = [item.get("company_name", ""), *item.get("company_aliases", [])]
        if any(company_norm == str(n).strip().lower() for n in names):
            return item.get("company_slug") or code
    return slugify(company)

def build_existing_role_index(repo_root: Path) -> dict[str, dict[str, Any]]:
    """
    Build a lookup by Teal UUID using existing data/roles/*.md.
    We match source_url containing the source_role_id UUID.
    """
    index: dict[str, dict[str, Any]] = {}
    for role_path in sorted((repo_root / "data" / "roles").glob("*.md")):
        text = role_path.read_text(encoding="utf-8")
        fm_text, _ = split_frontmatter(text)
        fm = parse_simple_yaml(fm_text)
        source_url = fm.get("source_url", "")
        m = re.search(r"/job-tracker/([a-f0-9-]{36})", source_url)
        if m:
            source_role_id = m.group(1)
            index[source_role_id] = {
                "role_id": fm.get("id", ""),
                "role_file": role_path.name,
                "jd_ids": fm.get("jd_ids", []),
            }
    return index

def clean_csv_value(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return "" if text.lower() == "nan" else text

def tracker_status(row: dict[str, Any]) -> str:
    return clean_csv_value(row.get("statusName")) or "unknown"

def active_from_archived(row: dict[str, Any]) -> bool:
    return clean_csv_value(row.get("archived_at")) == ""

def generate_tracker_role(row: dict[str, Any], csv_name: str, run_id: str, repo_root: Path, existing_index: dict[str, dict[str, Any]]) -> tuple[str, str, str]:
    source_role_id = clean_csv_value(row.get("id"))
    company = clean_csv_value(row.get("company_name"))
    title = clean_csv_value(row.get("role"))
    company_slug = registry_company_slug(company, repo_root)
    title_slug = slugify(title)
    year = (clean_csv_value(row.get("added_at")) or clean_csv_value(row.get("created_at")) or "2026")[:4]
    slug = f"{company_slug}-{title_slug}-{year}"
    tracker_id = f"tracker-role-{slug}"
    status = tracker_status(row)
    active = active_from_archived(row)
    existing = existing_index.get(source_role_id, {})
    existing_role_id = existing.get("role_id", "")
    existing_jd_ids = existing.get("jd_ids", [])
    match_status = "matched_role" if existing_role_id else "no_match"
    match_notes = f"Matched existing role {existing_role_id}" if existing_role_id else "No existing generated role matched this Teal source_role_id."

    data = {
        "id": tracker_id,
        "slug": slug,
        "type": "tracker_role",
        "title": f"{title} - {company}" if company else title,
        "categories": ["[[Careers]]", "[[Tracker]]", "[[Roles]]"],
        "tags": ["career", "tracker", "role"],
        "status": status,
        "version": "v1",
        "created": (clean_csv_value(row.get("created_at")) or clean_csv_value(row.get("added_at")))[:10],
        "last": (clean_csv_value(row.get("updated_at")) or clean_csv_value(row.get("created_at")) or clean_csv_value(row.get("added_at")))[:10],
        "company": company,
        "company_slug": company_slug,
        "source_system": "teal",
        "source_file": csv_name,
        "source_url": clean_csv_value(row.get("url")),
        "source_role_id": source_role_id,
        "origin": "import",
        "run_id": run_id,
        "source_title": title,
        "normalized_title": title,
        "location": clean_csv_value(row.get("location")),
        "tracker_source": clean_csv_value(row.get("source")),
        "tracker_status": status,
        "tracker_scope": "active" if active else "archived",
        "active_in_tracker": "true" if active else "false",
        "added_at": clean_csv_value(row.get("added_at")),
        "applied_at": clean_csv_value(row.get("applied_at")),
        "posted_at": clean_csv_value(row.get("posted_at")),
        "updated_at": clean_csv_value(row.get("updated_at")),
        "archived_at": clean_csv_value(row.get("archived_at")),
        "min_salary": clean_csv_value(row.get("min_salary")),
        "max_salary": clean_csv_value(row.get("max_salary")),
        "salary_currency": clean_csv_value(row.get("salary_currency")),
        "salary_pay_period": clean_csv_value(row.get("salary_pay_period")),
        "existing_role_id": existing_role_id,
        "existing_jd_ids": existing_jd_ids,
        "match_status": match_status,
        "match_notes": match_notes,
    }

    body = f"""# {data["title"]}

## Tracker Summary

- Company: {company}
- Title: {title}
- Tracker status: {status}
- Tracker scope: {data["tracker_scope"]}
- Source role ID: {source_role_id}
- Existing Career role match: {existing_role_id or "None"}

## Source

- Source system: Teal
- Source file: {csv_name}
- Source URL: {data["source_url"]}

## Linkage

- Existing role ID: {existing_role_id or "TBD"}
- Existing JD IDs: {", ".join(existing_jd_ids) if existing_jd_ids else "TBD"}

## Notes

{match_notes}
"""
    return tracker_id, render_frontmatter(data) + "\n" + body, match_status

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roles-csv", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--report-dir", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    csv_path = Path(args.roles_csv)
    output_dir = Path(args.output_dir)
    report_dir = Path(args.report_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    existing_index = build_existing_role_index(repo_root)

    rows: list[dict[str, Any]] = []
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    summary = {
        "run_id": args.run_id,
        "source_file": csv_path.name,
        "total_rows": len(rows),
        "matched_role": 0,
        "no_match": 0,
        "generated_files": [],
    }

    for row in rows:
        tracker_id, content, match_status = generate_tracker_role(row, csv_path.name, args.run_id, repo_root, existing_index)
        out_path = output_dir / f"{tracker_id}.md"
        out_path.write_text(content, encoding="utf-8")
        summary[match_status] = summary.get(match_status, 0) + 1
        summary["generated_files"].append(out_path.name)
        print(f"tracker role: {out_path.name} [{match_status}]")

    json_report = report_dir / f"tracker-role-link-report-{args.run_id}.json"
    json_report.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    md_report = report_dir / f"tracker-role-link-report-{args.run_id}.md"
    lines = [
        "---",
        f"id: tracker-role-link-report-{args.run_id}",
        "type: tracker_report",
        f"title: Tracker Role Link Report {args.run_id}",
        "categories:",
        "  - [[Careers]]",
        "  - [[Tracker]]",
        "tags:",
        "  - career",
        "  - tracker",
        "  - report",
        f"created: {args.run_id[4:14] if args.run_id.startswith('run-') else ''}",
        "---",
        "",
        f"# Tracker Role Link Report - {args.run_id}",
        "",
        f"- Source file: `{csv_path.name}`",
        f"- Total tracker roles: {summary['total_rows']}",
        f"- Matched existing roles: {summary['matched_role']}",
        f"- No match yet: {summary['no_match']}",
        "",
        "## Generated Files",
        "",
    ]
    for name in summary["generated_files"]:
        lines.append(f"- {name}")
    md_report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print()
    print(f"total_rows={summary['total_rows']}")
    print(f"matched_role={summary['matched_role']}")
    print(f"no_match={summary['no_match']}")
    print(f"report={md_report}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
