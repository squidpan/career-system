#!/usr/bin/env python3
from __future__ import annotations

import argparse
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
        "id", "slug", "type", "title",
        "categories", "tags",
        "status", "version", "created", "last",
        "company", "company_slug",
        "source_system", "source_file", "source_url",
        "origin", "run_id",
        "role_id", "jd_id",
        "resume_master_id", "resume_master_file",
        "resume_family",
        "role_family", "role_level", "role_qualifiers", "role_code",
        "submitted_date", "submitted_to"
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

def generate_resume_version(role_path: Path, output_dir: Path, run_id: str, repo_root: Path) -> Path:
    text = role_path.read_text(encoding="utf-8")
    fm_text, _body = split_frontmatter(text)
    role = parse_simple_yaml(fm_text)

    role_id = role.get("id", "")
    role_slug = role.get("slug", role_id.removeprefix("role-"))
    role_code = role.get("role_code", "")
    company = role.get("company", "")
    company_slug = role.get("company_slug", "")
    resume_family = role.get("recommended_resume_family", "")
    resume_master_id = role.get("recommended_resume_master_id", "")
    resume_master_file = role.get("recommended_resume_file", "")
    jd_id = first_item(role.get("jd_ids", []))

    if not role_id:
        raise ValueError(f"Missing role id in {role_path}")
    if not resume_master_id:
        raise ValueError(f"Missing recommended_resume_master_id in {role_path}")

    # Resume version id intentionally drops role- prefix and uses v1.
    resume_slug = role_slug
    resume_id = f"resume-{resume_slug}-v1"
    title = f"{company} {role_code} Resume v1".strip()

    data = {
        "id": resume_id,
        "slug": f"{resume_slug}-v1",
        "type": "resume_version",
        "title": title,
        "categories": ["[[Careers]]", "[[Resumes]]", "[[Applications]]"],
        "tags": ["career", "resume", "generated"],
        "status": "draft",
        "version": "v1",
        "created": role.get("created", ""),
        "last": role.get("last", ""),
        "company": company,
        "company_slug": company_slug,
        "source_system": "career-system",
        "source_file": role_path.name,
        "source_url": role.get("source_url", ""),
        "origin": "generated",
        "run_id": run_id,
        "role_id": role_id,
        "jd_id": jd_id,
        "resume_master_id": resume_master_id,
        "resume_master_file": resume_master_file,
        "resume_family": resume_family,
        "role_family": role.get("role_family", ""),
        "role_level": role.get("role_level", ""),
        "role_qualifiers": role.get("role_qualifiers", []),
        "role_code": role_code,
        "submitted_date": "",
        "submitted_to": "",
    }

    master_excerpt = ""
    master_path = repo_root / resume_master_file if resume_master_file else None
    if master_path and master_path.exists():
        master_text = master_path.read_text(encoding="utf-8")
        master_excerpt = master_text[:3000].rstrip()
    else:
        master_excerpt = f"Master resume file not found: {resume_master_file}"

    body = f"""# {title}

## Resume Version Summary

Generated first-pass resume version for:

- Role ID: {role_id}
- JD ID: {jd_id}
- Company: {company}
- Role code: {role_code}
- Resume family: {resume_family}
- Resume master: {resume_master_id}
- Resume master file: {resume_master_file}

## Tailoring Notes

TBD.

## JD / Role Alignment

TBD.

## Source Master Resume Excerpt

```markdown
{master_excerpt}
```

## Generated From

```text
{role_path.name}
```
"""
    out = output_dir / f"{resume_id}.md"
    out.write_text(render_frontmatter(data) + "\n" + body, encoding="utf-8")
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

    files = sorted(input_dir.glob("*.md"))
    if not files:
        print(f"No role markdown files found in {input_dir}")
        return 1

    for f in files:
        out = generate_resume_version(f, output_dir, args.run_id, repo_root)
        print(f"generated resume version: {f.name} -> {out.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
