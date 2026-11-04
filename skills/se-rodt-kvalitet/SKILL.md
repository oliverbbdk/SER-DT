---
name: se-rodt-kvalitet
description: "Test SE RØDT-hjemmesidens brugerforløb, mobilvisning og tilgængelighed for protanopi. Brug ved evaluering i Deliver, fejlrettelser og kontrol før aflevering."
---

# SE RØDT kvalitet og evaluering

Kontrollér, at det afleverede produkt svarer til gruppens faktiske krav og valgte design. Knyt evalueringen til Define-fasens succeskriterier og de spørgsmål, som prototyperne skulle afklare. Brug [kontrolplanen](references/kontrolplan.md) efter behov.

Det visuelle mål er gruppens Figma-design. Sammenlign med de fulde designskærme ved tilsvarende bredde, og registrér konkrete forskelle i layout, typografi, billeder, farver og afstande. De fulde skærme er endnu ikke modtaget; filoversigtens miniaturevisninger kan ikke dokumentere præcis visuel overensstemmelse.

## Undersøg før du konkluderer

- Find projektets startkommando og eksisterende checks. Åbn den aktuelle version i en browser, når browseradgang er tilgængelig.
- Beskriv præcist, hvilken version og hvilke sider eller forløb der er undersøgt. Genbrug eksisterende testresultater, når de stadig gælder.
- Skeln mellem gennemført teknisk kontrol, egen visuel vurdering, farvesimulering og brugertest. Hvis noget ikke kunne køres, skal det stå som ikke testet.

## De vigtigste forløb

1. En gæst forstår konceptet og finder dato, sted og aldersgrænse.
2. Gæsten skifter mellem dagene, finder en film og aflæser tid og gyseskala uden kun at bruge farve.
3. Gæsten forstår, hvad filterdemoen viser, og kan betjene den med tastatur.
4. Gæsten finder praktiske oplysninger og et relevant FAQ-svar.
5. Gæsten vælger en billet og ser pris og eventuel total. Et demoforløb er tydeligt angivet.

## Tilgængelighed og mobil

- Gennemgå med tastatur fra siden åbnes: navigation, mobilmenu, dagvalg, slider, FAQ og billetvalg. Fokus skal være synligt og må ikke blive fanget eller skjult.
- Undersøg farveafhængighed, herunder valgt tilstand, fejl, billetter, sale og gyseskala. Prøv også i gråtoner og med protanopi-simulering, når et værktøj er tilgængeligt.
- Mål kontrast i den faktiske UI. Brug eksempelvis `python scripts/contrast.py '#F2EFE6' '#0E0F14'` til ensfarvet, uigennemsigtig tekst og baggrund. Ved billeder, gennemsigtighed og gradienter skal den sammensatte baggrund og svageste relevante område måles særskilt.
- Kontroller tekstkontrast, nødvendige komponentgrænser og fokus i deres kontekst. En enkelt bestået måling dokumenterer ikke WCAG-overensstemmelse for hele siden.
- Kontroller 320 CSS px bredde, almindelig mobil og desktop samt forstørret tekst og zoom. Undgå klippet indhold og unødvendig vandret rulning.
- Prøv reduceret bevægelse og kontroller, at dekorative effekter ikke blinker eller skjuler indhold.

## Faktakontrol og levering

Sammenlign datoer, program, priser og vilkår med godkendt indhold. Kontrollér især tidspunkter efter midnat, lørdagens lille sal uden oplyste tider, uafklarede ratings, VIP-vilkår og ledsagerrabat. Der må ikke optræde et opdigtet eventår, adresse eller lagerstatus.

Kontroller relevante sidetitler, tekstindhold og konsistens mellem synlige oplysninger og eventuel JSON-LD. Kør build og projektets relevante checks. Ret reproducerbare fejl inden for opgaven, og gentest de berørte forløb.

Rapportér få, konkrete fund med placering, reproduktion, brugerbetydning og anbefalet rettelse. Skeln mellem blokeringer, forbedringer og ukendte forhold. En testrapport må aldrig hævde, at tests med rigtige deltagere er gennemført, hvis det kun var AI'ens egen gennemgang.

I Deliver dokumenteres kæden problem → ændring → gentest. Gennemfør kun brugerundersøgelser, som faktisk er mulige; giv ellers gruppen en klar testplan og behold teststatus åben.
