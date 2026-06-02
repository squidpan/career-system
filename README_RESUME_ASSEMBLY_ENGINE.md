# Career System Resume Assembly Engine v0.3.9

This overlay adds complete resume assembly.

## Purpose

Existing generated resume versions are metadata records with a source master excerpt.

v0.3.9 creates complete assembled resume markdown files using:

```text
Role
Normalized JD
Generated Resume Version Record
Full Master Resume
```

## Output

```text
data/resume-versions/assembled/
└── resume-<company-role>-assembled-v1.md
```

## Current behavior

This first version is deterministic and conservative:

- Uses the full selected master resume.
- Adds role/JD/application metadata.
- Adds tailoring notes and checklist sections.
- Does not invent unverified experience.
- Does not overwrite existing generated resume-version records.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-resume-assembly
mkdir -p /tmp/career-system-resume-assembly

unzip ~/Downloads/career-system-v0.3.9-resume-assembly-engine-overlay.zip \
  -d /tmp/career-system-resume-assembly

cp -R /tmp/career-system-resume-assembly/* .

chmod +x bin/run-resume-assembly.sh
chmod +x scripts/assemble_resumes.py
```

## Run all roles

```bash
./bin/run-resume-assembly.sh \
  run-2026-06-01-resume-assembly-v1 \
  data/roles
```

## Review

```bash
ls -1 data/resume-versions/assembled | sort
head -120 data/resume-versions/assembled/*.md
grep -n "## Work Experience" data/resume-versions/assembled/*.md
```

## Commit

```bash
git add README_RESUME_ASSEMBLY_ENGINE.md
git add bin/run-resume-assembly.sh
git add scripts/assemble_resumes.py
git add docs/standards/resume-assembly-workflow.md
git add templates/assembled-resume-template.md
git add data/resume-versions/assembled

git commit -m "Add resume assembly engine v0.3.9"
git push
```

Do not add `ops/runs/` artifacts.
