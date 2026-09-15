"""WOW website — shared layout, components and site data."""
from html import escape as e
import hashlib
import os

_SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def asset_version(rel_path):
    """Short content hash so browsers fetch new CSS/JS whenever it changes."""
    with open(os.path.join(_SITE_DIR, rel_path), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]

SITE = "https://wow.forus.digital"

AREAS = [
    dict(slug="wallet", n="01", name="Wallet & Payments", short="The digital unlocker", accent="green",
         tagline="Every rand in WOW lives in the industry’s own regulated wallet."),
    dict(slug="connect", n="02", name="Connect + Agent", short="Onboarding at the rank", accent="blue",
         tagline="Membership on the record, with WOW Agents at every rank."),
    dict(slug="fuel", n="03", name="WOW Fuel", short="The catalyst", accent="yellow",
         tagline="The industry buying fuel as one fleet, and earning it back."),
    dict(slug="mobile", n="04", name="WOW Mobile", short="Own your customers", accent="blue",
         tagline="The industry’s own mobile network. Data that doesn’t expire."),
    dict(slug="track", n="05", name="Cashless + Track", short="A true IPTMS", accent="red",
         tagline="Fleet control and cashless fares in one system."),
    dict(slug="luckyx", n="06", name="LuckyX", short="Earned, never bought", accent="pink",
         tagline="Everyday riding and spending becomes entries for real prizes."),
    dict(slug="merchants", n="07", name="Cashless Merchants", short="The ecosystem bridge", accent="green",
         tagline="Rank shops and spazas on the same wallet commuters carry."),
    dict(slug="wow-fi", n="08", name="WOW-Fi", short="Every vehicle a media channel", accent="blue",
         tagline="Free WiFi for commuters. A media business for the industry."),
    dict(slug="scholar", n="09", name="Scholar Transport", short="Safe, verified, paid", accent="yellow",
         tagline="Palm-scan boarding for 120 000+ scholars every school day."),
    dict(slug="wow-go", n="10", name="WOW-Go", short="Proudly South African e-hailing", accent="pink",
         tagline="E-hailing and deliveries on the industry’s own platform."),
]

AUDIENCES = [
    ("owners", "Owners & operators"), ("drivers", "Drivers"), ("commuters", "Commuters"),
    ("associations", "Associations & co-ops"), ("brands", "Brands & sponsors"), ("government", "Government"),
]

_ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "ext": '<path d="M14 5h5v5M19 5l-8 8M18 14v4a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h4"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "play": '<path d="M8 5l11 7-11 7z"/>',
}


def ic(name, label=None):
    aria = f'role="img" aria-label="{e(label)}"' if label else 'aria-hidden="true"'
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" {aria}>{_ICONS[name]}</svg>')


_ROUTES = [
    "M-40 120 L300 40 L80 250 L420 170 L200 440",
    "M460 60 L150 130 L400 240 L60 330 L330 440",
    "M-30 300 L180 80 L160 300 L380 60 L360 280 L470 200",
]


