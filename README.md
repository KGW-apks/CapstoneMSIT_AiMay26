# Capstone
Abschlussprojekt der MSIT mit IHK-Zertifizierung

## Projekt
Change-Request-Agent für ein fiktives Softwarehaus. Ein n8n-Workflow ordnet Kundenäußerungen ein (Fehlermeldung, Überlegung, Wunsch, Auftrag, Sonstiges), prüft sie gegen den Vertrag des Kunden und benennt die zuständige Rolle. Ein Mensch entscheidet jeden Fall.

## Gruppe
Knut, Michael

## Stand
Stand 2026-10-28: Die Kapitel 1 bis 6 der Projektarbeit und die Präsentation liegen vor. Kapitel 1 bis 5 sind von der Gruppe gegengelesen, Kapitel 6 enthält die Reflexionen beider Gruppenmitglieder. Der Workflow läuft in einer lokalen n8n-Instanz im Testbetrieb: Eingang über einen Postfach-Ordner, Freigabe über Slack.

## Inhalt
- `docs/kapitel-1-ist-und-soll.pdf`: Kapitel 1, Ist- und Soll-Situation mit den Erfolgskriterien K1 bis K6
- `docs/kapitel-2-einsatzbereiche.pdf`: Kapitel 2, mögliche KI-Einsatzbereiche und der gewählte Umfang
- `docs/kapitel-3-tool-vergleich.pdf`: Kapitel 3, Vergleich von drei Aufbauvarianten mit ersten Messungen
- `docs/kapitel-4-tool-auswahl-und-einsatzplanung.pdf`: Kapitel 4, begründete Auswahl und Einsatzplanung mit Pilotphase
- `docs/kapitel-5-erfolgskontrolle-kosten-und-nutzen.pdf`: Kapitel 5, Erfolgskontrolle mit Testrunden, Kennzahlen, Kosten und Nutzen
- `docs/kapitel-6-projektabschluss-und-ausblick.pdf`: Kapitel 6, Projektabschluss mit Stärken, Grenzen, Zielkonflikten, Wirtschaftlichkeit, nächsten Schritten und Reflexion
- `docs/praesentation/praesentation-change-request-agent.html`: die Präsentation, 22 Folien für rund 30 Minuten, im Browser öffnen, Pfeiltasten zum Blättern, F für Vollbild
- `docs/praesentation/sprechskript-change-request-agent.html`: das Sprechskript zur Präsentation, je Folie Kernpunkt und Sprechtext
- `docs/praesentation/backup-durchlauf.mp4`: Backup-Video des Durchlaufs (Mail, n8n, Slack, Freigabe), 77 Sekunden, für den Fall, dass die Live-Demo scheitert
- `docs/fiktive-firma.md`: das fiktive Softwarehaus mit Rollen, Abteilungen, Personen, Kunden, Vertragsarten und Regeln
- `docs/kandidatenbogen.md`: der Use Case als ausgefüllter Kandidatenbogen (Prozess, KI-Stellen, Erfolgskriterien, Daten, Risiken, Plan)
- `docs/kunden/firma-a` bis `firma-e`: je Kunde Vertrag, Beschreibung und anonymisierte Kurzfassung für den Agenten (Word und Markdown)
- `docs/tests/testbatterie-change-request-agent.docx`: 20 Testfälle für die Kunden A bis E mit Ergebnissen vom 23.10.2026, Befunden und Änderungsvorschlägen, abgeglichen mit dem Workflow-Stand 42ab6d2
- `workflow/change-request-agent.json`: der Hauptworkflow des Agenten, zum Importieren in n8n. Er trennt eine Mail in einzelne Anliegen
- `workflow/anliegen-bearbeiten.json`: der Sub-Workflow, der je Anliegen klassifiziert, den Vertrag prüft und an das Slack-Ende übergibt
- `workflow/slack-ende.json`: der Sub-Workflow für Weitergabe und Freigabe über Slack
- `docs/vorlagen/`: die drei Standardverträge (Pflege, Erstellung, Wartung Plus)
- `docs/schaubilder/organigramm`: Organigramm des fiktiven Softwarehauses (PNG und SVG)
- `docs/schaubilder/agent-aufgaben`: Aufgaben und Ausgänge des Agenten (PNG und SVG)
- `docs/schaubilder/architektur`: Ablauf des Agenten und die Umgebung jedes Schritts (PNG und SVG)

Alle Dokumente sind mit KI-Unterstützung erstellt.

## Mitarbeit
Jede Person arbeitet in ihrem eigenen Branch, `main` pflegt Knut. Zwei GitHub Actions wachen darüber (`.github/workflows/`): die Main-Wache und der Privatsphäre-Check.

## Hinweis
Alle Unternehmen, Personen, Kunden und Zahlen sind frei erfunden. Annahmen sind als solche gekennzeichnet.
