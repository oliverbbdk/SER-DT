from pathlib import Path
import html
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
base = Path(__file__).resolve().parent.parent
project = base
dist = project / 'dist'
assets = dist / 'assets'
origin = json.loads((project/'data/site.json').read_text(encoding='utf-8'))['origin'].rstrip('/')
assets.mkdir(parents=True, exist_ok=True)
trailers = {item['key']: item for item in json.loads((project/'data/FILMKILDER.json').read_text(encoding='utf-8'))}
festival_films = json.loads((project/'data/FESTIVALDATA.json').read_text(encoding='utf-8'))
film_by_id = {film['id']: film for film in festival_films}

eye = '''<svg viewBox="0 0 500 290" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g fill="none" stroke="#291419" stroke-width="9" stroke-linecap="round"><path d="M65 81 42 47m72 12-8-38m73 23 8-36m67 31 19-31m56 48 29-29m41 57 39-17M60 206l-28 30m78-12-12 38m78-25 9 38m66-39 18 34m63-50 30 28m38-57 42 14"/></g><path d="M20 150Q250-80 480 150Q250 390 20 150Z" fill="#f5e9d2" stroke="#291419" stroke-width="11"/><ellipse cx="250" cy="151" rx="93" ry="110" fill="#ffc348" stroke="#291419" stroke-width="8"/><g stroke="#a65532" stroke-width="3" opacity=".7"><path d="m250 48 0 40m40-31-15 36m43-17-27 28m42-2-33 17m41 16-39 5m32 34-37-10m17 45-30-25m4 48-21-37m-20 46-2-43m-40 34 19-36m-43 18 31-27m-45-4 40-7m-36-36 40 7m-27-42 34 20m-9-48 22 36"/></g><ellipse cx="250" cy="151" rx="43" ry="66" fill="#291419"/><ellipse cx="267" cy="124" rx="13" ry="19" fill="#f5e9d2"/><path d="M57 137q53-46 99-54m190 2q57 13 94 49" fill="none" stroke="#291419" stroke-width="4"/></svg>'''
star = '<svg viewBox="0 0 100 100" fill="currentColor" aria-hidden="true"><path d="m50 0 9 33 33-17-23 28 31 13-34 4 8 35-24-27-24 27 8-35L0 57l31-13L8 16l33 17Z"/></svg>'
logo = f'<a class="logo" href="index.html" aria-label="SE RØDT — forsiden">{eye}<span class="logo-text">SE<br>RØDT</span></a>'
navigation = [('index.html', 'Forside'), ('program.html', 'Program'), ('filter.html', 'Om filteret'),
              ('praktisk.html', 'Praktisk info'), ('faq.html', 'FAQ'), ('billetter.html', 'Køb billet')]


def header(active):
    links = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url == active else '')+
                    (' class="button"' if url == 'billetter.html' else '')+f'>{label}</a>'
                    for url, label in navigation if url != 'index.html')
    return f'''<a class="skip" href="#main">Spring til indhold</a>
<div class="topline">30.–31. oktober &nbsp; · &nbsp; Refshaleøen, København &nbsp; · &nbsp; 18+</div>
<header class="site-header"><div class="wrap nav">{logo}
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-navigation">Menu <span aria-hidden="true">☰</span></button>
<nav class="nav-links" id="main-navigation" aria-label="Hovednavigation">{links}</nav></div></header>'''


def footer():
    trailer_sources = ''.join(f'<li><a href="{item["url"]}" target="_blank" rel="noopener noreferrer">{html.escape(item["film"])} — {html.escape(item["publisher"])}</a></li>' for item in trailers.values())
    links = ''.join(f'<a href="{url}">{label}</a>' for url, label in navigation)
    return f'''<footer class="site-footer"><div class="wrap"><div class="footer-top">
<div>{logo}<p>Endelig ser du det, alle andre skriger over. Gys, film og fællesskab med plads til flere måder at se på.</p></div>
<div><h2>Find vej på siden</h2><nav class="footer-links" aria-label="Navigation i sidefod">{links}</nav></div>
<div><h2>Vi ses i mørket</h2><p>30.–31. oktober<br>Refshaleøen, København<br>For alle fra 18 år</p></div></div>
<div class="footer-bottom"><span>SE RØDT · Et skoleprojekt og festival-koncept. Billetvalg er en demo.</span>
<details class="credits"><summary>Design, illustrationer og kilder</summary><p>Visuel retning: gruppens Figma og moodboard. Gruppens billedinspiration: <a href="https://dk.pinterest.com/">Pinterest</a> og <a href="https://pixabay.com/da/">Pixabay</a>. Øjet og filterillustrationen er tegnet til prototypen. Filmkortene viser officielle trailerafspillere. Film og trailers tilhører deres respektive rettighedshavere; de er ikke angivet som copyright-frie. Typografisk inspiration: <a href="https://www.dafont.com/theme.php?cat=803">DaFont Halloween</a>. Overskrifter: <a href="https://fonts.google.com/specimen/Bebas+Neue">Bebas Neue</a> fra Dharma Type, under <a href="assets/BEBAS-LICENSE.txt">SIL Open Font License</a>. Logo: <a href="https://fonts.google.com/specimen/Creepster">Creepster</a> fra Font Diner, under <a href="assets/FONT-LICENSE.txt">SIL Open Font License</a>.</p><ul class="trailer-credit-list">{trailer_sources}</ul></details></div></div></footer>
<dialog class="dialog trailer-dialog" id="trailer-dialog" aria-labelledby="trailer-dialog-title"><div class="trailer-dialog-header"><h2 id="trailer-dialog-title">Officiel trailer</h2><button type="button" class="trailer-close" id="close-trailer-dialog" aria-label="Luk trailer" autofocus>×</button></div><div class="trailer-stage"><div class="trailer-poster" id="trailer-poster"><span id="trailer-poster-title"></span><img id="trailer-poster-image" alt="" hidden><button class="button" id="retry-trailer" type="button" hidden>Prøv igen</button></div><div class="trailer-frame" id="trailer-frame" hidden></div></div><p id="trailer-status" role="status" aria-live="polite"></p><a class="button trailer-external" id="trailer-external" target="_blank" rel="noopener noreferrer">Se på YouTube ↗</a><p id="trailer-publisher"></p></dialog>'''


