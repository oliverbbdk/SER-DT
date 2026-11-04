# SE RØDT – SER-DT

En responsiv, dansk hjemmeside til et skoleprojekt om en Halloween-filmfestival på Refshaleøen i København. Festivalidéen handler om gyserfilm, fællesskab og en biografoplevelse med fokus på protanopi, også kaldet rødblindhed.

Projektet indeholder både hele kildekoden og **én HTML-fil, der kan åbnes direkte i en browser**. Det kan åbnes og redigeres i PhpStorm. Hjemmesiden bruger HTML, CSS og JavaScript og kræver ingen PHP-server, database, npm-installation eller betalt tjeneste for at kunne vises lokalt.

Dette er en prototype: billetvalget er en demo, og filterillustrationen er ikke et dokumenteret hjælpemiddel mod farveblindhed.

## Kom hurtigt i gang

### Bare se hjemmesiden

1. Pak ZIP-filen ud.
2. Åbn `SE-RODT-aabn-i-browser.html` i projektmappen med din browser.
3. Brug menuen til at skifte mellem de seks sider.

HTML-filen indeholder JavaScript, CSS, fonte og egne illustrationer. Filmtrailers åbner på YouTube, og trailerbilleder hentes derfra, så de kræver internet. Navigation, filterdemo og billetdemo fungerer uden en lokal server. JavaScript skal være aktiveret.

Den samlede HTML-fil er en genereret visningskopi. Redigér webkilderne nedenfor, og generér den igen, når I vil dele en opdateret udgave.

### Åbn projektet i PhpStorm

1. Vælg **File → Open** i PhpStorm.
2. Vælg hele mappen `SER-DT`, hvor denne README ligger.
3. Start med `README.md`, `dist/index.html`, `dist/styles.css` og `dist/app.js`.

Mappen er allerede et Git-repository på branchen `main`, når den pakkes ud fra den komplette ZIP eller klones fra GitHub. PhpStorms lokale arbejdsindstillinger ligger under `.idea/` og er ignoreret af Git.

