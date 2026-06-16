# Application Tracker

## Purpose

Career System application tracker for monitoring job application lifecycle, submission outcomes, and future dashboard/database loading.

This tracker is intended to support:

* daily application status review
* manual dashboard use
* future PostgreSQL loading
* future Motorweb Career Center dashboard
* application outcome analysis
* continuous improvement of resumes and application packages

## Files

| File                            | Purpose                                 |
| ------------------------------- | --------------------------------------- |
| applications.csv                | Canonical application tracker dataset.  |
| application-status-reference.md | Allowed status values and status rules. |

## Workflow

After each application event:

1. Update the package `submission-notes.md`.
2. Update `data/application-tracker/applications.csv`.
3. Commit the changes.
4. Push to remote.

## Future Motorweb Use

This CSV will become the first source dataset for the Motorweb Career Center PostgreSQL POC.

Initial target table:

```sql
career_center.application
```

Example dashboard query:

```sql
select company,
       role,
       status,
       date_applied,
       last_update
from application
order by last_update desc;
```

