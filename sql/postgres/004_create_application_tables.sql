-- 004_create_application_tables.sql
-- Run against career_center database.
-- Creates first Career Center application tracking tables.

CREATE TABLE IF NOT EXISTS career.job_application (
    application_id           text PRIMARY KEY,
    company                  text,
    role                     text,
    role_id                  text,
    role_code                text,
    role_family              text,
    status                   text,
    date_applied             date,
    last_update              date,
    source                   text,
    location                 text,
    employment_type          text,
    resumes                  text,
    cover_letters            text,
    normalized_jd_file       text,
    raw_jd_file              text,
    final_resume_file        text,
    application_package_path text,
    notes                    text,
    created_at               timestamptz NOT NULL DEFAULT now(),
    updated_at               timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS career.job_description (
    jd_id                    bigserial PRIMARY KEY,
    application_id           text NOT NULL REFERENCES career.job_application(application_id) ON DELETE CASCADE,
    jd_type                  text NOT NULL,
    file_path                text NOT NULL,
    content_text             text,
    created_at               timestamptz NOT NULL DEFAULT now(),
    UNIQUE (application_id, jd_type)
);

CREATE TABLE IF NOT EXISTS career.application_artifact (
    artifact_id              bigserial PRIMARY KEY,
    application_id           text NOT NULL REFERENCES career.job_application(application_id) ON DELETE CASCADE,
    artifact_type            text NOT NULL,
    file_path                text NOT NULL,
    content_text             text,
    created_at               timestamptz NOT NULL DEFAULT now(),
    UNIQUE (application_id, artifact_type)
);

CREATE INDEX IF NOT EXISTS idx_job_application_status
    ON career.job_application(status);

CREATE INDEX IF NOT EXISTS idx_job_application_role_code
    ON career.job_application(role_code);

CREATE INDEX IF NOT EXISTS idx_job_description_application_id
    ON career.job_description(application_id);

CREATE INDEX IF NOT EXISTS idx_application_artifact_application_id
    ON career.application_artifact(application_id);
