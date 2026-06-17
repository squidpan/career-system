When you go back to the Career System v0.1 chat, don't ask it to generate more random stories.

Give it this exact direction:

Sprint Review Overlay Pack Request

We completed Sprint 1 design review and captured new architectural decisions.

Reference document:

README_CAREER SYSTEM_v0.4_DESIGN_DISCUSSION.md

Key design decisions already approved:

1. submission-notes.md is the Application Event Record

2. Normalized JD is the Job Metadata Record

3. applications.csv is a generated rollup dataset

4. Human-readable role name remains

5. role_code remains optional until normalization quality improves
Objective

Create a v0.4 Sprint Review Overlay Pack for Career System Requirements.

This is not implementation.

This is architecture and requirements alignment before Sprint 2.

Required Artifacts
Context Package

Create:

docs/requirements/context/
CTX-CS-002-application-tracking-architecture.md

Contents:

Purpose

Application Tracking Architecture

Source Of Truth Decisions

Data Flow

Relationship between:

submission-notes.md
normalized JD
applications.csv
PostgreSQL
Motorweb Dashboard
REST APIs

Future Direction

Traceability

Include architecture diagram.

New Business Requirements

Create:

BR-CS-003 Knowledge Reuse

BR-CS-004 Application Status Single Source Of Truth
New Stories

Create:

US-CS-049 Submission Notes Metadata Standard

US-CS-050 Application Tracker CSV Generation

US-CS-051 Role Metadata Propagation From Normalized JD

US-CS-052 Optional Role Classification Fields

US-CS-053 Application Status Single Source Of Truth

US-MW-027 PostgreSQL Schema Alignment

US-MW-028 JSON Payload Alignment

Each story must include:

Business Context

Scope

Out Of Scope

Acceptance Criteria

Manual Validation

Programmatic Validation

Regression Validation

Traceability
New Data Models

Create:

DM-CS-007 Application Event

DM-CS-008 Generated Application Rollup

Application Event should model:

company:
role:
status:
date_applied:
last_update:
resumes:

Generated Application Rollup should model:

submission-notes.md
      +
normalized JD
      ↓
applications.csv
Traceability Update

Update RTM:

submission-notes
      ↓
Application Event
      ↓
Generated CSV
      ↓
PostgreSQL Schema
      ↓
REST JSON Payload
Architecture Diagram

Create PlantUML:

docs/requirements/diagrams/
application-tracking-architecture.puml

Show:

submission-notes.md
       +
normalized JD
       ↓
applications.csv
       ↓
PostgreSQL
       ↓
Dashboard
       ↓
REST API
Overlay Deliverables

Generate:

career-system-v0.4-sprint-review-overlay.zip

Include:

README.md
overlay instructions
git add
git commit
git push
verification steps
Important Guidance

Do not create disconnected stories.

The order should be:

Design Decisions
      ↓
Context Package
      ↓
Business Requirements
      ↓
Data Model
      ↓
Stories
      ↓
Traceability

The goal is to keep Requirements System coherent and architecture-driven.

That's exactly what I would hand to the Career System chat next. It aligns with the Sprint 1 review document and preserves the architectural decisions before you start PostgreSQL work.

---

# Additional Notes
I would have Career System v0.1 create the stories, not this chat.

Here's why.

What this chat is doing

This chat has been acting like:

Enterprise Architect
+
Business Architect
+
Requirements Coach

We have been shaping:

Vision
Business Requirements
Architecture
Context Packages
Data Models
Traceability
What Career System v0.1 should do

Career System v0.1 knows:

Current repo structure
Existing requirement files
Existing IDs
Current epics
Current stories
Current traceability
Current naming conventions

Therefore it is in a much better position to create:

CTX-CS-002

BR-CS-003
BR-CS-004

US-CS-049
US-CS-050
US-CS-051
US-CS-052
US-CS-053

US-MW-027
US-MW-028

DM-CS-007
DM-CS-008

PlantUML diagrams

README

Overlay ZIP

directly consistent with the repository.

Recommended Workflow
Step 1

Go to:

Career System v0.1

Paste exactly the instructions I gave you.

Step 2

Tell it:

Generate the complete Sprint Review Overlay Pack.

DO IT FULL.

Since you've already trained that chat on your workflow, it should generate:

Overlay ZIP
README
on-screen instructions
git commands
verification steps
Step 3

Overlay into:

~/pjs/repos/career-system

Commit.

Push.

Step 4

Review the generated artifacts.

Especially:

CTX-CS-002
DM-CS-007
DM-CS-008
BR-CS-003
BR-CS-004

Those are the highest-value artifacts.

When To Come Back Here

Come back here when one of these happens:

A. Architecture review

Example:

Do these entities make sense?

Application
Application Event
Outcome
Evidence
Knowledge Asset
B. Data model review

Example:

Should Application Package
and Application be separate entities?
C. Story quality review

Example:

Are these stories actually useful?

Do they read like real requirements?
D. PostgreSQL design review

Example:

Before I create tables,
review my logical data model.
My Preference

I would let Career System v0.1 own:

Requirements repository content

and use this chat for:

Requirements methodology
Architecture
Modeling
BA coaching

That separation mirrors what happens in real projects:

Repository
    =
Source of Truth

Architecture Review
    =
Separate discussion

So yes:

✅ Paste the instructions into Career System v0.1.

✅ Have it generate the overlay pack.

✅ Apply the overlay.

✅ Commit and push.

Then review the results and come back to Career-system Requirements for the architecture/model review before Sprint 2 implementation starts.