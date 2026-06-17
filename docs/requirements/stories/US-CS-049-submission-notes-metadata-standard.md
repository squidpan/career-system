# US-CS-049 Submission Notes Metadata Standard

Status: Implemented

## Business Context

Application package submission notes need to be both human-readable and machine-readable.

## Acceptance Criteria

- Fields use snake_case.
- List fields use plural names.
- Required and optional fields are documented.
- Existing submission notes can be normalized by script.

## Validation

Run:

```bash
./bin/run-submission-notes-normalization.sh
grep -R "^status:" data/application-packages/*/submission-notes.md
