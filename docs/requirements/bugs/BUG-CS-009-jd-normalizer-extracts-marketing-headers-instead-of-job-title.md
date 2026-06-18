# BUG-CS-009 JD Normalizer Extracts Marketing Headers Instead Of Job Title

Status: Closed

Resolution:
- Rebuilt normalized titles from source_title metadata
- Corrected affected normalized JDs
- Validation completed

Closed: 2026-06-18


## Problem

Some normalized JD files have `title` and `normalized_title` populated from marketing copy or section headings instead of the actual job title.

Examples:

- `Your success is a train ride away!`
- `About The Team`
- `Role profile`
- `Location Designation`

## Expected Behavior

Normalized JD metadata should use clean role/company values.

Recommended rule:

- `title`: `<source_title> - <company>`
- `normalized_title`: `<source_title>`

## Acceptance Criteria

- `title` does not start with markdown formatting such as `**`.
- `normalized_title` does not start with markdown formatting such as `**`.
- `title` does not contain marketing headers.
- `normalized_title` does not contain marketing headers.
- For normalized JDs with `source_title`, title fields are rebuilt from source metadata.
- Validation script reports zero bad title metadata rows.

## Manual Validation

Run:

```bash
grep -R "^title: \*\*" data/jds/normalized || true
grep -R "^normalized_title: \*\*" data/jds/normalized || true
grep -R "Your success is a train ride away\|About The Team\|Role profile\|Location Designation" data/jds/normalized || true
