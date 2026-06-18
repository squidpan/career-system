# US-CS-050 Application Tracker CSV Generation

Status: Done

Implementation Status:
- applications.csv generated from submission-notes.md
- Status counts validated
- Required field validation completed

Completed: 2026-06-18

## Business Context

The application tracker CSV should be generated from application package metadata instead of manually edited.

## Acceptance Criteria

- applications.csv is generated from submission-notes.md.
- CSV includes one row per application package.
- Required fields are validated.
- Status counts are reliable.

## Validation

Run:

```bash
./bin/run-application-tracker-generator.sh
python3 - <<'PY'
import csv
from pathlib import Path
rows = list(csv.DictReader(Path("data/application-tracker/applications.csv").open()))
print(len(rows))
print(sorted(set(r["status"] for r in rows)))
PY