def page(filename, title, description, body, extra_schema=None):
    url = origin + '/' + ('' if filename == 'index.html' else filename)
    schema = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebSite', '@id': origin + '/#website', 'url': origin + '/', 'name': 'SE RØDT', 'inLanguage': 'da'},
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title,
         'description': description, 'inLanguage': 'da', 'isPartOf': {'@id': origin + '/#website'}}]}
    if extra_schema:
        schema['@graph'].append(extra_schema)
    document = f'''<!doctype html>
<html lang="da"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(description, quote=True)}">
<meta name="theme-color" content="#000000"><meta name="robots" content="index,follow">
<link rel="canonical" href="{url}"><link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<meta property="og:type" content="website"><meta property="og:locale" content="da_DK"><meta property="og:site_name" content="SE RØDT">
<meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(description, quote=True)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{origin}/assets/social-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="SE RØDT — Halloween-filmfestival, 30.–31. oktober på Refshaleøen">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title, quote=True)}"><meta name="twitter:description" content="{html.escape(description, quote=True)}"><meta name="twitter:image" content="{origin}/assets/social-card.png">
<link rel="preload" as="font" href="assets/bebas-neue.ttf" type="font/ttf" crossorigin><link rel="stylesheet" href="styles.css?v=trailers-6"><script src="app.js?v=trailers-6" defer></script>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head>
<body>{header(filename)}<main id="main">{body}</main>{footer()}</body></html>'''
    (dist / filename).write_text(document, encoding='utf-8')


def intro(label, heading, text):
    return f'<div class="wrap"><div class="page-intro"><p class="eyebrow gold">{label}</p><h1>{heading}</h1><p>{text}</p></div></div>'


def rating(value):
    return f'<div class="rating" aria-label="Gys {value} af 5, foreløbig vurdering"><span class="dots" aria-hidden="true">'+('●' * value)+f'<span class="empty">'+('○' * (5-value))+f'</span></span><span>Gys {value} af 5</span></div>'


def trailer_button(key):
    film = trailers[key]
    return (f'<a class="trailer-link" href="{film["url"]}" target="_blank" rel="noopener noreferrer" data-trailer-id="{film["video_id"]}" '
            f'data-trailer-title="{html.escape(film["film"], quote=True)}" '
            f'data-trailer-thumbnail="{html.escape(film.get("thumbnail_url", ""), quote=True)}" '
            f'data-trailer-publisher="{html.escape(film["publisher"], quote=True)}">'
            f'<span aria-hidden="true">▷</span> Se trailer til {html.escape(film["film"])}</a>')


def film_card(title, year, when, art, description, scare):
    film = trailers[art]
    name = html.escape(title, quote=True)
    return f'''<article class="film-card"><div class="film-media"><a class="trailer-preview" href="{film['url']}" target="_blank" rel="noopener noreferrer" data-trailer-id="{film['video_id']}" data-trailer-title="{name}" data-trailer-publisher="{html.escape(film['publisher'], quote=True)}" data-trailer-thumbnail="{html.escape(film.get('thumbnail_url', ''), quote=True)}" aria-label="Se officiel trailer til {name}"><span class="trailer-poster-label" aria-hidden="true">{html.escape(title)}<small>OFFICIEL TRAILER</small></span><img src="{html.escape(film.get('thumbnail_url', ''), quote=True)}" width="480" height="360" alt="" loading="lazy" onerror="this.hidden=true"><span class="trailer-play" aria-hidden="true">▶</span><span class="trailer-watch">Se trailer <span aria-hidden="true">↗</span></span></a></div><div class="film-info"><span class="film-tag">{when} · {year}</span><h3>{title}</h3><p>{description}</p>{rating(scare)}<a class="trailer-source" href="{film['url']}" target="_blank" rel="noopener noreferrer">Se på YouTube · {html.escape(film['publisher'])} ↗</a></div></article>'''


def closing():
    return '<section class="closing"><p class="eyebrow">Tag en ven med ind i mørket</p><h2>DIN NÆSTE BIOGRAFAFTEN STARTER HER.</h2><p>Vælg én aften, eller bliv til begge. Alle er velkomne fra 18 år.</p><a class="button" href="billetter.html">Find din billet <span class="arrow" aria-hidden="true">↗</span></a></section>'


(assets / 'eye.svg').write_text(eye, encoding='utf-8')
(assets / 'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="20" fill="#000000"/><path d="M8 50Q50 4 92 50Q50 96 8 50Z" fill="#f5e9d2"/><ellipse cx="50" cy="50" rx="22" ry="30" fill="#ffc348"/><ellipse cx="50" cy="50" rx="10" ry="19" fill="#291419"/></svg>', encoding='utf-8')

