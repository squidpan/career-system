#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <gap_analysis_dir> [jd_intelligence_dir] [roles_dir] [resumes_dir]" >&2
  exit 2
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

RUN_ID="$1"
GAP_DIR="$2"
JD_INTEL_DIR="${3:-data/jd-intelligence}"
ROLES_DIR="${4:-data/roles}"
RESUMES_DIR="${5:-data/resume-versions/teal-export}"

python3 scripts/generate_resume_tailoring.py "$RUN_ID" "$GAP_DIR" "$JD_INTEL_DIR" "$ROLES_DIR" "$RESUMES_DIR"
