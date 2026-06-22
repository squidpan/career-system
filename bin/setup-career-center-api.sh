#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

SERVICE_DIR="services/career-center-api"
VENV_DIR="${SERVICE_DIR}/.venv"

echo "=================================================="
echo "Career Center API Setup"
echo "=================================================="

python3.13 --version

if [ ! -d "$VENV_DIR" ]; then
    echo
    echo "Creating virtual environment..."
    python3.13 -m venv "$VENV_DIR"
fi

source "${VENV_DIR}/bin/activate"

echo
echo "Upgrading pip..."
pip install --upgrade pip

echo
echo "Installing requirements..."
pip install -r "${SERVICE_DIR}/requirements.txt"

echo
echo "Validating application files..."

test -f "${SERVICE_DIR}/app/main.py"
test -f "${SERVICE_DIR}/requirements.txt"
test -f "${SERVICE_DIR}/openapi/career-center-v1.yaml"

echo
echo "Career Center API setup complete."
