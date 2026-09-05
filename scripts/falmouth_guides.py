"""Guide and home page content for Falmouth Shore Excursion World 2.0."""
from falmouth_config import (
    BEACH_ALT,
    BEACH_IMG,
    BEST_ALT,
    BEST_IMG,
    BLUE_HOLE_ALT,
    BLUE_HOLE_IMG,
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
from falmouth_helpers import card_grid, comparison_section, href, internal_links, snapshot_default
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
            slug, "See details",
        ))
    return card_grid(cards)


def content_home() -> str:
    best_cards = card_grid([
        (MARTHA_IMG, MARTHA_ALT, "Martha Brae Rafting", "Peaceful bamboo rafting — one of the closest signature experiences to Falmouth.", "martha-brae-river-rafting", "Explore rafting"),
        (BEACH_IMG, BEACH_ALT, "Beach Escape", "White sand, turquoise water and a relaxed Caribbean beach day.", "beach-escape-excursion", "Explore beaches"),
        (DUNNS_IMG, DUNNS_ALT, "Dunn's River Falls", "Climb Jamaica's iconic terraced waterfall near Ocho Rios — longer road time.", "dunns-river-falls-tour", "See waterfall tour"),
        (BLUE_HOLE_IMG, BLUE_HOLE_ALT, "Blue Hole Adventure", "Rainforest pools and waterfalls in the hills — a longer attraction day.", "blue-hole-adventure", "See details"),
    ])
    featured = _featured_cards()
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <div class="section-label mx-auto">Best Excursions</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Best Falmouth Shore Excursions</h2>
    <p class="text-gray-600 text-sm max-w-2xl mx-auto">Plan around your ship's actual shore time — Martha Brae rafting, north-coast beaches, Dunn's River Falls and Blue Hole options from Falmouth, Jamaica.</p>
  </div>
  {best_cards}
  <p class="text-center mt-8"><a href="{href('best-falmouth-shore-excursions')}" class="text-ocean-600 font-semibold text-sm">See full comparison →</a></p>
</div></section>
<section class="pt-4 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Falmouth Jamaica Cruise Port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Passengers<br/><span class="text-ocean-600">Plan From Falmouth</span></h2>
    <p class="text-gray-600 leading-relaxed mb-5">Falmouth is a <strong>dock port</strong> on Jamaica's north coast. From Historic Falmouth Pier you can plan nearby river rafting, Montego Bay-direction beaches, or longer days toward Ocho Rios attractions. Jamaican dollars (JMD) are official; <strong>USD</strong> is widely accepted near the cruise port. Usable shore time depends on each ship call.</p>
    <div class="flex flex-wrap gap-3">
      <a href="{href('falmouth-port-guide')}" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port Guide</a>
      <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-semibold text-sm self-center">Best beaches →</a>
    </div>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Featured Planning Pages</h2>
  <p class="text-gray-600 text-sm mt-3 max-w-xl mx-auto">Editorial guides and excursion pages for cruise passengers researching Falmouth.</p></div>
  {featured}
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-10">Top Things To Do From Falmouth</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Martha Brae Rafting</h3><p class="text-gray-600 mb-3">Traditional bamboo rafting on a tranquil river — often among the closest signature options to the pier.</p><a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600 font-semibold">Martha Brae guide →</a></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Best Beaches</h3><p class="text-gray-600 mb-3">Montego Bay-direction beaches and organised beach escapes for a calmer Caribbean port day.</p><a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-semibold">Beach guide →</a></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Dunn's River Falls</h3><p class="text-gray-600 mb-3">Climb the famous terraced waterfall near Ocho Rios — plan realistic road time from Falmouth.</p><a href="{href('dunns-river-falls-guide')}" class="text-ocean-600 font-semibold">Falls guide →</a></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Blue Hole</h3><p class="text-gray-600 mb-3">Swim in rainforest pools farther east — a longer attraction day, not a pier walk.</p><a href="{href('blue-hole-jamaica-guide')}" class="text-ocean-600 font-semibold">Blue Hole guide →</a></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Private Driver</h3><p class="text-gray-600 mb-3">Flexible full-day touring when your group wants to set its own pace.</p><a href="{href('private-driver-guide-full-day')}" class="text-ocean-600 font-semibold">Private touring →</a></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Rum &amp; Culture</h3><p class="text-gray-600 mb-3">Hampden Estate distillery context and heritage sightseeing toward Montego Bay.</p><a href="{href('jamaican-rum-and-culture-guide')}" class="text-ocean-600 font-semibold">Culture guide →</a></div>
  </div>
