#!/usr/bin/env python3

import json
import sys
from pathlib import Path


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_file(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    if len(sys.argv) != 6:
        print(
            "Usage: generate_application_package.py "
            "<application-id> <resume-md> <resume-recommendation-json> "
            "<interview-recommendation-json> <output-dir>"
        )
        sys.exit(1)

    application_id = sys.argv[1]
    resume_path = Path(sys.argv[2])
    resume_recommendation_path = Path(sys.argv[3])
    interview_recommendation_path = Path(sys.argv[4])
    output_dir = Path(sys.argv[5])

    resume_text = resume_path.read_text(encoding="utf-8")
    resume_recommendation = load_json(resume_recommendation_path)
    interview_recommendation = load_json(interview_recommendation_path)

    package_dir = output_dir / application_id
    package_dir.mkdir(parents=True, exist_ok=True)

    write_file(package_dir / "resume.md", resume_text)

    summary_lines = [
        "# Application Summary",
        "",
        f"Application ID: `{application_id}`",
        f"Source JD: `{resume_recommendation.get('jd_path')}`",
        f"Experience Source: `{resume_recommendation.get('source_id')}`",
        "",
        "## Recommended Skills",
        ""
    ]

    for skill in resume_recommendation.get("recommended_skills", []):
        summary_lines.append(f"- {skill.get('name')} (`{skill.get('skill_id')}`)")

    summary_lines.extend([
        "",
        "## Resume Evidence Used",
        ""
    ])

    for evidence in resume_recommendation.get("recommended_resume_evidence", []):
        summary_lines.append(f"- {evidence.get('title')} (`{evidence.get('evidence_id')}`)")

    summary_lines.extend([
        "",
        "## Interview Stories To Prepare",
        ""
    ])

    for story in resume_recommendation.get("recommended_interview_stories", []):
        summary_lines.append(f"- {story.get('title')} (`{story.get('story_id')}`)")

    write_file(package_dir / "application-summary.md", "\n".join(summary_lines))

    prep_lines = [
        "# Interview Prep",
        "",
        f"Application ID: `{application_id}`",
        "",
        "## Recommended Interview Stories",
        ""
    ]

    for story in interview_recommendation.get("recommended_interview_stories", []):
        prep_lines.append(f"### {story.get('title')}")
        prep_lines.append("")
        prep_lines.append("Matched keywords:")
        for kw in story.get("matched_keywords", []):
            prep_lines.append(f"- `{kw}`")
        prep_lines.append("")
        prep_lines.append("Themes:")
        for theme in story.get("interview_themes", []):
            prep_lines.append(f"- {theme}")
        prep_lines.append("")

    prep_lines.extend([
        "## Interview Themes",
        ""
    ])

    for theme in interview_recommendation.get("recommended_interview_themes", []):
        prep_lines.append(f"- {theme.get('theme')}")

    write_file(package_dir / "interview-prep.md", "\n".join(prep_lines))

    cover_letter_lines = [
        "# Cover Letter Notes",
        "",
        f"Application ID: `{application_id}`",
        "",
        "## Positioning Notes",
        "",
        "Use the tailored resume and recommended evidence to draft a role-specific cover letter.",
        "",
        "## Suggested Themes",
        ""
    ]

    for skill in resume_recommendation.get("recommended_skills", [])[:5]:
        cover_letter_lines.append(f"- {skill.get('name')}")

    write_file(package_dir / "cover-letter-notes.md", "\n".join(cover_letter_lines))

    manifest = {
        "application_id": application_id,
        "resume": "resume.md",
        "application_summary": "application-summary.md",
        "interview_prep": "interview-prep.md",
        "cover_letter_notes": "cover-letter-notes.md",
        "source_resume": str(resume_path),
        "source_resume_recommendation": str(resume_recommendation_path),
        "source_interview_recommendation": str(interview_recommendation_path)
    }

    write_file(package_dir / "package-manifest.json", json.dumps(manifest, indent=2))

    print(f"Wrote application package: {package_dir}")


if __name__ == "__main__":
    main()
