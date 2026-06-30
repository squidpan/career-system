# Current Career System Pipeline — Recovery Notes

Status: Draft  
Branch: ops/recover-ats-html-workflow  
Date: 2026-06-30

## Goal

Recover the JD-to-ATS-HTML workflow safely without wiping existing generated data.

## Current Confirmed State

The 9 imported JDs have completed:

- raw JD import
- JD normalization
- role generation
- resume-version generation

## New JD Regression Set

- LangChain
- MarketAxess
- TIAA
- BlackRock
- Clearwater Analytics
- Experis
- Plexus Resource Solutions
- PRI Technology
- Raas Infotek LLC

## Confirmed Working Layers

```text
raw JD
→ normalized JD
→ role
→ resume version
