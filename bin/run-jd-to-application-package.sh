#!/usr/bin/env bash
set -euo pipefail

NORMALIZED_JD="${1:?Usage: run-jd-to-application-package.sh <normalized-jd> <job-slug> <application-id> [output-root]}"
JOB_SLUG="${2:?Usage: run-jd-to-application-package.sh <normalized-jd> <job-slug> <application-id> [output-root]}"
APPLICATION_ID="${3:?Usage: run-jd-to-application-package.sh <normalized-jd> <job-slug> <application-id> [output-root]}"
OUTPUT_ROOT="${4:-.}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$ROOT_DIR/bin/run-resume-final-mile-from-jd.sh" \
  "$NORMALIZED_JD" \
  "$JOB_SLUG" \
  "$OUTPUT_ROOT"

"$ROOT_DIR/bin/run-application-package.sh" \
  "$JOB_SLUG" \
  "$APPLICATION_ID" \
  "$OUTPUT_ROOT" \
  "$OUTPUT_ROOT"

PACKAGE_DIR="$OUTPUT_ROOT/data/application-packages/$APPLICATION_ID"

echo
echo "JD-to-Application Package workflow complete."
echo "Normalized JD: $NORMALIZED_JD"
echo "Job slug: $JOB_SLUG"
echo "Application ID: $APPLICATION_ID"
echo "Application Package: $PACKAGE_DIR"
