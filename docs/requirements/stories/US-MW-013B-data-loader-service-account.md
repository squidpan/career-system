# US-MW-013B Data Loader Service Account

Status: Proposed

## User Story

As a platform administrator,
I want Career System data loading processes to run under a dedicated service account,
so that imports from CSV, JD files, resume artifacts, and application packages are separated from human user accounts.

## Business Context

Career System currently uses local scripts and human users to prepare and load data.

As the platform matures, data loading should become a repeatable machine process that can be run during deployment, QA validation, or scheduled operational refreshes.

A dedicated service account such as `career-loader` separates data ingestion responsibility from API runtime responsibility.

## Scope

Define future standards for:

- `career-loader` Linux service account
- PostgreSQL loader permissions
- CSV import ownership
- JD import ownership
- resume artifact import ownership
- application package registration
- logging and audit output
- manual versus scheduled execution

## Out of Scope

- Creating the `career-loader` account now
- Implementing a scheduler now
- Rewriting loader scripts now
- Production data governance now

## Acceptance Criteria

- Dedicated loader service account is identified.
- Loader responsibility is separated from API runtime responsibility.
- PostgreSQL loader role responsibilities are documented.
- Future scheduling model is documented.
- Relationship to Career System operational data flows is documented.

## Future Target Model

```text
pl
    builds loader scripts and data model

ted
    validates tagged loader behavior

career-loader
    executes approved data loading workflows

career_app
    application database role

career_loader
    future PostgreSQL role with controlled write permissions
```

## Candidate Data Flows

```text
Tracker CSV
    ↓
career-loader
    ↓
PostgreSQL

Raw JD files
    ↓
normalization
    ↓
career-loader
    ↓
PostgreSQL

Application artifacts
    ↓
career-loader
    ↓
PostgreSQL metadata
```

## Notes

This story prepares Career System for repeatable data ingestion without implementing scheduling or service-account execution immediately.
