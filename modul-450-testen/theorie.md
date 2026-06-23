# Theorie- & Quizfragen – Modul 450 (Applikationen testen)

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

> **So nutzt du das:** Beantworte aus dem Kopf, **dann** unten bei **Selbstkontrolle** vergleichen.
> Fachbegriffe Deutsch **und** English. Nicht vorher spicken – das Erinnern ist der Lerneffekt.

## Block 1 – Testkonzept & Teststufen
1. Nenne die typischen **Teststufen** vom Kleinen zum Grossen (mind. 3).
2. Was ist der Unterschied zwischen **Unit-Test** und **Integrationstest**?
3. Was beschreibt die **Testpyramide**? Welche Tests sollte es viele, welche wenige geben?
4. Was ist der Unterschied zwischen **Testumgebung** und **Produktivumgebung**?

## Block 2 – Testfälle ableiten
5. Was ist eine **Äquivalenzklasse (equivalence class)** und warum spart sie Tests?
6. Was ist **Grenzwertanalyse (boundary value analysis)** und warum gerade an Grenzen testen?
7. Aus welchen Teilen besteht ein guter **Testfall** (Stichworte: Vorbedingung, Eingabe, erwartetes Resultat, …)?
8. Was ist ein **Positivtest** vs. ein **Negativtest**?

## Block 3 – Test Doubles
9. Nenne die fünf gängigen **Test Doubles** und je einen Halbsatz dazu: **Dummy, Stub, Spy, Mock, Fake**.
10. Warum benutzt man ein **Mock** statt der echten Abhängigkeit (z. B. Datenbank/Netzwerk)?

## Block 4 – TDD, Clean Code, Protokoll
11. Beschreibe den **TDD-Zyklus** in drei Worten/Phasen.
12. Wofür stehen **AAA** bzw. **Given-When-Then**?
13. Was bedeuten die Clean-Code-Prinzipien **DRY**, **KISS**, **YAGNI**, **SRP**?
14. Was sagt **Code Coverage** aus – und warum ist 100 % nicht automatisch „gut getestet"?
15. Was gehört in ein **Testprotokoll**?

---
<details>
<summary><b>Selbstkontrolle (Lösungen) – erst aufklappen, wenn du geantwortet hast!</b></summary>

1. **Unit → Integration → System → Abnahme/Akzeptanz** (oft auch E2E dazwischen). Zusätzlich quer dazu: Last/Performance, Security.
2. **Unit-Test** prüft eine kleinste Einheit (Funktion/Klasse) isoliert. **Integrationstest** prüft das **Zusammenspiel** mehrerer Einheiten/Module (z. B. Service + Datenbank).
3. **Testpyramide:** viele schnelle **Unit-Tests** (Basis), weniger **Integrationstests** (Mitte), wenige langsame **E2E/UI-Tests** (Spitze). So bleibt die Suite schnell und stabil.
4. **Testumgebung** ist eine kontrollierte Kopie zum Prüfen (Testdaten, ggf. Mocks). **Produktivumgebung** ist das echte System mit echten Nutzern/Daten – dort testet man nicht „einfach so".
5. **Äquivalenzklasse:** Eingaben, die gleich behandelt werden. Statt alle Werte zu testen, genügt **ein** Repräsentant pro Klasse → weniger, aber aussagekräftige Tests.
6. **Grenzwertanalyse:** an den Rändern einer Klasse passieren die meisten Fehler (`<` vs. `<=`, Off-by-one). Darum genau **an** der Grenze und **knapp daneben** testen.
7. **Testfall:** Vorbedingung (Arrange/Given), Eingabe/Aktion (Act/When), **erwartetes** Resultat (Assert/Then), ggf. Nachbedingung. Wichtig: vorher festlegen, was erwartet wird.
8. **Positivtest:** gültige Eingabe → erwartetes Gutverhalten. **Negativtest:** ungültige Eingabe → erwartete Fehlerbehandlung (z. B. Exception).
9. **Dummy:** nur Platzhalter, wird nie wirklich benutzt. **Stub:** liefert feste Antworten. **Spy:** Stub, der zusätzlich mitschreibt, wie er aufgerufen wurde. **Mock:** prüft erwartete Aufrufe/Interaktionen. **Fake:** echte, aber vereinfachte Implementierung (z. B. In-Memory-DB).
10. Weil der echte Dienst **langsam, unzuverlässig oder nicht verfügbar** ist. Ein Mock macht Tests **schnell, deterministisch, unabhängig** und erlaubt das gezielte Erzeugen von Sonderfällen.
11. **Red → Green → Refactor** (Test schreiben/scheitern, minimal grün machen, aufräumen).
12. **Arrange-Act-Assert** bzw. **Given-When-Then** – ein klarer Drei-Schritt-Aufbau eines Tests (vorbereiten, ausführen, prüfen).
13. **DRY** = Don't Repeat Yourself (keine Duplikate). **KISS** = Keep It Simple. **YAGNI** = You Aren't Gonna Need It (nichts auf Vorrat bauen). **SRP** = Single Responsibility Principle (eine Verantwortung pro Einheit).
14. **Coverage** misst, **welcher Code** beim Testlauf ausgeführt wurde (z. B. Zeilen/Zweige). 100 % heisst nur „durchlaufen", nicht „richtig geprüft" – ohne sinnvolle Assertions sagt die Zahl wenig aus.
15. **Testprotokoll:** was getestet wurde, mit welchen Daten/Umgebung, erwartet vs. tatsächlich, Pass/Fail, Datum/Version, gefundene Mängel – nachvollziehbar und wiederholbar.
</details>
