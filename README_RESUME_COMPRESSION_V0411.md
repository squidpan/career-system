# Career System v0.4.1.1 Resume Compression Cleanup

## Purpose

Compress the v0.4.1 narrative master resumes toward a practical two-page Teal export target.

This is a content-only release. It does not change the JD pipeline, role pipeline, resume assembly engine, or Teal export engine.

## What Changed

- Reduced Core Competencies duplication against Skills.
- Compressed Gresham/FRBNY bullets from 10 to 8 for BA and 9 for SRE.
- Compressed Financial Data bullets.
- Merged Governance and Engineering sections in the BA master.
- Tightened SRE support language while preserving production support, runbooks, incident coordination, Linux, Oracle, AWS, REST, and financial data themes.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v0411-compression
mkdir -p /tmp/career-system-v0411-compression

unzip ~/Downloads/career-system-v0.4.1.1-resume-compression-cleanup-overlay.zip   -d /tmp/career-system-v0411-compression

cp -R /tmp/career-system-v0411-compression/* .

chmod +x bin/validate-resume-compression-v2.sh
chmod +x scripts/validate_resume_compression_v2.py
```

## Validate

```bash
./bin/validate-resume-master-v2.sh
./bin/validate-resume-compression-v2.sh
```

Expected:

```text
Narrative master validation PASSED
Resume compression v2 validation PASSED
```

## Regenerate

```bash
rm -rf ops/runs/run-2026-06-03-resume-assembly-v6
rm -rf data/resume-versions/assembled/*

./bin/run-resume-assembly.sh   run-2026-06-03-resume-assembly-v6   data/roles

rm -rf ops/runs/run-2026-06-03-teal-export-v7
rm -rf data/resume-versions/teal-export/*

./bin/run-teal-export.sh   run-2026-06-03-teal-export-v7   data/resume-versions/assembled
```

## Review

```bash
find data/resume-versions/assembled -type f | wc -l
find data/resume-versions/teal-export -type f | wc -l

sed -n '1,220p' data/resume-versions/teal-export/resume-citi-support-appsupport-2026-teal-v1.md
sed -n '1,220p' data/resume-versions/teal-export/resume-pico-sre-2026-teal-v1.md
```

## Teal Test

Test:

```text
resume-citi-support-appsupport-2026-teal-v1.md
resume-pico-sre-2026-teal-v1.md
```

Use:

```text
Teal Import -> Overwrite -> Export PDF
```

Success criteria:

```text
Citi: closer to 2 pages
Pico: stays 2 pages
No duplicate sections
No Publications overflow
No Learning REST APIs
```

## Git Add

```bash
git add README_RESUME_COMPRESSION_V0411.md
git add docs/standards/resume-compression-v2-standard.md
git add data/resume-masters/master-ba-resume.md
git add data/resume-masters/master-sre-resume.md
git add data/resume-masters/master-ba-resume-v2.md
git add data/resume-masters/master-sre-resume-v2.md
git add bin/validate-resume-compression-v2.sh
git add scripts/validate_resume_compression_v2.py
git add data/resume-versions/assembled
git add data/resume-versions/teal-export
```

## Commit

```bash
git commit -m "Compress narrative resume masters v0.4.1.1"
git push
```

## Tag

```bash
git tag -a v0.4.1.1-resume-compression   -m "Resume compression cleanup complete"

git push origin v0.4.1.1-resume-compression
```

## Rollback

```bash
git restore data/resume-masters/master-ba-resume.md
git restore data/resume-masters/master-sre-resume.md
git restore data/resume-masters/master-ba-resume-v2.md
git restore data/resume-masters/master-sre-resume-v2.md
git restore data/resume-versions/assembled
git restore data/resume-versions/teal-export
```
