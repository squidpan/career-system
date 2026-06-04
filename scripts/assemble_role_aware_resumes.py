#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

EMPLOYER_MAP = {
 "financial services production support & application modernization": ("Federal Reserve Bank of New York / Gresham Technologies","Senior Business Analyst / DevOps Release Coordinator","04/2017 – 02/2026","New York, NY",1),
 "financial services & enterprise financial applications": ("Federal Reserve Bank of New York / Gresham Technologies","Senior Business Analyst / DevOps Release Coordinator","04/2017 – 02/2026","New York, NY",1),
 "enterprise business systems support": ("EmblemHealth / AIG Property Casualty / AIG Travel Guard","Senior Business Analyst / Program Manager","01/2009 – 01/2016","New York, NY / Jersey City, NJ",2),
 "insurance portfolio & business systems": ("EmblemHealth / AIG Property Casualty / AIG Travel Guard","Senior Business Analyst / Program Manager","01/2009 – 01/2016","New York, NY / Jersey City, NJ",2),
 "financial data platforms": ("Asset Control / Solomon Page / Capgemini / Fidelity Investments","Financial Data Management Consultant / Business Analyst","Prior experience","New York, NY / Boston, MA",3),
 "financial data management platforms": ("Asset Control / Solomon Page / Capgemini / Fidelity Investments","Financial Data Management Consultant / Business Analyst","Prior experience","New York, NY / Boston, MA",3),
 "software engineering foundation": ("OpenPages / Thomson Reuters / PlanetCAD / Dassault Systèmes","Software Engineer / Technical Consultant","Prior experience","New York, NY / Various client sites",4),
 "governance, engineering software & cad/cam solutions": ("OpenPages / Thomson Reuters / PlanetCAD / Dassault Systèmes","Software Engineer / Technical Consultant","Prior experience","New York, NY / Various client sites",4),
}

