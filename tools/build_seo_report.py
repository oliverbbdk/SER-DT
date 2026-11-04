from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json

base=Path(__file__).resolve().parent.parent
source=base/'dist'
origin=json.loads((base/'data/site.json').read_text(encoding='utf-8'))['origin'].rstrip('/')

class Head(HTMLParser):
    def __init__(self):
        super().__init__();self.title='';self.description='';self.canonical='';self.h1='';self.types=[];self.mode=None;self.schema=''
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag in ('title','h1'):self.mode=tag
        if tag=='meta' and attrs.get('name')=='description':self.description=attrs['content']
        if tag=='link' and attrs.get('rel')=='canonical':self.canonical=attrs['href']
        if tag=='script' and attrs.get('type')=='application/ld+json':self.mode='schema';self.schema=''
    def handle_data(self,data):
        if self.mode=='title':self.title+=data
        if self.mode=='h1':self.h1+=data
        if self.mode=='schema':self.schema+=data
    def handle_endtag(self,tag):
        if tag in ('title','h1'):self.mode=None
        if tag=='script' and self.mode=='schema':
            self.types.extend(item['@type'] for item in json.loads(self.schema)['@graph']);self.mode=None

rows=[]
for filename in ['index.html','program.html','filter.html','praktisk.html','faq.html','billetter.html']:
    head=Head();head.feed((source/filename).read_text(encoding='utf-8'))
    rows.append(f'<tr><th scope="row"><a href="{head.canonical}">{escape(filename)}</a></th><td><strong>{escape(head.title)}</strong><p>{escape(head.description)}</p><small>H1: {escape(head.h1)}</small></td><td>{", ".join(head.types)}</td></tr>')

