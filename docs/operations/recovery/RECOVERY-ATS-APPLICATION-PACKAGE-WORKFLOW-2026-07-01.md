# Recovery — ATS Application Package Workflow

Date: 2026-07-01  
Branch: ops/recover-ats-html-workflow  
Status: In Progress

## Problem

The new imported JD pipeline produced intermediate resume artifacts, but the final application package output regressed.

The bad path was:

~~~text
assembled-v2 resume
→ teal-export md
→ application package
~~~

That produced thin resumes, duplicate FRBNY sections, misplaced skills, and incomplete content.

## Confirmed Good Path

The historical LSEG and Broadridge application packages prove the working final-mile path:

~~~text
application-summary.md
+ targeted FRBNY resume section
→ full-resume.md
→ ats-resume.md
→ full-resume.html
→ ats-resume.html
→ ats-resume.txt
→ data/application-packages/application-<job>-2026-v1/
~~~

## Validated Reference Packages

- LSEG Senior BA
- Broadridge Product Analyst

Both were rebuilt safely in /tmp and matched the known-good final outputs after restoring the proven FRBNY section content.

## Current Recovery Conclusion

The final-mile generators still work:

- scripts/assemble_full_resume.py
- scripts/assemble_ats_resume.py
- scripts/export_resume_html.py
- scripts/export_ats_text.py
- scripts/build_application_package.py

The missing bridge is:

~~~text
new pipeline outputs
→ application-summary.md
→ targeted FRBNY resume section
~~~

## Do Not Use As Final

Do not use data/resume-versions/assembled-v2/* or data/resume-versions/teal-export/* directly as application-final resumes.

They are intermediate artifacts only.
