---
title: "Softwareerstellungsvertrag (Cloud) – Kurzfassung, anonymisiert (Kunde E)"
---

*Gekürzte und anonymisierte Fassung eines Softwareerstellungsvertrags (Vertragsart: Erstellung in Bausteinen, Cloud). Enthalten sind nur die Regeln und Zahlen, die für die Bearbeitung von Änderungswünschen und die Projektsteuerung wichtig sind. Die Verweise in Klammern zeigen die Ziffer im Volltext. Namen, Anschriften, Kontaktdaten, Daten und Dienstleister sind durch Platzhalter ersetzt. Termine sind als Platzhalter und als Abstand in Wochen angegeben.*

# 1. Parteien

| Rolle | Angabe |
|:---|:---|
| Auftragnehmer (AN) | [ANBIETER] (Softwarehaus) |
| Auftraggeber (AG) | [KUNDE] (kleine Beratungsfirma, ca. 5 Mitarbeiter, wachsend) |
| Meldeweg Änderungswünsche | Ticketsystem des AN oder E-Mail an [PROJEKT-E-MAIL] (VII.1) |
| Vertragsbeginn | [DATUM] |

# 2. Kerndaten

| Punkt | Wert |
|:---|:---|
| Vertragsart | Erstellung einer Software in 4 Bausteinen; Betrieb ausschließlich in der Cloud (I.2, V) |
| Gesamtvergütung | 63.000 EUR netto, zuzüglich 19 % Mehrwertsteuer (11.970 EUR) = 74.970 EUR brutto (XI) |
| Zahlung | in Raten je Baustein, fällig nach Unterzeichnung des Teilabnahmeprotokolls; Rechnungen innerhalb von 14 Tagen (XI) |
| Stundensätze für Zusatzaufträge und Änderungen | Entwickler 95 EUR, Senior/Architekt 190 EUR (XI) |
| Gesamtfertigstellung | [TERMIN FERTIGSTELLUNG]; Gesamtabnahme [TERMIN GESAMTABNAHME] (IV, Anlage 3) |
| Terminvoraussetzung | Informationen und Freigaben des AG innerhalb von 5 Arbeitstagen, sonst verschieben sich die Termine um die Verzögerung (IV) |
| Quellcode | wird mit der Abnahme vollständig samt Entwicklerdokumentation an den AG übergeben; der AG darf ihn bearbeiten und weiterentwickeln (X) |
| Nutzungsrechte | ausschließlich, unbefristet, übertragbar, unwiderruflich, weltweit, alle Nutzungsarten (VI) |
| Hosting und Betrieb | nicht Teil dieses Vertrags, gesondert im Pflegevertrag (V) |
| Gewährleistung | 1 Jahr nach Abnahme (XII.1) |

# 3. Leistungsumfang (I)

- **ERP:** Mandantenstamm mit Ansprechpartnern, Beratungsprojekte mit Aufgaben, Fristen und Wiedervorlagen, Vorlagen für Datenschutzdokumente, Zeiterfassung, Angebote und Rechnungen, Rollen- und Rechtekonzept für bis zu 15 Nutzer (I.3 a).
- **Chatbot:** beantwortet Datenschutzfragen auf Grundlage einer vom AG gepflegten Wissensbasis mit Quellenangabe; deutlicher Hinweis auf den KI-Einsatz; Übergabe an einen Berater bei unsicheren oder personenbezogenen Fragen; Speicherung der Gespräche 30 Tage, danach Löschung; keine Verwendung der Eingaben zum Training allgemeiner Modelle; Hosting in der EU (I.3 b).
- **Verbindung** von Chatbot und ERP: Zuordnung der Gespräche zum Mandanten, Anlage von Aufgaben (I.3 c).
- Dazu Benutzungsanleitung, Quellcode, Dokumentation (I.1).
- **Abgrenzung Recht:** Der Chatbot soll so gestaltet werden, dass der AG die Anforderungen von DSGVO und EU AI Act, soweit sie den Chatbot betreffen, einhalten kann; konkretisiert im Pflichtenheft (Baustein 1). Der AN schuldet die Funktionen des Pflichtenhefts, **nicht** die rechtliche Bewertung des Einsatzes (I.2).
- **Qualität:** alle Anforderungen des Pflichtenhefts; Mindeststandard ist der aktuelle Stand der Informationstechnik (III).

