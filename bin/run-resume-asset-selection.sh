#!/usr/bin/env bash
set -euo pipefail

NORMALIZED_JD="${1:?Usage: run-resume-asset-selection.sh <normalized-jd> <job-slug> [output-root]}"
JOB_SLUG="${2:?Usage: run-resume-asset-selection.sh <normalized-jd> <job-slug> [output-root]}"
OUTPUT_ROOT="${3:-.}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3.13 "$ROOT_DIR/scripts/select_resume_assets.py" \
  --normalized-jd "$NORMALIZED_JD" \
  --job-slug "$JOB_SLUG" \
  --output-root "$OUTPUT_ROOT"
