# EFK / EOS Continuation Handoff

## Purpose

Continue Engineering Knowledge Framework and Engineering Operating System work in a dedicated chat without allowing framework design to displace Career System operational recovery.

## New Chat

Name: `EFK / EOS Continuation`

Goal: Continue engineering knowledge framework, standards, diagrams, validation, and observability.

## Current Branch

`docs/efk-eos-continuation`

Current head:

`2f357a7 Fix Obsidian category links in EFK artifacts`

## Scope

The new chat owns standards, templates, context, architecture, ADRs, data models, glossary, diagrams, traceability, validation, observability, Obsidian conventions, artifact lifecycle, and framework governance.

It does not own Career System pipeline recovery, resume generation, application-package production, operational bug fixing, or daily job-application work.

## Repository Source of Truth

Before authoring an artifact, inspect:

1. standards
2. templates
3. context
4. architecture and ADRs
5. data-model
6. glossary
7. parent and sibling artifacts
8. indexes and traceability
9. newest relevant evidence

Do not rely on generic conventions or older examples when repository guidance differs.

## Important Current Decisions

- Use `git branch` and `git switch`, not `git checkout`.
- Obsidian YAML category links are unquoted, for example `- [[Epics]]`.
- The user requested `project: career-system`, lowercase `type`, lowercase `status`, and `description` instead of `summary` for new artifacts. The EFK chat must reconcile these with current standards before broad normalization.
- Context and data-model folders must be part of every relevant EFK review.
- Long Markdown artifacts should be delivered as complete downloadable files or one verified heredoc, not fragmented append heredocs.
- Requirements artifacts are the project-tracking source, not Git history alone.
- At sprint closeout, run `git stash list`; every stash must be applied, dropped, or explicitly carried forward.

## First Session Objective

1. Inventory current front-matter conventions.
2. Identify conflicts and obsolete notes.
3. Classify guidance as stable, candidate, or legacy.
4. Define a bounded cleanup backlog.
5. Avoid mass normalization until migration impact is understood.
