import unittest

import privatsphaere as p

# Testdaten werden aus Teilen gebaut, damit der Check (und andere Waechter)
# diese Datei nicht selbst als Fund melden.
AT = "@"
PRIVAT = "anna" + AT + "gmail.com"
NOREPLY = "123+anna" + AT + "users.noreply.github.com"
BEISPIEL = "info" + AT + "nordlicht.example.com"


def patch(datei, *zeilen):
    return "\n".join([f"+++ b/{datei}"] + [f"+{z}" for z in zeilen])


class Mails(unittest.TestCase):
    def test_noreply_und_webcommits_sind_ok(self):
        self.assertEqual(p.pruefe_mails([NOREPLY, p.WEB_COMMITTER, ""]), [])

    def test_private_commit_mail_wird_maskiert_gemeldet(self):
        probleme = p.pruefe_mails([PRIVAT, PRIVAT])
        self.assertEqual(len(probleme), 1)
        self.assertNotIn(PRIVAT, probleme[0])


class Patch(unittest.TestCase):
    def test_fremde_mail_in_datei(self):
        self.assertTrue(p.pruefe_patch(patch("docs/a.md", "Kontakt: " + PRIVAT)))

    def test_testdomains_und_coauthor_sind_erlaubt(self):
        claude = "noreply" + AT + "anthropic.com"
        self.assertEqual(p.pruefe_patch(patch("daten/mails.json", BEISPIEL, "x" + AT + "kunde.test", claude)), [])

    def test_lokaler_pfad(self):
        pfad = "C:" + "\\" + "Users" + "\\" + "jemand\\Desktop"
        self.assertTrue(p.pruefe_patch(patch("notiz.md", pfad)))
        self.assertTrue(p.pruefe_patch(patch("skript.sh", "cd /" + "home/jemand")))

    def test_schluessel(self):
        self.assertTrue(p.pruefe_patch(patch("cfg.py", "x = 'ghp" + "_" + "a" * 30 + "'")))
        self.assertTrue(p.pruefe_patch(patch("cfg.env.example", "pass" + "word = hunter2hunter2")))

    def test_wikilink_nur_in_markdown(self):
        link = "[[" + "Geheime Notiz" + "]]"
        self.assertTrue(p.pruefe_patch(patch("docs/a.md", link)))
        self.assertEqual(p.pruefe_patch(patch("daten/x.json", '{"a": [[1, 2]]}')), [])

    def test_fremdformate(self):
        self.assertTrue(p.pruefe_patch("+++ b/material/folien.pptx"))
        self.assertTrue(p.pruefe_patch("+++ b/Skript.PDF"))
        self.assertEqual(p.pruefe_patch("+++ b/docs/bild.png"), [])

    def test_geloeschte_zeilen_zaehlen_nicht(self):
        self.assertEqual(p.pruefe_patch("+++ b/a.md\n-" + PRIVAT), [])

    def test_saubere_zeilen(self):
        self.assertEqual(p.pruefe_patch(patch("docs/a.md", "Ein ganz normaler Satz.", "token: ${{ github.token }}")), [])


class Bereich(unittest.TestCase):
    V, N = "a" * 40, "b" * 40

    def test_main_prueft_nur_den_push(self):
        self.assertEqual(p.bereich("main", self.V, self.N), [f"{self.V}..{self.N}"])
        self.assertEqual(p.bereich("main", p.NULL_SHA, self.N), [self.N])

    def test_anderer_branch_prueft_alles_noch_nicht_gemergte(self):
        self.assertEqual(p.bereich("anna", self.V, self.N), [f"origin/main..{self.N}"])
        self.assertEqual(p.bereich("anna", p.NULL_SHA, self.N), [f"origin/main..{self.N}"])

    def test_geloeschter_branch(self):
        self.assertIsNone(p.bereich("anna", self.V, p.NULL_SHA))


class Gesamt(unittest.TestCase):
    def test_pruefe_bereich_sammelt_alles_ohne_dubletten(self):
        antworten = {
            "%ae%n%ce": NOREPLY + "\n" + PRIVAT,
            "-p": patch("a.md", "Kontakt " + PRIVAT, "Kontakt " + PRIVAT),
            "%B": "Commit\n\nCo-authored-by: X <" + NOREPLY + ">",
        }

        def git(args):
            return next(v for k, v in antworten.items() if k in " ".join(args))

        probleme = p.pruefe_bereich(["x..y"], git=git)
        self.assertEqual(len(probleme), 2)


if __name__ == "__main__":
    unittest.main()
