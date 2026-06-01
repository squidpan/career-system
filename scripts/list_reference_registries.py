#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "data" / "reference"

def load(name: str):
    return json.loads((REF / name).read_text(encoding="utf-8"))

def main() -> int:
    companies = load("company-registry.json")
    role_codes = load("role-code-registry.json")
    resume_families = load("resume-family-registry.json")

    print("Company Registry")
    print("================")
    for code, item in sorted(companies.items()):
        print(f"{code:12} -> {item.get('company_name')}")

    print()
    print("Role Code Registry")
    print("==================")
    for code, item in sorted(role_codes.items()):
        resume = item.get("recommended_resume_master_id", "")
        print(f"{code:18} -> {item.get('description')} [{resume}]")

    print()
    print("Resume Family Registry")
    print("======================")
    for code, item in sorted(resume_families.items()):
        print(f"{code:12} -> {item.get('master_resume_file')}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
