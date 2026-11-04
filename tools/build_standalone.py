from pathlib import Path
from html import escape, unescape
import base64
import json
import mimetypes
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
base = Path(__file__).resolve().parent.parent
source = base/'dist'
output = base/'SE-RODT-aabn-i-browser.html'
routes = {'index.html':'forside','program.html':'program','filter.html':'filter',
          'praktisk.html':'praktisk','faq.html':'faq','billetter.html':'billetter'}
films = json.loads((base/'data/FILMKILDER.json').read_text(encoding='utf-8'))
film_by_id = {item['video_id']:item for item in films}


def data_uri(file):
    mime = mimetypes.guess_type(file.name)[0] or 'application/octet-stream'
    if file.suffix == '.ttf': mime = 'font/ttf'
    content = file.read_text(encoding='utf-8').encode('utf-8') if file.suffix in ('.svg','.txt') else file.read_bytes()
    return 'data:'+mime+';base64,'+base64.b64encode(content).decode('ascii')


previews = {item['video_id']: item.get('thumbnail_url','') for item in films}


def replace_player(match):
    tag = match.group(0)
    video = re.search(r'/embed/([A-Za-z0-9_-]{11})',tag).group(1)
    film = film_by_id[video]
    name = escape(film['film'])
    return (f'<a class="local-trailer-preview" href="{film["url"]}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="Se officiel trailer til {name} på YouTube (åbner i en ny fane)">'
            f'<img src="{escape(previews[video],quote=True)}" width="560" height="315" '
            f'alt="Forhåndsvisning af den officielle trailer til {name}" loading="lazy" '
            'onerror="this.hidden=true">'
            '<span class="local-play" aria-hidden="true">▶</span>'
            '<span class="local-watch">Se trailer på YouTube ↗</span></a>')


def replace_trailer_button(match):
    attributes, content = match.groups()
    video = re.search(r'data-trailer-id="([A-Za-z0-9_-]{11})"',attributes).group(1)
    return (f'<a class="trailer-link" href="https://www.youtube.com/watch?v={video}" '
            f'target="_blank" rel="noopener noreferrer">{content}<span aria-hidden="true">↗</span></a>')


pages = {}
for filename,route in routes.items():
    text = (source/filename).read_text(encoding='utf-8')
    body = re.search(r'<body>([\s\S]*)</body>',text).group(1)
    title = unescape(re.search(r'<title>(.*?)</title>',text).group(1))
    description = unescape(re.search(r'<meta name="description" content="([^"]*)"',text).group(1))
    for name,link in routes.items():
        body = body.replace(f'href="{name}"',f'href="#{link}"')
    body = re.sub(r'<iframe\b[\s\S]*?</iframe>',replace_player,body)
    body = re.sub(r'<button\b([^>]*data-trailer-id[^>]*)>([\s\S]*?)</button>',replace_trailer_button,body)
    for asset in (source/'assets').iterdir():
        if not asset.is_file(): continue
        relative = 'assets/'+asset.name
        if f'"{relative}"' not in body: continue
        replacement = ('https://github.com/google/fonts/blob/main/ofl/creepster/OFL.txt'
                       if asset.name == 'FONT-LICENSE.txt' else data_uri(asset))
        body = body.replace('"'+relative+'"','"'+replacement+'"')
    schema = json.loads(re.search(r'<script type="application/ld\+json">([\s\S]*?)</script>',text).group(1))
    canonical = unescape(re.search(r'<link rel="canonical" href="([^"]*)"',text).group(1))
    pages[route] = {'html':body,'title':title,'description':description,'schema':schema,'canonical':canonical}

css = (source/'styles.css').read_text(encoding='utf-8')
for asset in (source/'assets').iterdir():
    if asset.is_file(): css = css.replace('assets/'+asset.name,data_uri(asset))
css += '''
.local-trailer-preview{display:block;position:relative;width:100%;height:100%;min-height:210px;background:#0d0e12;overflow:hidden;text-decoration:none}
.local-trailer-preview img{width:100%;height:100%;min-height:210px;object-fit:cover;display:block}
.local-play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:grid;place-items:center;width:64px;height:48px;background:#e20020;color:#fff;border-radius:10px;font-size:24px;padding-left:4px}
.local-watch{position:absolute;left:0;right:0;bottom:0;text-align:center;padding:8px 10px;background:#000c;color:#fff;font-size:11px}
.local-trailer-preview:hover .local-play{background:#ff1839}
.local-open-note{font-size:11px;letter-spacing:.02em;text-transform:none;color:#d9c5b9}
'''

app = (source/'app.js').read_text(encoding='utf-8')
app = app.replace("document.addEventListener('keydown'", "pageRoot.addEventListener('keydown'")
app = app.replace("    const address = new URL(location.href);\n    address.searchParams.set('dag', button.dataset.dayButton);\n    history.replaceState({}, '', address);\n",'')
assert 'history.replaceState' not in app
script = '''
const pages = JSON.parse(document.querySelector('#page-data').textContent);
const pageHost = document.querySelector('#site');
let currentRoute = '';
function initializePage(pageRoot) {
'''+app+'''
}
function renderPage() {
  const requested = location.hash.slice(1).split('?')[0];
  if (requested === 'main' && currentRoute) return;
  const route = Object.hasOwn(pages,requested) ? requested : 'forside';
  if (route === currentRoute) return;
  const page = pages[route];
  const pageRoot = document.createElement('div');
  pageRoot.innerHTML = page.html;
  pageHost.replaceChildren(pageRoot);
  currentRoute = route;
  document.title = page.title;
  document.querySelector('meta[name="description"]').content = page.description;
  document.querySelector('link[rel="canonical"]').href = page.canonical;
  document.querySelector('#site-schema').textContent = JSON.stringify(page.schema);
  initializePage(pageRoot);
  window.scrollTo(0,0);
}
window.addEventListener('hashchange', renderPage);
renderPage();
'''
json_data = json.dumps(pages,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
license_text = (source/'assets/FONT-LICENSE.txt').read_text(encoding='utf-8')+'\n\nBEBAS NEUE\n'+(source/'assets/BEBAS-LICENSE.txt').read_text(encoding='utf-8')
document = f'''<!doctype html>
<html lang="da" data-standalone="true"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(pages['forside']['title'])}</title>
<meta name="description" content="{escape(pages['forside']['description'],quote=True)}"><meta name="theme-color" content="#000000">
<link rel="canonical" href="{escape(pages['forside']['canonical'],quote=True)}">
<script type="application/ld+json" id="site-schema">{json.dumps(pages['forside']['schema'],ensure_ascii=False).replace('<',chr(92)+'u003c')}</script>
<link rel="icon" href="{data_uri(source/'assets/favicon.svg')}" type="image/svg+xml">
<style>{css}</style></head><body>
<div id="site"></div><noscript>Aktivér JavaScript for at åbne den samlede hjemmeside.</noscript>
<script type="application/json" id="page-data">{json_data}</script>
<script type="text/plain" id="font-license">{license_text}</script>
<script>{script}</script></body></html>'''
output.write_text(document,encoding='utf-8')
(base/'.build').mkdir(exist_ok=True)
(base/'.build/standalone-app.js').write_text(script,encoding='utf-8')
assert 'src="app.js' not in document and 'href="styles.css' not in document
assert not re.search(r'(?:src|href)="assets/',document)
assert len(pages) == 6
print(f'Enkelt HTML-fil: {output} ({output.stat().st_size} bytes).')
print('Alle seks sider, typografi og egne illustrationer er indlejret. Trailerlinks åbner på YouTube.')
