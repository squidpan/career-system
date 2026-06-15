#!/usr/bin/env python3

import json
import sys
from pathlib import Path


BULLET_LIBRARY = {
    "mrprice_market_data_platform_support": [
        "Supported enterprise market-data pricing platform that normalized, validated, consolidated, and distributed fixed-income pricing from multiple vendor feeds to downstream consumers.",
        "Supported market-data workflows involving vendor feeds, pricing validation, fixed-income data, and downstream consumer delivery."
    ],
    "mrprice_production_support_operations": [
        "Provided production support for Linux/Oracle market-data platform, including monitoring, incident investigation, operational checks, and cross-team escalation.",
        "Investigated production issues involving market-data feeds, validation workflows, application behavior, and downstream consumer impact."
    ],
    "mrprice_cloud_migration_oracle_to_rest": [
    "Supported modernization of a real-time streaming market data pricing platform, transitioning distribution from Oracle consumer views toward REST API payloads and service-based access.",
    "Assisted cloud migration validation by comparing legacy Oracle-based data access patterns with emerging REST API delivery models."
    ],
"mrprice_oracle_distribution_consumer_views": [
    "Supported Oracle-based real-time streaming market data pricing distribution using master and consumer-specific views for downstream trading and financial applications.",
    "Analyzed consumer data requirements and Oracle view outputs used by downstream systems."
    ],
    "mrprice_technical_refresh": [
        "Supported technical refresh initiative that reduced custom code, improved maintainability, and leveraged platform out-of-box functionality.",
        "Participated in modernization activities involving legacy workflow analysis, data-load redesign, testing, and stakeholder coordination."
    ],
    "mrprice_tick_consolidation_data_quality": [
        "Supported pricing-data quality processes including vendor tick validation, CUSIP alignment, exception review, and consolidated price distribution.",
        "Assisted validation workflows for missing ticks, stale prices, bid/ask spread exceptions, and pricing anomalies."
    ],
    "mrprice_governance_four_eyes_controls": [
        "Supported controlled price-cleansing workflows using four-eyes review, exception queues, and audit-ready approval processes.",
        "Helped maintain pricing integrity through governed validation and approval workflows."
    ]
}


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_resume_bullets.py <resume-recommendation-json> <output-md>")
        sys.exit(1)

    recommendation_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    recommendation = load_json(recommendation_path)

    lines = []
    lines.append("# Resume Draft Assistance")
    lines.append("")
    lines.append(f"Source JD: `{recommendation.get('jd_path')}`")
    lines.append(f"Source Experience: `{recommendation.get('source_id')}`")
    lines.append("")
    lines.append("## Recommended Skills")
    lines.append("")

    for skill in recommendation.get("recommended_skills", []):
        lines.append(f"- {skill.get('name')} (`{skill.get('skill_id')}`)")

    lines.append("")
    lines.append("## Candidate Resume Bullets")
    lines.append("")

    used = set()

    for evidence in recommendation.get("recommended_resume_evidence", []):
        evidence_id = evidence.get("evidence_id")
        title = evidence.get("title", evidence_id)

        lines.append(f"### {title}")
        lines.append("")

        bullets = BULLET_LIBRARY.get(evidence_id, [])

        if not bullets:
            lines.append(f"- TODO: Add bullet library entry for `{evidence_id}`.")
        else:
            for bullet in bullets:
                if bullet not in used:
                    lines.append(f"- {bullet}")
                    used.add(bullet)

        lines.append("")
        lines.append("Matched keywords:")
        for kw in evidence.get("matched_keywords", []):
            lines.append(f"- `{kw}`")
        lines.append("")

    lines.append("## Recommended Interview Stories")
    lines.append("")

    for story in recommendation.get("recommended_interview_stories", []):
        lines.append(f"- {story.get('title')} (`{story.get('story_id')}`)")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
