#!/usr/bin/env bash
set -euo pipefail

SUMMARY="${1:?Usage: run-full-resume-generator.sh <summary-md> <frbny-resume-final-md> <output-md> <target-name>}"
FRBNY_FINAL="${2:?Usage: run-full-resume-generator.sh <summary-md> <frbny-resume-final-md> <output-md> <target-name>}"
OUTPUT="${3:?Usage: run-full-resume-generator.sh <summary-md> <frbny-resume-final-md> <output-md> <target-name>}"
TARGET="${4:?Usage: run-full-resume-generator.sh <summary-md> <frbny-resume-final-md> <output-md> <target-name>}"

python3.13 scripts/assemble_full_resume.py \
  "$SUMMARY" \
  "$FRBNY_FINAL" \
  "$OUTPUT" \
  "$TARGET"
