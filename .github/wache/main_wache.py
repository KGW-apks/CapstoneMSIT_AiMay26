#!/usr/bin/env python3
"""Main-Wache: haelt main frei von Pushes anderer und jeden in seinem Branch.

Laeuft als GitHub Action bei jedem Push. Regeln (Team in team.json):

- Auf main pusht nur der Owner. Pusht jemand anderes, sichert die Wache den
  Stand in einen Branch `gerettet/<account>-<sha>`, setzt main auf den Stand
  vor dem Push zurueck und oeffnet ein Issue, das der Person zugewiesen ist
  (Fingerklopfer, mit Zaehler). Der Lauf endet rot.
- Jedes Mitglied pusht nur in seinen Branch (`michi`, auch `michi/...`).
  Ein Push in einen fremden Branch wird nicht zurueckgedreht, aber gemeldet.

Grenze: Die Wache reagiert nach dem Push, sie verhindert ihn nicht. Wer im
selben Push den Workflow aendert, schaltet sie aus. Sie schuetzt vor
Versehen, nicht vor Absicht.

Testmodus (workflow_dispatch): WACHE_TESTZIEL nennt einen Test-Branch, der
statt main zurueckgedreht wird. main ist als Testziel verboten.
"""
import json
import os
import subprocess
import sys

NULL_SHA = "0" * 40
TITEL_MARKE = "Fingerklopfer"


def lade_team(pfad):
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def entscheide(actor, branch, team):
    """'ok', 'zurueckdrehen' oder 'fremder_branch'."""
    if actor == team["owner"]:
        return "ok"
    if branch == team.get("hauptbranch", "main"):
        return "zurueckdrehen"
    eigener = team.get("mitglieder", {}).get(actor)
    if eigener and (branch == eigener or branch.startswith(eigener + "/")):
        return "ok"
    return "fremder_branch"


def zaehle_verstoesse(issues, actor):
    """Bisherige Fingerklopfer-Issues dieser Person (aus `gh issue list --json`)."""
    n = 0
    for issue in issues:
        logins = {a.get("login") for a in issue.get("assignees", [])}
        if TITEL_MARKE in issue.get("title", "") and actor in logins:
            n += 1
    return n


def titel_main(actor, nummer, ziel="main"):
    return f"{TITEL_MARKE} Nr. {nummer} für @{actor}: Push auf {ziel} zurückgedreht"


def text_main(actor, ziel, before, after, rettung, eigener, zurueckgedreht):
    eigen = eigener or "<dein-branch>"
    if zurueckgedreht:
        zustand = (
            f"`{ziel}` steht wieder auf `{before[:7]}`, dem Stand vor deinem Push. "
            "Deine Arbeit ist nicht verloren, sie liegt im Branch "
            f"`{rettung}`."
        )
    else:
        zustand = (
            f"**Zurückdrehen hat nicht geklappt.** `{ziel}` enthält deinen Push noch. "
            f"Eine Sicherung liegt in `{rettung}`. @{{owner}} muss das von Hand lösen."
        )
    return f"""Hallo @{actor},

du hast direkt auf `{ziel}` gepusht (Commit `{after[:7]}`). Auf `{ziel}` merged nur Knut, ihr arbeitet in euren eigenen Branches. So bleibt `{ziel}` der abgestimmte Stand, den am Ende die MSIT liest.

{zustand}

**So holst du deine Änderungen in deinen Branch:**

```
git fetch origin
git switch {eigen}
git merge origin/{rettung}
git push origin {eigen}
git branch -f {ziel} origin/{ziel}
```

Die letzte Zeile setzt dein lokales `{ziel}` auf den Stand von GitHub zurück, damit der nächste Push nicht wieder dort landet.

Die Regeln stehen in `CONTRIBUTING.md`. Bitte kommentiere hier kurz mit „verstanden“ und schließe das Issue.
"""


def titel_fremd(actor, branch):
    return f"Hinweis für @{actor}: Push in fremden Branch `{branch}`"


