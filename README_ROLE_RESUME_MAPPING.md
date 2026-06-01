# Career System Role → Resume Mapping v0.3.4

This overlay updates role generation so roles are enriched with recommended resume metadata.

## Purpose

After v0.3.3, Career System has:

```text
data/reference/role-code-registry.json
data/reference/resume-family-registry.json
```

v0.3.4 makes `generate_roles_from_jds.py` consume those registries.

## New fields added to generated roles

```yaml
recommended_resume_family:
recommended_resume_master_id:
recommended_resume_file:
```

Example:

```yaml
role_code: sba-ai
recommended_resume_family: ba
recommended_resume_master_id: resume-master-ba-v1
recommended_resume_file: data/resume-masters/master-ba-resume.md
```

## Install

From repo root:

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-role-resume-mapping
mkdir -p /tmp/career-system-role-resume-mapping

unzip ~/Downloads/career-system-v0.3.4-role-resume-mapping-overlay.zip \
  -d /tmp/career-system-role-resume-mapping

cp -R /tmp/career-system-role-resume-mapping/* .

chmod +x scripts/generate_roles_from_jds.py
```

## Rerun role generation

```bash
rm -rf ops/runs/run-2026-06-01-role-generate-v2
rm -rf data/roles/*

./bin/run-role-generation.sh run-2026-06-01-role-generate-v2 data/jds/normalized
```

## Review

```bash
head -100 data/roles/*.md
```

Look for:

```yaml
recommended_resume_family:
recommended_resume_master_id:
recommended_resume_file:
```

## Commit

```bash
git add README_ROLE_RESUME_MAPPING.md
git add scripts/generate_roles_from_jds.py
git add templates/generated-role-template.md
git add docs/standards/role-resume-mapping-standard.md
git add data/roles

git commit -m "Add role resume mapping v0.3.4"
git push
```

Do not add `ops/runs/` run artifacts.
