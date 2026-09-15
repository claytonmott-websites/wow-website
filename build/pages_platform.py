"""WOW website — the ten focus-area pages."""
from html import escape as e
from layout import AREAS, page, page_hero, route, btn, more, tab, stats, cta_band, ic

ACCENT_HEX = {"yellow": "#F5B400", "blue": "#2A4FCC", "green": "#199A5D", "pink": "#E04689", "red": "#DE4038"}

CONTENT = {
    "wallet": dict(
        headline='Your money, <span class="hl">your wallet</span>, your co-op.',
        intro="Every rand in WOW lives in the industry’s own regulated digital wallet, run for the co-operative, not for a bank. It’s the foundation every other focus area is built on.",
        photo=("WOW_Photo_Commuter-Cashless-Payment.jpg", "A commuter pays her fare by phone at the driver’s window"),
        role="owner", features_title="Built like a bank. Owned by the industry.",
        features=[("Backed 1:1 by real rands", "Every unit in the wallet is matched by a real rand held in independent custody with one of South Africa’s largest asset managers. Your money is always your money."),
                  ("Your balance earns while it sits", "Wallet balances earn yield linked to money-market rates, the kind of return usually reserved for big corporates."),
                  ("Instant, free, wallet to wallet", "Transfers between WOW wallets settle in seconds and cost nothing. No bank queues, no EFT delays, no fees eating the margin."),
                  ("Every split enforced in code", "Operator, association, co-op: every share runs exactly as the co-operative sets it, automatically, on every transaction.")],
        highlight=("Bank-grade from day one.", "The wallet runs on the processor behind about 87% of South Africa’s Tier 1 retail payments, on regulated rails that settle with central-bank-grade certainty.", ("How the money layer works", "partners.html#money"))),
    "connect": dict(
        headline='Membership on the record. <span class="hl">Help at the rank.</span>',
        intro="The WOW Connect app puts membership, governance and revenue participation on the record, and WOW Agents bring it to life at every rank, in your language, where the industry works.",
        photo=None, role="association", features_title="Onboarding that happens where you work.",
        features=[("Membership on the record", "Every operator, vehicle and driver registered under the co-operative structure the industry built: 186 primary co-ops, 45 secondary co-ops, one tertiary co-op."),
                  ("Your rules, enforced", "Revenue shares and governance decisions run exactly as the co-operative sets them, automatically, on every transaction."),
                  ("Jobs in local communities", "Trained WOW Agents from local communities sign up owners, drivers, merchants and commuters. Thousands of jobs as the platform scales."),
                  ("Help where you work", "Registration, wallet top-ups and training happen at the rank, not in a bank branch in town.")],
        highlight=("186 primary co-ops. 45 secondary. One voice.", "WOW Connect records the structure the industry spent years building, so every decision and every rand follows it.", ("Why the structure matters", "why-wow.html#structure"))),
    "fuel": dict(
        headline='The fuel you already buy <span class="hl">now pays you back.</span>',
        intro="Fuel is the first focus area every operator feels in the pocket, and it rests on a simple principle: the industry finally negotiating as one.",
        photo=("WOW_Photo_WOW-Fuel-Forecourt.jpg", "A WOW Fuel attendant fills a minibus while talking with the owner"),
        role="owner", features_title="One fleet, finally recognised.",
        features=[("One fleet, at last", "For decades the industry’s enormous daily fuel spend was invisible, bought one tank at a time by fragmented owners. WOW aggregates that spend so the industry is seen as the single fleet it truly is."),
                  ("The recognition smaller fleets always had", "Private fleets a fraction of this size have always earned rebates on fuel. Collective scale earns the industry the same recognition, and more."),
                  ("The WOW Fuel Rebate Network", "Participating fuel sites across the Eastern Cape, in partnership with BT-Corp, with your WOW tag as the key."),
                  ("Savings flow back through the co-op", "Every rebate flows back through the co-operative structure the industry owns, to operators, associations and co-ops, on rules the industry sets.")],
        highlight=("Launching September 2026 in Komani.", "The WOW Fuel Rebate Network starts in Komani (Queenstown), then rolls out province-wide. No new cost. No cash.", ("Register your interest", "get-involved.html"))),
    "mobile": dict(
        headline='The industry’s own <span class="hl">mobile network.</span>',
        intro="WOW Mobile is the key to owning customer relationships, and to turning every vehicle into a connected business unit that does far more than transport.",
        photo=("WOW_Photo_Agent-At-The-Rank.jpg", "A WOW Agent helps a driver set up a WOW Mobile SIM"),
        role="commuter", features_title="Connectivity that keeps the margin home.",
        features=[("SIMs sold at the rank", "Affordable SIMs from WOW Agents right where you work, for drivers, owners, commuters and their families."),
                  ("Data that doesn’t expire", "Buy what you need, when you can. Your data stays yours until you use it. No more airtime lost at month-end."),
                  ("A data-free app", "Manage your wallet, rewards and account without using a single megabyte, and earn free data by watching ads or completing surveys."),
                  ("The margin comes home", "Every SIM sold and every top-up made earns for the industry. Money that used to leave the province now stays in it.")],
        highlight=("Transport is just the beginning.", "When the industry owns the network, every vehicle becomes a connected business unit.", ("See WOW-Fi", "platform/wow-fi.html"))),
    "track": dict(
        headline='Fleet control and cashless fares <span class="hl">in one system.</span>',
        intro="Across buses, minibuses, bakkies, scholar transport and e-hailing, WOW Cashless + WOW-Track deliver a truly Integrated Public Transport Management System (IPTMS) to commuters.",
        photo=("WOW_Photo_Field-Operations.jpg", "A WOW field technician checks a vehicle at the rank"),
        role="owner", features_title="See every vehicle. Record every fare.",
        features=[("Your fleet, on screen", "Live GPS on every vehicle, onboard cameras for safer drivers and passengers, and fuel consumption tracked at the tank, so theft has nowhere to hide."),
                  ("Every fare, on the record", "Card, app, QR or USSD: commuters pay cashless even on the simplest phone. Less cash in the vehicle means less risk on the road."),
                  ("Every mode, together", "One platform across every mode the co-operative runs, the integrated view no city system has achieved at this scale."),
                  ("Trusted records become bankable records", "Every recorded trip is proof of income: statements, credit history, and a path to vehicle finance that cash could never open.")],
        highlight=("From Gqeberha to Mthatha to Aliwal North.", "Every route the industry drives across the Eastern Cape, running on one integrated system.", ("The destination: a world-class IPTMS", "platform.html#destination"))),
    "luckyx": dict(
        headline='Earned, <span class="hl">never bought.</span>',
        intro="LuckyX turns everyday behaviour (riding, topping up, spending) into entries for real prizes. Earned through participation, never bought. Explicitly not gambling.",
        photo=None, role="brand", features_title="Rewards that respect commuters.",
        features=[("Earned through participation", "Riding, topping up and spending create an entry. Nobody buys a chance, and nobody needs to."),
                  ("Explicitly not gambling", "No stake is placed and nothing is ever put at risk. LuckyX is a sweepstake run on participation, not a wager."),
                  ("Works on any phone", "No smartphone and no data needed. Every commuter can take part on the handset they already own."),
                  ("Sponsors pay. Your passengers win.", "Major retailers fund the prizes to reach your commuters. The industry provides the audience.")],
        highlight=("Brands fund the prizes.", "Reach millions of daily commuters with rewards they actually earned.", ("Partner with LuckyX", "get-involved.html"))),
    "merchants": dict(
        headline='Rank shops and spazas, <span class="hl">cashless.</span>',
        intro="For rank shops, spazas, suppliers and every merchant in the public transport economy: the bridge that drives commuters to retailers and keeps money circulating in the community.",
        photo=None, role="other", features_title="The whole business in one device.",
        features=[("The whole business, in one system", "POS and card machine in one device, an online store out of the box, and quotes, invoices and receipts by print, SMS or email."),
                  ("Stock and numbers under control", "Inventory with a built-in barcode scanner, sales history, refunds, reporting and business analytics."),
                  ("Keep them coming back", "Loyalty and customer tools that grow repeat trade, with commuter wallets spending where the community lives."),
                  ("The retail connection", "Merchants plug into the same wallet the commuters carry, the bridge between the public transport economy and formal retail.")],
        highlight=("Money earned in the community stays in the community.", "Every cashless sale keeps value circulating locally, on the industry’s own rails.", ("Get your business on WOW", "get-involved.html"))),
    "wow-fi": dict(
        headline='Free WiFi for them. <span class="hl">A media business for you.</span>',
        intro="WOW-Fi turns every vehicle and every rank into connected space the industry owns: free connectivity for commuters, and a media channel for the platform’s owners.",
        photo=None, role="brand", features_title="The audience no other channel can match.",
        features=[("Commuters ride connected", "Free WiFi on board makes your vehicles the ride people choose, and keeps them loyal to your routes."),
                  ("An audience no channel can match", "10,7 million South Africans ride public transport every day. Brands will pay to reach them on WiFi the industry controls."),
                  ("The revenue is yours", "Every vehicle becomes a media channel owned by the platform you own, with advertising income flowing back to the industry."),
                  ("Value-added services", "Insurance, mobile top-ups and deals on goods and services, delivered over the connection the industry provides.")],
        highlight=("10,7 million riders. Every day.", "Advertise on the connection commuters choose, owned by the industry that carries them.", ("Advertise on WOW-Fi", "get-involved.html"))),
    "scholar": dict(
        headline='Safe children. Paid operators. <span class="hl">Accountable spend.</span>',
        intro="More than 120 000 scholars ride with the industry every school day. WOW solves what paper registers never could, with palm-vein biometrics: contactless, hygienic and impossible to forge.",
        photo=("WOW_Photo_Scholars-Palm-Scan.jpg", "A learner scans her palm to board scholar transport"),
        role="government", features_title="One scan answers who, where and when.",
        features=[("Parents & guardians", "Real-time alerts when their child boards and alights, with location attached: certainty their child was on the right vehicle, every day."),
                  ("Transport operators", "Trips logged automatically and invoices generated from verified trip data. No paper registers, and payment for the trips actually run, on time."),
                  ("Schools & authorities", "Every claim backed by who, where and when: biometric proof of service delivered, with fraud and ghost-learner claims designed out."),
                  ("Privacy by design", "Biometric templates are encrypted, with parental consent at enrolment. The palm is the one credential a child can’t lose, lend or have stolen.")],
        steps=[("Scan on", "A learner hovers a palm when boarding. Identity confirmed in under half a second."),
               ("Trip tracked", "Every event is GPS-located and time-stamped, checked against the planned route."),
               ("Scan off", "A second scan on alighting closes the trip record, validated inside the school’s geofence."),
               ("Parents notified", "Instant boarding and drop-off alerts with location. Peace of mind, every day.")],
        stats=[("< 0,5 s", "Per scan, so no queues at the door"), ("0", "Cards or tags to lose, lend or steal"), ("100%", "Of trips logged, geo-stamped and auditable"), ("120 000+", "Scholars transported every school day")],
        highlight=("One device. Every answer.", "The onboard terminal pairs a palm-vein sensor with GPS and always-on connectivity, fast enough for a full vehicle at the door, with store-and-forward for rural dead zones.", ("Talk to us about scholar transport", "get-involved.html"))),
    "wow-go": dict(
        headline='South Africa’s own <span class="hl">e-hailing.</span>',
        intro="E-hailing and deliveries on the industry’s own platform: proudly South African, built for our country, answering to its members instead of shareholders overseas.",
        photo=None, role="driver", features_title="The commission stays home.",
        features=[("SA’s own e-hailing app", "Around 15 000 e-hailing members have already joined the co-operative. WOW-Go gives them an industry-owned way to work."),
                  ("The commission stays home", "The cut that used to leave the province, and the country, now stays inside the co-operative and its members."),
                  ("Deliveries between peaks", "Minibuses, bakkies and e-hailing vehicles earn from township last-mile deliveries in the quiet hours, built for how South Africa actually moves."),
                  ("One wallet for everything", "Fares, fuel, rewards and payouts land in the same WOW wallet: one balance, one statement, one owner.")],
        highlight=("~15 000 e-hailing members already in.", "Drive for a platform you own, not one that answers to shareholders overseas.", ("Join WOW-Go", "get-involved.html"))),
}


