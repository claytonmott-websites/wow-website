# WOW — Wealth on Wheels website

A static HTML website built on the WOW Brand Guidelines v2.0 (September 2026). No framework, no dependencies: it runs on any static host (GitHub Pages, Netlify, S3, cPanel).

## Pages

| Page | File | Purpose |
| --- | --- | --- |
| Home | `index.html` | What WOW is, proof numbers, the 10 focus areas, why it can't be copied, audience pathways, Siyabangena, awards |
| Why WOW | `why-wow.html` | Co-operative structure, organised from within, Siyabangena, BIS evidence |
| Platform | `platform.html` | All 10 focus areas, operations backbone, the IPTMS destination |
| Focus areas | `platform/*.html` | One page each: Wallet, Connect + Agent, Fuel, Mobile, Cashless + Track, LuckyX, Merchants, WOW-Fi, Scholar, WOW-Go |
| Who it's for | `who-its-for.html` | Owners, drivers, commuters, associations & co-ops, brands, government |
| Partners | `partners.html` | Ecentric, FORUS Digital, BT-Corp, True Value Systems, the eZAR money layer |
| News | `news.html` | Awards and press coverage |
| Investors | `investors.html` | Investment case; links to the investor data room (`/investors`) |
| Get involved | `get-involved.html` | Ways in: investor data room, WOW portal sign-in (`/backoffice`), audience routes |

## Editing

Pages are generated from Python templates so the header, footer and components stay consistent.

```bash
python3 build/build.py
```

- `build/layout.py` — header, mega menu, footer, shared components, the focus-area list
- `build/pages_main.py` — home, Why WOW, platform overview
- `build/pages_more.py` — who it's for, partners, news, investors, get involved
- `build/pages_platform.py` — content for the ten focus-area pages
- `assets/css/site.css` — all styles (brand tokens at the top)
- `assets/js/site.js` — menu, mega menu, forms

Edit the content in `build/`, run the build, then commit the generated HTML. Editing the HTML directly works too, but the next build will overwrite it.

Preview locally:

```bash
python3 -m http.server 8770
```

## Before launch

1. **Add the remaining internal links.** The site has no forms. Calls to action link to the WOW apps: the investor data room (`https://wow.forus.digital/investors`) and the WOW portal (`https://wow.forus.digital/backoffice`). Add links for any other flows (for example owner or driver registration) on `get-involved.html`.
2. **Replace the photography.** The six images in `assets/img/` are AI-generated concepts. Commission real photography (see brand guide chapter 06) and keep the same file names.
3. **Confirm facts and figures** with ECTTC, especially the stats, launch dates and partner descriptions.
4. **Add the missing pages**: privacy policy (POPIA), terms, and the investor data room sign-in if it stays on this domain.
5. **Set the canonical domain** in `SITE` in `build/layout.py`, then rebuild.
6. **Add analytics** (with cookie consent) if required.

## Accessibility & quality

- WCAG 2.2 AA colour contrast; visible focus states; skip link; landmark roles
- Keyboard-accessible mega menu and mobile drawer (Escape closes)
- Responsive from 320 px; reduced-motion support
- Semantic headings, descriptive link text, alt text on all images
- Meta descriptions, Open Graph tags and canonical URLs on every page
- South African English and number style (67 000, R1 trillion, 0,5 s)
