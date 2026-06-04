# Career System v0.4.6 Resume Tailoring Intelligence

## Purpose

Generate resume-tailoring recommendations from Gap Analysis and JD Intelligence.

This release does **not** rewrite resumes directly. It creates a decision layer that explains what the resume generator should emphasize or de-emphasize for each role.

## Inputs

```text
data/gap-analysis
data/jd-intelligence
data/roles
data/resume-versions/teal-export
```

## Outputs

```text
data/resume-tailoring/
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v046-resume-tailoring
mkdir -p /tmp/career-system-v046-resume-tailoring

unzip ~/Downloads/career-system-v0.4.6-resume-tailoring-intelligence-overlay.zip \
  -d /tmp/career-system-v046-resume-tailoring

cp -R /tmp/career-system-v046-resume-tailoring/* .

chmod +x bin/run-resume-tailoring.sh
chmod +x scripts/generate_resume_tailoring.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-03-resume-tailoring-v1
rm -rf data/resume-tailoring

./bin/run-resume-tailoring.sh \
  run-2026-06-03-resume-tailoring-v1 \
  data/gap-analysis
```

## Review

```bash
find data/resume-tailoring -name 'resume-tailoring-*.md' | wc -l

sed -n '1,260p' data/resume-tailoring/resume-tailoring-pico-sre-2026.md
sed -n '1,260p' data/resume-tailoring/resume-tailoring-citi-support-appsupport-2026.md
sed -n '1,260p' data/resume-tailoring/resume-tailoring-vns-health-support-workday-2026.md
sed -n '1,260p' data/resume-tailoring/resume-tailoring-michael-baker-international-ba-requirements-2026.md
```

## Commit

```bash
git add README_RESUME_TAILORING_INTELLIGENCE.md
git add bin/run-resume-tailoring.sh
git add scripts/generate_resume_tailoring.py
git add docs/standards/resume-tailoring-intelligence-standard.md
git add templates/resume-tailoring-template.md
git add data/resume-tailoring

git commit -m "Add resume tailoring intelligence v0.4.6"
git push

git tag -a v0.4.6-resume-tailoring-intelligence \
  -m "Resume tailoring intelligence complete"

git push origin v0.4.6-resume-tailoring-intelligence
```
