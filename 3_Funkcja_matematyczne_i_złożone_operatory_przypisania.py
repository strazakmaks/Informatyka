'''
Temat: Funkcja matematyczne i złożone operatory przypisania.
cele lekcji:
- wykorzystuje w zapisie złożony operator
- importuje moduł math
- stosuje w praktyce funkcje matematyczne

+=, -=, *=, /=, //=, %=, **=

a=a*(b-4)
a*=b-4
'''
# ZAD. 1
# a=a*(3**3+b)
# k=k-(i*5+2)
# w=w/4+z**2
# m=m%{3-n/2}

m=float(input("Podaj m: "))
n=float(input("Podaj n: "))
m=m%(3-n/2)
m%=3-n/2
print(m)

a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
a=a*(3**3+b)
a*=3**3+b
print(a)

k=float(input("Podaj k: "))
i=float(input("Podaj i: "))
k=k-(i*5+2)
k-=i*5+2
print(k)

w=float(input("Podaj w: "))
z=float(input("Podaj z: "))
w/=4+z**2
print(w)

# sqrt()-pierwiastek

import math
print(math.sqrt(25))

from math import*
print(sqrt(49))

from math import sqrt
print(sqrt(49))

import math as  ma
print(ma.sqrt(25))

from math import sqrt as pierwiastek
print(pierwiastek(25))

# abs() - nie wymaga importu modułu math, działa dla liczb całkowitych i zmiennoprzecinkowych
# fabs() - wymaga importu math i działa na liczbach zmiennoprzecinkowych
from math import*
print(abs(-10))
print(abs(-10.2))
print(fabs(-10))
print(fabs(-10.2))

print(sin(1))
print(cos(1))
print(tan(1))

# zaokrąglanie
print(round(sin(1), 4))
print(f"{sin(1):.2f}")

print(floor(10.6))
print(ceil(10.6))

pow(x,y)
print(pow(2,3))
print(round(pi,2))

# zad
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
w=sqrt(7/(a**3+cos(b)))
print(w)

# zad
# Napisz program który oblicza średnią geometryczną dwóch liczb nieujemnych. Średnia geometryczna to pierwiastek iloczynu liczb.
# Specyfikacja:
# Dane: liczby rzeczywiste a,b>=0
# Wynik: średnia geometryczna: sg - liczba rzeczywista >=0

a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
sg=sqrt(a*b)
print(sg)
