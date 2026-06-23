# Theorie- & Quizfragen – Modul 323 (Funktional programmieren)

*Erstellt: 2026-06-23 · Zuletzt aktualisiert: 2026-06-23*

> **So nutzt du das:** Beantworte jede Frage **aus dem Kopf**, schriftlich oder laut.
> Erst danach unten bei **Selbstkontrolle** vergleichen. Nicht vorher spicken – das Erinnern
> ist genau der Lerneffekt (active recall). Fachbegriffe stehen Deutsch **und** Englisch dabei.

## Block A – Paradigmen & Grundbegriffe
1. Was ist der Unterschied zwischen **imperativer** und **deklarativer/funktionaler** Programmierung? Nenne je 1 Satz.
2. Was ist eine **reine Funktion (pure function)**? Nenne die zwei Bedingungen.
3. Was ist ein **Seiteneffekt (side effect)**? Gib zwei Beispiele.
4. Was bedeutet **Unveränderlichkeit (immutability)** und warum ist sie in FP wichtig?
5. Was ist eine **Lambda-Expression** und wie unterscheidet sie sich von einer mit `def` definierten Funktion?

## Block B – Higher-Order, Closures, Functor
6. Was ist eine **Funktion höherer Ordnung (higher-order function)**? Nenne 2 Beispiele aus Python.
7. Was macht **`map`**, was **`filter`**, was **`reduce`** – je in einem Satz?
8. Was ist eine **Closure**? Warum „erinnert" sich die innere Funktion an Werte?
9. Was ist ein **Callback**?
10. Grob: Was ist ein **Functor** (im FP-Sinn, z. B. etwas, worauf man `map` anwenden kann)?

## Block C – Komposition & Currying
11. Was bedeutet **Funktionskomposition (function composition)**? Wenn `h = f ∘ g`, was wird zuerst ausgeführt?
12. Was ist **Currying**? (Stichwort: eine Funktion mit mehreren Argumenten → Kette von Funktionen mit je einem Argument.)

## Block D – Nebenläufigkeit & Qualität
13. Warum erleichtert **Immutability** die **Nebenläufigkeit/Parallelität (concurrency)**?
14. Nenne einen Vorteil **und** einen Nachteil des funktionalen Paradigmas.
15. Warum sind reine Funktionen **besonders einfach zu testen (Unit-Test)**?

---
<details>
<summary><b>Selbstkontrolle (Lösungen) – erst aufklappen, wenn du geantwortet hast!</b></summary>

1. **Imperativ** beschreibt Schritt für Schritt *wie* (mit Schleifen, veränderlichem Zustand). **Deklarativ/funktional** beschreibt *was* das Ergebnis sein soll (z. B. via map/filter), ohne den genauen Ablauf vorzuschreiben.
2. **Pure function:** (a) gleicher Input → immer gleicher Output (deterministisch), (b) keine Seiteneffekte.
3. **Side effect:** Veränderung von etwas ausserhalb der Funktion. Beispiele: `print()`, in eine Datei/DB schreiben, globale Variable ändern, eine übergebene Liste mutieren.
4. **Immutability:** Daten werden nach dem Erstellen nicht mehr verändert; man erzeugt neue Werte statt bestehende zu ändern. Wichtig, weil es Fehler durch unerwartete Zustandsänderungen verhindert und Code vorhersehbar macht.
5. **Lambda:** anonyme Funktion als Ausdruck, `lambda a, b: a + b`; kurz, kein Name, nur ein Ausdruck (kein `return`, keine mehreren Anweisungen). `def` kann mehrzeilig sein, hat einen Namen und `return`.
6. **HOF:** nimmt Funktionen als Argument und/oder gibt eine Funktion zurück. Beispiele: `map`, `filter`, `reduce`, `sorted(key=...)`.
7. `map` wendet eine Funktion auf **jedes** Element an. `filter` behält nur Elemente, die eine **Bedingung** erfüllen. `reduce` faltet die Liste zu **einem** Wert zusammen.
8. **Closure:** eine Funktion zusammen mit dem „eingefangenen" Umgebungs-Zustand. Die innere Funktion behält Zugriff auf Variablen der äusseren Funktion, auch nachdem diese zurückgekehrt ist.
9. **Callback:** eine Funktion, die man einer anderen übergibt, damit sie zu einem späteren Zeitpunkt/aufgerufen wird.
10. **Functor:** ein „Behälter"/Typ, auf den man eine Funktion via `map` anwenden kann, ohne den Behälter selbst zu verändern (z. B. eine Liste: `map` über die Liste).
11. **Komposition:** zwei Funktionen zu einer verketten. Bei `h = f ∘ g` bzw. `f(g(x))` wird **zuerst `g`**, dann `f` ausgeführt.
12. **Currying:** eine Funktion mit n Argumenten in eine Kette von n Funktionen mit je einem Argument umwandeln, z. B. `add(a, b)` → `add(a)(b)`.
13. Bei **Immutability** kann kein Thread Daten unter einem anderen „wegändern" – es gibt keine geteilten veränderlichen Zustände, also weniger Race Conditions und kein/kaum Sperren (Locks) nötig.
14. **Vorteil:** vorhersehbar, gut testbar, weniger Bugs durch Zustand; gut parallelisierbar. **Nachteil:** teils ungewohnt/schwerer lesbar, ggf. mehr Speicher durch neue Objekte, nicht für jedes Problem ideal.
15. Reine Funktionen brauchen **kein Setup/keinen Zustand**: Eingabe rein, Ausgabe prüfen. Keine Mocks, keine Reihenfolgeabhängigkeit → einfache, wiederholbare Unit-Tests.
</details>
