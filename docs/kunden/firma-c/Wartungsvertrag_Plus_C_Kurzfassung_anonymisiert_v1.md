---
title: "Wartungsvertrag Plus (Cloud) – Kurzfassung, anonymisiert (Kunde C)"
---

*Gekürzte und anonymisierte Fassung eines Wartungsvertrags Plus (Vertragsart: Wartung mit Stundenkontingent, Cloud). Enthalten sind nur die Regeln und Zahlen, die für die Bearbeitung von Fehlermeldungen und Änderungswünschen wichtig sind. Die Verweise in Klammern zeigen den Paragraphen im Volltext. Namen, Anschriften, Kontaktdaten, Daten und Dienstleister sind durch Platzhalter ersetzt.*

# 1. Parteien

| Rolle | Angabe |
|:---|:---|
| Auftragnehmer | [ANBIETER] (Softwarehaus) |
| Auftraggeber | [KUNDE] (kleineres Industrieunternehmen, Zulieferer in der Robotik) |
| Ansprechpartner Auftraggeber | ein benannter Ansprechpartner mit Entscheidungsbefugnis, auch zuständig für Änderungswünsche (§ 5 Abs. 1); Name: [ANSPRECHPARTNER] |
| Meldeweg | Ticketsystem des Auftragnehmers oder E-Mail an [SUPPORT-E-MAIL] (§ 2 Abs. 1, § 4 Abs. 1) |
| Vertragsbeginn | [DATUM] |

# 2. Kerndaten

| Punkt | Wert |
|:---|:---|
| Vertragsart | Wartung Plus, ausschließlich Cloud; Hosting und Betrieb gehören zur Leistung des Auftragnehmers (§ 1 Abs. 1) |
| Pauschale | 1.500 EUR im Monat im Voraus, zuzüglich Umsatzsteuer (§ 6 Abs. 1) |
| Zahlungsziel Rechnungen | 14 Tage nach Zugang, ohne Abzug (§ 6 Abs. 2) |
| Stundenkontingent | 60 Stunden je Vertragsjahr für Kategorie A und, soweit es reicht, Kategorie B (§ 3 Abs. 1) |
| Zusatzpaket | 20 Stunden für 1.800 EUR netto (Anlage 1) |
| Stundensätze außerhalb von Pauschale und Kontingent | Entwickler 95 EUR, Senior/Architekt 190 EUR; Reisezeiten und -kosten nach Freigabe gesondert (§ 6 Abs. 4) |
| Preisanpassung | Pauschale um bis zu 20 % zum Beginn eines Vertragsjahres, Ankündigung 3 Monate vorher in Textform; Sonderkündigungsrecht des Auftraggebers innerhalb von 4 Wochen zum Ende des Vertragsjahres (§ 6 Abs. 3) |
| Laufzeit | 12 Monate, danach Verlängerung um jeweils 12 Monate (§ 8 Abs. 1) |
| Kündigung | 3 Monate zum Laufzeitende, in Textform (§ 8 Abs. 1); Kündigung aus wichtigem Grund bleibt möglich, § 627 BGB ausgeschlossen (§ 8 Abs. 2) |
| Datensicherung | täglich (§ 5 Abs. 2) |
| Beendigung | nicht verbrauchte Kontingentstunden werden nicht erstattet (§ 8 Abs. 3) |

# 3. Stundenkontingent (§ 3)

- Das Kontingent gilt je Vertragsjahr: 60 Stunden. Nicht verbrauchte Stunden **verfallen** am Ende des Vertragsjahres; kein Übertrag, keine Erstattung (§ 3 Abs. 3, Anlage 1).
- Erfassung in Viertelstunden; monatliche Mitteilung mit Datum, Tätigkeit und Stunden. Einwände innerhalb von **10 Arbeitstagen** in Textform, danach gilt die Mitteilung als anerkannt (§ 3 Abs. 2).
- Ist das Kontingent aufgebraucht, informiert der Auftragnehmer den Auftraggeber. Weitere Leistungen nur nach Beauftragung in Textform zum Stundensatz; der Auftraggeber kann jederzeit Zusatzpakete (20 Stunden für 1.800 EUR netto) hinzubuchen (§ 3 Abs. 4).
- Kategorie A und B werden auf das Kontingent gebucht, Kategorie B nur soweit es reicht, der Rest nach Stundensatz (§ 4 Abs. 3). Kategorie C wird nie auf das Kontingent gebucht.

