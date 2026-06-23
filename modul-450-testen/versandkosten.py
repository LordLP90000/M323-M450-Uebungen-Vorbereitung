"""
Modul 450 - Code, der GETESTET werden soll.  (Diese Datei NICHT veraendern.)
"""


def versandkosten(bestellwert):
    """
    Berechnet die Versandkosten nach Bestellwert (in CHF).

    Regeln:
      bestellwert < 0           -> ValueError (ungueltig)
      0   <= bestellwert <  50  -> 7.90
      50  <= bestellwert < 100  -> 3.90
      bestellwert >= 100        -> 0.00  (gratis)
    """
    if bestellwert < 0:
        raise ValueError("Bestellwert darf nicht negativ sein")
    if bestellwert < 50:
        return 7.90
    if bestellwert < 100:
        return 3.90
    return 0.00
