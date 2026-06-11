#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:?Usage: run-resume-quality-enhancer.sh <input-md> <target> <output-md>}"
TARGET="${2:?Usage: run-resume-quality-enhancer.sh <input-md> <target> <output-md>}"
OUTPUT="${3:?Usage: run-resume-quality-enhancer.sh <input-md> <target> <output-md>}"

python3.13 scripts/enhance_resume_quality.py \
  "$INPUT" \
  "$TARGET" \
  "$OUTPUT"
