---
id: PREREQ-MW-002
type: prerequisite
project: motorweb
status: backlog
created: 2026-06-14
updated: 2026-06-14
---

# PREREQ-MW-002 Career Center Database Created

## Required For

- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]

## Validation Command

```bash
psql -U postgres -d career_center -c "select current_database();"
```

## Expected Result

```text
 career_center
```
