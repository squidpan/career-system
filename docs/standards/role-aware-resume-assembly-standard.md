# Role-Aware Resume Assembly Standard v0.4.7

## Purpose

Generate assembled v2 resumes from resume-tailoring and bullet-ranking outputs.

## Inputs

- Resume bullet ranking
- Resume tailoring
- Teal-export resume markdown

## Output

- `data/resume-versions/assembled-v2/resume-<slug>-assembled-v2.md`

## Design

v0.4.7 is generation-oriented, but still conservative. It selects and orders existing truthful bullets. It does not invent new experience.
