# Career System v0.4.1 Resume Master Narrative Cleanup

## Install Overlay

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v041-narrative
mkdir -p /tmp/career-system-v041-narrative

unzip ~/Downloads/career-system-v0.4.1-resume-master-narrative-cleanup-overlay.zip \
  -d /tmp/career-system-v041-narrative

cp -R /tmp/career-system-v041-narrative/* .

chmod +x bin/validate-resume-master-v2.sh
chmod +x scripts/validate_resume_master_v2.py
```

## Validate v2 Masters

```bash
./bin/validate-resume-master-v2.sh
```

Expected:

```text
Narrative master validation PASSED
```

## Review v2 Masters

```bash
sed -n '1,260p' data/resume-masters/master-ba-resume-v2.md
sed -n '1,260p' data/resume-masters/master-sre-resume-v2.md
```

## Promote v2 Masters For Test Run

```bash
mkdir -p backup/resume-masters-before-v041

cp data/resume-masters/master-ba-resume.md \
   backup/resume-masters-before-v041/

cp data/resume-masters/master-sre-resume.md \
   backup/resume-masters-before-v041/

cp data/resume-masters/master-ba-resume-v2.md \
   data/resume-masters/master-ba-resume.md

cp data/resume-masters/master-sre-resume-v2.md \
   data/resume-masters/master-sre-resume.md
```

## Regenerate Downstream Artifacts

```bash
rm -rf ops/runs/run-2026-06-03-resume-assembly-v5
rm -rf data/resume-versions/assembled/*

./bin/run-resume-assembly.sh \
  run-2026-06-03-resume-assembly-v5 \
  data/roles

rm -rf ops/runs/run-2026-06-03-teal-export-v5
rm -rf data/resume-versions/teal-export/*

./bin/run-teal-export.sh \
  run-2026-06-03-teal-export-v5 \
  data/resume-versions/assembled
```

## Review Counts

```bash
find data/resume-versions/assembled -type f | wc -l
find data/resume-versions/teal-export -type f | wc -l
```

Expected:

```text
10
10
```

## Review Test Resumes

```bash
sed -n '1,220p' data/resume-versions/teal-export/resume-citi-support-appsupport-2026-teal-v1.md
sed -n '1,220p' data/resume-versions/teal-export/resume-pico-sre-2026-teal-v1.md
sed -n '1,220p' data/resume-versions/teal-export/resume-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-teal-v1.md
```

## Teal Test

Test these three resumes:

```text
resume-citi-support-appsupport-2026-teal-v1.md
resume-pico-sre-2026-teal-v1.md
resume-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-teal-v1.md
```

Workflow:

```text
Teal Export MD
Obsidian PDF
Teal Import using Overwrite
Teal PDF Export
```

Success criteria:

```text
2 pages preferred
No duplicates
Strong narrative
No Certifications / Learning REST APIs
No Publications overflow
```

## Git Add

```bash
git add README_RESUME_MASTER_NARRATIVE_CLEANUP.md
git add docs/design/resume-master-v2.md
git add docs/standards/resume-master-narrative-standard.md
git add data/resume-masters/master-ba-resume-v2.md
git add data/resume-masters/master-sre-resume-v2.md
git add bin/validate-resume-master-v2.sh
git add scripts/validate_resume_master_v2.py
git add data/resume-masters/master-ba-resume.md
git add data/resume-masters/master-sre-resume.md
git add data/resume-versions/assembled
git add data/resume-versions/teal-export
```

## Commit

```bash
git commit -m "Refactor resume masters into narrative structure v0.4.1"
git push
```

## Tag

```bash
git tag -a v0.4.1-resume-master-cleanup \
  -m "Resume master narrative cleanup complete"

git push origin v0.4.1-resume-master-cleanup
```

## Rollback

```bash
cp backup/resume-masters-before-v041/master-ba-resume.md \
   data/resume-masters/master-ba-resume.md

cp backup/resume-masters-before-v041/master-sre-resume.md \
   data/resume-masters/master-sre-resume.md
```
