-- Application Dashboard SQL Queries
-- Run against career_center.

-- 1. Application count
select count(*) as application_count
from career.job_application;

-- 2. Applications by status
select status, count(*) as count
from career.job_application
group by status
order by status;

-- 3. Applications by role code
select role_code, count(*) as count
from career.job_application
group by role_code
order by role_code;

-- 4. Application dashboard summary
select
    company,
    role,
    status,
    date_applied,
    last_update,
    role_code,
    source
from career.job_application
order by last_update desc nulls last, company;

-- 5. Applications missing final resume
select
    company,
    role,
    status,
    final_resume_file
from career.job_application
where final_resume_file is null
   or final_resume_file = ''
order by company;

-- 6. Application detail
select *
from career.job_application
where application_id = 'application-broadridge-product-analyst-2026-v1';

-- 7. JD text by application
select
    a.company,
    a.role,
    jd.jd_type,
    jd.file_path,
    length(jd.content_text) as content_length,
    left(jd.content_text, 500) as preview
from career.job_application a
join career.job_description jd
  on jd.application_id = a.application_id
where a.application_id = 'application-broadridge-product-analyst-2026-v1'
order by jd.jd_type;

-- 8. Artifacts by application
select
    a.company,
    a.role,
    ar.artifact_type,
    ar.file_path,
    length(ar.content_text) as content_length,
    left(ar.content_text, 500) as preview
from career.job_application a
join career.application_artifact ar
  on ar.application_id = a.application_id
where a.application_id = 'application-broadridge-product-analyst-2026-v1'
order by ar.artifact_type;
