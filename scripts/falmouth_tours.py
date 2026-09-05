"""Tour page content for Falmouth Shore Excursion — editorial / commercial-research only."""
from falmouth_config import CATEGORY_IMAGES, INTRO_ALT, INTRO_IMG, PORT_ALT, PORT_IMG
from falmouth_helpers import content_tour_page, href
from falmouth_tours_data import TOURS


def _family_note(tour: dict) -> str:
    activity = tour["activity"]
    size = tour["size"]
    cat = tour["category"]
    if activity == "Easy":
        return "Often suitable for families and mixed ages"
    if cat in ("beach", "martha"):
        return "Often suitable for families — relaxed pacing and easy activity"
    if size == "Private":
        return "Flexible pacing for families and private groups"
    if size == "Small":
        return "Useful for families wanting smaller groups"
    return "Check age limits for waterfall climbs; suitable for many teens and active families"


def _popular_types(category: str) -> str:
    mapping = {
        "waterfall": "Dunn's River Falls, Ocho Rios waterfalls, nature tours",
        "martha": "Bamboo rafting, river experiences, tranquil floats",
        "bluehole": "Blue Hole swimming, rainforest adventures, Ocho Rios hinterland",
        "beach": "Beach clubs, Montego Bay beach corridor, island time",
        "countryside": "Fern Gully, coffee farms, jerk lunch, local culture",
        "tubing": "River tubing, lazy river floats, rainforest",
        "rum": "Hampden Estate, rum tastings, distillery tours",
        "private": "Custom itineraries, private driver guides",
        "highlights": "Rose Hall, Montego Bay, heritage sightseeing",
        "combo": "Multi-activity combos, adventure packages",
    }
    return mapping.get(category, "Falmouth shore excursions, Jamaica cruise port tours")


def _best_for(tour: dict) -> str:
    cat = tour["category"]
    if tour["size"] == "Private":
        return "Groups wanting private pacing and a dedicated driver/guide"
    if cat == "waterfall":
        return "First-time Jamaica visitors wanting the iconic waterfall when shore time allows"
    if cat == "martha":
        return "Couples and relaxed travellers wanting a scenic river float nearer Falmouth"
    if cat == "bluehole":
        return "Adventure seekers exploring rainforest pools on a longer inland day"
    if cat == "beach":
        return "Families and passengers wanting a relaxed Caribbean beach day"
    if cat == "countryside":
        return "Culture-focused travellers and food lovers"
    if cat == "tubing":
        return "Active travellers wanting a river float adventure"
    if cat == "rum":
        return "Adults interested in Jamaican rum heritage and tastings"
    if cat == "highlights":
        return "History-minded travellers exploring Montego Bay heritage"
    return f"Passengers comparing {tour['title']} from Falmouth"


def _intro(tour: dict) -> str:
    title = tour["title"]
    seg = tour["seg_desc"]
    size = tour["size"]
    duration = tour["duration"]
    if size == "Small":
        size_note = "Small-group formats keep pacing personal with pickup framed at the Falmouth cruise port."
    elif size == "Private":
        size_note = "Private format lets your group set the pace with a dedicated driver/guide from the Falmouth pier."
    else:
        size_note = "Standard-group formats typically use Historic Falmouth Pier pickup and plan returns around cruise schedules — confirm details with any operator you choose."
    return (
        f"{title} is a Falmouth Jamaica shore-excursion style day many cruise passengers compare. "
        f"{seg} Published duration on this page is {duration.lower()}. {size_note} "
        f"This page is editorial only — no prices, availability or checkout here."
    )


def _bullets(tour: dict) -> list[str]:
    bullets = [
        f"Commonly listed around {tour['duration']} including transport from Falmouth cruise port — confirm the product you book.",
        f"{tour['activity']} activity level — plan footwear and fitness accordingly.",
        "Port pickup typically framed at Historic Falmouth Pier on Jamaica's north coast.",
        "Plan your own conservative buffer before all-aboard; confirm return policies with your operator.",
    ]
    if tour["size"] == "Small":
        bullets.append("Small-group format for more personal guide attention when offered.")
    elif tour["size"] == "Private":
        bullets.append("Private excursion style — your group, your pace, dedicated transport.")
    else:
        bullets.append("Cruise-timed departures are operator-specific — verify meeting instructions before travel.")
    cat = tour["category"]
    if cat in ("waterfall", "bluehole"):
        bullets.append("Longer drive from Falmouth than Martha Brae — not adjacent to the pier.")
    if cat == "martha":
        bullets.append("Often nearer to Falmouth than Ocho Rios waterfall or Blue Hole days.")
    return bullets


def _why_choose(tour: dict) -> list[str]:
    cat = tour["category"]
    points = [
        "Framed around Falmouth cruise port logistics — clear meeting points matter on ship days.",
        "Useful as a planning comparison even when you book elsewhere.",
        "North-coast drive times, waterfall conditions and beach access change — verify locally.",
    ]
    if tour["size"] == "Private":
        points.append("Private format helps when your group wants flexibility without a large coach.")
    elif tour["size"] == "Small":
        points.append("Smaller headcount can mean faster transitions when the operator delivers.")
    if cat == "waterfall":
        points.append("Dunn's River Falls is Jamaica's signature climb — plan the Ocho Rios transfer honestly.")
    elif cat == "martha":
        points.append("Martha Brae bamboo rafting is one of Jamaica's most peaceful river experiences near Falmouth.")
    elif cat == "bluehole":
        points.append("Blue Hole offers rainforest pools inland — treat it as a longer day from Falmouth.")
    elif cat == "beach":
        points.append("Beach escapes suit passengers who want swimming and facilities without designing every transfer.")
    elif cat == "rum":
        points.append("Hampden Estate showcases long-running Jamaican rum-making heritage with guided tastings when offered.")
    return points


