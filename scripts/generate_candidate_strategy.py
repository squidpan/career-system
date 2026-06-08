#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, re
from pathlib import Path
from typing import Any

def slugify(text: str) -> str:
    text = text.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "unknown"

def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def pick(data: dict[str, Any], *keys: str, default: str = "") -> str:
    for k in keys:
        v = data.get(k)
        if v is not None and str(v).strip():
            return str(v).strip()
    return default

def walk_text(x: Any, out: list[str]) -> None:
    if isinstance(x, dict):
        for v in x.values(): walk_text(v, out)
    elif isinstance(x, list):
        for v in x: walk_text(v, out)
    elif x is not None:
        out.append(str(x))

def score_strategy(candidate: dict[str, Any]) -> dict[str, Any]:
    company = pick(candidate, "company", default="Unknown")
    role = pick(candidate, "role", "title", "role_title", default="Unknown")
    role_code = pick(candidate, "role_code", default="unknown")
    resume_family = pick(candidate, "resume_family", "role_family", default="ba")
    technical = int(candidate.get("match_score") or candidate.get("score") or candidate.get("technical_match_score") or 70)

    parts: list[str] = []
    walk_text(candidate, parts)
    blob = " ".join(parts).lower()
    company_l = company.lower()
    role_l = role.lower()
    code_l = role_code.lower()
    all_l = " ".join([company_l, role_l, code_l, blob])

    personal = 70
    reasons: list[str] = []
    risks: list[str] = []

    def add(xs: list[str], msg: str) -> None:
        if msg not in xs: xs.append(msg)

    if any(x in company_l for x in ["citi","barclays","dtcc","new york life","dow jones","finbourne","amtrak","con edison","premera"]):
        personal += 10
        add(reasons, "Large/regulated/enterprise employer signal; likely stronger stability and benefits fit.")

    if any(x in all_l for x in ["financial","bank","trading","fixed income","market data","investment","insurance"]):
        personal += 8
        add(reasons, "Domain overlap with FRBNY, financial data, market data, or insurance/business systems experience.")

    if code_l.startswith("ba") or code_l == "bsa":
        personal += 8
        add(reasons, "BA/BSA role family aligns with strongest recent positioning.")

    if code_l.startswith("support"):
        personal += 9
        add(reasons, "Application/production support role family aligns with FRBNY runbook, incident, release, and support background.")

    if code_l == "sre":
        personal += 3
        add(reasons, "SRE is adjacent to production support and Linux/application operations, but may require deeper hands-on infrastructure depth.")

    if code_l == "ops":
        personal += 4
        add(reasons, "Operations role is adjacent to BA/support experience, but may need careful resume positioning.")

    if "ai" in code_l or "artificial intelligence" in all_l:
        personal += 3
        add(reasons, "AI appears as an interest/learning signal; position as BA/support workflow exposure, not AI engineering.")

    if any(x in company_l for x in ["citi","barclays","dtcc","new york life","amtrak","con edison","premera","vns health"]):
        personal += 6
        add(reasons, "Employer type is more likely to offer structured benefits; verify directly before applying.")

    if any(x in all_l for x in ["on-site","onsite","hybrid","new york, ny","whippany","newark","white plains"]):
        personal -= 2
        add(risks, "Location/hybrid/onsite requirement may require commute review.")

    if any(x in company_l for x in ["watg","infotrack","payabli","valon","grapevine","airops"]):
        personal -= 5
        add(risks, "Smaller/niche employer or less direct domain fit; verify stability, benefits, and role expectations.")

    if any(x in all_l for x in ["workday","gis","arcgis","geospatial","salesforce","unqork"]):
        personal -= 5
        add(risks, "Specialized platform/domain appears; tailor carefully and avoid overstating direct hands-on experience.")

    if code_l == "support-workday":
        personal -= 6
        add(risks, "Workday-specific role may require ramp-up framing from enterprise application support rather than direct Workday administration.")

    personal = max(40, min(100, personal))
    combined = round((technical * 0.55) + (personal * 0.45))

    if combined >= 92: rec = "pursue_first"
    elif combined >= 86: rec = "apply_this_week"
    elif combined >= 80: rec = "apply_selectively"
    elif combined >= 72: rec = "network_or_research_first"
    else: rec = "lower_priority"

    if code_l.startswith("support"):
        resume_strategy = "Use application-support / production-support resume variant."
    elif code_l.startswith("ba") or code_l == "bsa":
        resume_strategy = "Use BA/BSA resume variant."
    elif code_l == "sre":
        resume_strategy = "Use SRE-adjacent support resume variant."
    elif code_l == "ops":
        resume_strategy = "Use operations/support hybrid resume variant."
    else:
        resume_strategy = "Use BA/application-support general resume variant and tailor manually."

    if not reasons: reasons.append("General match based on candidate matching score and available JD intelligence.")
    if not risks: risks.append("No major deterministic risk flags detected; review manually before applying.")

    if rec == "pursue_first": next_action = "Prioritize this role first. Tailor resume and apply promptly."
    elif rec == "apply_this_week": next_action = "Apply this week after tailoring the summary and top bullets."
    elif rec == "apply_selectively": next_action = "Apply if benefits, commute, and fit remain attractive."
    elif rec == "network_or_research_first": next_action = "Research employer/role before spending time on full tailoring."
    else: next_action = "Keep lower priority unless quick apply or strong personal interest."

    return {
        "company": company, "role": role, "role_code": role_code, "resume_family": resume_family,
        "technical_match_score": technical, "personal_strategy_score": personal,
        "combined_strategy_score": combined, "pursuit_recommendation": rec,
        "resume_strategy": resume_strategy, "reasons": reasons, "risk_flags": risks,
        "next_action": next_action
    }