def text_fremd(actor, branch, eigener):
    eigen = f"`{eigener}`" if eigener else "deinen eigenen Branch (noch keiner eingetragen)"
    return f"""Hallo @{actor},

du hast in `{branch}` gepusht. Jede Person arbeitet nur in ihrem eigenen Branch, deiner ist {eigen}. Der Push bleibt stehen, bitte sprecht euch ab und verschiebt die Arbeit in den richtigen Branch.

Die Regeln stehen in `CONTRIBUTING.md`.
"""


def _run(cmd):
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        print(f"[wache] {' '.join(cmd[:3])}... Exit {proc.returncode}: {proc.stderr.strip()[:300]}")
    return proc.returncode, proc.stdout


def _issue(run, titel, text, actor):
    # Erst anlegen, dann zuweisen: `gh issue create --assignee` legt das Issue auch
    # dann an, wenn die Zuweisung scheitert (Testlauf 2026-10-14), ein zweiter
    # Versuch ergaebe eine Dublette.
    code, out = run(["gh", "issue", "create", "--title", titel, "--body", text])
    url = out.strip().splitlines()[-1] if code == 0 and out.strip() else ""
    if url:
        run(["gh", "issue", "edit", url, "--add-assignee", actor])
    return code


def fuehre_aus(aktion, actor, ziel, before, after, team, run=_run):
    """Fuehrt die Aktion aus. Rueckgabe: Exit-Code des Laufs (1 = Verstoss)."""
    if aktion == "ok":
        print(f"[wache] {actor} -> {ziel}: in Ordnung")
        return 0
    eigener = team.get("mitglieder", {}).get(actor)
    if aktion == "fremder_branch":
        _issue(run, titel_fremd(actor, ziel), text_fremd(actor, ziel, eigener), actor)
        return 1

    rettung = f"gerettet/{actor}-{after[:7]}"
    run(["git", "push", "origin", f"{after}:refs/heads/{rettung}"])
    zurueckgedreht = False
    if before and before != NULL_SHA:
        run(["git", "fetch", "origin", before])
        code, _ = run(["git", "push", "--force", "origin", f"{before}:refs/heads/{ziel}"])
        zurueckgedreht = code == 0
    code, out = run(["gh", "issue", "list", "--state", "all", "--search", f"{TITEL_MARKE} in:title",
                     "--json", "title,assignees", "--limit", "200"])
    try:
        bisher = zaehle_verstoesse(json.loads(out), actor) if code == 0 else 0
    except ValueError:
        bisher = 0
    text = text_main(actor, ziel, before or NULL_SHA, after, rettung, eigener, zurueckgedreht)
    _issue(run, titel_main(actor, bisher + 1, ziel), text.replace("{owner}", team["owner"]), actor)
    return 1


def main():
    team = lade_team(os.path.join(os.path.dirname(os.path.abspath(__file__)), "team.json"))
    actor = os.environ["WACHE_ACTOR"]
    testziel = os.environ.get("WACHE_TESTZIEL", "").strip()
    if testziel:
        if testziel == team.get("hauptbranch", "main"):
            print("[wache] Testmodus auf dem Hauptbranch ist verboten")
            return 2
        _run(["git", "fetch", "origin", testziel])
        after = _run(["git", "rev-parse", f"origin/{testziel}"])[1].strip()
        before = _run(["git", "rev-parse", f"origin/{testziel}~1"])[1].strip()
        aktion = "zurueckdrehen" if actor != team["owner"] else "ok"
        return fuehre_aus(aktion, actor, testziel, before, after, team)
    branch = os.environ["WACHE_BRANCH"]
    aktion = entscheide(actor, branch, team)
    return fuehre_aus(aktion, actor, branch, os.environ.get("WACHE_BEFORE", ""),
                      os.environ.get("WACHE_AFTER", ""), team)


if __name__ == "__main__":
    sys.exit(main())
