#!/usr/bin/env bash
set -euo pipefail

APPLICATION_ID="${1:?Usage: run-application-package-generator.sh <application-id> <resume-md> <resume-recommendation-json> <interview-recommendation-json> [output-dir]}"
RESUME="${2:?Usage: run-application-package-generator.sh <application-id> <resume-md> <resume-recommendation-json> <interview-recommendation-json> [output-dir]}"
RESUME_RECOMMENDATION="${3:?Usage: run-application-package-generator.sh <application-id> <resume-md> <resume-recommendation-json> <interview-recommendation-json> [output-dir]}"
INTERVIEW_RECOMMENDATION="${4:?Usage: run-application-package-generator.sh <application-id> <resume-md> <resume-recommendation-json> <interview-recommendation-json> [output-dir]}"
OUTPUT_DIR="${5:-data/application-packages}"

python3.13 scripts/generate_application_package.py \
  "$APPLICATION_ID" \
  "$RESUME" \
  "$RESUME_RECOMMENDATION" \
  "$INTERVIEW_RECOMMENDATION" \
  "$OUTPUT_DIR"
