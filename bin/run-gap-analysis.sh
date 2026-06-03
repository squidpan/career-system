#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <normalized_jds_dir> [roles_dir] [resume_master_dir]" >&2
  exit 2
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

RUN_ID="$1"
JDS_DIR="$2"
ROLES_DIR="${3:-data/roles}"
RESUME_MASTER_DIR="${4:-data/resume-masters}"

python3 scripts/generate_gap_analysis.py "$RUN_ID" "$JDS_DIR" "$ROLES_DIR" "$RESUME_MASTER_DIR"
