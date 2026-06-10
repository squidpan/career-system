#!/usr/bin/env python3

import json
import sys
from pathlib import Path


TOP_SKILLS = 5
TOP_EVIDENCE = 3
TOP_STORIES = 2


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: recommend_resume_assets.py "
            "<scored-match-json> <output-json>"
        )
        sys.exit(1)

    scored_match = load_json(sys.argv[1])

    result = {
        "jd_path": scored_match.get("jd_path"),
        "source_id": scored_match.get("source_id"),
        "recommendation_model": "v0.5.5",
        "recommended_skills":
            scored_match.get("ranked_skills", [])[:TOP_SKILLS],
        "recommended_resume_evidence":
            scored_match.get("ranked_evidence", [])[:TOP_EVIDENCE],
        "recommended_interview_stories":
            scored_match.get("ranked_stories", [])[:TOP_STORIES]
    }

    Path(sys.argv[2]).write_text(
        json.dumps(result, indent=2),
        encoding="utf-8"
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
