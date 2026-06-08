# Candidate Matching Standard

## Purpose

Candidate matching ranks available jobs against Paul's current experience, constraints, and practical job-search strategy.

## Input Contract

The engine consumes JD intelligence JSON files from:

```text
data/jd-intelligence/
```

Each file may contain different field names depending on prior release output. The engine must be resilient and extract useful text from all available JSON fields.

## Output Contract

Each candidate match file must include:

- company
- title
- role_code
- match_score
- recommendation
- resume_family
- strengths
- gaps
- tailoring_focus
- next_action

## Recommendation Bands

- `apply_now`: strong fit; tailor and apply first
- `apply_selectively`: good fit; apply when role is attractive or local/benefits are strong
- `possible_but_tailor_carefully`: plausible but gaps require careful positioning
- `deprioritize`: weak fit or role direction is less strategic

## Truthfulness Rules

- Do not imply hands-on experience the candidate does not have.
- Treat Python as learning/ramp-up unless separately supported.
- Treat AI usage as AI-assisted BA/knowledge workflow experience, not AI engineering.
- Treat Workday, GIS, and deep product/platform ownership as transferable only unless directly supported.

## Current Target Personas

The current job-search taxonomy uses these broad personas:

- `ba`
- `support`
- `ops`
- `sre`

More detailed title differences should be retained in metadata and tailoring notes.
