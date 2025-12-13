'''
Temat: Etapy rozwiązywania problemów za pomocą komputera

Cele lekcji
Uczeń:
- wyjaśnia pojęcie algorytmu
- omawia etapy rozwiązywania algorytmów

Alogrytm - to szczegółowa instrukcja rozwiązania zadania w skończonej liczbie kroków

Etapy:
1. Sformułowanie treści zadania
2. Okreslenie danych wejściowych
3. Określenie danych wyjściowych
2+3 - specyfikacja (zmienne, typy danych, warunki)
4. Wybór metody rozwiązania
5. Prezentowanie algorytmu
- lista kroków
- schemat blokowy
- pseudokod
- język programowania
6. Testowanie algorytmu
7. Analiza algorytmu: określenie złożoności obliczeniowej: czasowej i pamięciowej, błędy zaokrągleń

ZAD. 1 Skonstruuj algorytm który sprawdza czy liczba podana przez uż

Specyfikacja:
Dane: liczba - dowolna liczba rzeczywista
Wynik: komunikat infomujący "liczba dodatnia" lub "liczba ujemna"
- lista kroków
krok 1: pobierz liczbę: liczba
krok 2: jeśli liczba >= 0 to
  - wypisz "liczba dodatnia"
krok 3: w przeciwnym razie
  - wypisz "liczba ujemna"

Pseudokod:
wprowaź: liczba
Jeżeli liczba >= 0 
  wypisz "liczba dodatnia"
w przeciwnym razie
  wypisz "liczba ujemna"


ZAD. 2 Napisz program obliczający średnią arytmetyczną 3 liczb rzeczywistych
Specyfikacja:
Dane: a, b, c - dowolne liczby rzeczywiste
Wynik: średnia arytmetyczna liczb: avg - liczba rzeczywista
Lista kroków:
krok 1: pobierz liczby: a, b, c
krok 2: oblicz sumę liczb: suma = a + b + c ( :=, <-)
krok 3: podziel sumę przez 3: avg:= suma / 3
krok 4: wypisz avg
Pseudokod:
wprowadź: a
wprowadź: b
wprowadź: c
suma := a + b + c
avg := suma / 3
wypisz: avg
Shemat blokowy:
/zdj/zadanie2.png

ZAD. 3 Napisz program sprawdzający czy podana liczba jest parzysta
Specyfikacja:
Dane: x - dowolna liczba całkowita
Wynik: komunikat informujący "liczba parzysta" lub "liczba nieparzysta"
Lista kroków:
krok 1: wprowadź liczbę: x
krok 2: jeżeli x mod 2 = 0 to
  - wypisz "liczba parzysta"
krok 3: jeżeli x mod 2 <> 0 to (w przeciwnym razie)
  - wypisz "liczba nieparzysta"
Pseudokod:
wprowadź: x
jeżeli x mod 2 = 0 to
  wypisz "liczba parzysta"
w przeciwnym razie
  wypisz "liczba nieparzysta"


ZAD. 4 Na początku rower kosztuje pełną kwotę pieniędzy - cena1. Po podwyżkach cena wzrosła - cena2. Oblicz o ile procent wzrosła cena roweru.
Specyfikacja:
Dane: cena1 > 0, cena2 > 0 - liczby rzeczywiste
Wynik: procent - liczba rzeczywista
Lista kroków:
krok 1: wprowadź ceny: cena1, cena2
krok 2: oblicz różnicę cen: różnica = cena2 - cena1
krok 3: oblicz procent wzrostu: procent = różnica / cena1 * 100
krok 4: wypisz procent
Pseudokod:

ZAD. 5 Skonstruuj algorytm rozwiązujący równanie liniowe ax + b = 0
Specyfikacja:
Dane: a, b - dowolne liczby rzeczywiste
Wynik: pierwistek równania liniowego x - liczba rzeczywista lub komunikaty "równanie tożsamościowe", "równanie sprzeczne"
Lista kroków:
krok 1: wprowadź: a, b
krok 2: jeżeli a !=0 to przejdź do korku 2.1 w przeciwnym razie przejdz do kroku 3
  krok 2.1: zmiennej x przypisz -b/a  x:= -b/a
  krok 2.2: wypisz x
krok 3: jeżeli b = 0 to przejdź do kroku 3.1 w przeciwnym razie przejdź do kroku 4
  krok 3.1: wypisz "równanie tożsamościowe"
krok 4: wypisz "równanie sprzeczne"
Shemat blokowy:
/zdj/zadanie5.png
Pseudokod:
wprowadź: a
wprowadź: b
jeżeli a!=0 to
  x:= -b/a
  wypisz x
w przeciwnym razie
  jeżeli b=0 to
    wypisz "równanie tożsamościowe"
  w przeciwnym razie
    wypisz "równanie sprzeczne"

ZAD. 6 Napisz algorytm wyznaczjacy wartość bezwględeną liczby z
Dane: z - liczba rzeczywista
Wynik: wartość bezwzględna liczby z war: liczba rzeczywista >= 0
Lista kroków
krok 1: wprowadź: z
krok 2: jeżeli z >= 0 to przejdź do kroku 2.1 w przeciwnym razie przejdź do kroku 3
  krok 2.1: do zmiennej war przypisz z: war := z
  krok 2.2: wypisz war
krok 3: do zmiennej war przypisz -z: war := z*(-1)
krok 4: wypisz war
Pseudokod:
wprowadź: z
jeżeli z >= 0 to
  war := z
  wypisz war
w przeciwnym razie
  war := z*(-1)
  wypisz war
'''
