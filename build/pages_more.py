"""WOW website — who it's for, partners, news, investors, get involved."""
from html import escape as e
from layout import AREAS, AUDIENCES, page, page_hero, route, btn, more, tab, photo, stats, cta_band, ic

R = ""
AREA = {a["slug"]: a for a in AREAS}


def benefit_list(items):
    out = []
    for title, text, slug in items:
        a = AREA.get(slug)
        link = f' <a href="{R}platform/{slug}.html">{e(a["name"])}</a>' if a else ""
        dot = a["accent"] if a else ""
        out.append(f'<li><span class="dot {dot}"></span><b>{e(title)}</b><p>{e(text)}{link}</p></li>')
    return '<ul class="points">' + "".join(out) + "</ul>"


# ------------------------------------------------------------------ WHO IT'S FOR
AUD = {
    "owners": ("Earn more from the fleet <span class=\"hl\">you already run.</span>", "WOW turns the fuel you buy, the trips you run and the records you keep into money and leverage.", "owner", [
        ("Fuel rebates", "Collective buying power earns rebates at participating sites, paid back through your co-op.", "fuel"),
        ("Your fleet, on screen", "Live GPS, onboard cameras and fuel tracking, so theft has nowhere to hide.", "track"),
        ("Records the bank will accept", "Every recorded trip is proof of income and a path to vehicle finance.", "track"),
        ("Instant, free payouts", "Your share lands in your WOW wallet in seconds, split exactly as the co-op agreed.", "wallet")]),
    "drivers": ("Less cash. More control. <span class=\"hl\">Your own platform.</span>", "Carry less cash, get paid faster and earn in the quiet hours between peaks.", "driver", [
        ("Safer cashless fares", "Card, app, QR or USSD. Less cash in the vehicle means less risk on the road.", "track"),
        ("A wallet that pays instantly", "Wallet-to-wallet transfers settle in seconds and cost nothing.", "wallet"),
        ("Earn between peaks", "E-hailing and township deliveries on the industry’s own platform.", "wow-go"),
        ("Data that doesn’t expire", "Affordable SIMs sold at the rank, with data that stays yours until you use it.", "mobile")]),
    "commuters": ("Pay, connect and win <span class=\"hl\">on the ride you take.</span>", "WOW makes every trip simpler and more rewarding, on the phone you already own.", "commuter", [
        ("Pay on any phone", "No cash needed. Pay by card, app, QR or USSD, even on the simplest handset.", "track"),
        ("Free WiFi on board", "Ride connected on board and at ranks with WOW-Fi.", "wow-fi"),
        ("Win real prizes", "Riding, topping up and spending earn LuckyX entries. Never bought, never gambling.", "luckyx"),
        ("Scholars get home safely", "Parents get an alert when their child boards and arrives.", "scholar")]),
    "associations": ("Your co-op. Your rules. <span class=\"hl\">Enforced.</span>", "WOW records the structure your members built and runs it automatically, on every transaction.", "association", [
        ("Membership on the record", "Every operator, vehicle and driver registered under your co-operative.", "connect"),
        ("Splits enforced in code", "Operator, association and co-op shares run exactly as you set them.", "wallet"),
        ("Help at your rank", "WOW Agents register members, top up wallets and train people where they work.", "connect"),
        ("Rebates flow back to you", "Fuel savings return through the co-operative structure you own.", "fuel")]),
    "brands": ("Reach <span class=\"hl\">10,7 million riders</span> a day.", "Public transport carries more South Africans than any other channel. WOW lets brands reach them in ways commuters welcome.", "brand", [
        ("Advertise on WOW-Fi", "Reach commuters on the free WiFi they choose, on board and at ranks.", "wow-fi"),
        ("Sponsor LuckyX prizes", "Fund rewards that commuters earn by riding, topping up and spending.", "luckyx"),
        ("Connect to rank retail", "Drive commuter wallets to merchants in the public transport economy.", "merchants")]),
    "government": ("Accountable public transport, <span class=\"hl\">from the rank up.</span>", "WOW gives departments and municipalities verified data and a formal partner that represents the industry.", "government", [
        ("Verified scholar transport", "Biometric proof of every trip, with ghost-learner claims designed out.", "scholar"),
        ("An integrated transport system", "Buses, minibuses, bakkies, scholar transport and e-hailing on one platform, with live fleet visibility.", "track"),
        ("One organised counterpart", "A provincial co-operative with mandate, legitimacy and reach.", ""),
        ("A national template", "A model built in the Eastern Cape, ready to replicate province by province.", "")]),
}


