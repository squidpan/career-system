# ATS Resume Generator v0.7.2

## Goal

Generate ATS-friendly resumes that preserve employer history,
client assignments, dates, and role descriptions.

## Narrative Resume

Example:

Federal Reserve Bank of New York (On-Site via Gresham)

## ATS Resume

Example:

Gresham
Senior Business Analyst / DevOps Release Coordinator
Apr 2017 – Feb 2026 | Federal Reserve Bank of New York | On-site

## Design Rules

Employer = payroll employer

Client = location/context line

Narrative Resume may combine employer and client.

ATS Resume should separate them.

## Outputs

data/full-resumes/*-ats-resume-v1.md
data/full-resumes/*-ats-resume-v1.html

## Supported ATS

- Workday
- SuccessFactors
- Taleo
- Greenhouse
- Lever
- iCIMS
