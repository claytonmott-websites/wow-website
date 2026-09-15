"""WOW website — home, Why WOW and platform overview."""
from html import escape as e
from layout import AREAS, page, page_hero, route, btn, more, tab, photo, stats, cta_band, ic

R = ""  # top-level pages sit at the site root


def area_tiles(show_tagline=False):
    return '<div class="areas">' + "".join(
        f'<a class="area" href="{R}platform/{a["slug"]}.html"><span class="n">{a["n"]}<span class="dot {a["accent"]}"></span></span>'
        f'<h3>{e(a["name"])}</h3><p>{e(a["tagline"] if show_tagline else a["short"])}</p>{ic("arrow")}</a>'.replace("<svg", '<svg class="arrow"', 1)
        for a in AREAS) + "</div>"


def points(items):
    return '<ul class="points">' + "".join(f'<li><span class="dot"></span><b>{e(t)}</b><p>{e(d)}</p></li>' for t, d in items) + "</ul>"


# ------------------------------------------------------------------ HOME
def home():
    paths = [
        ("Owners & operators", "Earn fuel rebates, see your fleet on screen and turn trips into bankable records.", "who-its-for.html#owners"),
        ("Drivers", "Safer cashless fares, an instant wallet and your own e-hailing platform.", "who-its-for.html#drivers"),
        ("Commuters", "Pay on any phone, ride connected and win prizes on trips you already take.", "who-its-for.html#commuters"),
        ("Associations & co-ops", "Your rules, enforced automatically on every transaction.", "who-its-for.html#associations"),
        ("Brands & sponsors", "Reach 10,7 million daily riders through WOW-Fi and LuckyX.", "who-its-for.html#brands"),
        ("Government", "Verified scholar transport and an integrated public transport system.", "who-its-for.html#government"),
        ("Investors", "Access the data room, including the Eastern Cape Transport Bond.", "investors.html"),
    ]
    path_cards = "".join(f'<a class="card path" href="{h}"><h3>{e(t)}</h3><p>{e(d)}</p>{more("Find out more", h).replace("<a ", "<span ").replace("</a>", "</span>").replace(f' href="{h}"', "")}</a>' for t, d, h in paths)
    path_cards += f'<a class="card path" href="get-involved.html" style="background:var(--red);color:#fff"><h3>Ready to get involved?</h3><p style="color:#fff">Enter the data room, sign in to the WOW portal or find your way in.</p><span class="more" style="color:#fff">Get involved{ic("arrow")}</span></a>'

    body = f"""
<section class="hero" aria-labelledby="hero-title">
  <figure class="hero-media">
    <img src="{R}assets/img/WOW_Photo_Operator-Sunrise.jpg" srcset="{R}assets/img/WOW_Photo_Operator-Sunrise-960.jpg 960w, {R}assets/img/WOW_Photo_Operator-Sunrise.jpg 1672w" sizes="100vw" width="1672" height="941" alt="A public transport operator uses the WOW app on his phone beside his minibus at a fuel forecourt at sunrise, linked to icons for tracking, safety cameras, fuel and the wallet" fetchpriority="high" decoding="async">
  </figure>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <span class="eyebrow">Wealth on Wheels · Eastern Cape</span>
      <h1 class="display" id="hero-title">Crafted and <span class="hl">owned</span> by the public transport industry.</h1>
      <p class="lead">South Africa’s largest collectively owned public transport structure: one wallet, ten focus areas, and a digital platform the industry owns outright.</p>
      <div class="btns">{btn("Explore the platform", "platform.html")}{btn("Why WOW", "why-wow.html", "outline-white", False)}</div>
    </div>
  </div>
</section>

<section class="sec tight" aria-label="WOW in numbers">
  <div class="wrap">{stats([("~67 000", "Public transport operators, organised as one"), ("~105 000", "Vehicles on the network"), ("120 000+", "Scholars transported every school day"), ("~1/3", "Of South Africa’s national fleet")])}</div>
</section>

<section class="sec chalk" aria-labelledby="platform-title">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:16px"><span class="eyebrow">The platform</span><h2 class="h2" id="platform-title">Ten focus areas. <span class="hl">One wallet.</span> One owner.</h2></div>
      <div style="display:grid;gap:16px;justify-items:start"><p class="lead">Every service runs on the same wallet and the same organised industry, so each new capability makes the others stronger.</p>{more("Platform overview", "platform.html")}</div>
    </div>
    {area_tiles()}
  </div>
</section>

<section class="sec" aria-labelledby="why-title">
  <div class="wrap split">
    {photo(R, "WOW_Photo_Agent-At-The-Rank.jpg", "A WOW Agent helps a driver at the rank", "WOW Agents at every rank", "tar")}
    <div style="display:grid;gap:22px;justify-items:start">
      <span class="eyebrow">Why WOW</span>
      <h2 class="h2" id="why-title">Organised from within. <span class="hl">Impossible to copy.</span></h2>
      <p class="lead">Technology alone never worked in this industry. WOW starts with the thing no fintech, bank or corporate could buy or build: the industry itself, formally organised.</p>
      {points([("Adoption solved before deployment", "Collective ownership and stakeholder endorsement across the whole market, before a single device is installed."),
               ("Distribution, legitimacy, mandate", "Every region, association and operator in the province is connected to the co-operative that owns WOW."),
               ("Its own financial rails", "A regulated digital wallet and payment rails, owned rather than rented.")])}
      {more("Why WOW can’t be copied", "why-wow.html")}
    </div>
  </div>
</section>

<section class="sec chalk" aria-labelledby="paths-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Who it’s for</span><h2 class="h2" id="paths-title">Find your way in.</h2></div>
    <div class="grid4">{path_cards}</div>
  </div>
</section>

<section class="sec red-bg siya" aria-labelledby="siya-title">
  {route("#E5463E", 1, 80)}
  <div class="wrap siya-grid">
    <div><h2 class="siya-word" id="siya-title">Siyabangena!</h2><p class="siya-say">see-yah-bah-NGEH-nah · “we’re getting in”</p></div>
    <div style="display:grid;gap:22px;justify-items:start">
      <p>You <i>ngena</i> when you board: a bus, a minibus, a bakkie. Siyabangena is the public transport industry entering the digital economy on its own terms, with confidence and intent. And this time, everyone gets in.</p>
      {btn("What it means", "why-wow.html#siyabangena", "white")}
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="awards-title">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:16px"><span class="eyebrow">Recognition</span><h2 class="h2" id="awards-title">Award-winning, from the first stand.</h2></div>
      <div>{more("All news and press", "news.html")}</div>
    </div>
    <div class="grid2">
      <article class="award"><span class="yr">Africa Tech Festival 2024 · Cape Town</span>{tab("Winner", "red")}<h3>Fintech Innovation of the Year</h3><p>Recognising WOW as a breakthrough financial technology for the African continent.</p></article>
      <article class="award"><span class="yr">42nd Southern African Transport Conference · 2024</span>{tab("Winner", "red")}<h3>Best Exhibition Stand</h3><p>The first time a public transport industry solution has won this award.</p></article>
    </div>
  </div>
</section>
""" + cta_band(R)
    return page(R, "home", "WOW — Wealth on Wheels · Crafted and owned by the public transport industry",
                "WOW is South Africa’s industry-owned digital operating system for the public transport economy: one wallet, ten focus areas, owned by the co-operative.", body)