home = f'''<section class="wrap hero"><div class="hero-copy"><p class="eyebrow gold">Halloween-filmfestival · København</p>
<h1>GYS I ALLE<br><span>FARVER.</span></h1><p>To aftener med klassiske gyserfilm, farvetilpassede visninger og fællesskab. En biografoplevelse med fokus på protanopi — åben for alle fra 18 år.</p>
<div class="actions"><a class="button" href="billetter.html">Køb billet <span class="arrow" aria-hidden="true">↗</span></a><a class="button secondary" href="program.html">Se programmet <span aria-hidden="true">→</span></a></div>
<div class="hero-meta"><span>30.–31. oktober</span><span>Refshaleøen · KBH</span><span>18+</span></div></div>
<div class="hero-art"><div class="eye-ticket"><div class="ticket-top"><span>SE RØDT FILMFESTIVAL</span><span>No. 0031</span></div><div class="big-eye">{eye}</div><p class="ticket-label">DU SER DET.<br>DU MÆRKER DET.</p><div class="ticket-bottom"><span>TO AFTENER I MØRKET</span><strong>30—31 OKT.</strong></div></div><div class="sticker">ALLE<br>ER VELKOMNE</div><div class="small-star">{star}</div></div></section>
<div class="marquee" aria-label="Film, farver og fællesskab"><div class="wrap marquee-inner"><span>KLASSISKE GYS</span><b aria-hidden="true">✦</b><span>SKÆVE FARVER</span><b aria-hidden="true">✦</b><span>ÆGTE FÆLLESSKAB</span><b aria-hidden="true">✦</b><span>SE RØDT</span></div></div>
<section class="section wrap"><div class="section-head"><div><p class="eyebrow gold">På det store lærred</p><h2>KLASSIKERNE.<br>SOM DU HUSKER DEM. NÆSTEN.</h2></div><a href="program.html">Se hele programmet <span aria-hidden="true">↗</span></a></div><div class="film-grid">
{film_card("Don't Look Now", '1973', 'Fredag · 19:00', 'dont-look-now', 'En rød frakke. En mørk hemmelighed. Venedig har aldrig været mere urovækkende.', 3)}
{film_card('The Shining', '1980', 'Fredag · 21:45', 'shining', 'Tjek ind på Overlook Hotel. Det er ikke sikkert, at du har lyst til at blive.', 4)}
{film_card('Carrie', '1976', 'Lørdag · 18:00', 'carrie', 'En skolefest, du aldrig glemmer. Og en klassiker, der stadig rammer.', 4)}</div><p class="fieldset-note" style="margin:16px 0 0">Gyseskalaen er en foreløbig redaktionel vurdering.</p></section>
<section class="wrap section" style="padding-top:0"><div class="split-feature"><div class="feature-graphic"><div class="iris">{eye}</div></div><div class="feature-copy"><p class="eyebrow gold">Samme film. Flere detaljer.</p><h2>HVAD GEMMER<br>SIG I MØRKET?</h2><p>Horrorfilm fortæller også med farver. En frakke, et advarselslys eller en skygge kan være en del af historien.</p><p>SE RØDT undersøger en biografoplevelse, hvor udvalgte farver tilpasses protanopi. Du behøver ikke være farveblind for at være med.</p><a class="text-link" href="filter.html">Forstå idéen bag filteret ↗</a></div></div></section>{closing()}'''
page('index.html', 'SE RØDT | Halloween-filmfestival i København', 'Gyserfilm, farver og fællesskab på Refshaleøen 30.–31. oktober. Udforsk SE RØDT, en Halloween-filmfestival med fokus på protanopi. Se program og priser.', home)

friday = [
    ('18:00', 'Dørene åbner', '', 'Find din plads, få en velkomstdrink og mærk biografstemningen.', None),
    ('18:30', 'Hvad ser du egentlig?', 'INTRO OG DEMO', 'Fælles introduktion med en før/efter-visning på storskærm.', None),
    ('19:00', "Don't Look Now", '1973', 'Den røde frakke er en vigtig detalje i Nicolas Roegs psykologiske gyser.', 3),
    ('21:00', 'Pause, bar og farvequiz', '', 'Vend aftenens første film med de andre gæster.', None),
    ('21:45', 'The Shining', '1980', 'Tilbage til Overlook Hotel, elevatoren og det røde badeværelse.', 4),
    ('00:15', 'Nattevagten', '1994 · LILLE SAL', 'Dansk nattegys efter midnat. Hører til fredagens programaften.', 4)]
saturday = [
    ('16:00', 'I See Red — escape room', 'AKTIVITET', 'Gåder, farver og samarbejde. Konceptet arbejder med tidsbestilte hold.', None),
    ('17:00', 'En anden måde at se på', 'EKSPERT-TALK', 'Talk med optometrist og farveforsker om farver og filmoplevelser.', None),
    ('18:00', 'Carrie', '1976', 'En ikonisk skolefest og en historie om at stå udenfor.', 4),
    ('20:00', 'Kostumekonkurrence og bar', '', 'Kom som du er — eller som noget, de andre helst ikke vil møde i mørket.', None),
    ('21:00', 'Suspiria', '1977', 'Dario Argentos mareridt af stærke farver, dans og snigende uhygge.', 5),
    ('23:00', 'Publikumsvalg', 'CRIMSON PEAK / MIDSOMMAR', 'Publikum vælger mellem Crimson Peak (2015) og Midsommar (2019).', None),
    ('01:30', 'Hvad så du for første gang?', 'ÅBEN MIKROFON', 'Del aftenens oplevelse. Afslutningen ligger efter midnat natten til søndag.', None)]


