"""
Tests fuer Modul 323.  NICHT veraendern (ausser du moechtest eigene Tests ergaenzen).

Ausfuehren (im Ordner modul-323-funktional):
    python -m unittest

Am Anfang sind ALLE Tests rot (NotImplementedError) - das ist Absicht.
Dein Ziel: Implementiere die Funktionen in aufgaben.py, bis alles gruen (OK) ist.
"""
import unittest
import aufgaben as a


class TestBlockA(unittest.TestCase):
    def test_quadriere(self):
        self.assertEqual(a.quadriere(0), 0)
        self.assertEqual(a.quadriere(4), 16)
        self.assertEqual(a.quadriere(-3), 9)

    def test_ist_gerade(self):
        self.assertTrue(a.ist_gerade(0))
        self.assertTrue(a.ist_gerade(8))
        self.assertFalse(a.ist_gerade(7))

    def test_addiere_ist_lambda(self):
        self.assertEqual(a.addiere(2, 3), 5)
        self.assertEqual(a.addiere(-1, 1), 0)


class TestBlockB(unittest.TestCase):
    def test_verdopple_alle(self):
        self.assertEqual(a.verdopple_alle([1, 2, 3]), [2, 4, 6])
        self.assertEqual(a.verdopple_alle([]), [])

    def test_verdopple_alle_aendert_eingabe_nicht(self):
        original = [1, 2, 3]
        a.verdopple_alle(original)
        self.assertEqual(original, [1, 2, 3])  # Immutability!

    def test_nur_positive(self):
        self.assertEqual(a.nur_positive([-2, 3, 0, 5]), [3, 5])
        self.assertEqual(a.nur_positive([-1, -2]), [])

    def test_summe(self):
        self.assertEqual(a.summe([1, 2, 3, 4]), 10)
        self.assertEqual(a.summe([]), 0)
        self.assertEqual(a.summe([42]), 42)

    def test_namen_gross(self):
        self.assertEqual(a.namen_gross(['ann', 'bo']), ['ANN', 'BO'])
        self.assertEqual(a.namen_gross([]), [])

    def test_gesamtpreis(self):
        produkte = [
            {'name': 'Stift', 'preis': 2.0, 'menge': 3},
            {'name': 'Heft', 'preis': 4.0, 'menge': 2},
        ]
        self.assertEqual(a.gesamtpreis(produkte), 14.0)
        self.assertEqual(a.gesamtpreis([]), 0)


class TestBlockC(unittest.TestCase):
    def test_multiplikator(self):
        mal3 = a.multiplikator(3)
        self.assertEqual(mal3(10), 30)
        self.assertEqual(mal3(0), 0)
        mal5 = a.multiplikator(5)
        self.assertEqual(mal5(2), 10)
        self.assertEqual(mal3(2), 6)  # mal3 bleibt unveraendert

    def test_komponiere(self):
        h = a.komponiere(lambda x: x * x, lambda x: x + 1)
        self.assertEqual(h(2), 9)   # (2+1)=3, 3*3=9
        self.assertEqual(h(0), 1)

    def test_pipeline(self):
        p = a.pipeline(lambda x: x + 1, lambda x: x * 2, lambda x: x - 3)
        self.assertEqual(p(5), 9)   # ((5+1)*2)-3
        identitaet = a.pipeline()
        self.assertEqual(identitaet(42), 42)


class TestBlockD(unittest.TestCase):
    def test_fakultaet(self):
        self.assertEqual(a.fakultaet(0), 1)
        self.assertEqual(a.fakultaet(1), 1)
        self.assertEqual(a.fakultaet(5), 120)

    def test_summe_rekursiv(self):
        self.assertEqual(a.summe_rekursiv([4, 5, 6]), 15)
        self.assertEqual(a.summe_rekursiv([]), 0)
        self.assertEqual(a.summe_rekursiv([7]), 7)

    def test_mit_element(self):
        original = (1, 2)
        neu = a.mit_element(original, 3)
        self.assertEqual(neu, (1, 2, 3))
        self.assertEqual(original, (1, 2))      # Original unveraendert
        self.assertIsInstance(neu, tuple)

    def test_flach_bonus(self):
        self.assertEqual(a.flach([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(a.flach([]), [])


if __name__ == '__main__':
    unittest.main()
