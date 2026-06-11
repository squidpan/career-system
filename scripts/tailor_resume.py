#!/usr/bin/env python3

import sys
from pathlib import Path


TAILORING_RULES = {
    "finbourne": {
        "Supported enterprise market-data pricing platform": "Supported fixed-income market-data platform",
        "Provided production support": "Provided application and production support",
        "Supported modernization work": "Supported application modernization work",
        "Assisted cloud migration validation": "Assisted cloud and API migration validation"
    },
    "pico": {
        "Supported enterprise market-data pricing platform": "Supported market-data platform experience relevant to low-latency trading environments",
        "Provided production support": "Provided Linux-based production support",
        "Investigated production issues": "Investigated production and operational issues",
        "monitoring, incident investigation": "monitoring, troubleshooting, incident investigation"
    },
    "citi": {
        "Supported technical refresh initiative": "Supported enterprise modernization initiative",
        "Participated in modernization activities": "Partnered with stakeholders on modernization activities",
        "Supported modernization work": "Supported business and technology modernization work",
        "Analyzed consumer data requirements": "Analyzed stakeholder data requirements"
    }
}


def tailor_text(text: str, target: str) -> str:
    rules = TAILORING_RULES.get(target, {})

    tailored = text
    for old, new in rules.items():
        tailored = tailored.replace(old, new)

    return tailored


def main():
    if len(sys.argv) != 4:
        print("Usage: tailor_resume.py <input-md> <target> <output-md>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    target = sys.argv[2].lower().strip()
    output_path = Path(sys.argv[3])

    text = input_path.read_text(encoding="utf-8")
    tailored = tailor_text(text, target)

    header = f"<!-- Tailored by Career System v0.6.0 target={target} -->\n\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(header + tailored, encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
