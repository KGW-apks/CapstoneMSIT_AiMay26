# Pflegevertrag A (Cloud), Kurzfassung

Anonymisierte Kurzfassung eines Softwarepflegevertrags: Softwarehaus [ANBIETER], Industriekunde [KUNDE]. Gepflegt wird ein Chatbot mit Dokumentensuche (RAG) für Betriebsanleitungen, Wartungshefte und Ersatzteillisten; ein Mandant, ca. 30 Nutzer, ca. 500 Dokumente, Betrieb nur in der Cloud, keine Chatverläufe gespeichert. Ziffern in Klammern: Fundstelle im Volltext.

## 1. Inklusive (in der Pflege enthalten)

- Fehlerbehebung, Ausfälle, Einlesefehler (1.2, 2.1)
- Updates von Software, Modellen und Bibliotheken, tägliche Datensicherung, Überwachung, Doku-Pflege, Beratung per Ticket oder E-Mail (1.2, Anl. 1)
- Neue Dokumente einlesen: bis 100 Seiten je Kalendermonat inklusive, darüber nach Aufwand (7.1)
- Was im Leistungsschein nicht ausdrücklich als „nicht enthalten“ steht, gilt als geschuldet (Anl. 1)

## 2. Nicht inklusive (kostet extra)

- Individuelle Anpassungen der Software (1.4)
- Erstinstallation, Kompatibilität mit anderen oder geänderten Systemen, Schulung, Wechsel von Hardware oder Betriebssystem (1.4)
- Störungen durch Fehlbedienung, defekte Hardware, Stromausfall, Dritte oder höhere Gewalt (1.4)
- Ersteinlesen des Erstbestands (eigener Einrichtungsauftrag), Anbindung an ERP oder andere Systeme, Auswertung von Bildern und Zeichnungen (Anl. 1)
- Support außerhalb der Servicezeiten (4.3); wesentliche Erweiterungen (Upgrades) nur per Nachtrag (1.1)

Abrechnung außerhalb der Pauschale nach Aufwand: Entwickler 95 EUR/Std., Senior/Architekt 190 EUR/Std. (7.4). Die Grenze von 1.000 EUR entspricht rechnerisch ca. 10 Std. Entwickler.

## 3. Fehler oder Änderungswunsch?

Eine Fehlermeldung ist kein Änderungswunsch (6.1). Fehler = reproduzierbar, eine beschriebene Funktion läuft nicht oder falsch (2.1). Reaktion binnen 24 Std., Behebung spätestens nach 5 Werktagen, Fristen laufen nur in den Servicezeiten Mo bis Do, 9:30 bis 17:00 Uhr (2.2, 4.2). Wesentlicher Fehler: Software ganz oder in einer wesentlichen Funktion nicht nutzbar, keine zumutbare Umgehung (2.3). Änderungswünsche gehen per Ticketsystem oder E-Mail ein (6.1).

## 4. Änderungswünsche: Kategorien und Verfahren (6.2 bis 6.8, Anl. 2)

Der Anbieter ordnet jeden Änderungswunsch zuerst mit einem KI-gestützten System einer Kategorie zu:

| Kat. | Merkmale | Entscheidung und Folge |
|:---|:---|:---|
| A | Aufwand höchstens 1.000 EUR; keine Auswirkung auf Architektur, Datenmodelle, Schnittstellen, Sicherheit, Datenschutz. Beispiele: Text, Konfiguration, kleine Oberflächen- oder Berichtsänderung, neue Dokumente einlesen | System gibt frei, Mitarbeiter kann stichprobenartig prüfen. Abrechnung nach Aufwand. Bei geschätzt über 500 EUR vorab Freigabe des Kunden in Textform |
| B | Aufwand über 1.000 EUR oder nicht im Leistungsschein enthalten, aber kein C | Mitarbeiter kalkuliert, Kunde erhält Aufwandsschätzung, Umsetzung erst nach Bestätigung in Textform (Nachtrag) |
| C | Änderung von Architektur, Datenmodellen oder Schnittstellen; wesentliche Erweiterung (Upgrade); neue Module | Mitarbeiter prüft, Einzelangebot, Nachtrag oder gesonderter Vertrag |

- Ein Mitarbeiter prüft vor jeder Kalkulation, jedem Angebot und jedem Preis an den Kunden: jede Einordnung B oder C, jede unsichere Einordnung des Systems, jede Änderung mit Bezug zu Architektur, Datenmodellen, Schnittstellen, Sicherheit oder personenbezogenen Daten (6.4).
- Das System gibt keine rechtsverbindlichen Erklärungen ab, nimmt keine Aufträge an und stellt keine Rechnungen. Angebote, Nachträge und Preise gibt nur ein Mitarbeiter frei (6.4).
- Die Einordnung durch das System begründet keine Zahlungspflicht. Bei B und C entsteht Vergütung erst nach Bestätigung in Textform durch beide Parteien (6.6).
- Der Kunde kann binnen 5 Arbeitstagen eine Überprüfung der Einordnung verlangen; bis zur Entscheidung ruhen Umsetzung und Abrechnung (6.5).
- Aufwand aus einer Fehleinordnung des Anbieters (z. B. B oder C statt A) wird nicht berechnet (6.8).
