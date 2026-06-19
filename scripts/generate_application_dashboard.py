#!/usr/bin/env python3

import csv
from pathlib import Path

CSV_PATH = Path("data/application-tracker/applications.csv")
OUT_PATH = Path("data/application-tracker/applications.md")

COLUMNS = [
    "company",
    "role",
    "status",
    "date_applied",
    "last_update",
    "role_code",
    "source",
]


def clean(value: str) -> str:
    return (value or "").replace("|", "\\|").strip()


def md_link(path_value: str, label: str) -> str:
    path_value = (path_value or "").strip()
    if not path_value:
        return ""

    path = Path(path_value)
    display = label

    # Markdown link works in GitHub, VS Code, and Obsidian.
    return f"[{display}]({path_value})"


def main():
    rows = list(csv.DictReader(CSV_PATH.open(newline="", encoding="utf-8")))

    rows.sort(key=lambda r: (r.get("last_update", ""), r.get("company", "")), reverse=True)

    lines = []
    lines.append("# Application Tracker Dashboard")
    lines.append("")
    lines.append(f"Generated from `{CSV_PATH}`.")
    lines.append("")
    lines.append(f"Total applications: {len(rows)}")
    lines.append("")

    counts = {}
    for r in rows:
        status = r.get("status", "").strip() or "UNKNOWN"
        counts[status] = counts.get(status, 0) + 1

    lines.append("## Status Summary")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for status, count in sorted(counts.items()):
        lines.append(f"| {clean(status)} | {count} |")
    lines.append("")

    lines.append("## Applications")
    lines.append("")
    lines.append(
        "| Company | Role | Status | Date Applied | Last Update | Role Code | Source | Normalized JD | Raw JD | Resume | Package |"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|")

    for r in rows:
        base_values = [clean(r.get(c, "")) for c in COLUMNS]

        artifact_values = [
            md_link(r.get("normalized_jd_file", ""), "Normalized JD"),
            md_link(r.get("raw_jd_file", ""), "Raw JD"),
            md_link(r.get("final_resume_file", ""), "Resume"),
            md_link(r.get("application_package_path", ""), "Package"),
        ]

        lines.append("| " + " | ".join(base_values + artifact_values) + " |")

    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH} with {len(rows)} rows")


if __name__ == "__main__":
    main()
