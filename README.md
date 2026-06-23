# Übungen – Modul 323 & Modul 450

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

Übungsmaterial zum **selbst Lösen** für zwei Module der Informatik-Lehre (3. Lehrjahr):

| Modul | Thema | Ordner |
|-------|-------|--------|
| **323** | Funktional programmieren | [`modul-323-funktional/`](modul-323-funktional/) |
| **450** | Applikationen testen | [`modul-450-testen/`](modul-450-testen/) |

Sprache: **Python 3** (ist auf diesem Rechner installiert; das Test-Framework `unittest` ist eingebaut – du musst **nichts** installieren).

---

## So funktioniert das hier (wichtig!)

Das ist ein **Tutor**-Setup, kein Lösungsheft:

- Du **schreibst den Code selbst**. Ich gebe dir Aufgaben, Tests und Hinweise – aber **keine fertigen Lösungen**.
- **Die Tests sagen dir, ob es stimmt.** Rot = noch nicht fertig, Grün (`OK`) = geschafft.
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

1. `modul-323-funktional/README.md` lesen → Block A bis D der Reihe nach lösen.
2. `modul-450-testen/README.md` + `aufgaben.md` lesen → Aufgaben 1–6 der Reihe nach.

Viel Erfolg – dranbleiben lohnt sich. 💪
# M323-M450-Bungen-Vorbereitung
