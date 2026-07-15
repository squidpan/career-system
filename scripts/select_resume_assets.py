#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROFILE_MAP = {
    "ba": "ba",
    "bsa": "ba",
    "support": "support",
}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text.strip()

    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("Opening YAML front matter has no closing delimiter.")

    frontmatter = text[4:end].strip()
    body = text[end + 4 :].strip()
    return frontmatter, body


def read_frontmatter_value(frontmatter: str, key: str) -> str:
    match = re.search(
        rf"(?m)^{re.escape(key)}:\s*[\"']?([^\"'\n]*)[\"']?\s*$",
        frontmatter,
    )
    return match.group(1).strip() if match else ""


def read_role_family(normalized_jd: Path) -> str:
    text = normalized_jd.read_text(encoding="utf-8")
    frontmatter, _ = split_frontmatter(text)
    role_family = read_frontmatter_value(frontmatter, "role_family")

    if not role_family:
        raise ValueError(
            f"Missing role_family in normalized JD: {normalized_jd}"
        )

    return role_family.lower()


def read_asset_body(path: Path, expected_type: str) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Resume Asset not found: {path}")

    frontmatter, body = split_frontmatter(
        path.read_text(encoding="utf-8")
    )

    status = read_frontmatter_value(frontmatter, "status")
    asset_type = read_frontmatter_value(frontmatter, "asset_type")

    if status != "approved":
        raise ValueError(f"Resume Asset is not approved: {path}")

    if asset_type != expected_type:
        raise ValueError(
            f"Expected asset_type={expected_type}, "
            f"found {asset_type or '(missing)'}: {path}"
        )

    if not body:
        raise ValueError(f"Resume Asset body is empty: {path}")

    return body


def write_output(path: Path, body: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"Output already exists; use --force to replace it: {path}"
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Select approved Resume Assets using normalized role_family "
            "and publish legacy-compatible bridge artifacts."
        )
    )
    parser.add_argument("--normalized-jd", required=True, type=Path)
    parser.add_argument("--job-slug", required=True)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("."),
        help="Root under which data/application-summaries and "
             "data/resume-sections are written.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing bridge artifacts.",
    )
    args = parser.parse_args()

    if not args.normalized_jd.is_file():
        parser.error(
            f"Normalized JD not found: {args.normalized_jd}"
        )

    repo_root = Path(__file__).resolve().parents[1]
    role_family = read_role_family(args.normalized_jd)
    profile = PROFILE_MAP.get(role_family, "default")
    fallback_used = profile == "default" and role_family != "default"

    summary_asset = (
        repo_root
        / "data/resume-assets/professional-summary"
        / f"professional-summary-{profile}.md"
    )
    frbny_asset = (
        repo_root
        / "data/resume-assets/frbny"
        / f"frbny-{profile}.md"
    )

    summary_body = read_asset_body(
        summary_asset,
        "professional-summary",
    )
    frbny_body = read_asset_body(frbny_asset, "frbny")

    summary_output = (
        args.output_root
        / "data/application-summaries"
        / f"{args.job_slug}-summary-v1.md"
    )
    frbny_output = (
        args.output_root
        / "data/resume-sections"
        / f"{args.job_slug}-frbny-section.md"
    )

    write_output(summary_output, summary_body, args.force)
    write_output(frbny_output, frbny_body, args.force)

    print(f"role_family: {role_family}")
    print(f"content_profile: {profile}")
    print(f"fallback_used: {str(fallback_used).lower()}")
    print(f"professional_summary_asset: {summary_asset}")
    print(f"frbny_asset: {frbny_asset}")
    print(f"professional_summary_output: {summary_output}")
    print(f"frbny_output: {frbny_output}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, FileExistsError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
