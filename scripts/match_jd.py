#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def extract_keywords(text: str, keyword_groups: list[dict]) -> list[str]:
    normalized_text = normalize(text)
    all_keywords = set()

    for group in keyword_groups:
        for kw in group.get("keywords", []):
            kw_norm = normalize(kw)
            if kw_norm in normalized_text:
                all_keywords.add(kw_norm)

    return sorted(all_keywords)


def main():
    if len(sys.argv) != 4:
        print("Usage: match_jd.py <jd-file> <keyword-map-json> <output-json>")
        sys.exit(1)

    jd_path = Path(sys.argv[1])
    keyword_map_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    jd_text = jd_path.read_text(encoding="utf-8", errors="ignore")
    keyword_map = load_json(keyword_map_path)

    extracted_keywords = extract_keywords(jd_text, keyword_map.get("keyword_groups", []))

    matched_groups = []
    matched_skills = set()
    matched_evidence = set()
    matched_stories = set()

    for group in keyword_map.get("keyword_groups", []):
        group_keywords = {normalize(k) for k in group.get("keywords", [])}
        hits = sorted(set(extracted_keywords).intersection(group_keywords))

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
        "jd_path": str(jd_path),
        "source_id": keyword_map.get("source_id"),
        "source_release": keyword_map.get("source_release"),
        "extracted_keyword_count": len(extracted_keywords),
        "extracted_keywords": extracted_keywords,
        "matched_group_count": len(matched_groups),
        "matched_groups": matched_groups,
        "matched_skill_ids": sorted(matched_skills),
        "matched_evidence_ids": sorted(matched_evidence),
        "matched_story_ids": sorted(matched_stories)
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
