---
id: UAT-MW-001
type: uat
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
  - uat
---

# UAT-MW-001 PostgreSQL Environment Ready

## UAT Objective

Confirm that Paul can use the local PostgreSQL environment as the foundation for Motorweb Career Center POC work.

## Test Steps

### Step 1: Check PostgreSQL Client

Run:

```bash
psql --version
```

Expected:

```text
PostgreSQL client version is displayed.
```

### Step 2: Check PostgreSQL Service

Run:

```bash
systemctl status postgresql --no-pager
```

Expected:

```text
PostgreSQL service is active/running or otherwise confirmed available.
```

### Step 3: Connect as Admin User

Run the appropriate local connection command.

Expected:

```text
Connection succeeds.
```

## Pass / Fail

Pass if PostgreSQL is installed, running, and accessible from terminal.

Fail if PostgreSQL cannot be reached or credentials are not confirmed.

## Related Artifacts

- [[US-MW-001 PostgreSQL Environment Ready]]
- [[AC-MW-001]]

