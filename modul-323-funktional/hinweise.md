# Hinweise – Modul 323 (Funktional programmieren)

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

> Spielregel: Hier stehen **Denkanstösse**, keine fertigen Lösungen. Schau erst hier rein,
> wenn du wirklich feststeckst. Danach: selbst tippen, Tests laufen lassen.

## Allgemein
- `map(funktion, liste)` und `filter(bedingung, liste)` geben einen **Iterator** zurück –
  verpacke das Ergebnis mit `list(...)`, damit du eine Liste bekommst.
- `functools.reduce(funktion, liste, startwert)` faltet eine Liste zu **einem** Wert zusammen.
  Beispielidee: `reduce(lambda akku, x: akku + x, zahlen, 0)`.
- Immutability heisst: nie die Eingabe verändern (kein `.append()` auf die Eingabeliste).
  Eine neue Liste/ein neues Tuple zurückgeben statt das Original zu mutieren.

## Block A
- **A1/A2:** Einzeiler mit `return`. Bei A2 hilft der Modulo-Operator `%` (Rest beim Teilen durch 2).
- **A3:** Eine Lambda hat die Form `lambda parameter1, parameter2: ausdruck`. Kein `return`, kein `def`.

## Block B
- **B1 `verdopple_alle`:** `map` mit einer Funktion, die `x * 2` macht. Ergebnis in `list(...)`.
- **B2 `nur_positive`:** `filter` mit einer Bedingung `x > 0`.
- **B3 `summe`:** `reduce` mit Startwert `0`. Genau deshalb klappt `[]` → `0`.
- **B4 `namen_gross`:** `map` mit `str.upper` – die Methode `upper()` macht Grossbuchstaben.
- **B5 `gesamtpreis`:** erst `map` (pro Produkt `p['preis'] * p['menge']`), dann `reduce` (Summe, Start `0`).

## Block C
- **C1 `multiplikator`:** Innerhalb der Funktion eine **innere** Funktion definieren, die `faktor`
  benutzt, und diese innere Funktion `return`en (Closure – die innere merkt sich `faktor`).
- **C2 `komponiere`:** `return` eine Funktion `lambda x: f(g(x))`. Reihenfolge beachten: erst `g`, dann `f`.
- **C3 `pipeline`:** Über alle `funktionen` laufen und den Wert Schritt für Schritt durchreichen.
  Tipp: Startwert ist der Eingabewert; in einer Schleife `wert = fn(wert)`. Bei 0 Funktionen bleibt der Wert.

## Block D
- **D1 `fakultaet`:** Basisfall `n == 0` → `1`. Sonst `n * fakultaet(n - 1)`.
- **D2 `summe_rekursiv`:** Basisfall leere Liste → `0`. Sonst `liste[0] + summe_rekursiv(liste[1:])`.
- **D3 `mit_element`:** Tuples kann man mit `+` verbinden: `werte + (element,)`. Das Komma macht ein 1-Tuple.
- **D4 `flach` (Bonus):** Über die Elemente laufen. Ist ein Element eine Liste (`isinstance(x, list)`),
  dann `flach(x)` rekursiv anhängen, sonst das Element selbst anhängen.

---
Wenn ein Hinweis nicht reicht: frag mich nach **einem** weiteren Tipp (nicht nach der Lösung) –
so bleibt das Aha-Erlebnis bei dir.
