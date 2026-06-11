#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:?Usage: run-resume-tailor.sh <input-md> <target> <output-md>}"
TARGET="${2:?Usage: run-resume-tailor.sh <input-md> <target> <output-md>}"
OUTPUT="${3:?Usage: run-resume-tailor.sh <input-md> <target> <output-md>}"

python3 scripts/tailor_resume.py \
  "$INPUT" \
  "$TARGET" \
  "$OUTPUT"
