#!/usr/bin/env python3

import sys
from pathlib import Path


QUALITY_RULES = {
    "common": {
        "Federal Reserve Bank of New York": "Federal Reserve Bank of New York (On-Site)",
        "market-data platform": "streaming market-data platform",
        "fixed-income market-data platform": "streaming fixed-income market-data platform",
    },
    "finbourne": {
        "Provided application and production support": "Provided application and production support for mission-critical financial technology platforms",
        "monitoring, incident investigation": "monitoring, troubleshooting, incident investigation",
        "Supported application modernization work": "Supported application modernization and REST API transition work",
    },
    "citi": {
        "Partnered with stakeholders on modernization activities": "Partnered with stakeholders to analyze requirements and support modernization activities",
        "Supported enterprise modernization initiative": "Supported enterprise modernization initiative involving requirements analysis, workflow review, and platform transformation",
        "Analyzed stakeholder data requirements": "Analyzed stakeholder requirements, data needs, and Oracle view outputs",
    },
}


def apply_rules(text: str, target: str) -> str:
    result = text

    for old, new in QUALITY_RULES["common"].items():
        result = result.replace(old, new)

    for old, new in QUALITY_RULES.get(target, {}).items():
        result = result.replace(old, new)

    return result


def main():
    if len(sys.argv) != 4:
        print("Usage: enhance_resume_quality.py <input-md> <target> <output-md>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    target = sys.argv[2].lower().strip()
    output_path = Path(sys.argv[3])

    text = input_path.read_text(encoding="utf-8")
    enhanced = apply_rules(text, target)

    header = f"<!-- Enhanced by Career System v0.6.3 target={target} -->\n\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(header + enhanced, encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
