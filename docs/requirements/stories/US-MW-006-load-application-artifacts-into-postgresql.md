# US-MW-006 Load Application Artifacts into PostgreSQL

Status: Draft

## User Story

As a Motorweb Career Center user,
I want application artifact text loaded into PostgreSQL,
so that JDs, resumes, and notes can be queried through SQL and later exposed through REST APIs.

## Acceptance Criteria

- PostgreSQL schema supports application artifact detail records.
- Full artifact text is stored in `TEXT` columns.
- Artifacts are linked to `application_id`.
- Loader reads artifact paths from Career System tracker data.
- SQL queries can retrieve full JD text by application.
- SQL queries can retrieve final resume text by application.
- Missing artifacts are reported but do not break loading.

## Candidate Tables

- job_applications
- job_descriptions
- resumes
- application_notes

## Example Use Cases

- Query all applications where the JD mentions ACH.
- Retrieve final resume submitted for Broadridge.
- Compare normalized JD text to resume text.
