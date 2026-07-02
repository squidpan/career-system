# Pipeline Map — JD to Application Package

## Operational Goal

Produce a complete application package under:

~~~text
data/application-packages/application-<job-slug>-2026-v1/
~~~

This is the folder used to apply.

## Final Package Contents

Expected package shape:

~~~text
application-summary.md
ats-resume.html
ats-resume.md
ats-resume.txt
full-resume.html
full-resume.md
interview-recommendation.json
package-manifest.json
README.md
resume-enhanced.md
resume-generated.md
resume-recommendation.json
resume-tailored.md
submission-notes.md
~~~

## Proven Final-Mile Inputs

~~~text
data/application-summaries/<job-slug>-summary-v1.md
data/resume-sections/<job-slug>-frbny-section.md
~~~

## Missing Bridge

The new pipeline does not yet reliably produce:

~~~text
application-summary.md
targeted FRBNY resume section
~~~

That bridge must be restored before generating final packages for new JDs.