def rows(data):
    result = []
    for time, title, tag, description, scare in data:
        film = next((item for item in festival_films if item['title'] == title),None)
        if title == 'Publikumsvalg': film = film_by_id['publikumsvalg']
        controls = trailer_button(film['id']) if film and film['id'] in trailers else ''
        if title == 'Publikumsvalg': controls = trailer_button('crimson-peak')+trailer_button('midsommar')
        if controls: controls = '<div class="program-actions">'+controls+'</div>'
        kind = 'film' if film else 'activity'
        level = scare if scare else ''
        result.append(f'<article class="program-row" data-program-entry data-program-kind="{kind}" data-scare="{level}"><div class="program-time">{time}</div><div><h3>{title}'+
                      (f'<span>{tag}</span>' if tag else '')+f'</h3><p>{description}</p>{controls}</div>'+
                      (rating(scare) if scare else '')+'</article>')
    return ''.join(result)


activities = [ ('↔', 'Før & efter', 'Oplev idéen bag farvetilpasningen sammen på lærredet.'),
               ('✦', 'Kostumer & quiz', 'Halloween med humor, filmnørderi og plads til din udklædning.'),
               ('⌁', 'Et roligere hjørne', 'Tag en pause med brætspil, en snak og lidt afstand til lærredet.') ]
program = intro('To aftener. Masser af gys.', 'DIT NÆSTE<br>MARERIDT STARTER HER.', 'Find film, tider og aktiviteter. Vælg din aften — eller oplev begge med et festivalpas.')
program += f'''<div class="wrap page-content"><div class="day-switch" role="group" aria-label="Vælg programaften"><button class="day-button" data-day-button="fredag" aria-pressed="true">Fredag 30. oktober</button><button class="day-button" data-day-button="lordag" aria-pressed="false">Lørdag 31. oktober</button></div>
<div class="program-tools"><div class="program-search"><label for="program-search">Find en film eller aktivitet</label><input id="program-search" type="search" placeholder="Søg fx The Shining" autocomplete="off"></div><div class="program-level"><label for="program-level">Gyseskala</label><select id="program-level"><option value="">Alle niveauer</option><option value="3">3 af 5</option><option value="4">4 af 5</option><option value="5">5 af 5</option></select></div><label class="films-only"><input id="films-only" type="checkbox"> Kun film</label><button class="reset-search" id="reset-search" type="button">Nulstil søgning</button></div><p class="program-match-count" id="program-match-count" role="status" aria-live="polite"></p><p class="program-empty" id="program-empty" hidden>Ingen match på denne aften. Prøv den anden dag, eller nulstil søgningen.</p>
<section data-day-program="fredag" aria-label="Fredagens program"><div class="program-caption"><h2>FØRSTE GANG RØDT</h2><span>Gys 1–5 · Foreløbige redaktionelle vurderinger</span></div>{rows(friday)}</section>
<section data-day-program="lordag" aria-label="Lørdagens program"><div class="program-caption"><h2>HALLOWEEN I FULDE FARVER</h2><span>Gys 1–5 · Foreløbige redaktionelle vurderinger</span></div>{rows(saturday)}<section class="small-hall-program" data-small-hall aria-label="Lørdag i lille sal"><div class="small-hall-heading"><h3>OGSÅ I LILLE SAL</h3><p>Tidspunkter følger</p></div><div class="small-hall-grid"><article data-program-entry data-program-kind="film" data-scare=""><h4>Gæsterne <span>2022</span></h4>{trailer_button('gaesterne')}</article><article data-program-entry data-program-kind="film" data-scare=""><h4>It Follows <span>2014</span></h4>{trailer_button('it-follows')}</article><article data-program-entry data-program-kind="film" data-scare=""><h4>The Witch <span>2015</span></h4>{trailer_button('the-witch')}</article></div></section></section>
<p class="note">Natfilmene hører til den valgte programaften, selvom klokken er efter midnat. Gyseskalaen går fra 1 (let gys) til 5 (intenst). Konkrete filmadvarsler skal fastlægges inden eventet.</p>
<section class="section" style="padding-bottom:0"><p class="eyebrow gold">Der sker også noget uden for lærredet</p><h2>MERE END BARE FILM.</h2><div class="activity-grid">'''
program += ''.join(f'<article class="activity"><span class="icon" aria-hidden="true">{icon}</span><h3>{name}</h3><p>{text}</p></article>' for icon, name, text in activities)
program += '</div></section></div>'+closing()
page('program.html', 'Program og film | SE RØDT Halloween-filmfestival', 'Se film og tidspunkter til SE RØDT: Don’t Look Now, The Shining, Carrie, Suspiria og aktiviteter. Vælg fredag eller lørdag på Refshaleøen.', program)

