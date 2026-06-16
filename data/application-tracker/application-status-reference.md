# Application Status Reference

## Purpose

Defines canonical application lifecycle statuses used by Career System.

## Status Values

| Status | Meaning |
|---|---|
| DRAFT | Application package or opportunity exists but is not ready to submit. |
| READY | Application package is ready to submit. |
| APPLIED | Application was submitted. |
| INTERVIEW | Interview process started or pending. |
| REJECTED | Employer rejected application or role is no longer moving forward. |
| WITHDRAWN | Candidate withdrew from consideration. |
| NOT_PURSUED | Candidate intentionally decided not to apply. |
| POSITION_CLOSED | Role closed or disappeared before application. |
| OFFER | Offer received. |
| HIRED | Offer accepted / hired. |

## Rules

- Use only one canonical status per application.
- Update status immediately after application submission or outcome.
- Do not append duplicate status blocks in submission notes.
- Keep tracker status and package submission-notes status aligned.
