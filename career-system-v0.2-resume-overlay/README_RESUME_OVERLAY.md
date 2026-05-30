# Career System v0.2 Resume Overlay

This overlay adds the resume, cover-letter, and thank-you-letter foundation to `career-system`.

It is designed for your current workflow:

- Teal remains the resume builder/export tool.
- Obsidian remains the review/editing workspace.
- Career System becomes the source of truth for resume strategy, resume masters, role-specific versions, and communication history.

## What this overlay adds

```text
career-system/
├── docs/resume-system/
│   ├── RESUME_SYSTEM_README.md
│   ├── RESUME_VERSIONING.md
│   ├── RESUME_MASTER_STRATEGY.md
│   ├── RESUME_TO_JOB_WORKFLOW.md
│   └── COMMUNICATIONS_WORKFLOW.md
│
├── templates/
│   ├── resumes/
│   │   ├── resume-master-template.md
│   │   ├── resume-role-version-template.md
│   │   └── resume-version-record-template.json
│   └── communications/
│       ├── cover-letter-template.md
│       └── thank-you-letter-template.md
│
├── data/
│   ├── resume-masters/
│   │   ├── master-ba-resume.md
│   │   └── master-sre-resume.md
│   ├── resume-versions/
│   │   ├── svitla/resume-svitla-senior-ba-v1.md
│   │   ├── aegis/resume-aegis-senior-ba-v1.md
│   │   └── pico/resume-pico-sre-v1.md
│   ├── cover-letter-masters/
│   │   ├── cover-master-ba.md
│   │   └── cover-master-sre.md
│   ├── cover-letter-versions/
│   │   ├── aegis/cover-letter-aegis-senior-ba-v1.md
│   │   └── pico/cover-letter-pico-sre-v1.md
│   ├── thank-you-letters/
│   │   └── aegis/thank-you-aegis-2026-05-18.md
│   └── source-resumes/
│       ├── original-files/
│       └── pdf-text-extracts/
│
└── obsidian/
    ├── Resumes/
    └── Communications/
```

## How to apply this overlay

Assumption: your repo exists at:

```bash
cd ~/pjs/repos/career-system
```

If your repo path is different, adjust the `cd` command only.

## Step 1 — Create a safety branch

```bash
cd ~/pjs/repos/career-system
git status
git switch -c feature/resume-system-v0.2
```

## Step 2 — unzip overlay into a temporary folder

```bash
mkdir -p /tmp/career-system-overlay
unzip ~/Downloads/career-system-v0.2-resume-overlay.zip -d /tmp/career-system-overlay
```

## Step 3 — copy overlay contents into repo

```bash
cp -R /tmp/career-system-overlay/career-system-v0.2-resume-overlay/* .
```

## Step 4 — inspect new files

```bash
find docs/resume-system templates data/resume-masters data/resume-versions data/cover-letter-masters data/cover-letter-versions data/thank-you-letters obsidian -maxdepth 4 -type f | sort
```

## Step 5 — review markdown in Obsidian

Open these first:

```text
data/resume-masters/master-ba-resume.md
data/resume-masters/master-sre-resume.md
data/resume-versions/svitla/resume-svitla-senior-ba-v1.md
data/resume-versions/aegis/resume-aegis-senior-ba-v1.md
```

Recommended review order:

1. `master-ba-resume.md`
2. `resume-svitla-senior-ba-v1.md`
3. `resume-aegis-senior-ba-v1.md`
4. `master-sre-resume.md`
5. `resume-pico-sre-v1.md`

## Step 6 — git review

```bash
git status
git diff --stat
```

## Step 7 — commit

```bash
git add docs/resume-system templates data obsidian README_RESUME_OVERLAY.md
git commit -m "Add resume system v0.2 overlay"
```

## Step 8 — push

```bash
git push -u origin feature/resume-system-v0.2
```

## Important editing rule

Do not directly edit role-specific versions first.

Edit in this order:

```text
Master BA / Master SRE
        ↓
Role-specific resume
        ↓
Teal version
        ↓
PDF export
```

## Current recommendation

Use only two master resumes for now:

```text
master-ba-resume.md
master-sre-resume.md
```

The BA master covers:

- Senior Business Analyst
- Business Systems Analyst
- Application Support BA
- Enterprise Delivery BA
- Technical BA
- Insurance BA
- Financial Systems BA

The SRE master covers:

- Site Reliability Engineer
- Production Support
- Application Support Engineer
- Market Data Support
- Operations Engineer

This avoids maintaining too many master documents.
