# Modul 450 – Applikationen testen

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

Übungen zum **selbst Lösen** in **Python** (Test-Framework `unittest`, eingebaut – kein Setup).
Hier ist der **Code schon da** – **du schreibst die Tests**.

## Dateien
| Datei | Zweck |
|-------|-------|
| [aufgaben.md](aufgaben.md) | **Start hier.** Aufgaben 1–6 + Begriffe. |
| [versandkosten.py](versandkosten.py) · [passwort_pruefer.py](passwort_pruefer.py) · [warenkorb.py](warenkorb.py) | Vorgegebener Code zum Testen (nicht ändern). |
| [gutschein.py](gutschein.py) | TDD-Aufgabe: erst Tests, dann hier implementieren. |
| [test_versandkosten.py](test_versandkosten.py) · [test_passwort.py](test_passwort.py) · [test_warenkorb.py](test_warenkorb.py) · [test_gutschein.py](test_gutschein.py) | **Hier arbeitest du** – Tests ergänzen (`TODO`). |
| [hinweise.md](hinweise.md) | Denkanstösse + unittest-Spickzettel. |
| [theorie.md](theorie.md) | Theorie-/Quizfragen mit Selbstkontrolle. |

## Tests ausführen
```powershell
cd "modul-450-testen"
python -m unittest                      # alle Tests
python -m unittest test_versandkosten   # nur eine Datei
```
Beim ersten Lauf sind die **Beispieltests grün** und `test_gutschein` ist **skipped**.
Deine Aufgabe: die `TODO`-Tests schreiben.

## Inhalt (Handlungsziele) & Reihenfolge
1. **Äquivalenzklassen** bestimmen (Aufgabe 1)
2. **Grenzwertanalyse** (Aufgabe 2)
3. **Unit-Tests** schreiben: `versandkosten`, `ist_sicher` (Aufgaben 3–4)
4. **Test Doubles / Mock**: `Warenkorb` (Aufgabe 5)
5. **TDD**: `gutschein_anwenden` (Aufgabe 6)

## Empfehlung
Lies zuerst die Begriffe in [aufgaben.md](aufgaben.md) und mach **Block 1–2** der Fragen in
[theorie.md](theorie.md). Dann Aufgabe 1 → 6 der Reihe nach.
