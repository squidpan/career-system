# Experience Source Domain Model

## Purpose

This document defines the Career System domain model for external experience repositories.

Experience Sources allow Career System to use structured professional experience as evidence for:

* JD analysis
* candidate matching
* resume tailoring
* resume generation
* interview preparation
* skill extraction

The first implemented Experience Source is:

```text
mrprice-experience-intelligence
```

---

# Design Principle

Career System should not copy the full contents of external experience repositories.

Instead, Career System should maintain structured references, indexes, summaries, and mappings that point to the source repository.

```text
Experience Repository
        ↓
Career System Index
        ↓
JD Matching
        ↓
Resume Evidence
        ↓
Resume / Interview Output
```

This keeps responsibilities clean:

```text
mrprice-experience-intelligence
    = source knowledge

career-system
    = matching, scoring, tailoring, generation
```

---

# Core Domain Objects

## 1. ExperienceSource

Represents an external repository or knowledge source containing structured professional experience.

### Fields

```text
source_id
name
source_type
repository_name
repository_path
repository_url
branch
release
status
domains
primary_assets
notes
```

### Example

```json
{
  "source_id": "mrprice",
  "name": "MRPrice Experience Intelligence",
  "source_type": "experience_repository",
  "repository_name": "mrprice-experience-intelligence",
  "branch": "main",
  "release": "v0.4.1",
  "status": "active"
}
```

---

## 2. ExperienceAsset

Represents a specific reusable asset inside an Experience Source.

Examples:

* Resume evidence file
* STAR story file
* Interview bank
* Skills mapping
* Architecture note
* Diagram
* Deep architecture note

### Fields

```text
asset_id
source_id
asset_type
title
path
tags
domains
role_families
skill_ids
priority
status
```

### Asset Types

```text
architecture_note
deep_architecture_note
resume_evidence
star_story
interview_bank
skills_mapping
career_system_mapping
diagram
```

---

## 3. ExperienceSkill

Represents a skill derived from an Experience Source.

Examples:

* Market Data
* Vendor Normalization
* Tick Consolidation
* Oracle Distribution
* REST API Validation
* Production Support
* Four-Eyes Governance

### Fields

```text
skill_id
source_id
name
category
description
evidence_assets
jd_keywords
resume_families
confidence
status
```

---

## 4. ResumeEvidence

Represents reusable resume material derived from an Experience Source.

### Fields

```text
evidence_id
source_id
title
summary
resume_family
role_families
skill_ids
bullet_text
supporting_assets
claims_to_avoid
status
```

### Resume Families

```text
business_analyst
business_systems_analyst
application_support
production_support
market_data_support
technical_ba
cloud_migration
operations
```

---

## 5. InterviewStory

Represents an interview-ready STAR or story asset.

### Fields

```text
story_id
source_id
title
story_type
situation
task
actions
result
themes
linked_skills
linked_roles
supporting_assets
status
```

### Story Types

```text
technical_refresh
cloud_migration
production_support
data_quality
governance
market_data_operations
```

---

## 6. InterviewPromptMapping

Maps likely interview questions to stories and evidence.

### Fields

```text
prompt_id
question
role_family
source_id
recommended_story_ids
recommended_evidence_ids
talking_points
status
```

---

## 7. JDExperienceMatch

Represents the relationship between a JD and relevant Experience Source evidence.

### Fields

```text
match_id
jd_id
source_id
matched_skills
matched_assets
matched_resume_evidence
matched_interview_stories
fit_notes
risk_notes
status
```

---

# Folder Strategy

## Existing

```text
data/experience-sources/
  mrprice-experience-source.json
```

## Proposed

```text
data/experience-assets/
  mrprice-assets-index.json

data/experience-skills/
  mrprice-skills.json

data/resume-evidence/
  mrprice-resume-evidence.json

data/interview-stories/
  mrprice-interview-stories.json

data/interview-prompts/
  mrprice-interview-prompts.json

data/jd-experience-matches/
```

---

# MRPrice Initial Source Mapping

## Experience Source

```text
source_id: mrprice
repo: mrprice-experience-intelligence
release: v0.4.1
status: active
```

## Primary Assets

```text
MRPRICE_SKILLS_MAPPING
MRPRICE_RESUME_EVIDENCE
MRPRICE_STAR_STORIES
MRPRICE_INTERVIEW_BANK
MRPRICE_CAREER_SYSTEM_MAPPING
```

## Primary Domains

```text
market-data
production-support
application-support
business-analysis
technical-refresh
cloud-migration
data-quality
oracle
linux
rest-api
governance
```

---

# JD Keyword Mapping Concept

Career System should map JD language to Experience Source assets.

## Example

JD mentions:

```text
production support
incident investigation
Oracle
Linux
```

Career System should match:

```text
source_id: mrprice

assets:
- MRPRICE_STP_AND_BATCH_PROCESSING
- MRPRICE_PRODUCTION_SUPPORT
- MRPRICE_RESUME_EVIDENCE
- MRPRICE_INTERVIEW_BANK

resume evidence:
- production support for Linux/Oracle market-data platform
- feed monitoring
- incident investigation
- operational checks

interview stories:
- Production Support and Market Data Operations
```

---

# Resume Generation Concept

Current path:

```text
JD
  ↓
Resume Tailoring
  ↓
Resume Generation
```

Target path:

```text
JD
  ↓
Skill Extraction
  ↓
Experience Source Matching
  ↓
Resume Evidence Selection
  ↓
Resume Tailoring
  ↓
Resume Generation
```

---

# Interview Preparation Concept

Target path:

```text
JD
  ↓
Role Family Detection
  ↓
Experience Source Matching
  ↓
STAR Story Selection
  ↓
Interview Bank Selection
  ↓
Interview Prep Package
```

---

# Design Boundary

Career System owns:

* indexes
* matching logic
* scoring
* resume tailoring
* resume generation
* interview package generation

Experience Source repositories own:

* raw experience knowledge
* architecture notes
* stories
* evidence
* diagrams
* source context

---

# Initial Implementation Plan

## v0.5.0

Design Experience Source domain model.

Deliverables:

```text
docs/architecture/experience-source-domain-model.md
```

## v0.5.1

Create MRPrice structured indexes.

Deliverables:

```text
data/experience-assets/mrprice-assets-index.json
data/experience-skills/mrprice-skills.json
data/resume-evidence/mrprice-resume-evidence.json
data/interview-stories/mrprice-interview-stories.json
```

## v0.5.2

Create matching rules.

Deliverables:

```text
data/experience-matching/mrprice-keyword-map.json
docs/architecture/experience-matching-strategy.md
```

## v0.5.3

Integrate with resume tailoring.

Deliverables:

```text
updated resume-tailoring workflow
MRPrice evidence-aware tailoring output
```

---

# Open Questions

## Path References

Should Career System store absolute local paths, repo-relative paths, or logical Obsidian links?

Recommendation:

Use repo-relative paths plus source repository metadata.

## Source Sync

Should Career System copy source summaries or read directly from the MRPrice repository?

Recommendation:

Use structured summaries and indexes in Career System. Do not copy full source notes.

## Skills Repository Integration

Should skills be generated inside Career System or Obsidian Skills NG?

Recommendation:

Generate structured skill objects in Career System first. Later export or sync selected skills into Obsidian Skills NG.

---

# Summary

Experience Sources make Career System more powerful by connecting job descriptions to actual professional evidence.

MRPrice is the first Experience Source.

The model can later support additional experience repositories such as:

* AIG
* Thomson Reuters
* EmblemHealth
* Central Bank projects
* Motorweb proof-of-concept work

