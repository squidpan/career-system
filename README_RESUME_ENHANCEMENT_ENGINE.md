# Career System v0.4.8 Resume Enhancement Engine

## Purpose

Generate conservative wording improvements for existing ranked resume bullets.

This release does not overwrite assembled resumes. It creates enhancement reports that compare original bullets to proposed enhanced bullets.

## Inputs

```text
data/resume-bullet-ranking/
data/resume-tailoring/
```

## Output

```text
data/resume-enhancement/
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v048-resume-enhancement
mkdir -p /tmp/career-system-v048-resume-enhancement

unzip ~/Downloads/career-system-v0.4.8-resume-enhancement-engine-overlay.zip \
  -d /tmp/career-system-v048-resume-enhancement

cp -R /tmp/career-system-v048-resume-enhancement/* .

chmod +x bin/run-resume-enhancement.sh
chmod +x scripts/generate_resume_enhancement.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-04-resume-enhancement-v1
rm -rf data/resume-enhancement

./bin/run-resume-enhancement.sh \
  run-2026-06-04-resume-enhancement-v1 \
  data/resume-bullet-ranking
```

## Review

```bash
find data/resume-enhancement -name 'resume-enhancement-*.md' | wc -l

sed -n '1,260p' data/resume-enhancement/resume-enhancement-pico-sre-2026.md
sed -n '1,260p' data/resume-enhancement/resume-enhancement-citi-support-appsupport-2026.md
sed -n '1,260p' data/resume-enhancement/resume-enhancement-vns-health-support-workday-2026.md
sed -n '1,260p' data/resume-enhancement/resume-enhancement-michael-baker-international-ba-requirements-2026.md
```

## Commit

```bash
git add README_RESUME_ENHANCEMENT_ENGINE.md
git add bin/run-resume-enhancement.sh
git add scripts/generate_resume_enhancement.py
git add docs/standards/resume-enhancement-standard.md
git add templates/resume-enhancement-template.md
git add data/resume-enhancement

git commit -m "Add resume enhancement engine v0.4.8"
git push

git tag -a v0.4.8-resume-enhancement-engine \
  -m "Resume enhancement engine complete"

git push origin v0.4.8-resume-enhancement-engine
```
