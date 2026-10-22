# Das Ende des Workflows: was wann wie passiert

Festlegung für den Teil des Change-Request-Agenten **hinter dem Knoten „Ergebnis vereinheitlichen"**: wie ein Fall abgeschlossen wird, wer entscheidet, was der Kunde bekommt und was protokolliert wird.

Entwurf von Michi, Stand 2026-10-22, mit KI-Unterstützung (Claude Code) erstellt und von der Gruppe noch nicht abgestimmt. Alle Unternehmen, Personen und Zahlen sind fiktiv.

**Grundlage:** die Fassung des Workflows aus Commit `3907f75`. Knuts spätere Fassung `b5bdae6` mit Outlook-Eingang und Kundenstamm ist noch nicht eingearbeitet — die neuen Knoten hängen aber alle hinter „Ergebnis vereinheitlichen", das es in beiden Fassungen gibt, und lassen sich deshalb übertragen.

**Zum Ausprobieren:** [change-request-agent-mit-ende-entwurf.json](../workflow/change-request-agent-mit-ende-entwurf.json) in n8n importieren (Neuer Workflow, Drei-Punkte-Menü, „Import from File"). Enthält den vollständigen Agenten einschließlich der zwölf neuen Knoten.

## Drei Grundsätze

**1. Immer ein Mensch.** Auch Kategorie A geht über eine Freigabe. Kein Fall erreicht den Kunden, ohne dass ein Mitarbeiter entschieden hat.

**2. Die Freigabe ist der Klick, das Senden ist Maschinensache.** Ziffer 6.4 verlangt, dass Angebote, Nachträge und Preise ausschließlich ein Mitarbeiter freigibt — nicht, dass er die Mail selbst tippt. Klickt er in Slack auf Freigeben, verschickt der Workflow. Nur so ist die Freigabe auch protokollierbar; schreibt der Mitarbeiter aus seinem eigenen Postfach, weiß der Workflow nichts davon und das Protokoll nach Ziffer 6.7 hat Löcher.

**3. Zwei Nachrichten an den Kunden.** Eine Eingangsbestätigung sofort, die eigentliche Antwort nach der Freigabe. Beide tragen die Ticketnummer im Betreff und laufen im selben Thread.

## Die Fallunterscheidung

Der Knoten `Fall und Antwortvorschlag aufbereiten` leitet aus Klasse, Urteil, Kategorie und Kontingentstand genau einen von sieben Fällen ab. Der Fall steuert alles Weitere.

| Fall | Bedingung | Antwort an den Kunden |
|---|---|---|
| `bug` | Klasse ist Bugreport | Als Fehlermeldung aufgenommen, es gelten die Reaktions- und Behebungszeiten. Kein Änderungsverfahren |
| `a_innerhalb` | Urteil inklusive oder Kategorie A, Kontingent reicht | Kategorie A, vom Leistungsumfang gedeckt, wird umgesetzt, kein Nachtrag |
| `a_ausserhalb` | wie oben, aber Kontingent knapp, aufgebraucht oder Periode abgelaufen | Kategorie A, aber Freigabe des Kunden in Textform nötig, Aufwandsschätzung folgt |
| `b` | Kategorie B | Zusatzleistung, Aufwandsschätzung folgt, Umsetzung erst nach Bestätigung in Textform |
| `c` | Kategorie C | Größere Änderung, Einzelangebot folgt, Nachtrag oder gesonderter Vertrag, Termine werden neu vereinbart |
| `e` | Kategorie E (nur Erstellungsvertrag) | Erforderliche Änderung, wird ohne Zusatzentgelt umgesetzt |
| `pruefung` | alles andere, auch unsichere Einordnungen | Wird von einem Mitarbeiter geprüft, Einordnung folgt gesondert |

Dazu kommt der Fall **Ablehnung**: lehnt der Mitarbeiter ab, ersetzt ein eigener Text die obige Antwort, mit seiner Begründung im Wortlaut.

**Zur Grenze zwischen `a_innerhalb` und `a_ausserhalb`:** Eigentlich entscheidet der geschätzte Aufwand in Euro gegen die Freigabegrenze des Kunden (Ziffer 6.3). Der Preis wird im Workflow aber noch nicht berechnet (`preis: null`). Solange das so ist, entscheidet ersatzweise der Kontingentstatus. Das ist eine Krücke und als solche im Code vermerkt.

## Der Ablauf Schritt für Schritt

```
Ergebnis vereinheitlichen
  ├─ Antwort senden          (unverändert, HTTP-Antwort)
  ├─ Log schreiben           (unverändert, legt die Protokollzeile an)
  └─ Kundenantwort nötig?
       ├─ nein → Kein Kundenkontakt nötig, bereits beantwortet
       └─ ja  → Fall und Antwortvorschlag aufbereiten
                  └─ Text der Eingangsbestätigung
                       └─ Eingangsbestätigung an Kunden          ← geht sofort raus
                            └─ Slack: Freigabe durch Projektleitung
                                 ├─ freigegeben → Standard-Antworttext je Kategorie
                                 └─ abgelehnt   → Slack: Begründung der Ablehnung
                                                    └─ Standard-Antworttext je Kategorie
                                                         └─ E-Mail an Kunden senden
                                                              └─ Freigabe ins Protokoll schreiben
```

**Kundenantwort nötig?** filtert ungültige Eingaben aus. Die sind an dieser Stelle schon erledigt (Grund gesetzt, HTTP 400 geschickt, protokolliert), und eine Kundenmail wäre gar nicht möglich, weil die Kunden-ID in diesen Fällen nicht A bis E ist. Der Zweig endet deshalb bewusst in einem No-Op-Knoten, damit auf der Canvas sichtbar ist, dass hier nichts vergessen wurde.

**Die Eingangsbestätigung steht in Reihe vor dem Slack-Knoten, nicht parallel.** Parallel würde n8n die Zweige nach Knotenposition abarbeiten, und der Send-and-Wait-Knoten blockiert — die Bestätigung käme dann erst nach der Freigabe, also womöglich Stunden später.

**Die Wartezeit auf die Freigabe ist auf 8 Stunden begrenzt.** Danach läuft der Fall über den Ablehnungszweig weiter, wird also nicht still liegengelassen.

## Was in den Nachrichten steht

### Eingangsbestätigung, sofort, ohne Freigabe

Dank, Ticketnummer, die Bitte die Nummer im Betreff zu lassen, und dass ein Mitarbeiter sich innerhalb der Servicezeiten meldet.

**Enthält ausdrücklich keine Einordnung und keine Zusage** — und sagt das auch. Solange kein Mitarbeiter geprüft hat, darf das System nach Ziffer 6.4 keine rechtsverbindliche Erklärung abgeben, und Ziffer 6.6 stellt klar, dass eine Einordnung durch das System allein keine Zahlungspflicht begründet.

### Die Antwort nach der Freigabe

Je nach Fall einer der sieben Texte. Jeder Text mit einer Einordnung enthält zusätzlich zwei Pflichtbestandteile:

- **Die Begründung und die Fundstelle** im Vertrag (Ziffer 6.5: Einordnung mit kurzer Begründung in Textform).
- **Den Hinweis auf das Überprüfungsrecht**: innerhalb von 5 Arbeitstagen kann der Kunde eine Überprüfung durch einen Mitarbeiter verlangen, bis dahin ruhen Umsetzung und Abrechnung (Ziffer 6.5).

Und alle Texte enden mit dem **Hinweis auf den KI-Einsatz**, den Ziffer 6.9 verlangt: „Zur Vorbereitung der Einordnung setzen wir ein KI-gestütztes System ein. Die Entscheidung und die Freigabe dieser Nachricht liegen bei einem Mitarbeiter."

**Kein Text nennt einen Preis.** Preise, Angebote und Nachträge gibt nach Ziffer 6.4 ausschließlich ein Mitarbeiter frei; die kommen außerhalb dieses Workflows.

## Die Slack-Karte

Ein Kanal für alle Änderungswünsche. Die Karte enthält Ticketnummer, Kunde, den abgeleiteten Fall und darunter den Vorschlag des Systems: Klasse, Urteil und Kategorie, Begründung, Fundstelle mit dem Vermerk ob das Zitat im Vertrag belegt ist, Sicherheitswert, Kontingentstand und die Freigabegrenze des Kunden.

Zwei Knöpfe: **Freigeben und an Kunden senden** oder **Ablehnen**. Bei Ablehnung folgt eine Freitextabfrage nach der Begründung, die wörtlich in die Kundenmail übernommen wird.

`captureResponder` ist eingeschaltet, Slack liefert damit zurück, wer geklickt hat. Das ist das Protokollfeld „Mitwirkung eines Mitarbeiters" aus Ziffer 6.7, das sonst leer bliebe. Es braucht eine zusätzliche Einstellung in der Slack-App.

## Das Protokoll

Eine Zeile je Ticket in der Data Table `capstone_agent_log`, zweimal angefasst: `Log schreiben` legt sie beim Eingang an, `Freigabe ins Protokoll schreiben` ergänzt sie nach der Freigabe per Update. Gematcht wird über `ticket_id`.

Die sechs Pflichtfelder aus Ziffer 6.7:

| Pflichtfeld | Spalte |
|---|---|
| Eingang | `zeit` |
| Einordnung | `urteil`, `kategorie`, `klasse` |
| Begründung | `grund`, bei Ablehnung `ablehnungsgrund` |
| Sicherheitswert | `sicherheit` |
| Mitwirkung eines Mitarbeiters | `freigabe_durch` |
| Freigabe | `freigabe_status`, `freigabe_zeit` |

Zusätzlich `fundstelle` und `zitat_belegt` (ob das Modellzitat wörtlich im Vertrag stand), weil beides für die Qualitätskontrolle nach Anlage 2 brauchbar ist.

**Achtung bei zwei Fallen**, die beim Nachbauen leicht übersehen werden:

- Die Spalte `ticket_id` enthält die **rohe** Ticket-ID, nicht die Anzeigenummer `CR-2026-nnnn`. Würde über die Anzeigenummer gematcht, fände das Update nie eine Zeile — ohne Fehlermeldung.
- Der Outlook-Knoten **überschreibt `$json`** mit seiner eigenen Antwort. Der Protokollknoten greift deshalb ausdrücklich auf `$('Standard-Antworttext je Kategorie')` zurück.

## Fehlerfälle

Alle Fehlerausgänge der letzten Schritte laufen in `Eskalation: Freigabe oder Versand fehlgeschlagen`. Ohne diesen Knoten würden Tickets bei einem Slack- oder Outlook-Ausfall stillschweigend verschwinden.

Eine Besonderheit: der Fehlerausgang der **Eingangsbestätigung** führt zweimal weiter — in die Eskalation **und** weiter in die Freigabe. Grund: fällt Outlook aus, soll die Freigabekarte trotzdem erscheinen, weil „immer ein Mensch" der Grundsatz ist. Gleichzeitig soll der fehlgeschlagene Versand nicht untergehen.

## Was eingerichtet werden muss

**Platzhalter in der Datei:**

| Platzhalter | Was hin muss |
|---|---|
| `<SLACK_KANAL_CHANGE_REQUESTS>` | Name des Slack-Kanals |
| `<MAIL_KUNDE_AUS_KUNDENSTAMM>` | Empfängeradresse, gehört in den Kundenstamm |
| `<DATA_TABLE_ID_CAPSTONE_AGENT_LOG>` | ID der Data Table, an zwei Knoten |
| `[ABSENDER]` | Grußformel in den Antworttexten |

**Credentials:** Slack und Microsoft Outlook. Dazu die bestehenden für OpenRouter und Google Drive.

**Die Data Table** braucht neben Knuts neun Spalten diese zehn: `ticket_nummer`, `urteil`, `kategorie`, `fundstelle`, `sicherheit` (Zahl), `zitat_belegt` (Wahrheitswert), `freigabe_status`, `freigabe_durch`, `freigabe_zeit`, `ablehnungsgrund`.

**Der Kundenstamm** braucht vier neue Spalten: Mailadresse, Vertragsart, Freigabegrenze in EUR und die Slack-Kennung des zuständigen Projektleiters. Die Freigabegrenzen stehen derzeit als Platzhalterwerte im Code des Knotens `Fall und Antwortvorschlag aufbereiten` — sie gehören in die Tabelle.

**`approvers` am Slack-Knoten ist leer**, aktuell darf also jeder im Kanal freigeben. Ziffer 6.4 verlangt einen qualifizierten Mitarbeiter; sobald die Slack-Kennungen da sind, sollte das eingeschränkt werden.

## Was bewusst offen ist

**Die Rückrichtung vom Kunden fehlt vollständig.** Bei Kategorie B verlangt der Vertrag „Umsetzung erst nach Bestätigung in Textform", bei C folgt ein Einzelangebot. Diese Bestätigung kommt per Mail zurück und müsste wieder im Ticket landen. Derzeit endet der Workflow mit dem Versand. Das ist der größte offene Block.

**Der Zustand „ruht" fehlt.** Verlangt der Kunde nach Ziffer 6.5 eine Überprüfung, ruhen Umsetzung und Abrechnung bis zur Entscheidung. Dafür braucht das Ticket einen Status, den der Workflow setzen und lesen kann.

**Die korrigierte Einordnung des Menschen wird nicht erfasst.** Das Protokoll zeigt, ob freigegeben oder abgelehnt wurde, aber nicht, ob der Mitarbeiter die Kategorie geändert hat. Genau das verlangt Anlage 2 Abschnitt 4 („insbesondere Änderungen der Kategorie B oder C, die als A freigegeben wurden"). Dafür müsste die Slack-Karte von zwei Knöpfen auf ein kleines Formular wechseln, in dem die Kategorie korrigierbar ist.

**Der Preis wird nicht berechnet.** Stundensatz mal Aufwand ist nicht angebunden, deshalb die oben beschriebene Krücke bei der Freigabegrenze.

**Die Reaktionszeit bei Fehlermeldungen** ist nur teilweise erfüllt. Die Eingangsbestätigung geht sofort raus, aber Ziffer 2.2 verlangt zusätzlich, dem Kunden die voraussichtliche Dauer der Störungsanalyse mitzuteilen. Die nennt der Text nicht.

**Beim Umzug in die Outlook-Fassung** ist ein Punkt zu beachten: der Zweig für ungültige Eingaben endet in einer Webhook-Antwort. Kommen die Anfragen per Mail, bekommt der Absender einer ungültigen Nachricht gar keine Rückmeldung.

## Wenn der Kundentext nach Slack geht

Dann verarbeitet Slack personenbezogene Daten für das Unternehmen und gehört damit in die Dienstleister-Tabelle in Ziffer 8.5 beziehungsweise XIV.5, die derzeit noch auf `[Name]` und `[Land]` steht. Alternative: in Slack geht nur die bereits geschwärzte Fassung, den Volltext sieht der Mitarbeiter im Ticketsystem. Die Schwärzung durch den Guardrails-Knoten liegt im Ablauf ohnehin vor der Klassifikation, der geschwärzte Text ist also vorhanden.

## Vertragsbezüge auf einen Blick

| Ziffer (Pflege, Wartung Plus) | Ziffer (Erstellung) | Was daraus folgt |
|---|---|---|
| 6.3 | VII.3 | Folgen je Kategorie, Freigabegrenze bei A |
| 6.4 | VII.4 | Menschliche Prüfung, nur Mitarbeiter geben frei |
| 6.5 | VII.5 | Einordnung mit Begründung, Überprüfung binnen 5 Arbeitstagen, Ruhen |
| 6.6 | VII.6 | Einordnung durch das System begründet keine Zahlungspflicht |
| 6.7 | VII.7 | Protokoll mit sechs Feldern, Aufbewahrung Vertragsdauer plus 12 Monate |
| 6.9 | VII.9 | Hinweis auf den KI-Einsatz, kein Training mit Kundeninhalten |
| 2.2 | — | Reaktions- und Behebungszeiten bei Fehlermeldungen |