</div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Martha Brae River Rafting</h2>
    <p class="text-gray-600 leading-relaxed mb-4"><strong>Martha Brae River</strong> bamboo rafting is one of Jamaica's most peaceful experiences — glide along calm waters on a hand-poled raft. Existing site material places the rafting area about <strong>20–30 minutes</strong> from Falmouth by road, making it a strong short-to-mid port-day candidate.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Read the <a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600 font-medium">Martha Brae guide</a>, then <a href="{href('martha-brae-river-rafting')}" class="text-ocean-600 font-medium">explore the rafting option</a> for cruise-day logistics.</p>
    <a href="{href('martha-brae-river-rafting')}" class="text-ocean-600 font-semibold text-sm">Explore Martha Brae →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{MARTHA_IMG}" alt="{MARTHA_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Beach Experiences</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Falmouth itself is not primarily a walk-off beach port. Most beach days involve travelling west toward the <strong>Montego Bay</strong> coastline (often described as around <strong>30 minutes</strong> in existing site material) or booking an organised beach escape with facilities and return planning.</p>
    <p class="text-gray-600 leading-relaxed mb-5">Start with <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-medium">best beaches near Falmouth</a> and the <a href="{href('beach-escape-excursion')}" class="text-ocean-600 font-medium">Beach Escape</a> page.</p>
    <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-semibold text-sm">Beach guide →</a>
  </div>
</div></div></section>
<section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Dunn's River Falls</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Dunn's River Falls is Jamaica's signature climb — a terraced waterfall near <strong>Ocho Rios</strong>. Existing material places it about <strong>23 miles / roughly 45 minutes east</strong> of Falmouth. It is a longer-distance choice compared with Martha Brae.</p>
    <p class="text-gray-600 leading-relaxed mb-5">See the <a href="{href('dunns-river-falls-guide')}" class="text-ocean-600 font-medium">Dunn's River Falls guide</a> and related tour pages for cruise-day practicality.</p>
    <a href="{href('dunns-river-falls-tour')}" class="text-ocean-600 font-semibold text-sm">See Dunn's River tour →</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{DUNNS_IMG}" alt="{DUNNS_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
{comparison_section(comparison_rows())}
{home_faq_section()}
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Falmouth Port Day</h2>
  <p class="text-white/85 text-sm mb-6">Compare excursions, read the Falmouth port guide and build a realistic Jamaica itinerary before you dock.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="{href('best-falmouth-shore-excursions')}" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Compare Excursions</a>
    <a href="{href('falmouth-port-guide')}" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
  </div>
</div></section>"""


def home_faq_section() -> str:
    return f"""<section class="py-16 bg-white"><div class="max-w-3xl mx-auto px-4">
  <h2 class="text-3xl font-display font-bold text-gray-900 text-center mb-8">Falmouth Shore Excursions FAQ</h2>
  <div class="space-y-4">
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Falmouth a dock or tender port?</summary>
      <p class="mt-4 text-sm text-gray-500">Falmouth is a <strong>dock port</strong> — ships tie up at Historic Falmouth Pier and you walk off directly. No tender boats required.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far is Martha Brae from Falmouth?</summary>
      <p class="mt-4 text-sm text-gray-500">Existing planning material places Martha Brae about <strong>20–30 minutes</strong> by road from the Falmouth cruise port — closer than Dunn's River or Blue Hole.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far is Dunn's River Falls from Falmouth?</summary>
      <p class="mt-4 text-sm text-gray-500">Dunn's River Falls near Ocho Rios is approximately <strong>23 miles / about 45 minutes</strong> east of the Falmouth cruise port by road. Confirm live traffic on the day.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Falmouth?</summary>
      <p class="mt-4 text-sm text-gray-500">Many Falmouth calls are often described in the <strong>6–10 hour</strong> range, but usable shore time depends on your ship. Always use your daily programme.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What currency is used in Jamaica?</summary>
      <p class="mt-4 text-sm text-gray-500">Jamaican dollars (JMD) are official. US dollars are widely accepted near the cruise port — carry small bills for tips and souvenirs.</p></details>
    <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Falmouth safe for shore excursions?</summary>
      <p class="mt-4 text-sm text-gray-500">Organised excursions with reputable operators are a common approach. See our <a href="{href('is-falmouth-safe-for-cruise-passengers')}" class="text-ocean-600">safety guide</a> and verify operator return policies yourself.</p></details>
  </div>
  <p class="text-center mt-8"><a href="{href('falmouth-shore-excursions-faq')}" class="text-ocean-600 font-semibold text-sm">Full FAQ →</a> · <a href="{href('falmouth-port-guide')}" class="text-ocean-600 font-semibold text-sm">Port guide →</a></p>
</div></section>"""


def home_faq_data() -> list[tuple[str, str]]:
    return [
        ("Is Falmouth Jamaica a dock port for cruise ships?", "Yes — ships dock at Historic Falmouth Pier and passengers walk off directly."),
        ("How far is Martha Brae River from Falmouth?", "Existing site material places Martha Brae about 20–30 minutes by road from the Falmouth cruise port."),
        ("How far is Dunn's River Falls from the Falmouth cruise port?", "Approximately 23 miles / about 45 minutes east to the Ocho Rios area — confirm live traffic."),
        ("How long do cruise ships stay in Falmouth Jamaica?", "Many calls are often around 6–10 hours, but always confirm your ship’s times."),
        ("What currency is used in Jamaica?", "Jamaican dollars (JMD); US dollars are widely accepted near the port."),
        ("What is a strong Falmouth excursion for a shorter call?", "Martha Brae rafting or a carefully timed beach day are often more practical than longer Ocho Rios attraction days."),
        ("Is Falmouth safe for cruise passengers on excursions?", "Organised shore excursions with reputable operators are a common approach; verify return policies and meeting points yourself."),
    ]


def content_best_excursions() -> str:
    snap = snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    rankings = f"""<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Excursions by Traveller Type</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Families</h3><p class="text-gray-600 mb-3">Beach Escape, Martha Brae rafting and countryside tours often suit mixed ages.</p><a href="{href('beach-escape-excursion')}" class="text-ocean-600 font-semibold">Compare beach options →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Adventure Seekers</h3><p class="text-gray-600 mb-3">Blue Hole, river tubing and Dunn's River Falls climbs — plan longer road time.</p><a href="{href('blue-hole-adventure')}" class="text-ocean-600 font-semibold">Explore Blue Hole →</a></div>
    <div class="bg-sand-50 rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">First Timers</h3><p class="text-gray-600 mb-3">Dunn's River Falls and Area Highlights for Jamaica's iconic waterfall experience.</p><a href="{href('dunns-river-falls-guide')}" class="text-ocean-600 font-semibold">See Dunn's River guide →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Couples</h3><p class="text-gray-600 mb-3">Martha Brae rafting and Jamaica Highlights heritage touring.</p><a href="{href('martha-brae-river-rafting')}" class="text-ocean-600 font-semibold">Explore Martha Brae →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Culture Lovers</h3><p class="text-gray-600 mb-3">Countryside sightseeing, rum distillery and Rose Hall heritage context.</p><a href="{href('rum-and-culture-experience')}" class="text-ocean-600 font-semibold">Explore rum &amp; culture →</a></div>
    <div class="bg-ocean-50 rounded-3xl p-6 border border-ocean-100"><h3 class="font-display font-bold text-lg mb-2">Private Groups</h3><p class="text-gray-600 mb-3">Full-day private driver/guide with custom itinerary flexibility.</p><a href="{href('private-driver-guide-full-day')}" class="text-ocean-600 font-semibold">Explore private touring →</a></div>
  </div>
</div></section>"""
    cards = card_grid([
        (MARTHA_IMG, MARTHA_ALT, "Martha Brae", "Tranquil bamboo river rafting near Falmouth.", "martha-brae-river-rafting", "Explore"),
        (BEACH_IMG, BEACH_ALT, "Beach Escape", "Relaxed north-coast beach day.", "beach-escape-excursion", "Explore"),
        (DUNNS_IMG, DUNNS_ALT, "Dunn's River Falls", "Jamaica's iconic waterfall climb.", "dunns-river-falls-tour", "Explore"),
        (BLUE_HOLE_IMG, BLUE_HOLE_ALT, "Blue Hole", "Rainforest pools and waterfalls.", "blue-hole-adventure", "Explore"),
    ])
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Falmouth Shore Excursions</h2>
  <p class="text-gray-600 leading-relaxed text-sm">Compare the excursion themes actually covered on this site. Operators typically meet near <strong>Historic Falmouth Pier</strong>. This is an editorial comparison — we do not take bookings here.</p>
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
    snap = snapshot_default(
        activity_level="Low at terminal; moderate on tours",
        popular="Pier pickups, tour departures, historic town walking",
        return_ship="Build your own buffer; confirm with operators and your ship",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Cruise ships <strong>dock at Historic Falmouth Pier</strong> in Trelawny parish on Jamaica's north coast. Many calls are often around <strong>6–10 hours</strong>, but usable shore time depends on your ship's programme.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Falmouth Cruise Port Location</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_ARRIVAL_IMG}" alt="{PORT_ARRIVAL_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-3 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Dock Port</h3><p class="text-gray-600">Ships tie up at the pier — you walk off directly without tender boats. The port area typically has shops, facilities and tour pickup zones.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Tour Pickups</h3><p class="text-gray-600">Shore excursion operators usually meet inside or immediately outside the cruise terminal. Confirm your exact meeting instructions before travel.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100"><h3 class="font-display font-bold text-lg mb-2">Walking Falmouth</h3><p class="text-gray-600">Historic Falmouth town is walkable from the pier — Georgian architecture, local shops and the waterfront. Longer attractions require transport.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-4">Distances and Port-Day Practicality</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-8">Travel times below come from existing researched site material and are planning estimates only. Traffic, weather and ship schedules vary — reconfirm on the day.</p>
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Martha Brae</strong><p class="mt-2 text-gray-600">Often about <strong>20–30 minutes</strong> by road from Falmouth pier — among the closer signature options.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Montego Bay beaches</strong><p class="mt-2 text-gray-600">Often about <strong>30 minutes west</strong> — common beach-club direction, not a Falmouth walk-off beach.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Dunn's River Falls</strong><p class="mt-2 text-gray-600">About <strong>23 miles / ~45 min</strong> east toward Ocho Rios — longer-distance waterfall day.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Blue Hole</strong><p class="mt-2 text-gray-600">Often about <strong>45 minutes</strong> east into St. Mary parish hills — not adjacent to the pier.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Taxis</strong><p class="mt-2 text-gray-600">Official taxis operate at the port — agree the fare before departing. We do not invent fare tables here.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Jamaican dollars (JMD). <strong>USD</strong> widely accepted near port.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Return planning</strong><p class="mt-2 text-gray-600">Build a conservative buffer before all aboard. Do not treat marketing “guarantees” as automatic.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Independent vs organised</strong><p class="mt-2 text-gray-600">Town walking can work independently; waterfalls, Blue Hole and many beaches need transport and timing discipline.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Shorter calls</strong><p class="mt-2 text-gray-600">Prefer Martha Brae, a carefully timed beach day, private touring with firm return rules, or stay near the pier.</p></div>
  </div>
  <p class="text-center mt-8"><a href="{href('one-day-in-falmouth-from-a-cruise-ship')}" class="text-ocean-600 font-semibold text-sm">One-day scenarios →</a> · <a href="{href('best-falmouth-shore-excursions')}" class="text-ocean-600 font-semibold text-sm">Compare excursions →</a> · <a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600 font-semibold text-sm">Martha Brae →</a> · <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-semibold text-sm">Beaches →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>"""


def content_one_day() -> str:
    snap = snapshot_default(best_for="Scenarios matched to shore time — not a fixed timetable")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 text-sm">Usable shore time depends on <strong>your ship’s call</strong>. The scenarios below are planning patterns, not a promise that every ship stays long enough for every option.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4 space-y-8">
  <div class="bg-white rounded-2xl p-6 border border-pr-100">
    <h2 class="text-xl font-display font-bold mb-3">Easy Falmouth + nearby day</h2>
    <p class="text-sm text-gray-600 mb-3">Walk off at Historic Falmouth Pier, explore the Georgian town and waterfront, then keep a generous return buffer. Best when you want a low-stress call without long road time.</p>
    <a href="{href('can-you-explore-falmouth-without-an-excursion')}" class="text-ocean-600 font-semibold text-sm">Independent Falmouth tips →</a>
  </div>
  <div class="bg-white rounded-2xl p-6 border border-pr-100">
    <h2 class="text-xl font-display font-bold mb-3">Martha Brae day</h2>
    <p class="text-sm text-gray-600 mb-3">A strong mid-length pattern: pier pickup, bamboo rafting on the Martha Brae, and return planning. Often more practical than Ocho Rios-distance attractions on tighter calls.</p>
    <a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600 font-semibold text-sm">Martha Brae guide →</a> · <a href="{href('martha-brae-river-rafting')}" class="text-ocean-600 font-semibold text-sm">Explore rafting option →</a>
  </div>
  <div class="bg-white rounded-2xl p-6 border border-pr-100">
    <h2 class="text-xl font-display font-bold mb-3">Beach day</h2>
    <p class="text-sm text-gray-600 mb-3">Travel toward Montego Bay-direction beaches or book an organised beach escape with facilities. Falmouth is not mainly a walk-off beach port.</p>
    <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-semibold text-sm">Best beaches →</a> · <a href="{href('beach-escape-excursion')}" class="text-ocean-600 font-semibold text-sm">Beach Escape →</a>
  </div>
  <div class="bg-white rounded-2xl p-6 border border-pr-100">
    <h2 class="text-xl font-display font-bold mb-3">Longer attraction day</h2>
    <p class="text-sm text-gray-600 mb-3">Dunn's River Falls or Blue Hole need more road time. Choose these when your published shore window is comfortably long and you still keep a conservative return buffer.</p>
    <a href="{href('dunns-river-falls-guide')}" class="text-ocean-600 font-semibold text-sm">Dunn's guide →</a> · <a href="{href('blue-hole-jamaica-guide')}" class="text-ocean-600 font-semibold text-sm">Blue Hole guide →</a>
  </div>
  <div class="mt-4">{internal_links()}</div>
</div></section>"""


def content_dunns_guide() -> str:
    snap = snapshot_default(
        best_for="Waterfall climbs and Ocho Rios sightseeing",
        popular="Dunn's River Falls, human-chain climbs, terraced cascades",
        return_ship="Longer road time — confirm buffer with operator",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6"><strong>Dunn's River Falls</strong> is Jamaica's most visited natural attraction — a terraced waterfall near Ocho Rios that cruise passengers climb in a guided human chain. From Falmouth, existing material places the drive at approximately <strong>23 miles / about 45 minutes east</strong>. It is <strong>not adjacent</strong> to the Falmouth pier.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Water shoes</strong> — often essential; rentals may be available at the falls.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Moderate fitness</strong> — climbing is typically optional; viewing platforms exist.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Cruise practicality</strong> — choose this when shore time comfortably covers road + activity + return buffer.</li>
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
    <li><a href="{href('dunns-river-falls-tour')}" class="text-ocean-600 font-medium">Dunn's River Falls Tour</a> — focused waterfall climb format</li>
    <li><a href="{href('dunns-river-falls-and-area-highlights')}" class="text-ocean-600 font-medium">Dunn's River Falls and Area Highlights</a> — falls plus Ocho Rios sightseeing</li>
  </ul>
  <div class="mt-10">{internal_links([("martha-brae-river-rafting-guide", "Martha Brae (closer alternative)")])}</div>
</div></section>"""


def content_martha_guide() -> str:
    snap = snapshot_default(
        best_for="Peaceful river rafting and couples",
        popular="Bamboo rafts, Martha Brae, tranquil floats",
        activity_level="Easy",
        return_ship="Often more practical on mid-length calls than Ocho Rios-distance days",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">The <strong>Martha Brae River</strong> near Falmouth offers one of Jamaica's most serene cruise-day experiences: a bamboo raft poled by a skilled raftsman through tropical scenery. Existing planning material places the rafting village about <strong>20–30 minutes</strong> from the Falmouth cruise port — closer than Dunn's River Falls or Blue Hole.</p>
    <p class="text-gray-600 leading-relaxed mb-6">On the water, expect a calm float rather than white-water adventure. Rafts are typically shared by a small party; raftsmen often share local stories along the way. Activity level is generally easy — no waterfall climbing required.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Easy activity level</strong> — suits many couples, families and first-time visitors.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Typical float character</strong> — a scenic river stretch often described around an hour on the water within a longer excursion window.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>What to take</strong> — light clothing, sunscreen, a dry bag for phones, and cash for tips if you choose to tip.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Weather</strong> — rain can change river character; confirm operator advice on the day.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{MARTHA_IMG}" alt="{MARTHA_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4 space-y-6">
  <h2 class="text-2xl font-display font-bold">Martha Brae vs beach day vs longer Jamaica excursions</h2>
  <p class="text-sm text-gray-600">Choose <strong>Martha Brae</strong> for a scenic, low-exertion signature experience relatively close to Falmouth. Choose a <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 font-medium">beach day</a> for swimming and sand time (usually involving Montego Bay-direction travel). Choose <a href="{href('dunns-river-falls-guide')}" class="text-ocean-600 font-medium">Dunn's River</a> or <a href="{href('blue-hole-jamaica-guide')}" class="text-ocean-600 font-medium">Blue Hole</a> only when shore time comfortably covers longer road legs.</p>
  <h2 class="text-2xl font-display font-bold">Return-to-ship planning</h2>
  <p class="text-sm text-gray-600">Ask any operator how they time the return against your all-aboard call. This site does not operate tours and does not offer a return guarantee. Keep your own conservative buffer.</p>
  <p class="text-sm text-gray-600"><a href="{href('martha-brae-river-rafting')}" class="text-ocean-600 font-medium">Explore the rafting option</a> for excursion-shaped logistics detail, or return to the <a href="{href('best-falmouth-shore-excursions')}" class="text-ocean-600 font-medium">excursions hub</a>.</p>
  <div class="mt-10">{internal_links([("martha-brae-river-rafting", "Martha Brae excursion page")])}</div>
</div></section>"""


def content_bluehole_guide() -> str:
    snap = snapshot_default(
        best_for="Rainforest swimming and adventure",
        popular="Blue Hole pools, St. Mary rainforest",
        return_ship="Longer eastern road time — not a short pier trip",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">The <strong>Blue Hole</strong> (Island Gully Falls area) in St. Mary parish is a rainforest destination with turquoise pools and waterfalls. Existing material places it about <strong>45 minutes</strong> from Falmouth — a longer-distance choice, not something adjacent to the pier.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Swimming shoes recommended</strong> — rocky pool bottoms are common.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Confirm inclusions</strong> — some excursion formats advertise lunch or shopping time; verify before travel.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Cruise practicality</strong> — best on longer Falmouth calls with a firm return plan.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BLUE_HOLE_IMG}" alt="{BLUE_HOLE_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <p class="text-sm text-gray-600"><a href="{href('blue-hole-adventure')}" class="text-ocean-600 font-medium">See Blue Hole adventure details</a> — editorial excursion page for cruise passengers researching rainforest pools from Falmouth.</p>
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_safety() -> str:
    snap = snapshot_default()
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Falmouth is one of Jamaica's primary cruise ports with established shore-excursion infrastructure. For cruise passengers, <strong>organised excursions with reputable operators</strong> remain a common way to explore beyond the pier — but you should still verify meeting points, inclusions and return policies yourself.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Prefer operators with clear meeting instructions and transparent return timing.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Stay with your tour group — be cautious with unlicensed transport offers.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>The Historic Falmouth pier area is typically busy and monitored on cruise ship days.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span>Keep valuables secure and follow your cruise line’s port-day guidance.</li>
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
    <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Port shopping</strong> — shops at the cruise terminal area.</li>
    <li class="flex gap-2"><span class="text-ocean-500">✓</span><strong>Official taxis</strong> — negotiate fares for short trips; agree price before departing.</li>
  </ul>
  <h2 class="text-2xl font-display font-bold mb-4">When an Excursion Makes Sense</h2>
  <p class="text-gray-600 text-sm mb-6">Dunn's River Falls, Blue Hole, Martha Brae and north-coast beaches require transport and timing discipline. Organised excursions can simplify logistics — especially with a fixed all-aboard deadline — but you still need to verify return policies. This site does not sell tickets.</p>
  <div>{internal_links([("falmouth-port-guide", "Port Guide")])}</div>
</div></section>"""


def content_beaches() -> str:
    snap = snapshot_default(
        best_for="Beach clubs and relaxed Caribbean port days",
        popular="Montego Bay beaches, Bamboo Beach Club, Doctor's Cave, Beach Escape",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Falmouth is a <strong>dock port</strong>, not primarily a walk-off beach destination. The beaches cruise passengers research most from Falmouth sit along Jamaica's north coast — especially west toward <strong>Montego Bay</strong> (often about <strong>30 minutes</strong> in existing site material) and, for some organised days, farther east toward the Ocho Rios coastline.</p>
    <p class="text-gray-600 leading-relaxed mb-6">This page covers only beaches and beach products already supported in our researched material: the <strong>Beach Escape</strong> excursion format, <strong>Bamboo Beach Club</strong> context, and <strong>Doctor's Cave Beach</strong> as a classic Montego Bay swimming beach. We do not invent beaches solely because they appear in search queries.</p>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{BEACH_IMG}" alt="{BEACH_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Which Beach Option Suits Your Port Day?</h2>
  <div class="grid lg:grid-cols-3 gap-6 text-sm mb-10">
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <h3 class="font-display font-bold text-lg mb-2">Beach Escape excursion</h3>
      <p class="text-gray-600 mb-3">Organised beach day with facilities and cruise-oriented return planning. Best when you want a packaged beach experience rather than DIY taxi logistics.</p>
      <ul class="text-gray-600 space-y-1 mb-4"><li>· Easy activity level</li><li>· Family-friendly framing</li><li>· Strong commercial pathway on this site</li></ul>
      <a href="{href('beach-escape-excursion')}" class="text-ocean-600 font-semibold">Explore Beach Escape →</a>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <h3 class="font-display font-bold text-lg mb-2">Doctor's Cave Beach</h3>
      <p class="text-gray-600 mb-3">Classic Montego Bay swimming beach known for clear water and a club-style setting. Reached by road west of Falmouth — not a pier walk. Useful as a named destination when comparing Montego Bay beach days.</p>
      <ul class="text-gray-600 space-y-1 mb-4"><li>· Strong swimming reputation</li><li>· Facilities typically available at the club</li><li>· Keep return buffer for road time</li></ul>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-pr-100">
      <h3 class="font-display font-bold text-lg mb-2">Bamboo Beach Club</h3>
      <p class="text-gray-600 mb-3">Named in existing Falmouth beach planning as a popular beach-club style stop, sometimes paired with river tubing combo days. Treat facilities and inclusions as operator-specific — confirm before travel.</p>
      <ul class="text-gray-600 space-y-1 mb-4"><li>· Beach-club atmosphere</li><li>· May appear in combo itineraries</li><li>· Not a Falmouth walk-off beach</li></ul>
    </div>
  </div>
  <div class="max-w-3xl mx-auto space-y-6 text-sm text-gray-600">
    <h2 class="text-2xl font-display font-bold text-gray-900">Cruise planning notes</h2>
    <p><strong>Organised vs independent:</strong> Organised beach escapes simplify timing. Independent taxis can work if you agree fares, know the destination, and protect return time — we do not invent fare tables.</p>
    <p><strong>Shorter calls:</strong> Prefer a nearby town day or Martha Brae over a long beach transfer if your ship’s window is tight.</p>
    <p><strong>Non-beach alternative:</strong> If you want a signature Jamaica experience without sand, see the <a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600 font-medium">Martha Brae rafting guide</a>.</p>
    <p><a href="{href('falmouth-port-guide')}" class="text-ocean-600 font-medium">Port guide</a> · <a href="{href('one-day-in-falmouth-from-a-cruise-ship')}" class="text-ocean-600 font-medium">One day scenarios</a> · <a href="{href('best-falmouth-shore-excursions')}" class="text-ocean-600 font-medium">Excursions hub</a></p>
  </div>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links([("beach-escape-excursion", "Beach Escape")])}</div>
</div></section>"""


def content_rum_guide() -> str:
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <p class="text-gray-600 leading-relaxed mb-6">Jamaica's rum heritage runs deep — from historic great houses like <strong>Rose Hall</strong> to working distilleries such as <strong>Hampden Estate</strong>. Cultural shore excursions from Falmouth combine tastings, history and countryside scenery. This page is editorial context only.</p>
    <ul class="space-y-3 mb-6 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><a href="{href('rum-and-culture-experience')}" class="text-ocean-600 font-medium">Rum and Culture Experience</a> — Hampden Estate distillery tour context.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><a href="{href('jamaica-highlights-tour')}" class="text-ocean-600 font-medium">Jamaica Highlights Tour</a> — Rose Hall Great House and Montego Bay framing.</li>
      <li class="flex gap-2"><span class="text-ocean-500">✓</span><a href="{href('jamaican-countryside-sightseeing-with-lunch')}" class="text-ocean-600 font-medium">Countryside Sightseeing</a> — jerk lunch and local culture.</li>
    </ul>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{RUM_IMG}" alt="{RUM_ALT}" width="600" height="450" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
  <div class="mt-10">{internal_links()}</div>
</div></section>"""


def content_faq_page() -> str:
    snap = snapshot_default(best_for="Quick Falmouth cruise planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Falmouth a dock or tender port?</summary>
    <p class="mt-4 text-sm text-gray-500">Dock port — ships tie up at Historic Falmouth Pier and passengers walk off directly.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do ships stay in Falmouth?</summary>
    <p class="mt-4 text-sm text-gray-500">Many calls are often around 6–10 hours, but always confirm gangway and all-aboard times on your ship’s programme.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is a practical shorter-call option?</summary>
    <p class="mt-4 text-sm text-gray-500">Martha Brae rafting, a carefully timed beach day, private touring with firm return rules, or staying near historic Falmouth are usually more practical than long Ocho Rios-distance days.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Beach day or Martha Brae?</summary>
    <p class="mt-4 text-sm text-gray-500">Choose beaches for swimming and sand; choose Martha Brae for a scenic river float closer to Falmouth. See the <a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600">beach guide</a> and <a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600">Martha Brae guide</a>.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Are Dunn's River and Blue Hole near the pier?</summary>
    <p class="mt-4 text-sm text-gray-500">No. Both are longer-distance eastern options. Dunn's River is often about 45 minutes toward Ocho Rios; Blue Hole is similarly a longer attraction day.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Do you take bookings on this site?</summary>
    <p class="mt-4 text-sm text-gray-500">Not in this phase. Falmouth Shore Excursion is an independent editorial planning guide. Verify prices and availability with operators you choose separately.</p></details>
  <details class="faq-item rounded-2xl border border-pr-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What currency should I bring?</summary>
    <p class="mt-4 text-sm text-gray-500">JMD is official; USD is widely accepted near the cruise port. Carry small notes for tips and small purchases.</p></details>
  {internal_links()}
</div></section>"""


def content_about() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">About Falmouth Shore Excursion</h1>
  <p class="text-gray-600 leading-relaxed mb-4">This site is an independent planning guide for cruise passengers calling at Falmouth, Jamaica. We help you compare Martha Brae rafting, north-coast beaches, Dunn's River Falls, Blue Hole days and other shore options against a realistic port day from Historic Falmouth Pier.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We do not operate tours, sell tickets or take payment on this website in this phase. If you book, you book with operators you choose separately. We are not affiliated with any cruise line.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We do not claim a Falmouth office, Jamaican staff desk, local operating fleet or first-hand operator relationships on this site.</p>
  <p class="text-gray-600 leading-relaxed">See our <a href="{href('methodology')}" class="text-ocean-600 underline">methodology</a> and <a href="{href('contact')}" class="text-ocean-600 underline">contact</a> pages.</p>
</section>"""


def content_contact() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Contact</h1>
  <p class="text-gray-600 leading-relaxed mb-4">This site is an independent Falmouth cruise planning guide. We do not take bookings or payments here.</p>
  <p class="text-gray-600 leading-relaxed mb-4">A public inbox for this domain is being prepared. Email routing for <span class="font-medium text-gray-800">hello@falmouthshoreexcursion.com</span> has not yet been verified as live, so please do not rely on that address until routing is confirmed.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Meanwhile, use the planning pages:</p>
  <ul class="list-disc pl-5 text-gray-600 space-y-2 mb-6">
    <li><a href="{href('one-day-in-falmouth-from-a-cruise-ship')}" class="text-ocean-600 underline">One day in Falmouth</a></li>
    <li><a href="{href('best-beaches-near-falmouth-jamaica')}" class="text-ocean-600 underline">Best beaches</a></li>
    <li><a href="{href('martha-brae-river-rafting-guide')}" class="text-ocean-600 underline">Martha Brae guide</a></li>
    <li><a href="{href('falmouth-port-guide')}" class="text-ocean-600 underline">Cruise port guide</a></li>
    <li><a href="{href('best-falmouth-shore-excursions')}" class="text-ocean-600 underline">Best shore excursions</a></li>
  </ul>
  <p class="text-sm text-gray-500 leading-relaxed">EMAIL ROUTING NEEDS MANUAL VERIFICATION. When routing is verified, this page will be updated with a working contact address.</p>
</section>"""


def content_privacy() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Privacy</h1>
  <p class="text-gray-600 leading-relaxed mb-4">Falmouth Shore Excursion is an editorial planning website. In this phase we do not operate an online booking or payment system on this domain.</p>
  <p class="text-gray-600 leading-relaxed mb-4">If you contact us once a verified public email is published, we will use your message only to respond to your enquiry. We do not sell personal information.</p>
  <p class="text-gray-600 leading-relaxed mb-4">This site may use standard hosting and analytics logs typical of websites served through Cloudflare. Those logs can include IP address, user agent and requested URLs.</p>
  <p class="text-gray-600 leading-relaxed">For questions about this policy, use the <a href="{href('contact')}" class="text-ocean-600 underline">contact</a> page once a working inbox is confirmed.</p>
</section>"""


def content_terms() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Terms of use</h1>
  <p class="text-gray-600 leading-relaxed mb-4">Content on Falmouth Shore Excursion is provided for general cruise-planning information only. It is not a booking contract, travel insurance policy or guarantee of shore time.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Operators, cruise lines, beach facilities, transport and weather change. Always verify final details with your cruise line and any operator you choose before travel.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We are not affiliated with cruise lines or third-party marketplaces. We do not take bookings on this site in this phase.</p>
  <p class="text-gray-600 leading-relaxed">To the fullest extent permitted by law, we are not liable for decisions made solely on the basis of this editorial guidance. Plan a conservative return buffer to your ship.</p>
</section>"""


def content_methodology() -> str:
    return f"""<section class="py-16 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h1 class="font-display text-3xl font-bold text-gray-900 mb-4">Methodology</h1>
  <p class="text-gray-600 leading-relaxed mb-4">This site is editorial. Recommendations are independent planning guidance for Falmouth cruise passengers, not paid placements or live inventory.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We do not invent star ratings, review counts, bestsellers or fabricated availability. Operator inclusions, prices, meeting points and timings can change — confirm details before travel.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Where exact taxi fares or admission prices cannot be verified, we avoid inventing numbers. Travel-time claims are drawn from existing researched site material and should be treated as estimates.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Ship schedule pages are deferred in this phase. Confirm arrival, departure and all-aboard times with your cruise line.</p>
  <p class="text-gray-600 leading-relaxed">See <a href="{href('about')}" class="text-ocean-600 underline">About</a> and <a href="{href('contact')}" class="text-ocean-600 underline">Contact</a>.</p>
</section>"""


def content_404() -> str:
    return f"""<section class="py-24 max-w-3xl mx-auto px-4 text-center">
  <h1 class="font-display text-4xl font-bold text-gray-900 mb-4">Page not found</h1>
  <p class="text-gray-600 mb-8">That URL is not part of this Falmouth planning site.</p>
  <div class="flex flex-col sm:flex-row gap-3 justify-center text-sm">
    <a href="/" class="btn-ocean text-white font-semibold px-6 py-3 rounded-full">Home</a>
    <a href="{href('best-beaches-near-falmouth-jamaica')}" class="btn-outline font-semibold px-6 py-3 rounded-full border border-ocean-600 text-ocean-700">Best Beaches</a>
    <a href="{href('best-falmouth-shore-excursions')}" class="btn-outline font-semibold px-6 py-3 rounded-full border border-ocean-600 text-ocean-700">Excursions</a>
  </div>
</section>"""


def faq_page_data() -> list[tuple[str, str]]:
    return [
        ("Is Falmouth a dock or tender port?", "Dock port — ships tie up at Historic Falmouth Pier and passengers walk off directly."),
        ("How long do ships stay in Falmouth?", "Many calls are often around 6–10 hours, but always confirm your ship’s programme."),
        ("What is a practical shorter-call option?", "Martha Brae rafting, a carefully timed beach day, private touring with firm return rules, or staying near historic Falmouth."),
        ("Beach day or Martha Brae?", "Beaches for swimming and sand; Martha Brae for a scenic river float closer to Falmouth."),
        ("Are Dunn's River and Blue Hole near the pier?", "No — both are longer-distance eastern options."),
        ("Do you take bookings on this site?", "Not in this phase — this is an independent editorial planning guide."),
        ("What currency should I bring?", "JMD is official; USD is widely accepted near the cruise port."),
    ]


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
        "falmouth-shore-excursions-faq.html": content_faq_page(),
        "about.html": content_about(),
        "contact.html": content_contact(),
        "privacy.html": content_privacy(),
        "terms.html": content_terms(),
        "methodology.html": content_methodology(),
        "404.html": content_404(),
    }
