# Notizen

Sammelstelle für Festlegungen und Textstellen, die später im n8n-Workflow oder in den anderen Dokumenten umgesetzt werden. Lose Arbeitsdatei aus Sprint 1, keine abgestimmte Fassung. Stand 2026-10-14. Das beschriebene Unternehmen und alle Zahlen sind fiktiv.

**Status der Angaben:** Zitate aus eigenen Entwürfen sind als solche gekennzeichnet. Was darunter als *Für die Umsetzung* steht, ist die Lesart des Eintragenden und noch keine Festlegung der Gruppe.

**Eintragen:** Neue Notiz unten anfügen, mit Quelle (welches Dokument, welche Ziffer) und Datum. Offene Platzhalter aus Entwürfen sammeln wir unten in einer Liste, damit sie nicht untergehen.

## Softwarepflegevertrag (Cloud): Verfahren für Änderungswünsche

Quelle: [30_Vorlage_Softwarepflegevertrag_Cloud_v5.docx](vorlagen/30_Vorlage_Softwarepflegevertrag_Cloud_v5.docx), Ziffer 6 und Anlage 2 — also die Vorlage, nicht der Vertrag eines bestimmten Kunden. Michi, Stand 2026-10-14. `[●]` sind dort noch offene Platzhalter.

### Kategorien (Ziffer 6.2 und Anlage 2 Abschnitt 1)

| Kategorie | Merkmale | Folge (Ziffer 6.3) |
|---|---|---|
| A — Kleinstveränderung | höchstens 1.000 EUR Aufwand je Änderung, berührt weder Architektur, Datenmodelle, Schnittstellen noch Sicherheit oder Datenschutz | System gibt frei, Abrechnung nach Aufwand; über `[●]` EUR vorab Freigabe des Kunden in Textform |
| B — Zusatzleistung | über der Grenze von A oder nicht im Leistungsschein, aber keine Architekturänderung | Mitarbeiter prüft, Kunde bestätigt in Textform (Nachtrag) |
| C — größere Änderung | Architektur, Datenmodelle, Schnittstellen, Upgrade nach Ziffer 1.1 oder neue Module | Mitarbeiter prüft, Einzelangebot oder gesonderter Vertrag |

*Für die Umsetzung:* Der Agent muss je Änderungswunsch drei Dinge ausgeben: Kategorie, kurze Begründung und einen Sicherheitswert. Begründung und Sicherheitswert sind nicht optional, Ziffer 6.5 und 6.7 verlangen beides.

### Menschliche Prüfung (Ziffer 6.4)

Ein Mitarbeiter prüft **vor** jeder Kalkulation, jedem Angebot und jedem Preis an den Kunden bei: Kategorie B, Kategorie C, unzureichender Sicherheit des Systems, und wenn die Änderung Architektur, Datenmodelle, Schnittstellen, Sicherheit oder personenbezogene Daten berührt. Das System gibt keine rechtsverbindlichen Erklärungen ab, nimmt keine Aufträge an und stellt keine Rechnungen.

*Für die Umsetzung:* Nur Kategorie A läuft ohne Menschen durch. Alles andere ist ein Tor vor der Ausgabe an den Kunden, unabhängig vom Sicherheitswert. Im Workflow also eine Weiche, die diese vier Fälle zusammenfasst, nicht vier verstreute Prüfungen.

Offen: Woran erkennt der Agent „berührt Architektur, Datenmodelle oder Schnittstellen"? Das setzt Wissen über den Aufbau der Kundensoftware voraus, das in der Kundenäußerung meist nicht steht. Entweder gibt das Modell das als eigenes Feld aus und wir messen, wie verlässlich es ist, oder die Entwicklung liefert die Einschätzung zu. Zu klären in der Gruppe.

### Protokoll (Ziffer 6.7)

Je Änderungswunsch festzuhalten: Eingang, Einordnung, Begründung, Sicherheitswert, Mitwirkung eines Mitarbeiters, Freigabe. Aufbewahrung Vertragsdauer plus 12 Monate, Auszug auf Verlangen des Kunden.

*Für die Umsetzung:* Das ist eine Anforderung an Speicherung, nicht an die Weiche — der Workflow braucht eine Ablage, aus der sich ein Kundenauszug erzeugen lässt. Die sechs Felder sind die Mindestspalten.

### Fehleinordnung (Ziffer 6.8)

Aufwand aus einer Fehleinordnung, die der Anbieter zu verantworten hat, wird dem Kunden nicht berechnet.

*Für die Umsetzung:* Damit das später zählbar ist, braucht die Ablage neben der Einordnung des Agenten die korrigierte Einordnung des Menschen als zweites Feld.

## Aus einer neueren Fassung der Anlage 2 (noch nicht im Repo)

Die folgenden Abschnitte 2 bis 4 der Anlage 2 stammen aus einem Entwurf, der über v5 hinausgeht: in `Softwarepflegevertrag_Cloud_v5.docx` endet die Anlage 2 nach Abschnitt 1. Beim nächsten Upload mit abgleichen.

### Abschnitt 2: Eskalation an einen Mitarbeiter (immer, unabhängig vom Sicherheitswert)

- Die Änderung berührt Architektur, Datenmodell oder eine Schnittstelle.
- Die Änderung betrifft Sicherheit, Berechtigungen oder personenbezogene Daten.
- Der Änderungswunsch betrifft mehr als eine Komponente oder ist widersprüchlich oder unklar.
- Streit über die Auslegung des Vertrags oder frühere Einordnung (Überprüfung nach Ziffer 6.5).
- Die geschätzte Aufwandsgrenze von Kategorie A wird überschritten oder ist unklar.

