# Career System v0.9.0 — Resume Generation Engine

## Purpose

Generate first-pass tailored resume drafts from v0.8.0 resume-tailoring artifacts.

v0.8.0 answers:

```text
How should Paul's resume be tailored?
```

v0.9.0 answers:

```text
What first-pass tailored resume draft should Paul review?
```

## Inputs

```text
data/resume-tailoring/*.json
```

## Outputs

```text
data/resume-generated/
  resume-generated-*.md
  resume-generated-*.json
  resume-generation-report-*.md
  resume-generation-report-*.json
```

## Important Scope

This release generates Markdown resume drafts only.

It does not:
- export PDF
- push into Teal
- guarantee final 2-page formatting
- replace manual review

## Install Overlay

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v090-resume-generation
mkdir -p /tmp/career-system-v090-resume-generation

unzip ~/Downloads/career-system-v0.9.0-resume-generation-engine-overlay.zip \
  -d /tmp/career-system-v090-resume-generation

cp -R /tmp/career-system-v090-resume-generation/* .

chmod +x bin/run-resume-generation.sh
chmod +x scripts/generate_resumes.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-08-resume-generation-v1
rm -rf data/resume-generated

./bin/run-resume-generation.sh \
  run-2026-06-08-resume-generation-v1 \
  data/resume-tailoring
```

## Validate

```bash
find data/resume-generated -name 'resume-generated-*.md' | wc -l

sed -n '1,260p' \
  data/resume-generated/resume-generation-report-run-2026-06-08-resume-generation-v1.md

sed -n '1,260p' \
  data/resume-generated/resume-generated-dow-jones-ba-ai-2026.md

sed -n '1,260p' \
  data/resume-generated/resume-generated-citi-support-appsupport-2026.md
```

Expected:

```text
27 generated resume drafts
1 generation report
role-specific summary, core skills, selected highlights, experience bullets, claims-to-avoid note
```

## Git Commit

After review:

```bash
git add README_RESUME_GENERATION_ENGINE.md
git add bin/run-resume-generation.sh
git add scripts/generate_resumes.py
git add docs/standards/resume-generation-standard.md
git add templates/generated-resume-template.md
git add data/resume-generated

git commit -m "Add resume generation engine v0.9.0"

git push

git tag -a v0.9.0-resume-generation-engine \
  -m "Resume generation engine complete"

git push origin v0.9.0-resume-generation-engine
```

## Notes

This is intentionally conservative. It generates reviewable resume drafts from known tailoring guidance, not fully final resumes.
