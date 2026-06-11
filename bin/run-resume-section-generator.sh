#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:?Usage: run-resume-section-generator.sh <input-md> <output-md>}"
OUTPUT="${2:?Usage: run-resume-section-generator.sh <input-md> <output-md>}"

python3 scripts/generate_resume_section.py \
  "$INPUT" \
  "$OUTPUT"
