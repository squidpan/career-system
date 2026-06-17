# Career System v0.4 Design Discussion

## Submission Notes, Application Tracker, and Role Metadata

**Date:** 2026-06-17

---

# Background

While implementing Sprint 1 application tracking improvements, a design review was performed on:

* submission-notes.md
* applications.csv
* application status lifecycle
* future PostgreSQL schema
* future Motorweb Career Center API model

The goal was to ensure that Career System operational data can later be loaded into PostgreSQL and exposed through REST APIs without redesign.

---

# Key Decisions

## Decision 1 - submission-notes.md is the Application Event Record

submission-notes.md represents the actual application event.

Examples:

* applied
* rejected
* withdrawn
* position closed
* not pursued

It is the authoritative source for application status.

Examples:

```text
Status: APPLIED
Date Applied: 2026-06-15
```

---

## Decision 2 - Normalized JD is the Job Metadata Record

Normalized JD files are the authoritative source for job metadata.

Examples:

```text
role_id
role_code
role_family
role_level
role_qualifiers
source
location
employment_type
```

These fields should ultimately be generated and maintained by the JD normalization pipeline.

---

## Decision 3 - applications.csv is a Generated Rollup Dataset

applications.csv should eventually be generated from:

* submission-notes.md
* normalized JD metadata

Conceptually:

```text
submission-notes.md
        +
normalized JD
        ↓
applications.csv
        ↓
PostgreSQL
        ↓
Motorweb Dashboard
        ↓
REST APIs
```

applications.csv should not become an independent source of truth.

---

## Decision 4 - Human Readable Role Name Remains

Field:

```text
role
```

should remain human-readable.

Example:

```text
Senior Business Analyst – Product Development, TradeAgent
```

Reason:

* matches LinkedIn/company posting
* easier to review manually
* useful in tracker reports

---

## Decision 5 - role_code Is Valuable But Not Yet Mandatory

Examples:

```text
ba
bsa
sba
sre
ops
appsupport
pm
```

Role classification is useful for:

* dashboard filtering
* reporting
* SQL queries
* analytics

However:

Current normalized JD generation does not reliably populate role_code.

Therefore:

role_code should remain optional until normalization quality improves.

---

# Proposed Submission Notes Standard

## Required Fields

```text
company
role
status
date_applied
last_update
resumes
```

---

## Optional Fields

```text
role_id
role_code
role_family
source
location
employment_type
cover_letters
notes
```

---

## Proposed Structure

```yaml
company:
role:
role_id:
role_code:
role_family:

status:
date_applied:
last_update:

source:
location:
employment_type:

resumes:
- ats-resume.html
- full-resume.html

cover_letters:
- none

notes:
```

---

# Future CSV Columns

Potential future application tracker columns:

```text
application_id
company
role
role_id
role_code
role_family
status
date_applied
last_update
source
location
employment_type
```

---

# Motorweb Impact

These decisions directly affect:

* PostgreSQL table design
* CSV import process
* JSON payload structures
* dashboard filtering
* REST API schemas

The PostgreSQL POC should align with this model whenever possible.

---

# Recommended Requirements Follow-Up

Create or update stories covering:

1. Submission Notes Metadata Standard
2. Application Tracker CSV Generation
3. Role Metadata Propagation from Normalized JD
4. Optional Role Classification Fields
5. CSV Generation from Source Artifacts
6. PostgreSQL Schema Alignment
7. JSON Payload Alignment
8. Application Status Single Source of Truth

These stories should be traceable to Motorweb PostgreSQL POC requirements.

# Notes to Requirements chat what to do
And yes, I would take this to the Requirements chat next and ask it to:

Review existing BUG-CS-004, BUG-CS-005, US-CS-042, US-CS-043.
Determine which are already covered.
Create any missing stories around:
JD metadata propagation
CSV generation
submission-notes schema
Postgres alignment
JSON payload alignment
Update the RTM if needed.

That keeps the design decision captured before we start Sprint 2 and before we build the PostgreSQL loader.