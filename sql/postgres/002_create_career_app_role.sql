-- 002_create_career_app_role.sql
-- Run as postgres/admin user.
-- Password should be changed locally before real use.

CREATE ROLE career_app
  WITH LOGIN
  PASSWORD 'career_app_dev_password';

GRANT CONNECT ON DATABASE career_center TO career_app;
