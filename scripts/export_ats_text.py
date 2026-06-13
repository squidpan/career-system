#!/usr/bin/env python3

import re
import sys
from pathlib import Path


def clean_markdown(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = text.replace("**", "")
    text = text.replace("•", "-")
    text = text.replace("–", "-")
    text = text.replace("—", "-")

    lines = []
    for line in text.splitlines():
        line = line.rstrip()

        if line.startswith("# "):
            lines.append(line[2:].strip().upper())
            lines.append("")
        elif line.startswith("## "):
            lines.append(line[3:].strip().upper())
            lines.append("")
        elif line.startswith("### "):
            lines.append(line[4:].strip())
            lines.append("")
        elif line.startswith("- "):
            lines.append("- " + line[2:].strip())
        else:
            lines.append(line.strip())

    cleaned = "\n".join(lines)

    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"


def main():
    if len(sys.argv) != 3:
        print("Usage: export_ats_text.py <input-md> <output-txt>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    text = input_path.read_text(encoding="utf-8")
    output = clean_markdown(text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
