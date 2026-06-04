# Career System v0.4.7.1 Employer-Aware Resume Assembly

## Purpose

Improve v0.4.7 by assembling resumes into real employer-based experience blocks instead of internal narrative groups.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v0471-employer-aware
mkdir -p /tmp/career-system-v0471-employer-aware

unzip ~/Downloads/career-system-v0.4.7.1-employer-aware-resume-assembly-overlay.zip \
  -d /tmp/career-system-v0471-employer-aware

cp -R /tmp/career-system-v0471-employer-aware/* .

chmod +x bin/run-role-aware-resume-assembly.sh
chmod +x scripts/assemble_role_aware_resumes.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-04-employer-aware-resume-assembly-v1
rm -rf data/resume-versions/assembled-v2

./bin/run-role-aware-resume-assembly.sh \
  run-2026-06-04-employer-aware-resume-assembly-v1 \
  data/resume-bullet-ranking
```

## Review

```bash
find data/resume-versions/assembled-v2 -name 'resume-*-assembled-v2.md' | wc -l

sed -n '1,260p' data/resume-versions/assembled-v2/resume-pico-sre-2026-assembled-v2.md
sed -n '1,260p' data/resume-versions/assembled-v2/resume-citi-support-appsupport-2026-assembled-v2.md
sed -n '1,260p' data/resume-versions/assembled-v2/resume-vns-health-support-workday-2026-assembled-v2.md
sed -n '1,260p' data/resume-versions/assembled-v2/resume-michael-baker-international-ba-requirements-2026-assembled-v2.md

grep -R "Financial Services Production Support" -n data/resume-versions/assembled-v2 || true
grep -R "Enterprise Business Systems Support" -n data/resume-versions/assembled-v2 || true
```

## Commit

```bash
git add README_EMPLOYER_AWARE_RESUME_ASSEMBLY.md
git add bin/run-role-aware-resume-assembly.sh
git add scripts/assemble_role_aware_resumes.py
git add docs/standards/employer-aware-resume-assembly-standard.md
git add templates/employer-aware-assembled-resume-template.md
git add data/resume-versions/assembled-v2

git commit -m "Add employer-aware resume assembly v0.4.7.1"
git push

git tag -a v0.4.7.1-employer-aware-resume-assembly \
  -m "Employer-aware resume assembly complete"

git push origin v0.4.7.1-employer-aware-resume-assembly
```
