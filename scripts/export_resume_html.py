#!/usr/bin/env python3

import sys
import html
from pathlib import Path


CSS = """
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10.5pt;
  line-height: 1.32;
  color: #222;
  max-width: 760px;
  margin: 28px auto;
}

h1 {
  font-size: 20pt;
  margin: 0 0 4px 0;
}

h2 {
  font-size: 12pt;
  margin: 16px 0 6px 0;
  text-transform: uppercase;
  border-bottom: 1px solid #999;
  padding-bottom: 2px;
}

h3 {
  font-size: 11pt;
  margin: 10px 0 4px 0;
}

p {
  margin: 4px 0;
}

ul {
  margin-top: 4px;
  margin-bottom: 8px;
  padding-left: 18px;
}

li {
  margin-bottom: 3px;
}

.comment {
  display: none;
}

.contact {
  margin-bottom: 8px;
}
"""


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    html_lines = []
    in_ul = False

    for line in lines:
        raw = line.rstrip()

        if raw.startswith("<!--"):
            continue

        if raw.startswith("- "):
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            html_lines.append(f"<li>{html.escape(raw[2:])}</li>")
            continue

        if in_ul:
            html_lines.append("</ul>")
            in_ul = False

        if raw.startswith("# "):
            html_lines.append(f"<h1>{html.escape(raw[2:])}</h1>")
        elif raw.startswith("## "):
            html_lines.append(f"<h2>{html.escape(raw[3:])}</h2>")
        elif raw.startswith("### "):
            html_lines.append(f"<h3>{html.escape(raw[4:])}</h3>")
        elif raw.strip() == "":
            html_lines.append("")
        else:
            text = html.escape(raw)
            text = text.replace("**", "")
            html_lines.append(f"<p>{text}</p>")

    if in_ul:
        html_lines.append("</ul>")

    return "\n".join(html_lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: export_resume_html.py <input-md> <output-html>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    md = input_path.read_text(encoding="utf-8")
    body = md_to_html(md)

    doc = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{html.escape(input_path.stem)}</title>
<style>
{CSS}
</style>
</head>
<body>
{body}
</body>
</html>
"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(doc, encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
