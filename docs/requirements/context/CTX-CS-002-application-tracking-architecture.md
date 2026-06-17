# CTX-CS-002 Application Tracking Architecture

## Status

Draft

## Key Decisions

- `submission-notes.md` is the Application Event Record.
- Normalized JD is the Job Metadata Record.
- `applications.csv` is a generated rollup, not manually edited.
- Human-readable `role` remains in submission notes.
- `role_code` and `role_family` are optional until normalized JD metadata is reliable.
- Field names use `snake_case`.
- List fields use plural names such as `resumes` and `cover_letters`.

## Required submission-notes fields

- company
- role
- status
- date_applied
- last_update
- resumes

## Optional submission-notes fields

- role_id
- role_code
- role_family
- source
- location
- employment_type
- cover_letters
- notes

## Data Flow

```text
normalized JD metadata
        +
submission-notes.md
        ↓
applications.csv
        ↓
PostgreSQL
        ↓
Motorweb Dashboard / REST API
