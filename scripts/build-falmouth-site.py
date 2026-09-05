#!/usr/bin/env python3
"""Generate Falmouth Shore Excursion World 2.0 static site files."""
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
from falmouth_guides import all_guide_content, faq_page_data, home_faq_data
from falmouth_helpers import (
    breadcrumb_schema,
    faq_schema,
    hero_inner,
    hero_wave,
    home_schema,
    href,
    static_page_shell,
    tourist_trip_schema,
)
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
          <span class="w-2 h-2 rounded-full bg-pr-400"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Falmouth · Jamaica</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Falmouth Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Plan Martha Brae rafting, north-coast beaches, Dunn's River Falls and Blue Hole days around the shore time your ship actually gives you in Falmouth, Jamaica.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="{href('best-falmouth-shore-excursions')}" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="{href('best-beaches-near-falmouth-jamaica')}" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Best Beaches</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Martha Brae</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Best Beaches</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Dunn's River</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Passengers</span>
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
        f"{tour['seg_desc']} Editorial planning page for Falmouth Jamaica cruise passengers — no booking on this site.",
        img,
        f"{tour['title']} Falmouth Jamaica shore excursion hero image for cruise passengers from Falmouth cruise port",
        breadcrumb=tour["title"],
    )


def nav_html() -> str:
    return f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-pr-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="/" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Falmouth Shore<br/><span class="text-[10px] font-body font-normal text-pr-600 tracking-widest uppercase">Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="{href('best-falmouth-shore-excursions')}" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Shore Excursions</a>
        <a href="{href('best-beaches-near-falmouth-jamaica')}" data-nav="beach" class="text-gray-600 hover:text-ocean-600 transition-colors">Best Beaches</a>
        <a href="{href('martha-brae-river-rafting-guide')}" data-nav="martha" class="text-gray-600 hover:text-ocean-600 transition-colors">Martha Brae</a>
        <a href="{href('falmouth-port-guide')}" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
        <a href="{href('one-day-in-falmouth-from-a-cruise-ship')}" data-nav="oneday" class="text-gray-600 hover:text-ocean-600 transition-colors">One Day</a>
      </div>
      <a href="{href('best-falmouth-shore-excursions')}" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu" aria-expanded="false">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
"""


def footer_html() -> str:
    featured = [t for t in TOURS if t.get("featured")][:6]
    tour_links = "".join(
        f'<li><a href="{href(t["slug"])}" class="hover:text-white transition-colors">{t["title"]}</a></li>'
        for t in featured
    )
    return f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="/" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise visitors to Falmouth, Jamaica. Not affiliated with any cruise line. We do not take bookings on this site in this phase.</p>
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
            <li><a href="{href('best-falmouth-shore-excursions')}" class="hover:text-white transition-colors">Shore Excursions</a></li>
            <li><a href="{href('best-beaches-near-falmouth-jamaica')}" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="{href('martha-brae-river-rafting-guide')}" class="hover:text-white transition-colors">Martha Brae</a></li>
            <li><a href="{href('falmouth-port-guide')}" class="hover:text-white transition-colors">Cruise Port Guide</a></li>
            <li><a href="{href('one-day-in-falmouth-from-a-cruise-ship')}" class="hover:text-white transition-colors">One Day in Falmouth</a></li>
            <li><a href="{href('dunns-river-falls-guide')}" class="hover:text-white transition-colors">Dunn's River Falls</a></li>
            <li><a href="{href('blue-hole-jamaica-guide')}" class="hover:text-white transition-colors">Blue Hole Guide</a></li>
            <li><a href="{href('falmouth-shore-excursions-faq')}" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Trust</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="{href('about')}" class="hover:text-white transition-colors">About</a></li>
            <li><a href="{href('contact')}" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="{href('methodology')}" class="hover:text-white transition-colors">Methodology</a></li>
            <li><a href="{href('privacy')}" class="hover:text-white transition-colors">Privacy</a></li>
            <li><a href="{href('terms')}" class="hover:text-white transition-colors">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking. Editorial planning only.</p>
      </div>
    </div>
  </footer>
"""


