import json
import os
import unittest

import main_wache as w

TEAM = {"owner": "chef", "hauptbranch": "main", "mitglieder": {"anna-gh": "anna", "ben-gh": "ben"}}
VORHER = "a" * 40
NACHHER = "b" * 40


class Entscheidung(unittest.TestCase):
    def test_owner_darf_ueberall_hin(self):
        for branch in ("main", "anna", "irgendwas"):
            self.assertEqual(w.entscheide("chef", branch, TEAM), "ok")

    def test_mitglied_auf_main_wird_zurueckgedreht(self):
        self.assertEqual(w.entscheide("anna-gh", "main", TEAM), "zurueckdrehen")

    def test_unbekannter_account_auf_main_wird_zurueckgedreht(self):
        self.assertEqual(w.entscheide("fremd", "main", TEAM), "zurueckdrehen")

    def test_eigener_branch_und_unterbranches_sind_ok(self):
        self.assertEqual(w.entscheide("anna-gh", "anna", TEAM), "ok")
        self.assertEqual(w.entscheide("anna-gh", "anna/entwurf", TEAM), "ok")

    def test_fremder_branch_wird_gemeldet(self):
        self.assertEqual(w.entscheide("anna-gh", "ben", TEAM), "fremder_branch")
        self.assertEqual(w.entscheide("anna-gh", "annabell", TEAM), "fremder_branch")
        self.assertEqual(w.entscheide("fremd", "anna", TEAM), "fremder_branch")

    def test_echte_team_datei_ist_gueltig(self):
        pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "team.json")
        team = w.lade_team(pfad)
        self.assertIn("owner", team)
        self.assertEqual(w.entscheide(team["owner"], "main", team), "ok")
        for account, branch in team["mitglieder"].items():
            self.assertEqual(w.entscheide(account, branch, team), "ok")
            self.assertEqual(w.entscheide(account, "main", team), "zurueckdrehen")


class Zaehler(unittest.TestCase):
    def test_zaehlt_nur_eigene_fingerklopfer(self):
        issues = [
            {"title": "Fingerklopfer Nr. 1 für @anna-gh: ...", "assignees": [{"login": "anna-gh"}]},
            {"title": "Fingerklopfer Nr. 1 für @ben-gh: ...", "assignees": [{"login": "ben-gh"}]},
            {"title": "Anderes Thema", "assignees": [{"login": "anna-gh"}]},
        ]
        self.assertEqual(w.zaehle_verstoesse(issues, "anna-gh"), 1)
        self.assertEqual(w.zaehle_verstoesse([], "anna-gh"), 0)


class Ausfuehrung(unittest.TestCase):
    def setUp(self):
        self.aufrufe = []

    def run_fake(self, antworten=None):
        antworten = antworten or {}

        def run(cmd):
            self.aufrufe.append(cmd)
            for schluessel, antwort in antworten.items():
                if schluessel in " ".join(cmd):
                    return antwort
            return 0, ""
        return run

    def test_ok_tut_nichts(self):
        code = w.fuehre_aus("ok", "anna-gh", "anna", VORHER, NACHHER, TEAM, run=self.run_fake())
        self.assertEqual(code, 0)
        self.assertEqual(self.aufrufe, [])

    def test_main_push_rettet_dreht_zurueck_und_klopft(self):
        vorher_issues = json.dumps([{"title": "Fingerklopfer Nr. 1 für @anna-gh", "assignees": [{"login": "anna-gh"}]}])
        run = self.run_fake({"issue list": (0, vorher_issues), "issue create": (0, "https://x/issues/7\n")})
        code = w.fuehre_aus("zurueckdrehen", "anna-gh", "main", VORHER, NACHHER, TEAM, run=run)
        self.assertEqual(code, 1)
        rettung = f"{NACHHER}:refs/heads/gerettet/anna-gh-{NACHHER[:7]}"
        self.assertIn(["git", "push", "origin", rettung], self.aufrufe)
        self.assertIn(["git", "push", "--force", "origin", f"{VORHER}:refs/heads/main"], self.aufrufe)
        # Sicherung kommt vor dem Zuruecksetzen
        reihenfolge = [" ".join(c) for c in self.aufrufe]
        self.assertLess(reihenfolge.index(f"git push origin {rettung}"),
                        reihenfolge.index(f"git push --force origin {VORHER}:refs/heads/main"))
        issue = next(c for c in self.aufrufe if c[:3] == ["gh", "issue", "create"])
        self.assertIn("Nr. 2", issue[issue.index("--title") + 1])
        self.assertIn("auf main", issue[issue.index("--title") + 1])
        self.assertIn(["gh", "issue", "edit", "https://x/issues/7", "--add-assignee", "anna-gh"], self.aufrufe)
        text = issue[issue.index("--body") + 1]
        self.assertIn("git switch anna", text)
        self.assertIn(f"gerettet/anna-gh-{NACHHER[:7]}", text)

    def test_misslungenes_zuruecksetzen_wird_im_issue_gemeldet(self):
        run = self.run_fake({"--force": (1, "")})
        w.fuehre_aus("zurueckdrehen", "anna-gh", "main", VORHER, NACHHER, TEAM, run=run)
        issue = next(c for c in self.aufrufe if c[:3] == ["gh", "issue", "create"])
        text = issue[issue.index("--body") + 1]
        self.assertIn("nicht geklappt", text)
        self.assertIn("@chef", text)
        self.assertNotIn("{owner}", text)

    def test_ohne_vorgaenger_kein_force_push(self):
        w.fuehre_aus("zurueckdrehen", "anna-gh", "main", w.NULL_SHA, NACHHER, TEAM, run=self.run_fake())
        self.assertFalse(any("--force" in c for c in self.aufrufe))

    def test_genau_ein_issue_auch_wenn_zuweisung_scheitert(self):
        run = self.run_fake({"issue create": (0, "https://x/issues/3\n"), "--add-assignee": (1, "")})
        w.fuehre_aus("fremder_branch", "fremd", "anna", VORHER, NACHHER, TEAM, run=run)
        erstellt = [c for c in self.aufrufe if c[:3] == ["gh", "issue", "create"]]
        self.assertEqual(len(erstellt), 1)
        self.assertNotIn("--assignee", erstellt[0])

    def test_testziel_steht_im_titel(self):
        self.assertIn("auf wache-test", w.titel_main("x", 1, "wache-test"))

    def test_fremder_branch_dreht_nichts_zurueck(self):
        code = w.fuehre_aus("fremder_branch", "anna-gh", "ben", VORHER, NACHHER, TEAM, run=self.run_fake())
        self.assertEqual(code, 1)
        self.assertFalse(any(c[:2] == ["git", "push"] for c in self.aufrufe))


class Testmodus(unittest.TestCase):
    def test_hauptbranch_als_testziel_ist_verboten(self):
        alt = dict(os.environ)
        try:
            os.environ.update({"WACHE_ACTOR": "jemand", "WACHE_TESTZIEL": "main"})
            self.assertEqual(w.main(), 2)
        finally:
            os.environ.clear()
            os.environ.update(alt)


if __name__ == "__main__":
    unittest.main()