# 4. Leistungsumfang

## Enthalten

- Fehlerbehebung für Mängel, die den vertragsgemäßen Gebrauch nicht nur unerheblich beeinträchtigen; der Auftragnehmer steht auf Erfolg ein; ist eine endgültige Behebung nicht rechtzeitig möglich, stellt er eine Umgehungslösung bereit (§ 2 Abs. 1).
- Sicherheitsupdates für die eingesetzten Komponenten und Anpassung an neue Minor-Versionen von Bibliotheken und Laufzeitumgebungen, soweit für den sicheren Betrieb nötig (§ 2 Abs. 2).
- Support zu Nutzung und Betrieb innerhalb der Servicezeiten (§ 2 Abs. 3).
- Einfache Diagnose- und Kontrolltätigkeiten als Dienstleistung, ohne zugesagten Erfolg (§ 2 Abs. 4).

## Nicht enthalten

- Neuentwicklung von Funktionen, Funktionserweiterungen, größere Änderungen (Kategorie C), Schulungen, Hardware und Fremdsoftware, die nicht Teil der Vertragssoftware sind (§ 1 Abs. 3, § 2 Abs. 2).
- Kategorie B wird nur nach § 3 und § 4 erbracht (§ 1 Abs. 3).
- Fehler, die der Auftraggeber zu vertreten hat (z. B. Eingriffe in den Quellcode, unsachgemäße Bedienung, Fremdsoftware): Abrechnung nach Aufwand (§ 2 Abs. 5).

# 5. Fehlermeldungen und Service Level (Anlage 2)

**Servicezeiten:** Montag bis Donnerstag, 9:30 bis 17:00 Uhr, außer bundeseinheitliche Feiertage und Feiertage am Sitz des Auftragnehmers. Fristen laufen nur innerhalb der Servicezeiten.

| Fehlerklasse | Beschreibung | Reaktionszeit | Behebung oder Umgehungslösung |
|:---|:---|:---|:---|
| 1 (kritisch) | Software nicht nutzbar, kein Workaround | 2 Std. | 8 Std. |
| 2 (schwer) | Wesentliche Funktion eingeschränkt, Workaround vorhanden | 4 Std. | 3 Arbeitstage |
| 3 (leicht) | Geringe Beeinträchtigung | 2 Arbeitstage | nächste planmäßige Version, spätestens 6 Wochen |

- Die Einstufung nimmt der Auftragnehmer nach Rücksprache mit dem Auftraggeber nach billigem Ermessen vor. Die Zeiten sind Zielwerte, soweit der Auftraggeber seine Mitwirkungspflichten erfüllt hat (Anlage 2).
- Fehlermeldungen sind keine Änderungswünsche; Änderungswünsche laufen nach Abschnitt 7 dieser Kurzfassung (§ 4 Abs. 1).
- **Mitwirkung (§ 5):** Ansprechpartner mit Entscheidungsbefugnis benennen; Informationen, Zugänge und Testmöglichkeiten rechtzeitig bereitstellen (Abs. 1). Endgeräte und Internetverbindung bereitstellen, Zugangsdaten schützen, Änderungen mit Einfluss auf den Betrieb vorab mitteilen (Abs. 3). Bei Verletzung verlängern sich Fristen, Mehraufwand wird nach Aufwand vergütet (Abs. 4). Ein Zugriff auf Systeme des Auftraggebers ist nicht nötig (Abs. 2).

# 6. Haftung, Nutzungsrechte und Vertraulichkeit (§ 7)

