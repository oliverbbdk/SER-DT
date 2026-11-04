# Kontrolplan til aflevering

Brug de relevante punkter til den aktuelle ændring. Dette er et forslag til kontrol, ikke lærerens vurderingskriterier eller dokumentation for gennemførte tests.

## Tekniske og redaktionelle kontroller

| Område | Observerbart resultat |
| --- | --- |
| Forside | Koncept, 30.–31. oktober, Refshaleøen, 18+ og handlinger er lette at finde |
| Navigation | Links og CTA'er når det tilsigtede indhold, også fra mobilmenuen |
| Program | Begge dage virker; tider og titler matcher indholdsgrundlaget |
| Natprogram | 00:15 fredag og 01:30 lørdag placeres korrekt efter midnat |
| Lille sal lørdag | Ukendte tider fremstilles ikke som bekræftede |
| Gyseskala | Intensitet har tekst og tal; ratings har en kendt redaktionel status |
| Filterdemo | Både pointer, touch og tastatur kan bruges; tilstande forklares korrekt |
| Billetter | 299 / 349 / 549 / 799 kr. vises konsistent; ukendte rabatvilkår opfindes ikke |
| Demo | Ingen rigtig betaling, adgangsgivende QR eller falsk billetbekræftelse |
| FAQ | Spørgsmål og svar er tilgængelig tekst og kan åbnes med tastatur |
| Mobil og zoom | Indholdet kan læses og betjenes uden klipning og overlap |
| Tilgængelighed | Farve er suppleret, fokus ses, controls har navne, kontrast er målt |
| SEO og GEO | Metadata passer til siden; fakta er konsistente; schema matcher synlig tekst |
| Åbne fakta | År, adresse, billedrettigheder og integrationer har korrekt status |
| Drift | Den oplyste startkommando virker; relevante buildchecks er kørt |

## Forslag til brugertest i Deliver

Giv deltageren en opgave uden at vise, hvor svaret er. Notér, hvad personen gør, hvor personen tøver, om opgaven lykkes, og hvilken hjælp der eventuelt gives. Indhent ikke helbredsoplysninger, som testen ikke har behov for.

Mulige opgaver:

- “Du overvejer at tage en ven med. Find ud af, om I begge må komme, og hvad en lørdagsbillet koster.”
- “Find tidspunktet for The Shining og læs, hvordan filmens intensitet præsenteres.”
- “Find ud af, hvad filteret ændrer, og prøv demonstrationen.”
- “Du vil købe billet til begge aftener. Vælg den relevante billet og find prisen.”
- “Du har behov for niveaufri adgang. Find information om stedet.”

Sæt mål og registreringsmetode før testen. Brug eksempelvis opgaveløsning, behov for hjælp, fejl og forståelse af filteret; skriv kun tid og citater ind, hvis de faktisk er observeret. Hvis testpersonen ikke har protanopi, kan testen belyse generel brugbarhed, men den validerer ikke alene løsningen for protanopi.

## Dokumentation af et fund

Registrér problemets placering, trin til reproduktion, forventet adfærd, faktisk adfærd, betydning for brugeren, foreslået eller udført rettelse og genteststatus. Brug gruppens eksisterende format; en kort tabel er ofte nok.

Bevar skellet mellem en planlagt test, et faktisk resultat og en fortolkning. En farveblindhedssimulator eller en automatisk audit er ikke en rigtig bruger med protanopi.

## Kontrastværktøjets grænser

`scripts/contrast.py` beregner WCAG's kontrastforhold for to uigennemsigtige sRGB-hex-farver. Som standard afprøves 4,5:1; brug `--minimum 3` til en relevant 3:1-vurdering. Værktøjet afgør ikke selv, om en tekst er stor, eller om kriteriet gælder i den konkrete UI. Det analyserer ikke skærmbilleder, farvesyn, fokusforløb, bevægelse, semantik eller hele hjemmesidens tilgængelighed.

Kilder: [W3C om tekstkontrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) og [W3C om komponentkontrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