for mode, accent, secondary in [('original','#be334a','#7a1b35'), ('adapted','#f4c443','#68b6e5')]:
    scene = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="500" viewBox="0 0 900 500"><defs><radialGradient id="light"><stop stop-color="{secondary}" stop-opacity=".6"/><stop offset="1" stop-color="#15232a" stop-opacity="0"/></radialGradient></defs><rect width="900" height="500" fill="#101d29"/><path d="M0 20 330 130v260L0 500Zm900 0L570 130v260l330 110Z" fill="#1e3040"/><g fill="none" stroke="#536575" stroke-width="4"><path d="m30 35 300 102v250L30 486m90-421 220 81v236L120 455m750-420-300 102v250l300 99m-90-421-220 81v236l220 73"/></g><rect x="330" y="130" width="240" height="260" fill="#071019"/><rect x="355" y="150" width="190" height="240" fill="#182b35"/><ellipse cx="450" cy="300" rx="250" ry="230" fill="url(#light)"/><path d="M0 500 330 390h240l330 110Z" fill="#24343d"/><path d="m330 390-40 110m280-110 40 110m-160-110v110" stroke="#52606a" stroke-width="2"/><rect x="120" y="160" width="60" height="80" fill="{accent}"/><rect x="720" y="160" width="60" height="80" fill="{accent}"/><path d="M430 235q20-40 40 0l-2 21 29 95h-94l29-95Z" fill="{accent}"/><path d="m431 350-4 35m42-35 4 35" stroke="#070f18" stroke-width="13"/><path d="M438 235q12-18 24 0l-4 15h-16Z" fill="#0e1924"/><circle cx="450" cy="116" r="10" fill="{accent}"/></svg>'''
    (assets / f'filter-{mode}.svg').write_text(scene, encoding='utf-8')
filter_page = intro('Om idéen bag filteret', 'SAMME FILM.<br>NYE DETALJER.', 'Farver er en del af fortællingen. SE RØDT undersøger, hvordan en tilpasset visning kan gøre udvalgte detaljer lettere at skelne ved protanopi.')
filter_page += f'''<div class="wrap page-content"><div class="filter-top"><div class="filter-copy"><h2>DET HANDLER<br>OM FORSKELLENE.</h2><p>Protanopi er en form for rødblindhed. Nogle farveforskelle kan være svære at se — også når de spiller en rolle i en film.</p><p>Festivalens koncept bruger daltonisering: udvalgte farvenuancer flyttes, så forskelle bliver tydeligere. Det genskaber ikke normalt farvesyn.</p><p>Prøv illustrationen. Den viser princippet med det samme motiv og to forskellige farvevalg.</p></div>
<div class="comparison"><div class="compare-stage"><img src="assets/filter-original.svg" width="900" height="500" alt="Illustration af en mørk korridor med røde detaljer"><img class="compare-after" src="assets/filter-adapted.svg" width="900" height="500" alt="Samme korridor illustreret med gule og blå detaljer"><div class="compare-divider" aria-hidden="true"></div><div class="compare-labels" aria-hidden="true"><span>Original illustration</span><span>Tilpassede farver</span></div></div><div class="compare-controls"><label for="comparison-position">Flyt skellet mellem de to illustrationer</label><input id="comparison-position" type="range" min="0" max="100" value="50" aria-valuetext="50 procent original illustration"><small>Illustration af princippet — ikke en valideret protanopi-simulering eller en demonstration af en færdig filmbehandling. Brug også piletasterne.</small></div></div></div>
<section><div class="section-head"><div><p class="eyebrow gold">Et fællesskab på tværs af farvesyn</p><h2>DU BEHØVER IKKE<br>SE DET SAMME.</h2></div></div><div class="steps"><article class="step"><span class="number">01</span><h3>Forstå forskellen</h3><p>En fælles introduktion forklarer tanken bag tilpasningen før aftenens film.</p></article><article class="step"><span class="number">02</span><h3>Oplev sammen</h3><p>Tag en ven med. Festivalen er åben for alle fra 18 år, uanset farvesyn.</p></article><article class="step"><span class="number">03</span><h3>Tal om det bagefter</h3><p>Del dine oplevelser i pausen, til quizzen eller ved aftenens afslutning.</p></article></div></section></div>{closing()}'''
page('filter.html', 'Om farvefilteret og protanopi | SE RØDT', 'Forstå idéen bag SE RØDT og farvetilpassede gyserfilm til mennesker med protanopi. Prøv en illustrativ før/efter-slider og læs forklaringen.', filter_page)

practical = intro('Alt det, du gerne vil vide først', 'FIND VEJ<br>TIL MØRKET.', 'To aftener på Refshaleøen med film, aktiviteter og pauser. Her finder du de praktiske oplysninger i festival-konceptet.')
practical += '''<div class="wrap page-content"><div class="info-grid"><section class="paper-panel"><p class="eyebrow">Sæt kryds i kalenderen</p><div class="big-date">30—31<br>OKTOBER.</div><p><strong>Refshaleøen, København</strong><br>En rå værkstedshal danner rammen om festivalen.</p><p>Fredag åbner dørene kl. 18:00.<br>Lørdag starter aktiviteterne kl. 16:00.</p><p>Det præcise venue og eventår er endnu ikke fastlagt i skoleprojektets koncept.</p><a class="button" href="program.html">Find din aften <span aria-hidden="true">↗</span></a></section>
<section class="info-box"><h2>EN PLADS TIL ALLE.</h2><dl><dt>Aldersgrænse</dt><dd>18 år. Også gæster uden farveblindhed er velkomne.</dd><dt>Fysisk adgang</dt><dd>Konceptet omfatter niveaufri adgang og handicaptoilet.</dd><dt>Ro og pauser</dt><dd>Roligt pauserum, garderobe og et brætspilshjørne.</dd><dt>To sale</dt><dd>Stor sal med 170 pladser og lille sal med 80 pladser.</dd></dl></section>
<section class="info-box"><h2>REJSEN HERNED.</h2><p>Konceptet lægger op til havnebus, cykelparkering og information om natbus.</p><p>Præcis adresse, stop og aktuelle afgange kommer, når venue og dato er fastlagt. Planlæg også hjemturen: programmet fortsætter efter midnat.</p><p>Vi viser ikke et kort med et ubekræftet mødested.</p></section>
<section class="info-box"><h2>PAUSER MED SMAG.</h2><p>Food trucks og en Halloween-bar er en del af konceptet. Der planlægges vegetariske og veganske muligheder.</p><p>Gå på opdagelse i farvequiz, fotobox, filterstation og historievæg — eller tag en stille pause mellem filmene.</p><p>Udklædning er frivillig. Lørdag er der kostumekonkurrence.</p></section></div><p class="note">Priser: fredag 299 kr. · lørdag 349 kr. · festivalpas 549 kr. · VIP 799 kr. <a href="billetter.html">Se billetmulighederne</a>.</p></div>'''
page('praktisk.html', 'Praktisk info, adgang og transport | SE RØDT', 'Find dato, sted, 18-årsgrænse, adgangsforhold, mad og transportinformation til SE RØDT på Refshaleøen. Læs også om pauserum og biografsale.', practical)

faqs = [
    ('Skal jeg være farveblind for at deltage?', 'Nej. Alle fra 18 år er velkomne. Festival-konceptet er designet med fokus på mennesker med protanopi, men tag gerne en ven med.'),
    ('Hvordan virker farvefilteret?', 'Konceptet bruger daltonisering, som flytter udvalgte farvenuancer, så nogle forskelle bliver tydeligere. Det genskaber ikke normalt farvesyn. Du kan se en illustration af princippet på siden Om filteret.'),
    ('Hvad hvis jeg har en anden type farveblindhed?', 'SE RØDT fokuserer på protanopi. Oplevelsen kan variere, og konceptet lover ikke en bestemt effekt ved andre typer farveblindhed.'),
    ('Hvor uhyggelige er filmene?', 'Programmet blander klassikere og mere intense film. Vi bruger en gyseskala fra 1 til 5 med tal og tekst. Vurderingerne på prototypen er foreløbige redaktionelle forslag.'),
    ('Hvad er aldersgrænsen?', 'Festival-konceptet er for voksne fra 18 år på grund af baren og filmenes indhold.'),
    ('Kan jeg vælge kun én aften?', 'Ja. Konceptets priser er 299 kr. for fredag og 349 kr. for lørdag. Festivalpasset til begge aftener koster 549 kr.'),
    ('Er der mad og drikke?', 'Konceptet omfatter food trucks og en Halloween-bar samt vegetariske og veganske madmuligheder.'),
    ('Skal jeg være udklædt?', 'Nej, udklædning er frivillig. Der er en kostumekonkurrence i lørdagens program.'),
    ('Er der adgang for kørestolsbrugere?', 'Konceptet omfatter niveaufri adgang og handicaptoilet. De konkrete forhold skal bekræftes, når det endelige venue fastlægges.'),
    ('Kan jeg få pengene tilbage?', 'Eventkonceptet foreslår refusion indtil 7 dage før eventet. Denne hjemmeside er en skoleprototype og sælger ikke rigtige billetter; endelige købsvilkår er ikke fastlagt.'),
    ('Hvordan fungerer ledsagerrabatten?', 'Konceptet beskriver 50 kr. i rabat til en ven uden farveblindhed. Det er endnu ikke fastlagt, hvilke billettyper rabatten gælder for, og derfor beregnes den ikke i billetdemoen.'),
    ('Hvordan kommer jeg til festivalen?', 'Festival-konceptet ligger på Refshaleøen i København og lægger op til havnebus, cykelparkering og information om natbus. Præcis adresse og afgange afventer et fastlagt venue og eventår.')]
faq_content = intro('Et godt spørgsmål er en god start', 'SPØRG BARE.<br>VI BIDER IKKE.', 'Her er svar på de mest oplagte spørgsmål om SE RØDT, filteret og din aften i biografen.')
faq_content += '<div class="wrap page-content faq-layout"><section class="faq-list" aria-label="Ofte stillede spørgsmål">'+''.join(f'<details><summary>{html.escape(question)}</summary><p>{html.escape(answer)}</p></details>' for question, answer in faqs)+f'</section><aside class="faq-aside">{eye}<h2>KLAR TIL<br>AT BLIVE SKRÆMT?</h2><p>Se, hvad der venter på lærredet fredag og lørdag.</p><a class="text-link" href="program.html" style="color:var(--ink)">Find en film ↗</a></aside></div>'
faq_schema = {'@type': 'FAQPage', '@id': origin+'/faq.html#faq', 'mainEntity': [
    {'@type': 'Question', 'name': question, 'acceptedAnswer': {'@type': 'Answer', 'text': answer}}
    for question, answer in faqs]}
page('faq.html', 'FAQ — spørgsmål om festival, filter og billetter | SE RØDT', 'Få svar om SE RØDT: protanopi, farvefilter, aldersgrænse, billetpriser, adgangsforhold og udklædning. Alle voksne er velkomne.', faq_content, faq_schema)

tickets = [ ('Fredag', 299, 'Første gang rødt', ['Fredag 30. oktober', 'Film og aftenaktiviteter', 'Dørene åbner kl. 18:00'], 'EN AFTEN I MØRKET'),
            ('Lørdag', 349, 'Halloween-nat', ['Lørdag 31. oktober', 'Film, talk og Halloween', 'Aktiviteter fra kl. 16:00'], 'GYS PÅ HALLOWEEN'),
            ('Festivalpas', 549, 'Hele oplevelsen', ['Begge aftener', 'Fredagens og lørdagens film', 'Spar 99 kr. ift. to enkeltbilletter'], 'TO AFTENER. ÉT PAS.'),
            ('Crimson Pass', 799, 'VIP-oplevelsen', ['Reserveret sæde og drink', 'Goodiebag og meet & greet', 'Gyldighedsdage skal bekræftes'], 'LIDT MERE AF DET HELE') ]
ticket_content = intro('Vælg din plads i mørket', 'HVOR MEGET GYS<br>KAN DU KLARE?', 'Én aften, begge dage eller lidt ekstra. Sammenlign billetmulighederne og prøv dit valg i demoen.')
ticket_content += '<div class="wrap page-content"><form id="ticket-form"><fieldset class="ticket-selection"><legend>Vælg billettype</legend><div class="ticket-grid">'
for name, price, subtitle, benefits, foot in tickets:
    checked = ' checked' if name == 'Festivalpas' else ''
    ticket_content += f'<label class="ticket-option'+(' selected' if checked else '')+f'"><input type="radio" name="ticket" value="{price}" data-name="{name}"{checked}><span class="type-label">{subtitle}</span><h2>{name}</h2><span class="price">{price}<span>KR.</span></span><ul>'+''.join(f'<li>{benefit}</li>' for benefit in benefits)+f'</ul><span class="ticket-foot">{foot}</span></label>'
ticket_content += '''</div></fieldset><div class="order-bar"><label for="quantity">Antal billetter <select id="quantity" name="quantity"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option></select></label><div class="order-total"><small id="selected-ticket">1 × Festivalpas</small><span id="order-total" aria-live="polite" aria-atomic="true">549 kr.</span></div><button class="button" type="submit">Se dit billetvalg <span aria-hidden="true">↗</span></button></div></form>
<p class="order-fine"><strong>Billetdemo:</strong> Der foretages ingen betaling eller reservation. Priserne stammer fra skoleprojektets eventkoncept. En rigtig billetudbyder er ikke tilkoblet.</p><p class="note"><strong>En ven med?</strong> Konceptet beskriver en ledsagerrabat på 50 kr. Reglerne for, hvilke billetter den gælder for, mangler, så rabatten indgår ikke i demoens beregning. VIP's gyldighedsdage skal også fastlægges.</p>
<section class="section" style="padding-bottom:0"><div class="info-grid"><div><p class="eyebrow gold">Godt at vide</p><h2>GYS ER BEDST<br>I FÆLLESSKAB.</h2></div><div><p>Alle er velkomne fra 18 år, også gæster uden farveblindhed. Tag en ven med, og oplev klassikerne sammen.</p><p><a class="text-link" href="faq.html">Få svar om billetter og adgang ↗</a></p></div></div></section></div>
<dialog class="dialog" id="ticket-dialog" aria-labelledby="ticket-dialog-title"><p class="eyebrow gold">Dit valg i billetdemoen</p><h2 id="ticket-dialog-title">EN GOD AFTEN<br>STARTER HER.</h2><p id="demo-selection"></p><p>Dette er en demonstration af billetvalget. Der er ikke bestilt eller reserveret en billet, og der trækkes ingen penge.</p><button type="button" class="button" id="close-ticket-dialog">Tilbage til billetter</button></dialog>'''
page('billetter.html', 'Billetter og priser | SE RØDT Halloween-filmfestival', 'Sammenlign SE RØDTs konceptpriser: fredag 299 kr., lørdag 349 kr., festivalpas 549 kr. og VIP 799 kr. Prøv billetvalg uden betaling.', ticket_content)

urls = ['' if url == 'index.html' else url for url, _ in navigation]
(dist / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{origin}/{url}</loc></url>' for url in urls)+'</urlset>\n', encoding='utf-8')
(dist / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {origin}/sitemap.xml\n', encoding='utf-8')
(project / 'docs/AFLEVERING.txt').write_text('''SE RØDT — hjemmesideprototype

