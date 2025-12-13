# Informatyka - Zbiór Zadań i Algorytmów

Repozytorium zawiera notatki, kody źródłowe oraz schematy blokowe z lekcji informatyki. Projekt jest skonfigurowany do działania w środowisku Python 3.11 (Replit).

## 📂 Zawartość Repozytorium

### 1. [Algorytmika i Etapy Rozwiązywania Problemów](./1_etapy_rozwiązywania_problemów_za_pomocą_komputera.py)
**Temat:** Teoretyczne i praktyczne podstawy tworzenia algorytmów.
* **Teoria:** Definicja algorytmu, specyfikacja (dane wejściowe/wyjściowe), 7 etapów pracy nad problemem.
* **Przykładowe algorytmy:**
    * Sprawdzanie znaku liczby (dodatnia/ujemna).
    * **Średnia arytmetyczna** (zawiera schemat blokowy: `zdj/zadanie2.png`).
    * Sprawdzanie parzystości (modulo).
    * Obliczanie podwyżki procentowej.
    * **Równanie liniowe $ax + b = 0$** (zawiera schemat blokowy: `zdj/zadanie5.png`).
    * Wartość bezwzględna.

### 2. [Podstawy Języka Python](./2_Podstawy_pythona.py)
**Temat:** Wprowadzenie do składni i typów danych.
* **Typy danych:** `int`, `float`, `str`, `bool`.
* **Operatory:** Arytmetyczne (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
* **Wejście/Wyjście:** Funkcje `print()` oraz `input()`.

### 3. [Instrukcje Warunkowe](./3_Instrukcje_warunkowe_w_Pythonie.py)
**Temat:** Sterowanie przepływem programu.
* **Składnia:** `if`, `elif`, `else`.
* **Logika:** Operatory porównania (`>`, `<`, `==`, `!=`) oraz logiczne (`and`, `or`, `not`).
* **Zadania:** Ocena pełnoletności, system oceniania (progi procentowe).

### 4. [Pętle i Iteracje](./4_Instrukcje_iteracyjne.py)
**Temat:** Powtarzanie czynności i automatyzacja.
* **Pętla `for`:** Praca z zakresem `range()`, odliczanie w górę i w dół.
* **Pętla `while`:** Wykonywanie kodu dopóki warunek jest spełniony.
* **Instrukcje sterujące:** `continue` (pomijanie) i `break` (przerywanie).
* **Zadania:** Wypisywanie ciągów liczb, filtrowanie liczb podzielnych przez $n$.

---

## 🖼️ Schematy Blokowe
W folderze `zdj/` znajdują się wizualizacje algorytmów omawianych na lekcjach:

| Zadanie | Podgląd |
| :--- | :---: |
| **Średnia arytmetyczna** | ![Zadanie 2](./zdj/zadanie2.png) |
| **Równanie liniowe** | ![Zadanie 5](./zdj/zadanie5.png) |

---

## ⚙️ Informacje Techniczne
* **Język:** Python 3.11
* **Struktura projektu:**
    * `main.py` - selektor lekji do uruchomienia aby w replit można było uruchomić konkretny plik.
    * `.replit`, `uv.lock`, `pyproject.toml` - pliki konfiguracyjne środowiska Replit i menedżera pakietów UV.