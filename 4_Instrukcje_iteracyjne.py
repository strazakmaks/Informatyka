'''Temat:Instrukcje iteracyjne
Cele lekcji:
Uczeń:
- stosuje instrukcje iteracyjną w celu automatyzacji zadania
- poprawnie zapsuje pętle for i while
- stosuje instrukcje sterujące break i continue

iteracje - powtórzenia

for i in range(start,stop-1,step):
  instrukcje'''

#ZAD. 1 Napisz program który wypisze liczby od 1 do 10
for i in range(1,11,1):
  print(i, end=" ")
print()

#ZAD. 2 Napisz program który wypisze liczby od 10 do 1
for i in range(10,0,-1):
  print(i, end=" ")
print()

#(3,7,11,15,19,23)
for i in range(3,24,4):
  print(i, end=" ")
print()

#ZAD. 3 Napisz program który wypisze liczby od 1 do 15 podzielne przez 4
for i in range(1,16):
  if i %4 != 0:
    continue
  print(i, end=" ")
print()

#(10,8,7,5,4,2)
for i in range(10,1,-1):
  if i % 3 != 0:
    print(i, end=" ")
print()

#(-4,-1,5,11,14)
for i in range(-4,15,3):
  if i == 8 or i == 2:
    continue
  print(i, end=" ")
print()


#Wyświetl liczby od 1 do 10
i = 1
while i <= 10:
  print(i, end=" ")
  i += 1
print()

#Wyświetl liczby od 10 do 1
i = 10
while i >= 1:
  print(i, end=" ")
  i -= 1
print()

#(3,7,11,15,19,23)
i=3
while i <= 23:
  print(i, end=" ")
  i += 4
print()

#(9,8,7,6,5)
i = 9
while i >= 5:
  print(i, end=" ")
  i -= 1
print()

#(1,3,9,27,81)
i = 1
while i <= 81:
  print(i, end=" ")
  i *= 3
print()

#(5,6,7,8,9,10,11,13,14)
i = 5
while i <= 14:
  if i%4 != 0:
    print(i, end=" ")
  i += 1
print()

i = 5
while i <= 14:
  if i%4 == 0:
    i += 1
    continue
  print(i, end=" ")
  i += 1
print()

#(10,8,7,5,4,2)
i = 10
while i >= 2:
  if i%3 != 0:
    print(i, end=" ")
  i -= 1
print()
  
i= 10
while i >= 2:
  if i % 3 != 0:
    i -=1 
    continue
  print(i, end=" ")
  i -= 1
print()

#(-4,-1,5,11,14)
i = -4
while i <= 14:
  if i == 8 or i == 2:
    i += 3
    continue
  print(i, end=" ")
  i += 3
print()

#<2,16> które nie są podzielne przez 3 i 5 od najmniejszej do największej
i = 2
while i <= 16:
  if i % 3 == 0 or i % 5 == 0:
    i += 1
    continue
  print(i, end=" ")
  i += 1
print()

for i in range(2,17):
  if i%3 == 0 or i%5 == 0:
    continue
  print(i, end=" ")
print()

#<8,24> które są podzielne przez 4 i 7 od największej do najmniejszej
i = 24
while i >= 8:
  if i % 4 != 0 and i % 7 != 0:
    i -= 1
    continue
  print(i, end=" ")
  i -= 1
print()

for i in range(24,7,-1):
  if i % 4 != 0 and i % 7 != 0:
    continue
  print(i, end=" ")
print()