START LOKALT
Kør fra projektmappen: python -m http.server 8765 --directory dist
Åbn derefter http://localhost:8765
Der er ingen pakkedependenser eller buildproces.

INDHOLD
Seks HTML-sider: forside, program, filterforklaring, praktisk info, FAQ og billetter.
Programsøgning, filtrering efter gyseskala og film/aktiviteter, dagvalg,
tastaturbetjent illustrationsslider og billetdemo med antal og samlet pris.
Der er ingen Min aften-funktion eller gemte film.
Danske sidetitler, beskrivelser, canonical, Open Graph, sitemap og robots.txt.
WebSite/WebPage-JSON-LD og FAQPage-data, der svarer til den synlige FAQ.

STATUS OG MANGLENDE INPUT
Visuelt er siden en foreløbig fortolkning af gruppens Figma-miniaturer.
De fulde 1.png–6.png eller et Figma-link mangler stadig.
Gruppens konkrete Pinterest/Pixabay-billeder og DaFont-fontfiler mangler.
Forsiden viser forhåndsvisninger fra de officielle YouTube-trailers.
Ni film har verificerede kildelinks og trailerknapper i programmet.
Der er ikke indsat en trailer til Nattevagten, fordi en passende officiel kilde ikke er verificeret.
De konkrete kilder og udgivere står i FILMKILDER.json og sidens kildeoversigt.
Webversionen indlæser udbyderens afspiller efter klik. Forhåndsvisninger hentes hos YouTube.
Der gemmes ingen kopier af videoerne eller filmplakater. Direkte trailerlinks er altid tilgængelige.
Materialet er ikke angivet som copyright-frit. Mulig alders-/regionsbegrænsning styres af YouTube.
Øje og filterillustration er tegnet til prototypen. Creepster og Bebas Neue har vedlagte OFL-licenser.
Filmratings er foreløbige redaktionelle forslag og skal godkendes af gruppen.
Filterdemoen er en illustration af princippet, ikke valideret daltonisering.
Eventår, venueadresse, VIP-dage og ledsagerrabattens regler er uafklarede.
Der sælges ikke billetter. Ingen personoplysninger eller betaling indsamles.
Event-JSON-LD er udeladt, fordi eventår og præcis adresse ikke er fastlagt.
Det private Sites-link er til review; ekstern SEO/GEO-synlighed kræver offentlig adgang.
Sidens schema og metadata lover ikke placeringer, rich results eller AI-citater.

