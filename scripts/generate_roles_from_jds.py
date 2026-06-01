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
        "source_title", "normalized_title",
        "role_family", "role_level", "role_qualifiers", "role_code", "role_code_confidence", "role_summary",
        "role_source_type",
        "jd_ids", "resume_ids", "cover_letter_ids", "event_ids",
        "tracker_scope", "active_in_teal"
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

def role_summary_from_jd(jd: dict[str, Any]) -> str:
    company = jd.get("company", "")
    title = jd.get("normalized_title") or jd.get("source_title") or jd.get("title", "")
    code = jd.get("role_code", "")
    return f"{title} role at {company} classified as {code}."

def generate_role(jd_path: Path, output_dir: Path, run_id: str) -> Path:
    text = jd_path.read_text(encoding="utf-8")
    fm_text, _body = split_frontmatter(text)
    jd = parse_simple_yaml(fm_text)

    role_id = jd.get("role_id", "")
    if not role_id:
        raise ValueError(f"Missing role_id in {jd_path}")

    role_slug = role_id.removeprefix("role-")
    jd_id = jd.get("id", "")
    company = jd.get("company", "")
    normalized_title = jd.get("normalized_title") or jd.get("source_title") or jd.get("title", "")
    title = f"{normalized_title} - {company}" if company else normalized_title

    role = {
        "id": role_id,
        "slug": role_slug,
        "type": "role",
        "title": title,
        "categories": ["[[Careers]]", "[[Roles]]"],
        "tags": ["career", "role", "generated"],
        "status": "active",
        "version": "v1",
        "created": jd.get("created", ""),
        "last": jd.get("last", ""),
        "company": company,
        "company_slug": jd.get("company_slug", ""),
        "source_system": "career-system",
        "source_file": jd_path.name,
        "source_url": jd.get("source_url", ""),
        "origin": "generated",
        "run_id": run_id,
        "source_title": jd.get("source_title", ""),
        "normalized_title": normalized_title,
        "role_family": jd.get("role_family", ""),
        "role_level": jd.get("role_level", ""),
        "role_qualifiers": jd.get("role_qualifiers", []),
        "role_code": jd.get("role_code", ""),
        "role_code_confidence": jd.get("role_code_confidence", ""),
        "role_summary": role_summary_from_jd(jd),
        "role_source_type": "jd",
        "jd_ids": [jd_id] if jd_id else [],
        "resume_ids": [],
        "cover_letter_ids": [],
        "event_ids": [],
        "tracker_scope": "",
        "active_in_teal": "",
    }

    body = f"""# {title}

## Role Summary

{role["role_summary"]}

## Linked Job Descriptions

- {jd_id}

## Resume Strategy

TBD.

## Notes

Generated from normalized JD file:

```text
{jd_path.name}
```
"""
    out = output_dir / f"{role_id}.md"
    out.write_text(render_frontmatter(role) + "\n" + body, encoding="utf-8")
    return out

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(input_dir.glob("*.md"))
    if not files:
        print(f"No normalized JD markdown files found in {input_dir}")
        return 1

    for f in files:
        out = generate_role(f, output_dir, args.run_id)
        print(f"generated role: {f.name} -> {out.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