report='''<!doctype html><html lang="da"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SE RØDT – sådan tjekker I SEO og GEO</title>
<style>body{margin:0;background:#f5f3ec;color:#202124;font:16px/1.7 Arial,sans-serif}main{max-width:1050px;margin:auto;padding:48px 24px 80px}h1{font-size:clamp(30px,5vw,48px);line-height:1.15;margin:12px 0 24px}h2{font-size:24px;margin:38px 0 12px}a{color:#12478a}p{max-width:84ch}.tag{font-size:12px;letter-spacing:.12em;text-transform:uppercase}.status{border-left:5px solid #986300;background:#fff5d9;padding:18px 22px}.table-wrap{overflow:auto}table{width:100%;border-collapse:collapse;background:white;font-size:14px}th,td{text-align:left;padding:15px;vertical-align:top;border-bottom:1px solid #ddd}th{min-width:110px}td p{margin:8px 0;font-size:13px}small{color:#51565d}code{background:#e7e6e0;padding:2px 5px;border-radius:3px;overflow-wrap:anywhere}li{margin-bottom:12px}footer{margin-top:45px;font-size:13px;border-top:1px solid #ccc;padding-top:18px}</style></head><body><main>
<p class="tag">SE RØDT · teknisk kontrol · 4. november 2026</p><h1>Sådan tjekker I SEO og GEO</h1>
<div class="status"><strong>Koden er forberedt. Søgesynligheden er endnu ikke dokumenteret.</strong><br>Det udgivne Sites-link er stadig privat for ejeren. Google og andre eksterne tjenester kan derfor ikke læse selve hjemmesiden gennem login. En HTML-fil på jeres computer bliver heller ikke indekseret som en offentlig hjemmeside.</div>
<h2>1. Se SEO direkte i koden</h2><p>Åbn en af de seks HTML-filer fra hjemmesidens ZIP i en teksteditor. På den udgivne side kan I også bruge <strong>Vis sidens kilde</strong> eller <strong>Ctrl+U</strong> i en almindelig browser, efter I er logget ind. Søg efter:</p>
<ul><li><code>&lt;title&gt;</code>: sidens unikke titel, som søgemaskinen kan bruge som udgangspunkt.</li><li><code>name="description"</code>: en kort beskrivelse af netop den side.</li><li><code>rel="canonical"</code>: den foretrukne URL på det udgivne domæne.</li><li><code>application/ld+json</code>: strukturerede data om siden. FAQ-siden har også <code>FAQPage</code>, som matcher de synlige spørgsmål og svar.</li></ul>
<p>Den samlede fil <code>SE-RODT-aabn-i-browser.html</code> indeholder de samme metadata og schema for alle seks visninger. Den opdaterer dem med JavaScript, når I skifter side. De seks separate HTML-sider i ZIP-filen er den statiske webversion og det bedste grundlag for denne kodekontrol.</p>
<h2>2. Det er faktisk implementeret</h2><p>Alle seks sider har én hovedoverskrift, dansk sprogkode, forskellige titler og beskrivelser, canonical og strukturerede data. Lokale links, schema-JSON og overensstemmelsen mellem FAQ og FAQ-markup er kontrolleret automatisk. Det dokumenterer implementeringen; det er ikke en måling af Google-placeringer.</p>
<div class="table-wrap"><table><thead><tr><th>Side</th><th>Titel, beskrivelse og hovedoverskrift</th><th>Schema-typer</th></tr></thead><tbody>'''+''.join(rows)+'''</tbody></table></div>
<p>Der findes også <a href="'''+origin+'''/sitemap.xml">sitemap.xml</a> og <a href="'''+origin+'''/robots.txt">robots.txt</a> på webversionen. De ophæver ikke det private login. Event-markup er udskudt, fordi eventåret og den præcise adresse ikke er oplyst.</p>
<h2>3. Sådan kontrollerer I strukturerede data nu</h2><p>Brug <a href="https://validator.schema.org/">Schema Markup Validator</a>, vælg kodeindtastning, og indsæt kildekoden fra f.eks. <code>faq.html</code>. Det kan kontrollere schema uden at skulle logge ind på jeres private side. Google henviser til dette værktøj til generel schema-validering. Et gyldigt schema er ikke en garanti for et særligt søgeresultat.</p>
<h2>4. Sådan måler I SEO efter offentlig lancering</h2><ol><li>Hjemmesiden skal først være offentligt tilgængelig uden login. Adgangen er ikke ændret i denne rettelse.</li><li>Tilføj og verificér ejerskabet i <a href="https://search.google.com/search-console/">Google Search Console</a>.</li><li>Brug <strong>URL-inspektion</strong> på den præcise sideadresse. Se om Google kan hente siden, og om den er indekseret. Indsend sitemap, når den offentlige version er klar.</li><li>Følg visninger, klik og søgeord i rapporten <strong>Effektivitet</strong> over tid. Ingen målinger fra Search Console er foretaget i dette projekt.</li></ol>
<h2>5. Sådan vurderer I GEO</h2><p>GEO betyder her, at indholdet er forståeligt og brugbart for AI-baseret søgning. På jeres side ligger grundlaget i korte svar, tydelige oplysninger om koncept, sted, dato, målgruppe og priser samt ens fakta på tværs af siderne. Google oplyser, at almindelig SEO også gælder for AI Overviews og AI Mode; der kræves ikke en særlig AI-fil eller ekstra schema.</p>
<p>Efter en offentlig lancering kan I undersøge konkrete spørgsmål i søgetjenester med AI, f.eks. <em>“Hvad er SE RØDT?”</em> eller <em>“Hvad koster billetter til SE RØDT?”</em>. Registrér dato, tjeneste, spørgsmål, svar og den kildeadresse, der faktisk citeres. Et svar er kun dokumentation for en henvisning til jeres side, når tjenesten faktisk linker til den. Resultater kan variere. At give AI'en linket direkte tester læsbarhed, ikke om den selv finder jer.</p>
<p>Der er ikke dokumenteret AI-citater eller søgeplaceringer for siden. Google kræver, at sider er indekserede og egnede til almindelige søgeresultater for at kunne bruges som støttende links i deres AI-søgefunktioner. Omtale er stadig ikke garanteret.</p>
<h2>Formulering til jeres aflevering</h2><p><em>“Vi har implementeret teknisk SEO med unikke metadata, semantisk HTML, intern navigation, sitemap og strukturerede data. Vores GEO-arbejde bygger på tydelige festivalfakta og korte, konsistente svar. Implementeringen er kontrolleret, men effekt i søgemaskiner og AI-søgning er ikke målt, da prototypen fortsat er privat.”</em></p>
<footer>Officielle kilder: <a href="https://developers.google.com/search/docs/appearance/ai-features">Google: AI features and your website</a> · <a href="https://developers.google.com/search/docs/essentials/technical">Tekniske krav</a> · <a href="https://support.google.com/webmasters/answer/9012289">URL-inspektion</a> · <a href="https://developers.google.com/search/docs/appearance/structured-data">Schema-testværktøjer</a>. Kontrolleret 4. november 2026.</footer>
</main></body></html>'''
(base/'docs/SEO-GEO-kontrol.html').write_text(report,encoding='utf-8')
print('SEO/GEO guide created with actual metadata from all six pages.')
