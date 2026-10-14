# Notizen

Sammelstelle für Festlegungen und Textstellen, die später im n8n-Workflow oder in den anderen Dokumenten umgesetzt werden. Lose Arbeitsdatei aus Sprint 1, keine abgestimmte Fassung. Stand 2026-10-14. Das beschriebene Unternehmen und alle Zahlen sind fiktiv.

**Status der Angaben:** Zitate aus eigenen Entwürfen sind als solche gekennzeichnet. Was darunter als *Für die Umsetzung* steht, ist die Lesart des Eintragenden und noch keine Festlegung der Gruppe.

**Eintragen:** Neue Notiz unten anfügen, mit Quelle (welches Dokument, welche Ziffer) und Datum. Offene Platzhalter aus Entwürfen sammeln wir unten in einer Liste, damit sie nicht untergehen.

## Vertragsentwurf: Einordnung und Eskalation

Quelle: Vertragsentwurf Change-Request-Agent (Michi), Stand 2026-10-14. Ziffern wie im Entwurf. `[●]` sind dort noch offene Platzhalter.

### Ziffer 2: Eskalation an einen Mitarbeiter (immer, unabhängig vom Sicherheitswert)

- Die Änderung berührt Architektur, Datenmodell oder eine Schnittstelle.
- Die Änderung betrifft Sicherheit, Berechtigungen oder personenbezogene Daten.
- Der Änderungswunsch betrifft mehr als eine Komponente oder ist widersprüchlich oder unklar.
- Streit über die Auslegung des Vertrags oder frühere Einordnung (Überprüfung nach Ziffer 6.5).
- Die geschätzte Aufwandsgrenze von Kategorie A wird überschritten oder ist unklar.

*Für die Umsetzung:* Diese fünf Fälle sind ein Tor **vor** der Sicherheitsschwelle aus Ziffer 3 und greifen auch bei hohem Sicherheitswert. Im Workflow also eine eigene Prüfung, die unabhängig vom Schwellenwert zum Menschen leitet, nicht ein weiterer Zweig hinter der Schwelle.

Offen: Woran erkennt der Agent "berührt Architektur, Datenmodell oder Schnittstelle" und "mehr als eine Komponente"? Beides setzt Wissen über den Aufbau der Kundensoftware voraus, das in der Kundenäußerung meist nicht steht. Entweder gibt das Modell je Fall ein eigenes Feld dazu aus (und wir messen, wie verlässlich das ist), oder die Entwicklung liefert die Einschätzung zu. Zu klären in der Gruppe.

### Ziffer 3: Sicherheitsschwelle

> Erreicht das System bei der Einordnung einen Sicherheitswert von weniger als `[●]` % (Vorschlag: `[80]` %), prüft ein Mitarbeiter, bevor dem Kunden eine Einordnung mitgeteilt wird.

*Für die Umsetzung:* Der Workflow braucht je Einordnung einen numerischen Sicherheitswert und eine Verzweigung an der Schwelle. Zweite Hälfte des Satzes ist die eigentliche Wirkung: unter der Schwelle geht **nichts** an den Kunden, bevor ein Mensch gesehen hat.

Offen: Wie entsteht der Sicherheitswert, und ist er kalibriert? Ein selbst berichteter Wert des Modells ist nicht ohne weiteres eine Wahrscheinlichkeit. Das hängt an den Erfolgskriterien im [Kandidatenbogen](kandidatenbogen.md).

### Ziffer 4: Qualitätskontrolle

> Der Anbieter lässt mindestens `[●]` % der Einordnungen je `[Quartal]` durch einen Mitarbeiter gegenprüfen und erfasst Fehleinordnungen, insbesondere Änderungen der Kategorie B oder C, die als A freigegeben wurden. Die Ergebnisse stellt er dem Kunden auf Verlangen zur Verfügung.

*Für die Umsetzung:* Das ist keine Weiche, sondern eine Anforderung an Protokollierung und Ablage. Nötig sind: jede Einordnung wird mit Eingabe, Ergebnis, Sicherheitswert und Datum festgehalten; eine Stichprobe lässt sich daraus ziehen; das Ergebnis der Gegenprüfung wird zurückgeschrieben; daraus entsteht eine Auswertung, die dem Kunden vorgelegt werden kann.

Offen: Wo liegen diese Daten? Für `B oder C als A freigegeben` braucht es neben der Einordnung des Agenten die korrigierte Einordnung des Menschen als zweites Feld, sonst ist der Fehler später nicht zählbar.

### Kategorien A, B, C

Die Ziffern 2 und 4 verweisen auf Aufwandskategorien A, B und C, die im Repo noch nirgends definiert sind. Die Definition samt Aufwandsgrenze für A gehört in den Vertrag oder in die Leistungsbeschreibung und muss zum Workflow passen.

## Offene Platzhalter aus dem Vertragsentwurf

| Stelle | Platzhalter | Vorschlag im Entwurf |
|---|---|---|
| Ziffer 3 | Sicherheitswert, ab dem ein Mitarbeiter prüft | 80 % |
| Ziffer 4 | Anteil der Einordnungen in der Gegenprüfung | offen |
| Ziffer 4 | Zeitraum der Gegenprüfung | Quartal |
| Ziffer 2 | Aufwandsgrenze der Kategorie A | offen |
