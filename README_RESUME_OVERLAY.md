# Career System v0.2.1 Resume Overlay

This overlay adds the first resume-management layer to the Career System project.

It includes:

- Master BA resume in Markdown
- Master SRE resume in Markdown
- Role-specific resume versions for Svitla, AEGIS, and Pico
- Master cover letter templates for BA and SRE
- AEGIS and Pico cover letters
- AEGIS thank-you letter
- Resume and communication templates
- Original source PDFs and extracted text
- Obsidian-friendly mirror folders
- Resume system documentation

## Important Overlay Rule

The zip contains a wrapper folder:

```text
career-system-v0.2.1-resume-overlay/
```

Do **not** keep that wrapper folder inside the repo as the final structure.

The repo root should contain the overlay subfolders directly:

```text
career-system/
├── data/
├── docs/
├── obsidian/
├── templates/
└── README_RESUME_OVERLAY.md
```

Use `/tmp` as a staging area, then copy only the contents of the wrapper folder into the repo root.

---

# A-Z Setup: New Local Git Repo + Overlay + GitHub Push

These steps assume you do **not** have a Career System git repo yet.

## Phase 0 — Confirm Zip Location

Assuming the zip is in Downloads:

```bash
ls -l ~/Downloads/career-system-v0.2.1-resume-overlay.zip
```

If your downloaded file has a slightly different name, adjust the commands below.

---

## Phase 1 — Create the Local Repo

```bash
mkdir -p ~/pjs/repos/career-system
cd ~/pjs/repos/career-system

git init
git branch -M main
git status
```

Expected:

```text
On branch main
No commits yet
```

---

## Phase 2 — Unzip to /tmp Staging Area

This prevents the wrapper folder from accidentally becoming part of the repo structure.

```bash
rm -rf /tmp/career-system-overlay
mkdir -p /tmp/career-system-overlay

unzip ~/Downloads/career-system-v0.2.1-resume-overlay.zip \
  -d /tmp/career-system-overlay
```

Verify staging folder:

```bash
tree -L 2 /tmp/career-system-overlay
```

Expected:

```text
/tmp/career-system-overlay
└── career-system-v0.2.1-resume-overlay
    ├── data
    ├── docs
    ├── obsidian
    ├── templates
    └── README_RESUME_OVERLAY.md
```

---

## Phase 3 — Copy Only Overlay Contents Into Repo Root

```bash
cd ~/pjs/repos/career-system

cp -R /tmp/career-system-overlay/career-system-v0.2.1-resume-overlay/* .
```

Verify repo structure:

```bash
tree -L 3
```

Expected top-level structure:

```text
.
├── data
├── docs
├── obsidian
├── templates
└── README_RESUME_OVERLAY.md
```

The repo should **not** contain this:

```text
career-system-v0.2.1-resume-overlay/
```

If it does, remove it:

```bash
rm -rf career-system-v0.2.1-resume-overlay
```

---

## Phase 4 — Review Files Before Commit

```bash
git status
git diff --stat
find . -maxdepth 2 -type d | sort
```

Optional Obsidian check:

```bash
ls -l obsidian/Resumes/Masters
ls -l obsidian/Resumes/Versions
```

---

## Phase 5 — First Commit

```bash
git add .
git status
git commit -m "Initial Career System v0.2.1 resume foundation"
```

Verify:

```bash
git log --oneline --decorate -5
```

---

## Phase 6 — Create Empty GitHub Repo

Create a new GitHub repo named:

```text
career-system
```

Do **not** initialize it with:

- README
- .gitignore
- license

The local repo already has files.

---

## Phase 7 — Connect Remote

Use your GitHub SSH host alias:

```bash
git remote add origin git@github-squidpan:squidpan/career-system.git
```

Verify:

```bash
git remote -v
```

Expected:

```text
origin  git@github-squidpan:squidpan/career-system.git (fetch)
origin  git@github-squidpan:squidpan/career-system.git (push)
```

---

## Phase 8 — Push main

```bash
git push -u origin main
```

---

## Phase 9 — Final Verification

```bash
git status
git log --oneline --decorate -5
```

Expected:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

---

# If You Already Accidentally Unzipped the Wrapper Folder Into Repo Root

If your tree looks like this:

```text
career-system/
└── career-system-v0.2.1-resume-overlay/
    ├── data
    ├── docs
    ├── obsidian
    └── templates
```

Fix it with:

```bash
cd ~/pjs/repos/career-system

cp -R career-system-v0.2.1-resume-overlay/* .
rm -rf career-system-v0.2.1-resume-overlay

tree -L 3
```

Then continue with:

```bash
git add .
git commit -m "Initial Career System v0.2.1 resume foundation"
```

---

# Recommended Next Step After Push

Review these files in Obsidian first:

```text
obsidian/Resumes/Masters/Master BA Resume.md
obsidian/Resumes/Masters/Master SRE Resume.md
obsidian/Resumes/Versions/Svitla Senior BA Resume v1.md
obsidian/Resumes/Versions/AEGIS Senior BA Resume v1.md
```

The Master BA and Master SRE resumes are the source-of-truth working resumes. The role-specific resumes are derived versions.
