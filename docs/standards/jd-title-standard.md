# JD Title Standard

## Purpose

Ensure downstream candidate matching and resume tailoring use clean source job titles.

## Precedence

For JD intelligence output, title must be selected in this order:

```text
source_title
normalized_title
title
filename fallback
```

## Why

Some normalized JDs contain body-derived headings in `normalized_title`, such as:

```text
**About The Team
**Location Designation:** Hybrid
Workforce Classification: Telecommuter
```

The `source_title` field is currently the safer source of truth for job identity.

## Validation

Candidate matching reports should not display marketing headings, location headings, or generic JD section headings as role names.
