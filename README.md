# Übungen – Modul 323 & Modul 450

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

Übungsmaterial zum **selbst Lösen** für zwei Module der Informatik-Lehre (3. Lehrjahr):

| Modul | Thema | Ordner |
|-------|-------|--------|
| **323** | Funktional programmieren | [`modul-323-funktional/`](modul-323-funktional/) |
| **450** | Applikationen testen | [`modul-450-testen/`](modul-450-testen/) |

Sprache: **Python 3** (ist auf diesem Rechner installiert; das Test-Framework `unittest` ist eingebaut – du musst **nichts** installieren).

> **Hinweis zur Sprache:** Welche Sprache die Schule in 323/450 nimmt, ist noch offen. Python ist hier startklar und ideal zum Foundation-Bauen – die **Konzepte** (reine Funktionen, map/filter/reduce, Äquivalenzklassen, Mocks, TDD) sind in **jeder** Sprache gleich. Falls es später Java oder C# wird, bauen wir die Übungen schnell um; dein gelerntes Wissen bleibt gültig.

---

## So funktioniert das hier (wichtig!)

Das ist ein **Tutor**-Setup, kein Lösungsheft:

- Du **schreibst den Code selbst**. Ich gebe dir Aufgaben, Tests und Hinweise – aber **keine fertigen Lösungen**.
- **Die Tests sagen dir, ob es stimmt.** Rot = noch nicht fertig, Grün (`OK`) = geschafft.
- Pro Modul gibt es zusätzlich **`theorie.md`** mit Theorie-/Quizfragen und Selbstkontrolle – erst aus dem Kopf beantworten, dann vergleichen.
- Wenn du nicht weiterkommst: zuerst in die `hinweise.md` schauen. Hilft das nicht, frag mich nach **einem** Hinweis (nicht nach der Lösung) – so lernst du es wirklich.

Roter Faden:
- In **Modul 323** gebe ich dir die Tests → du schreibst den Code, bis sie grün sind.
- In **Modul 450** gebe ich dir den Code → du schreibst die Tests selbst.

---

## Schnellstart

Öffne ein Terminal **im jeweiligen Modul-Ordner** und führe die Tests aus.

**Modul 323:**
```powershell
cd "modul-323-funktional"
python -m unittest
```
Am Anfang sind alle Tests **rot** (`NotImplementedError`) – das ist Absicht. Dein Ziel: alle grün.

**Modul 450:**
```powershell
cd "modul-450-testen"
python -m unittest
```
Hier laufen die mitgelieferten **Beispiel-Tests** durch (grün). Deine Aufgabe: weitere Tests ergänzen.

> Tipp: Einen einzelnen Test gezielt laufen lassen, z. B.
> `python -m unittest test_aufgaben.TestBlockB.test_summe`

---

## Empfohlene Reihenfolge

1. **Modul 323:** `modul-323-funktional/README.md` lesen → ein paar Fragen aus `theorie.md` (Block A) → dann `aufgaben.py` Block A–D der Reihe nach lösen.
2. **Modul 450:** `modul-450-testen/README.md` + `aufgaben.md` lesen → Theoriefragen Block 1–2 aus `theorie.md` → dann Aufgaben 1–6 der Reihe nach.

Pro Modul also immer: **kurz Theorie (aus dem Kopf) → dann coden/testen → mit Tests prüfen.**

Viel Erfolg – dranbleiben lohnt sich. 💪