Gruppens repository er [oliverbbdk/SER-DT](https://github.com/oliverbbdk/SER-DT). Hent det med **Get from Version Control** i PhpStorm eller:

```sh
git clone https://github.com/oliverbbdk/SER-DT.git
```

For at arbejde med webversionen kan I bruge PhpStorms **Open in Browser** på `dist/index.html`, eller starte en lille server fra projektmappen:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Åbn derefter <http://127.0.0.1:8765/>. Hvis jeres computer bruger kommandoen `python3`, bruges den i stedet for `python`. Stop serveren med Ctrl+C. Serveren viser kun indholdet i `dist/`.

## Hvad de seks sider gør

| Side | Fil | Indhold og funktioner |
| --- | --- | --- |
| Forside | `dist/index.html` | Festivalens idé, dato, sted, aldersgrænse, tre filmkort og adgang til program og billetter. |
| Program | `dist/program.html` | Fredag/lørdag, klokkeslæt, film, aktiviteter, programsøgning, gyseskala, “Kun film” og officielle trailerlinks. |
| Om filteret | `dist/filter.html` | Forklarer protanopi og konceptet. En slider viser en illustreret før/efter-sammenligning. |
| Praktisk info | `dist/praktisk.html` | Kendte oplysninger om stedet, adgang, alder og forhold, der fortsat skal afklares. |
| FAQ | `dist/faq.html` | Korte spørgsmål og svar i elementer, der kan foldes ud. |
| Billetter | `dist/billetter.html` | Billetvalg, antal og samlet pris. Bekræftelsen er tydeligt en demo uden betaling. |

Menu, sidefod og centrale festivaloplysninger går igen på siderne. Sort baggrund, lyse tekster, gyldne detaljer og tydeligt tastaturfokus understøtter det valgte udtryk. Logoet bruger Creepster, overskrifter bruger Bebas Neue, og brødtekst bruger systemfonten Arial eller en tilsvarende sans serif.

## Projektets filer

```text
SER-DT/
├── README.md
├── SE-RODT-aabn-i-browser.html    Den samlede fil til hurtig fremvisning
├── .git/                        Lokal Git-historik i den komplette ZIP
├── .gitignore
├── .gitattributes
├── .editorconfig
├── requirements-dev.txt         Kun til valgfri generering af delingsbillede
├── data/
│   ├── site.json                Webdomænet til canonical, sitemap og schema
│   ├── FESTIVALDATA.json         Film-id'er, programdata og foreløbige gys-vurderinger
│   └── FILMKILDER.json           Officielle trailerlinks, udgivere og billed-URL'er
├── dist/                        Webversionen – klar til en statisk webserver
│   ├── index.html
│   ├── program.html
│   ├── filter.html
│   ├── praktisk.html
│   ├── faq.html
│   ├── billetter.html
│   ├── styles.css
│   ├── app.js
│   ├── robots.txt
│   ├── sitemap.xml
│   └── assets/                  SVG, fonte, fontlicenser og delingsbillede
├── docs/
│   ├── SEO-GEO-kontrol.html      Læsbar kontrolvejledning med sidernes metadata
│   ├── AFLEVERING.txt            Tidligere teknisk kontrol og kendte begrænsninger
│   └── KILDESTATUS.md            Oprindelse og version af gruppeafleveringen
├── skills/                      Fem AI-skills med projektets arbejdsgrundlag
└── tools/                       Portable bygge- og kontrolscripts
```

### HTML, CSS og JavaScript

HTML beskriver sidernes struktur, tekster, navigation, formularer og metadata. CSS står for farver, typografi, afstande, komponenter og mobiltilpasning. JavaScript i `dist/app.js` styrer mobilmenu, dagvalg, programsøgning, filter-slider, billetberegning og trailerdialog.

Der er ingen backend. Valg og priser behandles i browseren. Der oprettes ingen rigtig booking, og der indsamles ikke betalingsoplysninger. Der er heller ingen “Min aften”, gemte film eller konto på selve prototypen.

### Hvor skal vi redigere?

| Ændring | Sted |
| --- | --- |
| Farver, layout, skrifter og mobilvisning | `dist/styles.css` |
| Interaktioner og beregninger | `dist/app.js` |
| Fælles navigation, sidefod, HTML-indhold og metadata | `tools/build_site.py` |
| Film-id'er og gys-vurderinger | `data/FESTIVALDATA.json` |
| Trailere, officielle udgivere og forhåndsvisninger | `data/FILMKILDER.json` |
| Domæne til SEO-URL'er | `data/site.json` |

De seks HTML-sider er genereret fra `tools/build_site.py`. I kan åbne dem og ændre dem direkte, men næste kørsel af det script overskriver HTML-ændringerne. Lav derfor varige HTML- og tekstændringer i generatoren. CSS og JavaScript bliver bevaret ved genbygning.

**Vigtigt om data:** `FESTIVALDATA.json` er et arbejdsgrundlag, som generatoren bruger til bl.a. filmidentifikation og gys-vurderinger. Ikke alle gentagne felter bliver automatisk læst derfra. Klokkeslæt, billetpriser og flere tekster står også i generatoren. Søg efter den gamle værdi i hele projektet, og kontroller de relevante sider efter en ændring. En centralisering af alle festivaloplysninger kan være en senere forbedring.

## Generér en opdateret fremvisningsfil

Python-scripts bruger kun standardbiblioteket, undtagen det valgfrie script til delingsbilledet. Kør fra projektmappen efter jeres ændringer:

```sh
python tools/build_site.py
python tools/build_standalone.py
python tools/build_seo_report.py
python tools/check_site.py
python tools/check_delivery.py
```

Dette genbygger websidernes HTML, opdaterer den samlede HTML-fil og SEO/GEO-kontrollen og kontrollerer links, metadata og leverancen. `tools/build_standalone.py` læser altid den aktuelle CSS og JavaScript fra `dist/`, så også rene designændringer skal følges af dette script, før I sender HTML-filen videre.

Hvis I vil opdatere delingsbilledet:

```sh
python -m pip install -r requirements-dev.txt
python tools/build_social_card.py
```

Det bruger Pillow og de vedlagte fonte. Det færdige billede findes allerede i `dist/assets/social-card.png`; der kræves ingen installation for at bruge hjemmesiden.

Der findes en særskilt test af trailerfejl, som kræver Node.js:

```sh
node tools/test_trailer_failure.cjs
```

En valgfri kildeopdatering kan køres med `python tools/refresh_trailers.py`. Den kontakter YouTubes oEmbed-endpoint og opdaterer metadata i `data/FILMKILDER.json`; den downloader ingen videofiler. Kør bagefter byggekommandoerne ovenfor.

## SEO – hvordan siden bliver forståelig for søgemaskiner

SEO betyder **Search Engine Optimization**, altså søgemaskineoptimering. På denne hjemmeside er det indarbejdet i kildekoden og indholdet:

| Del | Hvad vi har gjort | Hvor det findes |
| --- | --- | --- |
| Sidetitel | Hver side har en forskellig titel, der passer til indholdet. | `<title>` i de seks HTML-filer |
| Beskrivelse | Hver side har sin egen korte beskrivelse. | `<meta name="description">` |
| Læsbart indhold | Festivalfakta findes som rigtig tekst, med én hovedoverskrift på hver side. | `<main>`, `<h1>`, afsnit og links |
| Intern navigation | Menu, filmkort, CTA'er og sidefod forbinder siderne. | HTML-links mellem siderne |
| Canonical | Angiver den foretrukne webadresse for den enkelte side. | `<link rel="canonical">` |
| Strukturerede data | Beskriver website, webside og de synlige FAQ-svar. | `<script type="application/ld+json">` |
| Sitemap | Oplister webversionens seks sideadresser. | `dist/sitemap.xml` |
| Robots | Indeholder crawl-instruktion og henvisning til sitemap. | `dist/robots.txt` |
| Deling | Titel, beskrivelse og delingsbillede til tjenester, der bruger disse metadata. | Open Graph- og Twitter-metadata |

Eksempel på sidetitel: `Program og film | SE RØDT Halloween-filmfestival`. Søgemaskinen afgør selv, hvordan et søgeresultat bliver vist; den er ikke bundet til at bruge vores titel og beskrivelse ordret.

Schema er JSON-LD med typerne `WebSite` og `WebPage`. FAQ-siden har også `FAQPage`, der matcher sidens synlige spørgsmål og svar. `Event` er bevidst udeladt: eventåret og den præcise adresse er ikke oplyst og skal ikke opfindes for at udfylde et schema.

Domænet læses fra `data/site.json`. Hvis I senere flytter hjemmesiden, opdateres det dér, hvorefter HTML, sitemap og fremvisningsfil genbygges. Det udgivne Sites-link var ejerprivat ved den seneste kontrol. `robots.txt` og `index,follow` ophæver ikke et login. En fil på jeres computer bliver heller ikke til et offentligt søgeresultat.

### Sådan kontrollerer vi SEO

Åbn `docs/SEO-GEO-kontrol.html` for en oversigt over alle seks siders faktiske metadata. I kan også åbne HTML-koden i PhpStorm og søge efter `title`, `description`, `canonical` og `application/ld+json`.

Indsæt kildekoden i [Schema Markup Validator](https://validator.schema.org/) for at kontrollere schema. Efter en offentlig lancering kan ejeren verificere hjemmesiden i [Google Search Console](https://search.google.com/search-console/) og bruge URL-inspektion, sitemap og effektivitetsrapporten til at følge indeksering, visninger, klik og søgeord.

**Status:** Implementeringen er kontrolleret. Søgeplaceringer og trafik er ikke målt. Selv en teknisk gyldig offentlig side er ikke garanteret indeksering. Se [Googles tekniske krav](https://developers.google.com/search/docs/essentials/technical).

## GEO – hvordan indholdet kan bruges i AI-søgning

GEO betyder her **Generative Engine Optimization**. Det handler om at gøre hjemmesidens oplysninger forståelige og brugbare for søgetjenester med AI. “GO” i projektets beskrivelse forstås her som GEO.

Vi arbejder med direkte svar på gæstens spørgsmål: Hvad er SE RØDT? Hvor foregår det? Hvem kan komme? Hvad koster det? Hvordan fungerer idéen med filteret? Svarene findes som tekst, og fakta skal være ens på tværs af siderne. Ukendte oplysninger bliver angivet som uafklarede.

Google oplyser, at de almindelige SEO-principper også gælder for deres AI Overviews og AI Mode, uden en særlig AI-fil eller ekstra schema. Det giver ikke en garanti for omtale, og andre AI-tjenester kan fungere anderledes. [Googles vejledning om AI-søgning](https://developers.google.com/search/docs/appearance/ai-features).

Efter offentlig lancering kan I afprøve spørgsmål som “Hvad koster en billet til SE RØDT?”. Notér tjeneste, dato, spørgsmål, svar og det link, der faktisk citeres. Et svar alene dokumenterer ikke, at AI'en har brugt vores side. At give tjenesten linket direkte tester, om den kan læse siden; det tester ikke, om den selv finder os.

**Status:** Indholdet er struktureret til at være let at forstå. Der er ikke dokumenteret AI-citater eller en målt GEO-effekt. Der findes ingen indbygget knap, der gør os synlige i alle AI-tjenester.

En præcis formulering til afleveringen er:

> Vi har implementeret teknisk SEO med metadata, semantisk HTML, intern navigation, sitemap og strukturerede data. GEO-arbejdet bygger på klare festivalfakta og korte, konsistente svar. Implementeringen er kontrolleret, men effekten i søgemaskiner og AI-søgning er ikke målt, da prototypen fortsat er privat.

## Trailere, billeder og tilgængelighed

Forsiden viser forhåndsvisninger fra officielle trailers til Don't Look Now, The Shining og Carrie. Filmkort og program indeholder rigtige YouTube-links. Webversionen forsøger at vise en officiel afspiller i en dialog efter klik og viser en forklaring samt et direkte link, hvis indlæsning eller afspilning fejler. Lukning fjerner afspilleren og returnerer fokus.

Den samlede HTML-fil åbner trailers direkte på YouTube, da indlejring fra en lokal fil kan være begrænset. YouTube styrer region-, alder- og andre afspilningsbegrænsninger. Der er ni verificerede officielle kilder; Nattevagten har ikke fået en trailer, fordi en egnet officiel kilde ikke blev verificeret.

Film og trailers er ophavsretligt beskyttede og tilhører deres rettighedshavere. Der ligger ingen kopier af film eller filmplakater i projektet. Pinterest, Pixabay og DaFont var inspirationskilder. Det originale øje og før/efter-illustrationen ligger lokalt som SVG. Fontlicenserne følger med under `dist/assets/`.

Farve er ikke eneste signal for valgt programdag eller gyseskala. Siden bruger tekstlabels, tal, native formularfelter og tastaturfokus. Layoutet tilpasses mobil, og reduceret bevægelse respekteres. Filter-slideren er en illustration af idéen, ikke en valideret protanopi-simulation. Den tekniske kontrol er heller ikke en erklæring om fuld WCAG-overensstemmelse.

## Double Diamond og hvad der mangler

| Fase | Arbejdet i dette projekt |
| --- | --- |
| Discover | Gruppens koncept, moodboard og Figma-filoversigt giver arbejdsgrundlaget. Der er ikke gennemført interviews som del af dette arbejde. |
| Define | Fokus er en forståelig festivaloplevelse: find koncept, program, filterforklaring, praktiske svar og billetvalg. |
| Develop | Seks sider, responsivt design og fungerende prototypeinteraktioner er bygget og justeret efter brugerens ønsker. |
| Deliver | Kode, navigation, mobilforløb, metadata og trailerhåndtering er kontrolleret. Målgruppens brugertest og offentlig effektmåling mangler. |

Gyseskalaen er foreløbige redaktionelle forslag. Eventår, præcis venueadresse, VIP-billettens dage og ledsagerrabattens kombinationsregler er uafklarede. Ingen af de oplysninger er opfundet. Visninger efter midnat hører til den relevante programaften, selv om kalenderdatoen er skiftet.

Figma-grundlaget var kun en miniatureoversigt over seks skærme. En præcis visuel sammenligning kræver de fulde skærme eller Figma-filen. Se de fem skills under `skills/` for proces, designretning, frontend, SEO/GEO og kvalitet. `skills/START-HER.txt` forklarer brugen.

Tidligere udførte kontroller står i `docs/AFLEVERING.txt`: bl.a. programfiltre, billetberegning, slider, mobilmenu, FAQ, trailerafspilning og layout ved 320 CSS px. Direkte `file://`-åbning er ikke browserautomatiseret i Codex på grund af browserens URL-politik; fremvisningsfilen er struktur- og syntakskontrolleret.

## Git og samarbejde i gruppen

Den lokale Git-historik starter med denne samlede gruppeaflevering. Første commit bruger den neutrale forfatter `SE RODT projektgruppe` med en ikke-leverbar eksempeladresse; der er ikke konfigureret en fælles identitet til jeres fremtidige commits. Hver person bruger sit eget navn og sin egen Git-identitet.

Den komplette ZIP indeholder projektets `.git/`-mappe. Derudover følger en separat `SER-DT.bundle` med Git-historikken. Hvis en platform eller ZIP-udpakker skjuler `.git/`, kan bundle-filen genskabe repositoryet:

```sh
git clone SER-DT.bundle SER-DT
```

Åbn derefter den nye mappe i PhpStorm. En bundle kan bruges uden GitHub og internet. Den er en delbar kopi på et bestemt tidspunkt; den synkroniserer ikke automatisk gruppens ændringer.

For løbende samarbejde bruges [gruppens fælles GitHub-repository](https://github.com/oliverbbdk/SER-DT). En klon fra GitHub har allerede den rigtige `origin`. Kontrollér forbindelsen med:

```sh
git remote -v
git pull --ff-only
```

En klon fra bundle-filen får automatisk en `origin`, der peger på selve bundle-filen. Erstat den med GitHub-adressen, når I vil synkronisere online:

```sh
git remote set-url origin https://github.com/oliverbbdk/SER-DT.git
git push -u origin main
```

Repositoryet blev oprettet som offentligt af ejeren. Alle kan hente filerne; gruppemedlemmer skal have skriveadgang fra ejeren for at kunne pushe direkte. Adgangen til den eksisterende, private Sites-hjemmeside er en separat indstilling.

En enkel arbejdsgang er at hente nyeste `main`, oprette en branch til sin ændring, teste og sende en pull request. Undgå at redigere de samme områder samtidig. Git ignorerer IDE-caches, virtuelle miljøer og lokale hemmeligheder, men beholder de færdige webfiler og fremvisningsfilen, så alle kan åbne projektet med det samme.

## Offentligt web og drift

`dist/` kan lægges på en almindelig statisk webserver. PHP og en database er ikke nødvendige. Denne kopi indeholder ingen automatiske deployment-nøgler. En Git-commit udgiver derfor ikke automatisk ændringer på det eksisterende Sites-link.

Før en rigtig lancering skal gruppen afklare eventfakta, billetudbyder, adgangsforhold og selve publiceringen. Opdatér `data/site.json` til det endelige domæne, hvis I flytter siden, og genbyg filerne. Kontrollér derefter offentlig adgang, links og schema på det faktiske domæne.