def trust_strip_html() -> str:
    return """<section class="trust-strip" aria-label="Falmouth shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Martha Brae Guides</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Beach Planning</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Honest Cruise Timing</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Independent Planning</li>
    </ul>
  </div>
</section>
"""


def tour_data_page(tour: dict) -> str:
    cat = tour["category"]
    if cat == "martha":
        return "martha"
    if cat in ("waterfall", "bluehole", "tubing"):
        return "adventure"
    if cat in ("beach",):
        return "beach"
    if cat == "private":
        return "private"
    if cat in ("rum", "countryside", "highlights"):
        return "culture"
    return "tours"


GUIDE_META = [
    ("best-falmouth-shore-excursions.html", "Best Falmouth Shore Excursions | Compare Jamaica Cruise Tours",
     "Compare Falmouth shore excursions — Martha Brae rafting, beaches, Dunn's River Falls and Blue Hole with honest cruise timing from Falmouth Jamaica.",
     "Falmouth shore excursions, Falmouth Jamaica cruise port tours, compare Falmouth excursions, Jamaica cruise trips",
     "excursions", "partials/hero-excursions.html", BEST_IMG, "Best Falmouth Shore Excursions"),
    ("falmouth-port-guide.html", "Falmouth Cruise Port Guide | Jamaica for Cruise Passengers",
     "Falmouth Jamaica cruise port guide — pier logistics, Martha Brae, beaches, Dunn's River practicality, taxis and shore excursion planning.",
     "Falmouth cruise port guide, Falmouth Jamaica port day, cruise passenger guide Falmouth, Historic Falmouth Pier",
     "port", "partials/hero-port-guide.html", PORT_IMG, "Falmouth Cruise Port Guide"),
    ("one-day-in-falmouth-from-a-cruise-ship.html", "One Day in Falmouth from a Cruise Ship | Port Itinerary",
     "How to spend one day in Falmouth Jamaica on a cruise stop — Martha Brae, beach day or longer attraction scenarios matched to your ship.",
     "one day in Falmouth cruise, Falmouth Jamaica port day itinerary, cruise stop Falmouth planning",
     "oneday", "partials/hero-one-day.html", ONE_DAY_IMG, "One Day in Falmouth from a Cruise Ship"),
    ("dunns-river-falls-guide.html", "Dunn's River Falls Guide | Falmouth Jamaica Cruise Excursions",
     "Dunn's River Falls guide for Falmouth cruise passengers — honest distance from port, what to expect and cruise-day practicality.",
     "Dunns River Falls Falmouth, Dunn's River Falls cruise excursion, Ocho Rios waterfall Jamaica",
     "adventure", "partials/hero-dunns-guide.html", DUNNS_IMG, "Dunn's River Falls Guide"),
    ("martha-brae-river-rafting-guide.html", "Martha Brae River Rafting Guide | Falmouth Jamaica",
     "Martha Brae River rafting guide for Falmouth cruise passengers — experience, port practicality, beach alternative and return planning.",
     "Martha Brae rafting Falmouth, bamboo rafting Jamaica cruise, Martha Brae River excursion",
     "martha", "partials/hero-martha-guide.html", MARTHA_IMG, "Martha Brae River Rafting Guide"),
    ("blue-hole-jamaica-guide.html", "Blue Hole Jamaica Guide | Falmouth Cruise Excursions",
     "Blue Hole Jamaica guide for Falmouth cruise passengers — rainforest pools and honest distance from Falmouth port.",
     "Blue Hole Jamaica cruise, Blue Hole Falmouth excursion, Island Gully Falls Ocho Rios",
     "adventure", "partials/hero-bluehole-guide.html", BLUE_HOLE_IMG, "Blue Hole Jamaica Guide"),
    ("is-falmouth-safe-for-cruise-passengers.html", "Is Falmouth Safe for Cruise Passengers? | Jamaica Port Guide",
     "Safety advice for Falmouth Jamaica cruise passengers — organised excursions, port area tips and practical port-day guidance.",
     "is Falmouth safe cruise, Falmouth Jamaica safety, cruise passenger safety Jamaica",
     "port", "partials/hero-safety.html", PORT_IMG, "Is Falmouth Safe for Cruise Passengers"),
    ("can-you-explore-falmouth-without-an-excursion.html", "Can You Explore Falmouth Without an Excursion?",
     "Walking Falmouth Jamaica without a shore excursion — what to do at the pier, historic town and when organised tours make sense.",
     "explore Falmouth without excursion, walk Falmouth cruise port, Falmouth town self guided",
     "port", "partials/hero-port-guide.html", PORT_ARRIVAL_IMG, "Explore Falmouth Without an Excursion"),
    ("best-beaches-near-falmouth-jamaica.html", "Best Beaches Near Falmouth Jamaica | Cruise Passenger Guide",
     "Best beaches near Falmouth Jamaica for cruise passengers — Beach Escape, Doctor's Cave, Bamboo Beach Club and Montego Bay context.",
     "beaches near Falmouth Jamaica, Falmouth beach excursion, Montego Bay beach cruise, Doctor's Cave Beach",
     "beach", "partials/hero-beach-guide.html", BEACH_IMG, "Best Beaches Near Falmouth Jamaica"),
    ("jamaican-rum-and-culture-guide.html", "Jamaican Rum and Culture Guide | Falmouth Excursions",
     "Jamaican rum and culture guide for Falmouth cruise passengers — Hampden Estate, Rose Hall and cultural shore excursions.",
     "Jamaican rum tour Falmouth, Hampden Estate cruise excursion, Jamaica culture tour",
     "culture", "partials/hero-rum-guide.html", RUM_IMG, "Jamaican Rum and Culture Guide"),
    ("falmouth-shore-excursions-faq.html", "Falmouth Shore Excursions FAQ | Cruise Passenger Answers",
     "Falmouth Jamaica cruise FAQ — dock port facts, Martha Brae vs beaches, Dunn's River distance and planning answers.",
     "Falmouth shore excursions FAQ, Falmouth cruise FAQ, Falmouth Jamaica port questions",
     "faq", "partials/hero-faq.html", FAQ_IMG, "Falmouth Shore Excursions FAQ"),
]


