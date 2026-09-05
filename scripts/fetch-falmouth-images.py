#!/usr/bin/env python3
"""Download/refresh images from Wikimedia Commons / documented sources for Falmouth site."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

# Prefer Special:FilePath for stable redirects. Blue Hole MUST NOT use Dunn's River.
DOWNLOADS: list[tuple[str, str, str]] = [
    ("hero-falmouth.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Dunn%27s%20River%20Falls%2C%20Jamaica.jpg?width=1920",
     "Wikimedia: Dunn's River Falls Jamaica"),
    ("falmouth-cruise-port.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Falmouth%20Jamaica%20Harbour.jpg?width=1920",
     "Wikimedia: Falmouth Jamaica harbour"),
    ("falmouth-port-arrival.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Falmouth%20Jamaica%20Harbour.jpg?width=1920",
     "Wikimedia: Falmouth Jamaica harbour (port arrival)"),
    ("dunns-river-falls.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Dunn%27s%20River%20Falls%2C%20Jamaica.jpg?width=1920",
     "Wikimedia: Dunn's River Falls Jamaica"),
    ("martha-brae-rafting.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Martha%20Brae%20River%2C%20Jamaica.jpg?width=1920",
     "Wikimedia: Martha Brae River Jamaica"),
    ("blue-hole-jamaica.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Island%20Gully%20Falls%20-%20Blue%20Hole%20(31614815034).jpg?width=1920",
     "Wikimedia: Island Gully Falls / Blue Hole (NOT Dunn's River)"),
    ("jamaica-beach.png",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Doctor%27s%20Cave%20Beach%20Club%2C%20Montego%20Bay%2C%20Jamaica.jpg?width=1920",
     "Wikimedia: Doctor's Cave Beach Montego Bay Jamaica"),
]


def download(filename: str, url: str, note: str) -> bool:
    dest = IMAGES / filename
    print(f"  {filename}")
    print(f"    {note}")
    result = subprocess.run(
        ["curl", "-fsSL", "-L", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Falmouth Wikimedia images (core set)…")
    print("Note: Unsplash/Pexels diversifying assets are managed in ATTRIBUTION.md / Phase 9B.")
    failed = 0
    for i, (filename, url, note) in enumerate(DOWNLOADS):
        if i:
            time.sleep(1.5)
        if not download(filename, url, note):
            failed += 1
    if failed:
        print(f"Warning: {failed} download(s) failed — existing files retained where present.")
    else:
        print("Done.")


if __name__ == "__main__":
    main()
