# US-CS-054 Application Artifact Metadata Propagation

Status: Done

## User Story

As a Career System user,
I want artifact references to be populated automatically,
so that tracker rows do not require manual updates when application packages are created or refreshed.

## Acceptance Criteria

- Artifact references are derived from application package structure and/or package manifest.
- `normalized_jd_file` is populated where a normalized JD exists.
- `raw_jd_file` is populated where a raw JD exists.
- `final_resume_file` is populated where a final resume exists.
- `application_package_path` is populated for every tracked application.
- Missing artifact references are reported but do not fail generation.

## Implementation Notes

Prefer deterministic mapping over fuzzy matching.

Current source candidates:

- `package-manifest.json`
- `submission-notes.md`
- normalized JD metadata
- application package folder naming
