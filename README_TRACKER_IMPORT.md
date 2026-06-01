# Career System Tracker Import Foundation v0.3.6

This overlay adds the first Teal tracker roles CSV import pipeline.

## Scope

v0.3.6 imports only:

```text
jobtracker-roles-2026-06-01.csv
```

It intentionally ignores tracker events for now.

## Purpose

Teal tracker exports define the active job-search inventory.

The tracker role import creates normalized tracker-role Markdown records and links them to existing Career System role records when possible.

## Workflow

```text
Teal roles CSV
  -> data/tracker/imports/
  -> bin/run-tracker-role-import.sh
  -> data/tracker/normalized/
  -> data/tracker/reports/
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-tracker-import
mkdir -p /tmp/career-system-tracker-import

unzip ~/Downloads/career-system-v0.3.6-tracker-import-overlay.zip \
  -d /tmp/career-system-tracker-import

cp -R /tmp/career-system-tracker-import/* .

chmod +x bin/run-tracker-role-import.sh
chmod +x scripts/import_tracker_roles.py
```

## Run

```bash
./bin/run-tracker-role-import.sh \
  run-2026-06-01-tracker-role-import-v1 \
  data/tracker/imports/jobtracker-roles-2026-06-01.csv
```

## Review

```bash
tree data/tracker -L 3
head -80 data/tracker/normalized/*.md
cat data/tracker/reports/tracker-role-link-report-run-2026-06-01-tracker-role-import-v1.md
```

## Commit

```bash
git add README_TRACKER_IMPORT.md
git add bin/run-tracker-role-import.sh
git add scripts/import_tracker_roles.py
git add docs/standards/tracker-import-workflow.md
git add templates/tracker-role-template.md
git add data/tracker

git commit -m "Add tracker role import foundation v0.3.6"
git push
```

Do not add `ops/runs/` run artifacts.
