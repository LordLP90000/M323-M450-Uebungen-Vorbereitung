# Modul 323 – Funktional programmieren

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

Übungen zum **selbst Lösen** in **Python**. Du schreibst den Code, die Tests sagen dir, ob es stimmt.

## Dateien
| Datei | Zweck |
|-------|-------|
| [aufgaben.py](aufgaben.py) | **Hier arbeitest du.** 15 Funktionen (Block A–D) mit `TODO`. |
| [test_aufgaben.py](test_aufgaben.py) | Tests, die deine Lösungen prüfen. Nicht ändern. |
| [hinweise.md](hinweise.md) | Denkanstösse pro Aufgabe (keine Lösungen). |
| [theorie.md](theorie.md) | Theorie-/Quizfragen mit Selbstkontrolle. |

## Ablauf (pro Aufgabe)
1. Funktion in [aufgaben.py](aufgaben.py) implementieren (das `raise NotImplementedError(...)` löschen).
2. Tests laufen lassen:
   ```powershell
   cd "modul-323-funktional"
   python -m unittest
   ```
3. Rot → nochmal. Grün (`OK`) → nächste Aufgabe.
4. Nur einen Test gezielt prüfen, z. B.:
   ```powershell
   python -m unittest test_aufgaben.TestBlockB.test_summe
   ```

## Inhalt (Handlungsziele) & Reihenfolge
- **Block A – Pure Functions & Lambdas:** reine Funktionen, Seiteneffekte, Lambda.
- **Block B – Higher-Order Functions:** `map`, `filter`, `functools.reduce`, Immutability.
- **Block C – Komposition & Closures:** Funktionen zurückgeben, `komponiere`, `pipeline`.
- **Block D – Rekursion & Immutability:** Rekursion statt Schleife, unveränderliche Tuples.

Arbeite **A → B → C → D** der Reihe nach – die Blöcke bauen aufeinander auf.

## Empfehlung
Mach **erst** ein paar Theoriefragen aus [theorie.md](theorie.md) (Block A), **dann** die passenden
Coding-Aufgaben. So verbindest du Begriff und Praxis.
