---
id: AC-MW-003
type: acceptance-criteria
project: motorweb
story: US-MW-003
status: backlog
created: 2026-06-14
updated: 2026-06-14
---

# AC-MW-003 Load Career System Data

## Acceptance Criteria

### AC1 Source Files Identified

Given Career System contains tracker and JD source files,
when the load process is prepared,
then the required source files are documented.

### AC2 Initial Tables Populated

Given source data exists,
when the load process runs,
then initial Career Center tables are populated with role, event, JD, and application-package metadata where available.

### AC3 Load Is Repeatable

Given the same source files,
when the load process is rerun,
then results are consistent and do not create uncontrolled duplicates.

### AC4 Load Results Are Visible

Given data has loaded,
when SQL count queries are executed,
then row counts are returned for each populated table.
