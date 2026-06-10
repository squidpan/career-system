# Career System Roadmap v0.5.x

## Purpose

Define the v0.5.x roadmap for Experience Source integration, JD matching, scoring, and resume/interview recommendation.

## Completed

### v0.5.0 — Experience Source Domain Model

Defined the domain model for external experience repositories.

### v0.5.1 — MRPrice Experience Metadata

Added MRPrice source registration, asset index, skills index, resume evidence index, interview story index, and keyword map.

### v0.5.2 — Experience Matching Prototype

Added keyword-based experience matching.

### v0.5.3 — JD Experience Matching Prototype

Matched normalized JD files against MRPrice experience metadata.

### v0.5.4 — Experience Scoring Prototype

Ranked matched skills, resume evidence, and interview stories.

## Next

### v0.5.5 — Resume Recommendation Prototype

Goal:

```text
Scored JD Match
    ↓
Top Skills
    ↓
Top Resume Evidence
    ↓
Top Interview Stories
    ↓
Recommendation Output
```

Deliverables:

```text
scripts/recommend_resume_assets.py
bin/run-resume-recommendation.sh
docs/prototypes/resume-recommendation-prototype-v0.5.5.md
data/experience-matches/finbourne-resume-recommendation.json
```

## Later

### v0.5.6 — Interview Recommendation Prototype

Recommend top STAR stories and interview talking points.

### v0.5.7 — Resume Draft Assistance

Use recommended evidence to assist tailored resume generation.

### v0.6.0 — Multi-Source Experience Graph

Support multiple experience sources beyond MRPrice.

## Design Principle

Career System should remain a matcher, router, scorer, and generator.

Experience repositories remain source-of-truth knowledge bases.

