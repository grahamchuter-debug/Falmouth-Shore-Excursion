"""Falmouth Shore Excursion site configuration."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://falmouthshoreexcursion.com"
SITE = "Falmouth Shore Excursion"
DATE = "2026-06-06"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(37, 99, 235, 0.75) 0%, "
    "rgba(249, 115, 22, 0.65) 50%, rgba(30, 58, 138, 0.55) 100%)"
)
ACCENT = "text-pr-300"

HOME_HERO = "images/hero-falmouth.png"
HOME_HERO_ALT = (
    "Cascading tiers of Dunn's River Falls in Jamaica with lush green foliage "
    "and turquoise pool — iconic shore excursion destination for cruise "
    "passengers visiting Falmouth Jamaica cruise port"
)
PORT_IMG = "images/falmouth-cruise-port.png"
PORT_ALT = (
    "Falmouth Jamaica cruise port with cruise ship docked at Historic Falmouth "
    "Pier for cruise passenger shore excursion pickups"
)
PORT_ARRIVAL_IMG = "images/falmouth-port-arrival.png"
PORT_ARRIVAL_ALT = (
    "Cruise ship docked at Falmouth Jamaica Historic Pier with passengers "
    "disembarking for shore excursions in Trelawny parish"
)
BEST_IMG = "images/best-falmouth-excursions.png"
BEST_ALT = (
    "Jamaica coastline and waterfalls representing the best Falmouth shore "
    "excursions for cruise passengers from Falmouth Jamaica cruise port"
)
ONE_DAY_IMG = "images/one-day-falmouth.png"
ONE_DAY_ALT = (
    "Jamaican rainforest and coastline for planning a one-day cruise ship "
    "shore excursion itinerary from Falmouth Jamaica"
)
INTRO_IMG = "images/falmouth-intro.png"
INTRO_ALT = (
    "Scenic Jamaica north coast near Falmouth cruise port for waterfall, "
    "river rafting and beach shore excursions"
)
DUNNS_IMG = "images/dunns-river-falls.png"
DUNNS_ALT = (
    "Cruise passengers climbing the terraced limestone rocks of Dunn's River "
    "Falls in Jamaica during a shore excursion from Falmouth cruise port"
)
MARTHA_IMG = "images/martha-brae-rafting.png"
MARTHA_ALT = (
    "Cruise passengers enjoying a peaceful bamboo rafting tour on the "
    "turquoise Martha Brae River surrounded by lush tropical forest near "
    "Falmouth Jamaica cruise port"
)
BLUE_HOLE_IMG = "images/blue-hole-jamaica.png"
BLUE_HOLE_ALT = (
    "Turquoise Blue Hole lagoon with cascading waterfall and lush tropical "
    "rainforest on a Jamaica adventure shore excursion from Falmouth cruise "
    "port"
)
BEACH_IMG = "images/jamaica-beach.png"
BEACH_ALT = (
    "White sand Jamaica beach and turquoise Caribbean water on a cruise "
    "passenger beach escape shore excursion from Falmouth"
)
COUNTRYSIDE_IMG = "images/jamaica-countryside.png"
COUNTRYSIDE_ALT = (
    "Jamaican countryside villages and lush hills on a sightseeing shore "
    "excursion for cruise passengers from Falmouth Jamaica"
)
TUBING_IMG = "images/river-tubing-jamaica.png"
TUBING_ALT = (
    "River tubing adventure through Jamaica rainforest on a shore excursion "
    "for cruise passengers from Falmouth Jamaica cruise port"
)
RUM_IMG = "images/jamaican-rum.png"
RUM_ALT = (
    "Traditional Jamaican rum distillery tasting experience on a cultural "
    "shore excursion for cruise passengers from Falmouth Jamaica"
)
PRIVATE_IMG = "images/private-tour-jamaica.png"
PRIVATE_ALT = (
    "Private driver guide tour with scenic Jamaica viewpoints on a full-day "
    "shore excursion for cruise passengers from Falmouth port"
)
HIGHLIGHTS_IMG = "images/jamaica-highlights.png"
HIGHLIGHTS_ALT = (
    "Jamaica highlights including historic great house and coastal scenery "
    "on a sightseeing shore excursion from Falmouth cruise port"
)
FAQ_IMG = "images/falmouth-faq.png"
FAQ_ALT = (
    "Falmouth Jamaica waterfront and cruise port area for cruise passenger "
    "shore excursion planning and FAQ guidance"
)
SAFETY_IMG = "images/falmouth-safety.png"
SAFETY_ALT = (
    "Organised shore excursion group at Falmouth Jamaica cruise port for "
    "safe cruise passenger day trips in Jamaica"
)

CATEGORY_IMAGES = {
    "waterfall": (DUNNS_IMG, DUNNS_ALT),
    "martha": (MARTHA_IMG, MARTHA_ALT),
    "bluehole": (BLUE_HOLE_IMG, BLUE_HOLE_ALT),
    "beach": (BEACH_IMG, BEACH_ALT),
    "countryside": (COUNTRYSIDE_IMG, COUNTRYSIDE_ALT),
    "tubing": (TUBING_IMG, TUBING_ALT),
    "rum": (RUM_IMG, RUM_ALT),
    "private": (PRIVATE_IMG, PRIVATE_ALT),
    "highlights": (HIGHLIGHTS_IMG, HIGHLIGHTS_ALT),
    "combo": (INTRO_IMG, INTRO_ALT),
}

ALL_IMAGES = [
    HOME_HERO, PORT_IMG, PORT_ARRIVAL_IMG, BEST_IMG, ONE_DAY_IMG, INTRO_IMG,
    DUNNS_IMG, MARTHA_IMG, BLUE_HOLE_IMG, BEACH_IMG, COUNTRYSIDE_IMG,
    TUBING_IMG, RUM_IMG, PRIVATE_IMG, HIGHLIGHTS_IMG, FAQ_IMG, SAFETY_IMG,
]

SHIP_ICON = (
    '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">'
    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" '
    'd="M3 17h18M5 17l2-8h10l2 8M9 9l1-4h4l1 4"/></svg>'
)

PLACEHOLDER_PNG = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
    b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
)

GUIDE_PAGES = [
    "falmouth-port-guide",
    "one-day-in-falmouth-from-a-cruise-ship",
    "best-falmouth-shore-excursions",
    "dunns-river-falls-guide",
    "martha-brae-river-rafting-guide",
    "blue-hole-jamaica-guide",
    "is-falmouth-safe-for-cruise-passengers",
    "can-you-explore-falmouth-without-an-excursion",
    "best-beaches-near-falmouth-jamaica",
    "jamaican-rum-and-culture-guide",
]
