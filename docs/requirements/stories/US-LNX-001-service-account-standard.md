# US-LNX-001 Linux Service Account Standard

Status: Proposed

## User Story

As a platform administrator,
I want standard Linux service account rules,
so that long-running services and machine processes do not run under human user accounts.

## Business Context

Career System and Motorweb are evolving from local developer tools into service-oriented platforms.

Human users such as `pl`, `bas`, `ted`, and future `dev` should be separated from machine identities such as `career-api`, `career-loader`, `motorweb-api`, and `market-streamer`.

## Scope

Define standards for:

- Human accounts
- Service accounts
- Naming conventions
- Login policy
- Home directory policy
- File ownership
- systemd execution
- Secrets handling
- Auditability

## Out of Scope

- Immediate implementation
- Creating service accounts now
- Production deployment
- Cloud IAM

## Acceptance Criteria

- Standard differentiates human users and service accounts.
- Candidate service account names are documented.
- Non-login policy is documented.
- systemd ownership model is documented.
- Relationship to linux-dev-env is documented.

## Candidate Human Accounts

- `pl` — admin / architect / primary developer
- `dev` — future developer
- `ted` — QA / release validation user
- `bas` — Linux standards and environment validation user

## Candidate Service Accounts

- `career-api`
- `career-loader`
- `motorweb-api`
- `market-streamer`

## Notes

This story belongs primarily in linux-dev-env but is tracked here because Career System and Motorweb are the first consumers of the standard.

Service accounts should eventually be created as non-login users, for example:

```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin career-api
```
