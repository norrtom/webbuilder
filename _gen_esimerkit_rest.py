#!/usr/bin/env python3
"""Generate dental, real-estate, construction, and law demo sites."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "esimerkit"
ORDER = "https://webbuilder.tom-1e4.workers.dev/hinnasto.html#tilaa"

BANNER_CSS = """
.wb-demo-banner{position:sticky;top:0;z-index:1000;background:#111;color:#fff;font-family:system-ui,sans-serif;font-size:.875rem;line-height:1.4}
.wb-demo-banner a{color:#fff;text-decoration:underline}
.wb-demo-banner-inner{max-width:1100px;margin:0 auto;padding:.65rem 1.25rem;display:flex;flex-wrap:wrap;gap:.75rem 1.5rem;align-items:center;justify-content:space-between}
.wb-demo-banner p{margin:0}
.wb-demo-back{white-space:nowrap;text-decoration:none!important;opacity:.85}
.wb-demo-back:hover{opacity:1}
@media(max-width:640px){.wb-demo-banner-inner{flex-direction:column;align-items:flex-start}}
"""

FORM_ALERT = "event.preventDefault();alert('Esimerkkilomake — tilaa oikeat sivut Webbuilderilta.');"


def banner(price: str, label: str, back: str) -> str:
    return f"""<div class="wb-demo-banner">
  <div class="wb-demo-banner-inner">
    <p><strong>Esimerkkisivusto</strong> · Näin voisi näyttää {label}. Hintaesimerkki <strong>{price}</strong> (alv 0 %). <a href="{ORDER}">Tilaa vastaava Webbuilderilta →</a></p>
    <a class="wb-demo-back" href="{back}">← Takaisin esittelysivulle</a>
  </div>
</div>"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", path.relative_to(Path(__file__).resolve().parent))


def nav_links(items: list[tuple[str, str]], current: str) -> str:
    parts = []
    for href, text in items:
        cur = ' aria-current="page"' if href == current else ""
        parts.append(f'<a href="{href}"{cur}>{text}</a>')
    return "".join(parts)


def head(title: str, desc: str, css: str, fonts: str, lang: str = "fi") -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="robots" content="noindex,follow"/>
<meta name="description" content="{desc}"/>
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="{fonts}" rel="stylesheet"/>
<link rel="stylesheet" href="{css}"/>
</head>
<body>
"""


# ---------------------------------------------------------------------------
# 3) HAMMAS — HammasStudio Aura — 6 pages + EN landing
# ---------------------------------------------------------------------------
def build_hammas() -> None:
    d = ROOT / "hammasstudio-aura"
    css = BANNER_CSS + """
:root{--bg:#f5f9fc;--surface:#fff;--text:#15233a;--muted:#5a6d82;--accent:#1a7ab8;--accent2:#0e4f7a;--line:#d4e3ef;--soft:#e8f2f9;--display:"Fraunces",Georgia,serif;--sans:"DM Sans",system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.65}
img{max-width:100%;display:block;height:auto}a{color:var(--accent)}
.wrap{max-width:1080px;margin:0 auto;padding:0 1.25rem}
.site-header{background:var(--surface);border-bottom:1px solid var(--line);box-shadow:0 1px 0 rgba(21,35,58,.04)}
.header-row{display:flex;align-items:center;justify-content:space-between;padding:1rem 0;gap:1rem;flex-wrap:wrap}
.logo{font-family:var(--display);font-size:1.4rem;color:var(--accent2);text-decoration:none;font-weight:500}
nav{display:flex;gap:1rem;flex-wrap:wrap;align-items:center}
nav a{text-decoration:none;color:var(--muted);font-weight:500;font-size:.9rem}
nav a[aria-current="page"],nav a:hover{color:var(--accent)}
.lang{margin-left:.5rem;padding-left:.85rem;border-left:1px solid var(--line);font-size:.85rem;font-weight:600}
.lang a{margin:0 .15rem}
.btn{display:inline-flex;padding:.75rem 1.4rem;background:var(--accent);color:#fff!important;text-decoration:none;font-weight:600;border:none;cursor:pointer;font:inherit;border-radius:.35rem}
.btn:hover{background:var(--accent2)}
.hero{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:center;padding:3.25rem 0 2.5rem}
.hero h1{font-family:var(--display);font-size:clamp(2.1rem,4.2vw,3.1rem);line-height:1.12;margin:0 0 1rem;font-weight:500}
.hero p{color:var(--muted);font-size:1.08rem;margin:0 0 1.5rem}
.hero-img{aspect-ratio:4/3;object-fit:cover;width:100%;border-radius:.5rem}
.section{padding:2.75rem 0}
.section h2,.page-title{font-family:var(--display);font-size:1.85rem;font-weight:500;margin:0 0 1rem}
.page-title{font-size:2.2rem}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.15rem}
.card{background:var(--surface);padding:1.35rem;border:1px solid var(--line);border-radius:.4rem}
.card h3{margin:0 0 .5rem;font-size:1.05rem;font-family:var(--display);font-weight:500}
.card p{margin:0;color:var(--muted);font-size:.95rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center}
.team{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.team article{background:var(--surface);border:1px solid var(--line);border-radius:.4rem;overflow:hidden}
.team img{aspect-ratio:1;object-fit:cover;width:100%}
.team div{padding:1rem 1.1rem}
.muted{color:var(--muted)}
.eyebrow{letter-spacing:.1em;text-transform:uppercase;font-size:.75rem;font-weight:700;color:var(--accent);margin:0 0 .75rem}
.site-footer{background:var(--accent2);color:#c9dde9;padding:2.5rem 0;margin-top:2rem}
.site-footer a{color:#fff}
.form{display:grid;gap:.85rem;max-width:32rem}
.form label{font-weight:600;font-size:.9rem;display:block;margin-bottom:.25rem}
.form input,.form textarea,.form select{width:100%;padding:.7rem .8rem;border:1px solid var(--line);font:inherit;background:#fff;border-radius:.3rem}
.form textarea{min-height:7.5rem}
.price-table{width:100%;border-collapse:collapse}
.price-table th,.price-table td{padding:.8rem 0;border-bottom:1px solid var(--line);text-align:left}
.price-table td:last-child{text-align:right;font-weight:600}
@media(max-width:800px){.hero,.split,.cards,.team{grid-template-columns:1fr}}
"""
    fonts = "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=DM+Sans:wght@400;500;600;700&display=swap"
    links = [
        ("index.html", "Etusivu"),
        ("palvelut.html", "Palvelut"),
        ("vastaanotto.html", "Vastaanotto"),
        ("tiimi.html", "Tiimi"),
        ("ajanvaraus.html", "Ajanvaraus"),
        ("yhteystiedot.html", "Yhteystiedot"),
    ]
    b = banner("792 €", "hammaslääkäripaketti (6 sivua, ajanvaraus, SEO, FI+EN)", "../../kotisivut-hammaslaakarille.html")
    b_en = banner("792 €", "hammaslääkäripaketti (6 sivua, ajanvaraus, SEO, FI+EN)", "../../../kotisivut-hammaslaakarille.html")

    def hdr(cur: str, prefix: str = "") -> str:
        lang = f'<span class="lang"><a href="{prefix}index.html"{" aria-current=\"page\"" if cur != "en" else ""}>FI</a> | <a href="{prefix}en/index.html"{" aria-current=\"page\"" if cur == "en" else ""}>EN</a></span>'
        nav = nav_links([(prefix + h, t) for h, t in links], prefix + cur if cur != "en" else "")
        logo = f'{prefix}index.html'
        return f"""{b if cur != "en" else b_en}<header class="site-header"><div class="wrap header-row">
<a class="logo" href="{logo}">HammasStudio Aura</a>
<nav aria-label="Päävalikko">{nav}{lang}</nav>
</div></header>"""

    foot = f"""<footer class="site-footer"><div class="wrap">
<p><strong>HammasStudio Aura Oy</strong> · Kauppakatu 28, 40100 Jyväskylä · Y-tunnus 2345678-9</p>
<p style="color:#8eb4cd">Esimerkkiklinikka Webbuilder-demoa varten. <a href="{ORDER}">Tilaa omat sivut</a></p>
</div></footer></body></html>"""

    write(d / "styles.css", css)
    write(
        d / "index.html",
        head("HammasStudio Aura — hammasklinikka Jyväskylässä", "Rauhallinen hammasklinikka Jyväskylän keskustassa. Ajanvaraus verkossa.", "styles.css", fonts)
        + hdr("index.html")
        + """
<main>
<section class="wrap hero">
  <div>
    <p class="eyebrow">Hammasklinikka · Jyväskylä</p>
    <h1>Hymy, jota uskallat näyttää.</h1>
    <p>HammasStudio Aura on pieni, moderni vastaanotto Kauppakadulla. Painotamme kivutonta hoitoa, selkeää hinnoittelua ja aikaa kuunnella.</p>
    <a class="btn" href="ajanvaraus.html">Varaa aika</a>
  </div>
  <img class="hero-img" src="https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1000&q=80" alt="Moderni hammashoitotuoli kirkkaassa vastaanottotilassa" width="1000" height="750"/>
</section>
<section class="section" style="background:var(--soft)">
  <div class="wrap">
    <h2>Miksi Aura</h2>
    <div class="cards">
      <article class="card"><h3>Kivuton lähtökohta</h3><p>Paikallispuudutus, hellä tekniikka ja aikaa totutella — erityisesti pelkopotilaille.</p></article>
      <article class="card"><h3>Selkeä hinta</h3><p>Saat arvion ennen toimenpidettä. Yleisimmät hinnat ovat palvelusivulla.</p></article>
      <article class="card"><h3>Samat tutut kasvot</h3><p>Pieni tiimi: kaksi hammaslääkäriä ja suuhygienisti. Et joudu selittämään historiaasi uudelleen.</p></article>
    </div>
  </div>
</section>
<section class="section wrap split">
  <img src="https://images.unsplash.com/photo-1606811841689-23dfdb7ee46b?auto=format&fit=crop&w=900&q=80" alt="Hammaslääkäri valmistautuu tutkimukseen" width="900" height="675" style="border-radius:.5rem"/>
  <div>
    <h2>Perushoidosta estetiikkaan</h2>
    <p class="muted">Tarkastukset, paikkaukset, juurihoidot, proteetiikka ja hampaiden valkaisu. Lasten vastaanotto maanantaisin ja keskiviikkoisin.</p>
    <p><a class="btn" href="palvelut.html">Katso palvelut</a></p>
  </div>
</section>
</main>
"""
        + foot,
    )
    write(
        d / "palvelut.html",
        head("Palvelut | HammasStudio Aura", "Tarkastus, paikkaus, juurihoito, valkaisu ja proteetiikka Jyväskylässä.", "styles.css", fonts)
        + hdr("palvelut.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Palvelut</h1>
  <p class="muted">Hinnat ovat suuntaa-antavia. Lopullinen suunnitelma ja hinta vahvistetaan tutkimuksessa.</p>
  <table class="price-table" style="margin-top:1.5rem">
    <thead><tr><th>Toimenpide</th><th>Alkaen</th></tr></thead>
    <tbody>
      <tr><td>Tarkastus ja hoitoarvio</td><td>75 €</td></tr>
      <tr><td>Hammaskiven poisto</td><td>89 €</td></tr>
      <tr><td>Paikkaus (1 pinta)</td><td>95 €</td></tr>
      <tr><td>Juurihoidon aloitus</td><td>210 €</td></tr>
      <tr><td>Hampaiden valkaisu (vastaanotto)</td><td>320 €</td></tr>
      <tr><td>Keraaminen kruunu</td><td>690 €</td></tr>
    </tbody>
  </table>
  <section class="section">
    <h2>Erityisosaaminen</h2>
    <div class="cards">
      <article class="card"><h3>Pelkopotilaat</h3><p>Ensimmäinen käynti voi olla vain tutustuminen. Kerro pelostasi ajanvarauksessa.</p></article>
      <article class="card"><h3>Lasten hammashoito</h3><p>Rauhallinen vastaanotto 3-vuotiaasta ylöspäin. Vanhempi saa olla mukana.</p></article>
      <article class="card"><h3>Estetiikka</h3><p>Valkaisu, muotoilupaikkaukset ja kruunut — luonnollinen lopputulos.</p></article>
    </div>
  </section>
</main>
"""
        + foot,
    )
    write(
        d / "vastaanotto.html",
        head("Vastaanotto | HammasStudio Aura", "Näin vastaanotto toimii Kauppakadulla Jyväskylässä.", "styles.css", fonts)
        + hdr("vastaanotto.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Vastaanotto</h1>
  <div class="split" style="margin-top:1.5rem">
    <div>
      <p class="muted">Sijaintimme on Kauppakatu 28, 2. kerros. Hissi on käytössä. Parkki P-Sokoksella tai Asemakadun kadunvarsilla.</p>
      <h2 style="margin-top:1.75rem">Käynnin kulku</h2>
      <ol class="muted" style="padding-left:1.2rem">
        <li>Saavut 5 minuuttia ennen — ilmoittaudut vastaanottotiskillä.</li>
        <li>Käymme läpi oireet, lääkitykset ja toiveet.</li>
        <li>Tutkimus ja tarvittaessa röntgen (digitaalinen, matala säteily).</li>
        <li>Saat kirjallisen hoitoarvion ennen isompia toimenpiteitä.</li>
      </ol>
      <p class="muted" style="margin-top:1.25rem"><strong>Aukiolo:</strong> ma–to 8–17, pe 8–15. Päivystystä ei ole — akuuteissa tilanteissa ohjaamme päivystykseen.</p>
    </div>
    <img src="https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=900&q=80" alt="Vastaanoton odotustila" width="900" height="675" style="border-radius:.5rem"/>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "tiimi.html",
        head("Tiimi | HammasStudio Aura", "Tutustu hammaslääkäreihin ja suuhygienistiin.", "styles.css", fonts)
        + hdr("tiimi.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Tiimi</h1>
  <p class="muted">Pieni klinikka, tutut kasvot. Työskentelemme yhdessä saman potilaan parissa.</p>
  <div class="team" style="margin-top:1.75rem">
    <article>
      <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=600&q=80" alt="Hammaslääkäri Elina Aura" width="600" height="600" loading="lazy"/>
      <div><h3 style="margin:0 0 .35rem;font-family:var(--display);font-weight:500">Elina Aura</h3><p class="muted" style="margin:0;font-size:.9rem">Hammaslääkäri, perustaja. Proteetiikka ja pelkopotilaat.</p></div>
    </article>
    <article>
      <img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=600&q=80" alt="Hammaslääkäri Markus Niemi" width="600" height="600" loading="lazy"/>
      <div><h3 style="margin:0 0 .35rem;font-family:var(--display);font-weight:500">Markus Niemi</h3><p class="muted" style="margin:0;font-size:.9rem">Hammaslääkäri. Juurihoidot ja lasten hammashoito.</p></div>
    </article>
    <article>
      <img src="https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=600&q=80" alt="Suuhygienisti Saara Laine" width="600" height="600" loading="lazy"/>
      <div><h3 style="margin:0 0 .35rem;font-family:var(--display);font-weight:500">Saara Laine</h3><p class="muted" style="margin:0;font-size:.9rem">Suuhygienisti. Hammaskivi, ohjaus ja valkaisut.</p></div>
    </article>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "ajanvaraus.html",
        head("Ajanvaraus | HammasStudio Aura", "Varaa aika hammashoitoon Jyväskylässä.", "styles.css", fonts)
        + hdr("ajanvaraus.html")
        + f"""
<main class="wrap section">
  <h1 class="page-title">Ajanvaraus</h1>
  <p class="muted" style="max-width:36rem">Kerro toiveesi ja sopiva ajankohta. Palaamme vahvistukseen yleensä saman työpäivän aikana. Akuuteissa kivuissa soita suoraan +358 14 123 4567.</p>
  <form class="form" style="margin-top:1.5rem" action="#" method="get" onsubmit="{FORM_ALERT}">
    <div><label for="n">Nimi *</label><input id="n" required/></div>
    <div><label for="p">Puhelin *</label><input id="p" type="tel" required/></div>
    <div><label for="e">Sähköposti *</label><input id="e" type="email" required/></div>
    <div><label for="s">Käynnin syy</label>
      <select id="s"><option>Tarkastus</option><option>Kipu / akuutti</option><option>Hammaskivi</option><option>Valkaisu</option><option>Muu</option></select>
    </div>
    <div><label for="a">Toivottu aika</label><input id="a" placeholder="esim. ti 9–12 tai pe iltapäivä"/></div>
    <div><label for="m">Lisätiedot</label><textarea id="m" placeholder="Oireet, pelko hammashoitoa kohtaan, vakuutus…"></textarea></div>
    <button class="btn" type="submit">Lähetä varauspyyntö</button>
  </form>
</main>
"""
        + foot,
    )
    write(
        d / "yhteystiedot.html",
        head("Yhteystiedot | HammasStudio Aura", "Osoite, puhelin ja yhteydenottolomake.", "styles.css", fonts)
        + hdr("yhteystiedot.html")
        + f"""
<main class="wrap section">
  <div class="split">
    <div>
      <h1 class="page-title">Yhteystiedot</h1>
      <p class="muted">HammasStudio Aura Oy<br/>Kauppakatu 28, 40100 Jyväskylä<br/>+358 14 123 4567<br/>ajanvaraus@aura-example.fi</p>
      <p class="muted">ma–to 8–17 · pe 8–15</p>
      <p class="muted">KELA-korvaukset hoidetaan vastaanotolla. Hyväksymme yleisimmät vakuutukset.</p>
    </div>
    <form class="form" action="#" method="get" onsubmit="{FORM_ALERT}">
      <h2 class="page-title" style="font-size:1.45rem">Lähetä viesti</h2>
      <div><label for="cn">Nimi *</label><input id="cn" required/></div>
      <div><label for="ce">Sähköposti *</label><input id="ce" type="email" required/></div>
      <div><label for="cm">Viesti *</label><textarea id="cm" required></textarea></div>
      <button class="btn" type="submit">Lähetä</button>
    </form>
  </div>
</main>
"""
        + foot,
    )
    # English landing
    write(
        d / "en" / "index.html",
        head(
            "HammasStudio Aura — dental clinic in Jyväskylä",
            "Modern dental care in central Jyväskylä. Book an appointment online.",
            "../styles.css",
            fonts,
            lang="en",
        )
        + hdr("en", prefix="../")
        + f"""
<main>
<section class="wrap hero">
  <div>
    <p class="eyebrow">Dental clinic · Jyväskylä, Finland</p>
    <h1>Care that feels calm.</h1>
    <p>HammasStudio Aura is a small private clinic on Kauppakatu. We focus on gentle treatment, clear pricing, and time to listen — in Finnish and English.</p>
    <a class="btn" href="../ajanvaraus.html">Request an appointment</a>
  </div>
  <img class="hero-img" src="https://images.unsplash.com/photo-1609840114035-3c981b782dfe?auto=format&fit=crop&w=1000&q=80" alt="Dental instruments on a sterile tray" width="1000" height="750"/>
</section>
<section class="section wrap">
  <h2>Bilingual site structure</h2>
  <p class="muted">This English landing page shows how a Webbuilder multilanguage package can work: shared design, Finnish service pages, and a dedicated EN entry for international patients and expats in Central Finland.</p>
  <div class="cards" style="margin-top:1.5rem">
    <article class="card"><h3>Check-ups & hygiene</h3><p>Exams, cleaning, and preventive care with a familiar team.</p></article>
    <article class="card"><h3>Restorative care</h3><p>Fillings, root canals, and crowns — estimate before treatment.</p></article>
    <article class="card"><h3>Book online</h3><p>Send a request via the Finnish booking form; we reply the same business day.</p></article>
  </div>
  <p style="margin-top:2rem"><a class="btn" href="../index.html">← Back to Finnish site</a></p>
</section>
</main>
<footer class="site-footer"><div class="wrap">
<p><strong>HammasStudio Aura Oy</strong> · Kauppakatu 28, 40100 Jyväskylä</p>
<p style="color:#8eb4cd">Demo clinic for Webbuilder. <a href="{ORDER}">Order your own site</a></p>
</div></footer></body></html>
""",
    )


# ---------------------------------------------------------------------------
# 4) LKV — Koti & Kaupunki — 8 pages + gallery
# ---------------------------------------------------------------------------
def build_lkv() -> None:
    d = ROOT / "koti-kaupunki"
    css = BANNER_CSS + """
:root{--bg:#f7f5f0;--surface:#fff;--text:#0f1c2e;--muted:#5c6570;--accent:#c4a35a;--navy:#0f1c2e;--navy2:#1a2f4a;--line:#e2ddd2;--display:"Playfair Display",Georgia,serif;--sans:"Manrope",system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.65}
img{max-width:100%;display:block;height:auto}a{color:var(--navy2)}
.wrap{max-width:1120px;margin:0 auto;padding:0 1.25rem}
.site-header{background:var(--navy);color:#fff}
.header-row{display:flex;align-items:center;justify-content:space-between;padding:1.05rem 0;gap:1rem;flex-wrap:wrap}
.logo{font-family:var(--display);font-size:1.35rem;color:#fff;text-decoration:none}
.logo span{color:var(--accent)}
nav{display:flex;gap:1rem;flex-wrap:wrap}
nav a{text-decoration:none;color:rgba(255,255,255,.78);font-weight:500;font-size:.88rem}
nav a[aria-current="page"],nav a:hover{color:var(--accent)}
.btn{display:inline-flex;padding:.75rem 1.4rem;background:var(--accent);color:var(--navy)!important;text-decoration:none;font-weight:700;border:none;cursor:pointer;font:inherit}
.btn:hover{filter:brightness(1.05)}
.btn-outline{background:transparent;border:1px solid var(--accent);color:var(--accent)!important}
.hero{position:relative;min-height:68vh;display:flex;align-items:flex-end;color:#fff;background:#0f1c2e}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.55}
.hero-inner{position:relative;padding:4rem 0 3rem;max-width:36rem}
.hero h1{font-family:var(--display);font-size:clamp(2.3rem,5vw,3.4rem);line-height:1.1;margin:0 0 1rem;font-weight:500}
.hero p{margin:0 0 1.5rem;color:rgba(255,255,255,.88);font-size:1.08rem}
.section{padding:3rem 0}
.section h2,.page-title{font-family:var(--display);font-size:1.9rem;font-weight:500;margin:0 0 1rem}
.page-title{font-size:2.3rem}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}
.card{background:var(--surface);padding:1.4rem;border:1px solid var(--line)}
.card h3{margin:0 0 .5rem;font-family:var(--display);font-weight:500;font-size:1.15rem}
.card p{margin:0;color:var(--muted);font-size:.95rem}
.listings{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.listing{background:var(--surface);border:1px solid var(--line);overflow:hidden}
.listing img{aspect-ratio:4/3;object-fit:cover;width:100%}
.listing-body{padding:1rem 1.1rem 1.25rem}
.listing h3{margin:0 0 .35rem;font-size:1.05rem;font-family:var(--display);font-weight:500}
.price{color:var(--navy2);font-weight:700;margin:.5rem 0 0}
.muted{color:var(--muted)}
.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .75rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:2.25rem;align-items:center}
.site-footer{background:var(--navy);color:rgba(255,255,255,.7);padding:2.5rem 0;margin-top:2rem}
.site-footer a{color:var(--accent)}
.form{display:grid;gap:.85rem;max-width:32rem}
.form label{font-weight:600;font-size:.9rem;display:block;margin-bottom:.25rem}
.form input,.form textarea,.form select{width:100%;padding:.7rem .8rem;border:1px solid var(--line);font:inherit;background:#fff}
.form textarea{min-height:7.5rem}
@media(max-width:850px){.cards,.listings,.split{grid-template-columns:1fr}}
"""
    fonts = "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Manrope:wght@400;500;600;700&display=swap"
    links = [
        ("index.html", "Etusivu"),
        ("myynti.html", "Myynti"),
        ("ostajalle.html", "Ostajalle"),
        ("kohteet.html", "Kohteet"),
        ("alue-kukkumaki.html", "Kukkumäki"),
        ("alue-centrum.html", "Centrum"),
        ("meista.html", "Meistä"),
        ("yhteystiedot.html", "Yhteys"),
    ]
    b = banner("692 €", "kiinteistönvälittäjän paketti (8 sivua, galleria, SEO)", "../../kotisivut-kiinteistovalittajalle.html")

    def hdr(cur: str) -> str:
        return f"""{b}<header class="site-header"><div class="wrap header-row">
<a class="logo" href="index.html">Koti <span>&amp;</span> Kaupunki</a>
<nav aria-label="Päävalikko">{nav_links(links, cur)}</nav>
</div></header>"""

    foot = f"""<footer class="site-footer"><div class="wrap">
<p><strong>Koti &amp; Kaupunki LKV Oy</strong> · LKV · Jyväskylä · Y-tunnus 3456789-0</p>
<p>Esimerkkivälitysliike Webbuilder-demoa varten. <a href="{ORDER}">Tilaa omat sivut</a></p>
</div></footer></body></html>"""

    write(d / "styles.css", css)
    write(
        d / "index.html",
        head("Koti & Kaupunki LKV — kiinteistönvälitys Jyväskylässä", "Asuntojen myynti ja osto Jyväskylässä. Paikallinen LKV-kumppani.", "styles.css", fonts)
        + hdr("index.html")
        + """
<main>
<section class="hero">
  <img class="hero-bg" src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1600&q=80" alt="Valoisa omakotitalo puutarhan laidalla"/>
  <div class="wrap hero-inner">
    <p class="eyebrow">LKV · Jyväskylä</p>
    <h1>Koti vaihtaa omistajaa — me hoidamme polun.</h1>
    <p>Koti &amp; Kaupunki on paikallinen välitysliike. Myymme asuntoja Kukkumäessä, keskustassa ja lähialueilla — selkeällä prosessilla ja rehellisellä hinnoittelulla.</p>
    <a class="btn" href="myynti.html">Arvioi asuntosi</a>
  </div>
</section>
<section class="section wrap">
  <h2>Miten autamme</h2>
  <div class="cards">
    <article class="card"><h3>Myynti</h3><p>Arvio, kuvat, ilmoitukset ja näytöt. Saat viikoittaisen tilannekatsauksen.</p></article>
    <article class="card"><h3>Ostajalle</h3><p>Alueiden tuntemus, tarjousneuvottelu ja kaupanteon tuki ilman painostusta.</p></article>
    <article class="card"><h3>Kohteet</h3><p>Ajankohtaiset asunnot galleriassa — suodata alueen ja budjetin mukaan.</p></article>
  </div>
</section>
<section class="section" style="background:#fff;border-block:1px solid var(--line)">
  <div class="wrap split">
    <div>
      <h2>Tunnetut korttelit</h2>
      <p class="muted">Kirjoitimme erilliset aluesivut Kukkumäelle ja keskustalle — juuri niitä hakuja varten, joilla ostajat löytävät välittäjän.</p>
      <p><a class="btn" href="alue-kukkumaki.html">Kukkumäki</a> <a class="btn btn-outline" href="alue-centrum.html" style="margin-left:.5rem">Centrum</a></p>
    </div>
    <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=900&q=80" alt="Asuntojen avaimet pöydällä" width="900" height="675"/>
  </div>
</section>
</main>
"""
        + foot,
    )
    write(
        d / "myynti.html",
        head("Asunnon myynti | Koti & Kaupunki LKV", "Arvio, markkinointi ja kaupanteko Jyväskylässä.", "styles.css", fonts)
        + hdr("myynti.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Myynti</h1>
  <p class="muted" style="max-width:40rem">Aloitamme ilmaisella arviokäynnillä. Saat kirjallisen hinta-arvion, myyntisuunnitelman ja ehdotuksen palkkiosta ennen kuin sitoudut.</p>
  <div class="cards" style="margin-top:2rem">
    <article class="card"><h3>1. Arvio</h3><p>Käymme asunnon läpi, vertaamme toteutuneisiin kauppoihin ja sovimme lähtöhinnan.</p></article>
    <article class="card"><h3>2. Markkinointi</h3><p>Ammattikuvat, pohjapiirros, Oikotie/Etuovi ja oma kohdesivu. Digimainonta tarvittaessa.</p></article>
    <article class="card"><h3>3. Kaupat</h3><p>Näytöt, tarjoukset, pankkiyhteydet ja kauppakirjat — pidämme aikataulun kasassa.</p></article>
  </div>
  <p style="margin-top:2rem"><a class="btn" href="yhteystiedot.html">Pyydä arviokäynti</a></p>
</main>
"""
        + foot,
    )
    write(
        d / "ostajalle.html",
        head("Ostajalle | Koti & Kaupunki LKV", "Apua asunnon ostoon Jyväskylässä.", "styles.css", fonts)
        + hdr("ostajalle.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Ostajalle</h1>
  <div class="split">
    <div>
      <p class="muted">Etsitkö ensimmäistä kotia, sijoitusasuntoa tai isompaa tilaa perheelle? Autamme rajaamaan alueen, budjetin ja riskit — ilman että myymme sinulle väkisin.</p>
      <ul class="muted" style="padding-left:1.2rem">
        <li>Aluekohtaiset faktat: palvelut, koulut, liikenneyhteydet</li>
        <li>Tarjousstrategia ja kilpailutilanteen lukeminen</li>
        <li>Kuntotarkastuksen tilaus ja kaupanteon checklist</li>
      </ul>
      <p style="margin-top:1.5rem"><a class="btn" href="kohteet.html">Selaa kohteita</a></p>
    </div>
    <img src="https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=900&q=80" alt="Moderni olohuone suurine ikkunoineen" width="900" height="675"/>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "kohteet.html",
        head("Kohteet | Koti & Kaupunki LKV", "Ajankohtaiset asunnot myynnissä Jyväskylässä.", "styles.css", fonts)
        + hdr("kohteet.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Kohteet</h1>
  <p class="muted">Valikoima esimerkki-ilmoituksia. Oikealla sivustolla kohteet päivittyvät myynnin mukaan.</p>
  <div class="listings" style="margin-top:1.75rem">
    <article class="listing">
      <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80" alt="Omakotitalo Kukkumäessä" width="800" height="600" loading="lazy"/>
      <div class="listing-body"><h3>Kukkumäki · 4h+k</h3><p class="muted" style="margin:0;font-size:.9rem">128 m² · 1998 · piha ja autokatos</p><p class="price">348 000 €</p></div>
    </article>
    <article class="listing">
      <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=800&q=80" alt="Keskustakaksio Jyväskylässä" width="800" height="600" loading="lazy"/>
      <div class="listing-body"><h3>Centrum · 2h+kt</h3><p class="muted" style="margin:0;font-size:.9rem">54 m² · 2012 · hissi</p><p class="price">189 000 €</p></div>
    </article>
    <article class="listing">
      <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80" alt="Rivitalokolmio" width="800" height="600" loading="lazy"/>
      <div class="listing-body"><h3>Huhtasuo · 3h+k</h3><p class="muted" style="margin:0;font-size:.9rem">82 m² · 2005 · oma piha</p><p class="price">229 000 €</p></div>
    </article>
    <article class="listing">
      <img src="https://images.unsplash.com/photo-1600047509807-ba8f99d2cd00?auto=format&fit=crop&w=800&q=80" alt="Valoisa yksiö" width="800" height="600" loading="lazy"/>
      <div class="listing-body"><h3>Lutakko · 1h+kk</h3><p class="muted" style="margin:0;font-size:.9rem">32 m² · 2018 · sijoitus</p><p class="price">132 000 €</p></div>
    </article>
    <article class="listing">
      <img src="https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=800&q=80" alt="Perheasunto avokeittiöllä" width="800" height="600" loading="lazy"/>
      <div class="listing-body"><h3>Äijälä · 5h+k</h3><p class="muted" style="margin:0;font-size:.9rem">145 m² · 2010 · sauna</p><p class="price">419 000 €</p></div>
    </article>
    <article class="listing">
      <img src="https://images.unsplash.com/photo-1600573472592-401b489a3cdc?auto=format&fit=crop&w=800&q=80" alt="Parvekkeellinen kolmio" width="800" height="600" loading="lazy"/>
      <div class="listing-body"><h3>Kortepohja · 3h+k</h3><p class="muted" style="margin:0;font-size:.9rem">76 m² · 1992 · parveke</p><p class="price">198 000 €</p></div>
    </article>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "alue-kukkumaki.html",
        head("Kukkumäki | Koti & Kaupunki LKV", "Asuinalue-esittely: Kukkumäki Jyväskylä.", "styles.css", fonts)
        + hdr("alue-kukkumaki.html")
        + """
<main class="wrap section">
  <p class="eyebrow">Aluesivu · SEO</p>
  <h1 class="page-title">Kukkumäki</h1>
  <div class="split">
    <div>
      <p class="muted">Kukkumäki on rauhallinen omakoti- ja rivitalovaltaisen alue Jyväskylän länsipuolella. Perheet arvostavat lähikouluja, ulkoilureittejä ja lyhyttä matkaa keskustaan.</p>
      <p class="muted">Tyypilliset kohteet: 1970–2000-luvun omakotitalot, tonttikoot 600–1200 m². Kysyntä on tasaista — hyvin valmisteltu kohde menee usein alle kuukaudessa.</p>
      <p><a class="btn" href="kohteet.html">Katso Kukkumäen kohteet</a></p>
    </div>
    <img src="https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=900&q=80" alt="Rauhallinen asuinalue puiden keskellä" width="900" height="675"/>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "alue-centrum.html",
        head("Jyväskylän keskusta | Koti & Kaupunki LKV", "Asuinalue-esittely: Jyväskylän keskusta ja Lutakko.", "styles.css", fonts)
        + hdr("alue-centrum.html")
        + """
<main class="wrap section">
  <p class="eyebrow">Aluesivu · SEO</p>
  <h1 class="page-title">Centrum &amp; Lutakko</h1>
  <div class="split">
    <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=900&q=80" alt="Kaupungin keskustan rakennuksia" width="900" height="675"/>
    <div>
      <p class="muted">Keskusta ja Lutakko houkuttelevat työikäisiä ja sijoittajia: kävelyetäisyys palveluihin, hyvä vuokrakysyntä ja uudempaa kerrostalokantaa.</p>
      <p class="muted">Autamme hinnoittelussa taloyhtiön kunnon, vastikkeiden ja näkymien perusteella — ei vain neliöhinnan.</p>
      <p><a class="btn" href="yhteystiedot.html">Kerro mitä etsit</a></p>
    </div>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "meista.html",
        head("Meistä | Koti & Kaupunki LKV", "Paikallinen kiinteistönvälitys Jyväskylässä.", "styles.css", fonts)
        + hdr("meista.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Meistä</h1>
  <div class="split">
    <div>
      <p class="muted">Koti &amp; Kaupunki LKV perustettiin 2016. Teemme vuodessa noin 80–100 kauppaa — tarpeeksi rutiinia, tarpeeksi pieni jotta vastaamme puhelimeen itse.</p>
      <p class="muted"><strong>Laura Korhonen</strong>, LKV — myynti ja arviot<br/><strong>Janne Virtanen</strong>, LKV — ostajat ja sijoitusasunnot</p>
      <p class="muted">Kuulumme Suomen Kiinteistönvälittäjät ry:hyn. Toimisto Asemakadulla, auki ma–pe 9–17.</p>
    </div>
    <img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=900&q=80" alt="Kaksi ammattilaista keskustelee toimistossa" width="900" height="675"/>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "yhteystiedot.html",
        head("Yhteystiedot | Koti & Kaupunki LKV", "Ota yhteyttä kiinteistönvälittäjään Jyväskylässä.", "styles.css", fonts)
        + hdr("yhteystiedot.html")
        + f"""
<main class="wrap section">
  <div class="split">
    <div>
      <h1 class="page-title">Yhteystiedot</h1>
      <p class="muted">Koti &amp; Kaupunki LKV Oy<br/>Asemakatu 7, 40100 Jyväskylä<br/>+358 40 555 1212<br/>hei@kotikaupunki-example.fi</p>
      <p class="muted">ma–pe 9–17 · näyttöjä myös iltaisin sopimuksen mukaan</p>
    </div>
    <form class="form" action="#" method="get" onsubmit="{FORM_ALERT}">
      <h2 class="page-title" style="font-size:1.45rem">Jätä yhteydenotto</h2>
      <div><label for="n">Nimi *</label><input id="n" required/></div>
      <div><label for="p">Puhelin *</label><input id="p" type="tel" required/></div>
      <div><label for="t">Aihe</label>
        <select id="t"><option>Arviopyyntö (myynti)</option><option>Ostajan yhteydenotto</option><option>Muu</option></select>
      </div>
      <div><label for="m">Viesti *</label><textarea id="m" required placeholder="Asunnon osoite / budjetti / alue…"></textarea></div>
      <button class="btn" type="submit">Lähetä</button>
    </form>
  </div>
</main>
"""
        + foot,
    )


# ---------------------------------------------------------------------------
# 5) RAKENNUS — Rakennus Joki Oy — 6 pages + gallery
# ---------------------------------------------------------------------------
def build_rakennus() -> None:
    d = ROOT / "rakennus-joki"
    css = BANNER_CSS + """
:root{--bg:#1a1a1a;--surface:#242424;--text:#f2efe8;--muted:#a8a29a;--accent:#e85d04;--accent2:#f48c06;--line:#3a3a3a;--display:"Oswald",Impact,sans-serif;--sans:"IBM Plex Sans",system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.65}
img{max-width:100%;display:block;height:auto}a{color:var(--accent2)}
.wrap{max-width:1100px;margin:0 auto;padding:0 1.25rem}
.site-header{background:#111;border-bottom:3px solid var(--accent)}
.header-row{display:flex;align-items:center;justify-content:space-between;padding:1rem 0;gap:1rem;flex-wrap:wrap}
.logo{font-family:var(--display);font-size:1.55rem;letter-spacing:.04em;text-transform:uppercase;color:#fff;text-decoration:none}
nav{display:flex;gap:1.1rem;flex-wrap:wrap}
nav a{text-decoration:none;color:var(--muted);font-weight:500;font-size:.9rem;text-transform:uppercase;letter-spacing:.04em}
nav a[aria-current="page"],nav a:hover{color:var(--accent2)}
.btn{display:inline-flex;padding:.8rem 1.5rem;background:var(--accent);color:#fff!important;text-decoration:none;font-weight:700;border:none;cursor:pointer;font:inherit;text-transform:uppercase;letter-spacing:.06em;font-size:.85rem}
.btn:hover{background:var(--accent2);color:#111!important}
.hero{display:grid;grid-template-columns:1.05fr .95fr;gap:0;min-height:70vh}
.hero-copy{padding:3.5rem 1.25rem;display:flex;flex-direction:column;justify-content:center;max-width:34rem;margin-left:auto}
.hero h1{font-family:var(--display);font-size:clamp(2.6rem,6vw,4rem);line-height:1.05;margin:0 0 1rem;text-transform:uppercase;font-weight:500;letter-spacing:.02em}
.hero p{color:var(--muted);font-size:1.1rem;margin:0 0 1.75rem}
.hero-img{width:100%;height:100%;min-height:320px;object-fit:cover}
.section{padding:3rem 0}
.section h2,.page-title{font-family:var(--display);font-size:2rem;font-weight:500;margin:0 0 1rem;text-transform:uppercase;letter-spacing:.03em}
.page-title{font-size:2.4rem}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.card{background:var(--surface);padding:1.4rem;border-left:3px solid var(--accent)}
.card h3{margin:0 0 .5rem;font-family:var(--display);text-transform:uppercase;font-size:1.1rem;font-weight:500;letter-spacing:.03em}
.card p{margin:0;color:var(--muted);font-size:.95rem}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem}
.gallery img{aspect-ratio:4/3;object-fit:cover;width:100%}
.steps{display:grid;gap:1rem}
.step{display:grid;grid-template-columns:3.5rem 1fr;gap:1rem;align-items:start;background:var(--surface);padding:1.2rem}
.step-num{font-family:var(--display);font-size:2rem;color:var(--accent);line-height:1}
.muted{color:var(--muted)}
.eyebrow{font-family:var(--display);letter-spacing:.14em;text-transform:uppercase;font-size:.8rem;color:var(--accent);margin:0 0 .75rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center}
.site-footer{background:#111;border-top:1px solid var(--line);color:var(--muted);padding:2.5rem 0;margin-top:2rem}
.site-footer a{color:var(--accent2)}
.form{display:grid;gap:.85rem;max-width:34rem}
.form label{font-weight:600;font-size:.9rem;display:block;margin-bottom:.25rem}
.form input,.form textarea,.form select{width:100%;padding:.75rem .85rem;border:1px solid var(--line);font:inherit;background:#111;color:var(--text)}
.form textarea{min-height:8rem}
@media(max-width:850px){.hero,.split,.cards,.gallery{grid-template-columns:1fr}.hero-copy{max-width:none;margin:0}}
"""
    fonts = "https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap"
    links = [
        ("index.html", "Etusivu"),
        ("palvelut.html", "Palvelut"),
        ("referenssit.html", "Referenssit"),
        ("prosessi.html", "Prosessi"),
        ("meista.html", "Meistä"),
        ("tarjous.html", "Tarjous"),
    ]
    b = banner("594 €", "rakennusyrityksen paketti (6 sivua, galleria, SEO)", "../../kotisivut-rakennusyritykselle.html")

    def hdr(cur: str) -> str:
        return f"""{b}<header class="site-header"><div class="wrap header-row">
<a class="logo" href="index.html">Rakennus Joki</a>
<nav aria-label="Päävalikko">{nav_links(links, cur)}</nav>
</div></header>"""

    foot = f"""<footer class="site-footer"><div class="wrap">
<p><strong>Rakennus Joki Oy</strong> · Y-tunnus 4567890-1 · Jyväskylä / Keski-Suomi</p>
<p>Esimerkkirakennusliike Webbuilder-demoa varten. <a href="{ORDER}">Tilaa omat sivut</a></p>
</div></footer></body></html>"""

    write(d / "styles.css", css)
    write(
        d / "index.html",
        head("Rakennus Joki Oy — uudis- ja korjausrakentaminen", "Paikallinen rakennusliike Keski-Suomessa. Tarjouspyyntö verkossa.", "styles.css", fonts)
        + hdr("index.html")
        + """
<main>
<section class="hero">
  <div class="hero-copy wrap" style="padding-left:0;padding-right:0">
    <div style="padding:0 1.25rem;max-width:34rem;margin-left:auto">
      <p class="eyebrow">Rakentaminen · Keski-Suomi</p>
      <h1>Tehdään se kerralla oikein.</h1>
      <p>Uudiskohteet, remontoinnit ja pienet taloyhtiötyöt. Aikataulu, turvallisuus ja selkeä tarjous — ilman turhaa jargon.</p>
      <a class="btn" href="tarjous.html">Pyydä tarjous</a>
    </div>
  </div>
  <img class="hero-img" src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1200&q=80" alt="Rakennustyömaa nostureineen aamuauringossa" width="1200" height="900"/>
</section>
<section class="section wrap">
  <h2>Mitä teemme</h2>
  <div class="cards">
    <article class="card"><h3>Uudisrakentaminen</h3><p>Omakotitalot ja pienet rivitalot avaimet käteen -mallilla.</p></article>
    <article class="card"><h3>Korjaus</h3><p>Märkätilat, julkisivut, katot ja linjasaneerausten osaurakat.</p></article>
    <article class="card"><h3>Taloyhtiöt</h3><p>Kilpailutetut urakat, dokumentointi ja työmaakokoukset.</p></article>
  </div>
</section>
</main>
"""
        + foot,
    )
    write(
        d / "palvelut.html",
        head("Palvelut | Rakennus Joki Oy", "Uudisrakentaminen, korjaus ja taloyhtiöurakat.", "styles.css", fonts)
        + hdr("palvelut.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Palvelut</h1>
  <p class="muted" style="max-width:40rem">Toimimme Jyväskylässä ja noin 80 km säteellä. Urakat 15 000 € – 1,5 M€. Käytämme omia kirvesmiehiä ja vakituisia aliurakoitsijoita.</p>
  <div class="cards" style="margin-top:2rem">
    <article class="card"><h3>Omakotitalot</h3><p>Suunnitteluyhteistyö arkkitehdin kanssa, perustukset, runko, sisätyöt ja piha.</p></article>
    <article class="card"><h3>Märkätilaremontit</h3><p>Vedeneristykset sertifikaatilla, laatat ja kalusteet — yksi vastuullinen urakoitsija.</p></article>
    <article class="card"><h3>Julkisivu &amp; katto</h3><p>Puu- ja tiilijulkisivut, vesikatot, räystäät. Talvi- ja kesätyöt erikseen hinnoiteltuna.</p></article>
  </div>
  <section class="section">
    <h2>Miksi meidät valitaan</h2>
    <p class="muted">Kiinteä hinta tai urakkamuoto sovitaan kirjallisesti. Viikoittainen työmaapäivitys WhatsAppissa tai sähköpostilla. Turvallisuusdokumentit ajan tasalla.</p>
  </section>
</main>
"""
        + foot,
    )
    write(
        d / "referenssit.html",
        head("Referenssit | Rakennus Joki Oy", "Kuvia valmistuneista työmaista ja remonteista.", "styles.css", fonts)
        + hdr("referenssit.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Referenssit</h1>
  <p class="muted">Valikoima valmistuneita kohteita. Klikkaa kuvaa isommaksi omalla laitteellasi — galleria on kevyt ja nopea.</p>
  <div class="gallery" style="margin-top:1.5rem">
    <img src="https://images.unsplash.com/photo-1541888946425-d81bb19240f5?auto=format&fit=crop&w=800&q=80" alt="Työmaa betonivalun aikana" width="800" height="600" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=800&q=80" alt="Moderni omakotitalo valmistumisen jälkeen" width="800" height="600" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=800&q=80" alt="Rakentaja työskentelee työmaalla" width="800" height="600" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=800&q=80" alt="Märkätilaremontti käynnissä" width="800" height="600" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1590496793929-36417d3117de?auto=format&fit=crop&w=800&q=80" alt="Uusi katto asennettuna" width="800" height="600" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1558618666-fcd25c85f82e?auto=format&fit=crop&w=800&q=80" alt="Taloyhtiön julkisivuremontti" width="800" height="600" loading="lazy"/>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "prosessi.html",
        head("Prosessi | Rakennus Joki Oy", "Miten urakka etenee tarjouspyynnöstä luovutukseen.", "styles.css", fonts)
        + hdr("prosessi.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Prosessi</h1>
  <p class="muted">Neljä vaihetta — tiedät aina missä mennään.</p>
  <div class="steps" style="margin-top:1.75rem">
    <div class="step"><div class="step-num">01</div><div><h3 style="margin:0 0 .35rem;font-family:var(--display);text-transform:uppercase">Tarjouspyyntö</h3><p class="muted" style="margin:0">Kerrot kohteen, aikataulun ja budjettihaarukan. Sovitaan katselmus.</p></div></div>
    <div class="step"><div class="step-num">02</div><div><h3 style="margin:0 0 .35rem;font-family:var(--display);text-transform:uppercase">Urakkatarjous</h3><p class="muted" style="margin:0">Saat kirjallisen tarjouksen 5–10 arkipäivässä, eriteltynä työvaiheisiin.</p></div></div>
    <div class="step"><div class="step-num">03</div><div><h3 style="margin:0 0 .35rem;font-family:var(--display);text-transform:uppercase">Työmaa</h3><p class="muted" style="margin:0">Aloituskokous, aikataulu ja viikkopäivitykset. Muutostyöt kirjataan erikseen.</p></div></div>
    <div class="step"><div class="step-num">04</div><div><h3 style="margin:0 0 .35rem;font-family:var(--display);text-transform:uppercase">Luovutus</h3><p class="muted" style="margin:0">Tarkastuslista, dokumentit ja takuu. Jälkikäynti sovitaan tarvittaessa.</p></div></div>
  </div>
  <p style="margin-top:2rem"><a class="btn" href="tarjous.html">Aloita tarjouspyynnöllä</a></p>
</main>
"""
        + foot,
    )
    write(
        d / "meista.html",
        head("Meistä | Rakennus Joki Oy", "Paikallinen rakennusliike vuodesta 2009.", "styles.css", fonts)
        + hdr("meista.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Meistä</h1>
  <div class="split">
    <img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?auto=format&fit=crop&w=900&q=80" alt="Työkalut ja kypärä työmaalla" width="900" height="675"/>
    <div>
      <p class="muted">Rakennus Joki Oy on perheyritys Jyväskylästä. Perustaja <strong>Mika Joki</strong> on rakennusmestari; työmailla on tyypillisesti 8–14 omaa työntekijää.</p>
      <p class="muted">Kuulumme Rakennusteollisuus RT:hen. Vastuuvakuutus ja tilaajavastuutiedot ajan tasalla. Referenssejä saat pyynnöstä myös yhteystietoineen.</p>
      <p class="muted">Toimisto: Sepänkatu 4, 40320 Jyväskylä · ma–pe 7–16.</p>
    </div>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "tarjous.html",
        head("Tarjouspyyntö | Rakennus Joki Oy", "Lähetä tarjouspyyntö rakennusurakasta.", "styles.css", fonts)
        + hdr("tarjous.html")
        + f"""
<main class="wrap section">
  <h1 class="page-title">Tarjouspyyntö</h1>
  <p class="muted" style="max-width:36rem">Kerro kohde ja toiveet. Palaamme 1–2 arkipäivässä ja sovimme katselmuksen. Voit myös soittaa +358 40 222 3344.</p>
  <form class="form" style="margin-top:1.5rem" action="#" method="get" onsubmit="{FORM_ALERT}">
    <div><label for="n">Nimi / yritys *</label><input id="n" required/></div>
    <div><label for="p">Puhelin *</label><input id="p" type="tel" required/></div>
    <div><label for="e">Sähköposti *</label><input id="e" type="email" required/></div>
    <div><label for="t">Urakan tyyppi</label>
      <select id="t"><option>Uudisrakentaminen</option><option>Korjaus / remontti</option><option>Taloyhtiö</option><option>Muu</option></select>
    </div>
    <div><label for="l">Kohteen sijainti</label><input id="l" placeholder="esim. Jyväskylä, Palokka"/></div>
    <div><label for="m">Kuvaus *</label><textarea id="m" required placeholder="Neliöt, aikataulu, budjettihaarukka…"></textarea></div>
    <button class="btn" type="submit">Lähetä tarjouspyyntö</button>
  </form>
</main>
"""
        + foot,
    )


# ---------------------------------------------------------------------------
# 6) LAKI — Asianajotoimisto Meri — 6 pages + EN
# ---------------------------------------------------------------------------
def build_laki() -> None:
    d = ROOT / "meri-laki"
    css = BANNER_CSS + """
:root{--bg:#f3efe6;--surface:#faf7f0;--text:#14261c;--muted:#5a655c;--accent:#1f4d3a;--accent2:#163528;--ink:#0c1a14;--line:#d9d2c4;--display:"Newsreader",Georgia,serif;--sans:"Figtree",system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.7}
img{max-width:100%;display:block;height:auto}a{color:var(--accent)}
.wrap{max-width:1000px;margin:0 auto;padding:0 1.25rem}
.site-header{background:var(--surface);border-bottom:1px solid var(--line)}
.header-row{display:flex;align-items:center;justify-content:space-between;padding:1.15rem 0;gap:1rem;flex-wrap:wrap}
.logo{font-family:var(--display);font-size:1.45rem;color:var(--accent);text-decoration:none;font-weight:500}
nav{display:flex;gap:1.15rem;flex-wrap:wrap;align-items:center}
nav a{text-decoration:none;color:var(--muted);font-weight:500;font-size:.92rem}
nav a[aria-current="page"],nav a:hover{color:var(--accent)}
.lang{margin-left:.35rem;padding-left:.85rem;border-left:1px solid var(--line);font-size:.85rem;font-weight:600}
.lang a{margin:0 .15rem}
.btn{display:inline-flex;padding:.75rem 1.35rem;background:var(--accent);color:#faf7f0!important;text-decoration:none;font-weight:600;border:none;cursor:pointer;font:inherit}
.btn:hover{background:var(--accent2)}
.hero{padding:3.75rem 0 2.5rem;display:grid;grid-template-columns:1.15fr .85fr;gap:2.5rem;align-items:center}
.hero h1{font-family:var(--display);font-size:clamp(2.2rem,4.5vw,3.2rem);line-height:1.15;margin:0 0 1.1rem;font-weight:500}
.hero p{color:var(--muted);font-size:1.1rem;margin:0 0 1.5rem}
.hero-img{aspect-ratio:3/4;object-fit:cover;width:100%;max-height:520px}
.section{padding:2.75rem 0}
.section h2,.page-title{font-family:var(--display);font-size:1.85rem;font-weight:500;margin:0 0 1rem}
.page-title{font-size:2.25rem}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:1.15rem}
.card{background:var(--surface);padding:1.4rem 1.5rem;border:1px solid var(--line)}
.card h3{margin:0 0 .5rem;font-family:var(--display);font-weight:500;font-size:1.2rem}
.card p{margin:0;color:var(--muted)}
.team{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
.team article{display:grid;grid-template-columns:120px 1fr;gap:1.1rem;align-items:center;background:var(--surface);border:1px solid var(--line);padding:1rem}
.team img{width:120px;height:120px;object-fit:cover}
.muted{color:var(--muted)}
.eyebrow{letter-spacing:.14em;text-transform:uppercase;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .75rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:start}
.site-footer{background:var(--ink);color:#b8c4bc;padding:2.5rem 0;margin-top:2.5rem}
.site-footer a{color:#e8efe9}
.form{display:grid;gap:.85rem}
.form label{font-weight:600;font-size:.9rem;display:block;margin-bottom:.25rem}
.form input,.form textarea,.form select{width:100%;padding:.7rem .8rem;border:1px solid var(--line);font:inherit;background:#fff}
.form textarea{min-height:8rem}
.fee-list{list-style:none;padding:0;margin:1.5rem 0 0}
.fee-list li{display:flex;justify-content:space-between;gap:1rem;padding:1rem 0;border-bottom:1px solid var(--line)}
@media(max-width:800px){.hero,.split,.cards,.team{grid-template-columns:1fr}.team article{grid-template-columns:1fr}.hero-img{max-height:360px;aspect-ratio:16/10}}
"""
    fonts = "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=Figtree:wght@400;500;600;700&display=swap"
    links = [
        ("index.html", "Etusivu"),
        ("oikeudenalat.html", "Oikeudenalat"),
        ("tiimi.html", "Tiimi"),
        ("palkkiot.html", "Palkkiot"),
        ("yhteystiedot.html", "Yhteystiedot"),
    ]
    b = banner("883 €", "lakitoimiston paketti (6 sivua, SEO, FI+EN, sisältö)", "../../kotisivut-lakitoimistolle.html")
    b_en = banner("883 €", "lakitoimiston paketti (6 sivua, SEO, FI+EN, sisältö)", "../../../kotisivut-lakitoimistolle.html")

    def hdr(cur: str, prefix: str = "") -> str:
        lang = f'<span class="lang"><a href="{prefix}index.html"{" aria-current=\"page\"" if cur != "en" else ""}>FI</a> | <a href="{prefix}en/index.html"{" aria-current=\"page\"" if cur == "en" else ""}>EN</a></span>'
        nav = nav_links([(prefix + h, t) for h, t in links], prefix + cur if cur != "en" else "")
        return f"""{b if cur != "en" else b_en}<header class="site-header"><div class="wrap header-row">
<a class="logo" href="{prefix}index.html">Asianajotoimisto Meri</a>
<nav aria-label="Päävalikko">{nav}{lang}</nav>
</div></header>"""

    foot = f"""<footer class="site-footer"><div class="wrap">
<p><strong>Asianajotoimisto Meri Oy</strong> · Asianajaja · Helsinki · Y-tunnus 5678901-2</p>
<p style="color:#7a8a80">Esimerkkitoimisto Webbuilder-demoa varten. <a href="{ORDER}">Tilaa omat sivut</a></p>
</div></footer></body></html>"""

    write(d / "styles.css", css)
    write(
        d / "index.html",
        head("Asianajotoimisto Meri — selkeää neuvontaa", "Yritys- ja perheoikeutta Helsingissä. Ensimmäinen keskustelu 30 min.", "styles.css", fonts)
        + hdr("index.html")
        + """
<main>
<section class="wrap hero">
  <div>
    <p class="eyebrow">Asianajotoimisto · Helsinki</p>
    <h1>Oikeudellista selkeyttä ilman turhaa jargonia.</h1>
    <p>Autamme yrityksiä ja yksityishenkilöitä sopimuksissa, työoikeudessa ja perheoikeuden kysymyksissä. Ensimmäinen 30 minuutin kartoitus on kiinteähintainen.</p>
    <a class="btn" href="yhteystiedot.html">Varaa kartoitus</a>
  </div>
  <img class="hero-img" src="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=900&q=80" alt="Lakikirjoja ja asiakirjoja puupöydällä" width="900" height="1200"/>
</section>
<section class="section" style="background:var(--surface);border-block:1px solid var(--line)">
  <div class="wrap">
    <h2>Missä autamme</h2>
    <div class="cards">
      <article class="card"><h3>Yritykset</h3><p>Osakassopimukset, kauppakirjat, GDPR ja työoikeuden päivittäiset kysymykset.</p></article>
      <article class="card"><h3>Yksityiset</h3><p>Avioehto, perunkirjoitus, testamentti ja huoltajuuteen liittyvä neuvonta.</p></article>
      <article class="card"><h3>Riidat</h3><p>Neuvottelu ensin, oikeudenkäynti tarvittaessa — realistinen riskiarvio alusta asti.</p></article>
      <article class="card"><h3>Englanti</h3><p>Palvelemme myös englanniksi. Katso English landing page -sivumme.</p></article>
    </div>
  </div>
</section>
</main>
"""
        + foot,
    )
    write(
        d / "oikeudenalat.html",
        head("Oikeudenalat | Asianajotoimisto Meri", "Yritys-, työ- ja perheoikeus Helsingissä.", "styles.css", fonts)
        + hdr("oikeudenalat.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Oikeudenalat</h1>
  <p class="muted">Emme ole “kaikkea kaikille” -toimisto. Syvennymme näihin alueisiin, jotta neuvonta on käytännöllistä.</p>
  <div class="cards" style="margin-top:1.75rem">
    <article class="card"><h3>Yritysoikeus</h3><p>Yhtiöjärjestykset, osakassopimukset, yrityskaupat ja hallituksen päätöksenteko.</p></article>
    <article class="card"><h3>Sopimukset</h3><p>Toimitus-, lisenssi- ja yhteistyösopimukset. Riskien ja vastuun rajaus selkokielellä.</p></article>
    <article class="card"><h3>Työoikeus</h3><p>Työsopimukset, irtisanomiset, yhteistoiminta ja kilpailukiellot — työnantajille ja työntekijöille.</p></article>
    <article class="card"><h3>Perheoikeus</h3><p>Avioehdot, ositukset, perunkirjoitukset ja testamentit. Emme hoida rikosasioita.</p></article>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "tiimi.html",
        head("Tiimi | Asianajotoimisto Meri", "Asianajajat Meri ja Koljonen.", "styles.css", fonts)
        + hdr("tiimi.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Tiimi</h1>
  <p class="muted">Kaksi asianajajaa, yksi assistentti. Saat aina tutun yhteyshenkilön.</p>
  <div class="team" style="margin-top:1.75rem">
    <article>
      <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=300&q=80" alt="Asianajaja Hanna Meri" width="300" height="300" loading="lazy"/>
      <div>
        <h3 style="margin:0 0 .35rem;font-family:var(--display);font-weight:500">Hanna Meri</h3>
        <p class="muted" style="margin:0;font-size:.95rem">Asianajaja, osakas. Yritys- ja sopimusoikeus. Englanti sujuvasti.</p>
      </div>
    </article>
    <article>
      <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=300&q=80" alt="Asianajaja Antti Koljonen" width="300" height="300" loading="lazy"/>
      <div>
        <h3 style="margin:0 0 .35rem;font-family:var(--display);font-weight:500">Antti Koljonen</h3>
        <p class="muted" style="margin:0;font-size:.95rem">Asianajaja. Työ- ja perheoikeus. Oikeudenkäynnit.</p>
      </div>
    </article>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "palkkiot.html",
        head("Palkkiot | Asianajotoimisto Meri", "Läpinäkyvä hinnoittelu asianajopalveluille.", "styles.css", fonts)
        + hdr("palkkiot.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Palkkiot</h1>
  <p class="muted" style="max-width:38rem">Kerromme arvion ennen työn aloitusta. Tuntihinta tai kiinteä toimeksianto — valitaan tilanteen mukaan. Alv 25,5 % lisätään.</p>
  <ul class="fee-list">
    <li><span>Kartoituskeskustelu 30 min</span><strong>120 €</strong></li>
    <li><span>Asianajajan tuntihinta</span><strong>260 €</strong></li>
    <li><span>Avioehto (kiinteä)</span><strong>alkaen 450 €</strong></li>
    <li><span>Testamentti (kiinteä)</span><strong>alkaen 550 €</strong></li>
    <li><span>Osakassopimus (kiinteä)</span><strong>alkaen 1 800 €</strong></li>
  </ul>
  <p class="muted" style="margin-top:1.5rem">Oikeusturvavakuutus ja maksuton oikeusapu selvitetään tarvittaessa ensimmäisessä keskustelussa.</p>
</main>
"""
        + foot,
    )
    write(
        d / "yhteystiedot.html",
        head("Yhteystiedot | Asianajotoimisto Meri", "Varaa kartoitus tai lähetä viesti.", "styles.css", fonts)
        + hdr("yhteystiedot.html")
        + f"""
<main class="wrap section">
  <div class="split">
    <div>
      <h1 class="page-title">Yhteystiedot</h1>
      <p class="muted">Asianajotoimisto Meri Oy<br/>Bulevardi 12 A 4, 00120 Helsinki<br/>+358 9 4242 1100<br/>toimisto@meri-example.fi</p>
      <p class="muted">ma–pe 9–16 · ajanvarauksella myös etänä</p>
      <p class="muted">Kuulumme Suomen Asianajajaliittoon. Salassapito ja esteellisyystarkistus kuuluvat jokaiseen toimeksiantoon.</p>
    </div>
    <form class="form" action="#" method="get" onsubmit="{FORM_ALERT}">
      <h2 class="page-title" style="font-size:1.4rem">Varaa kartoitus</h2>
      <div><label for="n">Nimi *</label><input id="n" required/></div>
      <div><label for="e">Sähköposti *</label><input id="e" type="email" required/></div>
      <div><label for="p">Puhelin</label><input id="p" type="tel"/></div>
      <div><label for="t">Aihe</label>
        <select id="t"><option>Yritys / sopimus</option><option>Työoikeus</option><option>Perheoikeus</option><option>Muu</option></select>
      </div>
      <div><label for="m">Lyhyt kuvaus *</label><textarea id="m" required placeholder="Älä lähetä salassa pidettäviä liitteitä tähän demoon."></textarea></div>
      <button class="btn" type="submit">Lähetä</button>
    </form>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "en" / "index.html",
        head(
            "Meri Law Office — clear legal advice in Helsinki",
            "Corporate, employment and family law in Helsinki. English available.",
            "../styles.css",
            fonts,
            lang="en",
        )
        + hdr("en", prefix="../")
        + f"""
<main>
<section class="wrap hero">
  <div>
    <p class="eyebrow">Law firm · Helsinki</p>
    <h1>Practical legal advice — without the fog.</h1>
    <p>We advise companies and individuals on contracts, employment matters and family law. A 30-minute scoping call has a fixed fee. Finnish and English.</p>
    <a class="btn" href="../yhteystiedot.html">Book a scoping call</a>
  </div>
  <img class="hero-img" src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=900&q=80" alt="Professional reviewing documents at a desk" width="900" height="1200"/>
</section>
<section class="section wrap">
  <h2>Bilingual structure</h2>
  <p class="muted">This English landing page demonstrates a Webbuilder multilanguage package: shared visual identity, Finnish practice-area pages with substantial content, and a dedicated EN entry for international clients.</p>
  <div class="cards" style="margin-top:1.5rem">
    <article class="card"><h3>Corporate &amp; contracts</h3><p>Shareholder agreements, commercial contracts and day-to-day board questions.</p></article>
    <article class="card"><h3>Employment</h3><p>Employment contracts, terminations and co-operation procedures.</p></article>
    <article class="card"><h3>Family law</h3><p>Prenuptial agreements, estates and wills — clear next steps.</p></article>
    <article class="card"><h3>Fees</h3><p>Hourly or fixed — estimates before work begins. See the Finnish fees page.</p></article>
  </div>
  <p style="margin-top:2rem"><a class="btn" href="../index.html">← Finnish site</a></p>
</section>
</main>
<footer class="site-footer"><div class="wrap">
<p><strong>Asianajotoimisto Meri Oy</strong> · Bulevardi 12 A 4, Helsinki</p>
<p style="color:#7a8a80">Demo firm for Webbuilder. <a href="{ORDER}">Order your own site</a></p>
</div></footer></body></html>
""",
    )


def build_all_rest() -> None:
    ROOT.mkdir(exist_ok=True)
    build_hammas()
    build_lkv()
    build_rakennus()
    build_laki()
    print("Built hammas + lkv + rakennus + laki")


if __name__ == "__main__":
    build_all_rest()
