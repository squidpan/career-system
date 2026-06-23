#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

SERVICE_DIR="services/career-center-api"
VENV_DIR="${SERVICE_DIR}/.venv"

echo "Starting Career Center API..."

if [ ! -d "$VENV_DIR" ]; then
    echo "ERROR: Missing virtual environment: $VENV_DIR"
    echo "Run: ./bin/setup-career-center-api.sh"
    exit 1
fi

if [ -z "${CAREER_DB_PASSWORD:-}" ]; then
    echo "ERROR: CAREER_DB_PASSWORD is not set"
    echo "Example:"
    echo "  CAREER_DB_PASSWORD='career_app_dev_password' ./bin/run-career-center-api.sh"
    exit 1
fi

test -f "${SERVICE_DIR}/app/main.py" || {
    echo "ERROR: Missing ${SERVICE_DIR}/app/main.py"
    exit 1
}

test -f "${SERVICE_DIR}/requirements.txt" || {
    echo "ERROR: Missing ${SERVICE_DIR}/requirements.txt"
    exit 1
}

source "${VENV_DIR}/bin/activate"

cd "$SERVICE_DIR"

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
