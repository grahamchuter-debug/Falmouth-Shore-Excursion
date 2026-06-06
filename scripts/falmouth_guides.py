"""Guide and home page content for Falmouth Shore Excursion."""
from falmouth_config import (
    BEACH_ALT,
    BEACH_IMG,
    BEST_ALT,
    BEST_IMG,
    BLUE_HOLE_ALT,
    BLUE_HOLE_IMG,
    COUNTRYSIDE_ALT,
    COUNTRYSIDE_IMG,
    DUNNS_ALT,
    DUNNS_IMG,
    FAQ_ALT,
    FAQ_IMG,
    INTRO_ALT,
    INTRO_IMG,
    MARTHA_ALT,
    MARTHA_IMG,
    ONE_DAY_ALT,
    ONE_DAY_IMG,
    PORT_ARRIVAL_ALT,
    PORT_ARRIVAL_IMG,
    PORT_ALT,
    PORT_IMG,
    PRIVATE_ALT,
    PRIVATE_IMG,
    RUM_ALT,
    RUM_IMG,
    SAFETY_ALT,
    SAFETY_IMG,
)
from falmouth_helpers import card_grid, comparison_section, internal_links, snapshot_default
from falmouth_tours import comparison_rows
from falmouth_tours_data import FEATURED_TOURS, TOURS


def _featured_cards() -> str:
    cards = []
    for slug in FEATURED_TOURS[:4]:
        t = next(x for x in TOURS if x["slug"] == slug)
        from falmouth_config import CATEGORY_IMAGES
        img, alt = CATEGORY_IMAGES.get(t["category"], (INTRO_IMG, INTRO_ALT))
        cards.append((
            img, alt, t["title"], t["seg_desc"][:120] + "…",
            f"{slug}.html", "View Tour",
        ))
    return card_grid(cards)


def content_home() -> str:
    best_cards = card_grid([
        (DUNNS_IMG, DUNNS_ALT, "Dunn's River Falls", "Climb Jamaica's iconic 600-foot terraced waterfall near Ocho Rios.", "dunns-river-falls-tour.html", "Waterfall Tour"),
        (MARTHA_IMG, MARTHA_ALT, "Martha Brae Rafting", "Peaceful bamboo rafting on one of Jamaica's most scenic rivers.", "martha-brae-river-rafting.html", "River Rafting"),
        (BLUE_HOLE_IMG, BLUE_HOLE_ALT, "Blue Hole Adventure", "Rainforest pools, waterfalls and swimming in unspoiled St. Mary.", "blue-hole-adventure.html", "Blue Hole"),
        (BEACH_IMG, BEACH_ALT, "Beach Escape", "White sand, turquoise water and a relaxed Caribbean beach day.", "beach-escape-excursion.html", "Beach Day"),
    ])
    featured = _featured_cards()
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <div class="section-label mx-auto">Best Excursions</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Best Falmouth Shore Excursions</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Ranked for cruise schedules — Dunn's River Falls, Martha Brae rafting, Blue Hole adventures and beach escapes from Falmouth, Jamaica.</p>
  </div>
  {best_cards}
  <p class="text-center mt-8"><a href="best-falmouth-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">See full comparison →</a></p>
</div></section>
<section class="pt-4 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Falmouth Jamaica Cruise Port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Passengers<br/><span class="text-ocean-600">Choose Falmouth</span></h2>
    <p class="text-gray-600 leading-relaxed mb-5">Falmouth puts <strong>Dunn's River Falls</strong>, <strong>Martha Brae rafting</strong>, rainforest <strong>Blue Hole</strong> pools and north-coast beaches within reach on a typical <strong>6–10 hour</strong> port call. Jamaica dollars (JMD) are official; <strong>USD</strong> is widely accepted near the cruise port.</p>
    <a href="falmouth-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port Guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Featured Excursions</h2>
  <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Most-booked shore excursions for cruise passengers from Falmouth, Jamaica.</p></div>
  {featured}
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-10">Top Things To Do In Falmouth</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Dunn's River Falls</h3><p class="text-gray-600">Climb the famous terraced waterfall near Ocho Rios — Jamaica's most iconic shore excursion.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Martha Brae Rafting</h3><p class="text-gray-600">Traditional bamboo rafting on a tranquil river — perfect for couples and relaxed port days.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Blue Hole</h3><p class="text-gray-600">Swim in crystal-clear rainforest pools and waterfalls in the hills above Ocho Rios.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Beach Escape</h3><p class="text-gray-600">White sand beaches and turquoise water on Jamaica's north coast near Montego Bay.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Countryside Tour</h3><p class="text-gray-600">Fern Gully, coffee farms, local markets and authentic jerk lunch in the Jamaican hills.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Rum &amp; Culture</h3><p class="text-gray-600">Hampden Estate distillery tours and tastings — centuries of Jamaican rum heritage.</p></div>
  </div>
