#!/usr/bin/env python3

import csv
from pathlib import Path

ROOT = Path("data/application-packages")
OUT = Path("data/application-tracker/applications.csv")

FIELDS = [
    "application_package_id",
    "company",
    "role",
    "role_id",
    "role_code",
    "role_family",
    "status",
    "date_applied",
    "last_update",
    "source",
    "location",
    "employment_type",
    "resumes",
    "cover_letters",
    "notes",
]

def parse_note(path: Path) -> dict:
    data = {field: "" for field in FIELDS}
    data["application_package_id"] = path.parent.name

    current_list = None
    lists = {"resumes": [], "cover_letters": [], "notes": []}

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        if not line or line.startswith("#"):
            continue

        if line in ("resumes:", "cover_letters:", "notes:"):
            current_list = line[:-1]
            continue

        if line.startswith("- ") and current_list:
            value = line[2:].strip()
            if value:
                lists[current_list].append(value)
            continue

        current_list = None

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in data:
                data[key] = value

    for key, values in lists.items():
        data[key] = "|".join(values)

    return data

def main():
    rows = []
    for note in sorted(ROOT.glob("*/submission-notes.md")):
        rows.append(parse_note(note))

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUT} with {len(rows)} rows")

if __name__ == "__main__":
    main()
