---
id: PREREQ-MW-001
type: prerequisite
project: motorweb
story: US-MW-001
status: draft
priority: high
created: 2026-06-14
updated: 2026-06-14
tags:
  - requirements
  - motorweb
  - postgres
  - prerequisite
---

# PREREQ-MW-001 PostgreSQL Installed

## Purpose

Confirm PostgreSQL is installed locally and available for Motorweb Career Center POC work.

## Validation Commands

```bash
psql --version
systemctl status postgresql --no-pager
```

## Expected Results

- `psql --version` returns a PostgreSQL client version
- PostgreSQL service is active or otherwise confirmed running locally

## Manual Verification

Paul can connect to PostgreSQL from terminal or pgAdmin.

## Related Artifacts

- [[US-MW-001 PostgreSQL Environment Ready]]