def area_page(i):
    a = AREAS[i]
    c = CONTENT[a["slug"]]
    root = "../"
    prev_a, next_a = AREAS[i - 1], AREAS[(i + 1) % len(AREAS)]
    accent = a["accent"]
    if c["photo"]:
        visual = f'<div class="fa-visual bg-{accent}"><img src="{root}assets/img/{c["photo"][0]}" alt="{e(c["photo"][1])}" width="1200" height="900"></div>'
    else:
        visual = f'<div class="fa-visual bg-{accent}" aria-hidden="true">{route(ACCENT_HEX[accent], i % 3, 72)}<span class="big">{a["n"]}</span></div>'

    hero = page_hero(root, f'Focus area {a["n"]} · {a["name"]}', c["headline"], e(c["intro"]),
                     [("Platform", root + "platform.html"), (a["name"], None)],
                     aside=visual, ground="", route_color=None, cls="fa-hero")
    hero = hero.replace('<div class="btns"></div>', '')
    hero = hero.replace('<p class="lead">', f'<div style="display:flex;gap:10px;flex-wrap:wrap">{tab(a["short"], accent)}</div><p class="lead">', 1)
    hero = hero.replace('</p></div>\n      <div>', f'</p><div class="btns">{btn("Get involved", root + "get-involved.html")}{btn("All focus areas", root + "platform.html", "secondary", False)}</div></div>\n      <div>', 1)

    feats = "".join(f'<article class="feature"><h3><span class="dot {accent}"></span>{e(t)}</h3><p>{e(d)}</p></article>' for t, d in c["features"])
    body = hero + f"""
<section class="sec chalk" aria-labelledby="f-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">What it does</span><h2 class="h2" id="f-title">{e(c["features_title"])}</h2></div>
    <div class="features" style="--x:0">{feats.replace('class="feature"', 'class="feature" style="background:#fff"')}</div>
  </div>
</section>"""

    if c.get("steps"):
        steps = "".join(f'<li class="step"><span class="sn" aria-hidden="true">{n}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for n, (t, d) in enumerate(c["steps"], 1))
        body += f"""
<section class="sec" aria-labelledby="s-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">How a trip works</span><h2 class="h2" id="s-title">Four steps, every trip.</h2></div>
    <ol class="steps" style="list-style:none;padding:0;margin:0">{steps.replace('class="step"', 'class="step" style="background:var(--chalk)"')}</ol>
    <div style="margin-top:56px">{stats(c["stats"])}</div>
  </div>
</section>"""

    ht, hd, (hl, hh) = c["highlight"]
    hl_ground = {"yellow": "bg-yellow", "blue": "bg-blue", "green": "bg-green", "pink": "bg-pink", "red": "bg-red"}[accent]
    btn_kind = "white" if accent in ("blue", "red") else "secondary"
    body += f"""
<section class="sec" aria-labelledby="h-title">
  <div class="wrap">
    <div class="highlight {hl_ground}">
      {route(ACCENT_HEX[accent], 2, 70)}
      <h2 class="h2" id="h-title">{e(ht)}</h2>
      <div><p style="font-size:19px;line-height:1.5">{e(hd)}</p><div class="btns">{btn(hl, root + hh, btn_kind)}</div></div>
    </div>
  </div>
</section>
<section class="sec tight" aria-label="More focus areas">
  <div class="wrap">
    <div class="pn">
      <a href="{prev_a['slug']}.html"><small>← {prev_a['n']} Previous</small><b>{e(prev_a['name'])}</b></a>
      <a href="{next_a['slug']}.html"><small>Next {next_a['n']} →</small><b>{e(next_a['name'])}</b></a>
    </div>
    <p style="margin-top:24px;text-align:center">{more("See all ten focus areas", root + "platform.html")}</p>
  </div>
</section>""" + cta_band(root)

    return page(root, "platform", a["name"], f'{a["name"]} — {a["tagline"]}', body,
                image=c["photo"][0] if c["photo"] else "WOW_Photo_Owner-Golden-Hour.jpg", path=f'platform/{a["slug"]}.html')


def build_all():
    return {f'platform/{a["slug"]}.html': area_page(i) for i, a in enumerate(AREAS)}
