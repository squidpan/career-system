#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <resume_tailoring_dir> [resumes_dir]" >&2
  exit 2
fi
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
RUN_ID="$1"
TAILORING_DIR="$2"
RESUMES_DIR="${3:-data/resume-versions/teal-export}"
python3 scripts/generate_resume_bullet_ranking.py "$RUN_ID" "$TAILORING_DIR" "$RESUMES_DIR"
