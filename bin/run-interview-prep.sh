#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <gap_analysis_dir> [jds_dir] [roles_dir] [resumes_dir] [jd_intelligence_dir]" >&2
  exit 2
fi
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
RUN_ID="$1"
GAP_DIR="$2"
JDS_DIR="${3:-data/jds/normalized}"
ROLES_DIR="${4:-data/roles}"
RESUMES_DIR="${5:-data/resume-versions/teal-export}"
JD_INTEL_DIR="${6:-data/jd-intelligence}"
python3 scripts/generate_interview_prep.py "$RUN_ID" "$GAP_DIR" "$JDS_DIR" "$ROLES_DIR" "$RESUMES_DIR" "$JD_INTEL_DIR"