def md_list(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)

def render_one(run_id: str, s: dict[str, Any]) -> str:
    return f"""---
type: candidate_strategy
status: draft
run_id: {run_id}
source: career-system
company: {s['company']}
role: {s['role']}
role_code: {s['role_code']}
technical_match_score: {s['technical_match_score']}
personal_strategy_score: {s['personal_strategy_score']}
combined_strategy_score: {s['combined_strategy_score']}
pursuit_recommendation: {s['pursuit_recommendation']}
resume_family: {s['resume_family']}
---

# Candidate Strategy — {s['company']} — {s['role']}

## Recommendation

**{s['pursuit_recommendation']}**

## Scores

- Technical match score: **{s['technical_match_score']}**
- Personal strategy score: **{s['personal_strategy_score']}**
- Combined strategy score: **{s['combined_strategy_score']}**

## Resume Strategy

{s['resume_strategy']}

## Why This Ranking

{md_list(s['reasons'])}

## Risk Flags

{md_list(s['risk_flags'])}

## Next Action

{s['next_action']}
"""

def render_report(run_id: str, items: list[dict[str, Any]]) -> str:
    lines = [
        "---", "type: candidate_strategy_report", "status: draft", f"run_id: {run_id}",
        "source: career-system", f"candidate_count: {len(items)}", "---", "",
        f"# Personalized Candidate Strategy Report — {run_id}", "",
        "## Summary", "", f"- Candidate count: **{len(items)}**",
        "- Scoring model: deterministic v0.6.0",
        "- Purpose: choose which jobs to pursue first based on technical fit plus Paul-specific strategy priorities.",
        "", "## Ranked Strategy", "",
        "| Rank | Combined | Technical | Personal | Recommendation | Company | Role | Resume Family | Role Code |",
        "|---:|---:|---:|---:|---|---|---|---|---|"
    ]
    for i, s in enumerate(items, 1):
        lines.append(f"| {i} | {s['combined_strategy_score']} | {s['technical_match_score']} | {s['personal_strategy_score']} | {s['pursuit_recommendation']} | {s['company']} | {s['role']} | {s['resume_family']} | {s['role_code']} |")
    lines += ["", "## Pursuit Guidance", "", "1. Start with `pursue_first` roles.", "2. Use `apply_this_week` for strong roles that need normal tailoring.", "3. Use `apply_selectively` for roles with fit but less urgency or more uncertainty.", "4. Research or network first when stability, benefits, commute, or role expectations are unclear."]
    return "\n".join(lines) + "\n"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    items: list[dict[str, Any]] = []
    for path in sorted(input_dir.glob("candidate-match-*.json")):
        if path.name.startswith("candidate-match-report-run-"):
            continue
        s = score_strategy(load_json(path))
        items.append(s)
        slug = slugify(f"{s['company']}-{s['role_code']}-2026")
        write_json(output_dir / f"candidate-strategy-{slug}.json", s)
        (output_dir / f"candidate-strategy-{slug}.md").write_text(render_one(args.run_id, s), encoding="utf-8")
        print(f"generated candidate strategy: {path.name} -> candidate-strategy-{slug}.md")

    items.sort(key=lambda x: (x["combined_strategy_score"], x["technical_match_score"], x["personal_strategy_score"]), reverse=True)

    report_base = f"candidate-strategy-report-{args.run_id}"
    write_json(output_dir / f"{report_base}.json", {"type": "candidate_strategy_report", "run_id": args.run_id, "candidate_count": len(items), "strategies": items})
    (output_dir / f"{report_base}.md").write_text(render_report(args.run_id, items), encoding="utf-8")
    print(f"generated candidate strategy report: {report_base}.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
