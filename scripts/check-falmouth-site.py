#!/usr/bin/env python3
"""QA checks for Falmouth Shore Excursion World 2.0 site."""
from pathlib import Path
import hashlib
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "falmouthshoreexcursion.com"

FORBIDDEN = [
    "barbados", "antigua", "cozumel", "aruba", "st maarten", "st. maarten",
    "bonaire", "dominica", "flam", "flåm", "belize", "altun ha", "caye caulker",
    "amber cove", "grand cayman", "san juan", "tortola", "gibraltar", "norway",
    "costa maya", "bimini", "curacao", "st lucia", "st. lucia", "grand turk",
    "stripe", "viator", "getyourguide",
]

SCAN_EXTENSIONS = {".html", ".py", ".json", ".jsonc", ".txt", ".xml", ".md", ".js", ".css", ".sh"}
SKIP_DIRS = {"node_modules", ".git", "scripts/__pycache__"}

MUST_PRESERVE = [
    "index.html",
    "best-beaches-near-falmouth-jamaica.html",
    "martha-brae-river-rafting-guide.html",
    "martha-brae-river-rafting.html",
    "falmouth-port-guide.html",
    "best-falmouth-shore-excursions.html",
]

TRUST_PAGES = [
    "about.html", "contact.html", "privacy.html", "terms.html",
    "methodology.html", "falmouth-shore-excursions-faq.html", "404.html",
]


def iter_files() -> list[Path]:
    files = []
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS or part == "__pycache__" for part in p.parts):
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
    if '"main": "worker.js"' not in wrangler and "'main': 'worker.js'" not in wrangler:
        errors.append("wrangler.jsonc missing worker.js main")

    if not (ROOT / "worker.js").exists():
        errors.append("worker.js missing")

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
        htmlish = [u for u in locs if u and u.rstrip("/").endswith(".html")]
        if htmlish:
            errors.append(f"sitemap.xml still has .html locs: {htmlish[:3]}")
        if len(locs) < 25:
            errors.append(f"sitemap.xml has only {len(locs)} URLs (expected 25+)")

    index = (ROOT / "index.html").read_text(encoding="utf-8") if (ROOT / "index.html").exists() else ""
    if "Falmouth Shore Excursion" not in index:
        errors.append("index.html missing Falmouth site title")
    if 'id="page-content"' in index and "Martha Brae" not in index:
        errors.append("index.html appears to lack inlined Martha Brae content")
    if 'rel="canonical" href="https://falmouthshoreexcursion.com/"' not in index:
        errors.append("index.html canonical not extensionless apex")

    return errors


def check_required_content() -> list[str]:
    errors = []
    for g in MUST_PRESERVE + TRUST_PAGES:
        if not (ROOT / g).exists():
            errors.append(f"Missing required page: {g}")
    tours = [
        "dunns-river-falls-tour.html",
        "dunns-river-falls-and-area-highlights.html",
        "jamaican-countryside-sightseeing-with-lunch.html",
        "private-driver-guide-full-day.html",
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


def check_trust_language() -> list[str]:
    errors = []
    patterns = [
        r"return-to-ship guarantee",
        r"return to ship guarantee",
        r"easy booking with cruise-timed",
        r'"@type":\s*"LocalBusiness"',
        r'"@type": "AggregateRating"',
        r'"@type": "Offer"',
    ]
    for path in ROOT.glob("*.html"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        for pat in patterns:
            if re.search(pat, text if pat.startswith(r'"') else lower, re.I):
                errors.append(f"Trust/schema issue '{pat}' in {path.name}")
    return errors


def check_images() -> list[str]:
    errors = []
    images = ROOT / "images"
    blue = images / "blue-hole-jamaica.png"
    dunns = images / "dunns-river-falls.png"
    if not blue.exists() or not dunns.exists():
        errors.append("Missing blue-hole or dunns image")
        return errors
    if hashlib.md5(blue.read_bytes()).hexdigest() == hashlib.md5(dunns.read_bytes()).hexdigest():
        errors.append("Blue Hole image binary matches Dunn's River — mismatch not fixed")
    if not (images / "ATTRIBUTION.md").exists():
        errors.append("images/ATTRIBUTION.md missing")
    return errors


def check_no_js_content() -> list[str]:
    errors = []
    samples = [
        ("index.html", "Martha Brae"),
        ("best-beaches-near-falmouth-jamaica.html", "Doctor"),
        ("martha-brae-river-rafting-guide.html", "bamboo"),
        ("falmouth-port-guide.html", "Historic Falmouth"),
        ("about.html", "independent"),
    ]
    for name, needle in samples:
        text = (ROOT / name).read_text(encoding="utf-8", errors="ignore")
        if needle.lower() not in text.lower():
            errors.append(f"{name} missing inlined content marker '{needle}'")
        if 'data-content=' in text and 'data-inlined="true"' not in text:
            errors.append(f"{name} still uses client-only content loading")
    return errors


def main() -> None:
    print("Running Falmouth World 2.0 QA checks…")
    errors = []
    errors.extend(check_forbidden_references())
    errors.extend(check_domain_config())
    errors.extend(check_required_content())
    errors.extend(check_trust_language())
    errors.extend(check_images())
    errors.extend(check_no_js_content())

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
