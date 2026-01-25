# ZAD. 1 Napisz funkcję dodawania ułamków zwykłych. Wynikiem funkcji ma być ułamek przedstawiony w najprostszej postaci. Nie zawsze bedzie możliowść wyciągniecia całości z ułamka. Wykorzytaj NWW do skrócenia ułamków, oraz NWD do wyciągnięcia całości z ułamka.

licznik1 = int(input("Podaj pierwszy licznik: "))
mianownik1 = int(input("Podaj pierwszy mianownik: "))
licznik2 = int(input("Podaj drugi licznik: "))
mianownik2 = int(input("Podaj drugi mianownik: "))

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
liczbaCalkowita = licznik3//NWW1
licznik4 = licznik3%NWW1
print(f"{liczbaCalkowita} {licznik4}/{NWW1}")