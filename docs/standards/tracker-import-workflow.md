# Tracker Import Workflow

## Principle

Tracker owns lifecycle. JD owns content.

```text
Tracker = active job-search inventory
JD = job description content and role classification evidence
Role = normalized Career System role object
```

## Source

The first supported tracker source is Teal roles CSV.

## Important Fields

From Teal roles CSV:

```text
id
company_name
role
url
location
source
statusName
added_at
applied_at
created_at
updated_at
archived_at
```

## Career System Fields

```yaml
source_system: teal
source_role_id:
tracker_status:
tracker_scope:
active_in_tracker:
existing_role_id:
existing_jd_ids:
```

## Matching Strategy

1. Match Teal `id` against existing role/JD `source_url` values containing the same UUID.
2. If matched, populate `existing_role_id`.
3. If unmatched, leave `existing_role_id` blank and set `match_status: no_match`.

## Deletion / Scope Rule

If a role disappears from a future Teal export, Career System should not delete it.

It should eventually mark prior tracker records as:

```yaml
tracker_scope: out_of_scope
active_in_tracker: false
```
