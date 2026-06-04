# Career System v0.4.9 Resume Narrative Assembly

## Purpose

Generate `assembled-v3` resumes by combining employer-aware assembled-v2 resumes with resume enhancement reports.

This release does not enforce a two-page resume. It improves final resume flow by applying conservative enhanced wording and limiting lower-priority bullets.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v049-resume-narrative
mkdir -p /tmp/career-system-v049-resume-narrative

unzip ~/Downloads/career-system-v0.4.9-resume-narrative-assembly-overlay.zip \
  -d /tmp/career-system-v049-resume-narrative

cp -R /tmp/career-system-v049-resume-narrative/* .

chmod +x bin/run-resume-narrative-assembly.sh
chmod +x scripts/assemble_resume_narratives.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-05-resume-narrative-assembly-v1
rm -rf data/resume-versions/assembled-v3

./bin/run-resume-narrative-assembly.sh \
  run-2026-06-05-resume-narrative-assembly-v1 \
  data/resume-versions/assembled-v2
```

## Review

```bash
find data/resume-versions/assembled-v3 -name 'resume-*-assembled-v3.md' | wc -l

sed -n '1,260p' data/resume-versions/assembled-v3/resume-pico-sre-2026-assembled-v3.md
sed -n '1,260p' data/resume-versions/assembled-v3/resume-citi-support-appsupport-2026-assembled-v3.md
sed -n '1,260p' data/resume-versions/assembled-v3/resume-vns-health-support-workday-2026-assembled-v3.md
sed -n '1,260p' data/resume-versions/assembled-v3/resume-michael-baker-international-ba-requirements-2026-assembled-v3.md
```

## Commit

```bash
git add README_RESUME_NARRATIVE_ASSEMBLY.md
git add bin/run-resume-narrative-assembly.sh
git add scripts/assemble_resume_narratives.py
git add docs/standards/resume-narrative-assembly-standard.md
git add templates/resume-narrative-assembly-template.md
git add data/resume-versions/assembled-v3

git commit -m "Add resume narrative assembly v0.4.9"
git push

git tag -a v0.4.9-resume-narrative-assembly \
  -m "Resume narrative assembly complete"

git push origin v0.4.9-resume-narrative-assembly
```
