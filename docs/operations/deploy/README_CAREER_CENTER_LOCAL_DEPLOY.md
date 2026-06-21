# Career Center Local Deployment Guide

## Purpose

Deploy Career Center from a clean git clone to a fully operational local environment.

## Prerequisites

### Operating System

* Pop!_OS 22.04 LTS

### Software

* PostgreSQL 14+
* Python 3.13
* Git

### Access

* sudo privileges
* PostgreSQL superuser access

---

## Step 1 — Clone Repository

```bash
git clone git@github-squidpan:squidpan/career-system.git
cd career-system
```

---

## Step 2 — Create PostgreSQL Database

Run:

```bash
sql/postgres/001_create_career_center_database.sql
sql/postgres/002_create_career_app_role.sql
sql/postgres/003_create_career_schema.sql
sql/postgres/004_create_application_tables.sql
```

Verify:

```bash
psql -h localhost -U career_app -d career_center
```

---

## Step 3 — Load Application Data

```bash
PGPASSWORD='<password>' \
./bin/load-applications-to-postgres.sh
```

Verify:

```sql
select count(*) from career.job_application;
```

---

## Step 4 — Load Application Artifacts

```bash
PGPASSWORD='<password>' \
./bin/load-application-artifacts-to-postgres.sh
```

Verify:

```sql
select count(*) from career.job_description;
select count(*) from career.application_artifact;
```

---

## Step 5 — Start API

```bash
CAREER_DB_PASSWORD='<password>' \
./bin/run-career-center-api.sh
```

Verify:

```bash
curl http://127.0.0.1:8000/health
```

---

## Step 6 — Run Smoke Tests

```bash
./bin/smoke-test-career-center-api.sh
```

Expected:

PASS for all endpoints.

---

## Troubleshooting

### Connection Refused

Verify API process running.

### Authentication Failed

Verify career_app password.

### Missing Tables

Re-run schema scripts.

---

## Validation Checklist

* Database created
* Schema created
* Tables created
* Applications loaded
* Artifacts loaded
* API running
* Smoke tests passed

Deployment complete.

