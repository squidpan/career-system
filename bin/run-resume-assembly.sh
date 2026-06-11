#!/usr/bin/env bash
set -euo pipefail

RECOMMENDATION="${1:?Usage: run-resume-assembly.sh <resume-recommendation-json> <resume-section-md> <output-md>}"
SECTION="${2:?Usage: run-resume-assembly.sh <resume-recommendation-json> <resume-section-md> <output-md>}"
OUTPUT="${3:?Usage: run-resume-assembly.sh <resume-recommendation-json> <resume-section-md> <output-md>}"

python3 scripts/assemble_resume.py \
  "$RECOMMENDATION" \
  "$SECTION" \
  "$OUTPUT"
