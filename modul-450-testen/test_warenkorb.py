"""
Modul 450 - Aufgabe 5: Test Double / Mock fuer den Warenkorb.

Teste Warenkorb.gesamtsumme(), OHNE den echten Preisservice.
Ersetze ihn durch einen Mock (unittest.mock.MagicMock), dem du feste Preise
vorgibst. So testest du den Warenkorb unabhaengig vom Preisservice.

Ausfuehren (im Ordner modul-450-testen):
    python -m unittest test_warenkorb
"""
import unittest
from unittest.mock import MagicMock
from warenkorb import Warenkorb


class TestWarenkorb(unittest.TestCase):

    def test_leerer_warenkorb_summe_null(self):
        mock_service = MagicMock()
        korb = Warenkorb(mock_service)
        self.assertEqual(korb.gesamtsumme(), 0.0)

    # -- Beispiel: so gibst du dem Mock einen festen Preis vor --
    def test_eine_position(self):
        mock_service = MagicMock()
        mock_service.preis_fuer.return_value = 10.0   # jeder Artikel kostet 10
        korb = Warenkorb(mock_service)
        korb.hinzufuegen("A1", 3)
        self.assertEqual(korb.gesamtsumme(), 30.0)

    # TODO: mehrere Positionen mit UNTERSCHIEDLICHEN Preisen
    #   Tipp: mock_service.preis_fuer.side_effect = lambda nr: {"A1": 10.0, "A2": 5.0}[nr]

    # TODO: hinzufuegen mit menge <= 0 -> ValueError
    #   Tipp:
    #   with self.assertRaises(ValueError):
    #       korb.hinzufuegen("A1", 0)

    # TODO: anzahl_positionen() stimmt nach mehreren hinzufuegen()


if __name__ == '__main__':
    unittest.main()
