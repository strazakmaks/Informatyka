'''
Temat: Instrukcje warunkowe w Pythonie
Cele lekcji:
Uczeń:
- realizuje algorytm z wieloma warunkami
- stosuje operatory relacyjne i logiczne w zapisie wyrażeń

operatory relacyjne:
> - większe
< - mniejsze
>= - większe lub równe
<= - mniejsze lub równe
== - równe
!= - różne

operatory logiczne:
and - i
or - lub
not - nie

if warunek:
  instrukcje
else:
  instrukcje
'''
#Napisz program który sprawdzi czy liczba całkowita (a) jest parzysta
a = int(input("podaj liczbę: "))
if a % 2 == 0:
   print("liczba parzysta")
else:
   print("liczba nieparzysta")

#Napisz program który sprawdzi czy podana liczba jest dodatnia, ujemna czy równa 0
a = int(input("podaj liczbę: "))
if a > 0:
   print("liczba dodatnia")
elif a < 0:
  print("liczba ujemna")
else:
  print("liczba równa 0")

#Napisz program który będzie wystawiał oceny w ZSŁ na podstawie procentowych kryteriów
p = float(input("podaj procent: "))
if p>=0 and p<=100:
  if p>=0 and p<40:
    print(1)
  elif p>=40 and p<50:
    print(2)
  elif p>=50 and p<70:
    print(3)
  elif p>=70 and p<90:
    print(4)
  elif p>=90 and p<=98:
    print(5)
  else:
    print(6)
else:
  print("błędny procent")
