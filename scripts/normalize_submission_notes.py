#!/usr/bin/env python3

from pathlib import Path
import re
from datetime import date

ROOT = Path("data/application-packages")

STATUS_MAP = {
    "Applied": "APPLIED",
    "Submitted": "APPLIED",
    "Ready to Apply": "READY",
    "Draft / Not Submitted": "DRAFT",
    "Rejected": "REJECTED",
    "Position Closed": "POSITION_CLOSED",
    "Not Pursued": "NOT_PURSUED",
}

def extract_value(text, keys):
    for key in keys:
        m = re.search(rf"^{re.escape(key)}:\s*(.*)$", text, re.MULTILINE | re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""

def extract_list(text, heading_names):
    lines = text.splitlines()
    results = []
    capture = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("## "):
            capture = any(stripped.lower() == f"## {h.lower()}" for h in heading_names)
            continue

        if capture and stripped.startswith("- "):
            value = stripped[2:].strip()
            if value:
                results.append(value)

    return results

def normalize_status(value):
    if not value:
        return ""
    return STATUS_MAP.get(value, value.upper().replace(" ", "_"))

def infer_role_id(package_dir):
    return package_dir.name

def write_note(path):
    text = path.read_text(encoding="utf-8")
    package_dir = path.parent

    company = extract_value(text, ["company", "Company"])
    role = extract_value(text, ["role", "Role"])
    role_id = extract_value(text, ["role_id", "Role ID"]) or infer_role_id(package_dir)
    role_code = extract_value(text, ["role_code", "Role Code"])
    role_family = extract_value(text, ["role_family", "Role Family"])

    status = normalize_status(extract_value(text, ["status", "Status"]))
    date_applied = extract_value(text, ["date_applied", "Date Applied"])
    last_update = extract_value(text, ["last_update", "Last Update"]) or str(date.today())

    source = extract_value(text, ["source", "Source"])
    location = extract_value(text, ["location", "Location"])
    employment_type = extract_value(text, ["employment_type", "Employment Type"])

    resumes = extract_list(text, ["Resume", "Resumes"]) or ["ats-resume.html", "full-resume.html"]
    cover_letters = extract_list(text, ["Cover Letter", "Cover Letters"]) or ["none"]
    notes = extract_list(text, ["Notes"]) or [""]

    output = []
    output.append("# Submission Notes")
    output.append("")
    output.append("## Application")
    output.append("")
    output.append(f"company: {company}")
    output.append(f"role: {role}")
    output.append(f"role_id: {role_id}")
    output.append(f"role_code: {role_code}")
    output.append(f"role_family: {role_family}")
    output.append("")
    output.append("## Status")
    output.append("")
    output.append(f"status: {status}")
    output.append(f"date_applied: {date_applied}")
    output.append(f"last_update: {last_update}")
    output.append("")
    output.append("## Application Method")
    output.append("")
    output.append(f"source: {source}")
    output.append(f"location: {location}")
    output.append(f"employment_type: {employment_type}")
    output.append("")
    output.append("## Resumes")
    output.append("")
    output.append("resumes:")
    for item in resumes:
        output.append(f"- {item}")
    output.append("")
    output.append("## Cover Letters")
    output.append("")
    output.append("cover_letters:")
    for item in cover_letters:
        output.append(f"- {item}")
    output.append("")
    output.append("## Notes")
    output.append("")
    output.append("notes:")
    for item in notes:
        output.append(f"- {item}")
    output.append("")

    path.write_text("\n".join(output), encoding="utf-8")
    print(f"normalized: {path}")

def main():
    files = sorted(ROOT.glob("*/submission-notes.md"))
    if not files:
        raise SystemExit("No submission-notes.md files found.")

    for path in files:
        write_note(path)

if __name__ == "__main__":
    main()
