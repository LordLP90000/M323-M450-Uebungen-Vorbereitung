# Hinweise – Modul 450 (Applikationen testen)

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

> Denkanstösse, keine fertigen Testlösungen. Erst selbst versuchen!

## unittest-Grundgerüst
```python
import unittest
from modul import funktion

class TestXY(unittest.TestCase):
    def test_etwas(self):
        self.assertEqual(funktion(eingabe), erwartet)

if __name__ == '__main__':
    unittest.main()
```

## Nützliche Assertions
- `self.assertEqual(a, b)` – gleich?
- `self.assertTrue(x)` / `self.assertFalse(x)` – Wahrheitswert.
- Erwartete Exception:
  ```python
  with self.assertRaises(ValueError):
      funktion(boese_eingabe)
  ```

## Aufgabe 1 & 2 (Äquivalenzklassen / Grenzwerte)
- Pro Klasse genügt **ein** Repräsentant – aber **jede** Klasse braucht einen.
- Grenzwerte kommen **paarweise**: direkt an der Grenze und knapp daneben.
  Bei Grenze 50 also z. B. `49` (bzw. `49.99`) und `50`.

## Aufgabe 3 (`versandkosten`)
- Denk an **vier** Klassen (ungültig / klein / mittel / gratis) **plus** die Grenzwerte 0, 50, 100.
- Den negativen Fall mit `assertRaises(ValueError)` prüfen, nicht mit `assertEqual`.

## Aufgabe 4 (`ist_sicher`)
- Baue für jede „Verletzung" genau einen Testfall: zu kurz, ohne Ziffer, ohne Grossbuchstaben.
- Positiv-Test nicht vergessen (alle Regeln erfüllt). Grenzwert: **genau 8** Zeichen vs. **7**.

## Aufgabe 5 (Mock)
- `MagicMock()` erzeugt ein Objekt, das beliebige Methoden „kann".
- Fester Rückgabewert: `mock.preis_fuer.return_value = 10.0`.
- Unterschiedliche Werte je Argument: `mock.preis_fuer.side_effect = lambda nr: {...}[nr]`.
- Du gibst diesen Mock dem `Warenkorb(...)` statt des echten `Preisservice`.

## Aufgabe 6 (TDD)
- Schreibe **einen** Test, sieh ihn **rot** scheitern, mach ihn mit minimalem Code **grün**, dann nächster Test.
- Reihenfolge der Fälle: Normalfall „WILLKOMMEN10" → „GRATIS5" → „nie unter 0" → unbekannter Code → `ValueError`.
- `assertAlmostEqual` kann bei Kommazahlen helfen, falls dich Rundung ärgert.

---
Stecken bleiben? Frag mich nach **einem** nächsten Tipp – ich verrate die Tests nicht, ich zeige dir, wo du ansetzen kannst.
