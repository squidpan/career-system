# US-MW-013A Career API Service Account

Status: Proposed

## User Story

As a platform administrator,
I want the Career Center FastAPI service to run under a dedicated Linux service account,
so that the API does not depend on a human developer account.

## Business Context

Career Center currently runs manually from a human user session during development.

For production-style deployment, the API should eventually run as a managed service under a machine identity such as `career-api`.

This supports clearer ownership, safer permissions, and better operational discipline.

## Scope

Define future standards for:

- `career-api` Linux service account
- non-interactive login policy
- systemd service ownership
- environment variable handling
- PostgreSQL credential handling
- log location
- startup and restart behavior

## Out of Scope

- Creating the `career-api` account now
- Creating a systemd service now
- Moving deployment to `/opt/projects` now
- Production hardening now

## Acceptance Criteria

- Dedicated service account is identified.
- Human users and service account responsibilities are separated.
- Future systemd ownership model is documented.
- PostgreSQL connection responsibility is documented.
- This story is linked to the Linux Service Account Standard.

## Future Target Model

```text
pl
    builds and releases Career System

ted
    validates tagged releases

career-api
    runs the deployed FastAPI process

career_app
    PostgreSQL database role used by the FastAPI process
```

## Notes

This story prepares Career Center for production-style deployment without implementing it immediately.