# ------------------------------------------------------------------ WHY WOW
def why():
    principles = [
        ("A territory larger than England", "The cohesion spans the entire Eastern Cape (buses, minibuses, bakkies, scholar transport, e-hailing and township deliveries), a formal co-operative structure that exists in no other province."),
        ("Adoption solved before deployment", "Every earlier technology attempt in this space died on adoption. WOW starts with collective ownership and endorsement across the entire market, before a single device is deployed."),
        ("Distribution, legitimacy, mandate", "What would be a rank-by-rank sales grind becomes an organised, endorsed and well-communicated province-wide rollout."),
        ("Its own financial rails", "ECTTC owns and operates a regulated digital wallet and payment rails. This is the industry holding financial infrastructure most corporates only rent."),
        ("An economic blueprint", "Industry-owned structures plus advanced technology can bring informal economies into the digital mainstream, in transport and far beyond it."),
        ("A world-class IPTMS", "A clear roadmap to an Integrated Public Transport Management System, owned by the people who operate it."),
    ]
    cards = "".join(f'<article class="card"><h3>{e(t)}</h3><p>{e(d)}</p></article>' for t, d in principles)
    tiers = "".join(f'<li class="tier"><b>{n}</b><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for n, t, d in [
        ("1", "Tertiary co-operative", "ECTTC: one provincial voice, founded in 2014."),
        ("45", "Secondary co-operatives", "Regional structures that aggregate and represent the primaries."),
        ("186", "Primary co-operatives", "Associations and operators, united at the rank and in logical geographic clusters.")])
    body = page_hero(R, "Why WOW", 'The asset others <span class="hl">cannot replicate.</span>',
                     "Our technology creates the capability. The industry-owned co-operative structure is what makes the move from an informal economy to a connected digital economy possible.",
                     [("Why WOW", None)], aside=photo(R, "WOW_Photo_Field-Operations.jpg", "WOW field operations team checking vehicles at the rank", "Organised from within", "tar"))
    body += f"""
<nav class="subnav" aria-label="On this page"><div class="wrap"><ul>
  <li><a href="#structure">The structure</a></li><li><a href="#from-within">Organised from within</a></li><li><a href="#siyabangena">Siyabangena</a></li><li><a href="#evidence">The evidence</a></li>
</ul></div></nav>

<section class="sec" id="structure" aria-labelledby="structure-title">
  <div class="wrap split" style="align-items:start">
    <div style="display:grid;gap:22px">
      <span class="eyebrow">The co-operative structure</span>
      <h2 class="h2" id="structure-title">A remarkable institutional feat, years in the making.</h2>
      <div class="prose"><p>Over years of painstaking groundwork, the Eastern Cape Transport Tertiary Co-operative (ECTTC) has done what no fintech, bank or corporate could buy or build.</p><p>It organised an informal, fragmented, fiercely independent industry into a formal co-operative structure spanning an entire province.</p></div>
    </div>
    <ol class="tiers chalk" style="list-style:none;margin:0;padding:24px;border-radius:var(--r-xl)">{tiers}</ol>
  </div>
  <div class="wrap" style="margin-top:64px">{stats([("~67 000", "Operators represented"), ("~105 000", "Vehicles"), ("~15 000", "E-hailing vehicles"), ("~1/3", "Of the national fleet")])}</div>
</section>

<section class="sec chalk" id="from-within" aria-labelledby="within-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Organised from within</span><h2 class="h2" id="within-title">Built with the industry, not imposed on it.</h2>
      <p class="lead">The public transport economy has long resisted structures imposed from outside. Many technology projects failed because they tried to digitise the industry before understanding how it is organised. ECTTC did the opposite.</p></div>
    <div class="grid3">{cards}</div>
  </div>
</section>

<section class="sec red-bg siya" id="siyabangena" aria-labelledby="siya-title">
  {route("#E5463E", 2, 80)}
  <div class="wrap siya-grid" style="align-items:start">
    <div><span class="eyebrow">The word beneath our logo</span><h2 class="siya-word" id="siya-title" style="margin-top:18px">Siyabangena!</h2><p class="siya-say">see-yah-bah-NGEH-nah · “we’re getting in”</p></div>
    <div class="prose" style="display:grid;gap:18px">
      <p style="color:#fff">It’s uniquely South African and means “we’re getting in”, literally “we are entering”, with confidence and intent. It’s what a football side says when it takes the game to the opposition: never a polite knock at the door.</p>
      <p style="color:#fff">The root verb <i>-ngena</i>, “to enter”, is the everyday verb of public transport. You <i>ngena</i> a bus, a minibus or a bakkie when you board it. Because <i>ukungena</i> is shared across the Nguni languages, it reads instantly in isiZulu and isiXhosa alike.</p>
      <p style="color:#fff">That’s why it sits beneath the logo. WOW is the public transport industry entering the digital economy on its own terms, in payments, connectivity and technology. Siyabangena: we’re getting in. And this time, everyone gets in.</p>
    </div>
  </div>
</section>

<section class="sec tar" id="evidence" aria-labelledby="evidence-title">
  <div class="wrap quote">
    <span class="eyebrow" id="evidence-title">The evidence</span>
    <blockquote>“A 1 percentage point increase in the use of digital payments corresponds to a 0,10 percentage point rise in per capita GDP growth over a two-year period.”</blockquote>
    <cite><b>Bank for International Settlements</b>Working Paper 1196 · <a href="https://www.bis.org/publ/work1196.htm" style="color:#FF8F87" rel="noopener" target="_blank">Read the paper</a></cite>
  </div>
</section>
""" + cta_band(R, "Your co-op. <span class=\"hl\">Your rules.</span>")
    return page(R, "why-wow", "Why WOW", "The asset others cannot replicate: an industry-owned co-operative structure spanning the Eastern Cape, organised from within.", body,
                image="WOW_Photo_Field-Operations.jpg", path="why-wow.html")