*Für die Umsetzung:* Deckt sich größtenteils mit Ziffer 6.4, geht aber zwei Fälle darüber hinaus: „mehr als eine Komponente" und „Streit über die Auslegung". Letzterer ist kein Fall für den Agenten, sondern ein Wiedervorlage-Pfad nach Ziffer 6.5.

### Abschnitt 3: Sicherheitsschwelle

> Erreicht das System bei der Einordnung einen Sicherheitswert von weniger als `[●]` % (Vorschlag: `[80]` %), prüft ein Mitarbeiter, bevor dem Kunden eine Einordnung mitgeteilt wird.

*Für die Umsetzung:* Braucht einen numerischen Sicherheitswert je Einordnung und eine Verzweigung an der Schwelle. Wirkung ist die zweite Satzhälfte: unter der Schwelle geht nichts an den Kunden, bevor ein Mensch gesehen hat.

Offen: Wie entsteht der Sicherheitswert, und ist er kalibriert? Ein selbst berichteter Wert des Modells ist nicht ohne weiteres eine Wahrscheinlichkeit. Hängt an den Erfolgskriterien im [Kandidatenbogen](kandidatenbogen.md).

### Abschnitt 4: Qualitätskontrolle

> Der Anbieter lässt mindestens `[●]` % der Einordnungen je `[Quartal]` durch einen Mitarbeiter gegenprüfen und erfasst Fehleinordnungen, insbesondere Änderungen der Kategorie B oder C, die als A freigegeben wurden. Die Ergebnisse stellt er dem Kunden auf Verlangen zur Verfügung.

*Für die Umsetzung:* Zusätzlich zum Protokoll nach Ziffer 6.7 braucht es eine Stichprobe und ein Rückschreiben des Prüfergebnisses. Richtung „B oder C als A freigegeben" ist die gefährliche: zu niedrig eingeordnet heißt ohne Menschen freigegeben.

## Offene Platzhalter

| Stelle | Platzhalter | Stand |
|---|---|---|
| Ziffer 6.3 | Aufwand, ab dem bei Kategorie A vorab die Freigabe des Kunden nötig ist | offen |
| Anlage 2 Abschnitt 3 | Sicherheitswert, ab dem ein Mitarbeiter prüft | Vorschlag 80 % |
| Anlage 2 Abschnitt 4 | Anteil der Einordnungen in der Gegenprüfung | offen |
| Anlage 2 Abschnitt 4 | Zeitraum der Gegenprüfung | Vorschlag Quartal |
| Ziffer 8.5 | Hosting- und KI-Dienstleister, Sitz, Auftragsverarbeitung | offen, betrifft den Workflow direkt |
| Anlage 1 | Programmtabelle (gepflegte Software, Blacklist) | offen |

Aufwandsgrenze der Kategorie A: in der Vorlage 1.000 EUR je Änderung (Ziffer 6.2). **Wichtig: der Wert ist je Kunde verschieden** — Kunde B hat 2.500 EUR mit Freigabe ab 1.500 EUR, der Wartungsvertrag Plus (Kunden C und D) 500 EUR. Die Schwellen gehören also in eine Konfiguration je Kunde, nicht in den Workflow fest verdrahtet. Werte je Kunde siehe die Kurzfassungen unter [kunden/](kunden/).

## Redaktioneller Hinweis zum Vertrag

Die Änderungstabelle am Anfang des Vertrags nennt „Ziffer 7.6: Vergütung der Änderungen nach Ziffer 6". Im Vertragstext steht das aber in Ziffer 7.4, Ziffer 7.6 ist die Umsatzsteuer. Beim nächsten Durchgang korrigieren.

## Kunden A bis E: Vertragsart und Konfiguration

Quelle: die Verträge und Kurzfassungen unter [kunden/](kunden/), Stand 2026-10-17. Alle Firmen und Zahlen sind erfunden.

| Kunde | Vertragsart | Pauschale | Laufzeit | Grenze Kategorie A |
|---|---|---|---|---|
| A — klein | Softwarepflege (Cloud) | 3.200 EUR/Monat | 24 Monate | 1.000 EUR |
| B — groß | Softwarepflege (Cloud) | 8.000 EUR/Monat | 36 Monate | 2.500 EUR, Freigabe ab 1.500 EUR |
| C — klein | Wartung Plus | 1.500 EUR/Monat, 60 Stunden Kontingent | 12 Monate | 500 EUR |
| D — groß | Wartung Plus | 9.500 EUR/Monat, 200 Stunden Kontingent | 36 Monate | 500 EUR |
| E — klein | Softwareerstellung | 63.000 EUR netto in 4 Bausteinen | bis 30.07.2027 | Änderungspuffer, Freigabe ab 500 EUR |

*Für die Umsetzung:* Drei Vertragsarten, fünf Kunden — das Verfahren nach Ziffer 6 ist in allen Verträgen gleich aufgebaut, **die Zahlen darin sind es nicht**. Der Workflow braucht also pro Kunde einen Satz Parameter (Vertragsart, Grenze A, Freigabegrenze, Servicezeiten, Reaktions- und Behebungszeiten) und darf keine Schwelle fest verdrahten. Die anonymisierten Kurzfassungen je Kunde sind dafür die passende Quelle, weil sie genau diese Werte in gleicher Gliederung enthalten.

Offen: Die Vorauswahl, welcher Vertrag zu einer eingehenden Kundenäußerung gehört, muss vor der Einordnung stehen. Ohne Kundenzuordnung kann der Agent gar nicht prüfen.
