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
        ("Free WiFi on board", "Ride connected on taxis and at ranks with WOW-Fi.", "wow-fi"),
        ("Win real prizes", "Riding, topping up and spending earn LuckyX entries. Never bought, never gambling.", "luckyx"),
        ("Scholars get home safely", "Parents get an alert when their child boards and arrives.", "scholar")]),
    "associations": ("Your co-op. Your rules. <span class=\"hl\">Enforced.</span>", "WOW records the structure your members built and runs it automatically, on every transaction.", "association", [
        ("Membership on the record", "Every operator, vehicle and driver registered under your co-operative.", "connect"),
        ("Splits enforced in code", "Operator, association and co-op shares run exactly as you set them.", "wallet"),
        ("Help at your rank", "WOW Agents register members, top up wallets and train people where they work.", "connect"),
        ("Rebates flow back to you", "Fuel savings return through the co-operative structure you own.", "fuel")]),
    "brands": ("Reach <span class=\"hl\">10,7 million riders</span> a day.", "Minibus taxis carry more South Africans than any other channel. WOW lets brands reach them in ways commuters welcome.", "brand", [
        ("Advertise on WOW-Fi", "Reach commuters on the free WiFi they choose, on taxis and at ranks.", "wow-fi"),
        ("Sponsor LuckyX prizes", "Fund rewards that commuters earn by riding, topping up and spending.", "luckyx"),
        ("Connect to rank retail", "Drive commuter wallets to merchants in the taxi economy.", "merchants")]),
    "government": ("Accountable public transport, <span class=\"hl\">from the rank up.</span>", "WOW gives departments and municipalities verified data and a formal partner that represents the industry.", "government", [
        ("Verified scholar transport", "Biometric proof of every trip, with ghost-learner claims designed out.", "scholar"),
        ("An integrated transport system", "Taxis, buses and e-hailing on one platform, with live fleet visibility.", "track"),
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
      {btn("Get involved", f"{R}get-involved.html?role={role}")}
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
    return page(R, "who-its-for", "Who it’s for", "What WOW offers taxi owners, drivers, commuters, associations and co-ops, brands and government.", body,
                image="WOW_Photo_Agent-At-The-Rank.jpg", path="who-its-for.html")


# ------------------------------------------------------------------ PARTNERS
def partners():
    rows = [
        ("Technology partner & system operator", "Ecentric Payment Systems", "The payment backbone of South African retail, processing more than R1 trillion for the country’s largest retailers, now pointed at the taxi economy. Ecentric runs the switch, the settlement and the waterfall: every split enforced in code, on every transaction, from the forecourt to final settlement. Five years assessing this industry before a cent was committed."),
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
        ("ITWeb", "2024-11-20", "20 Nov 2024", "Taxi industry enters SA’s MVNO market with WOW Mobile", "The South African taxi industry has become the latest player to provide a local mobile virtual network operator offering.", "https://www.itweb.co.za/article/taxi-industry-enters-sas-mvno-market-with-wow-mobile/O2rQGqAEb9zqd1ea"),
        ("Africa Business", "2024-07-25", "25 Jul 2024", "Industry-led tech solution designed to bring SA’s minibus taxis into the digital age", "WOW aims to revolutionise the local minibus taxi industry through technologies such as digital cash payments and blockchain.", "https://africabusiness.com/2024/07/25/industry-led-tech-solution-designed-to-bring-sas-minibus-taxis-into-the-digital-age/"),
        ("ITWeb", "2024-07-11", "11 Jul 2024", "Eastern Cape readies digital taxi initiative", "The ECTTC is preparing to officially launch the Wealth on Wheels Cashless and Digitisation Project across the Eastern Cape.", "https://www.itweb.co.za/article/eastern-cape-readies-digital-taxi-initiative/lLn14MmQ2Q1MJ6Aa"),
        ("TechFinancials", "2024-07-10", "10 Jul 2024", "Digital taxi initiative WOWs SA Transport Conference", "Delegates at the 42nd Southern African Transport Conference found colourful minibus taxis parked inside the venue foyer.", "https://techfinancials.co.za/2024/07/10/digital-taxi-initiative-wows-sa-transport-conference/"),
        ("ITWeb", "2023-09-06", "6 Sept 2023", "‘Wealth on Wheels’ digital payments target Eastern Cape taxis", "The ECTTC partnered with Forus Digital Group and Ecentric Payment Solutions to introduce a digital platform for taxi commuters.", "https://www.itweb.co.za/article/wealth-on-wheels-digital-payments-target-ecape-taxis/GxwQDM1DpnO7lPVo"),
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
      <article class="award"><span class="yr">SATC 2024 · 42nd Southern African Transport Conference</span>{tab("Winner", "red")}<h3>Best Exhibition Stand</h3><p>The first time a taxi industry solution has won this award.</p></article>
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
def investors():
    steps = [("Request access", "Tell us who you are and which organisation you represent."), ("We verify", "The WOW team confirms your details and investor status."),
             ("Receive your code", "You get a personal invite code with a set access period."), ("Enter the data room", "Review documents, including the Eastern Cape Transport Bond.")]
    body = page_hero(R, "Investors", 'Invest in the industry’s <span class="hl">own infrastructure.</span>',
                     "WOW’s investor data room is open by invitation. It includes the Eastern Cape Transport Bond.",
                     [("Investors", None)], ground="ox", route_color="#4E1618")
    body = body.replace('</p></div>\n      ', f'</p><div class="btns">{btn("Request access", "#request", "white")}</div></div>\n      ', 1)
    body += f"""
<section class="sec" aria-labelledby="case-title">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">The case</span><h2 class="h2" id="case-title">Scale that’s already organised.</h2></div>
    {stats([("~105 000", "Minibus taxis on the network"), ("~67 000", "Operators organised as one"), ("~1/3", "Of the national fleet"), ("R1 trillion+", "Processed annually by our payments partner")])}
    <div class="grid3" style="margin-top:48px">
      <article class="card"><h3>Adoption solved first</h3><p>Collective ownership and endorsement across the market before a single device is deployed.</p></article>
      <article class="card"><h3>Owned financial rails</h3><p>A regulated wallet backed 1:1 by real rands, run on central-bank-grade settlement.</p></article>
      <article class="card"><h3>Ten compounding revenue lines</h3><p>Fuel, mobile, media, payments and more, all on one wallet and one customer base.</p></article>
    </div>
    <p style="margin-top:32px">{more("Why WOW can’t be copied", R + "why-wow.html")}</p>
  </div>
</section>
<section class="sec chalk" id="request" aria-labelledby="req-title">
  <div class="wrap split" style="align-items:start">
    <div style="display:grid;gap:28px">
      <div style="display:grid;gap:16px"><span class="eyebrow">Data room access</span><h2 class="h2" id="req-title">How access works.</h2></div>
      <ol class="steps" style="grid-template-columns:1fr 1fr;list-style:none;padding:0;margin:0">{"".join(f'<li class="step"><span class="sn" aria-hidden="true">{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(steps, 1))}</ol>
    </div>
    <div class="form-card">
      <form class="form" data-form data-done="#inv-done" data-endpoint="">
        <div class="field"><label for="inv-name">Full name <span class="req">*</span></label><input id="inv-name" name="name" autocomplete="name" required><span class="err">Enter your full name.</span></div>
        <div class="field"><label for="inv-org">Organisation <span class="req">*</span></label><input id="inv-org" name="organisation" autocomplete="organization" required><span class="err">Enter your organisation.</span></div>
        <div class="field full"><label for="inv-email">Work email <span class="req">*</span></label><input id="inv-email" name="email" type="email" autocomplete="email" required><span class="err">Enter a valid email address, like name@company.co.za.</span></div>
        <div class="field full"><label for="inv-type">Investor type <span class="req">*</span></label><select id="inv-type" name="investor_type" required><option value="">Choose one</option><option>Asset manager</option><option>Development finance institution</option><option>Bank</option><option>Private equity or venture</option><option>Other</option></select><span class="err">Choose an investor type.</span></div>
        <div class="field full"><label for="inv-msg">What are you interested in?</label><textarea id="inv-msg" name="message"></textarea></div>
        <p class="field full check"><input type="checkbox" id="inv-ok" required><label for="inv-ok">I agree that WOW may contact me about data room access.</label></p>
        <div class="field full"><button class="btn btn-primary" type="submit">Request access</button><p class="err" data-form-error hidden style="display:block;color:var(--red-deep)">We couldn’t send your request. Check your connection and try again.</p></div>
      </form>
      <div class="form-done" id="inv-done" tabindex="-1" hidden>{tab("Request received", "green")}<h3 class="h3">Thank you. We’ll be in touch.</h3><p class="muted">The WOW team will verify your details and email your invite code.</p></div>
    </div>
  </div>
</section>"""
    return page(R, "investors", "Investors", "Request access to the WOW investor data room, including the Eastern Cape Transport Bond.", body, path="investors.html")


# ------------------------------------------------------------------ GET INVOLVED
def get_involved():
    roles = [("owner", "Taxi owner or fleet owner"), ("driver", "Driver"), ("commuter", "Commuter"), ("association", "Association or co-op"),
             ("government", "Government or municipality"), ("brand", "Brand or sponsor"), ("investor", "Investor or funder"), ("other", "Merchant or other")]
    body = page_hero(R, "Get involved", 'Siyabangena. <span class="hl">Let’s get you in.</span>',
                     "Tell us who you are and what you need. The right WOW team will be in touch.", [("Get involved", None)])
    body += f"""
<section class="sec" aria-labelledby="form-title">
  <div class="wrap split" style="align-items:start">
    <div class="form-card" style="box-shadow:none;border:1px solid var(--stone)">
      <h2 class="h3" id="form-title" style="margin-bottom:24px">Send us a message</h2>
      <form class="form" data-form data-done="#done" data-endpoint="">
        <div class="field"><label for="name">Full name <span class="req">*</span></label><input id="name" name="name" autocomplete="name" required><span class="err">Enter your full name.</span></div>
        <div class="field"><label for="org">Organisation</label><input id="org" name="organisation" autocomplete="organization"></div>
        <div class="field"><label for="email">Email address <span class="req">*</span></label><input id="email" name="email" type="email" autocomplete="email" required><span class="err">Enter a valid email address, like name@example.co.za.</span></div>
        <div class="field"><label for="phone">Phone number</label><input id="phone" name="phone" type="tel" autocomplete="tel"><span class="hint">Optional. We can WhatsApp you.</span></div>
        <div class="field full"><label for="role">I am a… <span class="req">*</span></label><select id="role" name="role" required><option value="">Choose one</option>{"".join(f'<option value="{v}">{e(l)}</option>' for v, l in roles)}</select><span class="err">Choose the option that fits you best.</span></div>
        <div class="field full"><label for="msg">How can we help?</label><textarea id="msg" name="message"></textarea></div>
        <p class="field full check"><input type="checkbox" id="consent" required><label for="consent">I agree that WOW may contact me about my enquiry.</label></p>
        <div class="field full"><button class="btn btn-primary" type="submit">Send message</button><p class="err" data-form-error hidden style="display:block;color:var(--red-deep)">We couldn’t send your message. Check your connection and try again.</p></div>
      </form>
      <div class="form-done" id="done" tabindex="-1" hidden>{tab("Message sent", "green")}<h3 class="h3">Thank you. Siyabangena!</h3><p class="muted">Your message is with the WOW team, and the right person will contact you.</p>{more("Explore the platform", "platform.html")}</div>
    </div>
    <div style="display:grid;gap:28px">
      <div style="display:grid;gap:16px"><span class="eyebrow">What happens next</span><h2 class="h2">We’ll connect you with the right team.</h2></div>
      <ul class="points">
        <li><span class="dot"></span><b>We read every message</b><p>Your enquiry goes to the team that looks after your part of WOW.</p></li>
        <li><span class="dot"></span><b>We reply with next steps</b><p>That might be a call, a meeting or registration details.</p></li>
        <li><span class="dot"></span><b>A WOW Agent can meet you at the rank</b><p>Owners, drivers and co-ops can get help in person, in their own language.</p></li>
      </ul>
      {photo(R, "WOW_Photo_Agent-At-The-Rank.jpg", "A WOW Agent helps a driver at the rank", "WOW Agents at every rank", "tar")}
      <p class="card" style="flex-direction:row;align-items:center;justify-content:space-between;flex-wrap:wrap"><span><b>Investor?</b> Request data room access instead.</span>{more("Investors", "investors.html")}</p>
    </div>
  </div>
</section>"""
    return page(R, "get-involved", "Get involved", "Get in touch with WOW: taxi owners, drivers, commuters, co-ops, brands, government and investors.", body,
                image="WOW_Photo_Agent-At-The-Rank.jpg", path="get-involved.html")


def build_all():
    return {"who-its-for.html": who(), "partners.html": partners(), "news.html": news(), "investors.html": investors(), "get-involved.html": get_involved()}
