#!/usr/bin/env python3
"""
OO skeleton for future refactor.

For now, use scripts/normalize_jd.py as the working implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys

@dataclass
class JDNormalizationRun:
    input_dir: Path
    output_dir: Path
    run_id: str

    def execute(self) -> int:
        script = Path(__file__).with_name("normalize_jd.py")
        return subprocess.call([
            sys.executable,
            str(script),
            "--input-dir", str(self.input_dir),
            "--output-dir", str(self.output_dir),
            "--run-id", self.run_id,
        ])

def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()
    return JDNormalizationRun(Path(args.input_dir), Path(args.output_dir), args.run_id).execute()

if __name__ == "__main__":
    raise SystemExit(main())
