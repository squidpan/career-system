#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../services/career-center-api"

source .venv/bin/activate

export CAREER_DB_HOST="${CAREER_DB_HOST:-localhost}"
export CAREER_DB_NAME="${CAREER_DB_NAME:-career_center}"
export CAREER_DB_USER="${CAREER_DB_USER:-career_app}"

python -m uvicorn app.main:app --reload
