# Install Career System v0.2.1 Resume Overlay From Zip

Use this exact flow when the repo does not exist yet.

```bash
mkdir -p ~/pjs/repos/career-system
cd ~/pjs/repos/career-system

git init
git branch -M main

rm -rf /tmp/career-system-overlay
mkdir -p /tmp/career-system-overlay

unzip ~/Downloads/career-system-v0.2.1-resume-overlay.zip \
  -d /tmp/career-system-overlay

cp -R /tmp/career-system-overlay/career-system-v0.2.1-resume-overlay/* .

rm -rf career-system-v0.2.1-resume-overlay

tree -L 3

git add .
git commit -m "Initial Career System v0.2.1 resume foundation"

git remote add origin git@github-squidpan:squidpan/career-system.git
git push -u origin main

git status
```
```
