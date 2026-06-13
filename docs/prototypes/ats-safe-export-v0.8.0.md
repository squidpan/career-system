# ATS-Safe Export v0.8.0

## Purpose

Generate ATS-safe resume formats for job sites that fail to parse browser-generated PDFs.

## Problem Found

Citi application site could not parse the browser-generated PDF resume. The application was still submitted, but future applications need safer upload formats.

## Outputs

- Plain text resume
- Simple markdown resume
- Later: DOCX resume

## Design Rule

Use simple employer-based structure:

Employer
Title
Dates | Client / Location
Bullets

Avoid complex HTML, CSS, browser PDF rendering, tables, columns, and icons.
