# Career System

Career System is a personal job-search operating system for managing job opportunities, job descriptions, resumes, cover letters, thank-you letters, interview notes, tracker events, and reusable career knowledge.

The immediate purpose is practical: help ME apply to jobs faster, keep each application organized, and turn every job description into better resumes, better interview preparation, and better Obsidian notes.

The long-term purpose is architectural: start with simple Markdown, JSON, CSV, and file folders, then evolve toward the Motorweb Job Application Platform with PostgreSQL, FastAPI CRUD services, REST APIs, and eventually a web UI.

---

## Current Version

```text
Career System v0.12.0

Current Focus:
Operational Hardening and Career Center Foundation

Latest Release:
v0.11.1-deployment-prep

Current Major Capabilities:

- Resume System
- Application Package Generation
- JD Normalization
- Requirements Framework
- PostgreSQL Career Center
- FastAPI Career Center
- Deployment Automation
- Smoke Testing
- Release Management
```

Current release stream focuses on:

```text
- Operational hardening
- PostgreSQL deployment automation
- FastAPI deployment automation
- Startup validation
- Smoke testing
- Release management
- Multi-user deployment validation
```

---

## Why This Project Exists

The job search creates a lot of scattered artifacts:

```text
Job descriptions
Resume PDFs
Resume exports from Teal
Cover letters
Recruiter messages
Interview notes
Thank-you letters
Follow-up emails
Skills notes
Application status notes
```

Without a system, each new application becomes a one-off effort.

Career System turns that into a repeatable workflow:

```text
Job Description
    ↓
Role Record
    ↓
Skill / Requirement Analysis
    ↓
Tailored Resume
    ↓
Cover Letter
    ↓
Application Tracker Event
    ↓
Interview Prep
    ↓
Thank-You / Follow-Up
    ↓
Reusable Career Knowledge
```

---

## Core Intent

Career System is designed to support four goals:

1. Apply to jobs faster.
2. Keep every job opportunity organized.
3. Build reusable master resumes instead of rewriting from scratch.
4. Feed Obsidian and future Motorweb development with clean, structured data.

---

## Strategic Positioning

The current resume strategy recognizes two major career tracks:

```text
Master BA Resume
    Senior Business Analyst
    Business Systems Analyst
    Application Support BA
    Enterprise Delivery BA
    Insurance / Financial Systems BA

Master SRE Resume
    Site Reliability Engineer
    Application Support Engineer
    Production Support Analyst
    Market Data Support
    Technical Operations Support
```

Most immediate opportunities will likely derive from the Master BA Resume, especially hybrid roles that combine:

```text
Business Analysis
Application Support
Release Coordination
Production Operations
QA / UAT
Runbooks
ServiceNow
Jira / Confluence
Linux / Oracle / AWS familiarity
```

---

## Current Platform Capabilities

Career System now provides:

* Resume system
* Application package generation
* JD normalization
* Application tracker generation
* Requirements and story management
* Sprint planning and closeout tracking
* PostgreSQL Career Center database
* FastAPI Career Center API
* OpenAPI contracts
* Deployment automation
* Smoke testing
* Release tagging and release notes

---

## Career Center PostgreSQL

Career Center includes a local PostgreSQL deployment.

Primary objects:

* Database: `career_center`
* Role: `career_app`
* Schema: `career`

Core tables:

* `career.job_application`
* `career.job_description`
* `career.application_artifact`

Deployment:

```bash
./bin/setup-career-center-postgres.sh
```

Data loading:

```bash
./bin/load-applications-to-postgres.sh
./bin/load-application-artifacts-to-postgres.sh
```

---

## Career Center FastAPI

Career Center includes a FastAPI backend service.

Current endpoints:

* `GET /health`
* `GET /applications`
* `GET /applications/{id}`
* `GET /applications/{id}/jd`
* `GET /applications/{id}/artifacts`

Service location:

```text
services/career-center-api/
```

Startup:

```bash
CAREER_DB_PASSWORD='career_app_dev_password' \
./bin/run-career-center-api.sh
```

---

## Deployment and Operations

Deployment validation has been completed using:

* pl
* ted

Operational assets include:

* Deployment runbook
* PostgreSQL setup automation
* API setup automation
* Smoke tests
* Startup validation checks

Primary documentation:

```text
docs/operations/deploy/
```

---

## Requirements and Sprint Workflow

Career System uses Markdown-based requirements management.

Primary areas:

```text
docs/requirements/epics/
docs/requirements/stories/
docs/requirements/context/
docs/requirements/data-model/
docs/requirements/sprints/
```

Workflow:

```text
Story
→ Feature Branch
→ Implementation
→ Validation
→ Merge
→ Sprint Closeout
→ Release Tag
```

---

## Release Management

Current release tags include:

* v0.11.0-postgres-api-foundation
* v0.11.1-deployment-prep

Release documentation:

```text
docs/releases/
```

Release process:

```text
Development
→ Validation
→ Release Notes
→ Git Tag
→ Deployment
```

---

## Linux Dev Environment Alignment

Career System is generating reusable Linux standards.

Current lessons learned:

* Multi-user GitHub SSH setup
* Service-local Python virtual environments
* Deployment-user validation
* PostgreSQL deployment practices
* Release management workflow

Alignment backlog:

```text
docs/reference/LINUX_DEV_ENV_ALIGNMENT_BACKLOG.md
```

---

## Repository Structure

```text
career-system/
├── bin/
├── data/
├── docs/
│   ├── requirements/
│   ├── releases/
│   ├── standards/
│   └── reference/
├── services/
│   └── career-center-api/
├── sql/
│   └── postgres/
├── templates/
└── obsidian/
```

---

## Important Folder Roles

### `data/`

This is the system-of-record area for structured career artifacts.

Use it for canonical files that should eventually support scripts, JSON records, PostgreSQL tables, REST APIs, and Motorweb integration.

### `obsidian/`

This is the Obsidian-friendly mirror.

Files here may have human-friendly names and wiki-link-friendly organization.

### `templates/`

Reusable templates for future resume versions, cover letters, and thank-you letters.

### `docs/`

Design notes, workflows, versioning rules, and architecture decisions.

### `data/source-resumes/`

Archive area for original PDFs and extracted text. This preserves the source material used to create the markdown masters and role-specific resume versions.

---

## Resume Workflow

Recommended resume workflow:

```text
1. Save the JD exactly as received.
2. Identify the target track: BA or SRE.
3. Start from the matching master resume.
4. Select the most relevant bullets.
5. Create a role-specific resume version.
6. Export or recreate the final resume in Teal if needed.
7. Store the final version back in Career System.
8. Add interview notes and follow-up communications.
```

For example:

```text
Master BA Resume
    ↓
Svitla Senior BA Resume v1

Master BA Resume
    ↓
AEGIS Senior BA Resume v1

Master SRE Resume
    ↓
Pico SRE Resume v1
```

---

## Communication Workflow

Career System stores communications as part of the application record:

```text
Cover letter
Thank-you letter
Follow-up email
Recruiter message draft
Interview recap
```
Current communication artifacts include:

```text
Cover letter masters
Role-specific cover letters
Thank-you letters
Recruiter follow-ups
Application communications
```

---

## Relationship to Teal

Teal can remain the operational tool for formatting, exporting, and tracking some application activity.

Career System should become the long-term source of truth for:

```text
Raw job descriptions
Resume strategy
Resume versions
Application-specific notes
Reusable skills
Interview prep
Historical decisions
```

In short:

```text
Teal = resume builder / application helper
Career System = durable career knowledge base and data model
```

---

## Relationship to Obsidian

Obsidian is the thinking and review layer.

Career System stores Obsidian-friendly markdown so resumes, skills, job notes, and communication drafts can be reviewed like normal notes.

This supports the larger goal:

```text
JD → Skills → Resume → Interview Prep → Obsidian Knowledge
```

---

## Relationship to Motorweb

Career System is the source data and design foundation for a future Motorweb Job Application Platform.

Planned evolution:

```text
Markdown / JSON / CSV files
    ↓
Python utility scripts
    ↓
Repository layer
    ↓
PostgreSQL
    ↓
FastAPI CRUD
    ↓
Motorweb Job Application Platform UI
```

Career System remains file-first for many artifacts while progressively adding PostgreSQL and API capabilities.

---

## Current Non-Goals

For the current release stream, do not build yet:

```text
Authentication
Authorization
React UI
HTTPS
Containers
Kubernetes
Cloud deployment
Vector database
Production AI automation
Complex resume scoring
```

The current focus is:

```text
Operational hardening
Dashboard API foundation
Deployment consistency
Developer onboarding
Motorweb alignment
```

---

## Installation Summary

Clone the repository:

```bash
git clone git@github-squidpan:squidpan/career-system.git
cd career-system
```

Setup PostgreSQL:

```bash
./bin/setup-career-center-postgres.sh
```

Load data:

```bash
PGPASSWORD='career_app_dev_password' \
./bin/load-applications-to-postgres.sh

PGPASSWORD='career_app_dev_password' \
./bin/load-application-artifacts-to-postgres.sh
```

Setup API:

```bash
./bin/setup-career-center-api.sh
```

Start API:

```bash
CAREER_DB_PASSWORD='career_app_dev_password' \
./bin/run-career-center-api.sh
```

Validate:

```bash
./bin/smoke-test-career-center-api.sh
```

Detailed deployment instructions:

```text
docs/operations/deploy/
```

---

## First Review Checklist

After installing, review these first:

```text
sql/postgres/
services/career-center-api/
docs/requirements/
docs/releases/
docs/standards/python/
data/resume-masters/master-ba-resume.md
data/resume-masters/master-sre-resume.md
data/resume-versions/svitla/resume-svitla-senior-ba-v1.md
data/resume-versions/aegis/resume-aegis-senior-ba-v1.md
obsidian/Resumes/Masters/Master BA Resume.md
obsidian/Resumes/Masters/Master SRE Resume.md
```

---

## Next Recommended Version

Suggested v0.12.x Scope

- Operational hardening completion
- Dashboard summary APIs
- OpenAPI / Swagger exposure
- Developer bootstrap standards
- Motorweb Career Center alignment
- PostgreSQL and API operational maturity
