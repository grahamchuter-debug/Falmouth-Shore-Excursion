#!/usr/bin/env python3
"""Generate Falmouth Shore Excursion static site files."""
from pathlib import Path

from falmouth_config import (
    ACCENT,
    ALL_IMAGES,
    BEST_ALT,
    BEST_IMG,
    BLUE_HOLE_ALT,
    BLUE_HOLE_IMG,
    CATEGORY_IMAGES,
    DATE,
    DOMAIN,
    DUNNS_ALT,
    DUNNS_IMG,
    FAQ_ALT,
    FAQ_IMG,
    HERO_GRADIENT,
    HOME_HERO,
    HOME_HERO_ALT,
    INTRO_ALT,
    INTRO_IMG,
    MARTHA_ALT,
    MARTHA_IMG,
    ONE_DAY_ALT,
    ONE_DAY_IMG,
    PLACEHOLDER_PNG,
    PORT_ALT,
    PORT_IMG,
    PORT_ARRIVAL_ALT,
    PORT_ARRIVAL_IMG,
    PRIVATE_ALT,
    PRIVATE_IMG,
    ROOT,
    RUM_ALT,
    RUM_IMG,
    SITE,
    BEACH_ALT,
    BEACH_IMG,
)
from falmouth_guides import all_guide_content, home_faq_data
from falmouth_helpers import hero_inner, hero_wave, home_schema, page_shell, tourist_trip_schema
from falmouth_tours import all_tour_content
from falmouth_tours_data import SITEMAP_PAGES, TOURS


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-pr-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Falmouth · Jamaica</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Falmouth Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Dunn's River Falls, Martha Brae rafting, Blue Hole adventures and beach escapes — the shore excursions cruise passengers book most from Falmouth, Jamaica.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-falmouth-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="dunns-river-falls-tour.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Dunn's River Falls</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Dunn's River Falls</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Martha Brae</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Blue Hole</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Passengers</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">JMD &amp; USD</span>
        </div>
      </div>
    </div>
    {hero_wave()}
  </section>"""


def tour_hero(tour: dict) -> str:
    img, alt = CATEGORY_IMAGES.get(tour["category"], (INTRO_IMG, INTRO_ALT))
    title_parts = tour["title"].replace(" and ", " &amp; ").split(" ", 2)
    if len(title_parts) >= 2:
        h1 = f"{title_parts[0]}<br/><span class=\"{ACCENT}\">{title_parts[1]}</span>"
        if len(title_parts) > 2:
            h1 += f"<br/>{title_parts[2]}"
    else:
        h1 = tour["title"]
    return hero_inner(
        f"{tour['duration']} · {tour['activity']}",
        h1,
        f"{tour['seg_desc']} Shore excursion for Falmouth Jamaica cruise passengers with port pickup and return-to-ship timing.",
        img,
        f"{tour['title']} Falmouth Jamaica shore excursion hero image for cruise passengers from Falmouth cruise port",
        breadcrumb=tour["title"],
    )


def nav_html() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-pr-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Falmouth Shore<br/><span class="text-[10px] font-body font-normal text-pr-600 tracking-widest uppercase">Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-falmouth-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="dunns-river-falls-guide.html" data-nav="waterfall" class="text-gray-600 hover:text-ocean-600 transition-colors">Waterfalls</a>
        <a href="best-beaches-near-falmouth-jamaica.html" data-nav="beach" class="text-gray-600 hover:text-ocean-600 transition-colors">Beaches</a>
        <a href="private-driver-guide-full-day.html" data-nav="private" class="text-gray-600 hover:text-ocean-600 transition-colors">Private</a>
        <a href="falmouth-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-falmouth-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
"""


def footer_html() -> str:
    featured = [t for t in TOURS if t.get("featured")][:6]
    tour_links = "".join(
        f'<li><a href="{t["slug"]}.html" class="hover:text-white transition-colors">{t["title"]}</a></li>'
        for t in featured
    )
    return f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Falmouth, Jamaica. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            {tour_links}
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Guides</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-falmouth-shore-excursions.html" class="hover:text-white transition-colors">Falmouth Shore Excursions</a></li>
            <li><a href="falmouth-port-guide.html" class="hover:text-white transition-colors">Cruise Port Guide</a></li>
            <li><a href="one-day-in-falmouth-from-a-cruise-ship.html" class="hover:text-white transition-colors">One Day in Falmouth</a></li>
            <li><a href="dunns-river-falls-guide.html" class="hover:text-white transition-colors">Dunn's River Falls</a></li>
            <li><a href="martha-brae-river-rafting-guide.html" class="hover:text-white transition-colors">Martha Brae Rafting</a></li>
            <li><a href="blue-hole-jamaica-guide.html" class="hover:text-white transition-colors">Blue Hole Guide</a></li>
            <li><a href="best-beaches-near-falmouth-jamaica.html" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="is-falmouth-safe-for-cruise-passengers.html" class="hover:text-white transition-colors">Safety Guide</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