TRUST_META = [
    ("about.html", "About Falmouth Shore Excursion",
     "Independent planning guide for Falmouth Jamaica cruise shore excursions — editorial only, no bookings in this phase.",
     "about Falmouth Shore Excursion, Falmouth cruise planning guide",
     "about", "About"),
    ("contact.html", "Contact Falmouth Shore Excursion",
     "Contact Falmouth Shore Excursion — independent cruise planning guide. Email routing pending manual verification.",
     "contact Falmouth Shore Excursion, Falmouth cruise guide contact",
     "contact", "Contact"),
    ("privacy.html", "Privacy Policy | Falmouth Shore Excursion",
     "Privacy policy for Falmouth Shore Excursion editorial planning website.",
     "Falmouth Shore Excursion privacy",
     "privacy", "Privacy"),
    ("terms.html", "Terms of Use | Falmouth Shore Excursion",
     "Terms of use for Falmouth Shore Excursion cruise planning guidance.",
     "Falmouth Shore Excursion terms",
     "terms", "Terms"),
    ("methodology.html", "Methodology | Falmouth Shore Excursion",
     "How Falmouth Shore Excursion researches and presents cruise planning guidance without invented prices or ratings.",
     "Falmouth Shore Excursion methodology",
     "methodology", "Methodology"),
]