# ------------------------------------------------------------------ PLATFORM OVERVIEW
def platform():
    ops = [("Live dashboards", "Owners, co-ops and ECTTC see fleet, fare and wallet activity as it happens."),
           ("Provincial command centre", "One view of every route and vehicle across the Eastern Cape."),
           ("Support desk", "Help for operators, drivers and commuters, in their own language."),
           ("Field operations", "WOW Agents and technicians at the rank, installing, training and fixing.")]
    body = page_hero(R, "The platform", 'Ten focus areas. One wallet. <span class="hl">One owner.</span>',
                     "Each focus area rides the same wallet and the same organised industry: a compounding digital economy where every new capability makes every other one stronger.",
                     [("Platform", None)])
    body += f"""
<section class="sec" aria-labelledby="areas-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Focus areas</span><h2 class="h2" id="areas-title">Choose a focus area to see how it works.</h2></div>
    {area_tiles(True)}
  </div>
</section>

<section class="sec tar" aria-labelledby="ops-title">
  <div class="wrap">
    <div class="sec-head split">
      <div style="display:grid;gap:16px"><span class="eyebrow">Underpinning all ten</span><h2 class="h2" id="ops-title">Run by the industry, <span class="hl">for the industry.</span></h2></div>
      <p class="lead">The same operations backbone supports every focus area, so nothing is bolted on and nobody is left without help.</p>
    </div>
    <div class="grid4">{"".join(f'<article class="card"><span class="dot"></span><h3>{e(t)}</h3><p>{e(d)}</p></article>' for t, d in ops)}</div>
  </div>
</section>

<section class="sec chalk" id="destination" aria-labelledby="dest-title">
  <div class="wrap split">
    <div style="display:grid;gap:22px;justify-items:start">
      <span class="eyebrow">The destination</span>
      <h2 class="h2" id="dest-title">A world-class IPTMS, <span class="hl">owned by the people who operate it.</span></h2>
      <p class="lead">Buses, minibuses, bakkies, e-hailing, scholar transport and township delivery on one Integrated Public Transport Management System, unlocking prosperity through digitalisation.</p>
      {points([("Every mode, one system", "Shared rails, live fleet visibility, cashless fares on any phone and one wallet across the whole journey."),
               ("Ownership as infrastructure", "The platform, the wallet, the data and the revenue belong to the co-operative the industry built."),
               ("The national template", "Organised industry first, technology second, prosperity third. A blueprint for province after province.")])}
    </div>
    {photo(R, "WOW_Photo_Commuter-Cashless-Payment.jpg", "A commuter pays her fare by phone at the driver’s window", "One wallet across the journey", "green")}
  </div>
</section>
""" + cta_band(R)
    return page(R, "platform", "Platform", "Ten focus areas, one wallet, one owner: wallet and payments, fuel, mobile, tracking, scholar transport, e-hailing and more.", body,
                image="WOW_Photo_Commuter-Cashless-Payment.jpg", path="platform.html")


def build_all():
    return {"index.html": home(), "why-wow.html": why(), "platform.html": platform()}
