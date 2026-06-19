# Career Center PostgreSQL Setup

## Purpose

Create the local PostgreSQL database foundation for Career System / Motorweb Career Center.

## Approved Local Environment

- PostgreSQL: 14.23
- Cluster: 14/main
- Port: 5432
- Access: localhost only
- Database: career_center
- Application role: career_app
- Application schema: career

## Setup Order

Run as PostgreSQL admin user:

```bash
sudo -u postgres psql -f sql/postgres/001_create_career_center_database.sql
sudo -u postgres psql -f sql/postgres/002_create_career_app_role.sql
sudo -u postgres psql -d career_center -f sql/postgres/003_create_career_schema.sql
