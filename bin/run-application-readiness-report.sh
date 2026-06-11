#!/usr/bin/env bash
set -euo pipefail

PACKAGE_DIR="${1:?Usage: run-application-readiness-report.sh <application-package-dir> [output-md]}"
OUTPUT="${2:-$PACKAGE_DIR/application-readiness-report.md}"

python3.13 scripts/generate_application_readiness_report.py \
  "$PACKAGE_DIR" \
  "$OUTPUT"
