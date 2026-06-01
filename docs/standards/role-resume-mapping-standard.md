# Role → Resume Mapping Standard

## Purpose

A role should recommend the best resume master/family.

This lets Career System move from:

```text
JD -> Role
```

to:

```text
JD -> Role -> Resume
```

## Source Registry

The mapping is driven by:

```text
data/reference/role-code-registry.json
data/reference/resume-family-registry.json
```

## Generated Role Fields

```yaml
recommended_resume_family:
recommended_resume_master_id:
recommended_resume_file:
```

## Rule

The role generator should not invent resume mappings.

It should look up the role code in `role-code-registry.json`.

If the role code is missing, generated roles should keep the fields blank and the registry should be updated later.