# 4. Bausteine, Termine und Zahlungsplan (Anlage 3)

Alle Beträge netto. Baustein 2 und 3 bilden die Basisversion (II.3), Baustein 4 die Endversion (II.4). Die Bausteine 2 und 3 können parallel bearbeitet werden.

| Baustein | Inhalt | Termine | Vergütung |
|:---|:---|:---|:---|
| 1 – Konzept und Pflichtenheft | Anforderungen beider Systeme, Datenschutz- und KI-Anforderungen für den Chatbot (u. a. KI-Kennzeichnung, Übergabe an Berater, Löschfristen), Datenmodell, Rollenkonzept, Pflichtenheft als Anlage 1 | Fertigstellung [TERMIN 1]; Unterschrift unter das Pflichtenheft 2 Wochen später | 6.000 EUR |
| 2 – ERP-Kern | Mandantenstamm, Beratungsprojekte mit Fristen, Zeiterfassung, Angebote und Rechnungen, Rollen und Rechte | Bereitstellung [TERMIN 2]; Teilabnahme 5 Wochen später | 24.000 EUR |
| 3 – Chatbot | Wissensbasis, Beantwortung mit Quellenangabe, KI-Kennzeichnung, Übergabe an Berater, Löschung nach 30 Tagen | Bereitstellung 9 Wochen nach Baustein 2; Teilabnahme 5 Wochen später | 21.000 EUR |
| 4 – Integration und Abschluss | Verbindung von Chatbot und ERP, Datenübernahme, Gesamttest, Dokumentation, Übergabe des Quellcodes | Bereitstellung 9 Wochen nach Baustein 3; Gesamtabnahme 5 Wochen später | 12.000 EUR |
| **Summe** | | | **63.000 EUR** (74.970 EUR brutto) |

- Reihenfolge: Pflichtenheft (Bst. 1) → Basisversion (Bst. 2 und 3) → Freigabe durch den AG → Endversion (Bst. 4) (II).
- Das Pflichtenheft wird gemeinsam erstellt, mit Datum rechtsverbindlich unterzeichnet und ist Anlage 1 (II.2).
- Bei Terminüberschreitung des AN um mehr als 4 Wochen nach angemessener Nachfrist kann der AG vom Vertrag zurücktreten; bereits gezahlte (Teil-)Vergütung ist zurückzuzahlen (IV). Bei vom AG verlangten erheblichen Vertragsänderungen wird der Termin unwirksam und nach Ziffer VII neu vereinbart (IV).

# 5. Einweisung und Abnahme (VIII, IX)

| Punkt | Regel |
|:---|:---|
| Einweisung | nach Bereitstellung; bei Baustein 2 bis 4 jeweils online, 4 Stunden je Baustein; weitere Einweisungen gegen zusätzliche Vergütung (VIII) |
| Abnahmetests | der AN weist binnen einer Woche nach der ersten Einweisung die Funktion durch Abnahmetests nach (IX.1) |
| Testphase | 4 Wochen nach der Einweisung, je Baustein (IX.1, Anlage 3) |
| Teilabnahme | jeder Baustein einzeln; nach Baustein 4 die Gesamtabnahme; Baustein 1: Unterschrift unter das Pflichtenheft ersetzt die Abnahme (IX.1) |
| Abnahmeprotokoll | von beiden Parteien unterzeichnet; festgestellte Mängel werden dokumentiert (IX.1) |
| Kleinere Mängel | hindern die Abnahme nicht, wenn der AN Beseitigung spätestens binnen 3 Tagen zusagt (IX.2) |
| Unerhebliche Mängel | berechtigen nicht zur Verweigerung der Abnahme; läuft eine vom AN gesetzte Abnahmefrist ergebnislos ab, gilt die Abnahme als erteilt (IX.3) |
| Erhebliche Mängel | unverzügliche Beseitigung; Abnahme innerhalb einer Woche nach Anzeige wiederholen (IX.4) |
| Nutzung vor Abnahme | zu Zwecken der Freigabe und Abnahmeprüfung gestattet (VI) |

