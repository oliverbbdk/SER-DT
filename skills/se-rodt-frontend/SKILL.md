---
name: se-rodt-frontend
description: "Byg og ret SE RØDT-hjemmesidens responsive frontend. Brug ved navigation, program, filmkort, filterdemo, FAQ og billetvalg i denne festivalopgave."
---

# SE RØDT frontend

Implementér en dansk, brugbar festivalhjemmeside, der følger gruppens godkendte indhold og design. Kerneopgaverne er at forstå konceptet, finde et programpunkt, læse om filteret og vælge billet.

Brugeren har valgt gruppens Figma-design som visuel målestok. Følg dets konkrete layout, farver, typografi og billeder, når de fulde skærme eller designfilen er tilgængelige. Den modtagne filoversigt viser kun miniaturevisninger af `1.png` til `6.png`, så den kan ikke bruges som grundlag for en præcis gengivelse. Bed om fulde eksportbilleder eller et tilgængeligt Figma-link til visuelle detaljer; fortsæt samtidig arbejde, som ikke afhænger af dem.

Seneste direkte ændring: Sidebaggrunden skal være ensfarvet sort uden røde eller bordeauxfarvede striber. SEO og GEO indgår udtrykkeligt i brugerens hjemmesidebestilling.

## Før du vælger løsning

- Undersøg eksisterende projekt, opgavekrav og teknologistak. Bevar den valgte arkitektur. Materialet fastlægger ikke React, Tailwind, WordPress eller andre bestemte teknologier.
- Hvis der ingen kode eller tekniske krav er, så vælg en enkel løsning, gruppen kan forklare og arbejde videre med. Semantisk HTML, CSS og lidt JavaScript er et muligt udgangspunkt.
- Brug eventkonceptet som indholdsgrundlag. Hvis hele skillpakken findes, ligger den samlede oversigt i `../se-rodt-double-diamond/references/opgavegrundlag.md`. Hvis den ikke findes, brug de vedlagte projektkilder; opfind ikke manglende detaljer.
- Fortsæt fra den aktuelle Develop- eller Deliver-fase. En kodeændring kræver ikke, at tidligere research gentages.

## Indhold og struktur

Dæk Forside, Program, Om filteret, Praktisk info, FAQ og Køb billet. Brug sider eller sektioner efter opgavens krav. Primær handling er “Køb billet”, sekundær er “Se programmet”. Hold dato, priser og program i én autoritativ datakilde i projektet, så gentagelser er konsistente.

Brug `lang="da"`, meningsfulde overskrifter, navigation, ét primært `main`-område og korrekte links og knapper. Vigtige fakta skal være rigtig tekst. Brug dato-/tidselementer, når de præcise værdier kendes; et ubekræftet eventår må ikke blive til et ISO-tidsstempel.

## Funktioner

**Navigation:** Alle menupunkter og CTA'er skal nå det rigtige indhold. Mobilmenuen skal kunne åbnes og lukkes med tastatur, have korrekt udvidelsestilstand og en forståelig fokusadfærd. Brug native elementer frem for at give tilfældige elementer knaproller.

**Program:** Dagvalg viser det relevante program og en synlig valgt tilstand. Brug tekst som “Fredag” og “Lørdag”, ikke kun farver. Hold programaften og kalenderdato adskilt: fredag 00:15 er næste kalenderdag; lørdag 01:30 er søndag. Sæt ikke ukendte slutklokkeslæt, salplaceringer eller filmlængder ind som fakta.

**Filmkort:** Vis titel, oplyst år, tidspunkt og eventuelt bekræftet sal. Understøt gyseskala som tal, tekst og ikoner. De konkrete ratings og filmadvarsler er ikke leveret; brug gruppens godkendte data eller markér dem som uafklarede i arbejdsgrundlaget.

**Før/efter-demo:** Brug et mærket native range-input eller en tilsvarende tilgængelig kontrol, så demoen virker med tastatur og touch. Labels må ikke blive skjult, når slideren flyttes. Brug samme motiv på begge sider. Vis tydeligt, hvis billederne kun illustrerer en prototype; en dekorativ farveændring er ikke valideret daltonisering.

**FAQ:** Brug eksempelvis `details` og `summary`, hvis det passer til designet, eller en korrekt implementeret accordion. Spørgsmål og svar skal findes i tekstindholdet.

**Billetvalg:** Vis fredag 299 kr., lørdag 349 kr., festivalpas 549 kr. og VIP 799 kr. Ledsagerrabat er oplyst som 50 kr., men grundbillet og kombinationsregler mangler. VIP-dage er heller ikke fastlagt. Beregn kun beløb med kendte regler. Vis valgt type, antal og beregnet total tydeligt, hvis valg og antal indgår i prototypen.

En skoleprototype skal have et tydeligt demoforløb, hvis der ikke er en rigtig billetintegration. Indsaml ikke kortoplysninger, og fremstil ikke en demobekræftelse som en rigtig billet. En rigtig købsknap kan føre til en godkendt billetudbyder, når den faktiske URL er leveret. Generér ikke en QR-kode, der udgiver sig for at være adgangsgivende.

## Visuel og teknisk kvalitet

- Følg det valgte Figma-design. Brug moodboardet som baggrund, og lad ikke det tidligere paletteforslag i PDF'en tilsidesætte Figma. Hold dekorative teksturer væk fra vigtig tekst.
- Sørg for tydeligt tastaturfokus, labels og fejlbeskeder i tekst. Farve må ikke være eneste informationsbærer.
- Lad layoutet fungere med smalle skærme, forstørret tekst og lange danske ord. Undgå faste højder, som klipper program eller billetvilkår.
- Optimér billeder i relevante størrelser, angiv deres dimensioner, og indlæs billeder længere nede på siden efter behov. Prioriter synligt indhold over dekorative effekter.
- Respektér reduceret bevægelse. Der skal ikke være stroboskop, påtvungen lyd eller en video, som forhindrer adgang til indholdet.
- Integrér sidetitler, beskrivelser og semantisk indhold under implementeringen. Brug kun strukturerede eventdata med kendt år, adresse og andre nødvendige fakta.

## Afslut ændringen

Kør projektets relevante build eller kontrol, og prøv de ændrede brugerforløb i en browser. Kontroller mobil, tastatur og konsistens mellem program og billetter. Rapportér kort, hvad der virker, hvad der er testet, og hvad der fortsat kræver data eller integration. Tilføj ikke et stort testsetup til en lille prototype uden et konkret behov.

Sammenlign implementeringen med de fulde Figma-skærme ved tilsvarende skærmbredde. Kontroller struktur, størrelse, afstande, typografi, billedudsnit og farver. Markér visuel overensstemmelse som ikke verificeret, så længe kun miniatureoversigten findes.

Lever kode og en præcis startkommando, der passer til det faktiske projekt. Publicering indgår kun, når brugeren har bedt om det.
