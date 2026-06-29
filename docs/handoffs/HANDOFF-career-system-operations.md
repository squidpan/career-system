# HANDOFF — Career System Operations

## Purpose

Keep Career System operational for applying to jobs.

## Current Priority

Recover reliable ATS HTML workflow:

Raw JD → normalized JD → resume → ATS HTML → browser PDF → application package.

## Current Repo State

Branch: main  
Latest known good main: 3199fec  
Current issue: new normalized JDs exist, but ATS HTML/application package generation workflow is not currently one reliable command.

## Do Not Touch In This Chat

- EKF architecture
- Motorweb API design
- PostgreSQL schema changes unless needed for application tracker
- Large refactors

## Important Tags

- v0.7.2-ats-resume-generator
- v0.8.0-ats-safe-export
- v0.9.0-application-package-generator
- v0.13.0-api-contract-hardening

## Immediate Diagnostic Commands

```bash
git status
git log --oneline --decorate --graph -20
find data/application-packages -type f -name "ats-resume.html" | sort
find data/full-resumes -type f -name "*ats-resume-v1.html" | sort
cat bin/run-application-package.sh
cat scripts/build_application_package.py
cat bin/run-ats-resume-generator.sh
cat bin/run-resume-html-export.sh
