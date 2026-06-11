#!/usr/bin/env python3

import sys
from pathlib import Path


HEADER = """# Resume Experience Section

## Federal Reserve Bank of New York
Senior Business Analyst / DevOps Release Coordinator
Apr 2017 – Feb 2026

### Relevant Experience

"""


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_resume_section.py input.md output.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    text = input_path.read_text(encoding="utf-8")

    bullets = []
    seen = set()

    for line in text.splitlines():
        line = line.strip()

        if line.startswith("- ") and "`" not in line:
            if line not in seen:
                bullets.append(line)
                seen.add(line)

    output = HEADER

    for bullet in bullets:
        output += f"{bullet}\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
