#!/usr/bin/env bash
set -euo pipefail

NORMALIZED_JD="${1:?Usage: run-resume-final-mile-from-jd.sh <normalized-jd> <job-slug> [output-root]}"
JOB_SLUG="${2:?Usage: run-resume-final-mile-from-jd.sh <normalized-jd> <job-slug> [output-root]}"
OUTPUT_ROOT="${3:-.}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SUMMARY_DIR="$OUTPUT_ROOT/data/application-summaries"
SECTION_DIR="$OUTPUT_ROOT/data/resume-sections"
FULL_DIR="$OUTPUT_ROOT/data/full-resumes"
ATS_DIR="$OUTPUT_ROOT/data/ats-exports"

SUMMARY="$SUMMARY_DIR/${JOB_SLUG}-summary-v1.md"
FRBNY="$SECTION_DIR/${JOB_SLUG}-frbny-section.md"
FULL_MD="$FULL_DIR/${JOB_SLUG}-full-resume-v1.md"
FULL_HTML="$FULL_DIR/${JOB_SLUG}-full-resume-v1.html"
ATS_MD="$FULL_DIR/${JOB_SLUG}-ats-resume-v1.md"
ATS_HTML="$FULL_DIR/${JOB_SLUG}-ats-resume-v1.html"
ATS_TXT="$ATS_DIR/${JOB_SLUG}-ats-resume-v1.txt"

mkdir -p \
  "$SUMMARY_DIR" \
  "$SECTION_DIR" \
  "$FULL_DIR" \
  "$ATS_DIR"

"$ROOT_DIR/bin/run-resume-asset-selection.sh" \
  "$NORMALIZED_JD" \
  "$JOB_SLUG" \
  "$OUTPUT_ROOT"

"$ROOT_DIR/bin/run-full-resume-generator.sh" \
  "$SUMMARY" \
  "$FRBNY" \
  "$FULL_MD" \
  "$JOB_SLUG"

"$ROOT_DIR/bin/run-ats-resume-generator.sh" \
  "$SUMMARY" \
  "$FRBNY" \
  "$ATS_MD" \
  "$JOB_SLUG"

"$ROOT_DIR/bin/run-resume-html-export.sh" \
  "$FULL_MD" \
  "$FULL_HTML"

"$ROOT_DIR/bin/run-resume-html-export.sh" \
  "$ATS_MD" \
  "$ATS_HTML"

"$ROOT_DIR/bin/run-ats-text-export.sh" \
  "$ATS_MD" \
  "$ATS_TXT"

echo
echo "Final-mile resume generation complete."
echo "Job slug: $JOB_SLUG"
echo "Output root: $OUTPUT_ROOT"
echo "Full resume: $FULL_MD"
echo "ATS resume: $ATS_MD"
echo "ATS text: $ATS_TXT"
