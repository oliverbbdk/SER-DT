---
name: se-rodt-seo-geo
description: "Skriv og implementér SEO og GEO til SE RØDT. Brug ved søgeord, metadata, synlige festivalfakta, FAQ, intern navigation og strukturerede data til søgemaskiner og AI-søgning."
---

# SE RØDT SEO og GEO

Gør festivalens indhold nemt at finde og forstå for mennesker, søgemaskiner og AI-søgetjenester. GEO betyder her Generative Engine Optimization, ikke geografisk lokalisering. Begynd med tydeligt indhold og almindelig teknisk SEO; lov ikke bestemte placeringer, AI-citater eller synlighed.

Læs [søge- og indholdsgrundlaget](references/soegegrundlag.md), når du udarbejder metadata, FAQ eller strukturerede data. Tjek aktuelle officielle retningslinjer, når du implementerer features, der afhænger af en søgetjenestes regler.

## Indhold og søgeintention

- Prioritér dansk: Halloween-filmfestival i København, gyserfilm, rødblindhed, protanopi og en tilgængelig biografoplevelse. Brug ordene, hvor de hjælper gæsten; undgå gentagelser for søgeordenes skyld.
- Besvar konkrete spørgsmål: Hvad er SE RØDT? Hvem kan komme? Hvornår er det? Hvad koster det? Hvordan fungerer filteret? Hvordan er den fysiske adgang?
- Saml navn, koncept, dato, sted, målgruppe, 18-årsgrænse og priser i synlig tekst. Brug samme fakta i program, billetområde, FAQ og metadata.
- Skriv korte, direkte svar med forklarende overskrifter. Lad vigtige oplysninger stå som HTML-tekst frem for kun i en plakat, video eller slider.
- Dokumentér faktapåstande. Brug ikke “Danmarks første”, dokumenteret effekt eller aktuelle transportdetaljer som fakta uden belæg. Skoleprojektets eventidé er ikke ekstern dokumentation.

## Teknisk SEO

- Brug præcis sidetitel og beskrivelse. Hvis projektet har flere sider, giv dem forskellige titler og beskrivelser, der passer til deres indhold.
- Hav en klar hovedoverskrift og logisk struktur, beskrivende interne links og alt-tekst, som passer til billedets funktion.
- Kontroller, at vigtige sider og indhold kan åbnes og læses, også via direkte URL'er. Generér eller server tekstindhold hensigtsmæssigt for den valgte stack.
- Brug først canonical-URL, delings-URL'er og sitemap med det rigtige domæne. Opfind ikke produktionsadresser.
- Kontroller crawl- og indekseringsindstillinger ved en faktisk lancering. Bevar tilsigtede begrænsninger på en privat prototype; en lokal side kan ikke forventes at få søgetrafik.
- Prioriter brugbar mobilside og hurtig adgang til programmet. Mål eksisterende problemer før større optimeringer.

## Strukturerede data

- Eventkonceptet foreslår `Event` og `FAQPage` som JSON-LD. Vælg typer og egenskaber, der svarer til det faktiske synlige indhold og aktuelle officielle retningslinjer.
- Eventåret og den præcise venueadresse er ikke leveret. Opfind ikke `startDate`, `endDate`, adresse, arrangør, billet-URL eller lagerstatus for at udfylde markup. Markér, hvad der mangler i projektdokumentationen, og udskyd produktionsklar Event-markup til fakta kendes.
- Natprogrammet går over midnat. Skeln mellem programaften og kalenderdato, når bekræftede datoer omsættes til tidsstempler. Brug korrekt lokal tidszone og et bekræftet sluttidspunkt.
- Tilføj kun tilbud med korrekte beløb og `DKK`, som matcher siden og de afklarede billetvilkår. En demobutik er ikke et reelt tilgængeligt tilbud.
- FAQ-markup må kun beskrive de synlige spørgsmål og svar. Validering af markup betyder ikke, at Google viser et udvidet resultat; kontrollér særlige adgangskrav, hvis det er målet.

## Realistisk GEO og dokumentation

Google beskriver, at almindelige SEO-principper fortsat gælder for deres AI-søgefunktioner. Der kræves ikke et særligt “AI-schema” eller en magisk GEO-fil. Antag ikke, at alle andre AI-tjenester har samme indeksering eller regler.

I Double Diamond kobles valg af spørgsmål til Discover/Define, indholdsstruktur til Develop og teknisk validering og evaluering til Deliver. Dokumentér, hvad der faktisk er implementeret. Søgeplaceringer og AI-omtale kræver en offentlig side og observation over tid; de må ikke skrives som opnåede resultater på en lokal prototype.
