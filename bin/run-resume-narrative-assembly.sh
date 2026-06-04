#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <assembled_v2_dir> [resume_enhancement_dir]" >&2
  exit 2
fi
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
python3 scripts/assemble_resume_narratives.py "$1" "$2" "${3:-data/resume-enhancement}"
