#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <gap_analysis_dir> [jds_dir] [roles_dir] [resumes_dir]" >&2
  exit 2
fi
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
python3 scripts/generate_interview_prep.py "$1" "$2" "${3:-data/jds/normalized}" "${4:-data/roles}" "${5:-data/resume-versions/teal-export}"