DOUBLE DIAMOND
Discover/Define: Leveret koncept og brugerens designvalg er anvendt som arbejdsgrundlag.
Der er ikke gennemført interviews, persona-research eller brugertests i dette arbejde.
Develop: Fungerende responsiv prototype med seks sider og centrale interaktioner.
Deliver: JavaScript-syntaks, lokale links, billeder, unikke sidetitler og beskrivelser,
JSON-LD, FAQ-overensstemmelse, SVG og sitemap er kontrolleret.
Browserkontrol: alle seks sider uden vandret overflow ved 320 CSS px;
programskift, 2 lørdagsbilletter = 698 kr., demodialog, FAQ, slider med piletast,
mobilmenu med Escape/fokus og desktopforside ved 1440 px er gennemgået.
Ingen browserkonsolfejl blev registreret i den kontrollerede session.
Baggrunden er efter brugerens ønske ensfarvet sort uden røde striber.
Dette er teknisk kontrol, ikke en gennemført brugertest med målgruppen.
Opdatering med filmtrailers: Ni kilder er kontrolleret via YouTubes oEmbed-endpoint.
De tre forsidespillere indlæser de officielle filmvisninger; The Shining-afspilning
blev observeret frem til 20 sekunder med en varighed på 55 sekunder.
Trailerpopup, Escape, fokusretur og fjernelse af iframe ved lukning er testet.
Forside og popup er gentestet ved 320 CSS px uden vandret overflow.
Lørdagens syv trailerknapper samt fredagens to matcher kildelisten.
En efterfølgende alders-/regionsbegrænsning hos udbyderen kan ikke udelukkes.
Professionel gennemgang: Bebas Neue til overskrifter, roligere typografi,
ensartede komponenter, mere luft og tydeligere hierarki på alle seks sider.
Min aften og gemte film er udeladt efter brugerens præcisering.
Programsøgning, nulstilling, tomt søgeresultat, gyseskala og Kun film er testet.
Kontrol: Shining giver ét resultat fredag, gys 4 giver to fredag og ét lørdag,
og Gæsterne findes korrekt i lørdagens lille sal. Mobil ved 320 CSS px er
kontrolleret på alle seks sider uden vandret overflow.
Den samlede HTML-fil er strukturelt kontrolleret og har bestået JS-syntakskontrol.
Direkte file://-åbning kan ikke testes i Codex-browseren på grund af dens URL-politik.

