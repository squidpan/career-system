# Career System Release Process

## Purpose

Provide a repeatable process for creating, validating, tagging, and deploying Career System releases.

## Release Workflow

Requirements Complete
→ Sprint Closeout
→ Smoke Test Validation
→ Release Notes
→ Git Tag
→ Push Tag
→ Ted Deployment Validation
→ Operate
→ Collect Findings
→ Next Sprint

## Pre-Release Checklist

* All sprint stories updated
* Acceptance criteria validated
* Working tree clean
* Smoke tests pass
* Release notes created

## Release Notes

Create:

docs/releases/RELEASE-<version>.md

Document:

* Features completed
* Deployment changes
* Known issues
* Follow-up work

## Tag Creation

Example:

git tag -a v0.11.1-deployment-prep 
-m "Deployment automation foundation"

git push origin v0.11.1-deployment-prep

## Ted Validation

Validate:

* Repository clone
* Python environment setup
* PostgreSQL connectivity
* Data loading
* API startup
* Smoke test suite

## Rollback

Checkout previous tag:

git checkout <tag>

Recreate environment as needed.

## Lessons Learned

Capture deployment findings and operational issues before beginning the next sprint.

