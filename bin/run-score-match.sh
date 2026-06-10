#!/usr/bin/env bash
set -euo pipefail

MATCH_FILE="${1:?Usage: run-score-match.sh <match-json> [output-json]}"
OUTPUT_FILE="${2:-data/experience-matches/scored-match.json}"

python3 scripts/score_experience_match.py \
  "$MATCH_FILE" \
  data/experience-skills/mrprice-skills.json \
  data/resume-evidence/mrprice-resume-evidence-index.json \
  data/interview-stories/mrprice-interview-stories-index.json \
  | tee "$OUTPUT_FILE"