def _highlights(tour: dict, img: str, alt: str) -> list[tuple]:
    cat = tour["category"]
    title = tour["title"]
    cards = [
        (img, alt, title, tour["seg_desc"]),
        (PORT_IMG, PORT_ALT, "Falmouth Port Pickup", "Meeting points are usually at or near Historic Falmouth Pier — confirm exact instructions."),
        (img, f"{title} shore excursion highlight for Falmouth Jamaica cruise passengers", "Return Planning", "Leave margin before all-aboard; this site does not guarantee ship waits."),
    ]
    if cat == "waterfall":
        cards[0] = (img, alt, "Iconic Waterfall", "Climb the terraced cascades at Dunn's River Falls when fitness and shore time allow.")
    elif cat == "martha":
        cards[0] = (img, alt, "Bamboo Rafting", "Glide along the Martha Brae on a hand-poled bamboo raft through tropical scenery.")
    elif cat == "bluehole":
        cards[0] = (img, alt, "Rainforest Pools", "Swim in Blue Hole pools tucked in the Jamaican hills — jumps are optional where offered.")
    return cards


def _extra_links(tour: dict) -> list[tuple[str, str]]:
    cat = tour["category"]
    links = [
        ("falmouth-port-guide", "Port Guide"),
        ("best-falmouth-shore-excursions", "Best Excursions"),
        ("one-day-in-falmouth-from-a-cruise-ship", "One Day in Falmouth"),
    ]
    if cat == "waterfall":
        links.append(("dunns-river-falls-guide", "Dunn's River Falls Guide"))
    elif cat == "martha":
        links.append(("martha-brae-river-rafting-guide", "Martha Brae Guide"))
    elif cat == "bluehole":
        links.append(("blue-hole-jamaica-guide", "Blue Hole Guide"))
    elif cat == "beach":
        links.append(("best-beaches-near-falmouth-jamaica", "Beach Guide"))
    elif cat == "rum":
        links.append(("jamaican-rum-and-culture-guide", "Rum &amp; Culture Guide"))
    elif cat == "private":
        links.append(("martha-brae-river-rafting-guide", "Martha Brae Guide"))
    return links


def _editorial_note(tour: dict) -> str:
    if tour["category"] == "martha":
        return (
            f'Editorial / commercial-research page. Read the companion '
            f'<a href="{href("martha-brae-river-rafting-guide")}" class="text-ocean-600 font-semibold">Martha Brae guide</a> '
            f'for cruise-day context. No booking on this site.'
        )
    if tour["category"] == "beach":
        return (
            f'Editorial beach day page. Compare context on '
            f'<a href="{href("best-beaches-near-falmouth-jamaica")}" class="text-ocean-600 font-semibold">Best Beaches</a>.'
        )
    if tour["category"] == "waterfall":
        return (
            f'Editorial waterfall page. Dunn\'s River is a longer drive from Falmouth — see the '
            f'<a href="{href("dunns-river-falls-guide")}" class="text-ocean-600 font-semibold">falls guide</a>.'
        )
    if tour["category"] == "bluehole":
        return (
            f'Editorial adventure page. Blue Hole is inland from Ocho Rios — see the '
            f'<a href="{href("blue-hole-jamaica-guide")}" class="text-ocean-600 font-semibold">Blue Hole guide</a>.'
        )
    if tour["category"] == "private":
        return "Editorial private-touring page — useful for planning custom days; no supplier rates or checkout here."
    return "Editorial planning page — not live inventory."


def _tour_content(tour: dict) -> str:
    cat = tour["category"]
    img, alt = CATEGORY_IMAGES.get(cat, (INTRO_IMG, INTRO_ALT))
    alt = f"{tour['title']} Falmouth Jamaica shore excursion for cruise passengers — {alt}"
    return content_tour_page(
        _intro(tour),
        _bullets(tour),
        _highlights(tour, img, alt),
        dict(
            best_for=_best_for(tour),
            activity_level=tour["activity"],
            family=_family_note(tour),
            popular=_popular_types(cat),
            return_ship="Confirm buffer and meeting points with your operator",
        ),
        img,
        alt,
        _why_choose(tour),
        badge=tour.get("badge"),
        highlights_subtitle=f"What to expect when comparing {tour['title']} from Falmouth Jamaica cruise port.",
        extra_links=_extra_links(tour),
        editorial_note=_editorial_note(tour),
    )


def all_tour_content() -> dict[str, str]:
    return {f"{t['slug']}.html": _tour_content(t) for t in TOURS}


def comparison_rows() -> list[tuple]:
    featured = [t for t in TOURS if t.get("featured")]
    # Include non-featured that matter for hub completeness
    extra_slugs = {"river-tubing-adventure", "jamaica-highlights-tour", "rum-and-culture-experience"}
    seen = {t["slug"] for t in featured}
    rows_tours = list(featured)
    for t in TOURS:
        if t["slug"] in extra_slugs and t["slug"] not in seen:
            rows_tours.append(t)
    rows = []
    for t in rows_tours:
        dur = t["duration"].replace(" Hours", " hrs").replace(" Hour", " hr").replace(" Minutes", " min")
        rows.append((
            t["title"],
            dur,
            t.get("badge", "Falmouth excursion").replace("Best ", ""),
            t["activity"],
            t["slug"],
        ))
    return rows
