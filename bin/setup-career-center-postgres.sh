#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Setting up Career Center PostgreSQL objects..."

TMP_DIR="/tmp/career-center-postgres-setup"
rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"
chmod 755 "$TMP_DIR"

cp sql/postgres/001_create_career_center_database.sql "$TMP_DIR/"
cp sql/postgres/002_create_career_app_role.sql "$TMP_DIR/"
cp sql/postgres/003_create_career_schema.sql "$TMP_DIR/"
cp sql/postgres/004_create_application_tables.sql "$TMP_DIR/"
chmod 644 "$TMP_DIR"/*.sql

sudo -u postgres bash -c "cd /tmp && psql -f '$TMP_DIR/001_create_career_center_database.sql'"
sudo -u postgres bash -c "cd /tmp && psql -f '$TMP_DIR/002_create_career_app_role.sql'"
sudo -u postgres bash -c "cd /tmp && psql -d career_center -f '$TMP_DIR/003_create_career_schema.sql'"
sudo -u postgres bash -c "cd /tmp && psql -d career_center -f '$TMP_DIR/004_create_application_tables.sql'"

echo
echo "Validating PostgreSQL setup..."

sudo -u postgres psql -c "\l career_center"
sudo -u postgres psql -c "\du career_app"
sudo -u postgres psql -d career_center -c "\dn career"
sudo -u postgres psql -d career_center -c "\dt career.*"

echo
echo "Career Center PostgreSQL setup complete."
