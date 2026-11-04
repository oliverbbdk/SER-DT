# Designretning fra Figma, moodboard og eventkoncept

## Gruppens valgte Figma-design har forrang

Seneste direkte designvalg: Brugeren ønsker en ensfarvet sort sidebaggrund. Dette går forud for eventuelle røde eller bordeauxfarvede baggrunde i Figma-miniaturer eller moodboardet. Ingen røde baggrundsstriber. Gode kontraster og redundant information er fortsat nødvendige; en sort baggrund validerer ikke alene designets tilgængelighed.

Brugeren har efter den første skillpakke vist en filoversigt og skrevet, at hjemmesiden skal se sådan ud. Denne beslutning erstatter en åben udforskning af det overordnede udtryk: Figma er den primære visuelle reference; moodboardet forklarer inspirationen, og PDF'en beskriver et tidligere koncept.

Den modtagne [oversigt](figma-oversigt.png) viser seks filer, `1.png` til `6.png`, med meget små miniaturebilleder. De fulde filer er ikke vedlagt, og der er ikke modtaget et Figma-link. Filnavnene dokumenterer ikke, hvilken side hver fil viser, eller i hvilken rækkefølge siderne skal bygges. Der kan ikke udledes præcise dimensioner, farvekoder, skrifter, tekstindhold eller responsive regler fra oversigten.

Når fulde skærme eller designfilen modtages, kortlæg deres sider, struktur, komponenter, skrifter, farver, afstande og interaktioner. Følg disse valg ved implementering. Hvis mobilversionen ikke er designet, lav en responsiv tilpasning af det samme udtryk og marker tilpasningsvalgene som fortolkninger. Opfind ikke detaljer og præsenter dem som aflæst fra Figma.

Tilgængelighed vurderes på den faktiske implementering. Bevar designets identitet og håndter konkrete problemer med mindst mulige ændringer frem for at udskifte hele paletten eller layoutet.

## Hvad moodboardet bidrager med

Moodboardet er brugerens collage med gyserfilm på VHS, en ældre skærm med Halloween, biografplakater, publikum, en mørk biografsal, popcorn, papirbilletter, en belyst pil, stjerner, græskar og flagermus. Lys beige papir, sort, rustfarvede kanter, blå, lilla og dæmpede gyldne farver binder collagen sammen.

Brug det som retning for nostalgisk biograf og analogt tryk. Oversæt eksempelvis:

| Reference | Mulig anvendelse på siden |
| --- | --- |
| VHS-rygge og filmplakater | Smalle etiketter, store filmtitler og tydelige programrækker |
| Papirbilletter | Billetkort med diskret perforering og fremhævet pris |
| Biograflys og lysende pil | Tydelig primær handling og enkelte varme lysdetaljer |
| Korn og slidt papir | Svag tekstur på dekorative flader |
| Græskar og flagermus | Få dekorative detaljer uden betydning for navigationen |
| Mørk sal og lærred | Stor hero og tydelig kontrast mellem baggrund og indhold |

Collagens mange lag skal ikke kopieres én til én til hjemmesiden. Gæsten har brug for læsbar rækkefølge og rolige områder til program og billetvalg. Moodboardets film er inspiration; de erstatter ikke festivalens filmprogram.

## Tidligere farveforslag fra PDF'ens side 5

Disse værdier beskriver konceptets udgangspunkt, ikke aflæste Figma-værdier. Brug dem kun, hvor det passer med det valgte design, eller hvor gruppen udtrykkeligt vælger dem.

| Tokenforslag | Farve | Rolle |
| --- | --- | --- |
| `--color-bg` | `#0E0F14` | Mørk baggrund |
| `--color-text` | `#F2EFE6` | Lys tekst |
| `--color-cta` | `#F2B705` | Primær handling, som udgangspunkt med mørk tekst |
| `--color-blue` | `#3A7BD5` | Blå accent; mål kontrast før brug som lille linktekst |
| `--color-purple` | `#4B2E83` | Lilla accentflade |

Blå eller gul er ikke automatisk tilgængelig på alle baggrunde. Kontroller normal, hover, fokus, valgt og fejl. Justér token eller rolle, hvis kontrastkravet ikke nås. Benhvid på næsten sort er et stærkt udgangspunkt, men siger intet om alle de andre kombinationer.

Som praktiske mål bruges mindst 4,5:1 for normal tekst, 3:1 for stor tekst og 3:1 for de visuelle dele af brugerfladen, som er nødvendige for at identificere komponenter og tilstande. Stor tekst betyder her mindst 18 pt, cirka 24 CSS px, eller 14 pt fed, cirka 18,7 CSS px. Tærskler skal anvendes på den faktiske skrift og kontekst.

## Typografi og billeder

Brugeren har oplyst disse kildeområder: [Pinterest](https://dk.pinterest.com/), [Pixabay](https://pixabay.com/da/) og [DaFont Halloween](https://www.dafont.com/theme.php?cat=803). De er ikke specifikke billedlinks eller valgte fontfiler. Kopiér ikke tilfældige billeder og angiv dem som gruppens originale materiale. Registrér de faktiske kilder til indlæste aktiver; en alternativ font eller illustration skal beskrives som et foreløbigt valg i afleveringen.

Fontnavnene i moodboardet er Alter Creed, Deadbeat, Halloween Spooky, Draconis og Denitah Stellar. De er inspirationsmuligheder, ikke vedlagte fontfiler eller et krav om at bruge dem alle. Brug højst få skrifter med et klart hierarki; dekoration og tekst skal have forskellige roller.

Se efter realistiske biografmaterialer, mørke sale og analog filmstemning. Brug brugerleverede eller lovligt tilgængelige billeder med registreret kilde. En fil i moodboardet dokumenterer ikke rettigheder til de enkelte plakater eller figurer. Originale illustrationer eller egne fotos kan udfylde samme visuelle rolle. Få filmplakater og logoer godkendt eller erstattet før offentlig brug, når brugsretten er uafklaret.

Gør dekorative teksturer og flagermus usynlige for hjælpemidler. Beskriv informative billeder med alt-tekst, der passer til deres funktion. Undgå at skrive dato, pris eller vigtig forklaring ind i et billede.

## Filterdemo

Brug to registrerede billeder med identisk motiv, udsnit og dimensioner. Sæt synlige labels på begge tilstande og forklar, hvad demoen viser. Hvis der ikke findes en dokumenteret farvetilpasning, kan en fungerende interaktionsprototype vises som en illustration, tydeligt mærket som sådan. Opfind ikke dokumentation for behandlingens effekt.

## Kilder

- Brugerens Figma-filoversigt, vedlagt som `figma-oversigt.png`; fulde designskærme afventes.
- Brugerens moodboard, vedlagt som `moodboard.png` i samme mappe.
- Brugerens eventkoncept, PDF side 5, for palette og visuel retning.
- [W3C om tekstkontrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- [W3C om kontrast i komponenter og grafik](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