| Punkt | Regel |
|:---|:---|
| Unbeschränkte Haftung | bei Vorsatz und grober Fahrlässigkeit, bei Verletzung von Leben, Körper oder Gesundheit und nach dem Produkthaftungsgesetz (§ 7 Abs. 2) |
| Leichte Fahrlässigkeit | nur bei Verletzung wesentlicher Vertragspflichten, begrenzt auf den vertragstypischen, vorhersehbaren Schaden, **höchstens 50.000 EUR je Schadensfall** und insgesamt auf die in den letzten 12 Monaten gezahlte Vergütung (§ 7 Abs. 3) |
| Datenverlust | begrenzt auf den Aufwand, der für die Wiederherstellung aus der Datensicherung angefallen wäre (§ 7 Abs. 3) |
| KI-Einsatz | ändert die Haftung nicht; eine Einordnung durch das System entbindet den Auftragnehmer nicht von der Verantwortung für die Ergebnisse (§ 7 Abs. 6) |
| Nutzungsrechte | für Änderungen aus der Wartung gelten die Nutzungsrechte des zugrunde liegenden Softwarevertrags; ohne Regelung einfaches, unbefristetes Nutzungsrecht für eigene betriebliche Zwecke, entsteht mit vollständiger Zahlung (§ 7 Abs. 1) |
| Vertraulichkeit | gegenseitig, gilt 5 Jahre über das Vertragsende hinaus (§ 7 Abs. 4) |

Der Vertrag enthält keine eigene Gewährleistungs- oder Garantieregelung; die Mängelhaftung ergibt sich aus der Fehlerbehebung (§ 2 Abs. 1, Anlage 2) und der Haftungsregelung oben. Eine zugesagte Garantie ist im Vertrag nicht vorgesehen.

# 7. Änderungswünsche und Nachtragsverfahren (§ 4)

**Einreichung (Abs. 1):** in Textform über das Ticketsystem oder per E-Mail, mit Beschreibung des gewünschten Ergebnisses und, soweit bekannt, der Dringlichkeit.

**Ersteinordnung (Abs. 2):** Der Auftragnehmer ordnet jeden Änderungswunsch zuerst mit einem KI-gestützten System nach den Regeln der Anlage 3 einer Kategorie zu.

| Kategorie | Merkmale | Wer entscheidet | Folge und Abrechnung | Freigabe des Auftraggebers |
|:---|:---|:---|:---|:---|
| A – Kleinstveränderung | Aufwand höchstens 1.000 EUR je Änderung; keine Auswirkung auf Architektur, Datenmodelle, Schnittstellen, Sicherheit oder Datenschutz. Beispiele: Text-, Konfigurations-, kleine Oberflächen- oder Berichtsänderung | System gibt frei; ein Mitarbeiter kann stichprobenartig nachsehen | Mitteilung, Umsetzung ohne Einzelangebot, Buchung auf das Stundenkontingent | Vorab in Textform, wenn der geschätzte Aufwand über 500 EUR liegt |
| B – Zusatzleistung | Aufwand über der Grenze von A oder nicht im Leistungsumfang, aber ohne Architekturänderung (keine Kategorie C) | Mitarbeiter nach Kalkulation | Aufwandsschätzung; Umsetzung erst nach Bestätigung in Textform; Buchung auf das Kontingent, soweit es reicht, sonst Stundensatz | immer (Bestätigung) |
| C – größere Änderung | Änderung von Architektur, Datenmodellen oder Schnittstellen; neue Module | Mitarbeiter | Einzelangebot nach menschlicher Prüfung; gesonderte Beauftragung (Einzelangebot, Projekt- oder Aufwandsvertrag); nicht auf das Kontingent | immer (Angebot) |

**Menschliche Prüfung (Abs. 4):** Ein Mitarbeiter prüft jede Einordnung in B oder C, jede unsichere Einordnung des Systems und jede Änderung, die Architektur, Datenmodelle, Schnittstellen, Sicherheit oder personenbezogene Daten berührt, bevor der Auftraggeber eine Kalkulation, ein Angebot oder einen Preis erhält. Das System gibt keine rechtsverbindlichen Erklärungen ab, nimmt keine Aufträge an und stellt keine Rechnungen. Angebote, Nachträge und Preise gibt ausschließlich ein Mitarbeiter frei.