def build_page_meta() -> list[dict]:
    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Martha Brae, Beaches &amp; Cruise Tours from Falmouth Jamaica",
            description="Plan Falmouth Jamaica shore excursions for cruise passengers — Martha Brae rafting, best beaches, Dunn's River Falls and Blue Hole days from Falmouth cruise port.",
            keywords="Falmouth shore excursions, Falmouth Jamaica cruise excursions, Martha Brae rafting cruise, beaches near Falmouth, Dunns River Falls Falmouth",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema=home_schema(home_faq_data()),
            trust=True,
        ),
    ]
    for path, title, desc, kw, data_page, hero, preload, schema_name in GUIDE_META:
        slug = path.removesuffix(".html")
        schema_extra: list = [
            breadcrumb_schema([("Home", ""), (schema_name, slug)]),
        ]
        if slug == "falmouth-shore-excursions-faq":
            schema_extra.append(faq_schema(faq_page_data()))
        pages.append(dict(
            file=path,
            title=title,
            description=desc,
            keywords=kw,
            path=slug,
            data_page=data_page,
            hero=hero,
            content=path,
            preload=preload,
            schema=schema_extra,
            trust=True,
        ))
    for tour in TOURS:
        img, _ = CATEGORY_IMAGES.get(tour["category"], (INTRO_IMG, INTRO_ALT))
        pages.append(dict(
            file=f"{tour['slug']}.html",
            title=f"{tour['title']} | Falmouth Jamaica Cruise Shore Excursion",
            description=f"{tour['title']} shore excursion planning for Falmouth Jamaica cruise passengers — {tour['seg_desc']} Editorial only; no booking on this site.",
            keywords=f"{tour['title']} Falmouth, Falmouth shore excursion cruise, {tour['category']} Jamaica tour",
            path=tour["slug"],
            data_page=tour_data_page(tour),
            hero=f"partials/hero-{tour['slug']}.html",
            content=f"{tour['slug']}.html",
            preload=img,
            schema=[
                tourist_trip_schema(tour["title"], f"{tour['seg_desc']} Shore excursion planning from Falmouth Jamaica cruise port."),
                breadcrumb_schema([("Home", ""), (tour["title"], tour["slug"])]),
            ],
            trust=True,
        ))
    for path, title, desc, kw, data_page, label in TRUST_META:
        slug = path.removesuffix(".html")
        pages.append(dict(
            file=path,
            title=title,
            description=desc,
            keywords=kw,
            path=slug,
            data_page=data_page,
            hero="",
            content=path,
            preload=PORT_IMG,
            schema=[breadcrumb_schema([("Home", ""), (label, slug)])],
            trust=False,
            main_pad=True,
        ))
    pages.append(dict(
        file="404.html",
        title=f"Page Not Found | {SITE}",
        description="That URL is not part of the Falmouth Shore Excursion planning site.",
        keywords="Falmouth 404",
        path="404",
        data_page="404",
        hero="",
        content="404.html",
        preload=PORT_IMG,
        schema=None,
        trust=False,
        main_pad=True,
    ))
    return pages


