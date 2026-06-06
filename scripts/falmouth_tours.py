"""Tour page content for Falmouth Shore Excursion."""
from falmouth_config import CATEGORY_IMAGES, INTRO_ALT, INTRO_IMG, PORT_ALT, PORT_IMG
from falmouth_helpers import content_tour_page
from falmouth_tours_data import TOURS


def _family_note(tour: dict) -> str:
    activity = tour["activity"]
    size = tour["size"]
    cat = tour["category"]
    if activity == "Easy":
        return "Excellent for families and mixed ages"
    if cat == "beach" or cat == "martha":
        return "Great for families — relaxed pacing and easy activity"
    if size == "Private":
        return "Flexible pacing for families and private groups"
    if size == "Small":
        return "Good for families wanting smaller groups"
    return "Good for teens and active families; check age limits for waterfall climbs"


def _popular_types(category: str) -> str:
    mapping = {
        "waterfall": "Dunn's River Falls, Ocho Rios waterfalls, nature tours",
        "martha": "Bamboo rafting, river experiences, tranquil floats",
        "bluehole": "Blue Hole swimming, rainforest adventures, Ocho Rios",
        "beach": "Beach clubs, Montego Bay beaches, island time",
        "countryside": "Fern Gully, coffee farms, jerk lunch, local culture",
        "tubing": "White water tubing, lazy river floats, rainforest",
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
        return "First-time Jamaica visitors and waterfall lovers"
    if cat == "martha":
        return "Couples and relaxed travelers wanting a scenic river float"
    if cat == "bluehole":
        return "Adventure seekers and swimmers exploring rainforest pools"
    if cat == "beach":
        return "Families and passengers wanting a relaxed Caribbean beach day"
    if cat == "countryside":
        return "Culture-focused travelers and food lovers"
    if cat == "tubing":
        return "Active travelers wanting river adventure"
    if cat == "rum":
        return "Adults interested in Jamaican rum heritage and tastings"
    if cat == "highlights":
        return "History buffs and couples exploring Montego Bay heritage"
    return f"Passengers booking {tour['title']} from Falmouth"


def _intro(tour: dict) -> str:
    title = tour["title"]
    seg = tour["seg_desc"]
    size = tour["size"]
    duration = tour["duration"]
    if size == "Small":
        size_note = "Small-group departure keeps pacing personal with straightforward pickup at the Falmouth cruise port."
    elif size == "Private":
        size_note = "Private format lets your group set the pace with a dedicated driver/guide from the Falmouth pier."
    else:
        size_note = "Standard-group format with port pickup at Historic Falmouth Pier and return-to-ship timing built for cruise schedules."
    return (
        f"{title} is one of the shore excursions cruise passengers book most from Falmouth, Jamaica. "
        f"{seg} Operators meet you at the cruise port and plan the {duration.lower()} itinerary "
        f"with buffer before your ship's all-aboard call. {size_note}"
    )


def _bullets(tour: dict) -> list[str]:
    bullets = [
        f"{tour['duration']} including transport from Falmouth cruise port.",
        f"{tour['activity']} activity level — plan footwear and fitness accordingly.",
        "Port pickup at Historic Falmouth Pier on the north coast of Jamaica.",
        "Return-to-ship guarantee with 60–90 minute buffer before all aboard.",
    ]
    if tour["size"] == "Small":
        bullets.append("Small-group format for more personal guide attention.")
    elif tour["size"] == "Private":
        bullets.append("Private excursion — your group, your pace, dedicated transport.")
    else:
        bullets.append("Easy booking with cruise-timed departures and clear meeting instructions.")
    return bullets


def _why_choose(tour: dict) -> list[str]:
    cat = tour["category"]
    points = [
        "Designed around Falmouth cruise port logistics — clear meeting points right at the pier.",
        "Return-to-ship focus with operators who understand cruise all-aboard deadlines.",
        "Local guides who know north-coast drive times, waterfall conditions and beach club access.",
    ]
    if tour["size"] == "Private":
        points.append("Private format ideal when your group wants flexibility without sharing a large coach.")
    elif tour["size"] == "Small":
        points.append("Smaller headcount means faster transitions and more time at each stop.")
    if cat == "waterfall":
        points.append("Dunn's River Falls is Jamaica's signature experience — human-chain climbs with expert guides.")
    elif cat == "martha":
        points.append("Martha Brae bamboo rafting is one of Jamaica's most peaceful and photogenic river experiences.")
    elif cat == "bluehole":
        points.append("Blue Hole offers unspoiled rainforest pools away from the busiest cruise crowds.")
    elif cat == "beach":
        points.append("Beach escapes timed for calmer morning departures and reliable port returns.")
    elif cat == "rum":
        points.append("Hampden Estate showcases centuries of Jamaican rum-making heritage with guided tastings.")
    return points


def _highlights(tour: dict, img: str, alt: str) -> list[tuple]:
    cat = tour["category"]
    title = tour["title"]
    cards = [
        (img, alt, title, tour["seg_desc"]),
        (PORT_IMG, PORT_ALT, "Falmouth Port Pickup", "Meet at Historic Falmouth Pier — transport included on organised excursions."),
        (img, f"{title} shore excursion highlight for Falmouth Jamaica cruise passengers", "Cruise-Timed Returns", "Itineraries built with buffer before all aboard so you can enjoy Jamaica without watching the clock."),
    ]
    if cat == "waterfall":
        cards[0] = (img, alt, "Iconic Waterfall", "Climb the terraced cascades at Dunn's River Falls — Jamaica's most famous natural attraction.")
    elif cat == "martha":
        cards[0] = (img, alt, "Bamboo Rafting", "Glide along the Martha Brae on a hand-poled bamboo raft through lush tropical scenery.")
    elif cat == "bluehole":
        cards[0] = (img, alt, "Rainforest Pools", "Swim and cliff-jump in crystal-clear Blue Hole pools tucked in the Jamaican hills.")
    return cards


def _extra_links(tour: dict) -> list[tuple[str, str]]:
    cat = tour["category"]
    links = [
        ("falmouth-port-guide.html", "Port Guide"),
        ("best-falmouth-shore-excursions.html", "Best Excursions"),
        ("one-day-in-falmouth-from-a-cruise-ship.html", "One Day in Falmouth"),
    ]
    if cat == "waterfall":
        links.append(("dunns-river-falls-guide.html", "Dunn's River Falls Guide"))
    elif cat == "martha":
        links.append(("martha-brae-river-rafting-guide.html", "Martha Brae Guide"))
    elif cat == "bluehole":
        links.append(("blue-hole-jamaica-guide.html", "Blue Hole Guide"))
    elif cat == "beach":
        links.append(("best-beaches-near-falmouth-jamaica.html", "Beach Guide"))
    elif cat == "rum":
        links.append(("jamaican-rum-and-culture-guide.html", "Rum &amp; Culture Guide"))
    return links


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
        ),
        img,
        alt,
        _why_choose(tour),
        badge=tour.get("badge"),
        highlights_subtitle=f"What to expect on {tour['title']} from Falmouth Jamaica cruise port.",
        extra_links=_extra_links(tour),
    )


def all_tour_content() -> dict[str, str]:
    return {f"{t['slug']}.html": _tour_content(t) for t in TOURS}


def comparison_rows() -> list[tuple]:
    featured = [t for t in TOURS if t.get("featured")]
    rows = []
    for t in featured:
        dur = t["duration"].replace(" Hours", " hrs").replace(" Hour", " hr").replace(" Minutes", " min")
        rows.append((
            t["title"],
            dur,
            t.get("badge", "Falmouth excursion").replace("Best ", ""),
            t["activity"],
            f"{t['slug']}.html",
        ))
    return rows
