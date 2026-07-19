#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


EXAMPLES_DIR = Path(__file__).resolve().parents[2]
SCRIPT = EXAMPLES_DIR / "scripts" / "render_cover_examples.py"


def main() -> int:
    return subprocess.call([sys.executable, str(SCRIPT), "--project", "projeto-romance-com-orelhas"])


if __name__ == "__main__":
    raise SystemExit(main())
