#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

DB_NAME="${CAREER_DB_NAME:-career_center}"
DB_USER="${CAREER_DB_USER:-career_app}"
DB_PASSWORD="${CAREER_DB_PASSWORD:-career_app_dev_password}"

TMP_DIR="/tmp/career-center-postgres-setup"

echo "Setting up Career Center PostgreSQL objects..."
echo "Database: $DB_NAME"
echo "Role:     $DB_USER"
echo

rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"
chmod 755 "$TMP_DIR"

cp sql/postgres/003_create_career_schema.sql "$TMP_DIR/"
cp sql/postgres/004_create_application_tables.sql "$TMP_DIR/"
chmod 644 "$TMP_DIR"/*.sql

echo "Checking database..."
if sudo -u postgres bash -c "cd /tmp && psql -tAc \"SELECT 1 FROM pg_database WHERE datname='${DB_NAME}'\"" | grep -q 1; then
    echo "Database already exists: $DB_NAME"
else
    echo "Creating database: $DB_NAME"
    sudo -u postgres bash -c "cd /tmp && createdb '${DB_NAME}'"
fi

echo
echo "Checking role..."
if sudo -u postgres bash -c "cd /tmp && psql -tAc \"SELECT 1 FROM pg_roles WHERE rolname='${DB_USER}'\"" | grep -q 1; then
    echo "Role already exists: $DB_USER"
else
    echo "Creating role: $DB_USER"
    sudo -u postgres bash -c "cd /tmp && psql -c \"CREATE ROLE ${DB_USER} WITH LOGIN PASSWORD '${DB_PASSWORD}';\""
fi

echo
echo "Granting database access..."
sudo -u postgres bash -c "cd /tmp && psql -c \"GRANT CONNECT ON DATABASE ${DB_NAME} TO ${DB_USER};\""

echo
echo "Creating schema and tables..."
sudo -u postgres bash -c "cd /tmp && psql -d '${DB_NAME}' -f '$TMP_DIR/003_create_career_schema.sql'"
sudo -u postgres bash -c "cd /tmp && psql -d '${DB_NAME}' -f '$TMP_DIR/004_create_application_tables.sql'"

echo
echo "Validating PostgreSQL setup..."
sudo -u postgres bash -c "cd /tmp && psql -c \"\\l ${DB_NAME}\""
sudo -u postgres bash -c "cd /tmp && psql -c \"\\du ${DB_USER}\""
sudo -u postgres bash -c "cd /tmp && psql -d '${DB_NAME}' -c \"\\dn career\""
sudo -u postgres bash -c "cd /tmp && psql -d '${DB_NAME}' -c \"\\dt career.*\""

echo
echo "Career Center PostgreSQL setup complete."