def build_hero_defs() -> dict[str, str]:
    heroes = {
        "hero-home.html": hero_home(),
        "hero-excursions.html": hero_inner(
            "Falmouth · Jamaica",
            f"Falmouth<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Martha Brae rafting, beaches, Dunn's River Falls and Blue Hole options for your Falmouth cruise ship schedule.",
            BEST_IMG, BEST_ALT, breadcrumb="Shore Excursions",
        ),
        "hero-port-guide.html": hero_inner(
            "Cruise Passenger Guide",
            f"Falmouth<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Pier logistics, Historic Falmouth town, distances to Martha Brae, beaches and waterfalls, and return planning.",
            PORT_IMG, PORT_ALT, breadcrumb="Port Guide",
            cta=("best-falmouth-shore-excursions", "View Shore Excursions →"),
            tags=["Dock Port", "Martha Brae", "Beaches", "JMD &amp; USD"],
        ),
        "hero-one-day.html": hero_inner(
            "Port Day Scenarios",
            f"One Day in<br/><span class=\"{ACCENT}\">Falmouth</span>",
            "Realistic cruise-day scenarios — Martha Brae, beach day or longer attractions — adjusted to your ship's call.",
            ONE_DAY_IMG, ONE_DAY_ALT, breadcrumb="One Day in Falmouth",
        ),
        "hero-dunns-guide.html": hero_inner(
            "Waterfall Guide",
            f"Dunn's River<br/><span class=\"{ACCENT}\">Falls Guide</span>",
            "Honest distance from Falmouth, what to expect climbing Jamaica's iconic waterfall and cruise-day practicality.",
            DUNNS_IMG, DUNNS_ALT, breadcrumb="Dunn's River Falls Guide",
        ),
        "hero-martha-guide.html": hero_inner(
            "River Rafting",
            f"Martha Brae<br/><span class=\"{ACCENT}\">Rafting Guide</span>",
            "Bamboo rafting on the Martha Brae River — experience, port practicality and how it compares with beach or waterfall days.",
            MARTHA_IMG, MARTHA_ALT, breadcrumb="Martha Brae Guide",
            cta=("martha-brae-river-rafting", "Explore the rafting option →"),
        ),
        "hero-bluehole-guide.html": hero_inner(
            "Rainforest Adventure",
            f"Blue Hole<br/><span class=\"{ACCENT}\">Jamaica Guide</span>",
            "Rainforest pools and waterfalls east of Falmouth — a longer attraction day, not a pier walk.",
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
            "Beach Escape, Doctor's Cave, Bamboo Beach Club and Montego Bay beach context for Falmouth cruise passengers.",
            BEACH_IMG, BEACH_ALT, breadcrumb="Beach Guide",
            cta=("beach-escape-excursion", "Explore Beach Escape →"),
        ),
        "hero-rum-guide.html": hero_inner(
            "Jamaican Heritage",
            f"Rum &amp;<br/><span class=\"{ACCENT}\">Culture Guide</span>",
            "Hampden Estate distillery, Rose Hall heritage and cultural shore excursions from Falmouth.",
            RUM_IMG, RUM_ALT, breadcrumb="Rum &amp; Culture",
        ),
        "hero-faq.html": hero_inner(
            "Cruise Planning Answers",
            f"Falmouth<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Dock port facts, Martha Brae vs beaches, Dunn's River distance and honest booking status.",
            FAQ_IMG, FAQ_ALT, breadcrumb="FAQ",
        ),
    }
    for tour in TOURS:
        heroes[f"hero-{tour['slug']}.html"] = tour_hero(tour)
    return heroes


def write_worker_and_config() -> None:
    write("worker.js", """/**
 * Falmouth Shore Excursion — Workers Assets entry.
 * www → apex (one hop); .html → extensionless (one hop); combined in one hop when both apply.
 */
const APEX_HOST = 'falmouthshoreexcursion.com';

function stripHtmlPath(pathname) {
  if (!pathname.toLowerCase().endsWith('.html')) return pathname;
  let path = pathname.slice(0, -5);
  if (path.toLowerCase().endsWith('/index')) path = path.slice(0, -6);
  if (path === '' || path === '/index') path = '/';
  return path || '/';
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();
    const isWww = host === `www.${APEX_HOST}`;
    const hasHtml = url.pathname.toLowerCase().endsWith('.html');

    if (isWww || hasHtml) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      if (hasHtml) dest.pathname = stripHtmlPath(url.pathname);
      else if (isWww) dest.pathname = url.pathname || '/';
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    const assetResponse = await env.ASSETS.fetch(request);

    if (assetResponse.status === 404) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    return assetResponse;
  },
};
""")

    write("wrangler.jsonc", """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "falmouth-shore-excursion",
  "main": "worker.js",
  "compatibility_date": "2026-06-06",
  "workers_dev": true,
  "observability": { "enabled": true },
  "assets": {
    "directory": ".",
    "binding": "ASSETS",
    "html_handling": "drop-trailing-slash",
    "not_found_handling": "404-page",
    "run_worker_first": true
  },
  "routes": [
    {
      "pattern": "www.falmouthshoreexcursion.com/*",
      "zone_name": "falmouthshoreexcursion.com"
    },
    {
      "pattern": "falmouthshoreexcursion.com/*",
      "zone_name": "falmouthshoreexcursion.com"
    }
  ]
}
""")

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


