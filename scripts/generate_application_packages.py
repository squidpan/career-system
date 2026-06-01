#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
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
    order = ["id", "type", "title", "categories", "tags", "status", "version", "created", "last", "company", "company_slug", "role_id", "jd_id", "resume_id", "application_package_id", "origin", "run_id"]
    lines = ["---"]
    for key in order:
        value = data.get(key, "")
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n"

def first_item(value: Any) -> str:
    if isinstance(value, list) and value:
        return value[0]
    if isinstance(value, str):
        return value
    return ""

def read_md_meta(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(text)
    return parse_simple_yaml(fm)

def find_file_by_id(directory: Path, item_id: str) -> Path | None:
    if not item_id:
        return None
    direct = directory / f"{item_id}.md"
    if direct.exists():
        return direct
    for p in sorted(directory.glob("*.md")):
        try:
            if read_md_meta(p).get("id") == item_id:
                return p
        except Exception:
            pass
    return None

def find_resume_for_role(resume_dir: Path, role_id: str) -> Path | None:
    for p in sorted(resume_dir.glob("*.md")):
        try:
            if read_md_meta(p).get("role_id") == role_id:
                return p
        except Exception:
            pass
    return None

def write_cover_letter(package_dir: Path, run_id: str, role: dict[str, Any], jd: dict[str, Any], resume: dict[str, Any], app_id: str) -> tuple[str, Path]:
    company = role.get("company", "")
    role_title = role.get("normalized_title") or role.get("source_title") or role.get("title", "")
    role_id = role.get("id", "")
    jd_id = jd.get("id", "")
    resume_id = resume.get("id", "")
    cover_id = f"cover-{app_id.removeprefix('application-')}"
    title = f"{company} Cover Letter Draft v1"
    fm = {
        "id": cover_id,
        "type": "cover_letter",
        "title": title,
        "categories": ["[[Careers]]", "[[CoverLetters]]", "[[Applications]]"],
        "tags": ["career", "cover-letter", "generated"],
        "status": "draft",
        "version": "v1",
        "created": role.get("created", ""),
        "last": role.get("last", ""),
        "company": company,
        "company_slug": role.get("company_slug", ""),
        "role_id": role_id,
        "jd_id": jd_id,
        "resume_id": resume_id,
        "application_package_id": app_id,
        "origin": "generated",
        "run_id": run_id,
    }
    body = f"""# {title}

Dear Hiring Team,

I am interested in the {role_title} opportunity at {company}.

## Draft Notes

- Align opening paragraph to the role.
- Pull 2–3 strongest matches from the generated resume.
- Reference relevant domain experience from FRBNY/AIG/EmblemHealth where appropriate.
- Keep the final letter concise and specific.

## Role Alignment

- Role ID: {role_id}
- JD ID: {jd_id}
- Resume ID: {resume_id}

## Resume Evidence

TBD.

## Closing

TBD.
"""
    out = package_dir / "cover-letter.md"
    out.write_text(render_frontmatter(fm) + "\n" + body, encoding="utf-8")
    return cover_id, out

def generate_package(role_path: Path, output_dir: Path, run_id: str, repo_root: Path) -> Path:
    role = read_md_meta(role_path)
    role_id = role.get("id", "")
    slug = role.get("slug", role_id.removeprefix("role-"))
    app_id = f"application-{slug}-v1"
    package_dir = output_dir / app_id
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)
    jd_id = first_item(role.get("jd_ids", []))
    jd_path = find_file_by_id(repo_root / "data" / "jds" / "normalized", jd_id)
    resume_path = find_resume_for_role(repo_root / "data" / "resume-versions" / "generated", role_id)
    if not jd_path:
        raise ValueError(f"Could not find JD for role {role_id}: jd_id={jd_id}")
    if not resume_path:
        raise ValueError(f"Could not find resume for role {role_id}")
    jd = read_md_meta(jd_path)
    resume = read_md_meta(resume_path)
    shutil.copyfile(role_path, package_dir / "role.md")
    shutil.copyfile(jd_path, package_dir / "jd.md")
    shutil.copyfile(resume_path, package_dir / "resume.md")
    cover_id, cover_path = write_cover_letter(package_dir, run_id, role, jd, resume, app_id)
    manifest = {
        "application_package_id": app_id,
        "company": role.get("company", ""),
        "company_slug": role.get("company_slug", ""),
        "role_id": role_id,
        "jd_id": jd.get("id", ""),
        "resume_id": resume.get("id", ""),
        "cover_letter_id": cover_id,
        "package_status": "draft",
        "created": role.get("created", ""),
        "last": role.get("last", ""),
        "source_files": {
            "role": str(role_path),
            "jd": str(jd_path),
            "resume": str(resume_path),
            "cover_letter": str(cover_path),
        },
    }
    (package_dir / "application-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return package_dir

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    roles = sorted(Path(args.input_dir).glob("*.md"))
    if not roles:
        print(f"No role files found in {args.input_dir}")
        return 1
    for role_path in roles:
        package_dir = generate_package(role_path, output_dir, args.run_id, repo_root)
        print(f"generated application package: {role_path.name} -> {package_dir.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
