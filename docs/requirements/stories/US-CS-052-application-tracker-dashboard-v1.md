# US-CS-052 Application Tracker Dashboard v1

Status: Done

## User Story

As a Career System user,
I want a Markdown dashboard generated from `applications.csv`,
so that I can quickly review current application status in Obsidian without opening the CSV directly.

## Acceptance Criteria

- Dashboard is generated from `data/application-tracker/applications.csv`.
- Dashboard is written to `data/application-tracker/applications.md`.
- Dashboard includes total application count.
- Dashboard includes status summary counts.
- Dashboard includes an application table.
- Application table includes company, role, status, date applied, last update, role code, and source.
- Dashboard generator can be run from `bin/run-application-dashboard-generator.sh`.

## Implementation Notes

Implemented by:

- `scripts/generate_application_dashboard.py`
- `bin/run-application-dashboard-generator.sh`
- `data/application-tracker/applications.md`

## Validation

Validated with 11 application rows and status summary:

- APPLIED: 7
- POSITION_CLOSED: 2
- REJECTED: 1
- NOT_PURSUED: 1