# 6. Gewährleistung, Garantie und Haftung (XII, XIII)

## Gewährleistung (XII)

| Punkt | Regel |
|:---|:---|
| Umfang | funktionsfehlerfreies Laufen entsprechend dem Pflichtenheft; bei Abnahme anerkannter Stand der Technik und keine Mängel (XII.1) |
| Dauer | **1 Jahr nach Abnahme** (XII.1) |
| Nacherfüllung | Kommt der AN in einer angemessenen Frist seiner Mängelbeseitigung nicht nach, kann der AG die Maßnahmen auf Kosten und Gefahr des AN selbst vornehmen oder von Dritten vornehmen lassen (XII.1) |
| Rücktritt, Minderung | erst nach Fehlschlagen der Nacherfüllung (XII.2) |
| Rechtsmängel, Schutzrechte Dritter | Der AN verschafft auf eigene Kosten nach Wahl des AG das Nutzungsrecht oder gestaltet die Software schutzrechtsfrei und stellt den AG von Ansprüchen Dritter frei (XV) |
| Fehlermeldung ist kein Änderungswunsch | Mängel laufen über Ziffer XII, Änderungswünsche über Abschnitt 7 dieser Kurzfassung (VII.1) |

## Haftung (XIII)

- Haftung für Schäden wegen Rechtsmängeln, für Vorsatz und grobe Fahrlässigkeit (Körperschäden ausgenommen von der Beschränkung).
- Bei leichter Fahrlässigkeit nur bis **63.000 EUR** sowie für typischerweise zu erwartende Schäden bei Softwareentwicklungsaufträgen.
- Im Übrigen ausgeschlossen, auch für Datenverluste und Folgeschäden; ausgeschlossen auch, soweit zugunsten des AG eine Versicherung besteht.
- Der KI-Einsatz im Änderungsverfahren ändert die Haftung nicht.
- Eine ausdrückliche Garantie ist im Vertrag nicht vorgesehen; die Gewährleistung nach XII ist die maßgebliche Zusage.

# 7. Änderungswünsche und Nachtragsverfahren (VII)

**Einreichung (VII.1):** in Textform über das Ticketsystem oder per E-Mail, mit Beschreibung des gewünschten Ergebnisses und, soweit bekannt, der Dringlichkeit.

**Ersteinordnung (VII.2):** Der AN ordnet jeden Änderungswunsch zuerst mit einem KI-gestützten System nach den Regeln der Anlage 2 einer Kategorie zu.

| Kategorie | Merkmale | Wer entscheidet | Folge und Abrechnung | Freigabe des AG |
|:---|:---|:---|:---|:---|
| A – Kleinstveränderung | geringfügige Abweichung vom Pflichtenheft, Aufwand höchstens 1.000 EUR je Änderung; keine Auswirkung auf Architektur, Datenmodelle, Schnittstellen, Sicherheit oder Datenschutz; verschiebt den Fertigstellungstermin nicht. Beispiele: Text-, Konfigurations-, kleine Oberflächen- oder Berichtsänderung | System gibt frei; ein Mitarbeiter kann stichprobenartig nachsehen | Mitteilung und Umsetzung ohne Nachtrag; **ohne Zusatzentgelt bis zu einem Änderungspuffer von insgesamt 3.000 EUR**, darüber nach Stundensatz | Vorab in Textform, wenn der geschätzte Aufwand über 500 EUR liegt |
| B – Zusatzleistung | Abweichung vom Pflichtenheft über der Grenze von A, aber keine Kategorie C oder E | Mitarbeiter nach Kalkulation | Aufwandsschätzung mit Auswirkung auf Termin und Vergütung; Umsetzung erst nach Bestätigung in Textform (Nachtrag); Zusatzentgelt nach Stundensatz | immer (Bestätigung) |
| C – größere Änderung | Änderung von Architektur, Datenmodellen oder Schnittstellen; neue Module | Mitarbeiter | Einzelangebot nach menschlicher Prüfung; Nachtrag oder gesonderter Vertrag; Fertigstellungstermin wird insoweit unwirksam und neu vereinbart | immer (Angebot) |
| E – erforderliche Änderung | erforderlich, um den mit dem Vertragsgegenstand verbundenen Erfolg zu erreichen oder zu sichern; **ob eine Änderung erforderlich ist, entscheidet nicht das System, sondern ein Mitarbeiter** | Mitarbeiter des AN | ohne Zusatzentgelt (Anlage 2) | im Vertrag nicht gesondert geregelt |

