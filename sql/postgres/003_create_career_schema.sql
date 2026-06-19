-- 003_create_career_schema.sql
-- Run against career_center database as postgres/admin user.

CREATE SCHEMA IF NOT EXISTS career AUTHORIZATION career_app;

GRANT USAGE ON SCHEMA career TO career_app;
GRANT CREATE ON SCHEMA career TO career_app;

ALTER ROLE career_app SET search_path TO career, public;
