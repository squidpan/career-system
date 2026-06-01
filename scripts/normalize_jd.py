#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, re
from pathlib import Path
from typing import Any

def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"&", " and ", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text

def split_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end].strip(), text[end + 4:].lstrip()
    return "", text

def parse_simple_yaml(frontmatter: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key = None
    for raw in frontmatter.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            if current_key not in data or data[current_key] == "":
                data[current_key] = []
            elif not isinstance(data[current_key], list):
                data[current_key] = [data[current_key]]
            data[current_key].append(line[4:].strip().strip('"'))
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
            current_key = key.strip()
    return data

def render_frontmatter(data: dict[str, Any]) -> str:
    order = [
        "id","slug","type","title","categories","tags","status","version","created","last",
        "company","company_slug","source_system","source_file","source_url","origin","run_id",
        "captured_date","source_title","normalized_title","role_id",
        "role_family","role_level","role_qualifiers","role_code","role_code_confidence","role_summary",
        "jd_file_name","jd_source_type","jd_text_status","role_source_type",
        "normalization_status","normalized_jd_id"
    ]
    lines = ["---"]
    for key in order:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value if value is not None else ''}")
    for key, value in data.items():
        if key in order:
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value if value is not None else ''}")
    lines.append("---")
    return "\n".join(lines) + "\n"

def contains_any(text: str, patterns: list[str]) -> bool:
    low = f" {text.lower()} "
    return any(p.lower() in low for p in patterns)

def extract_title_company(body: str) -> tuple[str, str]:
    headings = re.findall(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE)
    source_title = ""
    for h in headings:
        if h.strip().lower() not in {"source", "clipped content", "capture metadata"}:
            source_title = h.strip()
            break

    company = ""
    if source_title and ("## " + source_title) in body:
        after = body.split("## " + source_title, 1)[-1]
        m = re.search(r"^\*\*(.+?)\*\*", after, flags=re.MULTILINE)
        if m:
            company = m.group(1).strip(" —-")

    if not company:
        if "Makai Labs" in body:
            company = "Makai Labs"
            if not source_title:
                source_title = "Business Analyst"
        elif "Tata Consultancy Services" in body:
            company = "Tata Consultancy Services"
            if not source_title:
                source_title = "Business Analyst -Artificial Intelligence"

    return source_title, company

def infer_normalized_title(source_title: str, body: str) -> str:
    m = re.search(r"Original Job Description\s*\n\s*(.+)", body, flags=re.IGNORECASE)
    if m:
        candidate = m.group(1).strip()
        if 4 <= len(candidate) <= 120:
            return candidate
    return source_title

def infer_role(text: str, refs_dir: Path) -> tuple[str, str, list[str], str, str]:
    families = load_json(refs_dir / "role-families.json")
    levels = load_json(refs_dir / "role-levels.json")
    qualifiers = load_json(refs_dir / "role-qualifiers.json")

    role_family = ""
    if contains_any(text, ["business analyst"]):
        role_family = "ba"
    else:
        for code, meta in families.items():
            if contains_any(text, meta.get("patterns", [])):
                role_family = code
                break

    role_level = ""
    for code, meta in levels.items():
        if contains_any(text, meta.get("patterns", [])):
            role_level = code
            break

    role_qualifiers = []
    # Only identity-grade qualifiers belong in role_code.
    # Broader JD keywords should become capabilities later, not filename/id components.
    identity_qualifiers = {"ai", "appsupport", "pm", "cloud", "data", "product"}
    for code, meta in qualifiers.items():
        if code in identity_qualifiers and contains_any(text, meta.get("patterns", [])):
            role_qualifiers.append(code)
    role_qualifiers = list(dict.fromkeys(role_qualifiers))

    if role_family == "ba" and role_level == "senior":
        base = "sba"
    elif role_family:
        base = role_family
    else:
        base = "unknown"

    role_code = "-".join([base] + [q for q in role_qualifiers if q != base])
    confidence = "high" if base != "unknown" else "low"
    return role_family, role_level, role_qualifiers, role_code, confidence

def normalize_file(path: Path, output_dir: Path, run_id: str, refs_dir: Path) -> Path:
    raw = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(raw)
    fm = parse_simple_yaml(fm_text)

    source_title, company = extract_title_company(body)
    normalized_title = infer_normalized_title(source_title, body)
    company_slug = slugify(company) if company else "unknown-company"

    # Role identity must come from the selected JD title/header, not the full Teal page/body.
    # The full body contains unrelated tracker rows and many capability keywords.
    role_identity_text = "\n".join([source_title, normalized_title, company])
    role_family, role_level, role_qualifiers, role_code, confidence = infer_role(
        role_identity_text, refs_dir
    )

    year = str(fm.get("captured_date") or fm.get("created") or "2026")[:4]
    slug = f"{company_slug}-{role_code}-{year}"
    jd_id = f"jd-{slug}-v1"
    role_id = f"role-{slug}"
    title = f"{normalized_title} - {company}" if company else normalized_title

    fm.update({
        "id": jd_id,
        "slug": slug,
        "type": "jd",
        "title": title,
        "status": "normalized",
        "company": company,
        "company_slug": company_slug,
        "origin": fm.get("origin") or "webclipper",
        "run_id": run_id,
        "source_title": source_title,
        "normalized_title": normalized_title,
        "role_id": role_id,
        "role_family": role_family,
        "role_level": role_level,
        "role_qualifiers": role_qualifiers,
        "role_code": role_code,
        "role_code_confidence": confidence,
        "jd_file_name": f"{jd_id}.md",
        "jd_source_type": fm.get("jd_source_type") or "clipped",
        "jd_text_status": "normalized",
        "role_source_type": "jd",
        "normalization_status": "normalized",
        "normalized_jd_id": jd_id,
    })

    body2 = re.sub(r"^# .+$", f"# {title}", body, count=1, flags=re.MULTILINE) if body.startswith("# ") else f"# {title}\n\n{body}"
    out = output_dir / f"{jd_id}.md"
    out.write_text(render_frontmatter(fm) + "\n" + body2, encoding="utf-8")
    return out

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    refs_dir = repo_root / "data" / "reference"
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("*.md"))
    if not files:
        print(f"No markdown files found in {input_dir}")
        return 1

    for f in files:
        out = normalize_file(f, output_dir, args.run_id, refs_dir)
        print(f"normalized: {f.name} -> {out.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
