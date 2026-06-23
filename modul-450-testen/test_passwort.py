"""
Modul 450 - Aufgabe 4: Tests fuer ist_sicher().

Leite die Testfaelle aus den Regeln ab (Aequivalenzklassen + Grenzwerte!)
und schreibe sie. Ein gueltiges Beispiel ist als Muster schon da.

Ausfuehren (im Ordner modul-450-testen):
    python -m unittest test_passwort
"""
import unittest
from passwort_pruefer import ist_sicher


class TestIstSicher(unittest.TestCase):

    # -- Beispiel: erfuellt alle Regeln (>=8 Zeichen, Ziffer, Grossbuchstabe) --
    def test_gueltiges_passwort(self):
        self.assertTrue(ist_sicher("Sicher12"))

    # TODO: zu kurz (< 8 Zeichen) -> False
    # TODO: keine Ziffer -> False
    # TODO: kein Grossbuchstabe -> False
    # TODO: Grenzwert genau 8 Zeichen, alle Regeln erfuellt -> True
    # TODO: Grenzwert 7 Zeichen -> False


if __name__ == '__main__':
    unittest.main()
