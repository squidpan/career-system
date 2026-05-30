# Resume Versioning Standard

## Naming

```text
master-ba-resume.md
master-sre-resume.md
resume-<company>-<role>-v<version>.md
```

Examples:

```text
resume-svitla-senior-ba-v1.md
resume-aegis-senior-ba-v1.md
resume-pico-sre-v1.md
```

## Version bump rule

Use a new version when any of the following changes:

- Summary positioning changes materially
- Experience bullets are rewritten for a different role
- Skills section changes materially
- Resume is sent externally
- Resume is exported to PDF

## Record fields for future JSON tracking

```json
{
  "resume_version_id": "resume_svitla_senior_ba_v1",
  "source_master": "master-ba-resume.md",
  "company": "Svitla",
  "role_title": "Senior Business Analyst",
  "status": "sent",
  "created_date": "2026-05-30",
  "based_on_files": []
}
```
