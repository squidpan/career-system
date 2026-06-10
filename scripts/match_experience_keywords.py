#!/usr/bin/env python3

import json
import sys
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize(text):
    return text.lower().strip()


def main():
    if len(sys.argv) < 3:
        print("Usage: match_experience_keywords.py <keyword-map-json> <comma-separated-keywords>")
        sys.exit(1)

    keyword_map_path = Path(sys.argv[1])
    input_keywords = [normalize(k) for k in sys.argv[2].split(",") if k.strip()]

    data = load_json(keyword_map_path)

    matched_groups = []
    matched_skills = set()
    matched_evidence = set()
    matched_stories = set()

    for group in data.get("keyword_groups", []):
        group_keywords = [normalize(k) for k in group.get("keywords", [])]

        hits = sorted(set(input_keywords).intersection(group_keywords))

        if hits:
            matched_groups.append({
                "group_id": group.get("group_id"),
                "matched_keywords": hits,
                "skill_ids": group.get("skill_ids", []),
                "evidence_ids": group.get("evidence_ids", []),
                "story_ids": group.get("story_ids", [])
            })

            matched_skills.update(group.get("skill_ids", []))
            matched_evidence.update(group.get("evidence_ids", []))
            matched_stories.update(group.get("story_ids", []))

    result = {
        "input_keywords": input_keywords,
        "source_id": data.get("source_id"),
        "source_release": data.get("source_release"),
        "matched_group_count": len(matched_groups),
        "matched_groups": matched_groups,
        "matched_skill_ids": sorted(matched_skills),
        "matched_evidence_ids": sorted(matched_evidence),
        "matched_story_ids": sorted(matched_stories)
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