def who():
    labels = dict(AUDIENCES)
    sub = "".join(f'<li><a href="#{s}">{e(l)}</a></li>' for s, l in AUDIENCES) + f'<li><a href="{R}investors.html">Investors</a></li>'
    secs = ""
    for i, (slug, (title, lead, role, items)) in enumerate(AUD.items()):
        ground = "chalk" if i % 2 else ""
        secs += f"""
<section class="sec {ground}" id="{slug}" aria-labelledby="{slug}-title">
  <div class="wrap split" style="align-items:start">
    <div style="display:grid;gap:22px;justify-items:start;position:sticky;top:160px">
      {tab(labels[slug], "red" if i % 2 == 0 else "")}
      <h2 class="h2" id="{slug}-title">{title}</h2>
      <p class="lead">{e(lead)}</p>
      {btn("Get involved", f"{R}get-involved.html")}
    </div>
    {benefit_list(items)}
  </div>
</section>"""
    body = page_hero(R, "Who it’s for", 'Built for everyone who <span class="hl">gets in.</span>',
                     "Owners, drivers, commuters, co-ops, brands and government each get something different from WOW. Find your part.",
                     [("Who it’s for", None)])
    body += f'<nav class="subnav" aria-label="Audiences"><div class="wrap"><ul>{sub}</ul></div></nav>' + secs
    body += f"""
<section class="sec tight ox" aria-labelledby="inv-title">
  <div class="wrap cta-inner">
    <div style="display:grid;gap:14px"><span class="eyebrow">Investors</span><h2 class="h2" id="inv-title">Invest in the industry’s own infrastructure.</h2></div>
    <div style="display:grid;gap:20px;justify-items:start"><p class="lead">The WOW data room is open by invitation and includes the Eastern Cape Transport Bond.</p>{btn("Investor information", R + "investors.html", "white")}</div>
  </div>
</section>"""
    return page(R, "who-its-for", "Who it’s for", "What WOW offers owners and operators, drivers, commuters, associations and co-ops, brands and government.", body,
                image="WOW_Photo_Agent-At-The-Rank.jpg", path="who-its-for.html")


# ------------------------------------------------------------------ PARTNERS
def partners():
    rows = [
        ("Technology partner & system operator", "Ecentric Payment Systems", "The payment backbone of South African retail, processing more than R1 trillion for the country’s largest retailers, now pointed at the public transport economy. Ecentric runs the switch, the settlement and the waterfall: every split enforced in code, on every transaction, from the forecourt to final settlement. Five years assessing this industry before a cent was committed."),
        ("Ecosystem & business model", "FORUS Digital", "The architect of the WOW ecosystem and its business model: the WOW Connect app, the agent network, rewards and the commercial engine that turns platform activity into livelihoods. FORUS designs how the pieces earn together, so value created by the industry flows back to the industry."),
        ("Fuel rebate partner", "BT-Corp", "Aggregates the industry’s fuel spend and operates the rebate programme across the WOW Fuel Rebate Network."),
        ("GPS & mobility technology innovation partner", "True Value Systems", "The innovation force behind WOW-Track, onboard devices, biometrics and the scholar transport hardware: mobility technology built for South African conditions."),
    ]
    rows_html = "".join(f'<article class="partner"><div><span class="eyebrow">{e(r)}</span><h3>{e(n)}</h3></div><p class="lead" style="max-width:62ch">{e(d)}</p></article>' for r, n, d in rows)
    money = [("What eZAR is", "eZAR is a digital rand. Every eZAR in a WOW wallet is matched one for one by a real rand held in independent custody with Ninety One, one of South Africa’s largest asset managers. It’s always worth exactly one rand, and the balance earns while it sits."),
             ("Who stands behind it", "RainFin, a licensed financial services provider, issues eZAR and carries the regulatory responsibility: the same duties of care a bank carries, applied to the industry’s own wallet."),
             ("The rails it runs on", "OPEN is the regulated network eZAR moves on, technology that grew out of the South African Reserve Bank’s Project Khokha 2. Money moves between wallets instantly, costs nothing to send and settles with central-bank-grade certainty.")]
    body = page_hero(R, "Partners", 'The industry owns it. <span class="hl">World-class partners deliver it.</span>',
                     "WOW belongs to the co-operative. Specialist partners run the payments, technology and programmes behind it.", [("Partners", None)])
    body += f"""
<section class="sec" aria-labelledby="delivery-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Delivery partners</span><h2 class="h2" id="delivery-title">Who does what.</h2></div>
    {rows_html}
  </div>
</section>
<section class="sec chalk" id="money" aria-labelledby="money-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">The money layer · OPEN, RainFin &amp; eZAR</span><h2 class="h2" id="money-title">The digital rand, <span class="hl">explained simply.</span></h2></div>
    <div class="grid3">{"".join(f'<article class="card"><h3>{e(t)}</h3><p>{e(d)}</p></article>' for t, d in money)}</div>
  </div>
</section>""" + cta_band(R)
    return page(R, "partners", "Partners", "Ecentric, FORUS Digital, BT-Corp, True Value Systems and the eZAR money layer: the partners that deliver WOW.", body, path="partners.html")


