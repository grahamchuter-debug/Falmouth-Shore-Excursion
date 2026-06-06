#!/usr/bin/env python3
"""Download images from Wikimedia Commons for Falmouth site."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

DOWNLOADS: list[tuple[str, str, str]] = [
    ("hero-falmouth.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: Dunn's River Falls Jamaica"),
    ("falmouth-cruise-port.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Falmouth_Jamaica_Harbour.jpg/1920px-Falmouth_Jamaica_Harbour.jpg",
     "Wikimedia: Falmouth Jamaica harbour"),
    ("falmouth-port-arrival.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Falmouth_Jamaica_Harbour.jpg/1920px-Falmouth_Jamaica_Harbour.jpg",
     "Wikimedia: Falmouth Jamaica waterfront"),
    ("falmouth-intro.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: Jamaica north coast scenery"),
    ("best-falmouth-excursions.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: Falmouth excursions destination"),
    ("one-day-falmouth.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: One day Falmouth itinerary"),
    ("dunns-river-falls.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: Dunn's River Falls Jamaica"),
    ("martha-brae-rafting.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Martha_Brae_River%2C_Jamaica.jpg/1920px-Martha_Brae_River%2C_Jamaica.jpg",
     "Wikimedia: Martha Brae River Jamaica"),
    ("blue-hole-jamaica.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: Jamaica waterfall pools illustrative"),
    ("jamaica-beach.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Doctor%27s_Cave_Beach_Club%2C_Montego_Bay%2C_Jamaica.jpg/1920px-Doctor%27s_Cave_Beach_Club%2C_Montego_Bay%2C_Jamaica.jpg",
     "Wikimedia: Doctor's Cave Beach Montego Bay Jamaica"),
    ("jamaica-countryside.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Martha_Brae_River%2C_Jamaica.jpg/1920px-Martha_Brae_River%2C_Jamaica.jpg",
     "Wikimedia: Jamaican countryside river"),
    ("river-tubing-jamaica.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Martha_Brae_River%2C_Jamaica.jpg/1920px-Martha_Brae_River%2C_Jamaica.jpg",
     "Wikimedia: Jamaica river illustrative"),
    ("jamaican-rum.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Falmouth_Jamaica_Harbour.jpg/1920px-Falmouth_Jamaica_Harbour.jpg",
     "Wikimedia: Falmouth Jamaica heritage"),
    ("private-tour-jamaica.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dunn%27s_River_Falls%2C_Jamaica.jpg/1920px-Dunn%27s_River_Falls%2C_Jamaica.jpg",
     "Wikimedia: Jamaica scenic tour"),
    ("jamaica-highlights.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Falmouth_Jamaica_Harbour.jpg/1920px-Falmouth_Jamaica_Harbour.jpg",
     "Wikimedia: Jamaica highlights"),
    ("falmouth-faq.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Falmouth_Jamaica_Harbour.jpg/1920px-Falmouth_Jamaica_Harbour.jpg",
     "Wikimedia: Falmouth FAQ page"),
    ("falmouth-safety.png",
     "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Falmouth_Jamaica_Harbour.jpg/1920px-Falmouth_Jamaica_Harbour.jpg",
     "Wikimedia: Falmouth safety guide"),
]


def download(filename: str, url: str, note: str) -> bool:
    dest = IMAGES / filename
    print(f"  {filename}")
    print(f"    {note}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
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
    print("Downloading Falmouth images…")
    failed = 0
    for i, (filename, url, note) in enumerate(DOWNLOADS):
        if i:
            time.sleep(1.5)
        if not download(filename, url, note):
            failed += 1
    if failed:
        print(f"Warning: {failed} download(s) failed — placeholders remain for those files.")
    else:
        print("Done.")


if __name__ == "__main__":
    main()
