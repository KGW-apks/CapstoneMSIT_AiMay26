# Capstone
Abschlussprojekt der MSIT mit IHK-Zertifizierung

## Projekt
Change-Request-Agent für ein fiktives Softwarehaus. Ein n8n-Workflow ordnet Kundenäußerungen ein (Überlegung, Wunsch, Auftrag, Fehler, Reklamation), prüft sie gegen den Vertrag des Kunden und benennt die zuständige Rolle. Ein Mensch entscheidet jeden Fall.

## Gruppe
Knut, Michi, Sebastian

## Stand
Sprint 1, Entwurfsphase (2026-10-15), Architektur liegt als Entwurf vor. Es ist noch nichts gebaut.

## Inhalt
- `docs/fiktive-firma.md`: das fiktive Softwarehaus mit Rollen, Abteilungen, Personen, Kunden, Vertragsarten und Regeln
- `docs/kandidatenbogen.md`: der Use Case als ausgefüllter Kandidatenbogen (Prozess, KI-Stellen, Erfolgskriterien, Daten, Risiken, Plan)
- `docs/notizen.md`: Sammelstelle für Festlegungen und Textstellen, die später im Workflow umgesetzt werden (Arbeitsdatei, wächst weiter)
- `docs/schaubilder/organigramm`: Organigramm des fiktiven Softwarehauses (PNG und SVG)
- `docs/schaubilder/agent-aufgaben`: Aufgaben und Ausgänge des Agenten (PNG und SVG)
- `docs/schaubilder/architektur`: Ablauf des Agenten und die Umgebung jedes Schritts (PNG und SVG)

Die Dokumente sind Entwürfe aus Sprint 1, mit KI-Unterstützung (Claude Code) erstellt und von der Gruppe noch nicht abgestimmt.

## Mitarbeit
Jede Person arbeitet in ihrem eigenen Branch, `main` pflegt Knut. Regeln und Einrichtung in [CONTRIBUTING.md](CONTRIBUTING.md). Zwei GitHub Actions wachen darüber (`.github/workflows/`): die Main-Wache und der Privatsphäre-Check.

## Hinweis
Alle Unternehmen, Personen, Kunden und Zahlen sind frei erfunden. Annahmen sind als solche gekennzeichnet.