# ------------------------------------------------------------------ NEWS
def news():
    press = [
        ("ITWeb", "2024-11-20", "20 Nov 2024", "Taxi industry enters SA’s MVNO market with WOW Mobile", "The industry has become the latest player to launch its own mobile virtual network operator (MVNO).", "https://www.itweb.co.za/article/taxi-industry-enters-sas-mvno-market-with-wow-mobile/O2rQGqAEb9zqd1ea"),
        ("Africa Business", "2024-07-25", "25 Jul 2024", "Industry-led tech solution designed to bring SA’s minibus taxis into the digital age", "WOW brings the public transport industry into the digital age with digital payments and blockchain technology.", "https://africabusiness.com/2024/07/25/industry-led-tech-solution-designed-to-bring-sas-minibus-taxis-into-the-digital-age/"),
        ("ITWeb", "2024-07-11", "11 Jul 2024", "Eastern Cape readies digital taxi initiative", "The ECTTC is preparing to officially launch the Wealth on Wheels Cashless and Digitisation Project across the Eastern Cape.", "https://www.itweb.co.za/article/eastern-cape-readies-digital-taxi-initiative/lLn14MmQ2Q1MJ6Aa"),
        ("TechFinancials", "2024-07-10", "10 Jul 2024", "Digital taxi initiative WOWs SA Transport Conference", "Delegates at the 42nd Southern African Transport Conference found WOW-branded vehicles parked inside the venue foyer.", "https://techfinancials.co.za/2024/07/10/digital-taxi-initiative-wows-sa-transport-conference/"),
        ("ITWeb", "2023-09-06", "6 Sept 2023", "‘Wealth on Wheels’ digital payments target Eastern Cape taxis", "The ECTTC partnered with Forus Digital Group and Ecentric Payment Solutions to introduce a digital platform for public transport commuters.", "https://www.itweb.co.za/article/wealth-on-wheels-digital-payments-target-ecape-taxis/GxwQDM1DpnO7lPVo"),
    ]
    items = "".join(f'<a href="{u}" target="_blank" rel="noopener"><span class="src">{e(s)}</span><time datetime="{d}">{e(dl)}</time><div><h3>{e(t)}</h3><p>{e(x)}</p></div>{ic("ext", "Opens in a new tab")}</a>' for s, d, dl, t, x, u in press)
    body = page_hero(R, "In the news", 'Recognised across <span class="hl">Africa’s tech and business media.</span>',
                     "WOW has been covered by leading South African and African technology and business media since 2023.", [("News", None)])
    body += f"""
<section class="sec" aria-labelledby="awards-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Awards</span><h2 class="h2" id="awards-title">Two firsts in 2024.</h2></div>
    <div class="grid2">
      <article class="award"><span class="yr">Africa Tech Festival 2024 · Cape Town</span>{tab("Winner", "red")}<h3>Fintech Innovation of the Year</h3><p>Recognising WOW as a breakthrough financial technology for the African continent.</p></article>
      <article class="award"><span class="yr">SATC 2024 · 42nd Southern African Transport Conference</span>{tab("Winner", "red")}<h3>Best Exhibition Stand</h3><p>The first time a public transport industry solution has won this award.</p></article>
    </div>
  </div>
</section>
<section class="sec chalk" aria-labelledby="press-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Press coverage</span><h2 class="h2" id="press-title">What the media says.</h2></div>
    <div class="press">{items}</div>
  </div>
</section>""" + cta_band(R)
    return page(R, "news", "In the news", "Awards and press coverage for WOW — Wealth on Wheels, from ITWeb, TechFinancials, Africa Business and more.", body, path="news.html")


# ------------------------------------------------------------------ INVESTORS
DATA_ROOM = "https://wow.forus.digital/investors"
PORTAL = "https://wow.forus.digital/backoffice"


