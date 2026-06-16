---
id: REL-MW-0.4
type: release
project: motorweb
status: draft
priority: high
tags: [requirements, motorweb, postgresql]
created: 2026-06-14
updated: 2026-06-14
---

# REL-MW-0.4 PostgreSQL POC

## Objective

Load Career System application tracker data into local PostgreSQL and query application status via SQL.

## Included Stories

- [[US-MW-020 Create Local career_center PostgreSQL Database]]
- [[US-MW-021 Create Application Status Reference Table]]
- [[US-MW-022 Create Application Table]]
- [[US-MW-023 Load Career System applications.csv]]
- [[US-MW-024 Query Applications by Status]]
- [[US-MW-025 Query Applications by Company and Date]]
- [[US-MW-026 Validate Career System CSV Matches PostgreSQL Rows]]

## Not Included

- REST API
- React UI
- Dockerized deployment

## Exit Criteria

- SQL proves data loaded correctly.
- Application counts match Career System tracker.
- Initial dashboard query works from psql.
