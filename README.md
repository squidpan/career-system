# Career System

Career System is a personal job-search operating system for managing job opportunities, job descriptions, resumes, cover letters, thank-you letters, interview notes, tracker events, and reusable career knowledge.

The immediate purpose is practical: help Paul apply to jobs faster, keep each application organized, and turn every job description into better resumes, better interview preparation, and better Obsidian notes.

The long-term purpose is architectural: start with simple Markdown, JSON, CSV, and file folders, then evolve toward the Motorweb Job Application Platform with PostgreSQL, FastAPI CRUD services, REST APIs, and eventually a web UI.

---

## Current Version

```text
Career System v0.2.2
Focus: Resume system foundation
```

This version adds the first structured resume layer:

```text
Master BA Resume
Master SRE Resume
Role-specific resume versions
Cover letter masters
Role-specific cover letters
Thank-you letters
Resume templates
Obsidian-friendly mirrors
Source resume archive
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

## Repository Structure

```text
career-system/
├── README.md
├── INSTALL_FROM_ZIP.md
├── README_RESUME_OVERLAY.md
├── install-overlay.sh
│
├── docs/
│   └── resume-system/
│       ├── RESUME_SYSTEM_README.md
│       ├── RESUME_VERSIONING.md
│       ├── RESUME_MASTER_STRATEGY.md
│       ├── RESUME_TO_JOB_WORKFLOW.md
│       └── COMMUNICATIONS_WORKFLOW.md
│
├── data/
│   ├── resume-masters/
│   ├── resume-versions/
│   ├── cover-letter-masters/
│   ├── cover-letter-versions/
│   ├── thank-you-letters/
│   ├── source-resumes/
│   └── resume-system-manifest.json
│
├── templates/
│   ├── resumes/
│   └── communications/
│
└── obsidian/
    ├── Resumes/
    └── Communications/
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

For v0.2.2, the communication layer includes:

```text
Cover Master BA
Cover Master SRE
AEGIS Cover Letter v1
Pico Cover Letter v1
AEGIS Thank You 2026-05-18
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

Do not overbuild yet. v0.2.2 is intentionally file-first.

---

## Current Non-Goals

For this version, do not build yet:

```text
PostgreSQL
FastAPI
Authentication
Web UI
Vector database
Full AI automation
Complex resume scoring
```

The current goal is clean structure and useful artifacts.

---

## Installation Summary

Use the safe `/tmp` overlay pattern:

```bash
mkdir -p ~/pjs/repos/career-system
cd ~/pjs/repos/career-system

git init
git branch -M main

rm -rf /tmp/career-system-overlay
mkdir -p /tmp/career-system-overlay

unzip ~/Downloads/career-system-v0.2.2-resume-overlay.zip \
  -d /tmp/career-system-overlay

cp -R /tmp/career-system-overlay/career-system-v0.2.2-resume-overlay/* .

tree -L 3

git add .
git commit -m "Initial Career System v0.2.2 resume foundation"
```

Then create an empty GitHub repo named `career-system` and push:

```bash
git remote add origin git@github-squidpan:squidpan/career-system.git
git push -u origin main
```

See `INSTALL_FROM_ZIP.md` for the detailed A-Z install flow.

---

## First Review Checklist

After installing, review these first:

```text
data/resume-masters/master-ba-resume.md
data/resume-masters/master-sre-resume.md
data/resume-versions/svitla/resume-svitla-senior-ba-v1.md
data/resume-versions/aegis/resume-aegis-senior-ba-v1.md
obsidian/Resumes/Masters/Master BA Resume.md
obsidian/Resumes/Masters/Master SRE Resume.md
```

---

## Next Recommended Version

Suggested v0.3 scope:

```text
Job description storage
Role records
Application tracker events
Resume-version-to-role linking
Source system standards: LinkedIn, Indeed, Dice, Monster, ZipRecruiter, recruiter, referral
ID generation utility scripts
```

