#!/usr/bin/env python3
"""Privatsphaere-Check: prueft jeden Push auf Dinge, die nicht ins Repo gehoeren.

Am Ende liest die MSIT mit, deshalb wird rot, was hier landet:
- echte Mailadressen in Dateien oder Commit-Texten (erlaubt: noreply,
  anthropic.com fuer Co-Author-Zeilen, reservierte Testdomains wie example.com)
- lokale Benutzerpfade, Schluessel und Tokens
- Wikilinks in Markdown (Verweise aus privaten Notizsammlungen)
- Schluessel- und Datenbankdateien (.env, .pem, .key, .sqlite, ...)

Geprueft werden nur neue Commits: auf main die des Pushes, auf jedem anderen
Branch alles, was noch nicht auf main liegt (also das, was gemerged wuerde).
"""
import os
import re
import subprocess
import sys

NULL_SHA = "0" * 40
ERLAUBTE_DOMAINS = ("users.noreply.github.com", "anthropic.com")
TEST_DOMAINS = ("example.com", "example.org", "example.net")
TEST_ENDUNGEN = (".example", ".test", ".invalid", ".localhost")

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@([A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)+)")
WIKILINK_RE = re.compile(r"\[\[[^\]\n]+\]\]")
MUSTER = [
    ("lokaler Benutzerpfad", re.compile(r"[A-Za-z]:[\\/]+Users[\\/]|/Users/\w|/home/\w", re.IGNORECASE)),
    (
        "Schlüssel oder Token",
        re.compile(
            r"ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_\-]{20,}|AKIA[0-9A-Z]{16}"
            r"|xox[abprs]-[A-Za-z0-9\-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----"
            r"|(?:api[_-]?key|secret|token|passwort|password)\s*[:=]\s*[\"']?[A-Za-z0-9_\-./+]{8,}",
            re.IGNORECASE,
        ),
    ),
]
# Nur Schluessel- und Datenbankdateien. PDF, Word und Excel sind erlaubt: fiktive
# Vertraege und Leistungsbeschreibungen sind echtes Projektmaterial (Knut, 2026-10-14).
VERBOTENE_ENDUNGEN = (".env", ".pem", ".key", ".p12", ".pfx", ".sqlite", ".db")


def maskiere(text):
    text = text or "(leer)"
    return text[:3] + "***" if len(text) > 6 else text


def domain_erlaubt(domain):
    d = domain.lower()
    return (d.endswith(ERLAUBTE_DOMAINS) or d.endswith(TEST_ENDUNGEN)
            or any(d == t or d.endswith("." + t) for t in TEST_DOMAINS))


def pruefe_text(text, wo):
    return [f"fremde Mailadresse in {wo} ({maskiere(m.group(0))})"
            for m in EMAIL_RE.finditer(text) if not domain_erlaubt(m.group(1))]


def pruefe_patch(patch):
    """Sucht in neuen Zeilen und Dateinamen eines `git log -p`-Textes."""
    probleme, datei = [], ""
    for zeile in patch.splitlines():
        # Binaerdateien haben keine +++-Zeile, nur "Binary files ... differ";
        # der Name kommt deshalb auch aus der diff-Kopfzeile.
        kopf = re.match(r"diff --git a/.* b/(.+)$", zeile)
        if kopf:
            datei = kopf.group(1).strip()
            if datei.lower().endswith(VERBOTENE_ENDUNGEN):
                probleme.append(f"verbotener Dateityp: {datei}")
            continue
        if zeile.startswith("+++ "):
            datei = zeile[4:].strip()
            datei = datei[2:] if datei.startswith("b/") else datei
            if datei.lower().endswith(VERBOTENE_ENDUNGEN):
                probleme.append(f"verbotener Dateityp: {datei}")
            continue
        if not zeile.startswith("+"):
            continue
        inhalt = zeile[1:]
        probleme += pruefe_text(inhalt, datei or "?")
        for name, rx in MUSTER:
            if rx.search(inhalt):
                probleme.append(f"{name} in {datei or '?'}")
        if datei.lower().endswith(".md") and WIKILINK_RE.search(inhalt):
            probleme.append(f"Wikilink in {datei}")
    return probleme


def bereich(branch, before, after, hauptbranch="main"):
    """Commit-Bereich als git-Argumente, None wenn nichts zu pruefen ist."""
    if not after or after == NULL_SHA:
        return None  # Branch geloescht
    if branch == hauptbranch:
        return [after] if not before or before == NULL_SHA else [f"{before}..{after}"]
    return [f"origin/{hauptbranch}..{after}"]


def _git(args):
    proc = subprocess.run(["git"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args[:2])}: {proc.stderr.strip()[:300]}")
    return proc.stdout


def pruefe_bereich(rev, git=_git):
    patch = git(["log", "-p", "--no-color", "-U0", "--format="] + rev)
    meldungen = git(["log", "--format=%B"] + rev)
    probleme = pruefe_patch(patch) + pruefe_text(meldungen, "Commit-Text")
    return list(dict.fromkeys(probleme))


def main():
    rev = bereich(os.environ.get("WACHE_BRANCH", ""), os.environ.get("WACHE_BEFORE", ""),
                  os.environ.get("WACHE_AFTER", ""))
    if rev is None:
        print("Nichts zu prüfen.")
        return 0
    probleme = pruefe_bereich(rev)
    zeilen = ["## Privatsphäre-Check", ""]
    if probleme:
        zeilen += ["Gefunden, bitte vor dem Merge entfernen:", ""] + [f"- {p}" for p in probleme]
    else:
        zeilen.append("Nichts gefunden.")
    bericht = "\n".join(zeilen)
    print(bericht)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(bericht + "\n")
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
