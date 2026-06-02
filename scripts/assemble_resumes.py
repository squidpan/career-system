#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

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
        "id", "slug", "type", "title", "categories", "tags", "status", "version",
        "created", "last", "company", "company_slug", "role_id", "jd_id",
        "resume_version_id", "resume_master_id", "resume_master_file",
        "resume_family", "role_family", "role_level", "role_qualifiers", "role_code",
        "application_package_id", "origin", "run_id"
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
    lines.append("---")
    return "\n".join(lines) + "\n"

def first_item(value: Any) -> str:
    if isinstance(value, list) and value:
        return value[0]
    if isinstance(value, str):
        return value
    return ""

def read_md(path: Path) -> tuple[dict[str, Any], str, str]:
    text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(text)
    return parse_simple_yaml(fm_text), body, text

def find_file_by_id(directory: Path, item_id: str) -> Path | None:
    if not item_id:
        return None
    direct = directory / f"{item_id}.md"
    if direct.exists():
        return direct
    for p in sorted(directory.glob("*.md")):
        try:
            fm, _, _ = read_md(p)
            if fm.get("id") == item_id:
                return p
        except Exception:
            pass
    return None

def find_resume_version_for_role(resume_dir: Path, role_id: str) -> Path | None:
    for p in sorted(resume_dir.glob("*.md")):
        try:
            fm, _, _ = read_md(p)
            if fm.get("role_id") == role_id:
                return p
        except Exception:
            pass
    return None

def clean_master_body(body: str) -> str:
    # Keep full master resume body, but strip accidental surrounding whitespace.
    return body.strip() + "\n"

def extract_jd_keywords(jd_body: str) -> list[str]:
    keywords = []
    patterns = [
        "requirements", "user stories", "acceptance criteria", "uat", "jira",
        "workday", "enterprise applications", "application support", "production support",
        "rest api", "api", "data mapping", "sdlc", "agile", "linux", "oracle",
        "aws", "servicenow", "runbooks", "gis", "saas", "integration"
    ]
    lower = jd_body.lower()
    for word in patterns:
        if word in lower:
            keywords.append(word)
    return keywords[:12]

def assemble_resume(role_path: Path, output_dir: Path, run_id: str, repo_root: Path) -> Path:
    role, _, _ = read_md(role_path)
    role_id = role.get("id", "")
    slug = role.get("slug", role_id.removeprefix("role-"))
    jd_id = first_item(role.get("jd_ids", []))
    jd_path = find_file_by_id(repo_root / "data" / "jds" / "normalized", jd_id)
    resume_version_path = find_resume_version_for_role(repo_root / "data" / "resume-versions" / "generated", role_id)

    if not jd_path:
        raise ValueError(f"Could not find JD for role {role_id}: jd_id={jd_id}")
    if not resume_version_path:
        raise ValueError(f"Could not find generated resume version for role {role_id}")

    jd, jd_body, _ = read_md(jd_path)
    resume_version, _, _ = read_md(resume_version_path)

    master_file = resume_version.get("resume_master_file", "")
    master_path = repo_root / master_file
    if not master_path.exists():
        raise ValueError(f"Could not find master resume file: {master_file}")
    master_fm, master_body, _ = read_md(master_path)

    assembled_id = f"resume-{slug}-assembled-v1"
    application_package_id = f"application-{slug}-v1"
    company = role.get("company", "")
    role_title = role.get("normalized_title") or role.get("source_title") or role.get("title", "")
    keywords = extract_jd_keywords(jd_body)

    fm = {
        "id": assembled_id,
        "slug": f"{slug}-assembled-v1",
        "type": "assembled_resume",
        "title": f"{company} {role_title} Assembled Resume v1",
        "categories": ["[[Careers]]", "[[Resumes]]", "[[Applications]]"],
        "tags": ["career", "resume", "assembled"],
        "status": "draft",
        "version": "v1",
        "created": role.get("created", ""),
        "last": role.get("last", ""),
        "company": company,
        "company_slug": role.get("company_slug", ""),
        "role_id": role_id,
        "jd_id": jd.get("id", ""),
        "resume_version_id": resume_version.get("id", ""),
        "resume_master_id": resume_version.get("resume_master_id", ""),
        "resume_master_file": master_file,
        "resume_family": resume_version.get("resume_family", ""),
        "role_family": role.get("role_family", ""),
        "role_level": role.get("role_level", ""),
        "role_qualifiers": role.get("role_qualifiers", []),
        "role_code": role.get("role_code", ""),
        "application_package_id": application_package_id,
        "origin": "generated",
        "run_id": run_id,
    }

    keyword_lines = "\n".join([f"- {k}" for k in keywords]) if keywords else "- TBD"
    body = f"""# {company} — {role_title} — Assembled Resume v1

## Assembly Summary

- Company: {company}
- Role: {role_title}
- Role ID: {role_id}
- JD ID: {jd.get("id", "")}
- Resume version ID: {resume_version.get("id", "")}
- Master resume: {master_file}
- Resume family: {resume_version.get("resume_family", "")}
- Role code: {role.get("role_code", "")}

## Tailoring Checklist

Review and tailor the full resume below before submitting.

### JD Keywords Detected

{keyword_lines}

### Manual Tailoring Steps

- Adjust the professional summary toward this role.
- Reorder or trim core strengths based on the JD.
- Emphasize the most relevant Gresham/FRBNY bullets.
- Keep claims truthful and consistent with actual experience.
- Export final version to PDF after review.

---

## Resume Body

{clean_master_body(master_body)}
"""

    out = output_dir / f"{assembled_id}.md"
    out.write_text(render_frontmatter(fm) + "\n" + body, encoding="utf-8")
    return out

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    roles = sorted(input_dir.glob("*.md"))
    if not roles:
        print(f"No role files found in {input_dir}")
        return 1

    for role_path in roles:
        out = assemble_resume(role_path, output_dir, args.run_id, repo_root)
        print(f"assembled resume: {role_path.name} -> {out.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