</div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{DUNNS_IMG}" alt="{DUNNS_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Dunn's River Falls</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Dunn's River Falls is Jamaica's signature experience — a 600-foot terraced waterfall you climb hand-in-hand with guides and fellow passengers. The falls sit near <strong>Ocho Rios</strong>, about <strong>45 minutes east</strong> of the Falmouth cruise port.</p>
    <p class="text-gray-600 leading-relaxed mb-5">The focused <a href="dunns-river-falls-tour.html" class="text-ocean-600 font-medium">Dunn's River Falls Tour</a> is ideal for waterfall purists. The <a href="dunns-river-falls-and-area-highlights.html" class="text-ocean-600 font-medium">Area Highlights</a> tour adds Ocho Rios sightseeing. See our <a href="dunns-river-falls-guide.html" class="text-ocean-600 font-medium">Dunn's River Falls guide</a> for distances and tips.</p>
    <a href="dunns-river-falls-tour.html" class="text-ocean-600 font-semibold text-sm">Dunn's River Falls excursions →</a>
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Martha Brae River Rafting</h2>
    <p class="text-gray-600 leading-relaxed mb-4"><strong>Martha Brae River</strong> bamboo rafting is one of Jamaica's most peaceful experiences — glide along calm waters on a hand-poled raft while your raftsman shares local folklore. The river is about <strong>20–30 minutes</strong> from Falmouth.</p>
    <p class="text-gray-600 leading-relaxed mb-5">The <a href="martha-brae-river-rafting.html" class="text-ocean-600 font-medium">Martha Brae River Rafting</a> excursion fits most port calls with easy activity level. Read our <a href="martha-brae-river-rafting-guide.html" class="text-ocean-600 font-medium">Martha Brae guide</a> for what to expect.</p>
    <a href="martha-brae-river-rafting.html" class="text-ocean-600 font-semibold text-sm">Martha Brae rafting →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{MARTHA_IMG}" alt="{MARTHA_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BLUE_HOLE_IMG}" alt="{BLUE_HOLE_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Blue Hole Adventure</h2>
    <p class="text-gray-600 leading-relaxed mb-4">The <strong>Blue Hole</strong> is an unspoiled rainforest gem in the hills of St. Mary — turquoise pools, cascading waterfalls and cliff-jumping opportunities away from the busiest tourist crowds. About <strong>45 minutes</strong> from Falmouth.</p>
    <p class="text-gray-600 leading-relaxed mb-5">The <a href="blue-hole-adventure.html" class="text-ocean-600 font-medium">Blue Hole Adventure</a> includes lunch and Ocho Rios shopping time. Compare options in our <a href="blue-hole-jamaica-guide.html" class="text-ocean-600 font-medium">Blue Hole guide</a>.</p>
    <a href="blue-hole-adventure.html" class="text-ocean-600 font-semibold text-sm">Blue Hole adventures →</a>
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Beach Experiences</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Jamaica's north coast offers white sand beaches and warm Caribbean water within <strong>30–45 minutes</strong> of Falmouth. Beach club excursions include facilities, food options and return-to-ship timing built for cruise schedules.</p>
    <p class="text-gray-600 leading-relaxed mb-5">The <a href="beach-escape-excursion.html" class="text-ocean-600 font-medium">Beach Escape Excursion</a> is the go-to relaxed port day. See <a href="best-beaches-near-falmouth-jamaica.html" class="text-ocean-600 font-medium">best beaches near Falmouth</a> for comparisons.</p>
    <a href="best-beaches-near-falmouth-jamaica.html" class="text-ocean-600 font-semibold text-sm">Beach guide →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
{comparison_section(comparison_rows())}
{home_faq_section()}
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Falmouth Port Day</h2>
  <p class="text-white/85 text-sm mb-6">Compare excursions, read the Falmouth port guide and build your Jamaica itinerary before you dock in Falmouth.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="best-falmouth-shore-excursions.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Compare Excursions</a>
    <a href="falmouth-port-guide.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
  </div>
</div></section>"""


def home_faq_section() -> str:
    return """<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">Falmouth Shore Excursions FAQ</h2>
  <div class="space-y-4">
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Falmouth a dock or tender port?</summary>
      <p class="mt-4 text-sm text-gray-500">Falmouth is a <strong>dock port</strong> — ships tie up at Historic Falmouth Pier and you walk off directly. No tender boats required.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far is Dunn's River Falls from Falmouth?</summary>
      <p class="mt-4 text-sm text-gray-500">Dunn's River Falls near Ocho Rios is approximately <strong>23 miles / 45 minutes</strong> east of the Falmouth cruise port by road.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is the best excursion for first-time visitors?</summary>
      <p class="mt-4 text-sm text-gray-500">Dunn's River Falls and the Area Highlights tour showcase Jamaica's iconic waterfall. Martha Brae rafting suits passengers wanting a relaxed experience.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Falmouth?</summary>
      <p class="mt-4 text-sm text-gray-500">Most Falmouth port calls are 6 to 10 hours. Full-day waterfall tours need 5–6 hours; Martha Brae rafting fits shorter windows.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What currency is used in Jamaica?</summary>
      <p class="mt-4 text-sm text-gray-500">Jamaican dollars (JMD) are official. US dollars are widely accepted near the cruise port — carry small bills for tips and souvenirs.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Falmouth safe for shore excursions?</summary>
      <p class="mt-4 text-sm text-gray-500">Organised excursions with reputable operators are the standard approach. See our <a href="is-falmouth-safe-for-cruise-passengers.html" class="text-ocean-600">safety guide</a>.</p></details>
  </div>
  <p class="text-center mt-8"><a href="falmouth-port-guide.html" class="text-ocean-600 font-semibold text-sm">Read port guide →</a></p>
</div></section>"""


def home_faq_data() -> list[tuple[str, str]]:
    return [
        ("Is Falmouth Jamaica a dock port for cruise ships?", "Yes — ships dock at Historic Falmouth Pier and passengers walk off directly."),
        ("How far is Dunn's River Falls from the Falmouth cruise port?", "Approximately 23 miles / 45 minutes east to Ocho Rios."),
        ("How far is Martha Brae River from Falmouth?", "Approximately 20–30 minutes by road from the Falmouth cruise port."),
        ("How long do cruise ships stay in Falmouth Jamaica?", "Most port calls are 6 to 10 hours."),
        ("What currency is used in Jamaica?", "Jamaican dollars (JMD); US dollars widely accepted near the port."),
        ("What is the best Falmouth excursion for first-time visitors?", "Dunn's River Falls or the Area Highlights tour."),
        ("Is Falmouth safe for cruise passengers on excursions?", "Organised shore excursions with return-to-ship guarantees are the recommended approach."),
    ]


def content_best_excursions() -> str:
    snap = snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    rankings = """<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveler Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Families</h3><p class="text-gray-600 mb-3">Beach Escape, Martha Brae rafting and countryside tours suit mixed ages.</p><a href="beach-escape-excursion.html" class="text-ocean-600 font-semibold">Beach Escape →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Adventure Seekers</h3><p class="text-gray-600 mb-3">Blue Hole, river tubing and Dunn's River Falls climbs.</p><a href="blue-hole-adventure.html" class="text-ocean-600 font-semibold">Blue Hole →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">First Timers</h3><p class="text-gray-600 mb-3">Dunn's River Falls and Area Highlights — Jamaica's iconic experience.</p><a href="dunns-river-falls-and-area-highlights.html" class="text-ocean-600 font-semibold">Area Highlights →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Couples</h3><p class="text-gray-600 mb-3">Martha Brae rafting and Jamaica Highlights heritage tour.</p><a href="martha-brae-river-rafting.html" class="text-ocean-600 font-semibold">Martha Brae →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Culture Lovers</h3><p class="text-gray-600 mb-3">Countryside sightseeing, rum distillery and Rose Hall heritage.</p><a href="rum-and-culture-experience.html" class="text-ocean-600 font-semibold">Rum Tour →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Private Groups</h3><p class="text-gray-600 mb-3">Full-day private driver/guide with custom itinerary.</p><a href="private-driver-guide-full-day.html" class="text-ocean-600 font-semibold">Private Tour →</a></div>
  </div>
</div></section>"""
    cards = card_grid([
        (DUNNS_IMG, DUNNS_ALT, "Dunn's River Falls", "Jamaica's iconic waterfall climb.", "dunns-river-falls-tour.html", "Waterfall"),
        (MARTHA_IMG, MARTHA_ALT, "Martha Brae", "Tranquil bamboo river rafting.", "martha-brae-river-rafting.html", "Rafting"),
        (BLUE_HOLE_IMG, BLUE_HOLE_ALT, "Blue Hole", "Rainforest pools and waterfalls.", "blue-hole-adventure.html", "Adventure"),
        (BEACH_IMG, BEACH_ALT, "Beach Escape", "Relaxed north-coast beach day.", "beach-escape-excursion.html", "Beach"),
    ])
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Falmouth Shore Excursions</h2>
  <p class="text-gray-600 leading-relaxed text-sm">Operators meet at <strong>Historic Falmouth Pier</strong> and plan returns with buffer before all aboard on your Caribbean cruise.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
{comparison_section(comparison_rows())}
{rankings}
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Popular Excursion Guides</h2>
  {cards}
  <div class="mt-12 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_port_guide() -> str:
    snap = snapshot_default(activity_level="Low at terminal; moderate on tours", popular="Pier pickups, tour departures, historic town walking")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Cruise ships <strong>dock at Historic Falmouth Pier</strong> in Trelawny parish on Jamaica's north coast — a typical <strong>6–10 hour</strong> port call.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Falmouth Cruise Port Location</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_ARRIVAL_IMG}" alt="{PORT_ARRIVAL_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Dock Port</h3><p class="text-gray-600">Ships tie up at the pier — you walk off directly without tender boats. The port area has shops, facilities and tour pickup zones.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Tour Pickups</h3><p class="text-gray-600">Shore excursion operators meet inside or immediately outside the cruise terminal. Most tours depart within 30 minutes of gangway opening.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Walking Falmouth</h3><p class="text-gray-600">Historic Falmouth town is walkable from the pier — Georgian architecture, local shops and the waterfront. Organised tours reach Dunn's River Falls, Martha Brae and beaches.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Practical Port Day Info</h2>
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Distance to Dunn's River Falls</strong><p class="mt-2 text-gray-600">~23 miles / <strong>45 min</strong> east to Ocho Rios.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Distance to Martha Brae</strong><p class="mt-2 text-gray-600">~20–30 min by road from Falmouth pier.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Distance to Blue Hole</strong><p class="mt-2 text-gray-600">~45 min east into St. Mary parish hills.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Taxis</strong><p class="mt-2 text-gray-600">Official taxis at the port — agree fare before departing. Organised excursions include transport.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Jamaican dollars (JMD). <strong>USD</strong> widely accepted near port.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Return Timing</strong><p class="mt-2 text-gray-600">Allow <strong>60–90 minutes</strong> before all aboard for traffic buffer.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Weather</strong><p class="mt-2 text-gray-600">Warm and humid year-round. Lightweight clothing, reef-safe sunscreen and water shoes for waterfalls.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Montego Bay Beaches</strong><p class="mt-2 text-gray-600">~30 min west — popular beach club excursions.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Short Port Day?</strong><p class="mt-2 text-gray-600">Martha Brae rafting (4 hrs) or walk historic Falmouth town.</p></div>
  </div>
  <p class="text-center mt-8"><a href="one-day-in-falmouth-from-a-cruise-ship.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a> · <a href="best-falmouth-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">Compare excursions →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_one_day() -> str:
    snap = snapshot_default(best_for="Morning waterfall or rafting + afternoon beach if time allows")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 text-sm">Sample timeline for a <strong>6–10 hour</strong> Falmouth port call. Adjust for your ship's actual gangway and all-aboard times.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Falmouth Port Day</h2>
  <ol class="space-y-4 text-sm">
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Walk off the ship</strong><p class="text-gray-600 mt-1">Dock directly at Historic Falmouth Pier — no tender required.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">08:30</span><div><strong>Meet excursion</strong><p class="text-gray-600 mt-1">Depart for Dunn's River Falls, Martha Brae or Blue Hole — morning starts beat afternoon rain.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">12:00</span><div><strong>Main activity peak</strong><p class="text-gray-600 mt-1">Waterfall climb, bamboo rafting or Blue Hole swimming depending on your tour.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">14:30</span><div><strong>Return inland</strong><p class="text-gray-600 mt-1">Transport back toward Falmouth with operator-managed timing.</p></div></li>
    <li class="flex gap-4 bg-white rounded-2xl p-5 border border-pr-100"><span class="font-bold text-ocean-600 shrink-0">16:00</span><div><strong>Back aboard</strong><p class="text-gray-600 mt-1">Allow margin before published all-aboard — shore excursions build this buffer in.</p></div></li>
  </ol>
  <div class="mt-8 bg-white rounded-2xl p-6 border border-pr-100">
    <h3 class="font-display font-bold text-lg mb-3">Suggested Excursions</h3>
    <ul class="space-y-2 text-sm text-gray-600">
      <li><a href="dunns-river-falls-and-area-highlights.html" class="text-ocean-600 font-medium">Dunn's River Falls and Area Highlights</a> — best first-timer combo</li>
      <li><a href="martha-brae-river-rafting.html" class="text-ocean-600 font-medium">Martha Brae River Rafting</a> — relaxed 4-hour river experience</li>
      <li><a href="beach-escape-excursion.html" class="text-ocean-600 font-medium">Beach Escape Excursion</a> — easy Caribbean beach day</li>
    </ul>
  </div>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_dunns_guide() -> str:
    snap = snapshot_default(best_for="Waterfall climbs and Ocho Rios sightseeing", popular="Dunn's River Falls, human-chain climbs, terraced cascades")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6"><strong>Dunn's River Falls</strong> is Jamaica's most visited natural attraction — a 600-foot terraced waterfall near Ocho Rios that cruise passengers climb in a human chain led by expert guides. From Falmouth, the drive is approximately <strong>23 miles / 45 minutes east</strong>.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Water shoes essential</strong> — available for rent at the falls.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Moderate fitness</strong> — climbing is optional; viewing platforms available.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Return-to-ship</strong> — tours build all-aboard buffer into timing.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{DUNNS_IMG}" alt="{DUNNS_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold mb-6">Dunn's River Falls Tours from Falmouth</h2>
  <ul class="space-y-3 text-sm text-gray-600">
    <li><a href="dunns-river-falls-tour.html" class="text-ocean-600 font-medium">Dunn's River Falls Tour</a> — focused 3.5-hour waterfall climb</li>
    <li><a href="dunns-river-falls-and-area-highlights.html" class="text-ocean-600 font-medium">Dunn's River Falls and Area Highlights</a> — small-group falls plus Ocho Rios</li>
  </ul>
  <div class="mt-10">{internal_links([("falmouth-port-guide.html", "Port Guide")])}</div>
</div></section>"""


def content_martha_guide() -> str:
    snap = snapshot_default(best_for="Peaceful river rafting and couples", popular="Bamboo rafts, Martha Brae, tranquil floats")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">The <strong>Martha Brae River</strong> near Falmouth offers one of Jamaica's most serene experiences — a 30-foot bamboo raft poled by a skilled raftsman through tropical scenery. The rafting village is about <strong>20–30 minutes</strong> from the Falmouth cruise port.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Easy activity level</strong> — no climbing or strenuous effort required.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>~3-mile float</strong> — approximately one hour on the water.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Great for couples</strong> — romantic and photogenic.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{MARTHA_IMG}" alt="{MARTHA_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold mb-6">Martha Brae Rafting from Falmouth</h2>
  <p class="text-sm text-gray-600 mb-4"><a href="martha-brae-river-rafting.html" class="text-ocean-600 font-medium">Martha Brae River Rafting</a> — 4-hour excursion with easy activity level, ideal for relaxed port days.</p>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_bluehole_guide() -> str:
    snap = snapshot_default(best_for="Rainforest swimming and adventure", popular="Blue Hole pools, cliff jumping, St. Mary rainforest")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">The <strong>Blue Hole</strong> (Island Gully Falls area) in St. Mary parish is an unspoiled rainforest destination with turquoise pools, waterfalls and cliff-jumping spots. About <strong>45 minutes</strong> from Falmouth, it offers a more adventurous alternative to crowded tourist sites.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Swimming shoes recommended</strong> — rocky pool bottoms.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Lunch included</strong> on the organised Blue Hole Adventure tour.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>6-hour excursion</strong> — fits full port days comfortably.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BLUE_HOLE_IMG}" alt="{BLUE_HOLE_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <p class="text-sm text-gray-600"><a href="blue-hole-adventure.html" class="text-ocean-600 font-medium">Blue Hole Adventure</a> — rainforest pools, lunch and Ocho Rios shopping from Falmouth.</p>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_safety() -> str:
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Falmouth is one of Jamaica's primary cruise ports with a well-developed shore excursion infrastructure. For cruise passengers, <strong>organised excursions</strong> with return-to-ship guarantees remain the safest and most reliable way to explore beyond the pier.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Book through reputable operators with verified reviews.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Stay with your tour group — do not accept unlicensed transport offers.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>The Historic Falmouth pier area is monitored during cruise ship days.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Keep valuables secure and use hotel-ship safes for passports when possible.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{SAFETY_IMG}" alt="{SAFETY_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_without_excursion() -> str:
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4">
  <p class="text-gray-600 leading-relaxed mb-6">Yes — you can explore Falmouth without booking an organised shore excursion. The <strong>historic town</strong> is walkable directly from the pier, with Georgian architecture, local craft shops and waterfront views.</p>
  <h2 class="text-2xl font-display font-bold mb-4">What You Can Do Independently</h2>
  <ul class="space-y-3 text-sm text-gray-600 mb-8">
    <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Walk historic Falmouth</strong> — one of the Caribbean's best-preserved Georgian towns.</li>
    <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Port shopping</strong> — duty-free and souvenir shops at the cruise terminal.</li>
    <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Official taxis</strong> — negotiate fares for short trips; agree price before departing.</li>
  </ul>
  <h2 class="text-2xl font-display font-bold mb-4">When an Excursion Makes Sense</h2>
  <p class="text-gray-600 text-sm mb-6">Dunn's River Falls, Blue Hole, Martha Brae and north-coast beaches require transport and local knowledge. Organised excursions handle timing, return-to-ship guarantees and guide expertise — especially important on a port day with a fixed all-aboard deadline.</p>
  <div>{internal_links([("falmouth-port-guide.html", "Port Guide")])}</div>
</div></section>"""


def content_beaches() -> str:
    snap = snapshot_default(best_for="Beach clubs and relaxed Caribbean port days", popular="Montego Bay beaches, Bamboo Beach Club, Doctor's Cave")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">The best beaches near Falmouth are along Jamaica's north coast — <strong>Montego Bay</strong> beaches sit about <strong>30 minutes west</strong>, while eastern beaches near Ocho Rios are about <strong>45 minutes</strong> from the pier.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Beach Escape Excursion</strong> — organised beach day with facilities and return timing.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Bamboo Beach Club</strong> — popular with river tubing combo tours.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Doctor's Cave Beach</strong> — classic Montego Bay swimming beach.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <p class="text-sm text-gray-600"><a href="beach-escape-excursion.html" class="text-ocean-600 font-medium">Beach Escape Excursion</a> from Falmouth — 5.5 hours, easy activity, family-friendly.</p>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_rum_guide() -> str:
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Jamaica's rum heritage runs deep — from historic great houses like <strong>Rose Hall</strong> to working distilleries such as <strong>Hampden Estate</strong>, where rum has been produced for over 260 years. Cultural shore excursions from Falmouth combine tastings, history and countryside scenery.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><a href="rum-and-culture-experience.html" class="text-ocean-600 font-medium">Rum and Culture Experience</a> — Hampden Estate distillery tour and tasting.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><a href="jamaica-highlights-tour.html" class="text-ocean-600 font-medium">Jamaica Highlights Tour</a> — Rose Hall Great House and Montego Bay.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><a href="jamaican-countryside-sightseeing-with-lunch.html" class="text-ocean-600 font-medium">Countryside Sightseeing</a> — jerk lunch and local culture.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{RUM_IMG}" alt="{RUM_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def all_guide_content() -> dict[str, str]:
    return {
        "home.html": content_home(),
        "best-falmouth-shore-excursions.html": content_best_excursions(),
        "falmouth-port-guide.html": content_port_guide(),
        "one-day-in-falmouth-from-a-cruise-ship.html": content_one_day(),
        "dunns-river-falls-guide.html": content_dunns_guide(),
        "martha-brae-river-rafting-guide.html": content_martha_guide(),
        "blue-hole-jamaica-guide.html": content_bluehole_guide(),
        "is-falmouth-safe-for-cruise-passengers.html": content_safety(),
        "can-you-explore-falmouth-without-an-excursion.html": content_without_excursion(),
        "best-beaches-near-falmouth-jamaica.html": content_beaches(),
        "jamaican-rum-and-culture-guide.html": content_rum_guide(),
    }
