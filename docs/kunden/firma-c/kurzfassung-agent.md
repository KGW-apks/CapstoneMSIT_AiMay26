# Wartungsvertrag Plus C (Cloud), Kurzfassung

Anonymisierte Kurzfassung eines Wartungsvertrags Plus (mit Stundenkontingent): Softwarehaus [ANBIETER], Industriekunde [KUNDE]. Gewartet wird eine Webanwendung für Kalibrier- und Prüfdaten von Sensoren, ca. 25 Nutzer, ca. 40 Kundenkonten, nur Cloud. Ziffern in Klammern: Fundstelle im Vertrag.

## 1. Inklusive (in der Pauschale enthalten)

- Fehlerbehebung bei Mängeln, die den vertragsgemäßen Gebrauch nicht nur unerheblich beeinträchtigen; Erfolg geschuldet, sonst Umgehungslösung (2.1)
- Sicherheitsupdates, Anpassung an neue Minor-Versionen eingesetzter Bibliotheken, soweit für den sicheren Betrieb nötig (2.2)
- Support in den Servicezeiten, einfache Diagnose ohne zugesagten Erfolg (2.3, 2.4); Hosting, Betrieb, tägliche Datensicherung (1.1, 5.2)

## 2. Nicht inklusive

- Neuentwicklung, Funktionserweiterungen, größere Änderungen (Kategorie C), Schulungen, Hardware und Fremdsoftware (1.3, 2.2); Zusatzleistungen der Kategorie B nur nach Ziffer 3 und 4 (1.3)
- Vom Kunden zu vertretende Mängel (Quellcode-Eingriffe, Fehlbedienung, Fremdsoftware) und Mehraufwand durch fehlende Mitwirkung: nach Aufwand (2.5, 5.4)

Außerhalb von Pauschale und Kontingent: Entwickler 95 EUR/Std., Senior/Architekt 190 EUR/Std. (6.4).

## 3. Stundenkontingent (3, Anl. 1)

- 60 Std. je Vertragsjahr für Kategorie A und, soweit es reicht, Kategorie B. Kein Übertrag, nicht verbrauchte Stunden verfallen ohne Erstattung (3.1, 3.3)
- Einwände gegen die monatliche Verbrauchsmitteilung binnen 10 Arbeitstagen in Textform, danach anerkannt (3.2)
- Kontingent aufgebraucht: weitere Leistungen nur nach Beauftragung in Textform zum Stundensatz; Zusatzpaket 20 Std. für 1.800 EUR netto jederzeit buchbar (3.4)
- Kategorie C wird nie auf das Kontingent gebucht (4.3).

## 4. Fehler oder Änderungswunsch?

Eine Fehlermeldung ist kein Änderungswunsch (4.1). Meldung in Textform per Ticketsystem oder E-Mail (2.1, 4.1). Servicezeiten: Montag bis Donnerstag, 9:30 bis 17:00 Uhr, außer bundeseinheitlichen und örtlichen Feiertagen; Fristen laufen nur in dieser Zeit (Anl. 2).

| Fehlerklasse | Beschreibung | Reaktion | Behebung oder Umgehung |
|:---|:---|:---|:---|
| 1 kritisch | Software nicht nutzbar, kein Workaround | 2 Std. | 8 Std. |
| 2 schwer | Wesentliche Funktion eingeschränkt, Workaround vorhanden | 4 Std. | 3 Arbeitstage |
| 3 leicht | Geringe Beeinträchtigung | 2 Arbeitstage | nächste Version, spätestens 6 Wochen |

Einstufung durch den Anbieter nach billigem Ermessen; die Zeiten sind Zielwerte, soweit der Kunde mitwirkt (Anl. 2).

## 5. Änderungswünsche: Kategorien und Verfahren (4.2 bis 4.8, Anl. 3)

Der Anbieter ordnet jeden Änderungswunsch zuerst per KI-gestütztem System einer Kategorie zu:

| Kat. | Merkmale | Entscheidung und Folge |
|:---|:---|:---|
| A | Aufwand höchstens 1.000 EUR; keine Auswirkung auf Architektur, Datenmodelle, Schnittstellen, Sicherheit, Datenschutz. Beispiele: Text, Konfiguration, kleine Oberflächen- oder Berichtsänderung | System gibt frei, Mitarbeiter kann stichprobenartig nachsehen; Buchung auf das Kontingent. Bei geschätzt über 500 EUR vorab Freigabe des Kunden in Textform |
| B | Aufwand über 1.000 EUR oder nicht im Leistungsumfang, aber kein C | Mitarbeiter kalkuliert, Aufwandsschätzung, Umsetzung erst nach Bestätigung in Textform; Kontingent, soweit es reicht, sonst Stundensatz |
| C | Änderung von Architektur, Datenmodellen oder Schnittstellen; neue Module | Mitarbeiter prüft, Einzelangebot, gesonderte Beauftragung, nicht auf das Kontingent |

- Ein Mitarbeiter prüft vor jeder Kalkulation, jedem Angebot und jedem Preis an den Kunden: jede Einordnung B oder C, jede unsichere Einordnung, jede Änderung mit Bezug zu Architektur, Datenmodellen, Schnittstellen, Sicherheit oder personenbezogenen Daten. Das System gibt keine rechtsverbindlichen Erklärungen ab, nimmt keine Aufträge an, stellt keine Rechnungen; Angebote, Nachträge und Preise gibt nur ein Mitarbeiter frei (4.4)
- Die Einordnung begründet keine Zahlungspflicht; bei B und C entsteht Vergütung erst nach Bestätigung in Textform durch beide Parteien (4.6)
- Der Kunde kann binnen 5 Arbeitstagen eine Überprüfung der Einordnung verlangen; bis zur Entscheidung ruhen Umsetzung und Abrechnung, außer er verlangt in Textform sofortige Umsetzung unter Vorbehalt (4.5)
- Aufwand aus einer Fehleinordnung des Anbieters (z. B. B oder C statt A) wird nicht berechnet, Kontingentstunden werden gutgeschrieben (4.8)
