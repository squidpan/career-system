#!/usr/bin/env bash
set -euo pipefail

SUMMARY="${1:?Usage: run-ats-resume-generator.sh <summary-md> <frbny-md> <output-md> <target-name>}"
FRBNY="${2:?Usage: run-ats-resume-generator.sh <summary-md> <frbny-md> <output-md> <target-name>}"
OUTPUT="${3:?Usage: run-ats-resume-generator.sh <summary-md> <frbny-md> <output-md> <target-name>}"
TARGET="${4:?Usage: run-ats-resume-generator.sh <summary-md> <frbny-md> <output-md> <target-name>}"

python3.13 scripts/assemble_ats_resume.py \
  "$SUMMARY" \
  "$FRBNY" \
  "$OUTPUT" \
  "$TARGET"
