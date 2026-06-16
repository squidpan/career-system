# Application Status Update Workflow

## Purpose

Defines the standard process for updating application status within Career System.

## Source Of Truth

applications.csv is the authoritative source.

submission-notes.md is a package-level view.

If values differ:

applications.csv wins.

---

## Workflow

### New Application

1. Create application package
2. Generate resumes
3. Submit application
4. Update applications.csv
5. Update submission-notes.md
6. Commit
7. Push

### Status Change

Examples:

- Interview
- Rejected
- Offer
- Position Closed
- Withdrawn

Steps:

1. Update applications.csv
2. Update submission-notes.md
3. Commit
4. Push

---

## Allowed Status Values

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
