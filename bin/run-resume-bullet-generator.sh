#!/usr/bin/env bash
set -euo pipefail

RECOMMENDATION="${1:?Usage: run-resume-bullet-generator.sh <resume-recommendation-json> [output-md]}"
OUTPUT="${2:-data/resume-drafts/resume-bullets.md}"

python3 scripts/generate_resume_bullets.py \
  "$RECOMMENDATION" \
  "$OUTPUT"
