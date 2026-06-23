"""
Modul 323 - Funktional programmieren
Uebungsaufgaben (Python)

SO ARBEITEST DU:
  1. Implementiere jede Funktion an der Stelle "TODO".
  2. Loesche das  raise NotImplementedError(...)  und schreibe deinen Code.
  3. Fuehre die Tests aus:   python -m unittest
  4. Ziel: Alle Tests sind gruen (OK).

REGELN der funktionalen Programmierung in diesen Aufgaben:
  - KEINE Veraenderung der Eingabeparameter (Immutability). Gib immer NEUE Werte zurueck.
  - KEINE globalen Variablen veraendern, KEIN print/input in den Funktionen (keine Seiteneffekte).
  - Wo gefordert: nutze map / filter / functools.reduce / lambda statt einer for-Schleife.

Kommst du nicht weiter?  ->  schau in  hinweise.md  (Hinweise, keine Loesungen).
"""

from functools import reduce  # fuer die reduce-Aufgaben (B3, B5)


# =============================================================
# Block A - Pure Functions & Lambdas
# =============================================================

def quadriere(x):
    """Gib das Quadrat von x zurueck (x * x). Reine Funktion."""
    # TODO: implementieren
    raise NotImplementedError("Aufgabe A1")


def ist_gerade(n):
    """Gib True zurueck, wenn n gerade ist, sonst False."""
    # TODO
    raise NotImplementedError("Aufgabe A2")


# A3: Definiere  addiere  als LAMBDA (nicht mit def).
#     Ersetze None durch einen lambda-Ausdruck, der zwei Zahlen addiert.
addiere = None  # TODO:  addiere = lambda a, b: ...


# =============================================================
# Block B - Funktionen hoeherer Ordnung (map / filter / reduce)
# =============================================================

def verdopple_alle(zahlen):
    """
    Gib eine NEUE Liste zurueck, in der jede Zahl verdoppelt ist. Nutze map().
    Die Eingabeliste darf NICHT veraendert werden.
    Beispiel: [1, 2, 3] -> [2, 4, 6]
    """
    raise NotImplementedError("Aufgabe B1")


def nur_positive(zahlen):
    """
    Gib eine NEUE Liste mit nur den Zahlen > 0 zurueck. Nutze filter().
    Beispiel: [-2, 3, 0, 5] -> [3, 5]
    """
    raise NotImplementedError("Aufgabe B2")


def summe(zahlen):
    """
    Berechne die Summe ALLER Zahlen mit functools.reduce().
    Die eingebaute Funktion sum() ist hier NICHT erlaubt.
    Beispiel: [1, 2, 3, 4] -> 10 ;  [] -> 0
    """
    raise NotImplementedError("Aufgabe B3")


def namen_gross(namen):
    """
    Gib eine neue Liste zurueck, in der jeder Name in GROSSBUCHSTABEN steht. Nutze map().
    Beispiel: ['ann', 'bo'] -> ['ANN', 'BO']
    """
    raise NotImplementedError("Aufgabe B4")


def gesamtpreis(produkte):
    """
    produkte ist eine Liste von Dicts:  {'name': str, 'preis': float, 'menge': int}
    Berechne die Gesamtsumme (preis * menge, ueber alle Produkte summiert).
    Tipp: zuerst map (preis * menge), dann reduce (aufsummieren).
    Beispiel:
      [{'name': 'Stift', 'preis': 2.0, 'menge': 3},
       {'name': 'Heft',  'preis': 4.0, 'menge': 2}]  ->  14.0
    """
    raise NotImplementedError("Aufgabe B5")


# =============================================================
# Block C - Funktionskomposition & Closures
# =============================================================

def multiplikator(faktor):
    """
    Closure: Gib eine FUNKTION zurueck, die ihr Argument mit  faktor  multipliziert.
    Beispiel:
      mal3 = multiplikator(3)
      mal3(10) -> 30
    """
    raise NotImplementedError("Aufgabe C1")


def komponiere(f, g):
    """
    Gib eine neue Funktion zurueck, die zuerst g und dann f anwendet:  f(g(x)).
    Beispiel:
      h = komponiere(lambda x: x * x, lambda x: x + 1)
      h(2) -> 9    (zuerst 2+1=3, dann 3*3=9)
    """
    raise NotImplementedError("Aufgabe C2")


def pipeline(*funktionen):
    """
    Gib eine Funktion zurueck, die alle uebergebenen Funktionen NACHEINANDER
    (von links nach rechts) auf den Eingabewert anwendet.
    Beispiel:
      p = pipeline(lambda x: x + 1, lambda x: x * 2, lambda x: x - 3)
      p(5) -> ((5 + 1) * 2) - 3 = 9
    Bei null Funktionen: gib den Wert unveraendert zurueck.
    """
    raise NotImplementedError("Aufgabe C3")


# =============================================================
# Block D - Rekursion & Immutability
# =============================================================

def fakultaet(n):
    """
    Berechne n! REKURSIV (ohne Schleife).  0! = 1.
    Beispiel: 5 -> 120
    """
    raise NotImplementedError("Aufgabe D1")


def summe_rekursiv(zahlen):
    """
    Summiere eine Liste REKURSIV (ohne Schleife, ohne sum() / reduce()).
    Beispiel: [4, 5, 6] -> 15 ;  [] -> 0
    """
    raise NotImplementedError("Aufgabe D2")


def mit_element(werte, element):
    """
    Immutability-Uebung:  werte  ist ein TUPLE. Gib ein NEUES Tuple zurueck,
    das zusaetzlich  element  am Ende enthaelt. Das Original bleibt unveraendert.
    Beispiel: mit_element((1, 2), 3) -> (1, 2, 3)
    """
    raise NotImplementedError("Aufgabe D3")


def flach(verschachtelt):
    """
    (BONUS) Mache eine verschachtelte Liste flach - REKURSIV.
    Beispiel: [1, [2, [3, 4]], 5] -> [1, 2, 3, 4, 5]
    Tipp: pruefe mit  isinstance(x, list), ob ein Element selbst eine Liste ist.
    """
    raise NotImplementedError("Aufgabe D4 (Bonus)")
