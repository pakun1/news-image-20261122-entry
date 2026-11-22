"""Front-page summary of 22 November 2026, rendered as a PNG image.

The newspaper front page (entry.png, sitting next to this file) is copied
byte-for-byte into the output directory. There is no randomness, no clock
and no network use, so every run produces the identical image.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"expected the front-page image at {source}")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
