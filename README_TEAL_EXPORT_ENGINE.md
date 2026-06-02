# Career System Teal Export Engine v0.4.0

Creates Teal-friendly resume markdown files from Career System assembled resumes.

## Input

```text
data/resume-versions/assembled/*.md
```

## Output

```text
data/resume-versions/teal-export/*.md
```

## What It Removes

- YAML frontmatter
- Assembly Summary
- Tailoring Checklist
- JD Keywords Detected
- Manual Tailoring Steps
- role IDs / run IDs / application package IDs
- internal Career System metadata

## What It Keeps

- Contact
- Target Positioning
- Professional Summary
- Core Strengths
- Work Experience
- Education
- Publications
- Skills
- Languages

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-teal-export
mkdir -p /tmp/career-system-teal-export

unzip ~/Downloads/career-system-v0.4.0-teal-export-engine-overlay.zip \
  -d /tmp/career-system-teal-export

cp -R /tmp/career-system-teal-export/* .

chmod +x bin/run-teal-export.sh
chmod +x scripts/generate_teal_export_resumes.py
```

## Run

```bash
./bin/run-teal-export.sh \
  run-2026-06-02-teal-export-v1 \
  data/resume-versions/assembled
```

## Review

```bash
ls -1 data/resume-versions/teal-export | sort

grep -R "Assembly Summary" data/resume-versions/teal-export || true
grep -R "Tailoring Checklist" data/resume-versions/teal-export || true
grep -R "JD Keywords" data/resume-versions/teal-export || true
grep -R "run_id" data/resume-versions/teal-export || true

grep -n "^## Professional Summary" data/resume-versions/teal-export/*.md
grep -n "^## Work Experience" data/resume-versions/teal-export/*.md
grep -n "^## Skills" data/resume-versions/teal-export/*.md

sed -n '1,220p' data/resume-versions/teal-export/resume-citi-support-appsupport-2026-teal-v1.md
```

## Commit

```bash
git add README_TEAL_EXPORT_ENGINE.md
git add INSTALL_TEAL_EXPORT_V040.md
git add bin/run-teal-export.sh
git add scripts/generate_teal_export_resumes.py
git add docs/standards/teal-export-workflow.md
git add templates/teal-export-resume-template.md
git add data/resume-versions/teal-export

git status
git commit -m "Add Teal export engine v0.4.0"
git push
```

## Tag After Teal Test

```bash
git tag -a v0.4.0-teal-export \
  -m "Teal export engine complete"

git push origin v0.4.0-teal-export
```

Do not add `ops/runs/`.
