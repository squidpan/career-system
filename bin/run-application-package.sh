#!/usr/bin/env bash
set -euo pipefail

JOB_SLUG="${1:?Usage: run-application-package.sh <job-slug> <application-id>}"
APPLICATION_ID="${2:?Usage: run-application-package.sh <job-slug> <application-id>}"

python3.13 scripts/build_application_package.py \
  "$JOB_SLUG" \
  "$APPLICATION_ID"
