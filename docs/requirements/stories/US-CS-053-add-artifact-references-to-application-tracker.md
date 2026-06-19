# US-CS-053 Add Artifact References to Application Tracker

Status: Done

## User Story

As a Career System user,
I want `applications.csv` to include references to key application artifacts,
so that each application row can be connected to its normalized JD, raw JD, final resume, and application package.

## Proposed Fields

- normalized_jd_file
- raw_jd_file
- final_resume_file
- application_package_path

## Acceptance Criteria

- `applications.csv` includes artifact reference columns.
- Existing 11 application rows remain valid.
- Artifact references are stored as file paths.
- Missing artifacts are allowed to be blank.
- Existing tracker generation continues to work.
- Dashboard generation continues to work.

## Implementation Notes

References should be lightweight paths, not full text.

Full artifact text will be loaded later into PostgreSQL detail tables.
