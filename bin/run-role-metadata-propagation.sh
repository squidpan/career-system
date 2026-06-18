#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 scripts/propagate_role_metadata_to_submission_notes.py
