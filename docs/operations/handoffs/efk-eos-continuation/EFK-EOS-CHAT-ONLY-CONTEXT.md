# EFK / EOS Chat-Only Context

## Why This Split Exists

The original Career System chat became large and slow because operations, requirements, and EFK design became mixed. The new chat exists to keep framework engineering separate from operational recovery.

## Lessons Learned

During a recovery-Epic attempt, the following problems occurred:

- `git checkout` was used instead of `git switch`;
- quoted Obsidian category links were generated;
- `summary` was used instead of `description`;
- `project` was omitted;
- type and status capitalization conflicted with requested conventions;
- a long artifact was split across append heredocs and became corrupted;
- standards and templates were considered without enough analysis of context and data-model;
- older artifacts were treated as safe models despite repository evolution.

## Branch State at Handoff

- `docs/efk-eos-continuation`: active EFK branch, one commit ahead of main.
- `ops/recover-ats-html-workflow`: active recovery history.
- `feature/cs-operational-recovery`: local duplicate of the ops branch.
- `fix/ats-html-application-package`: identical to main.
- `fix/jd-normalizer-title-company-extraction`: merged into main.
- One named stash preserves the operations Epic draft.

## Content Rules Relevant to Validation

Career System must preserve approved facts, including streaming market-data wording, FRBNY on-site wording, and correct PlanetCAD versus Dassault client attribution.
