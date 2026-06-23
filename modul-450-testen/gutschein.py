"""
Modul 450 - Aufgabe 6 (TDD).  HIER implementierst DU - aber Tests ZUERST!

Vorgehen (Test-Driven Development):
  1. Schreibe in test_gutschein.py zuerst die Tests (rot).
  2. Implementiere dann hier gerade so viel, dass die Tests gruen werden.
  3. Aufraeumen (refactor), Tests bleiben gruen.

Spezifikation fuer gutschein_anwenden(betrag, code):
  - code "WILLKOMMEN10" -> 10% Rabatt (betrag * 0.9)
  - code "GRATIS5"      -> 5 CHF Abzug, aber Ergebnis NIE unter 0
  - unbekannter Code     -> betrag unveraendert
  - betrag < 0           -> ValueError
"""


def gutschein_anwenden(betrag, code):
    # TODO (nach den Tests!): implementieren
    raise NotImplementedError("Aufgabe 6 - erst Tests schreiben, dann hier implementieren")
