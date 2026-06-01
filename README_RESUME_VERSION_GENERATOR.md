# Career System Resume Version Generator v0.3.5

This overlay adds resume-version generation from role records.

## Purpose

v0.3.4 created role files with resume recommendations:

```yaml
recommended_resume_family: ba
recommended_resume_master_id: resume-master-ba-v1
recommended_resume_file: data/resume-masters/master-ba-resume.md
```

v0.3.5 consumes those fields and generates first-pass resume-version Markdown files.

## Workflow

```text
Raw JD
  -> Normalized JD
  -> Role
  -> Resume Version
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-resume-version-generator
mkdir -p /tmp/career-system-resume-version-generator

unzip ~/Downloads/career-system-v0.3.5-resume-version-generator-overlay.zip \
  -d /tmp/career-system-resume-version-generator

cp -R /tmp/career-system-resume-version-generator/* .

chmod +x bin/run-resume-version-generation.sh
chmod +x scripts/generate_resume_versions_from_roles.py
```

## Run

```bash
./bin/run-resume-version-generation.sh run-2026-06-01-resume-version-generate-v1 data/roles
```

## Review

```bash
tree data/resume-versions/generated -L 2
head -120 data/resume-versions/generated/*.md
```

## Commit

```bash
git add README_RESUME_VERSION_GENERATOR.md
git add bin/run-resume-version-generation.sh
git add scripts/generate_resume_versions_from_roles.py
git add docs/standards/resume-version-generation-workflow.md
git add templates/generated-resume-version-template.md
git add data/resume-versions/generated

git commit -m "Add resume version generation v0.3.5"
git push
```

Do not add `ops/runs/` run artifacts.
