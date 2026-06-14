---
id: UAT-MW-003
type: uat
project: motorweb
story: US-MW-003
status: backlog
created: 2026-06-14
updated: 2026-06-14
---

# UAT-MW-003 Load Career System Data

## UAT Objective

Confirm Career System data can be loaded into PostgreSQL using a repeatable process.

## Test Steps

1. Identify Career System source files.
2. Run the data load command or script.
3. Query table counts.
4. Spot-check at least three job roles.
5. Confirm associated JD or application package metadata where available.

## Expected Result

Career System data appears in PostgreSQL and can be inspected using SQL.
