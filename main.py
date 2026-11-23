"""u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610 entry:
write one original roast line to /output/entry.txt.

The roast is a fixed string literal. The program just writes it, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ROAST = "My robot vacuum gets stuck on the same rug every day, beeps for rescue like I hired it to supervise me."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(ROAST, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the roast.
    if dest.read_text(encoding="utf-8") != ROAST:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the roast")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
