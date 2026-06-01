# Resume Version Generation Workflow

## Purpose

Generate first-pass resume-version Markdown files from role records.

## Inputs

```text
data/roles/*.md
data/resume-masters/*.md
```

## Outputs

```text
data/resume-versions/generated/*.md
```

## Design Rule

The generated resume version is not the final tailored resume.

It is a structured starting point that links:

- role
- JD
- recommended resume master
- company
- role code

The user can later edit the generated resume in Obsidian or Teal.
