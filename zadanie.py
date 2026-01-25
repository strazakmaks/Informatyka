# ZAD. 1 Napisz funkcję dodawania ułamków zwykłych. Wynikiem funkcji ma być ułamek przedstawiony w najprostszej postaci. Nie zawsze bedzie możliowść wyciągniecia całości z ułamka. Wykorzytaj NWW do skrócenia ułamków, oraz NWD do wyciągnięcia całości z ułamka.

licznik1 = int(input("Podaj pierwszy licznik: "))
mianownik1 = int(input("Podaj pierwszy mianownik: "))
while True:
    mianownik1 = int(input("Podaj pierwszy mianownik: "))
    if mianownik1 == 0:
        print("Mianownik nie może być zerem! Spróbuj ponownie.")
    else:
        break

licznik2 = int(input("Podaj drugi licznik: "))
mianownik2 = int(input("Podaj drugi mianownik: "))
while True:
    mianownik2 = int(input("Podaj pierwszy mianownik: "))
    if mianownik2 == 0:
        print("Mianownik nie może być zerem! Spróbuj ponownie.")
    else:
        break

def NWD (a,b):
  while b>0:
    a,b=b,a%b
  return a

def NWW(a,b):
  return (a*b)//NWD(a,b)

NWW1 = (NWW(mianownik2,mianownik1))

licznik11 = licznik1*(NWW1//mianownik1)
licznik22 = licznik2*(NWW1//mianownik2)
licznik3 = licznik11 + licznik22

NWD1 = (NWD(licznik3,NWW1))
licznik3 = licznik3//NWD1
NWW1 = NWW1//NWD1

liczbaCalkowita = licznik3//NWW1
licznik4 = licznik3%NWW1
if licznik4 == 0:
  print(f"{liczbaCalkowita}")
elif liczbaCalkowita == 0:
  print(f"{licznik4}/{NWW1}")
else:
  print(f"{liczbaCalkowita} {licznik4}/{NWW1}")