# Overlay Instructions

Copy these files into:

```text
docs/operations/handoffs/efk-eos-continuation/
```

Example:

```bash
cd ~/pjs/repos/career-system
mkdir -p docs/operations/handoffs/efk-eos-continuation
cp /path/to/efk-eos-continuation-handoff-20260714/*.md   docs/operations/handoffs/efk-eos-continuation/
git diff --check
git status --short
```

Commit on `docs/efk-eos-continuation`:

```bash
git add docs/operations/handoffs/efk-eos-continuation
git diff --cached --stat
git diff --cached --check
git commit -m "Add EFK EOS continuation handoff"
git push
```

For the new project chat, provide an updated snapshot of `docs/requirements/` and this handoff package as Project Sources.
