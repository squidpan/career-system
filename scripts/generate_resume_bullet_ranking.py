#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

BOOSTS = {
  "market":7,"data":3,"linux":8,"python":6,"oracle":8,"rest":8,"api":5,
  "runbook":8,"runbooks":8,"release":7,"deployment":7,"uat":7,
  "requirements":7,"acceptance":5,"stakeholder":6,"production":8,
  "support":6,"monitoring":7,"grafana":8,"prometheus":8,"incident":7,
  "risk":6,"validation":7,"validate":7,"workflow":6,"servicenow":6,
  "aws":6,"cloud":5,"financial":6,"workday":8,"gis":8,"geospatial":8,
  "documentation":5,"operational":5,"readiness":5,"escalation":6,
  "problem":5,"health":4,"checks":4,"jira":5,"agile":4,
  "devops":6,"qa":4,"database":4,"infrastructure":5,"stability":6,
  "resiliency":6,"troubleshooting":7,"environment":5
}

REMOVE_STRONG = [
    "cad/cam", "catia", "stonerule", "fortran", "aix", "sun", "ibm mainframe",
    "db2", "hyundai motor", "general dynamics", "sikorsky", "bell helicopter",
    "manufacturing", "aerospace", "automotive", "defense engineering"
]

def split_frontmatter(text: str):
    if not text.startswith("---"): return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3: return {}, text
    fm = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            k,v = line.split(":",1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, parts[2]

def read_doc(path: Path):
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    return {"path": path, "frontmatter": fm, "body": body, "text": text}

def slug_from_filename(path: Path) -> str:
    name = path.stem
    for prefix in ["resume-tailoring-","resume-","bullet-ranking-","gap-","jd-intelligence-"]:
        if name.startswith(prefix): name = name[len(prefix):]
    for suffix in ["-v1","-teal-v1","-assembled-v1"]:
        if name.endswith(suffix): name = name[:-len(suffix)]
    return name

def find_by_slug(folder: Path, prefix: str, slug: str, ext: str=".md") -> Path|None:
    direct = folder / f"{prefix}{slug}{ext}"
    if direct.exists(): return direct
    st = set(slug.split("-"))
    best, score = None, 0
    for p in folder.glob(f"*{ext}"):
        pt = set(slug_from_filename(p).split("-"))
        s = len(st & pt)
        if s > score:
            best, score = p, s
    return best if score >= 2 else None

def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9+#/.-]+", " ", s.lower()).strip()

def extract_bullets(text: str):
    bullets, section, company = [], "unknown", ""
    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped.startswith("## "):
            section = stripped.lstrip("#").strip()
            continue
        if stripped.startswith("### "):
            company = stripped.lstrip("#").strip()
            continue
        if stripped.startswith("- "):
            b = stripped[2:].strip()
            if len(b) >= 20:
                bullets.append({"section": section, "company": company, "bullet": b})
    return bullets

def json_load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def tokens_from_values(values):
    toks = []
    for v in values or []:
        for t in re.split(r"[,;:/()\-]+|\s+", str(v).lower()):
            t = t.strip()
            if len(t) >= 4:
                toks.append(t)
    return sorted(set(toks))

def classify_action(score: int, bullet: str, hits: list[str]):
    b = norm(bullet)
    if any(term in b for term in REMOVE_STRONG):
        return "remove"
    if score >= 45:
        return "promote"
    if score >= 25:
        return "keep"
    if score >= 10:
        return "compress"
    return "remove"

def action_reason(action: str):
    return {
        "promote": "Strong match to JD/tailoring signals; candidate for top experience bullets.",
        "keep": "Useful supporting bullet; keep if space allows or place after promoted bullets.",
        "compress": "Some relevance, but should be shortened or merged with adjacent experience.",
        "remove": "Low relevance for this target role; remove or move to highly compressed older-experience summary."
    }.get(action, "")

def score_bullet(bullet, positive_values, negative_values):
    b = norm(bullet)
    score, hits = 0, []
    for kw in tokens_from_values(positive_values):
        if kw in b:
            score += 3
            hits.append(kw)
    for kw, val in BOOSTS.items():
        if kw in b:
            score += val
            hits.append(kw)
    for kw in tokens_from_values(negative_values):
        if kw in b:
            score -= 2
    if any(term in b for term in REMOVE_STRONG):
        score -= 20
    return score, sorted(set(hits))[:15]

def md_ranked(items):
    if not items: return "- None identified\n"
    out = ""
    for i, x in enumerate(items, 1):
        hits = ", ".join(x.get("matched_terms", [])) or "none"
        out += f"{i}. **Score {x['score']} — {x['action'].upper()}** — {x['bullet']}\n"
        out += f"   - Section: {x.get('section','')}\n"
        if x.get("company"):
            out += f"   - Company/context: {x.get('company')}\n"
        out += f"   - Matched terms: {hits}\n"
        out += f"   - Rationale: {action_reason(x['action'])}\n"
    return out

def action_counts(items):
    counts = {"promote":0,"keep":0,"compress":0,"remove":0}
    for x in items:
        counts[x["action"]] += 1
    return counts

def rank_one(tailoring_json: Path, resume_path: Path):
    t = json_load(tailoring_json)
    resume = read_doc(resume_path)
    positives, negatives = [], t.get("demote", []) or []
    for key in ["jd_terms", "promote", "story_recommendations"]:
        positives += t.get(key, []) or []
    ranked = []
    for b in extract_bullets(resume["text"]):
        score, hits = score_bullet(b["bullet"], positives, negatives)
        action = classify_action(score, b["bullet"], hits)
        ranked.append({**b, "score": score, "matched_terms": hits, "action": action})
    ranked.sort(key=lambda x: x["score"], reverse=True)
    buckets = {
        "promote": [x for x in ranked if x["action"] == "promote"],
        "keep": [x for x in ranked if x["action"] == "keep"],
        "compress": [x for x in ranked if x["action"] == "compress"],
        "remove": [x for x in ranked if x["action"] == "remove"],
    }
    return t, buckets, ranked

def generate_one(tailoring_md: Path, resumes_dir: Path, output_dir: Path, run_id: str):
    slug = slug_from_filename(tailoring_md)
    tailoring_json = tailoring_md.with_suffix(".json")
    resume_path = find_by_slug(resumes_dir, "resume-", slug)
    if not resume_path:
        raise FileNotFoundError(f"Could not find resume for {slug}")
    t, buckets, ranked = rank_one(tailoring_json, resume_path)
    company = t.get("company", "unknown-company")
    title = t.get("title", slug)
    role_code = t.get("role_code", "")
    counts = action_counts(ranked)
    data = {
        "run_id": run_id, "company": company, "title": title, "role_code": role_code,
        "tailoring_file": str(tailoring_md), "resume_file": str(resume_path),
        "ranked_count": len(ranked), "action_counts": counts,
        "promote": buckets["promote"], "keep": buckets["keep"],
        "compress": buckets["compress"], "remove": buckets["remove"]
    }
    md_path = output_dir / f"bullet-ranking-{slug}.md"
    json_path = output_dir / f"bullet-ranking-{slug}.json"
    md = f"""---
type: resume_bullet_ranking
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
tailoring_file: {tailoring_md}
resume_file: {resume_path}
ranked_count: {len(ranked)}
promote_count: {counts['promote']}
keep_count: {counts['keep']}
compress_count: {counts['compress']}
remove_count: {counts['remove']}
---

# Resume Bullet Ranking — {company} — {title}

## Summary

- Company: **{company}**
- Role: **{title}**
- Role Code: **{role_code}**
- Resume File: `{resume_path}`
- Ranked Bullet Count: **{len(ranked)}**
- Promote: **{counts['promote']}**
- Keep: **{counts['keep']}**
- Compress: **{counts['compress']}**
- Remove: **{counts['remove']}**

## Promote — Move Up / Lead With These

{md_ranked(buckets['promote'])}
## Keep — Useful Supporting Bullets

{md_ranked(buckets['keep'])}
## Compress — Shorten Or Merge

{md_ranked(buckets['compress'])}
## Remove — De-Emphasize Strongly

{md_ranked(buckets['remove'])}
## How To Use This

1. Use **Promote** bullets as candidates for the first 8-10 bullets in the tailored resume.
2. Use **Keep** bullets as supporting evidence after the strongest recent-role bullets.
3. Convert **Compress** bullets into shorter sector summaries or merge them into broader experience blocks.
4. Remove or heavily compress **Remove** bullets when targeting this specific role.
5. Do not copy this ranking blindly. Review for truthfulness, resume length, and role fit.

## Notes

This v0.4.6.2 output refines v0.4.6.1 by assigning each existing resume bullet to Promote, Keep, Compress, or Remove.
"""
    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return md_path, json_path

def main(argv):
    if len(argv) < 3:
        print("Usage: generate_resume_bullet_ranking.py <run_id> <resume_tailoring_dir> [resumes_dir]", file=sys.stderr)
        return 2
    run_id = argv[1]
    tailoring_dir = Path(argv[2])
    resumes_dir = Path(argv[3]) if len(argv) > 3 else Path("data/resume-versions/teal-export")
    run_out = Path("ops/runs") / run_id / "output"
    data_out = Path("data/resume-bullet-ranking")
    run_out.mkdir(parents=True, exist_ok=True)
    data_out.mkdir(parents=True, exist_ok=True)
    generated = []
    for tailoring_md in sorted(tailoring_dir.glob("resume-tailoring-*.md")):
        md, js = generate_one(tailoring_md, resumes_dir, run_out, run_id)
        generated.append(md.name)
        for src in [md, js]:
            (data_out / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"generated bullet ranking: {tailoring_md.name} -> {md.name}")
    report = {"run_id": run_id, "count": len(generated), "generated": generated}
    for folder in [run_out, data_out]:
        (folder / f"resume-bullet-ranking-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("Done.")
    print(f"Run output: {run_out.resolve()}")
    print(f"Resume bullet ranking copied to: {data_out.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
