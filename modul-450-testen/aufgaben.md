# Aufgaben – Modul 450 (Applikationen testen)

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

In diesem Modul drehen wir den Spiess um: Der **Code ist schon da** – **du schreibst die Tests**.
So lernst du Testfälle systematisch abzuleiten statt „irgendwas zu klicken".

## Kurz-Begriffe (Deutsch / English)
- **Äquivalenzklasse (equivalence class):** Gruppe von Eingaben, die *gleich* behandelt werden. Pro Klasse genügt **ein** Testwert.
- **Grenzwertanalyse (boundary value analysis):** Fehler stecken oft an den **Grenzen** – teste direkt an der Grenze und knapp daneben.
- **Test Double:** Platzhalter für eine Abhängigkeit. Formen: **Dummy, Stub, Spy, Mock, Fake**.
- **TDD (Test-Driven Development):** Test zuerst (rot) → Code (grün) → aufräumen (refactor).
- **AAA / Arrange-Act-Assert** bzw. **Given-When-Then:** Aufbau eines Testfalls.

---

## Aufgabe 1 – Äquivalenzklassen bestimmen (Theorie, schriftlich)
Sieh dir [versandkosten.py](versandkosten.py) an. Fülle die Tabelle aus (auf Papier oder hier als Notiz):

| Klasse | Wertebereich | erwartetes Resultat | 1 Testwert |
|--------|--------------|---------------------|------------|
| ungültig | ... | ValueError | ... |
| klein | ... | 7.90 | ... |
| mittel | ... | 3.90 | ... |
| gratis | ... | 0.00 | ... |

## Aufgabe 2 – Grenzwertanalyse (Theorie, schriftlich)
Notiere **alle** interessanten Grenzwerte für `versandkosten` (an der Grenze **und** knapp darunter/darüber).
Tipp: Die Grenzen liegen bei **0, 50 und 100**. Welche Werte testest du rund um jede Grenze?

## Aufgabe 3 – Tests schreiben für `versandkosten`
Ergänze [test_versandkosten.py](test_versandkosten.py) so, dass **jede Äquivalenzklasse**
und **jeder Grenzwert** aus Aufgabe 1 & 2 durch einen Test abgedeckt ist – inkl. `ValueError` bei negativ.
Ziel: aussagekräftige Tests, nicht möglichst viele.

## Aufgabe 4 – Tests schreiben für `ist_sicher`
Leite aus den Regeln in [passwort_pruefer.py](passwort_pruefer.py) die Äquivalenzklassen ab
(zu kurz / keine Ziffer / kein Grossbuchstabe / alles erfüllt) und schreibe die Tests in
[test_passwort.py](test_passwort.py). Denk auch an den Grenzwert **genau 8 Zeichen**.

## Aufgabe 5 – Test Double / Mock (`Warenkorb`)
Der `Warenkorb` in [warenkorb.py](warenkorb.py) fragt einen `Preisservice`. Der **echte** Service
wirft im Test absichtlich einen Fehler – du **musst** ihn also mocken. Ergänze
[test_warenkorb.py](test_warenkorb.py): mehrere Positionen mit unterschiedlichen Preisen
(`side_effect`), Fehlerfall `menge <= 0`, und `anzahl_positionen()`.
> Frage zum Mitdenken: Warum ist ein Mock hier besser als der echte Service? (Stichworte: schnell, unabhängig, wiederholbar.)

## Aufgabe 6 – TDD (`gutschein_anwenden`)
Jetzt **Test zuerst**: Schreibe in [test_gutschein.py](test_gutschein.py) die Tests gemäss der
Spezifikation (siehe Kommentar in [gutschein.py](gutschein.py)) – **bevor** du die Funktion baust.
Dann implementiere [gutschein.py](gutschein.py) Schritt für Schritt, bis alle Tests grün sind.

---

## Tests ausführen
```powershell
cd "modul-450-testen"
python -m unittest            # alle Tests
python -m unittest test_versandkosten   # nur eine Datei
```
Am Anfang sind die mitgelieferten **Beispieltests grün** und `test_gutschein` ist **übersprungen** (skipped).
Deine Aufgabe: die `TODO`-Tests ergänzen.
