#!/usr/bin/env python3

import json
import sys
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 4:
        print("Usage: assemble_resume.py <resume-recommendation-json> <resume-section-md> <output-md>")
        sys.exit(1)

    recommendation_path = Path(sys.argv[1])
    section_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    recommendation = load_json(recommendation_path)
    section_text = section_path.read_text(encoding="utf-8")

    lines = []
    lines.append("# Tailored Resume Draft")
    lines.append("")
    lines.append(f"Source JD: `{recommendation.get('jd_path')}`")
    lines.append(f"Experience Source: `{recommendation.get('source_id')}`")
    lines.append("")
    lines.append("## Targeted Skills")
    lines.append("")

    for skill in recommendation.get("recommended_skills", []):
        lines.append(f"- {skill.get('name')}")

    lines.append("")
    lines.append(section_text)
    lines.append("")
    lines.append("## Resume Evidence Used")
    lines.append("")

    for evidence in recommendation.get("recommended_resume_evidence", []):
        lines.append(f"- {evidence.get('title')} (`{evidence.get('evidence_id')}`)")

    lines.append("")
    lines.append("## Interview Stories To Prepare")
    lines.append("")

    for story in recommendation.get("recommended_interview_stories", []):
        lines.append(f"- {story.get('title')} (`{story.get('story_id')}`)")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
