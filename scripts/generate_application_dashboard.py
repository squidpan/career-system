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
    lines.append("| Company | Role | Status | Date Applied | Last Update | Role Code | Source |")
    lines.append("|---|---|---|---|---|---|---|")

    for r in rows:
        lines.append(
            "| "
            + " | ".join(clean(r.get(c, "")) for c in COLUMNS)
            + " |"
        )

    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH} with {len(rows)} rows")

if __name__ == "__main__":
    main()