def investors():
    steps = [("Receive your access code", "The WOW investment team issues a personal code to verified investors."),
             ("Open the data room", "Go to the WOW investor data room and enter your code."),
             ("Review the documents", "Evaluate the opportunity, including the Eastern Cape Transport Bond."),
             ("Keep it confidential", "Contents are for evaluating a potential investment only, and may not be shared without written consent.")]
    body = page_hero(R, "Investors", 'Invest in the industry’s <span class="hl">own infrastructure.</span>',
                     "WOW’s investor data room is open by invitation. It includes the Eastern Cape Transport Bond.",
                     [("Investors", None)], ground="ox", route_color="#4E1618")
    body = body.replace('</p></div>\n      ', f'</p><div class="btns">{btn("Enter the data room", DATA_ROOM, "white")}</div></div>\n      ', 1)
    body += f"""
<section class="sec" aria-labelledby="case-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">The case</span><h2 class="h2" id="case-title">Scale that’s already organised.</h2></div>
    {stats([("~105 000", "Vehicles on the network"), ("~67 000", "Operators organised as one"), ("~1/3", "Of the national fleet"), ("R1 trillion+", "Processed annually by our payments partner")])}
    <div class="grid3" style="margin-top:48px">
      <article class="card"><h3>Adoption solved first</h3><p>Collective ownership and endorsement across the market before a single device is deployed.</p></article>
      <article class="card"><h3>Owned financial rails</h3><p>A regulated wallet backed 1:1 by real rands, run on central-bank-grade settlement.</p></article>
      <article class="card"><h3>Ten compounding revenue lines</h3><p>Fuel, mobile, media, payments and more, all on one wallet and one customer base.</p></article>
    </div>
    <p style="margin-top:32px">{more("Why WOW can’t be copied", R + "why-wow.html")}</p>
  </div>
</section>
<section class="sec chalk" id="data-room" aria-labelledby="req-title">
  <div class="wrap split" style="align-items:start">
    <div style="display:grid;gap:28px">
      <div style="display:grid;gap:16px"><span class="eyebrow">Data room access</span><h2 class="h2" id="req-title">How access works.</h2></div>
      <ol class="steps" style="grid-template-columns:1fr 1fr;list-style:none;padding:0;margin:0">{"".join(f'<li class="step"><span class="sn" aria-hidden="true">{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(steps, 1))}</ol>
    </div>
    <div class="card ox" style="padding:clamp(28px,4vw,48px);gap:20px;position:relative;overflow:hidden">
      {route("#4E1618", 2, 60, style="right:-22%;bottom:-40%;width:62%")}
      <div style="position:relative;display:grid;gap:18px;justify-items:start">
        {tab("Restricted access", "red")}
        <h3 class="h3" style="color:#fff">WOW investor data room</h3>
        <p style="color:#E9D6D4">Enter your access code to view confidential documents, including the Eastern Cape Transport Bond.</p>
        {btn("Enter the data room", DATA_ROOM, "white")}
        <p style="color:#E9D6D4;font-size:15px">No access code? Contact the WOW investment team.</p>
      </div>
    </div>
  </div>
</section>"""
    return page(R, "investors", "Investors", "The WOW investor data room, including the Eastern Cape Transport Bond. Access is by invitation.", body, path="investors.html")


# ------------------------------------------------------------------ GET INVOLVED
def get_involved():
    portals = [
        ("Investors", "Enter the WOW investor data room with your access code.", DATA_ROOM, "Enter the data room", "ox"),
        ("Co-ops, agents & WOW teams", "Sign in to the WOW portal to manage members, vehicles, captures and approvals.", PORTAL, "Sign in to the portal", "tar"),
    ]
    portal_cards = "".join(
        f'<a class="card {ground}" href="{href}" style="padding:clamp(28px,3.5vw,44px);gap:16px;color:#fff">{tab("WOW portal", "red")}'
        f'<h3 style="font-size:clamp(26px,2.6vw,34px);color:#fff">{e(t)}</h3><p style="color:#E9D6D4">{e(d)}</p>'
        f'<span class="more" style="color:#fff">{e(label)}{ic("arrow")}</span></a>'
        for t, d, href, label, ground in portals)
    routes_ = [(slug, label, AUD[slug][1]) for slug, label in AUDIENCES]
    route_cards = "".join(
        f'<a class="card path" href="{R}who-its-for.html#{slug}"><h3>{e(label)}</h3><p>{e(lead)}</p><span class="more">See what WOW offers{ic("arrow")}</span></a>'
        for slug, label, lead in routes_)
    body = page_hero(R, "Get involved", 'Siyabangena. <span class="hl">Let’s get you in.</span>',
                     "Choose your way in. Every link below takes you straight to the right place.", [("Get involved", None)])
    body += f"""
<section class="sec" aria-labelledby="portals-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Sign in</span><h2 class="h2" id="portals-title">Already part of WOW?</h2></div>
    <div class="grid2">{portal_cards}</div>
  </div>
</section>
<section class="sec chalk" aria-labelledby="routes-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Find your way in</span><h2 class="h2" id="routes-title">New to WOW? Start here.</h2>
      <p class="lead">See what WOW offers you, from fuel rebates and fleet tracking to cashless fares and scholar transport.</p></div>
    <div class="grid3">{route_cards}</div>
  </div>
</section>"""
    return page(R, "get-involved", "Get involved", "Ways into WOW: the investor data room, the WOW portal for co-ops and teams, and what WOW offers owners, operators, drivers, commuters, brands and government.", body,
                image="WOW_Photo_Agent-At-The-Rank.jpg", path="get-involved.html")


def build_all():
    return {"who-its-for.html": who(), "partners.html": partners(), "news.html": news(), "investors.html": investors(), "get-involved.html": get_involved()}
