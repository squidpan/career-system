#!/usr/bin/env bash
set -euo pipefail

OUTPUT="${1:-data/master-resumes/master-resume-v1.md}"

python3 scripts/generate_master_resume.py \
  data/experience-skills/mrprice-skills.json \
  data/resume-evidence/mrprice-resume-evidence-index.json \
  data/interview-stories/mrprice-interview-stories-index.json \
  "$OUTPUT"