**Menschliche Prüfung (VII.4):** Ein Mitarbeiter prüft jede Einordnung in B oder C, jede unsichere Einordnung des Systems und jede Änderung, die Architektur, Datenmodelle, Schnittstellen, Sicherheit oder personenbezogene Daten berührt, bevor der AG eine Kalkulation, ein Angebot oder einen Preis erhält. Das System gibt keine rechtsverbindlichen Erklärungen ab, nimmt keine Aufträge an und stellt keine Rechnungen. Angebote, Nachträge und Preise gibt ausschließlich ein Mitarbeiter frei.

**Mitteilung und Überprüfung (VII.5):** Die Einordnung wird mit kurzer Begründung in Textform mitgeteilt. Der AG kann innerhalb von 5 Arbeitstagen verlangen, dass ein Mitarbeiter sie überprüft. Bis zur Entscheidung ruhen Umsetzung und Abrechnung, außer der AG verlangt in Textform die sofortige Umsetzung unter Vorbehalt.

**Verbindlichkeit (VII.6):** Die Einordnung durch das System begründet keine Zahlungspflicht. Vergütung entsteht nur nach VII.3 und XI; bei B und C erst nach Bestätigung in Textform durch beide Parteien.

**Protokoll (VII.7):** Je Änderungswunsch werden Eingang, Einordnung, Begründung, Sicherheitswert, Mitwirkung eines Mitarbeiters und Freigabe protokolliert. Auszug auf Verlangen. Aufbewahrung: Vertragsdauer plus 12 Monate.

**Fehleinordnung (VII.8):** Aufwand durch eine Fehleinordnung, die der AN zu verantworten hat (z. B. B oder C statt A), wird nicht berechnet.

**KI-Einsatz (VII.9):** Die KI ist ein Hilfsmittel; der AN bleibt verantwortlich. Eingereichte Inhalte werden nur zur Einordnung und Bearbeitung verarbeitet und nicht zum Training allgemeiner Modelle verwendet. Bei personenbezogenen Daten wird vorab eine Auftragsverarbeitung nach Art. 28 DSGVO geschlossen. Der AN weist den AG auf den KI-Einsatz hin.

**Form (VII.10):** Nachträge und Zusatzvereinbarungen genügen der Textform (E-Mail oder Ticketsystem). Unvermeidliche Zeitverschiebungen teilt der AN unverzüglich mit.

# 8. Datenschutz, Geheimhaltung und Dienstleister (XIV)

- Der AN verwertet Geschäfts- und Betriebsgeheimnisse des AG nicht und teilt sie Dritten nicht mit; der Vertragsinhalt ist vertraulich; die Pflicht gilt über das Vertragsende hinaus (XIV.1 bis 3).
- Eingesetzte Dienstleister gelten als genehmigte Dritte und dürfen Inhalte nur nach VII.9 verarbeiten; eine Änderung teilt der AN vorab in Textform mit (XIV.4).

| Dienstleister | Sitz | Zweck | Auftragsverarbeitung |
|:---|:---|:---|:---|
| [HOSTING-DIENSTLEISTER] | Deutschland | Hosting der Cloud-Umgebung | geschlossen |
| [KI-DIENSTLEISTER] | EU | Einordnung von Änderungswünschen und Sprachmodell des Chatbots (KI) | geschlossen |

# 9. Bewusst weggelassen

Präambel und Anschriften, Einzelheiten zu Pflichtenheft-Inhalten über Abschnitt 3 und 4 hinaus, Gerichtsstand, anwendbares Recht, Schriftformklausel und Salvatorische Klausel (XVI, XVII), Unterschriftsblock.
