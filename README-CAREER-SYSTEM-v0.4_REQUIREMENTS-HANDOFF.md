# Career System v0.4 Requirements Handoff

## Purpose

This handoff summarizes the current Career System operational state and what should be created next in the **Career System Requirements v0.4** session.

The goal is to convert real issues discovered during operational job applications into formal requirements, user stories, bug stories, acceptance criteria, validation steps, and future Motorweb PostgreSQL POC requirements.

---

## Current Repo State

Repo:

```text
~/pjs/repos/career-system
```

Latest completed commits:

```text
a53026d Add application tracker foundation
37a1aaf Classify June 2026 JD source files
631cf8d Preserve ICE fit analysis summary separately
```

The repo should now be clean.

---

## Operational Progress

Career System is now being used operationally, not just prototyped.

Recent submitted applications:

| Company       | Status                                       |
| ------------- | -------------------------------------------- |
| Citi          | APPLIED                                      |
| Broadridge    | APPLIED                                      |
| ICE           | APPLIED                                      |
| QODE          | APPLIED                                      |
| Shutterstock  | APPLIED                                      |
| New York Life | APPLIED                                      |
| LSEG          | APPLIED                                      |
| AEGIS         | REJECTED / no response after extended period |
| Pico          | REJECTED                                     |
| Amtrak        | REJECTED                                     |
| UPMC          | NOT_PURSUED                                  |
| Finbourne     | POSITION_CLOSED                              |
| DTCC          | POSITION_CLOSED                              |

---

## New Application Tracker

Created:

```text
data/application-tracker/
├── README.md
├── application-status-reference.md
└── applications.csv
```

Canonical statuses:

```text
DRAFT
READY
APPLIED
INTERVIEW
REJECTED
WITHDRAWN
NOT_PURSUED
POSITION_CLOSED
OFFER
HIRED
```

Current tracker counts:

```text
7 APPLIED
3 REJECTED
2 POSITION_CLOSED
1 NOT_PURSUED
```

This tracker should become the first dataset for the Motorweb Career Center PostgreSQL POC.

---

## Motorweb POC Direction

Motorweb Career Center POC should be staged:

```text
POC 0: Local PostgreSQL only
POC 1: SQL dashboard queries
POC 2: REST API
POC 3: UI dashboard
```

Immediate Motorweb focus is **not REST yet**.

First objective:

```text
Load Career System application tracker data into local PostgreSQL and query application status via SQL.
```

Expected future table:

```text
career_center.application
```

Expected first SQL dashboard query:

```sql
select company,
       role,
       status,
       date_applied,
       last_update
from application
order by last_update desc;
```

---

## Requirements Needed

Create a new requirements set for:

```text
EPIC-CS-002 Application Tracking and Continuous Improvement
EPIC-MW-002 Motorweb Career Center PostgreSQL POC
```

Career System defines the business/data requirements.

Motorweb implements them in PostgreSQL first, then REST API later.

---

## User Stories Needed

### Career System Stories

Create stories for:

```text
US-CS-041 Application Tracker Foundation
US-CS-042 Standardize Submission Notes Format
US-CS-043 Normalize Application Status Lifecycle
US-CS-044 Detect Unknown Company During JD Normalization
US-CS-045 Detect Unknown Role During JD Normalization
US-CS-046 Separate Fit Analysis from Professional Summary
US-CS-047 Preserve Approved Resume Experience Facts
US-CS-048 Application Tracker Update Workflow
```

### Motorweb PostgreSQL POC Stories

Create stories for:

```text
US-MW-020 Create Local career_center PostgreSQL Database
US-MW-021 Create Application Status Reference Table
US-MW-022 Create Application Table
US-MW-023 Load Career System applications.csv
US-MW-024 Query Applications by Status
US-MW-025 Query Applications by Company and Date
US-MW-026 Validate Career System CSV Matches PostgreSQL Rows
```

REST API stories should come later, after the PostgreSQL POC works.

---

## Bugs Discovered During Operational Use

Create bug stories for:

```text
BUG-CS-001 Professional Summary overwritten by Application Summary / Fit Analysis content
BUG-CS-002 PlanetCAD client references lost or attributed incorrectly
BUG-CS-003 Real-time streaming market data wording lost during tailoring/enhancement
BUG-CS-004 submission-notes.md template inconsistent across packages
BUG-CS-005 Application status requires manual update in multiple locations
BUG-CS-006 JD normalizer creates unknown-company / unknown-role normalized files
BUG-CS-007 JD normalizer run_id polluted with source file path
BUG-CS-008 Application package generated from wrong source artifact type
```

---

## Testing Requirement

Every user story and bug story must include:

```text
Acceptance Criteria
Manual Validation Steps
Programmatic Validation Steps
Regression Validation Steps
```

Example for BUG-CS-001:

Manual validation:

```text
Open generated ATS resume.
Confirm Professional Summary contains only resume-ready summary text.
Confirm Recommendation, Fit Score, Gaps, and Mitigation do not appear in resume summary.
```

Programmatic validation:

```bash
grep -n "Recommendation\|Overall Fit Score\|Potential Gaps\|Mitigation" \
  data/full-resumes/*-ats-resume-v1.md
```

Regression validation:

```text
Generate ICE, QODE, LSEG packages.
Confirm all Professional Summary sections remain clean.
```

---

## Important Design Principle

No story is complete unless it has validation steps.

No bug is fixed unless it has a regression check.

No Motorweb POC story is accepted unless SQL proves the data loaded correctly.

---

## Current Next Step

In the Requirements chat, generate the v0.4 requirements artifacts:

```text
EPIC-CS-002
EPIC-MW-002
US-CS stories
US-MW PostgreSQL POC stories
BUG-CS stories
Traceability updates
Validation/test sections
```

After that, return to Career System implementation (see additional notes) and apply fixes before clipping/processing more JDs.

## ADDITIONAL NOTES:

Once above it done, go back to chat, Career Center v0.1 after you finish in the Requirements project Chat.

Think of the workflow like this:

Requirements Chat

Produces:

Epics
User Stories
Bug Stories
Acceptance Criteria
Validation/Test Cases
Traceability updates
Data Model changes
PostgreSQL POC requirements

This is your planning and requirements authority.

This Chat (Career System Operational / Implementation)

Consumes:

Approved requirements
Approved bug stories
Approved Motorweb POC stories

This is where we:

update repo structure
modify scripts
fix bugs
improve resume generation
improve JD normalization
implement tracker features
prepare PostgreSQL loads
prepare Motorweb handoff artifacts


### What to Bring Back to Career Center v0.1 Chat

When you finish in the Requirements chat, bring back:

1. New Epic files

Something like:

EPIC-CS-002
EPIC-MW-002
2. New Story list

Something like:

US-CS-041
US-CS-042
US-CS-043
...

US-MW-020
US-MW-021
US-MW-022
...
3. Bug list

Especially:

BUG-CS-001
BUG-CS-002
...
BUG-CS-008
4. Prioritization

Most important thing.

Ask the Requirements chat to produce:

Mini-v0.4 Implementation Order

For example:

P0
BUG-CS-001
BUG-CS-004
BUG-CS-006

P1
US-CS-041
US-CS-042

P2
US-MW-020
US-MW-021
US-MW-022

That implementation order will drive what we do here.
