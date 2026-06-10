#!/usr/bin/env python3

import json
import sys
from collections import Counter
from pathlib import Path


TOP_STORIES = 3
TOP_SKILLS = 5
TOP_THEMES = 8


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: recommend_interview_assets.py "
            "<scored-match-json> <output-json>"
        )
        sys.exit(1)

    scored_match = load_json(sys.argv[1])

    ranked_stories = scored_match.get("ranked_stories", [])
    ranked_skills = scored_match.get("ranked_skills", [])

    theme_counts = Counter()
    for story in ranked_stories:
        for theme in story.get("interview_themes", []):
            theme_counts[theme] += story.get("score", 0)

    result = {
        "jd_path": scored_match.get("jd_path"),
        "source_id": scored_match.get("source_id"),
        "recommendation_model": "v0.5.6",
        "recommended_interview_stories": ranked_stories[:TOP_STORIES],
        "recommended_interview_skills": ranked_skills[:TOP_SKILLS],
        "recommended_interview_themes": [
            {"theme": theme, "score": score}
            for theme, score in theme_counts.most_common(TOP_THEMES)
        ]
    }

    Path(sys.argv[2]).write_text(
        json.dumps(result, indent=2),
        encoding="utf-8"
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
