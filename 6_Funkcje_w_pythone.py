'''
Temat: Funkcje w pythonie
Cele lekcji:
Uczeń:
- konstruuje funkcje zwracającą i wyświetlającą z parametrem lub bez parametru

def nazwa_funkcji(parametry):
  ciało funkcji
'''
# Funkcja wyświetlająca bez parametru
def suma():
  a=int(input("Podaj a: "))
  b=int(input("Podaj b: "))
  wynik = a+b
  print(wynik)

suma()

# Funkcja wyświetlająca z parametrem
def suma1(a,b):
  wynik = a+b
  print(wynik)

suma1(4,7)

# Funkcja zwracająca z parametrem
def suma1(c,d):
  wynik = c+d
  return(wynik)

print(suma1(4,7))

def suma3(e,f):
  return(e+f)

print(suma3(4,7))

x=int(input("Podaj x: "))
y=int(input("Podaj y: "))
dodawanie=suma3(x,y)
print(dodawanie)

# ZAD. 1 Napisz funkcję która mnoży 3 liczby
def mnozenie(g,h,i):
   return(g*h*i)

print(mnozenie(1,2,3))

# ZAD. 2 Napisz funkcję która dzieli 2 liczby
def dzielenie(j,k):
  if b == 0:
    return("błąd dzielenia przez 0")
  else: 
    return(j/k)

print(dzielenie(1,2))

# ZAD. 3 Generowanie n wyrazowego ciągu
# (4,-8, 16, -32...)
def ciag(n):
  p=4
  for i in range(n):
    print(p, end=" ")
    p*=-2

ciag(10)

# (2,6,18...)
def ciag1(n):
  p=2
  for i in range(n):
     print(p, end=" ")
     p*=3

ciag1(10)

# (12,7,2)
def ciag2(n):
   p=12
   for i in range(n):
      print(p, end=" ")
      p-=5

ciag2(10)