def write_attribution() -> None:
    write("images/ATTRIBUTION.md", """# Image attribution

Active imagery for Falmouth Shore Excursion. Prefer OWNED / Wikimedia / Unsplash / Pexels only.
Do not use SEG, OTA, Google Images, or unknown commercial CDNs.

| Asset | Source | Notes / licence |
|-------|--------|-----------------|
| `hero-falmouth.png` | Wikimedia Commons — Dunn's River Falls, Jamaica | CC-compatible Commons source historically used for Falmouth hero |
| `dunns-river-falls.png` | Wikimedia Commons — Dunn's River Falls, Jamaica | Waterfall climb context |
| `martha-brae-rafting.png` | Wikimedia Commons — Martha Brae River, Jamaica | River rafting context |
| `blue-hole-jamaica.png` | Wikimedia Commons — Island Gully Falls / Blue Hole | Correct Blue Hole subject (not Dunn's River) |
| `jamaica-beach.png` | Wikimedia Commons — Doctor's Cave Beach Club, Montego Bay | Beach authority imagery |
| `falmouth-cruise-port.png` | Wikimedia Commons — Falmouth Jamaica Harbour | Port / pier context |
| `falmouth-port-arrival.png` | Wikimedia Commons — Falmouth Jamaica Harbour | Port arrival context (same harbour subject; valid reuse) |
| `falmouth-intro.png` | Unsplash — tropical coastline | General Jamaica north-coast atmosphere |
| `falmouth-safety.png` | Unsplash — tropical coastline | Safety / port-day atmosphere |
| `one-day-falmouth.png` | Unsplash — beach / coast | One-day planning atmosphere |
| `best-falmouth-excursions.png` | Unsplash — tropical water | Excursions hub atmosphere |
| `jamaica-countryside.png` | Unsplash — forest / countryside | Countryside touring atmosphere |
| `private-tour-jamaica.png` | Unsplash — travel road | Private touring atmosphere |
| `river-tubing-jamaica.png` | Pexels — river | River tubing atmosphere |
| `falmouth-faq.png` | Pexels — beach resort | FAQ / beach planning atmosphere |
| `jamaica-highlights.png` | Pexels — waterfall landscape | Highlights touring atmosphere |
| `jamaican-rum.png` | Unsplash — cocktail / spirits still life | Rum & culture atmosphere (not a specific distillery claim) |

Run `npm run images` only to refresh documented Wikimedia sources. Do not overwrite Blue Hole with Dunn's River imagery.
""")


def main() -> None:
    print("Building Falmouth Shore Excursion World 2.0…")

    write("partials/nav.html", nav_html())
    write("partials/footer.html", footer_html())
    write("partials/trust-strip.html", trust_strip_html())

    for name, html in build_hero_defs().items():
        write(f"partials/{name}", html)

    guides = all_guide_content()
    for name, html in guides.items():
        write(f"content/{name}", html)

    tours = all_tour_content()
    for name, html in tours.items():
        write(f"content/{name}", html)

    nav = nav_html()
    footer = footer_html()
    trust = trust_strip_html()
    heroes = build_hero_defs()

    for p in build_page_meta():
        hero_key = p["hero"].replace("partials/", "") if p.get("hero") else ""
        content_key = p["content"] if p["content"].endswith(".html") else f"{p['content']}.html"
        if content_key.startswith("content/"):
            content_key = content_key.replace("content/", "")
        content_html = guides.get(content_key) or tours.get(content_key, "")
        write(
            p["file"],
            static_page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                nav=nav,
                hero=heroes.get(hero_key, ""),
                content=content_html,
                footer=footer,
                trust=trust if p.get("trust") else "",
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
                main_pad=bool(p.get("main_pad")),
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

    write_worker_and_config()
    write_attribution()

    write("README.md", """# Falmouth Shore Excursion

Independent cruise-passenger planning guide for Falmouth, Jamaica shore excursions (World 2.0 static specialist).

## Development

```bash
npm install
npm run build
npm run check
npm run preview
```

Open http://localhost:8910 — primary content is inlined in HTML (works without JavaScript).

## Deploy to Cloudflare

```bash
npm run build && npm run check && ./deploy.sh
```

Domain: https://falmouthshoreexcursion.com

Schedule integration and direct payment are deferred.
""")

    # Ensure image files exist; do not overwrite meaningful assets with harbour clones
    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    for img in ALL_IMAGES:
        p = ROOT / img
        if not p.exists() or p.stat().st_size < 1000:
            print(f"  warning: missing or tiny image {img}")

    print("Done.")


if __name__ == "__main__":
    main()
