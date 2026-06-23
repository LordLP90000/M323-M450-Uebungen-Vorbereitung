"""
Modul 450 - Aufgabe 3: Tests fuer versandkosten().

Hier sind ZWEI Beispieltests als Vorlage. Ergaenze die fehlenden Tests so,
dass ALLE Aequivalenzklassen und ALLE Grenzwerte abgedeckt sind
(siehe aufgaben.md, Aufgabe 1 & 2).

Ausfuehren (im Ordner modul-450-testen):
    python -m unittest test_versandkosten
"""
import unittest
from versandkosten import versandkosten


class TestVersandkosten(unittest.TestCase):

    # -- Beispiel 1: ein normaler Wert aus der mittleren Klasse --
    def test_mittlere_klasse_normalwert(self):
        self.assertEqual(versandkosten(75), 3.90)

    # -- Beispiel 2: ein Grenzwert --
    def test_grenzwert_50(self):
        self.assertEqual(versandkosten(50), 3.90)

    # TODO: Klasse "kleiner Bestellwert" (0..49.99) -> 7.90
    # def test_kleine_klasse(self):
    #     self.assertEqual(versandkosten(20), 7.90)

    # TODO: Klasse "gratis" (>= 100) -> 0.00

    # TODO: Grenzwert 0  (genau an der unteren Grenze)

    # TODO: Grenzwert knapp unter 50  (z.B. 49.99) -> 7.90

    # TODO: Grenzwert knapp unter 100 (z.B. 99.99) -> 3.90

    # TODO: Grenzwert 100 -> 0.00

    # TODO: ungueltige Eingabe (negativ) -> ValueError
    #   Tipp:
    #   with self.assertRaises(ValueError):
    #       versandkosten(-1)


if __name__ == '__main__':
    unittest.main()