RETTELSE 4. NOVEMBER 2026
Brugeren oplevede sorte trailerfelter. Fejlen blev ikke reproduceret i lokal browserkontrol.
Forsiden viser nu billeder og links i stedet for at vente på tre indlejrede afspillere.
Der indlæses kun en afspiller efter klik, med eksplicit referrer og origin.
YouTube-fejl, manglende API og tidsgrænser viser en forklaring, en forhåndsvisning
og det fortsat tilgængelige YouTube-link. Den samlede HTML-fil bruger direkte links.
Alle ni officielle kilder og forhåndsvisnings-URL'er er kontrolleret via oEmbed igen.
Lokal browserkontrol: The Shining afspiller, alle tre forsidebilleder er indlæst,
programlink åbner korrekt film, Escape lukker og returnerer fokus, afspiller fjernes.
Dialogen er gentestet ved 320 CSS px; dialogens scrollbredde matcher klientbredden.
Målrettet test med simuleret udbyder kontrollerer fejl 153, API-fejl, indlæsnings-
og afspilningstimeout, lukning under indlæsning og direkte links i den samlede HTML-fil.
Adgang til den udgivne side viser login i denne browsersession; produktionsafspilning
er derfor ikke UI-verificeret. Siden er fortsat ejerprivat efter kontrol af adgangspolitikken.
SEO-GEO-kontrol.html forklarer kodekontrol, schema-validering og senere effektmåling.
SEO-metadata og JSON-LD følger nu også med den samlede HTML-fil og dens seks visninger.


KILDER
Gruppens SE_RODT_eventide.pdf, moodboard og Figma-filoversigt.
Gruppens angivne inspirationskilder: https://dk.pinterest.com/ og https://pixabay.com/da/
Typografisk inspiration: https://www.dafont.com/theme.php?cat=803
Anvendt font: https://github.com/google/fonts/tree/main/ofl/creepster
SEO/AI: https://developers.google.com/search/docs/appearance/ai-features
''', encoding='utf-8')

print('Bygget: seks statiske sider, SVG-illustrationer og SEO-filer. CSS og JavaScript bevares.')
