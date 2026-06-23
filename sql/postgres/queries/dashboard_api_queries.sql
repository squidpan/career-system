-- dashboard_api_queries.sql
-- Reference SQL for Career Center dashboard REST endpoints.
--
-- Purpose:
-- Keep SQL dashboard behavior traceable to FastAPI dashboard endpoints.
--
-- Related endpoints:
--   GET /dashboard/summary
--   GET /dashboard/statuses
--   GET /dashboard/roles
--   GET /dashboard/recent

-- ============================================================
-- GET /dashboard/summary
-- Total application count
-- ============================================================

select count(*) as application_count
from career.job_application;

-- ============================================================
-- GET /dashboard/statuses
-- Application counts by status
-- ============================================================

select
    status,
    count(*) as application_count
from career.job_application
group by status
order by status;

-- ============================================================
-- GET /dashboard/roles
-- Application counts by role code
-- ============================================================

select
    role_code,
    count(*) as application_count
from career.job_application
group by role_code
order by role_code;

-- ============================================================
-- GET /dashboard/recent
-- Recent applications
-- ============================================================

select
    application_id,
    company,
    role,
    status,
    last_update,
    role_code
from career.job_application
order by last_update desc nulls last, company
limit 10;
