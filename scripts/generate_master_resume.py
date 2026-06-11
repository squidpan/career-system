#!/usr/bin/env python3

import json
import sys
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 5:
        print(
            "Usage: generate_master_resume.py "
            "<skills-json> <resume-evidence-index-json> <interview-stories-index-json> <output-md>"
        )
        sys.exit(1)

    skills_path = Path(sys.argv[1])
    evidence_path = Path(sys.argv[2])
    stories_path = Path(sys.argv[3])
    output_path = Path(sys.argv[4])

    skills = load_json(skills_path)
    evidence = load_json(evidence_path)
    stories = load_json(stories_path)

    lines = []

    lines.append("# Master Resume v1")
    lines.append("")
    lines.append("## Professional Summary")
    lines.append("")
    lines.append(
        "Senior Business Analyst and Application Support professional with experience supporting "
        "mission-critical fixed-income market-data pricing platforms, production operations, "
        "data validation workflows, Oracle-based distribution models, technical refresh initiatives, "
        "and cloud/API modernization efforts."
    )
    lines.append("")

    lines.append("## Core Skills")
    lines.append("")
    for skill in skills.get("skills", []):
        lines.append(f"- {skill.get('name')} (`{skill.get('skill_id')}`)")
    lines.append("")

    lines.append("## Federal Reserve Bank of New York")
    lines.append("")
    lines.append("**Senior Business Analyst / DevOps Release Coordinator**")
    lines.append("")
    lines.append("Apr 2017 – Feb 2026")
    lines.append("")

    lines.append("### Experience Evidence")
    lines.append("")
    for item in evidence.get("evidence", []):
        lines.append(f"#### {item.get('title')}")
        lines.append("")
        lines.append(item.get("summary", ""))
        lines.append("")
        lines.append("Skills:")
        for skill_id in item.get("skill_ids", []):
            lines.append(f"- `{skill_id}`")
        lines.append("")
        lines.append("Source:")
        lines.append(f"- `{item.get('source_path')}`")
        lines.append("")

    lines.append("## Selected Interview Story References")
    lines.append("")
    for story in stories.get("stories", []):
        lines.append(f"### {story.get('title')}")
        lines.append("")
        lines.append(story.get("summary", ""))
        lines.append("")
        lines.append("Themes:")
        for theme in story.get("interview_themes", []):
            lines.append(f"- {theme}")
        lines.append("")
        lines.append("Source:")
        lines.append(f"- `{story.get('source_path')}`")
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append(
        "This master resume is generated from Career System metadata indexes. "
        "It is not a final application resume. Use it as the source for tailored resume generation."
    )
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
