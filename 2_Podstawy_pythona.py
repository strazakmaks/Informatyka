'''
Temat: Podstawy pythona
Cele lekcji:
Uczeń:
podaje typy danych
wykorzystuje w zapisie wyrażeń operatory arytmetyczne
nazywa zmienne i przypisuje im wartości
zna instrukcje wejścia i wyjścia

Python jest językiem zewnętrzym, interpretowanym, wysokiego poziomu.
Jest niezrozumiały dla procesora, dlatego musi być tłumaczony.
Tłymaczenie nazwyamy translacją.
Rodzaj translacji wykorzystwyany przez Pythona nazywamy interpretacją.
To oznacza, że przy każdym uruchomieniu programu, wiersze tłumaczone są na nowo.
To spowalnia działanie programu, ale jest to niezauważalne dla użytkownika.

print("Typy danych")
print("Liczby całkowite: ", 123, type(123))
print("Liczby rzeczywiste: ", 123.12, type(123.12))
print("tekst", type("tekst"))
print("dane logiczne", type(True))

print("operatory arytmetyczne, zmienne")
print(5 + 3)

zmienne:
- duża i mała litera ma znaczenie (liczba, Liczba)
- nie używamy spacji (nowaLiczba)
- nie używamy znaków specjalnych, słów kluczowych (and, or) i nazw funkcji wbudowanych
- cyfra nie może być na początku nazwy 

a = 10
b = 3
print("dodawanie", a + b)
print(f"dodawanie {a-b}")
print(f"odejmowanie {a-b}")
print(f"mnożenie {a*b}")
print(f"dzielenie z resztą{a/b}")
print(f"dzielenie całkowite {a//b}")
print(f"reszta z dzielenia {a%b}")
print(f"potęgowanie {a**b}")

input() - instrukcja wejścia
'''
#Napisz program który wczyta imię, nazwisko i wiek użytkownika i wypisze je na ekranie
imie = input("podaj imię: ")
nazwisko = input("podaj nazwisko: ")
wiek = int(input("podaj wiek: "))
print(f"witaj {imie} {nazwisko} lat {wiek}")
print("witaj", imie, nazwisko, "lat", wiek)


#Napisz prgram w którym wykonasz działania dla danych wprowadzonych z klawiatury
# a) w = b^3+5
# b) w = (4-b)/5
# c) w = (2^3+b)/3^2

b = float(input("podaj b: "))
w = b**3 + 5
print(f"w = {w}")
w = (4-b)/5
print(f"w = {w}")
w = (2**3 + b)/3**2
print(f"w = {w}")
