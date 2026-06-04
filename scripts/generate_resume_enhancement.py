#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

ACTION_REPLACEMENTS = [
    ("Supported incident-oriented troubleshooting by coordinating", "Coordinated production incident troubleshooting through"),
    ("Worked closely with", "Partnered with"),
    ("Worked with", "Partnered with"),
    ("Supported enterprise financial applications delivering", "Supported enterprise financial applications that delivered"),
    ("Executed environment readiness testing", "Executed environment readiness testing"),
    ("Coordinated deployment readiness", "Coordinated deployment readiness"),
    ("Validated REST API pricing payloads", "Validated REST API pricing payloads"),
    ("Maintained runbooks", "Maintained operational runbooks"),
    ("Produced operational runbooks", "Produced operational runbooks"),
    ("Created representative UAT data", "Created representative UAT data"),
    ("Gathered and documented requirements", "Gathered and documented requirements"),
    ("Collaborated with Product Owners and Scrum Masters", "Collaborated with Product Owners and Scrum Masters"),
    ("Partnered with enterprise architects", "Partnered with enterprise architects"),
    ("Processed and validated", "Processed and validated"),
    ("Configured and tested", "Configured and tested"),
]

JD_PHRASE_ALIGNMENTS = [
    ("issue resolution", "production issue resolution"),
    ("environment checks", "environment validation checks"),
    ("log review", "log review"),
    ("deployment procedures", "deployment procedures"),
    ("support documentation", "support documentation"),
    ("workflow validation", "workflow validation"),
    ("signoff readiness", "business signoff readiness"),
    ("production stability", "production stability"),
]

def slug_from_filename(path: Path) -> str:
    name = path.stem
    for prefix in ["bullet-ranking-","resume-enhancement-","resume-tailoring-","resume-"]:
        if name.startswith(prefix): name = name[len(prefix):]
    for suffix in ["-v1","-v2","-teal-v1","-assembled-v1","-assembled-v2"]:
        if name.endswith(suffix): name = name[:-len(suffix)]
    return name

def find_by_slug(folder: Path, prefix: str, slug: str, ext: str=".json") -> Path|None:
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

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def clean_spaces(s: str):
    return re.sub(r"\s+", " ", s).strip()

def role_terms(tailoring: dict):
    terms = tailoring.get("jd_terms", []) or []
    promote = tailoring.get("promote", []) or []
    return " ".join(terms + promote).lower()

def improve_bullet(original: str, context: str):
    enhanced = original.strip()

    for old, new in ACTION_REPLACEMENTS:
        if enhanced.startswith(old):
            enhanced = enhanced.replace(old, new, 1)
            break

    for old, new in JD_PHRASE_ALIGNMENTS:
        enhanced = enhanced.replace(old, new)

    ctx = context.lower()

    # Conservative role-aware sharpening. Only add phrasing when the source bullet supports it.
    if "incident" in enhanced.lower() or "troubleshooting" in enhanced.lower():
        if "incident management" in ctx or "production operations" in ctx or "sre" in ctx:
            enhanced = enhanced.replace("issue resolution", "production issue resolution")
            if "production" not in enhanced.lower():
                enhanced = enhanced.replace("troubleshooting", "production troubleshooting")

    if "runbook" in enhanced.lower() or "documentation" in enhanced.lower():
        if "support documentation" not in enhanced.lower() and "documentation" in enhanced.lower():
            enhanced = enhanced.replace("documentation", "support documentation")

    if "release" in enhanced.lower() or "deployment" in enhanced.lower():
        if "production" not in enhanced.lower() and "production" in ctx:
            enhanced = enhanced.replace("release", "production release")

    if "requirements" in enhanced.lower() or "acceptance criteria" in enhanced.lower():
        if "implementation-ready requirements" not in enhanced.lower() and "requirements" in enhanced.lower():
            enhanced = enhanced.replace("requirements", "implementation-ready requirements")

    # Avoid overlong doubled phrases.
    enhanced = enhanced.replace("support support documentation", "support documentation")
    enhanced = enhanced.replace("production production", "production")
    enhanced = enhanced.replace("implementation-ready implementation-ready", "implementation-ready")

    return clean_spaces(enhanced)

def classify_change(original: str, enhanced: str):
    if original == enhanced:
        return "unchanged"
    if len(enhanced) < len(original):
        return "tightened"
    if len(enhanced) > len(original):
        return "jd_aligned"
    return "rewritten"