def route(color="#EB4C44", variant=0, width=64, cls="route", style=""):
    return (f'<svg class="{cls}" style="{style}" viewBox="0 0 440 440" aria-hidden="true" focusable="false">'
            f'<path d="{_ROUTES[variant]}" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def btn(label, href, kind="primary", arrow=True, cls=""):
    return f'<a class="btn btn-{kind} {cls}" href="{href}">{e(label)}{ic("arrow") if arrow else ""}</a>'


def more(label, href):
    return f'<a class="more" href="{href}">{e(label)}{ic("arrow")}</a>'


def tab(label, color=""):
    return f'<span class="tab {color}">{e(label)}</span>'


def photo(root, file, alt, tag=None, tag_color="red", cls="", style=""):
    t = f'<span class="tab {tag_color}">{e(tag)}</span>' if tag else ""
    return (f'<figure class="photo {cls}" style="margin:0;{style}"><img src="{root}assets/img/{file}" alt="{e(alt)}" '
            f'loading="lazy" decoding="async" width="1200" height="900">{t}</figure>')


def stats(items):
    return '<div class="stats">' + "".join(
        f'<div class="stat"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in items) + "</div>"


def crumbs(root, items):
    parts = [f'<a href="{root}index.html">Home</a>']
    for label, href in items:
        parts.append('<span aria-hidden="true">/</span>')
        parts.append(f'<a href="{href}">{e(label)}</a>' if href else f'<span aria-current="page">{e(label)}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def page_hero(root, eyebrow, title_html, lead, trail, aside="", ground="chalk", route_color="#E7E1DE", cls=""):
    return f"""
<section class="page-hero {ground} {cls}">
  {route(route_color, 1, 60) if route_color else ""}
  <div class="wrap" style="position:relative">
    {crumbs(root, trail)}
    <div class="page-hero-grid">
      <div><span class="eyebrow">{e(eyebrow)}</span><h1 class="h1">{title_html}</h1><p class="lead">{lead}</p></div>
      {f'<div>{aside}</div>' if aside else ''}
    </div>
  </div>
</section>"""


def cta_band(root, title_html="The industry owns the road ahead.",
             text="WOW is live and rolling out across the Eastern Cape. Owner, operator, driver, co-op, brand or government partner: find your way in."):
    return f"""
<section class="sec tar cta" aria-labelledby="cta-title">
  {route("#2A2423", 2, 70)}
  <div class="wrap cta-inner">
    <div>
      <span class="eyebrow">Siyabangena</span>
      <h2 class="h2" id="cta-title" style="margin-top:16px">{title_html}</h2>
      <div class="cta-lines">{tab("Fuel", "yellow")}{tab("Ride", "white")}{tab("Pay", "green")}{tab("Earn", "pink")}{tab("Build", "blue")}</div>
    </div>
    <div style="display:grid;gap:24px">
      <p class="lead">{text}</p>
      <div class="btns">{btn("Get involved", root + "get-involved.html", "white")}{btn("Explore the platform", root + "platform.html", "outline-white", False)}</div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------- header & footer
NAV = [("Why WOW", "why-wow.html"), ("Platform", "platform.html"), ("Who it’s for", "who-its-for.html"),
       ("Partners", "partners.html"), ("News", "news.html"), ("Investors", "investors.html")]


def header(root, current):
    mega_links = "".join(
        f'<a href="{root}platform/{a["slug"]}.html"><span class="dot {a["accent"]}"></span><b>{e(a["name"])}</b><small>{e(a["short"])}</small></a>'
        for a in AREAS)
    items = []
    for label, href in NAV:
        if label == "Platform":
            cur = ' current' if current == "platform" else ''
            items.append(f'<div class="has-mega"><button type="button" class="{cur.strip()}" data-mega aria-expanded="false" aria-controls="mega">Platform{ic("chev")}</button>'
                         f'<div class="mega" id="mega" hidden><div><span class="eyebrow" style="margin:0 12px 10px;display:block">Ten focus areas</span><div class="mega-grid">{mega_links}</div></div>'
                         f'<div class="mega-side"><div style="display:grid;gap:10px"><h3>One wallet. One owner.</h3><p>Every focus area rides the same wallet and the same organised industry.</p></div>'
                         f'{btn("Platform overview", root + "platform.html", "white", True, "btn-sm")}</div></div></div>')
        else:
            key = href.replace(".html", "")
            cur = ' aria-current="page"' if current == key else ""
            items.append(f'<a href="{root}{href}"{cur}>{e(label)}</a>')
    drawer_areas = "".join(f'<a href="{root}platform/{a["slug"]}.html"><span class="dot {a["accent"]}"></span>{e(a["name"])}</a>' for a in AREAS)
    drawer = "".join(
        (f'<details><summary>Platform{ic("chev")}</summary><div><a href="{root}platform.html"><span class="dot"></span>Platform overview</a>{drawer_areas}</div></details>'
         if label == "Platform" else f'<a href="{root}{href}">{e(label)}</a>')
        for label, href in NAV)
    return f"""
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap hdr">
    <a class="logo" href="{root}index.html" aria-label="WOW — Wealth on Wheels, home"><img src="{root}assets/logos/WOW_Wordmark_Red.svg" alt="WOW!" width="128" height="34"></a>
    <nav class="nav" aria-label="Main">{"".join(items)}</nav>
    {btn("Get involved", root + "get-involved.html", "primary", False, "btn-sm")}
    <button type="button" class="menu-btn" aria-expanded="false" aria-controls="drawer" aria-label="Open menu">{ic("menu")}</button>
  </div>
  <nav class="drawer" id="drawer" aria-label="Mobile" hidden>{drawer}{btn("Get involved", root + "get-involved.html")}</nav>
</header>"""


def footer(root):
    col = lambda title, links: f'<div><h2>{title}</h2><ul>' + "".join(f'<li><a href="{h}">{e(l)}</a></li>' for l, h in links) + "</ul></div>"
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="ft">
      <div class="ft-brand">
        <img src="{root}assets/logos/WOW_Lockup-Siyabangena_White.svg" alt="WOW! Siyabangena!" width="210" height="82">
        <p>South Africa’s industry-owned digital operating system for South Africa’s public transport economy.</p>
        <div class="btns">{btn("Get involved", root + "get-involved.html", "white", True, "btn-sm")}</div>
      </div>
      {col("Platform", [("Platform overview", root + "platform.html")] + [(a["name"], f'{root}platform/{a["slug"]}.html') for a in AREAS[:6]])}
      {col("More focus areas", [(a["name"], f'{root}platform/{a["slug"]}.html') for a in AREAS[6:]])}
      {col("Who it’s for", [(l, f'{root}who-its-for.html#{s}') for s, l in AUDIENCES] + [("Investors", root + "investors.html")])}
      {col("WOW", [("Why WOW", root + "why-wow.html"), ("Partners", root + "partners.html"), ("In the news", root + "news.html"), ("Investor data room", root + "investors.html"), ("Contact us", root + "get-involved.html")])}
    </div>
    <div class="ft-base">
      <span>© <span data-year>2026</span> WOW — Wealth on Wheels. ECTTC Tertiary Co-operative. All rights reserved.</span>
      <span><b>Your co-op. Your rules.</b> Siyabangena!</span>
    </div>
  </div>
</footer>"""


def page(root, current, title, description, body, image="WOW_Photo_Operator-Sunrise.jpg", path="index.html"):
    full_title = f"{title} · WOW — Wealth on Wheels" if current != "home" else title
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="WOW — Wealth on Wheels">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:image" content="{SITE}/assets/img/{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#EB4C44">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Figtree:wght@400..800&family=JetBrains+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="{root}assets/css/site.css?v={asset_version("assets/css/site.css")}">
</head>
<body>
{header(root, current)}
<main id="main" tabindex="-1">
{body}
</main>
{footer(root)}
<script src="{root}assets/js/site.js?v={asset_version("assets/js/site.js")}" defer></script>
</body>
</html>
"""