def split_frontmatter(text):
    if not text.startswith("---"): return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3: return {}, text
    fm = {}
    for line in parts[1].splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            k,v = line.split(":",1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, parts[2]

def read_doc(path):
    txt = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(txt)
    return {"frontmatter": fm, "body": body, "text": txt}

def slug_from_filename(path):
    name = path.stem
    for p in ["bullet-ranking-","resume-tailoring-","resume-","gap-","jd-intelligence-"]:
        if name.startswith(p): name = name[len(p):]
    for s in ["-v1","-v2","-teal-v1","-assembled-v1","-assembled-v2"]:
        if name.endswith(s): name = name[:-len(s)]
    return name

def find_by_slug(folder, prefix, slug, ext=".json"):
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

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def md_list(items):
    return "".join(f"- {x}\n" for x in items) if items else "- None identified\n"

def bullets(items):
    return "".join(f"- {x.get('bullet','')}\n" for x in items) if items else "- None selected\n"

def contact_block(text):
    out = []
    for line in text.splitlines()[:25]:
        if line.strip().startswith("## "): break
        out.append(line)
    return "\n".join(out).strip()

def summary(role_code, terms):
    t = " ".join(terms).lower()
    rc = (role_code or "").lower()
    base = "Senior Business Analyst and Application Support professional"
    if "sre" in rc:
        return f"{base} with hands-on exposure to Linux-based enterprise application support, production readiness, incident coordination, release validation, runbooks, and financial market data environments."
    if "workday" in t or "hris" in t:
        return f"{base} with experience supporting enterprise applications, requirements, UAT, workflow analysis, service-management coordination, release readiness, and business-user support; positioned to ramp quickly into Workday/HRIS workflows."
    if "gis" in t or "geospatial" in t:
        return f"{base} with strengths in requirements analysis, stakeholder communication, UAT, REST API validation, Oracle data comparison, documentation, and support for domain-specific business applications."
    if "production operations" in t or "application support" in t or "support" in rc:
        return f"{base} with experience in application and production support, operational runbooks, incident coordination, release validation, stakeholder communication, risk-aware escalation, and enterprise financial systems."
    return f"{base} with experience in requirements, UAT, documentation, application support, release coordination, data validation, and cross-functional delivery across financial services and insurance environments."

def skills(terms):
    mapping = {
      "linux":"Linux application support","python":"Python learning / scripting ramp-up","oracle":"Oracle data validation",
      "rest api":"REST API validation","market data":"Market data / financial data systems","redline":"Vendor platform support mindset",
      "application support platform":"Application support","production operations":"Production operations","incident management":"Incident coordination",
      "problem management":"Problem management","release management":"Release coordination","monitoring":"Monitoring / operational health checks",
      "risk assessment":"Risk and impact assessment","documentation":"Runbooks and support documentation","requirements analysis":"Requirements analysis",
      "uat":"UAT / acceptance criteria","stakeholder communication":"Stakeholder communication","workday":"Workday / HRIS ramp-up",
      "gis":"GIS requirements ramp-up","jira":"Jira stories and acceptance criteria","agile":"Agile delivery"
    }
    out = []
    st = set(terms or [])
    for k,v in mapping.items():
        if k in st: out.append(v)
    return out[:14] or ["Business analysis","Application support","UAT","Documentation","Release coordination"]

def employer_meta(item):
    ctx = (item.get("company") or item.get("section") or "").strip().lower()
    if ctx in EMPLOYER_MAP: return EMPLOYER_MAP[ctx]
    if "financial services" in ctx or "enterprise financial" in ctx: return EMPLOYER_MAP["financial services & enterprise financial applications"]
    if "insurance" in ctx or "enterprise business" in ctx: return EMPLOYER_MAP["insurance portfolio & business systems"]
    if "financial data" in ctx or "asset control" in ctx: return EMPLOYER_MAP["financial data management platforms"]
    if "software" in ctx or "cad" in ctx or "governance" in ctx: return EMPLOYER_MAP["governance, engineering software & cad/cam solutions"]
    return ("Additional Experience","Prior Relevant Experience","Prior experience","",9)

def group_items(items):
    groups = {}
    for item in items:
        emp, role, dates, loc, order = employer_meta(item)
        key = (order, emp, role, dates, loc)
        groups.setdefault(key, []).append(item)
    return sorted(groups.items(), key=lambda kv: kv[0][0])

def assemble(slug, ranking_json, tailoring_json, resume_path, outdir, run_id):
    ranking = load_json(ranking_json)
    tailoring = load_json(tailoring_json) if tailoring_json and tailoring_json.exists() else {}
    resume = read_doc(resume_path)
    company = ranking.get("company") or tailoring.get("company") or "unknown-company"
    title = ranking.get("title") or tailoring.get("title") or slug
    role_code = ranking.get("role_code") or tailoring.get("role_code") or ""
    terms = tailoring.get("jd_terms", []) or []
    promote = ranking.get("promote", []) or ranking.get("top_bullets", []) or []
    keep = ranking.get("keep", []) or []
    compress = ranking.get("compress", []) or []
    selected = promote[:10] + keep[:5]
    compressed = compress[:4]

    lines = []
    cb = contact_block(resume["text"])
    lines.append(cb or f"# {company} Targeted Resume")
    lines += ["", f"<!-- Generated by Career System {run_id}; target: {company} — {title} -->", "", "## Professional Summary", "", summary(role_code, terms), "", "## Core Skills", "", md_list(skills(terms)), "## Professional Experience", ""]
    for (order, emp, role, dates, loc), items in group_items(selected):
        lines += [f"### {emp}", "", f"**{role}** | {dates}" + (f" | {loc}" if loc else ""), "", bullets(items), ""]
    if compressed:
        lines += ["## Additional Relevant Experience", ""]
        for (order, emp, role, dates, loc), items in group_items(compressed):
            lines += [f"### {emp}", "", f"**{role}** | {dates}" + (f" | {loc}" if loc else ""), "", bullets(items), ""]
    lines += ["## Assembly Notes", "", "- This v0.4.7.1 resume is generated from employer-aware bullet ranking and resume tailoring signals.", "- Review manually before using in Teal, Obsidian, PDF export, or job applications.", "- Verify length, formatting, dates, company names, and role titles before sending.", ""]
    md = "\n".join(lines)
    md_path = outdir / f"resume-{slug}-assembled-v2.md"
    js_path = outdir / f"resume-{slug}-assembled-v2.json"
    md_path.write_text(md, encoding="utf-8")
    js_path.write_text(json.dumps({
        "run_id":run_id, "company":company, "title":title, "role_code":role_code, "slug":slug,
        "ranking_file":str(ranking_json), "tailoring_file":str(tailoring_json or ""), "source_resume_file":str(resume_path),
        "assembled_resume_file":str(md_path), "employer_blocks_count":len(group_items(selected)),
        "primary_bullets_count":len(promote[:10]), "supporting_bullets_count":len(keep[:5]), "compressed_bullets_count":len(compressed)
    }, indent=2) + "\n", encoding="utf-8")
    return md_path, js_path

def main(argv):
    if len(argv) < 3:
        print("Usage: assemble_role_aware_resumes.py <run_id> <bullet_ranking_dir> [tailoring_dir] [resumes_dir]", file=sys.stderr)
        return 2
    run_id = argv[1]
    ranking_dir = Path(argv[2])
    tailoring_dir = Path(argv[3]) if len(argv) > 3 else Path("data/resume-tailoring")
    resumes_dir = Path(argv[4]) if len(argv) > 4 else Path("data/resume-versions/teal-export")
    run_out = Path("ops/runs") / run_id / "output"
    data_out = Path("data/resume-versions/assembled-v2")
    run_out.mkdir(parents=True, exist_ok=True)
    data_out.mkdir(parents=True, exist_ok=True)
    generated = []
    for rj in sorted(ranking_dir.glob("bullet-ranking-*.json")):
        slug = slug_from_filename(rj)
        tj = find_by_slug(tailoring_dir, "resume-tailoring-", slug, ".json")
        rp = find_by_slug(resumes_dir, "resume-", slug, ".md")
        if not rp:
            print(f"WARNING: no resume found for {slug}; skipping", file=sys.stderr)
            continue
        md, js = assemble(slug, rj, tj, rp, run_out, run_id)
        generated.append(md.name)
        for src in [md, js]:
            (data_out / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"assembled employer-aware resume: {rj.name} -> {md.name}")
    report = {"run_id":run_id, "count":len(generated), "generated":generated}
    for folder in [run_out, data_out]:
        (folder / f"employer-aware-resume-assembly-report-{run_id}.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print("Done.")
    print(f"Run output: {run_out.resolve()}")
    print(f"Assembled v2 resumes copied to: {data_out.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
