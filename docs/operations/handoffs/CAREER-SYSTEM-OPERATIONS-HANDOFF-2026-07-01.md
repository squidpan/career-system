# Career System Operations Handoff (2026-07-01)

## Mission

Restore the end-to-end pipeline that produces production-ready
application packages from a Job Description.

## Current Status

-   Proven regression packages: LSEG Senior BA, Broadridge Product
    Analyst.
-   Final-mile generators are validated:
    -   assemble_full_resume.py
    -   assemble_ats_resume.py
    -   export_resume_html.py
    -   export_ats_text.py
    -   build_application_package.py
-   New JD pipeline currently stops before generating
    application-summary and targeted FRBNY section.

## Target Flow

Raw JD -\> Normalized JD -\> Role -\> Resume Version -\> JD Intelligence
-\> Candidate Match -\> Candidate Strategy -\> Candidate Explainability
-\> Resume Tailoring -\> Resume Bullet Ranking -\> Application Summary +
Targeted FRBNY Section -\> ATS Resume -\> Full Resume -\> HTML/TXT -\>
Application Package

## Recovery Rules

-   application-packages is the operational deliverable.
-   Do not use assembled-v2 or teal-export as final resumes.
-   Use LSEG and Broadridge as regression tests.

## Next Sprint

1.  Generate application-summary automatically.
2.  Generate targeted FRBNY section automatically.
3.  Reconnect to existing final-mile generators.
4.  Add regression tests.
