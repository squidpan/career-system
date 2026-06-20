# US-MW-006B Load Application Artifacts into PostgreSQL

Status: Done

## User Story

As a Motorweb Career Center user,
I want full application artifact text loaded into PostgreSQL,
so that job descriptions, resumes, and submission notes can be queried through SQL and later exposed through REST APIs.

## Background

US-MW-006A created the local PostgreSQL foundation:

- Database: `career_center`
- Role: `career_app`
- Schema: `career`

The first loader populated:

- `career.job_application`

from:

- `data/application-tracker/applications.csv`

This story extends the loader workflow to populate related artifact detail tables.

## Source Data

Artifact references come from:

- `data/application-tracker/applications.csv`

Relevant fields:

- `normalized_jd_file`
- `raw_jd_file`
- `final_resume_file`
- `application_package_path`

Additional file:

- `submission-notes.md` inside each application package

## Target Tables

### `career.job_description`

Stores:

- normalized JD text
- raw JD text

Expected rows:

- 11 normalized JD rows
- 11 raw JD rows

### `career.application_artifact`

Stores:

- final resume text where available
- submission notes text

Expected rows:

- 11 submission notes rows
- resume rows where final resumes exist

## Acceptance Criteria

- Loader reads `applications.csv`.
- Loader reads normalized JD file content.
- Loader reads raw JD file content.
- Loader reads final resume content where available.
- Loader reads submission notes from `application_package_path`.
- Loader inserts normalized and raw JD content into `career.job_description`.
- Loader inserts resume and submission-note content into `career.application_artifact`.
- Missing resume files are allowed and reported.
- Loader can be rerun safely.
- Validation query confirms 22 rows in `career.job_description`.
- Validation query confirms submission notes loaded for all 11 applications.
- SQL can retrieve full JD text by `application_id`.
- SQL can retrieve resume text by `application_id` where available.

## Out of Scope

- Parsing HTML resumes
- Cleaning resume text
- Full-text search indexing
- REST API endpoints
- React dashboard
- Production secrets management

## Validation SQL

```sql
select jd_type, count(*)
from career.job_description
group by jd_type
order by jd_type;

select artifact_type, count(*)
from career.application_artifact
group by artifact_type
order by artifact_type;

select a.company, a.role, jd.jd_type, length(jd.content_text) as content_length
from career.job_application a
join career.job_description jd
  on jd.application_id = a.application_id
order by a.company, jd.jd_type;
