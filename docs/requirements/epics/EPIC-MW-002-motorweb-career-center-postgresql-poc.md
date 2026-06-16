---
id: EPIC-MW-002
type: epic
project: motorweb
status: draft
priority: high
tags: [requirements, motorweb, postgresql, career-center]
created: 2026-06-14
updated: 2026-06-14
---

# EPIC-MW-002 Motorweb Career Center PostgreSQL POC

## Technical Objective

Create the first Motorweb Career Center PostgreSQL proof of concept using Career System application tracker data.

## Business Context

Career System defines the business and data requirements. Motorweb implements the queryable platform layer.

## POC Stages

```text
POC 0: Local PostgreSQL only
POC 1: SQL dashboard queries
POC 2: REST API
POC 3: UI dashboard
```

## Initial Focus

The immediate focus is PostgreSQL and SQL only.

## First Dataset

```text
data/application-tracker/applications.csv
```

## Expected Table

```text
career_center.application
```

## First Dashboard Query

```sql
select company,
       role,
       status,
       date_applied,
       last_update
from application
order by last_update desc;
```

## Success Criteria

- Local career_center database exists.
- Application status reference table exists.
- Application table exists.
- Career System CSV data loads successfully.
- SQL queries prove the data loaded correctly.
- PostgreSQL row counts match Career System CSV counts.
