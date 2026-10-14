# Mitarbeit im Repo

Kurz und verbindlich für alle drei.

## Branches

- Michi arbeitet nur im Branch `michi`, Sebastian nur in `sebastian` (Unterbranches wie `michi/entwurf` sind erlaubt).
- Auf `main` pusht niemand direkt. Knut merged die Branches nach Durchsicht in `main`.
- Wer trotzdem auf `main` pusht, bekommt den Push automatisch zurückgedreht und ein Issue zugewiesen (mit Zähler). Die Arbeit geht nicht verloren, sie liegt danach in einem Branch `gerettet/...`, die Anleitung steht im Issue.
- Ein Push in den Branch eines anderen wird gemeldet.

Einmal einrichten:

```
git fetch origin
git switch -c michi        # beim ersten Mal, danach: git switch michi
git push -u origin michi
```

## Was nicht ins Repo gehört

Am Ende liest die MSIT mit. Bei jedem Push prüft der Privatsphäre-Check, und ein roter Haken heißt: so wird nicht gemerged.

- **Keine echten Mailadressen** in Dateien. Für Testdaten Domains wie `example.com` oder `kunde.test` verwenden.
- **Keine lokalen Pfade, Schlüssel, Tokens oder Passwörter.**
- **Kein Kursmaterial von MSIT oder IHK** (Folien, Skripte, Aufgabenblätter). Eigene fiktive Unterlagen wie Verträge oder Leistungsbeschreibungen dürfen PDF, Word oder Excel sein.
- **Keine Schlüssel- oder Datenbankdateien** (`.env`, `.pem`, `.key`, `.sqlite` und ähnliche).
