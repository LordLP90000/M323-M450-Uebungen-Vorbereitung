"""
Modul 450 - Code fuer die Mocking-Aufgabe.  (NICHT veraendern.)

Der Warenkorb kennt die Preise NICHT selbst - er fragt einen Preisservice.
In den Tests sollst du den Preisservice durch einen Mock ersetzen, damit
der Test schnell und unabhaengig laeuft (kein echter DB-/Netzwerkzugriff).
"""


class Preisservice:
    """Stellt (in echt) Preise bereit, z.B. aus einer Datenbank."""

    def preis_fuer(self, artikel_nr):
        # In der Realitaet: langsamer DB-/Netzwerk-Zugriff.
        raise RuntimeError(
            "Echter Preisservice ist im Test nicht verfuegbar - mocke ihn!"
        )


class Warenkorb:
    def __init__(self, preisservice):
        self._preisservice = preisservice
        self._positionen = []  # Liste von (artikel_nr, menge)

    def hinzufuegen(self, artikel_nr, menge):
        if menge <= 0:
            raise ValueError("Menge muss positiv sein")
        self._positionen.append((artikel_nr, menge))

    def anzahl_positionen(self):
        return len(self._positionen)

    def gesamtsumme(self):
        total = 0.0
        for artikel_nr, menge in self._positionen:
            total += self._preisservice.preis_fuer(artikel_nr) * menge
        return total
