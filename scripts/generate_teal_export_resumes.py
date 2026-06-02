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

def read_md(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    return parse_simple_yaml(fm), body

def extract_resume_body(body: str) -> str:
    marker = "\n## Resume Body\n"
    if marker in body:
        return body.split(marker, 1)[1].strip()
    if body.startswith("## Resume Body\n"):
        return body.split("## Resume Body\n", 1)[1].strip()
    return body.strip()

def normalize_for_teal(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^# .+?Assembled Resume v1\s*\n+", "", text)
    text = text.replace("# Paul Lyu — Master BA Resume", "Paul Lyu")
    text = text.replace("# Paul Lyu — Master SRE / Production Support Resume", "Paul Lyu")
    text = text.replace("Paul Lyu\n\nPaul Lyu", "Paul Lyu")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"

def output_name(input_path: Path, meta: dict[str, Any]) -> str:
    stem = input_path.stem
    stem = stem.replace("-assembled-v1", "-teal-v1")
    if not stem.endswith("-teal-v1"):
        slug = meta.get("slug", input_path.stem).replace("-assembled-v1", "")
        if slug.startswith("resume-"):
            stem = f"{slug}-teal-v1"
        else:
            stem = f"resume-{slug}-teal-v1"
    return f"{stem}.md"

def validate(text: str, source: Path) -> None:
    forbidden = [
        "Assembly Summary",
        "Tailoring Checklist",
        "JD Keywords",
        "Manual Tailoring Steps",
        "run_id:",
        "role_id:",
        "jd_id:",
        "application_package_id:",
        "resume_version_id:",
    ]
    for item in forbidden:
        if item in text:
            print(f"WARNING: {source.name}: found forbidden text: {item}")

    required = [
        "## Professional Summary",
        "## Work Experience",
        "## Skills",
    ]
    for item in required:
        if item not in text:
            print(f"WARNING: {source.name}: missing required section: {item}")

def generate_one(path: Path, output_dir: Path) -> Path:
    meta, body = read_md(path)
    teal_text = normalize_for_teal(extract_resume_body(body))
    validate(teal_text, path)
    out = output_dir / output_name(path, meta)
    out.write_text(teal_text, encoding="utf-8")
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
        print(f"No assembled resume files found in {input_dir}")
        return 1

    for path in files:
        out = generate_one(path, output_dir)
        print(f"generated teal export: {path.name} -> {out.name}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
