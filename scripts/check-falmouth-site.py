#!/usr/bin/env python3
"""QA checks for Falmouth Shore Excursion site."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "falmouthshoreexcursion.com"

FORBIDDEN = [
    "barbados", "antigua", "cozumel", "aruba", "st maarten", "st. maarten",
    "bonaire", "dominica", "flam", "flåm", "belize", "altun ha", "caye caulker",
    "amber cove", "grand cayman", "san juan", "tortola", "gibraltar", "norway",
    "costa maya", "bimini", "curacao", "st lucia", "st. lucia",
]

SCAN_EXTENSIONS = {".html", ".py", ".json", ".jsonc", ".txt", ".xml", ".md", ".js", ".css", ".sh"}
SKIP_DIRS = {"node_modules", ".git", "scripts/__pycache__"}


def iter_files() -> list[Path]:
    files = []
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in SCAN_EXTENSIONS:
            files.append(p)
    return files


def check_forbidden_references() -> list[str]:
    errors = []
    for path in iter_files():
        if path.name == "check-falmouth-site.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in FORBIDDEN:
            if term in text:
                errors.append(f"Forbidden reference '{term}' in {path.relative_to(ROOT)}")
    return errors


def check_domain_config() -> list[str]:
    errors = []
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8") if (ROOT / "robots.txt").exists() else ""
    if DOMAIN not in robots:
        errors.append("robots.txt missing falmouthshoreexcursion.com sitemap")

    wrangler = (ROOT / "wrangler.jsonc").read_text(encoding="utf-8") if (ROOT / "wrangler.jsonc").exists() else ""
    if DOMAIN not in wrangler:
        errors.append("wrangler.jsonc missing falmouthshoreexcursion.com domain")

    sitemap = ROOT / "sitemap.xml"
    if not sitemap.exists():
        errors.append("sitemap.xml missing")
    else:
        tree = ET.parse(sitemap)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [el.text for el in tree.findall(".//sm:loc", ns)]
        if not locs:
            locs = [el.text for el in tree.findall(".//loc")]
        bad = [u for u in locs if u and DOMAIN not in u]
        if bad:
            errors.append(f"sitemap.xml has non-Falmouth URLs: {bad[:3]}")
        if len(locs) < 20:
            errors.append(f"sitemap.xml has only {len(locs)} URLs (expected 21)")

    index = (ROOT / "index.html").read_text(encoding="utf-8") if (ROOT / "index.html").exists() else ""
    if "Falmouth Shore Excursion" not in index:
        errors.append("index.html missing Falmouth site title")

    return errors


def check_required_content() -> list[str]:
    errors = []
    guides = [
        "best-falmouth-shore-excursions.html",
        "falmouth-port-guide.html",
        "one-day-in-falmouth-from-a-cruise-ship.html",
        "dunns-river-falls-guide.html",
        "martha-brae-river-rafting-guide.html",
        "blue-hole-jamaica-guide.html",
        "is-falmouth-safe-for-cruise-passengers.html",
        "can-you-explore-falmouth-without-an-excursion.html",
        "best-beaches-near-falmouth-jamaica.html",
        "jamaican-rum-and-culture-guide.html",
    ]
    for g in guides:
        if not (ROOT / g).exists():
            errors.append(f"Missing guide page: {g}")
    tours = [
        "dunns-river-falls-tour.html",
        "dunns-river-falls-and-area-highlights.html",
        "jamaican-countryside-sightseeing-with-lunch.html",
        "private-driver-guide-full-day.html",
        "martha-brae-river-rafting.html",
        "blue-hole-adventure.html",
        "beach-escape-excursion.html",
        "river-tubing-adventure.html",
        "jamaica-highlights-tour.html",
        "rum-and-culture-experience.html",
    ]
    for t in tours:
        if not (ROOT / t).exists():
            errors.append(f"Missing tour page: {t}")
    return errors


def main() -> None:
    print("Running Falmouth site QA checks…")
    errors = []
    errors.extend(check_forbidden_references())
    errors.extend(check_domain_config())
    errors.extend(check_required_content())

    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  ✗ {e}")
        raise SystemExit(1)

    print("All checks passed.")
    print(f"  Domain: {DOMAIN}")
    print("  Ready for GitHub and Cloudflare deploy.")


if __name__ == "__main__":
    main()
