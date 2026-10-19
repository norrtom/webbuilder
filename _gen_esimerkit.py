#!/usr/bin/env python3
"""Generate 6 distinct example demo sites matching Webbuilder package sizes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "esimerkit"
ORDER = "https://webbuilder.tom-1e4.workers.dev/hinnasto.html#tilaa"
BASE = "https://webbuilder.tom-1e4.workers.dev"

BANNER_CSS = """
.wb-demo-banner{position:sticky;top:0;z-index:1000;background:#111;color:#fff;font-family:system-ui,sans-serif;font-size:.875rem;line-height:1.4}
.wb-demo-banner a{color:#fff;text-decoration:underline}
.wb-demo-banner-inner{max-width:1100px;margin:0 auto;padding:.65rem 1.25rem;display:flex;flex-wrap:wrap;gap:.75rem 1.5rem;align-items:center;justify-content:space-between}
.wb-demo-banner p{margin:0}
.wb-demo-back{white-space:nowrap;text-decoration:none!important;opacity:.85}
.wb-demo-back:hover{opacity:1}
@media(max-width:640px){.wb-demo-banner-inner{flex-direction:column;align-items:flex-start}}
"""


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
    print("wrote", path.relative_to(path.parents[2] if "esimerkit" in str(path) else path.parent))


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
# 1) YRITYS — Aava Konsultointi — 3 pages
# ---------------------------------------------------------------------------
def build_yritys() -> None:
    d = ROOT / "aava-konsultointi"
    css = BANNER_CSS + """
:root{--bg:#f4f6f4;--surface:#fff;--text:#1c2420;--muted:#5a6b62;--accent:#2f5d50;--accent2:#1a3a32;--line:#d5ddd8;--display:"Libre Baskerville",Georgia,serif;--sans:"Source Sans 3",system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.6}
img{max-width:100%;display:block;height:auto}a{color:var(--accent)}
.wrap{max-width:1080px;margin:0 auto;padding:0 1.25rem}
.site-header{background:var(--surface);border-bottom:1px solid var(--line)}
.header-row{display:flex;align-items:center;justify-content:space-between;padding:1rem 0;gap:1rem;flex-wrap:wrap}
.logo{font-family:var(--display);font-size:1.35rem;color:var(--accent2);text-decoration:none}
nav{display:flex;gap:1.25rem;flex-wrap:wrap}
nav a{text-decoration:none;color:var(--muted);font-weight:600;font-size:.95rem}
nav a[aria-current="page"],nav a:hover{color:var(--accent)}
.btn{display:inline-flex;padding:.75rem 1.35rem;background:var(--accent);color:#fff!important;text-decoration:none;font-weight:600;border:none;cursor:pointer;font:inherit}
.btn:hover{background:var(--accent2)}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:2rem;align-items:center;padding:3rem 0 2.5rem}
.hero h1{font-family:var(--display);font-size:clamp(2rem,4vw,3rem);line-height:1.15;margin:0 0 1rem;font-weight:400}
.hero p{color:var(--muted);font-size:1.1rem;margin:0 0 1.5rem}
.hero-img{aspect-ratio:4/3;object-fit:cover;width:100%}
.section{padding:2.75rem 0}
.section h2,.page-title{font-family:var(--display);font-size:1.75rem;font-weight:400;margin:0 0 1rem}
.page-title{font-size:2.25rem}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.card{background:var(--surface);padding:1.35rem;border:1px solid var(--line)}
.card h3{margin:0 0 .5rem;font-size:1.05rem}
.card p{margin:0;color:var(--muted);font-size:.95rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center}
.muted{color:var(--muted)}
.site-footer{background:var(--accent2);color:#d7e3de;padding:2.5rem 0;margin-top:2rem}
.site-footer a{color:#fff}
.form{display:grid;gap:.85rem;max-width:32rem}
.form label{font-weight:600;font-size:.9rem;display:block;margin-bottom:.25rem}
.form input,.form textarea{width:100%;padding:.7rem .8rem;border:1px solid var(--line);font:inherit;background:#fff}
.form textarea{min-height:8rem}
@media(max-width:800px){.hero,.split,.cards{grid-template-columns:1fr}}
"""
    fonts = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital@0;1&family=Source+Sans+3:wght@400;600;700&display=swap"
    links = [("index.html", "Etusivu"), ("palvelut.html", "Palvelut"), ("yhteystiedot.html", "Yhteystiedot")]
    b = banner("299 €", "yrityksen peruspaketti (3 sivua)", "../../kotisivut-yritykselle.html")

    def hdr(cur: str) -> str:
        return f"""{b}<header class="site-header"><div class="wrap header-row">
<a class="logo" href="index.html">Aava Konsultointi</a>
<nav aria-label="Päävalikko">{nav_links(links, cur)}</nav>
</div></header>"""

    foot = f"""<footer class="site-footer"><div class="wrap">
<p><strong>Aava Konsultointi Oy</strong> · Y-tunnus 1234567-8 · Tampere</p>
<p style="color:#a8bbb4">Esimerkkiyritys Webbuilder-demoa varten. <a href="{ORDER}">Tilaa omat sivut</a></p>
</div></footer></body></html>"""

    write(d / "styles.css", css)
    write(
        d / "index.html",
        head("Aava Konsultointi — liikevaihtoa kasvattavaa neuvontaa", "Liikkeenjohdon konsultointi Tampereella.", "styles.css", fonts)
        + hdr("index.html")
        + """
<main>
<section class="wrap hero">
  <div>
    <p class="muted" style="letter-spacing:.08em;text-transform:uppercase;font-size:.8rem;font-weight:700;margin:0 0 .75rem">Konsultointi · Tampere</p>
    <h1>Selkeämpi suunta. Parempi tulos.</h1>
    <p>Autamme kasvavia yrityksiä priorisoimaan oikein: strategia, myyntiputki ja arjen johtaminen ilman konsulttijargonia.</p>
    <a class="btn" href="yhteystiedot.html">Varaa kartoituskeskustelu</a>
  </div>
  <img class="hero-img" src="https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1000&q=80" alt="Neuvotteluhuone" width="1000" height="750"/>
</section>
<section class="section" style="background:#fff;border-block:1px solid var(--line)">
  <div class="wrap">
    <h2>Mihin pureudumme</h2>
    <div class="cards">
      <article class="card"><h3>Strategia 90 päivässä</h3><p>Yksi suunta, kolme mittaria ja realistinen tiekartta johdolle.</p></article>
      <article class="card"><h3>Myynnin rytmi</h3><p>Putken pullonkaulat, tarjousprosessi ja viikkorytmi, jota tiimi jaksaa.</p></article>
      <article class="card"><h3>Operaatiot kuntoon</h3><p>Vastuut, palaverit ja raportointi ilman turhia kerroksia.</p></article>
    </div>
  </div>
</section>
<section class="section wrap split">
  <img src="https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=900&q=80" alt="Tiimityötä" width="900" height="675"/>
  <div>
    <h2>Paikallinen kumppani, ei slide-show</h2>
    <p class="muted">Työskentelemme Tampereen seudun PK-yritysten kanssa. Ensimmäinen kartoitus on 45 minuuttia — saat kirjallisen yhteenvedon samalla viikolla.</p>
    <p><a class="btn" href="palvelut.html">Tutustu palveluihin</a></p>
  </div>
</section>
</main>
"""
        + foot,
    )
    write(
        d / "palvelut.html",
        head("Palvelut | Aava Konsultointi", "Strategia, myynti ja operaatiot.", "styles.css", fonts)
        + hdr("palvelut.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Palvelut</h1>
  <p class="muted">Kaikki toimeksiannot hinnoitellaan kiinteänä projektina tai kuukausipakettina.</p>
  <div class="cards" style="margin-top:2rem">
    <article class="card"><h3>Strategiasprintti</h3><p>2–3 workshopia, analysoitu tilannekuva ja 90 päivän suunnitelma.</p></article>
    <article class="card"><h3>Myyntikoneiston auditointi</h3><p>CRM, tarjoukset ja tapaamisrytmi — priorisoitu korjauslista.</p></article>
    <article class="card"><h3>Johdon sparraus</h3><p>Kuukausittainen sparraus toimitusjohtajalle tai myyntijohtajalle.</p></article>
  </div>
  <section class="section">
    <h2>Kenelle sopii</h2>
    <p class="muted">Liikevaihto tyypillisesti 0,5–15 M€. B2B-palvelut, teollisuus, digitaaliset tuotteet.</p>
  </section>
</main>
"""
        + foot,
    )
    write(
        d / "yhteystiedot.html",
        head("Yhteystiedot | Aava Konsultointi", "Ota yhteyttä Aava Konsultointiin.", "styles.css", fonts)
        + hdr("yhteystiedot.html")
        + f"""
<main class="wrap section">
  <div class="split">
    <div>
      <h1 class="page-title">Yhteystiedot</h1>
      <p class="muted">Aava Konsultointi Oy<br/>Hämeenkatu 12, 33100 Tampere<br/>+358 40 123 4567<br/>hei@aava-example.fi</p>
      <p class="muted">Avoinna ma–pe 9–16</p>
    </div>
    <form class="form" action="#" method="get" onsubmit="event.preventDefault();alert('Esimerkkilomake — tilaa oikeat sivut Webbuilderilta.');">
      <h2 class="page-title" style="font-size:1.5rem">Jätä viesti</h2>
      <div><label for="n">Nimi *</label><input id="n" name="name" required/></div>
      <div><label for="e">Sähköposti *</label><input id="e" name="email" type="email" required/></div>
      <div><label for="m">Miten voimme auttaa? *</label><textarea id="m" name="message" required placeholder="Kerro lyhyesti tilanteesta…"></textarea></div>
      <button class="btn" type="submit">Lähetä</button>
    </form>
  </div>
</main>
"""
        + foot,
    )


# ---------------------------------------------------------------------------
# 2) KAMPAAMO — Studio Lumi — 4 pages + gallery + booking
# ---------------------------------------------------------------------------
def build_kampaamo() -> None:
    d = ROOT / "studio-lumi"
    css = BANNER_CSS + """
:root{--bg:#faf6f2;--surface:#fffaf6;--text:#2a211c;--muted:#7a6a60;--accent:#9a4d3c;--accent2:#6e3428;--line:#e8ddd4;--display:"Cormorant Garamond",Georgia,serif;--sans:"Outfit",system-ui,sans-serif}
*{box-sizing:border-box}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--bg);line-height:1.65}
img{max-width:100%;display:block;height:auto}a{color:var(--accent)}
.wrap{max-width:1040px;margin:0 auto;padding:0 1.25rem}
.site-header{background:transparent;border-bottom:1px solid var(--line)}
.header-row{display:flex;align-items:center;justify-content:space-between;padding:1.1rem 0;gap:1rem;flex-wrap:wrap}
.logo{font-family:var(--display);font-size:1.75rem;font-weight:500;color:var(--text);text-decoration:none;letter-spacing:.02em}
nav{display:flex;gap:1.1rem;flex-wrap:wrap}
nav a{text-decoration:none;color:var(--muted);font-size:.9rem;font-weight:500}
nav a[aria-current="page"],nav a:hover{color:var(--accent)}
.btn{display:inline-flex;padding:.8rem 1.5rem;background:var(--accent);color:#fff!important;text-decoration:none;font-weight:600;border:none;cursor:pointer;font:inherit;border-radius:999px}
.btn:hover{background:var(--accent2)}
.hero{padding:3.5rem 0 2rem;text-align:center}
.hero h1{font-family:var(--display);font-size:clamp(2.5rem,6vw,4rem);font-weight:500;margin:0 0 1rem;line-height:1.1}
.hero p{max-width:34rem;margin:0 auto 1.75rem;color:var(--muted);font-size:1.1rem}
.hero-img{width:100%;aspect-ratio:21/9;object-fit:cover;margin-top:2rem}
.section{padding:2.75rem 0}
.section h2,.page-title{font-family:var(--display);font-size:2rem;font-weight:500;margin:0 0 1rem}
.price-table{width:100%;border-collapse:collapse}
.price-table th,.price-table td{padding:.85rem 0;border-bottom:1px solid var(--line);text-align:left}
.price-table td:last-child{text-align:right;font-weight:600}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem}
.gallery img{aspect-ratio:1;object-fit:cover;width:100%}
.muted{color:var(--muted)}
.site-footer{border-top:1px solid var(--line);padding:2rem 0;margin-top:2rem;color:var(--muted);font-size:.9rem}
.form{display:grid;gap:.85rem;max-width:28rem;margin:0 auto}
.form label{font-weight:600;font-size:.85rem;display:block;margin-bottom:.25rem}
.form input,.form textarea,.form select{width:100%;padding:.7rem .8rem;border:1px solid var(--line);font:inherit;background:#fff;border-radius:.35rem}
.form textarea{min-height:7rem}
@media(max-width:700px){.gallery{grid-template-columns:1fr 1fr}}
"""
    fonts = "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Outfit:wght@400;500;600&display=swap"
    links = [
        ("index.html", "Etusivu"),
        ("palvelut.html", "Palvelut & hinnasto"),
        ("galleria.html", "Galleria"),
        ("ajanvaraus.html", "Ajanvaraus"),
    ]
    b = banner("476 €", "kampaamopaketti (4 sivua, galleria, ajanvaraus)", "../../kotisivut-kampaamolle.html")

    def hdr(cur: str) -> str:
        return f"""{b}<header class="site-header"><div class="wrap header-row">
<a class="logo" href="index.html">Studio Lumi</a>
<nav aria-label="Päävalikko">{nav_links(links, cur)}</nav>
</div></header>"""

    foot = f"""<footer class="site-footer"><div class="wrap">
<p><strong>Studio Lumi</strong> · Hämeenpuisto 8, Tampere · ma–pe 10–18, la 10–15</p>
<p>Esimerkkikampaamo Webbuilder-demoa varten. <a href="{ORDER}">Tilaa omat sivut</a></p>
</div></footer></body></html>"""

    write(d / "styles.css", css)
    write(
        d / "index.html",
        head("Studio Lumi — kampaamo Tampereella", "Leikkaukset, värit ja kampaukset. Varaa aika Studio Lumissa.", "styles.css", fonts)
        + hdr("index.html")
        + """
<main>
<section class="wrap hero">
  <h1>Hiukset, jotka tuntuvat sinulta.</h1>
  <p>Studio Lumi on rauhallinen kampaamo Hämeenpuiston laidalla. Konsultaatio kuuluu aina ensimmäiseen käyntiin.</p>
  <a class="btn" href="ajanvaraus.html">Varaa aika</a>
  <img class="hero-img" src="https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1400&q=80" alt="Kampaamon tuoli" width="1400" height="600"/>
</section>
<section class="section wrap" style="text-align:center">
  <h2>Kenelle</h2>
  <p class="muted" style="max-width:36rem;margin:0 auto">Naiset, miehet ja teinit. Erityisosaaminen: pehmeät värit, kiharat ja matalan ylläpidon leikkaukset.</p>
</section>
</main>
"""
        + foot,
    )
    write(
        d / "palvelut.html",
        head("Palvelut ja hinnasto | Studio Lumi", "Leikkaus, väri ja kampaus — hinnat ja kestot.", "styles.css", fonts)
        + hdr("palvelut.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Palvelut &amp; hinnasto</h1>
  <p class="muted">Hinnat ovat suuntaa-antavia. Lopullinen hinta vahvistetaan konsultaatiossa.</p>
  <table class="price-table" style="margin-top:1.5rem">
    <thead><tr><th>Palvelu</th><th>Kesto</th><th>Hinta</th></tr></thead>
    <tbody>
      <tr><td>Naisten leikkaus</td><td>60–75 min</td><td>48–65 €</td></tr>
      <tr><td>Miesten leikkaus</td><td>45 min</td><td>35–42 €</td></tr>
      <tr><td>Väri / sävytys</td><td>90–150 min</td><td>89–149 €</td></tr>
      <tr><td>Balayage</td><td>2,5–3,5 h</td><td>159–210 €</td></tr>
      <tr><td>Kampaus</td><td>45–60 min</td><td>45–70 €</td></tr>
    </tbody>
  </table>
  <p style="margin-top:2rem"><a class="btn" href="ajanvaraus.html">Varaa aika</a></p>
</main>
"""
        + foot,
    )
    write(
        d / "galleria.html",
        head("Galleria | Studio Lumi", "Tuoreita töitä Studiosta Lumi.", "styles.css", fonts)
        + hdr("galleria.html")
        + """
<main class="wrap section">
  <h1 class="page-title">Galleria</h1>
  <p class="muted">Valikoima tuoreita töitä. Kuvat asiakkaiden luvalla.</p>
  <div class="gallery" style="margin-top:1.5rem">
    <img src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=700&q=80" alt="Hiustyö 1" width="700" height="700" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?auto=format&fit=crop&w=700&q=80" alt="Hiustyö 2" width="700" height="700" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?auto=format&fit=crop&w=700&q=80" alt="Hiustyö 3" width="700" height="700" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1633681926022-84c1035fe4f6?auto=format&fit=crop&w=700&q=80" alt="Hiustyö 4" width="700" height="700" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1519699047748-de8e457a769e?auto=format&fit=crop&w=700&q=80" alt="Hiustyö 5" width="700" height="700" loading="lazy"/>
    <img src="https://images.unsplash.com/photo-1492106087820-71f1a00d2b11?auto=format&fit=crop&w=700&q=80" alt="Hiustyö 6" width="700" height="700" loading="lazy"/>
  </div>
</main>
"""
        + foot,
    )
    write(
        d / "ajanvaraus.html",
        head("Ajanvaraus | Studio Lumi", "Varaa aika kampaamoon — Studio Lumi Tampere.", "styles.css", fonts)
        + hdr("ajanvaraus.html")
        + """
<main class="wrap section" style="text-align:center">
  <h1 class="page-title">Ajanvaraus</h1>
  <p class="muted" style="max-width:28rem;margin:0 auto 1.5rem">Kerro toiveesi ja sopiva ajankohta. Palaamme vahvistukseen saman päivän aikana.</p>
  <form class="form" action="#" method="get" onsubmit="event.preventDefault();alert('Esimerkkilomake — tilaa oikeat sivut Webbuilderilta.');" style="text-align:left">
    <div><label for="n">Nimi *</label><input id="n" required/></div>
    <div><label for="p">Puhelin *</label><input id="p" type="tel" required/></div>
    <div><label for="s">Palvelu</label>
      <select id="s"><option>Leikkaus</option><option>Väri</option><option>Balayage</option><option>Kampaus</option></select>
    </div>
    <div><label for="a">Toivottu aika</label><input id="a" placeholder="esim. pe 14–16"/></div>
    <div><label for="m">Lisätiedot</label><textarea id="m"></textarea></div>
    <button class="btn" type="submit">Lähetä varauspyyntö</button>
  </form>
  <p class="muted" style="margin-top:2rem">Tai soita +358 44 987 6543</p>
</main>
"""
        + foot,
    )


# Remaining sites live in _gen_esimerkit_rest.py
print("part1 helpers loaded")

if __name__ == "__main__":
    from _gen_esimerkit_rest import build_all_rest

    ROOT.mkdir(exist_ok=True)
    build_yritys()
    build_kampaamo()
    print("Built yritys + kampaamo")
    build_all_rest()
