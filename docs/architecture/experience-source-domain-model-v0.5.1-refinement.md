# Experience Source Domain Model v0.5.1 Refinement

## Purpose

Refine the Experience Source model so Career System stores metadata indexes and relationships, not full duplicated source content.

## Core Rule

Experience repositories remain the source of truth.

Career System stores:

- source registration
- asset indexes
- skill mappings
- evidence indexes
- story indexes
- JD matching relationships

Career System should not copy full resume evidence, STAR stories, interview banks, or architecture notes from source repositories.

## Why

Copying full content creates drift.

Example:

MRPrice repo updates:

- MRPRICE_RESUME_EVIDENCE.md
- MRPRICE_STAR_STORIES.md
- MRPRICE_INTERVIEW_BANK.md

If Career System also stores full copies, the two repositories can become inconsistent.

## Preferred Pattern

```text
MRPrice Repository
        ↓
Career System Metadata Index
        ↓
Matching / Selection
        ↓
Resume or Interview Output

## Asset Stability Rule

Experience assets should have stable identifiers.

Example:

```text
mrprice_vendor_normalization
mrprice_tick_consolidation
mrprice_resume_evidence
mrprice_star_stories
```

Career System relationships should reference asset_id rather than file names.

Reason:

File names may change during repository evolution.

Stable asset IDs allow:

* skill mappings
* resume evidence indexes
* interview story indexes
* JD matching relationships

to remain valid even if source file names are renamed.

Preferred pattern:

```text
skill
    ↓
asset_id
    ↓
source_path
```

Avoid:

```text
skill
    ↓
hard-coded file path
```

Asset IDs are the canonical reference mechanism across Career System.

## Future Experience Sources

The Experience Source model should support multiple repositories.

Examples:

```text
mrprice
aig
thomson_reuters
emblemhealth
motorweb
```

Each source should expose:

* source registration
* asset indexes
* skills
* resume evidence indexes
* interview story indexes

without requiring Career System to duplicate source content.

## Design Decision

Career System functions as a knowledge router and matching engine.

Experience repositories remain the source of truth.

Career System stores metadata, relationships, and matching logic.

This separation minimizes duplication and allows repositories to evolve independently.

