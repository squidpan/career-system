# Resume Assembly Workflow

## Purpose

Create complete application-ready resume markdown files from master resumes.

## Inputs

```text
data/roles/*.md
data/jds/normalized/*.md
data/resume-versions/generated/*.md
data/resume-masters/*.md
```

## Output

```text
data/resume-versions/assembled/*.md
```

## Design Rule

The assembled resume is a full resume, not a metadata record.

The generator may add a tailoring header and notes, but the main resume body should come from the full master resume unless a future tailoring engine makes explicit, reviewed edits.

## Future Enhancements

- JD keyword extraction
- prioritized bullet selection
- role-specific summary rewriting
- export to DOCX/PDF
- ATS formatting cleanup
