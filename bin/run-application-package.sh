#!/usr/bin/env bash
set -euo pipefail

JOB_SLUG="${1:?Usage: run-application-package.sh <job-slug> <application-id> [input-root] [output-root]}"
APPLICATION_ID="${2:?Usage: run-application-package.sh <job-slug> <application-id> [input-root] [output-root]}"
INPUT_ROOT="${3:-.}"
OUTPUT_ROOT="${4:-.}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3.13 "$ROOT_DIR/scripts/build_application_package.py" \
  "$JOB_SLUG" \
  "$APPLICATION_ID" \
  --input-root "$INPUT_ROOT" \
  --output-root "$OUTPUT_ROOT"