**Mitteilung und Überprüfung (Abs. 5):** Die Einordnung wird mit kurzer Begründung in Textform mitgeteilt. Der Auftraggeber kann innerhalb von 5 Arbeitstagen verlangen, dass ein Mitarbeiter sie überprüft. Bis zur Entscheidung ruhen Umsetzung und Abrechnung, außer der Auftraggeber verlangt in Textform die sofortige Umsetzung unter Vorbehalt.

**Verbindlichkeit (Abs. 6):** Die Einordnung durch das System begründet keine Zahlungspflicht. Vergütung entsteht nur nach Kontingent bzw. Stundensatz und diesem Verfahren; bei B und C erst nach Bestätigung in Textform durch beide Parteien.

**Protokoll (Abs. 7):** Je Änderungswunsch werden Eingang, Einordnung, Begründung, Sicherheitswert, Mitwirkung eines Mitarbeiters und Freigabe protokolliert. Auszug auf Verlangen. Aufbewahrung: Vertragsdauer plus 12 Monate.

**Fehleinordnung (Abs. 8):** Aufwand durch eine Fehleinordnung, die der Auftragnehmer zu verantworten hat (z. B. B oder C statt A), wird nicht berechnet; bereits auf das Kontingent gebuchte Stunden werden gutgeschrieben.

**KI-Einsatz (Abs. 9):** Die KI ist ein Hilfsmittel; der Auftragnehmer bleibt verantwortlich. Eingereichte Inhalte werden nur zur Einordnung und Bearbeitung verarbeitet und nicht zum Training allgemeiner Modelle verwendet. Bei personenbezogenen Daten wird vorab eine Auftragsverarbeitung nach Art. 28 DSGVO geschlossen. Der Auftragnehmer weist den Auftraggeber auf den KI-Einsatz hin.

# 8. Datenschutz und Dienstleister

- Werden bei Wartung oder im Änderungsverfahren personenbezogene Daten im Auftrag verarbeitet, besteht vorab eine Vereinbarung zur Auftragsverarbeitung nach Art. 28 DSGVO (§ 7 Abs. 5, Anlage 4).

| Dienstleister | Sitz | Zweck | Auftragsverarbeitung |
|:---|:---|:---|:---|
| [HOSTING-DIENSTLEISTER] | Deutschland | Hosting der Cloud-Umgebung | geschlossen |
| [KI-DIENSTLEISTER] | EU | Einordnung von Änderungswünschen (KI) | geschlossen |

Diese Dienstleister gelten als genehmigt; eine Änderung teilt der Auftragnehmer vorab in Textform mit (§ 7 Abs. 7).

**Auftragsverarbeitung, Kurzfassung (Anlage 4):** Weisungsgebunden. Verarbeitet werden Name, Firma, E-Mail-Adresse und Anmeldedaten der internen Nutzer und der Kundenkonten im Portal; Betroffene sind Mitarbeiter des Auftraggebers und Nutzer seiner Kunden. Maßnahmen: Zugriffsbeschränkung, Verschlüsselung bei Übertragung und Speicherung, tägliche Datensicherung, Protokollierung, Vertraulichkeitsverpflichtung der Mitarbeiter. Unterauftragnehmer nur die oben genannten. Nach Vertragsende Löschung oder Rückgabe der Daten.

# 9. Vertragssoftware (Anlage 1)

Webanwendung für Kalibrier- und Prüfdaten von Sensoren: Import der Messdaten von 4 Prüfständen, Erzeugen der Kalibrierzertifikate als PDF, Chargenrückverfolgung, Kundenportal zum Download der Zertifikate. Version 2.1, bis ca. 25 interne Nutzer und ca. 40 Kundenkonten. Betrieb ausschließlich in der Cloud.

# 10. Bewusst weggelassen

Präambel und Anschriften, Schlussbestimmungen (Textform, anwendbares Recht, Gerichtsstand, Salvatorische Klausel), Unterschriftsblock.
