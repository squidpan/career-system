# Tracker Role Classification Workflow

## Purpose

Classify tracker roles before JD clipping is complete.

This supports fast selection of target jobs and resume-family routing.

## Input

```text
data/tracker/normalized/*.md
```

## Output

The same tracker-role files enriched with:

```yaml
role_family:
role_level:
role_qualifiers:
role_code:
role_code_confidence:
recommended_resume_family:
recommended_resume_master_id:
recommended_resume_file:
classification_status:
classification_source:
```

## Rule

If classification is weak, keep:

```yaml
role_code: unknown
classification_status: needs_review
```
