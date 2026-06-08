# Career System v0.8.0 — Resume Tailoring Engine

## Purpose

Generate resume-tailoring guidance from candidate explainability artifacts.

v0.7.0 answers:

```text
Why should Paul pursue this role?
```

v0.8.0 answers:

```text
How should Paul's resume be tailored for this role?
```

## Inputs

```text
data/candidate-explainability/*.json
```

## Outputs

```text
data/resume-tailoring/
  resume-tailor-*.md
  resume-tailor-*.json
  resume-tailoring-report-*.md
  resume-tailoring-report-*.json
```

## Install Overlay

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v080-resume-tailoring
mkdir -p /tmp/career-system-v080-resume-tailoring

unzip ~/Downloads/career-system-v0.8.0-resume-tailoring-engine-overlay.zip \
  -d /tmp/career-system-v080-resume-tailoring

cp -R /tmp/career-system-v080-resume-tailoring/* .

chmod +x bin/run-resume-tailoring.sh
chmod +x scripts/generate_resume_tailoring.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-08-resume-tailoring-v1
rm -rf data/resume-tailoring

./bin/run-resume-tailoring.sh \
  run-2026-06-08-resume-tailoring-v1 \
  data/candidate-explainability
```

## Validate

```bash
find data/resume-tailoring -name 'resume-tailor-*.md' | wc -l

sed -n '1,260p' \
  data/resume-tailoring/resume-tailoring-report-run-2026-06-08-resume-tailoring-v1.md

sed -n '1,260p' \
  data/resume-tailoring/resume-tailor-dow-jones-ba-ai-2026.md

sed -n '1,260p' \
  data/resume-tailoring/resume-tailor-citi-support-appsupport-2026.md
```

Expected:

```text
27 tailoring files
1 tailoring report
per-role resume family, summary direction, bullets to emphasize, bullets to avoid, keywords, and cover/interview guidance
```

## Git Commit

After review:

```bash
git add README_RESUME_TAILORING_ENGINE.md
git add bin/run-resume-tailoring.sh
git add scripts/generate_resume_tailoring.py
git add docs/standards/resume-tailoring-standard.md
git add templates/resume-tailoring-template.md
git add data/resume-tailoring

git commit -m "Add resume tailoring engine v0.8.0"

git push

git tag -a v0.8.0-resume-tailoring-engine \
  -m "Resume tailoring engine complete"

git push origin v0.8.0-resume-tailoring-engine
```

## Notes

This release produces tailoring guidance, not final resumes. Final resume assembly should come later after the guidance layer is validated.