"""


def trust_strip_html() -> str:
    return """<section class="trust-strip" aria-label="Falmouth shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Dunn's River Falls</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Martha Brae Rafting</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Blue Hole Adventures</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Return To Ship On Time</li>
    </ul>
  </div>
</section>
"""


def tour_data_page(tour: dict) -> str:
    cat = tour["category"]
    if cat in ("waterfall", "bluehole", "tubing"):
        return "adventure"
    if cat in ("beach", "martha"):
        return "beach"
    if cat == "private":
        return "private"
    if cat in ("rum", "countryside", "highlights"):
        return "culture"
    return "tours"


GUIDE_META = [
    ("best-falmouth-shore-excursions.html", "Best Falmouth Shore Excursions | Compare Jamaica Cruise Tours",
     "Compare the best Falmouth shore excursions — Dunn's River Falls, Martha Brae rafting, Blue Hole and beach escapes with cruise timing from Falmouth Jamaica.",
     "Falmouth shore excursions, Falmouth Jamaica cruise port tours, compare Falmouth excursions, Jamaica cruise trips",
     "excursions", "partials/hero-excursions.html", BEST_IMG, "Best Falmouth Shore Excursions"),
    ("falmouth-port-guide.html", "Falmouth Cruise Port Guide | Jamaica for Cruise Passengers",
     "Falmouth Jamaica cruise port guide — pier logistics, distances to Dunn's River Falls and Martha Brae, taxis, currency and shore excursion planning.",
     "Falmouth cruise port guide, Falmouth Jamaica port day, cruise passenger guide Falmouth, Historic Falmouth Pier",
     "port", "partials/hero-port-guide.html", PORT_IMG, "Falmouth Cruise Port Guide"),
    ("one-day-in-falmouth-from-a-cruise-ship.html", "One Day in Falmouth from a Cruise Ship | Port Itinerary",
     "How to spend one day in Falmouth Jamaica on a cruise stop — waterfalls, river rafting or beach day with return-to-ship buffer.",
     "one day in Falmouth cruise, Falmouth Jamaica port day itinerary, cruise stop Falmouth planning",
     "port", "partials/hero-one-day.html", ONE_DAY_IMG, "One Day in Falmouth from a Cruise Ship"),
    ("dunns-river-falls-guide.html", "Dunn's River Falls Guide | Falmouth Jamaica Cruise Excursions",
     "Dunn's River Falls guide for Falmouth cruise passengers — distance from port, what to expect, best tours and return-to-ship timing.",
     "Dunns River Falls Falmouth, Dunn's River Falls cruise excursion, Ocho Rios waterfall Jamaica",
     "waterfall", "partials/hero-dunns-guide.html", DUNNS_IMG, "Dunn's River Falls Guide"),
    ("martha-brae-river-rafting-guide.html", "Martha Brae River Rafting Guide | Falmouth Jamaica",
     "Martha Brae River rafting guide for Falmouth cruise passengers — distance, bamboo rafting experience and best tours.",
     "Martha Brae rafting Falmouth, bamboo rafting Jamaica cruise, Martha Brae River excursion",
     "beach", "partials/hero-martha-guide.html", MARTHA_IMG, "Martha Brae River Rafting Guide"),
    ("blue-hole-jamaica-guide.html", "Blue Hole Jamaica Guide | Falmouth Cruise Excursions",
     "Blue Hole Jamaica guide for Falmouth cruise passengers — rainforest pools, adventure tours and distance from Falmouth port.",
     "Blue Hole Jamaica cruise, Blue Hole Falmouth excursion, Island Gully Falls Ocho Rios",
     "adventure", "partials/hero-bluehole-guide.html", BLUE_HOLE_IMG, "Blue Hole Jamaica Guide"),
    ("is-falmouth-safe-for-cruise-passengers.html", "Is Falmouth Safe for Cruise Passengers? | Jamaica Port Guide",
     "Safety advice for Falmouth Jamaica cruise passengers — organised excursions, port area security and practical port-day tips.",
     "is Falmouth safe cruise, Falmouth Jamaica safety, cruise passenger safety Jamaica",
     "port", "partials/hero-safety.html", PORT_IMG, "Is Falmouth Safe for Cruise Passengers"),
    ("can-you-explore-falmouth-without-an-excursion.html", "Can You Explore Falmouth Without an Excursion?",
     "Walking Falmouth Jamaica without a shore excursion — what to do at the pier, historic town and when organised tours make sense.",
     "explore Falmouth without excursion, walk Falmouth cruise port, Falmouth town self guided",
     "port", "partials/hero-port-guide.html", PORT_ARRIVAL_IMG, "Explore Falmouth Without an Excursion"),
    ("best-beaches-near-falmouth-jamaica.html", "Best Beaches Near Falmouth Jamaica | Cruise Passenger Guide",
     "Best beaches near Falmouth Jamaica for cruise passengers — Montego Bay, beach clubs and organised beach escape excursions.",
     "beaches near Falmouth Jamaica, Falmouth beach excursion, Montego Bay beach cruise",
     "beach", "partials/hero-beach-guide.html", BEACH_IMG, "Best Beaches Near Falmouth Jamaica"),
    ("jamaican-rum-and-culture-guide.html", "Jamaican Rum and Culture Guide | Falmouth Excursions",
     "Jamaican rum and culture guide for Falmouth cruise passengers — Hampden Estate, Rose Hall and cultural shore excursions.",
     "Jamaican rum tour Falmouth, Hampden Estate cruise excursion, Jamaica culture tour",
     "culture", "partials/hero-rum-guide.html", RUM_IMG, "Jamaican Rum and Culture Guide"),
]


def build_page_meta() -> list[dict]:
    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Dunn's River Falls, Rafting &amp; Beach Tours from Falmouth Jamaica",
            description="Plan Falmouth Jamaica shore excursions for cruise passengers — Dunn's River Falls, Martha Brae rafting, Blue Hole adventures and beach escapes from Falmouth cruise port.",
            keywords="Falmouth shore excursions, Falmouth Jamaica cruise excursions, Dunns River Falls Falmouth, Martha Brae rafting cruise, Blue Hole Jamaica tour",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema=home_schema(home_faq_data()),
        ),
    ]
    for path, title, desc, kw, data_page, hero, preload, schema_name in GUIDE_META:
        pages.append(dict(
            file=path,
            title=title,
            description=desc,
            keywords=kw,
            path=path,
            data_page=data_page,
            hero=hero,
            content=path,
            preload=preload,
            schema={"@context": "https://schema.org", "@type": "Article", "headline": schema_name, "url": f"{DOMAIN}/{path}"},
        ))
    for tour in TOURS:
        img, _ = CATEGORY_IMAGES.get(tour["category"], (INTRO_IMG, INTRO_ALT))
        pages.append(dict(
            file=f"{tour['slug']}.html",
            title=f"{tour['title']} | Falmouth Jamaica Cruise Shore Excursion",
            description=f"{tour['title']} shore excursion for Falmouth Jamaica cruise passengers — {tour['seg_desc']} {tour['duration']} from Falmouth cruise port with return-to-ship timing.",
            keywords=f"{tour['title']} Falmouth, Falmouth shore excursion cruise, {tour['category']} Jamaica tour",
            path=f"{tour['slug']}.html",
            data_page=tour_data_page(tour),
            hero=f"partials/hero-{tour['slug']}.html",
            content=f"{tour['slug']}.html",
            preload=img,
            schema=tourist_trip_schema(tour["title"], f"{tour['seg_desc']} Shore excursion from Falmouth Jamaica cruise port for cruise passengers."),
        ))
    return pages


def build_hero_defs() -> dict[str, str]:
    heroes = {
        "hero-home.html": hero_home(),
        "hero-excursions.html": hero_inner(
            "Falmouth · Jamaica",
            f"Falmouth<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Dunn's River Falls, Martha Brae rafting, Blue Hole adventures and beach escapes for your Falmouth cruise ship schedule.",
            BEST_IMG, BEST_ALT, breadcrumb="Shore Excursions",
        ),
        "hero-port-guide.html": hero_inner(
            "Cruise Passenger Guide",
            f"Falmouth<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Pier logistics, Historic Falmouth town, distances to waterfalls and beaches, taxis and return-to-ship timing.",
            PORT_IMG, PORT_ALT, breadcrumb="Port Guide",
            cta=("best-falmouth-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 Dock Port", "💧 Dunn's River Falls", "🛶 Martha Brae", "💵 JMD & USD"],
        ),
        "hero-one-day.html": hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">Falmouth</span>",
            "Hour-by-hour plan from gangway to departure — waterfalls, river rafting or beach day with return-to-ship buffer.",
            ONE_DAY_IMG, ONE_DAY_ALT, breadcrumb="One Day in Falmouth",
        ),
        "hero-dunns-guide.html": hero_inner(
            "Waterfall Guide",
            f"Dunn's River<br/><span class=\"{ACCENT}\">Falls Guide</span>",
            "Distance from Falmouth, what to expect climbing Jamaica's iconic waterfall and best cruise excursions.",
            DUNNS_IMG, DUNNS_ALT, breadcrumb="Dunn's River Falls Guide",
        ),
        "hero-martha-guide.html": hero_inner(
            "River Rafting",
            f"Martha Brae<br/><span class=\"{ACCENT}\">Rafting Guide</span>",
            "Bamboo rafting on the Martha Brae River — distance, experience and best tours from Falmouth cruise port.",
            MARTHA_IMG, MARTHA_ALT, breadcrumb="Martha Brae Guide",
        ),
        "hero-bluehole-guide.html": hero_inner(
            "Rainforest Adventure",
            f"Blue Hole<br/><span class=\"{ACCENT}\">Jamaica Guide</span>",
            "Unspoiled rainforest pools and waterfalls — adventure guide for Falmouth cruise passengers.",
            BLUE_HOLE_IMG, BLUE_HOLE_ALT, breadcrumb="Blue Hole Guide",
        ),
        "hero-safety.html": hero_inner(
            "Cruise Passenger Safety",
            f"Is Falmouth<br/><span class=\"{ACCENT}\">Safe?</span>",
            "Practical safety advice for cruise passengers exploring Falmouth Jamaica on a port day.",
            PORT_IMG, PORT_ALT, breadcrumb="Safety Guide",
        ),
        "hero-beach-guide.html": hero_inner(
            "North Coast Beaches",
            f"Best Beaches<br/><span class=\"{ACCENT}\">Near Falmouth</span>",
            "Montego Bay beaches, beach clubs and organised beach escape excursions from Falmouth Jamaica.",
            BEACH_IMG, BEACH_ALT, breadcrumb="Beach Guide",
        ),
        "hero-rum-guide.html": hero_inner(
            "Jamaican Heritage",
            f"Rum &amp;<br/><span class=\"{ACCENT}\">Culture Guide</span>",
            "Hampden Estate distillery, Rose Hall heritage and cultural shore excursions from Falmouth.",
            RUM_IMG, RUM_ALT, breadcrumb="Rum &amp; Culture",
        ),
    }
    for tour in TOURS:
        heroes[f"hero-{tour['slug']}.html"] = tour_hero(tour)
    return heroes


def main() -> None:
    print("Building Falmouth Shore Excursion site…")

    write("partials/nav.html", nav_html())
    write("partials/footer.html", footer_html())
    write("partials/trust-strip.html", trust_strip_html())

    for name, html in build_hero_defs().items():
        write(f"partials/{name}", html)

    for name, html in all_guide_content().items():
        write(f"content/{name}", html)

    for name, html in all_tour_content().items():
        write(f"content/{name}", html)

    for p in build_page_meta():
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in SITEMAP_PAGES:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write("package.json", """{
  "name": "falmouth-shore-excursion",
  "private": true,
  "scripts": {
    "build": "python3 scripts/build-falmouth-site.py",
    "images": "python3 scripts/fetch-falmouth-images.py",
    "check": "python3 scripts/check-falmouth-site.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8910"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""")

    write("wrangler.jsonc", """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "falmouth-shore-excursion",
  "compatibility_date": "2026-06-06",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "falmouthshoreexcursion.com",
      "custom_domain": true
    }
  ]
}
""")

    write("deploy.sh", f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""")

    (ROOT / "deploy.sh").chmod(0o755)

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    for img in ALL_IMAGES:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        p.write_bytes(PLACEHOLDER_PNG)

    write("images/ATTRIBUTION.md", """# Image attribution

Hero and content images are sourced from [Wikimedia Commons](https://commons.wikimedia.org) under Creative Commons licences where applicable.

Run `npm run images` to download location-accurate photos. Replace any image with your own assets — keep filenames consistent with `scripts/falmouth_config.py`.
""")

    write("README.md", """# Falmouth Shore Excursion

Cruise-passenger planning guide for Falmouth, Jamaica shore excursions.

## Development

```bash
npm install
npm run build
npm run images
npm run check
npm run preview
```

Open http://localhost:8910 (requires local server for partial loading).

## Deploy to Cloudflare

```bash
npm run build && npm run images && npm run check && ./deploy.sh
```

Domain: https://falmouthshoreexcursion.com
""")

    print("Done.")


if __name__ == "__main__":
    main()
