#!/usr/bin/env python3

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


PRIORITY_WEIGHT = {
    "critical": 25,
    "high": 15,
    "medium": 8,
    "low": 3
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def index_by(items, key):
    return {item[key]: item for item in items}


def score_item(item_id, count, metadata_index):
    item = metadata_index.get(item_id, {})
    priority = item.get("priority", "medium")
    return (count * 20) + PRIORITY_WEIGHT.get(priority, 8)


def main():
    if len(sys.argv) != 5:
        print(
            "Usage: score_experience_match.py "
            "<match-json> <skills-json> <resume-evidence-index-json> <interview-stories-index-json>"
        )
        sys.exit(1)

    match_path = Path(sys.argv[1])
    skills_path = Path(sys.argv[2])
    evidence_path = Path(sys.argv[3])
    stories_path = Path(sys.argv[4])

    match = load_json(match_path)
    skills = load_json(skills_path)
    evidence = load_json(evidence_path)
    stories = load_json(stories_path)

    skill_index = index_by(skills.get("skills", []), "skill_id")
    evidence_index = index_by(evidence.get("evidence", []), "evidence_id")
    story_index = index_by(stories.get("stories", []), "story_id")

    skill_counts = Counter()
    evidence_counts = Counter()
    story_counts = Counter()

    evidence_keyword_hits = defaultdict(list)
    story_keyword_hits = defaultdict(list)

    for group in match.get("matched_groups", []):
        hits = group.get("matched_keywords", [])

        for sid in group.get("skill_ids", []):
            skill_counts[sid] += len(hits)

        for eid in group.get("evidence_ids", []):
            evidence_counts[eid] += len(hits)
            evidence_keyword_hits[eid].extend(hits)

        for stid in group.get("story_ids", []):
            story_counts[stid] += len(hits)
            story_keyword_hits[stid].extend(hits)

    ranked_skills = []
    for sid, count in skill_counts.items():
        meta = skill_index.get(sid, {})
        ranked_skills.append({
            "skill_id": sid,
            "name": meta.get("name", sid),
            "category": meta.get("category"),
            "score": score_item(sid, count, {sid: {"priority": "medium"}}),
            "hit_count": count
        })

    ranked_evidence = []
    for eid, count in evidence_counts.items():
        meta = evidence_index.get(eid, {})
        ranked_evidence.append({
            "evidence_id": eid,
            "title": meta.get("title", eid),
            "score": score_item(eid, count, evidence_index),
            "hit_count": count,
            "matched_keywords": sorted(set(evidence_keyword_hits[eid])),
            "resume_families": meta.get("resume_families", []),
            "source_path": meta.get("source_path")
        })

    ranked_stories = []
    for stid, count in story_counts.items():
        meta = story_index.get(stid, {})
        ranked_stories.append({
            "story_id": stid,
            "title": meta.get("title", stid),
            "score": score_item(stid, count, story_index),
            "hit_count": count,
            "matched_keywords": sorted(set(story_keyword_hits[stid])),
            "interview_themes": meta.get("interview_themes", []),
            "source_path": meta.get("source_path")
        })

    ranked_skills.sort(key=lambda x: x["score"], reverse=True)
    ranked_evidence.sort(key=lambda x: x["score"], reverse=True)
    ranked_stories.sort(key=lambda x: x["score"], reverse=True)

    result = {
        "jd_path": match.get("jd_path"),
        "source_id": match.get("source_id"),
        "source_release": match.get("source_release"),
        "scoring_model": "deterministic_v0.5.4",
        "ranked_skills": ranked_skills,
        "ranked_evidence": ranked_evidence,
        "ranked_stories": ranked_stories
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
