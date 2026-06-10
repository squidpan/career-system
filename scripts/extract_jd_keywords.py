#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


KEYWORDS = [
    "production support", "application support", "incident management",
    "monitoring", "troubleshooting", "operations support",
    "market data", "pricing", "fixed income", "vendor feeds",
    "reference data", "real-time data",
    "data quality", "data validation", "data reconciliation",
    "root cause analysis", "exception handling", "controls",
    "oracle", "sql", "database", "views",
    "business analyst", "requirements", "stakeholder management",
    "process analysis", "functional analysis", "requirements gathering",
    "modernization", "technical refresh", "legacy modernization",
    "platform migration", "cloud migration", "aws", "migration",
    "service modernization", "rest api", "api testing", "api validation",
    "service integration", "web services", "governance", "audit",
    "approval workflow", "risk management", "compliance",
    "linux", "unix", "shell scripting", "batch processing", "cron"
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def main():
    if len(sys.argv) != 2:
        print("Usage: extract_jd_keywords.py <jd-file>")
        sys.exit(1)

    jd_path = Path(sys.argv[1])
    text = normalize(jd_path.read_text(encoding="utf-8", errors="ignore"))

    matched = sorted({kw for kw in KEYWORDS if kw in text})

    print(json.dumps({
        "jd_path": str(jd_path),
        "keyword_count": len(matched),
        "keywords": matched
    }, indent=2))


if __name__ == "__main__":
    main()
