"""
Modul 450 - Aufgabe 6: TDD fuer gutschein_anwenden().

REIHENFOLGE (Test-Driven Development):
  1. Schreibe HIER zuerst die Tests anhand der Spezifikation in gutschein.py (rot).
  2. Implementiere dann gutschein.py, bis die Tests gruen sind.
  3. Refactor - Tests bleiben gruen.

Das untenstehende Beispiel ist mit @unittest.skip deaktiviert, damit am Anfang
nichts kracht. Entferne die skip-Zeile, sobald du loslegst, und ergaenze weitere Tests.

Ausfuehren (im Ordner modul-450-testen):
    python -m unittest test_gutschein
"""
import unittest
from gutschein import gutschein_anwenden


class TestGutschein(unittest.TestCase):

    @unittest.skip("TODO: aktivieren, sobald du mit TDD startest")
    def test_willkommen10_gibt_10_prozent_rabatt(self):
        self.assertEqual(gutschein_anwenden(100, "WILLKOMMEN10"), 90.0)

    # TODO: "GRATIS5" zieht 5 CHF ab            (z.B. 20 -> 15)
    # TODO: "GRATIS5" nie unter 0               (z.B. 3  -> 0)
    # TODO: unbekannter Code -> Betrag unveraendert
    # TODO: betrag < 0 -> ValueError


if __name__ == '__main__':
    unittest.main()
