'''
Temat: Algorytm Euklidesa
Cele lekcji:
Uczeń:
- konstruuje algorytm Euklidesa czyli wyznaczania NWD 2 liczb naturalnych z wykorzystaniem metody wyznaczania reszty z dzielenia i metody odejmowania
- konstruuje algortym NWW 2 liczb naturalnych wykorzystujących funkcje NWD

NWD(5,15) = 5 
a      b  = wynik    reszta
5   :  15 = 0        5
15  :  5  = 3        0
5   :  0


NWD(116,324) = 4
a      b  = wynik    reszta
116 :  324 = 0       116
324 :  116 = 2       92
116 :  92  = 1       24
92  :  24  = 3       20
24  :  20  = 1       4
20  :  4   = 5       0
4   :  0 

'''
def NWD (a,b):
  while  b>0:
    reszta = a%b
    a = b
    b = reszta
  return a
print(NWD(116,324))

def NWD1 (a,b):
  while b>0:
    a,b=b,a%b
  return a
print(NWD1(116,324))
'''Metoda z odejmowaniem
NWD(5,15)
porófnanie   a  b
b>a         5   15-5=10
b>a         5   10-5=10
a=b

porófnanie  a           b
b>a         116         324-116=208
b>a         116         208-116=92
a>b         116-92=24   92
b>a         24          92-24=68
b>a         24          68-24=44
b>a         24          44-24=20
a>b         24-20=4     20
b>a         4           20-4=16
b>a         4           16-4=12
b>a         4           12-4=8
b>a         4           8-4=4
a=b
'''
def NWD2(a,b):
  while a!=b:
    if b>a:
      b-=a
    else:
      a-=b
  return a
print(NWD2(116,324))

def NWW(a,b):
  return (a*b)//NWD(a,b)
print(NWW(116,324))

licznik=3
mianownik=6
z=NWW(3,6)
skrl=licznik//z
skrm=mianownik//z
print(f"{licznik}/{mianownik} = {skrl}/{skrm}")

# ZAD. 1 Napisz funkcję dodawania ułamków zwykłych. Wynikiem funkcji ma być ułamek przedstawiony w najprostszej postaci. Nie zawsze bedzie możliowść wyciągniecia całości z ułamka. Wykorzytaj NWW do skrócenia ułamków, oraz NWD do wyciągnięcia całości z ułamka.

licznik1 = int(input("Podaj pierwszy licznik: "))
mianownik1 = int(input("Podaj pierwszy mianownik: "))
licznik2 = int(input("Podaj drugi licznik: "))
mianownik2 = int(input("Podaj drugi mianownik: "))

def NWW(a,b):
  return (a*b)//NWD(a,b)
print(NWW(licznik1,mianownik1))