def enhance_items(items, context):
    out = []
    for item in items or []:
        original = item.get("bullet", "")
        enhanced = improve_bullet(original, context)
        out.append({
            **item,
            "original_bullet": original,
            "enhanced_bullet": enhanced,
            "change_type": classify_change(original, enhanced),
            "truthfulness_note": "Conservative wording enhancement only; verify manually before use.",
        })
    return out

def md_pairs(items):
    if not items:
        return "- None identified\n"
    out = ""
    for i, item in enumerate(items, 1):
        out += f"{i}. **Original:** {item.get('original_bullet','')}\n"
        out += f"   - **Enhanced:** {item.get('enhanced_bullet','')}\n"
        out += f"   - Action: {item.get('action','')}\n"
        out += f"   - Score: {item.get('score','')}\n"
        out += f"   - Change type: {item.get('change_type','')}\n"
        out += f"   - Note: {item.get('truthfulness_note','')}\n"
    return out

def generate_one(ranking_json: Path, tailoring_dir: Path, output_dir: Path, run_id: str):
    slug = slug_from_filename(ranking_json)
    ranking = load_json(ranking_json)
    tailoring_path = find_by_slug(tailoring_dir, "resume-tailoring-", slug, ".json")
    tailoring = load_json(tailoring_path) if tailoring_path else {}

    context = role_terms(tailoring) + " " + (ranking.get("role_code") or "")

    promote = enhance_items(ranking.get("promote", []) or ranking.get("top_bullets", []), context)
    keep = enhance_items(ranking.get("keep", []), context)
    compress = enhance_items(ranking.get("compress", []), context)

    company = ranking.get("company") or tailoring.get("company") or "unknown-company"
    title = ranking.get("title") or tailoring.get("title") or slug
    role_code = ranking.get("role_code") or tailoring.get("role_code") or ""

    data = {
        "run_id": run_id,
        "company": company,
        "title": title,
        "role_code": role_code,
        "slug": slug,
        "ranking_file": str(ranking_json),
        "tailoring_file": str(tailoring_path or ""),
        "promote": promote,
        "keep": keep,
        "compress": compress,
    }

    md_path = output_dir / f"resume-enhancement-{slug}.md"
    json_path = output_dir / f"resume-enhancement-{slug}.json"

    md = f"""---
type: resume_enhancement
status: draft
run_id: {run_id}
source: career-system
company: {company}
title: {title}
role_code: {role_code}
ranking_file: {ranking_json}
tailoring_file: {tailoring_path or ""}
---

# Resume Enhancement — {company} — {title}

## Purpose

This report proposes conservative wording improvements for existing ranked resume bullets. It does not invent new experience, employers, dates, tools, or accomplishments.

## Promote Bullet Enhancements

{md_pairs(promote)}
## Keep Bullet Enhancements

{md_pairs(keep)}
## Compress Bullet Enhancements

{md_pairs(compress)}
## Manual Review Rules

1. Keep only enhanced bullets that remain fully truthful.
2. Do not add tools or platforms you did not use.
3. Prefer enhanced bullets when they improve clarity, action verbs, or JD alignment.
4. Keep original bullets when enhanced wording feels too strong.
5. Use this report as input for a future final-resume assembly step.

## Notes

v0.4.8 is a conservative deterministic enhancement engine. It prepares better wording but does not yet overwrite assembled resumes.
"""
    md_path.write_text(md, encoding="utf-8")
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return md_path, json_path

def main(argv):
    if len(argv) < 3:
        print("Usage: generate_resume_enhancement.py <run_id> <bullet_ranking_dir> [tailoring_dir]", file=sys.stderr)
        return 2

    run_id = argv[1]
    ranking_dir = Path(argv[2])
    tailoring_dir = Path(argv[3]) if len(argv) > 3 else Path("data/resume-tailoring")

    run_out = Path("ops/runs") / run_id / "output"
    data_out = Path("data/resume-enhancement")
    run_out.mkdir(parents=True, exist_ok=True)
    data_out.mkdir(parents=True, exist_ok=True)

    generated = []
    for ranking_json in sorted(ranking_dir.glob("bullet-ranking-*.json")):
        md, js = generate_one(ranking_json, tailoring_dir, run_out, run_id)
        generated.append(md.name)
        for src in [md, js]:
            (data_out / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"generated resume enhancement: {ranking_json.name} -> {md.name}")

    report = {"run_id": run_id, "count": len(generated), "generated": generated}
    for folder in [run_out, data_out]:
        (folder / f"resume-enhancement-report-{run_id}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print("Done.")
    print(f"Run output: {run_out.resolve()}")
    print(f"Resume enhancements copied to: {data_out.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
