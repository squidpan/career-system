# Regression Tests

## Purpose

Protect the operational Career System workflow used to apply for jobs.

## Critical Workflow

Raw JD → Normalized JD → Resume → ATS HTML → Browser PDF → Application Package

## Required Regression Coverage

- JD normalizer produces stable IDs for known raw JDs.
- Resume pipeline produces expected markdown outputs.
- ATS HTML export produces browser-openable HTML.
- Application package contains ats-resume.html, ats-resume.md, ats-resume.txt, full-resume.html, and package-manifest.json.
- Broad generators do not overwrite unrelated existing artifacts unexpectedly.

## Baseline Rule

Before adding new features, capture a known-good job slug and expected output files.

## Current Recovery Target

Recover one known working application package path first, then freeze it as the first regression fixture.
